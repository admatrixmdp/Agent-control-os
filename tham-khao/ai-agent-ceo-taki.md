# "AI Agent CEO" — lộ trình 16 bước AI OS (Taki Group)

**Nguồn:** bộ slide 57 trang "AI AGENT CEO" kèm kho 510 skill, khoá "AI Business Systems" của Nguyễn Tất Kiểm (Taki Group). Quân đưa vào ngày 2026-10-26. File gốc 67 MB không đưa vào repo.
**Tầng tri thức:** thu thập, chưa kiểm chứng. Các số liệu quảng bá trong slide (số học viên, doanh thu case study) chưa kiểm chứng.

## Nội dung chính

| Phần | Nội dung |
|---|---|
| Mở đầu | 10 tuyên bố cho CEO "AI first"; case Cal AI, MEDVi; FPT và SaaS bị định giá lại dưới áp lực AI |
| Kiến trúc | Cấu trúc 1 AI agent (đầu vào → hiểu yêu cầu → suy luận + bộ nhớ + tri thức + tool → thực thi → đầu ra, vòng phản hồi, giám sát an toàn); multi-agent (orchestrator + agent chuyên môn + QA agent); agentic AI; "công ty AI OS" |
| Prompt | Prompt = giao thức giao việc (goal, context, constraints, evaluation); "8 bước dễ nhớ cho CEO": vai trò, việc phải làm, cần biết gì, làm cho ai, trả ra kiểu gì, luật chơi, mẫu chuẩn, chấm–sửa–lưu → prompt → template → skill → agent |
| Lộ trình | 16 bước (bảng dưới), mức trưởng thành L0–L5, triển khai 90–180 ngày |

## 16 bước so với Agent-control-os

| Bước | Ý chính | MQ đã có | Khoảng trống |
|---|---|---|---|
| 1. Enterprise DNA | Nạp chiến lược, sản phẩm, khách hàng, quy trình, quy tắc, con người, KPI, dữ liệu | `sync/Who_am_i_user.md`, `product-marketing-context`, `00-context-ban-hang` — **rời rạc theo từng plugin** | **Chưa có một hồ sơ DNA chung** mà mọi skill đọc |
| 2. Bản đồ doanh nghiệp | 8 phòng ban quanh CEO | `danh-muc/skills.yaml` theo mảng | Nhân sự, vận hành, CSKH, IT, mua hàng chưa có repo |
| 3. Inventory công việc | Liệt kê việc ngày / tuần / tháng | Chưa | Thiếu |
| 4. Ma trận chọn việc | Mức lặp lại × mức chuẩn hoá | Chưa | Thiếu — ghép được với "Yêu 10 – Chọn 3 – Làm 1" |
| 5. Chọn use case ROI cao | Chấm 4 tiêu chí: tiết kiệm thời gian 40%, tăng doanh thu 30%, giảm lỗi 20%, dễ triển khai 10% | Chưa có bảng chấm | Thiếu |
| 6. Đóng gói skill | Input → context → workflow → tool/MCP → output → **KPI** | Chuẩn SKILL.md | Skill nội bộ **chưa ghi KPI đo hiệu quả** |
| 7. Skill library theo phòng ban | | 138 skill, 12 repo | Đã có |
| 8. Skill + DNA | Cùng skill, khác DNA → khác đầu ra | Một phần (file context theo plugin) | Phụ thuộc bước 1 |
| 9. Tool / API / MCP | | MCP Pancake, Bluecore, Meta, Lark, GoClaw… | Đã có |
| 10. Execution engine | Skill hub + AI router + engine (Codex, Claude Code, browser, workflow) | `dieu-phoi/bang-dinh-tuyen.md`, `nen-tang/` | Router mới là bảng tay |
| 11. Repo factory | Tìm trên GitHub → quét bảo mật/license → hợp DNA → fork/tuỳ biến → test & benchmark → triển khai | `doi-chieu/quy-trinh.md` + `skill-lab` | Đã có quy trình |
| 12. AI orchestrator | Planner, router, evaluator, memory, scheduler | GoClaw (cron, memory, trace) | Chưa có evaluator chạy tự động |
| 13. Multi-agent | Supervisor + agent theo phòng ban | Đội 7 agent marketing GoClaw | Chưa có cho phòng ban khác |
| 14. Duyệt & phân quyền | AI đề xuất → kiểm rule → người duyệt → AI thực thi; quyền theo vai trò (CEO, manager, nhân viên) | 3 mức quyền trong `AGENTS.md` | **Chưa phân quyền theo vai trò người dùng** |
| 15. AI Control Center | Một màn hình: skill đang chạy, agent, tỷ lệ tự động thành công, thời gian tiết kiệm, chi phí/token, cảnh báo, log, sự cố | Thiết kế 2 bảng LarkBase | **Chưa có dashboard** |
| 16. AI Loop | Execute → evaluate → feedback → improve → test → version → deploy; ví dụ skill v1.8 → test 20 case → v1.9 | Vòng B + `may-cham` | **Skill chưa có số phiên bản riêng** |

## Đánh giá

- **Khớp hướng:** bước 7–16 gần như trùng kiến trúc Agent-control-os. Đây là xác nhận độc lập cho hướng đi, không phải lý do để thay đổi.
- **Đáng lấy nhất:** bước 1 (một hồ sơ DNA chung), bước 3–5 (inventory → ma trận → chấm ROI để chọn việc giao AI), bước 6 (thêm KPI vào skill), bước 15 (dashboard điều hành).
- **Cẩn trọng:** slide là tài liệu bán khoá học; con số trong case study (Cal AI, MEDVi, FPT) và trọng số chấm ROI là tuyên bố của tác giả, chưa kiểm chứng.

## Đề xuất việc tiếp theo (chưa làm)

1. Hồ sơ DNA chung `dna/` trong Agent-control-os, gom từ `sync/Who_am_i_user.md`, `product-marketing-context`, `00-context-ban-hang`.
2. Thêm trường `kpi` và `phien_ban` vào `danh-muc/skills.yaml`.
3. Dashboard điều hành trên LarkBase từ 2 bảng đã thiết kế.
