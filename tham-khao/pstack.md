# pstack (Lauren Tan) — đã xét, ADAPT có chọn lọc

**Là gì:** bộ skill, nguyên tắc, playbook, subagent cho agent lập trình. Gốc trên Cursor; bản port `ahmedbenaw/pstack` chạy Claude Code / Codex / ChatGPT (MCP). Giấy phép MIT. 23 playbook, 23 nguyên tắc, 47 mục trên marketplace Cursor.

**Tầng tri thức:** thu thập, chưa kiểm chứng. Con số "1.000 PR", "20+ Bot" do tác giả tự công bố.

## Đã lấy vào repo này

| Thành phần pstack | Lấy gì | Ở đâu |
|---|---|---|
| 23 nguyên tắc dạng skill nhỏ | **Cách đóng gói** (không chép nội dung) | `dieu-phoi/nguyen-tac/` |
| Nguyên tắc "xác minh là hạ tầng" | Ý tưởng | `nguyen-tac/xac-minh-truoc-khi-bao-xong` |
| "Chi tiêu tính toán đúng chỗ" | Ý tưởng | `nguyen-tac/chi-dung-cho` |
| "Subtract before you add" | Ý tưởng, ghép với màng lọc Hermes | `nguyen-tac/bot-truoc-khi-them` |
| `/poteto-mode` (việc → playbook → skill) | Ý tưởng định tuyến | `dieu-phoi/bang-dinh-tuyen.md` |
| `/interrogate` (nhiều mô hình rà) | Giám khảo khác mô hình chạy | `may-cham/` |
| `docs/nativization-map.md` (chuyển đổi giữa nền tảng) | Cách làm | `nen-tang/` |
| MCP 3 tool đọc cho ChatGPT | Bài học giới hạn | `mcp/README.md` |
| Grok Bot "Chief of Staff" điều phối Bot theo mảng | Ý tưởng | `nen-tang/grok-bot.md` |

## Chưa lấy, có thể xét sau

| Thành phần | Khi nào xét |
|---|---|
| `create-verification-skill` / `maintain-verification-skill` | Khi viết công cụ sinh eval YAML tự động |
| `/automate-me` (rút thói quen người dùng thành skill) | Khi nâng cấp `cham-phien` và `Who_am_i_user` |
| `/arena` | Khi ghép với flow Arena Agent đang có |

## Bỏ

Playbook viết code (`tdd`, `typescript-best-practices`, perf, refactor, visual parity) — nếu cần thì cài riêng ở repo code. `benny` (không chạy). `/unslop`, `/bro` (đã có `viet-tu-nhien`).

## Cảnh báo

Thử nghiệm độc lập: tác vụ mất ~1 giờ so với 30 phút khi không dùng pstack. Quy trình nặng chỉ cho việc nặng.

## Nguồn
- https://www.theneuron.ai/explainer-articles/pstack-explained-lauren-tans-system-for-trustworthy-ai-agents/
- https://github.com/ahmedbenaw/pstack
- https://flaviocopes.com/pstack/
- https://aiidelist.com/blog/lauren-tan-grok-bot-pstack-workflow
