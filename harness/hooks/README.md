# Hooks

Đặc tả hành vi, độc lập nền tảng. Cài trên nền tảng lõi bằng cơ chế hook của nền tảng đó.

## Tên sự kiện chuẩn

Dùng đúng tên theo chuẩn Claude Code mà các harness lớn đang chép nhau (arXiv 2609.00006, mục 14.5): `session_start`, `user_prompt_submit`, `pre_tool_use`, `post_tool_use`, `stop`, `subagent_start`, `subagent_stop`.

## Hook đã đặc tả

| Hook | Sự kiện | Chặn được? | Mục đích |
|---|---|---|---|
| `chan-ghi-chua-duyet.md` | `pre_tool_use` | Có | Công cụ ghi mức "hỏi trước" phải có mã duyệt |
| `kiem-chung-truoc-khi-dung.md` | `stop` | Có | Không báo xong khi đã ghi mà chưa đọc lại |
| `lap-vo-han.md` | `pre_tool_use` | Có | 3 lệnh giống hệt liên tiếp → hỏi người |

## Luật chung

- **Lỗi thì chặn** (đóng khi lỗi) với mọi hook chặn được.
- Mỗi lần hook chặn phải ghi nhật ký: hook, lý do, phiên, công cụ.
- Thêm hook mới: qua `bot-truoc-khi-them` (`AGENTS.md` mục 4), kèm đề kiểm thử trong `../danh-gia/`.
