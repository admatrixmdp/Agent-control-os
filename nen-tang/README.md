# Hồ sơ điều khiển nền tảng agent

## Ba lớp

| Lớp | Nền tảng | Cách đưa tri thức vào | Chấm eval tự động? | Trace đọc bằng máy? |
|---|---|---|---|---|
| **A. Agent chạy trên repo** | `claude-code`, `codex`, `goclaw`, `goso` | SKILL.md, AGENTS.md, file agent | **Có** (`may-cham`) | Có |
| **B. Agent đám mây chạy nền** | `claude-duet`, `openai-dots`, `meta-muse`, `grok-bot` | Bộ nhớ dạng văn bản, quy tắc hành động, connector / **MCP** | Không (không có API điều khiển) | Không / hạn chế |
| **C. Mô hình qua API** | Claude API, OpenAI API, xAI API | Prompt hệ thống, định nghĩa tool | Có | Có |

**Hệ quả:** skill trong các repo `*-os` chỉ "cài" trực tiếp được vào lớp A. Lớp B nhận tri thức qua MCP (`mcp/README.md`) hoặc dán luật (`dieu-phoi/quy-tac-giao-viec.md` mục 2). Chất lượng lớp B chỉ đo được bằng chấm tay `vong-lap/cham-phien`.

## Mẫu hồ sơ

Mỗi file `<ten>.md` có các mục: Định danh · Lối vào tri thức · Lối vào quy tắc · Bộ nhớ · Lịch · Đầu ra & trace · Giới hạn cứng · Chi phí · Nên giao · Không giao · Nguồn & ngày xác nhận.

Thông tin lớp B thay đổi nhanh (sản phẩm ra mắt 8–10/2026). **Mỗi hồ sơ ghi ngày xác nhận; quá 60 ngày thì kiểm lại trước khi dựa vào.**

## Danh sách

| Hồ sơ | Lớp | Trạng thái dùng của MQ |
|---|---|---|
| [claude-code](claude-code.md) | A | Đang dùng |
| [codex](codex.md) | A | Đang dùng |
| [goclaw](goclaw.md) | A | Đang dùng (hạ tầng agent nội bộ) |
| [goso](goso.md) | A | Đang xây lại |
| [claude-duet](claude-duet.md) | B | Chưa xác nhận có quyền dùng |
| [openai-dots](openai-dots.md) | B | Chưa xác nhận có quyền dùng |
| [meta-muse](meta-muse.md) | B | Chưa xác nhận có quyền dùng |
| [grok-bot](grok-bot.md) | B | Chưa xác nhận có quyền dùng |
