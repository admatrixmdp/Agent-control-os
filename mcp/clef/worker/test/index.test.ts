import { test } from "node:test";
import assert from "node:assert/strict";
import { handle, maskText, type Env } from "../src/index.ts";

console.log = () => {}; // tắt log JSON khi chạy test; test che dữ liệu tự bắt log riêng
const KEYS = { CALLER_SECRET_CLAUDE: "test-secret-a", CALLER_SECRET_GOCLAW: "test-secret-b", CALLER_SECRET_GOSO: "test-secret-c" };

// Mock Workers AI: chọn phương án ĐẦU TIÊN (thiên vị vị trí) để thử tính ổn định khi xáo phương án.
function mockEnv(extra: Partial<Env> = {}) {
  const sent: any[] = [];
  const AI = {
    async run(model: string, body: any) {
      sent.push({ model, body });
      const answers: Record<string, unknown> = {};
      for (const [id, q] of Object.entries<any>(body.questions)) {
        if (q.type === "noul") answers[id] = { type: "noul", noul: 0.9 };
        if (q.type === "score") answers[id] = { type: "score", score: 1.5, confidence: 0.8, probabilities: {} };
        if (q.type === "choice") answers[id] = { type: "choice", choice: Object.keys(q.criteria)[0], confidence: 0.7, probabilities: {} };
      }
      return { model: "clef", answers, usage: { input_tokens: 100, output_tokens: 5 } };
    },
  };
  return { env: { AI, RATE_PER_MIN: "1000", CLEF_TIMEOUT_MS: "200", ...KEYS, ...extra } as Env, sent };
}

const QS = {
  co_can_nguoi: { type: "noul", instructions: "Tin nhắn có cần người thật trả lời không?" },
  muc_gap: { type: "score", instructions: "Mức gấp?", criteria: ["thấp", "vừa", "cao"] },
  kenh: { type: "choice", instructions: "Chuyển cho ai?", criteria: { sale: "bán hàng", ke_toan: "hoá đơn", bo_qua: "rác" } },
};

function req(body: unknown, caller = "claude", secret = "test-secret-a") {
  const h: Record<string, string> = { "content-type": "application/json", "x-caller": caller };
  if (secret) h.authorization = `Bearer ${secret}`;
  return new Request("https://clef.example.com/v1/systemone", { method: "POST", headers: h, body: JSON.stringify(body) });
}
const body = (extra: object = {}) => ({ model: "clef", context_version: "ctx-1", qset_version: "q-1", state: { tenant: "tenant-demo" }, questions: QS, ...extra });

test("không có secret -> 401; secret của bên gọi khác -> 401", async () => {
  const { env, sent } = mockEnv();
  assert.equal((await handle(req(body(), "claude", ""), env)).status, 401);
  assert.equal((await handle(req(body(), "claude", "test-secret-b"), env)).status, 401);
  assert.equal((await handle(req(body(), "la-hoac", "test-secret-a"), env)).status, 401);
  assert.equal(sent.length, 0);
  assert.equal((await handle(req(body(), "goclaw", "test-secret-b"), env)).status, 200);
});

test("đủ 3 loại câu hỏi trả đúng kiểu", async () => {
  const { env, sent } = mockEnv();
  const r = await (await handle(req(body()), env)).json();
  assert.equal(r.fallback, false);
  assert.equal(r.answers.co_can_nguoi.type, "noul");
  assert.equal(r.answers.muc_gap.type, "score");
  assert.equal(r.answers.kenh.type, "choice");
  assert.equal(sent[0].model, "@cf/cloudflare/clef");
  assert.equal(sent[0].body.model, "clef");
});

test("lô 65 câu bị từ chối trước khi gửi", async () => {
  const { env, sent } = mockEnv();
  const qs = Object.fromEntries(Array.from({ length: 65 }, (_, i) => [`q${i}`, { type: "noul", instructions: "x?" }]));
  assert.equal((await handle(req(body({ questions: qs })), env)).status, 400);
  assert.equal(sent.length, 0);
});

test("SĐT/tên giả bị che trong payload gửi Clef; log không chứa văn bản thô", async () => {
  const { env, sent } = mockEnv();
  // SĐT giả ghép lúc chạy để máy quét bí mật không coi file test là rò rỉ.
  const sdt1 = ["0912", "345", "678"].join(" "), sdt2 = "+84 " + "9876" + "54321";
  const raw = `Chị Lan Anh gọi ${sdt1}, anh Nguyễn Văn An để lại ${sdt2}, mail a@example.com`;
  const logs: string[] = [];
  const orig = console.log; console.log = (s: string) => logs.push(s);
  try { await handle(req(body({ state: { tin: raw } })), env); } finally { console.log = orig; }
  const out = JSON.stringify(sent[0].body);
  for (const s of ["0912", "987654321", "Lan Anh", "Nguyễn Văn An", "a@example.com"]) {
    assert.ok(!out.includes(s), `lọt ${s}`);
    assert.ok(!logs.join("\n").includes(s), `log lọt ${s}`);
  }
  assert.match(out, /\[SDT\].*\[TEN\]/);
  const line = JSON.parse(logs[0]);
  assert.deepEqual(Object.keys(line).sort(), ["caller", "context_version", "cost", "evt", "hash", "model", "qset_version", "result", "tokens"]);
  assert.equal(maskText(`gọi ${"035" + "6789012"} nhé`), "gọi [SDT] nhé");
});

test("mất mạng / timeout -> fallback=true, không chặn", async () => {
  const { env } = mockEnv({ AI: { run: async () => { throw new TypeError("network down"); } } });
  const r = await (await handle(req(body()), env)).json();
  assert.equal(r.fallback, true);
  const slow = mockEnv({ AI: { run: () => new Promise(() => {}) } }).env;
  assert.equal((await (await handle(req(body()), slow)).json()).reason, "timeout");
});

test("xáo thứ tự phương án choice -> cùng quyết định, cùng cache key", async () => {
  const { env, sent } = mockEnv();
  const xao = { ...QS, kenh: { ...QS.kenh, criteria: { bo_qua: "rác", sale: "bán hàng", ke_toan: "hoá đơn" } } };
  const a = await (await handle(req(body()), env)).json();
  const b = await (await handle(req(body({ questions: xao })), env)).json();
  assert.equal(a.answers.kenh.choice, b.answers.kenh.choice);
  assert.equal(JSON.stringify(sent[0].body), JSON.stringify(sent[1].body));
});

test("chọn model theo tên, log model thật; model lạ -> 400", async () => {
  const { env, sent } = mockEnv();
  await handle(req(body({ model: "clef-flash" })), env);
  assert.equal(sent[0].model, "@cf/cloudflare/clef-flash");
  assert.equal(sent[0].body.model, "clef-flash");
  assert.equal((await handle(req(body({ model: "khac" })), env)).status, 400);
});

test("cache: cùng text+ctx+qset+model không gọi lại; đổi qset thì gọi", async () => {
  const kv = new Map<string, string>();
  const { env, sent } = mockEnv({ CACHE: { get: async (k) => kv.get(k) ?? null, put: async (k, v) => void kv.set(k, v) } });
  await handle(req(body()), env);
  const r = await (await handle(req(body()), env)).json();
  assert.equal(r.cache, true);
  await handle(req(body({ qset_version: "q-2" })), env);
  assert.equal(sent.length, 2);
});

test("rate limit theo bên gọi", async () => {
  const { env } = mockEnv({ RATE_PER_MIN: "1", CALLER_SECRET_GOSO: "test-secret-c" });
  assert.equal((await handle(req(body(), "goso", "test-secret-c"), env)).status, 200);
  assert.equal((await handle(req(body(), "goso", "test-secret-c"), env)).status, 429);
});
