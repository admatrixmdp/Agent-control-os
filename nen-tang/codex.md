# OpenAI Codex (CLI / app)

| Mục | Nội dung |
|---|---|
| Lớp | A |
| Lối vào tri thức | Skill chuẩn SKILL.md: `.agents/skills/` (repo), `~/.agents/skills/` hoặc `~/.codex/skills/` (cá nhân); `AGENTS.md`; manifest `.codex-plugin/` |
| Lối vào quy tắc | Sandbox + mức phê duyệt; luật trong AGENTS.md |
| Bộ nhớ | AGENTS.md; không có bộ nhớ dài hạn riêng ngoài file |
| Lịch | Codex Automations (khi ra mắt chỉ chạy khi máy bật; bản đám mây được hứa — kiểm lại) |
| Đầu ra & trace | Log phiên; `codex exec` cho chạy lặp lại được |
| Giới hạn cứng | Danh mục skill vượt ngân sách ngữ cảnh thì mô tả bị cắt |
| Nên giao | Viết code, script, sửa nhiều file theo mẫu; chạy cùng bộ eval để kiểm skill có chạy tốt trên GPT không |
| Không giao | Quyết định nghiệp vụ không có tiêu chí kiểm |
| Eval | Có thể chạy cùng file YAML: một adapter gọi `codex exec` thay cho Claude API (chưa viết, xem `may-cham/README.md` mục Mở rộng) |

Nguồn: OpenAI "Testing Agent Skills Systematically with Evals"; Simon Willison về Codex app (2/2026). Xác nhận: 2026-10-26.
