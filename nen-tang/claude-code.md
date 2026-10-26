# Claude Code (gồm phiên Claude có shell / scheduled task)

| Mục | Nội dung |
|---|---|
| Lớp | A |
| Lối vào tri thức | Skill chuẩn SKILL.md (plugin qua `.claude-plugin/marketplace.json`), `CLAUDE.md`, `AGENTS.md`, MCP |
| Lối vào quy tắc | Chế độ quyền công cụ, hook (PreToolUse/PostToolUse), luật trong CLAUDE.md |
| Bộ nhớ | CLAUDE.md theo repo; bộ nhớ tài khoản Claude |
| Lịch | Scheduled task (mỗi lần chạy là phiên mới) |
| Đầu ra & trace | Transcript phiên; commit/PR; file. Hook cuối phiên có thể ghi dòng chấm điểm |
| Giới hạn cứng | Ngân sách ngữ cảnh: danh mục skill quá lớn thì mô tả bị cắt → định tuyến sai |
| Chi phí | Theo gói / API |
| Nên giao | Sửa repo skill, chạy `may-cham`, phân tích dữ liệu qua MCP, đối chiếu skill, mở PR |
| Không giao | Việc cần chạy liên tục nhiều giờ không người xem mà không có điều kiện dừng |
| Eval | `python may-cham/cham.py cham ...` (dùng Claude API) |
| Ghi chú | Lệnh `claude plugin eval` (cấu hình `experimental.evals`) là cơ chế thử nghiệm; `may-cham` không phụ thuộc vào nó |

Xác nhận: 2026-10-26.
