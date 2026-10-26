# Agent-control-os

**Lớp điều phối agent và skill của hệ MQ.** Một chỗ duy nhất để: chọn nền tảng agent cho từng loại việc, điều khiển các agent nền tảng (Claude Code, Codex, GoClaw, Goso, Claude Duet, OpenAI Dots, Meta Muse, Grok Bot), chấm eval cho mọi repo skill, và đối chiếu skill mới với skill đã có.

Repo này **không chứa skill nghiệp vụ**. Skill nghiệp vụ nằm ở các repo `*-os`; repo này giữ sổ đăng ký của chúng.

## Bản đồ

| Thư mục | Chứa gì | Đọc khi |
|---|---|---|
| `AGENTS.md` | Luật tối cao cho mọi agent | Luôn đọc trước |
| `dieu-phoi/` | Bảng định tuyến việc → nền tảng → skill; luật giao việc; nguyên tắc dạng skill | Chọn ai làm, làm theo luật nào |
| `nen-tang/` | Hồ sơ điều khiển từng nền tảng (3 lớp A/B/C) | Giao việc cho một nền tảng cụ thể |
| `danh-muc/` | `skills.yaml` — sổ đăng ký toàn bộ skill trong hệ | Tìm skill, kiểm trùng, xem độ phủ eval |
| `may-cham/` | Máy chấm eval dùng chung + kiểm thử | Sửa skill, gắn CI, chạy vòng cải tiến |
| `vong-lap/` | Vòng A (thực thi) và vòng B (tiến hoá); skill `cham-phien`; thiết kế bảng LarkBase | Sau mỗi phiên, cron ban đêm |
| `doi-chieu/` | Quy trình đối chiếu skill bên ngoài (290 skill) với skill nội bộ | Có skill mới cần xét |
| `mcp/` | Thiết kế điểm nối tới MQ Knowledge MCP cho agent đám mây | Đưa tri thức vào Duet, Dots, Muse, Grok Bot |
| `tham-khao/` | Ghi chú tri thức bên ngoài đã xét (vd pstack) | Tra nguồn gốc một ý tưởng |
| `DECISIONS.md` | Nhật ký quyết định kiến trúc | Trước khi đề xuất thay đổi lớn |

## Chạy nhanh máy chấm

```bash
pip install pyyaml
# Kiểm định dạng eval của một repo skill (không cần API key)
python may-cham/cham.py kiem --repo ../sale-suite-os
# Chấm thật một skill, so có skill / không skill (cần ANTHROPIC_API_KEY)
python may-cham/cham.py cham --repo ../sale-suite-os --skill 09-chot-sale --so-sanh
# Kiểm thử chính máy chấm
python may-cham/tests/kiem_thu.py
```

## Trạng thái (2026-10-26)

| Hạng mục | Trạng thái |
|---|---|
| Luật, định tuyến, hồ sơ 8 nền tảng | v1 |
| Máy chấm `kiem` + `cham` | v1, kiểm thử 7/7 đạt; chưa chạy thật với API |
| Sổ đăng ký skill | v1 |
| Eval trong các repo skill | 12 repo có eval; 7 PR `evals-v1` đang chờ duyệt |
| Vòng B tự động (cron) | Thiết kế, chưa dựng |
| Đối chiếu 290 skill | Quy trình xong; chờ nguồn 290 skill |
| MCP cho agent đám mây | Thiết kế, chưa dựng |
