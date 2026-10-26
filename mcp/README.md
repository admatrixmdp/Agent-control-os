# Điểm nối MCP cho agent đám mây (lớp B)

## Vì sao cần

Claude Duet, OpenAI Dots, Meta Muse, Grok Bot **không có API điều khiển** và không nạp được SKILL.md từ repo. Lối vào lập trình được duy nhất của chúng là **connector / MCP**:

| Agent | Nhận MCP thế nào |
|---|---|
| Grok Bot | MCP tuỳ chỉnh — phải truy cập công khai hoặc qua tunnel |
| Claude Duet | Kế thừa connector đã nối trong app Claude |
| OpenAI Dots | Qua hệ plugin của ChatGPT |
| Meta Muse | Chưa thấy cơ chế MCP — chỉ OAuth tới app có sẵn |

Vậy repo này không "cài" skill vào agent đám mây; nó **phục vụ** tri thức cho chúng qua MQ Knowledge MCP (ý định đã có).

## Thiết kế v1 (chưa dựng)

| Tool MCP | Làm gì | Ghi chú |
|---|---|---|
| `tim_skill` | Tìm skill theo mô tả việc → trả tên, mảng, mô tả | Đọc `danh-muc/skills.yaml` |
| `doc_skill` | Trả nội dung SKILL.md + danh sách references của một skill | Chỉ skill có `trang_thai: dang-dung` |
| `doc_tham_chieu` | Trả một file references | |
| `luat_mq` | Trả luật giao việc (`dieu-phoi/quy-tac-giao-viec.md` mục 2) | Agent đám mây gọi lúc bắt đầu việc |
| `ghi_cham_phien` | Ghi một dòng vào `Session_Scorecard` | Thu ngược dữ liệu chất lượng từ lớp B |

Chỉ đọc + một tool ghi có phạm vi hẹp. Không có tool ghi vào repo.

## Bài học từ pstack

pstack phát cho ChatGPT qua MCP server **chỉ 3 tool đọc**; các playbook cần tạo subagent (swarm, arena, interrogate) **mất chức năng** qua MCP. → Skill MQ phát qua MCP phải tự đủ trong một lượt; skill cần nhiều agent song song chỉ chạy ở lớp A.

## Rủi ro

- MCP công khai = tri thức nội bộ ra internet. Cần xác thực (token theo người dùng) và chỉ phát skill không chứa dữ liệu khách.
- Grok Bot: nhiều Bot dùng chung phiên đăng nhập → token MCP cấp cho một Bot là cấp cho cả tài khoản.

## Bước tiếp

1. Chốt skill nào được phát (cột `phat_mcp` sẽ thêm vào `danh-muc/skills.yaml`).
2. Dựng thử với một agent đám mây Quân đã có quyền dùng.
