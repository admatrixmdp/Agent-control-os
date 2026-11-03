// Cổng quyết định Clef: POST /v1/systemone -> Workers AI (env.AI.run). Worker không giữ token Cloudflare.
export type QType = "noul" | "choice" | "score";
export interface Question { type: QType; instructions: string; criteria?: unknown }
export interface Env {
  AI: { run(model: string, body: unknown, opts?: unknown): Promise<any> };
  CACHE?: { get(k: string): Promise<string | null>; put(k: string, v: string, o?: unknown): Promise<void> };
  RATE_LIMITER?: { limit(o: { key: string }): Promise<{ success: boolean }> };
  [k: string]: unknown; // ALLOWED_CALLERS, CALLER_SECRET_<TEN>, CLEF_TIMEOUT_MS, RATE_PER_MIN, COST_PER_M_TOKENS, AI_GATEWAY_ID
}

/** Bên gọi hợp lệ lấy từ var ALLOWED_CALLERS ("caller-a,caller-b"); secret: CALLER_SECRET_CALLER_A, ... */
export const callers = (env: Env) => String(env.ALLOWED_CALLERS ?? "").split(",").map((x) => x.trim()).filter(Boolean);
export const secretName = (caller: string) => `CALLER_SECRET_${caller.toUpperCase().replace(/[^A-Z0-9]/g, "_")}`;
export const MAX_QUESTIONS = 64;
// Mỗi model một đích riêng. clef-flash từng trả 422 khi thử: giữ cấu hình nhưng mặc định là clef.
export const MODELS: Record<string, { id: string; body_model: string }> = {
  clef: { id: "@cf/cloudflare/clef", body_model: "clef" },
  "clef-flash": { id: "@cf/cloudflare/clef-flash", body_model: "clef-flash" },
};

const PHONE = /(?<![\w.])(?:\+?84[ .-]?|0)[35789](?:[ .-]?\d){8}(?!\w)/g;
const EMAIL = /[\w.+-]+@[\w-]+(?:\.[\w-]+)+/g;
const TEN = "\\p{Lu}[\\p{Ll}\\p{M}]*"; // \\p{M}: chịu được chữ Việt dạng NFD
const HO = "Nguyễn|Trần|Lê|Phạm|Hoàng|Huỳnh|Phan|Vũ|Võ|Đặng|Bùi|Đỗ|Hồ|Ngô|Dương|Lý";
const FULLNAME = new RegExp(`(?<!\\p{L})(?:${HO})(?:\\s+${TEN}){1,3}(?!\\p{L})`, "gu"); // không cờ `i`
// Không dùng cờ `i`: với `i`, \p{Lu} khớp cả chữ thường và che nhầm nội dung ("em muốn hủy" -> "em [TEN]").
// Từ xưng hô nhận chữ hoa đầu câu bằng lớp ký tự; tên phía sau bắt buộc viết hoa.
const XUNG_HO = new RegExp(`(?<!\\p{L})([Aa]nh|[Cc]hị|[Ee]m|[Cc]ô|[Cc]hú|[Bb]ác|[Ôô]ng|[Bb]à|[Bb]ạn|[Kk]hách|[Tt]ên)\\s+${TEN}(?:\\s+${TEN}){0,2}(?!\\p{L})`, "gu");

export function maskText(s: string): string {
  return s.replace(PHONE, "[SDT]").replace(EMAIL, "[EMAIL]").replace(FULLNAME, "[TEN]")
    .replace(XUNG_HO, (_m, x) => `${x} [TEN]`);
}

export function maskDeep(v: unknown): unknown {
  if (typeof v === "string") return maskText(v);
  if (Array.isArray(v)) return v.map(maskDeep);
  if (v && typeof v === "object") return Object.fromEntries(Object.entries(v).map(([k, x]) => [k, maskDeep(x)]));
  return v;
}

/** JSON có khoá sắp xếp: thứ tự phương án choice không đổi payload, cache key hay quyết định. */
export function stable(v: unknown): string {
  if (Array.isArray(v)) return `[${v.map(stable).join(",")}]`;
  if (v && typeof v === "object")
    return `{${Object.keys(v).sort().map((k) => `${JSON.stringify(k)}:${stable((v as any)[k])}`).join(",")}}`;
  return JSON.stringify(v);
}

export async function sha256(s: string): Promise<string> {
  const d = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
  return [...new Uint8Array(d)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

function sameSecret(a: string, b: string): boolean {
  if (!a || !b || a.length !== b.length) return false;
  let x = 0;
  for (let i = 0; i < a.length; i++) x |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return x === 0;
}

const dem = new Map<string, { phut: number; n: number }>(); // dự phòng khi chưa gắn RATE_LIMITER
async function allow(env: Env, caller: string): Promise<boolean> {
  if (env.RATE_LIMITER) return (await env.RATE_LIMITER.limit({ key: caller })).success;
  const phut = Math.floor(Date.now() / 60000), max = Number(env.RATE_PER_MIN ?? 60);
  const c = dem.get(caller);
  if (!c || c.phut !== phut) { dem.set(caller, { phut, n: 1 }); return true; }
  return ++c.n <= max;
}

const json = (body: unknown, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { "content-type": "application/json" } });
const log = (o: Record<string, unknown>) => console.log(JSON.stringify({ evt: "clef", ...o }));

export async function handle(req: Request, env: Env): Promise<Response> {
  const url = new URL(req.url);
  if (req.method !== "POST" || url.pathname !== "/v1/systemone") return json({ error: "not_found" }, 404);
  const caller = req.headers.get("x-caller") ?? "";
  const token = (req.headers.get("authorization") ?? "").replace(/^Bearer\s+/i, "");
  const secret = String(env[secretName(caller)] ?? "");
  if (!callers(env).includes(caller) || !sameSecret(token, secret)) return json({ error: "unauthorized" }, 401);
  if (!(await allow(env, caller))) { log({ caller, rate_limited: true }); return json({ error: "rate_limited" }, 429); }

  let b: any;
  try { b = await req.json(); } catch { return json({ error: "bad_json" }, 400); }
  const qs: Record<string, Question> = b?.questions ?? {};
  const n = Object.keys(qs).length;
  if (n === 0 || n > MAX_QUESTIONS) return json({ error: `can 1..${MAX_QUESTIONS} cau hoi, nhan ${n}` }, 400);
  for (const [id, q] of Object.entries(qs))
    if (!["noul", "choice", "score"].includes(q?.type) || typeof q?.instructions !== "string")
      return json({ error: `cau hoi ${id} sai dinh dang` }, 400);
  const modelName = String(b.model ?? "clef");
  const m = MODELS[modelName];
  if (!m) return json({ error: `model ${modelName} khong ho tro` }, 400);
  const ctx = String(b.context_version ?? "0"), qset = String(b.qset_version ?? "0");

  const payload = JSON.parse(stable({ model: m.body_model, state: maskDeep(b.state ?? {}), questions: maskDeep(qs) }));
  const hash = await sha256(`${stable(payload)}|${ctx}|${qset}|${modelName}`);
  const base = { caller, hash, model: m.id, context_version: ctx, qset_version: qset };
  const hit = await env.CACHE?.get(hash);
  if (hit) { log({ ...base, cache: true }); return json({ ...JSON.parse(hit), cache: true, fallback: false }); }

  const ms = Number(env.CLEF_TIMEOUT_MS ?? 8000);
  const opts = env.AI_GATEWAY_ID ? { gateway: { id: String(env.AI_GATEWAY_ID) } } : undefined;
  let t: ReturnType<typeof setTimeout> | undefined;
  try {
    const r = await Promise.race([
      env.AI.run(m.id, payload, opts),
      new Promise((_, no) => { t = setTimeout(() => no(new Error("timeout")), ms); }),
    ]) as any;
    const res = r?.result ?? r;
    if (!res?.answers) throw new Error("bad_response");
    const tokens = (res.usage?.input_tokens ?? 0) + (res.usage?.output_tokens ?? 0);
    const cost = (tokens / 1e6) * Number(env.COST_PER_M_TOKENS ?? 0);
    const out = { answers: res.answers, model: res.model ?? m.id, tokens, cost };
    log({ ...base, model: out.model, result: res.answers, tokens, cost });
    await env.CACHE?.put(hash, JSON.stringify(out), { expirationTtl: 86400 });
    return json({ ...out, cache: false, fallback: false });
  } catch (e) {
    const reason = e instanceof Error ? e.message : "error";
    log({ ...base, fallback: true, reason });
    return json({ answers: null, model: m.id, fallback: true, reason }); // không chặn bên gọi
  } finally { clearTimeout(t); }
}

export default { fetch: handle };
