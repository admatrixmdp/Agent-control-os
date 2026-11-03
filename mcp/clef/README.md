# Cổng quyết định Clef

Một cổng nhỏ để các bên gọi (khai trong `ALLOWED_CALLERS`, ví dụ `caller-a`, `caller-b`) hỏi Clef những câu `noul` / `choice` / `score` trước khi đánh thức agent. **Chưa deploy.** Mọi test chạy offline với Workers AI giả.

| Phần | File | Việc |
|---|---|---|
| Worker | `worker/src/index.ts` | `POST /v1/systemone` → `env.AI.run("@cf/cloudflare/clef", body)`. Không giữ token Cloudflare. |
| Cấu hình | `worker/wrangler.toml` | Binding `AI`, `CACHE` (KV), `RATE_LIMITER`. Chỉ có placeholder, không có secret. |
| MCP | `mcp/server.py` | Tool `clef_decide` (stdio), chạy được với mcp 1.x và 2.x. |
| Lô | `batch/clef_batch.py` | Chia lô ≤64 câu, cache, trần số lần gọi, fallback. |
| Test | `worker/test/`, `tests/` | Offline toàn bộ. |

## Gọi cổng

```
POST https://clef.example.com/v1/systemone
x-caller: caller-a
authorization: Bearer <CALLER_SECRET_CALLER_A>
{"model":"clef","context_version":"ctx-1","qset_version":"q-1",
 "state":{"tenant":"tenant-demo"},
 "questions":{"kenh":{"type":"choice","instructions":"Chuyển cho ai?","criteria":{"sale":"...","bo_qua":"..."}}}}
```

Body gửi Clef theo định dạng Jev: `{model:"clef", state, questions}`. Tối đa 64 câu một lần; 65 câu bị trả 400 trước khi gọi Clef.

## Luật bắt buộc

0. **Bên gọi phải tự che dữ liệu trước khi gửi.** Lớp che trong Worker chỉ là lớp thứ hai, không thay cho bên gọi.
1. **Worker che thêm một lần.** SĐT Việt Nam, email, họ tên (họ phổ biến + từ xưng hô như "chị", "anh") đều bị thay bằng `[SDT]`, `[EMAIL]`, `[TEN]`. Che tên dựa trên heuristic, không dùng cờ `i`: tên phải viết hoa, câu thường như "em muốn hủy đơn hàng" giữ nguyên. Có thể sót tên không có họ hoặc xưng hô; bên gọi không nên gửi tên nếu không cần. Log chỉ có `caller, hash, model, context_version, qset_version, result, tokens, cost`, không bao giờ có văn bản thô.
2. **Mỗi bên gọi một secret.** Danh sách bên gọi nằm ở var `ALLOWED_CALLERS`; secret tên `CALLER_SECRET_<TEN_IN_HOA>` (vd `CALLER_SECRET_CALLER_A`), đặt bằng `wrangler secret put`. Thiếu secret hoặc dùng secret của bên khác thì trả 401. Rate limit theo tên bên gọi: dùng binding `RATE_LIMITER` nếu có, không thì dùng bộ đếm trong isolate (`RATE_PER_MIN`, chỉ để dự phòng).
3. **Cache key** = sha256(payload đã che + `context_version` + `qset_version` + model). Đổi bộ câu hỏi hoặc ngữ cảnh thì cache tự hết hiệu lực.
4. **Model theo tên**: `clef` → `@cf/cloudflare/clef`, `clef-flash` → `@cf/cloudflare/clef-flash`. Log ghi model mà Clef trả về. Lưu ý: khi thử trước đây chỉ `clef` chạy được, `clef-flash` trả 422. Mặc định vẫn là `clef`.
5. **Không chặn bên gọi.** Timeout `CLEF_TIMEOUT_MS`; lỗi mạng, timeout hay phản hồi hỏng đều trả `fallback: true` (HTTP 200), để bên gọi tự xử lý theo luật cũ.

Phương án `choice` được sắp theo khoá trước khi gửi, nên xáo thứ tự phương án không đổi payload hay cache key (test "payload ổn định"). Test này **không** đo thiên vị vị trí của Clef; việc đó làm trong bộ eval chạy thật (đổi nhãn tên phương án rồi so quyết định).

`wrangler.toml` để `workers_dev = true` cho giai đoạn thử. Chuyển sang route riêng trước khi nối dữ liệu thật.

## Chạy test

```
node --test mcp/clef/worker/test/*.test.ts         # Node >= 22.6 (type stripping)
python3 -m unittest discover -s mcp/clef/tests
```

MCP: `CLEF_GATE_URL=https://clef.example.com CLEF_CALLER=caller-a CLEF_CALLER_SECRET=... python3 mcp/clef/mcp/server.py` (cần `pip install mcp`).
