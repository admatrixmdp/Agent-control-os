# Bảng định tuyến: loại việc → nền tảng → skill

Cách dùng: tìm loại việc ở cột 1, giao cho nền tảng ở cột 2, gọi skill/repo ở cột 3, dừng khi đạt điều kiện ở cột 4. Nếu việc không khớp dòng nào, dùng dòng "Không rõ".

Ý tưởng gốc: lệnh `/poteto-mode` của pstack (nhận mô tả việc → chọn playbook → gọi skill). Ở đây thay playbook viết code bằng playbook nghiệp vụ. Xem `tham-khao/pstack.md`.

## 1. Bảng chính

| Loại việc | Nền tảng chính | Dự phòng | Skill / repo | Điều kiện dừng | Mức quyền |
|---|---|---|---|---|---|
| Chiến lược, kế hoạch, BSC, OKR, DMAIC | Claude (chat / Code) | Codex | `Company-suite-os` | Có tài liệu + bước tiếp có người chịu trách nhiệm | Tự làm |
| Kế hoạch marketing, nội dung, copy, brief | Claude | GoClaw (đội 7 agent MKT) | `marketing-business-skill` (vn/global) | Bản nháp qua checklist skill | Tự làm; **đăng bài = hỏi trước** |
| Phân tích quảng cáo Meta / Google / TikTok / Shopee | Claude Code + MCP quảng cáo | GoClaw cron | `meta-suite-os`, `google-marketing-os`, `tiktok-suite-os`, `shopee-suite-os` | Báo cáo có số từ nguồn + đề xuất | Đọc = tự làm; **sửa chiến dịch = hỏi trước** |
| Bán hàng B2B: lead, proposal, đàm phán | Claude | Goso / ZAgent | `sale-suite-os` | Tài liệu bán hàng + bước tiếp | Tự làm; **gửi cho khách = hỏi trước** |
| Kế toán, tài chính doanh nghiệp | Claude | — | `Company-finance-accountant-os` | Kết luận có căn cứ pháp lý | Tự làm; kết luận chính thức cần kế toán trưởng duyệt |
| Đầu tư, gọi vốn, định giá, M&A | Claude | — | `investment-MA-os` | Mô hình + giả định ghi rõ | Tự làm; không khuyến nghị giao dịch |
| Tuân thủ pháp lý doanh nghiệp VN | Claude | — | `compliance-vn` | Checklist có căn cứ, có dòng miễn trừ | Tự làm; thiếu căn cứ = "không đủ cơ sở" |
| Số liệu bán lẻ, dashboard | Claude + Bluecore MCP | — | Bluecore Data | Số lõi lấy từ bảng tính sẵn | Tự làm; **sửa card = hỏi trước** |
| Vận hành shop Pancake POS | Claude + Pancake MCP | GoClaw cron | `pancake-suite` | Báo cáo / cấu hình đã kiểm | Đọc = tự làm; **ghi đơn, cấu hình = hỏi trước** |
| Sản phẩm, Linear, Orca, UI | Claude Code | Codex | `product-dev-os` | Ticket / mô tả đạt checklist | **Ghi Linear = hỏi trước** |
| Viết code, sửa repo | Codex / Claude Code | Grok (qua `core-process`) | Repo code tương ứng | Test xanh + bằng chứng chạy thật | PR; **merge = hỏi trước** |
| Web, SEO, landing page | Claude Code | — | `webmaster-suite-os`, Webcake MCP | Trang đạt kiểm tra | **Publish = hỏi trước** |
| Việc nền định kỳ (báo cáo sáng, theo dõi) | GoClaw cron | Claude scheduled task, Claude Duet | Skill tương ứng | Kết quả ghi về LarkBase / sync | Theo mức của skill |
| Việc cần trình duyệt trên web không có API | Grok Bot / Claude in Chrome | OpenAI Dots | — | Ảnh chụp / bằng chứng thao tác | **Gửi form = hỏi trước** |
| Việc cá nhân (lịch, email, đặt chỗ) | Claude Duet / Dots / Muse | — | — | Xác nhận từ Quân | **Gửi, đặt, trả tiền = hỏi trước / cấm** |
| Chấm eval, cải tiến skill | Claude Code / GitHub Actions | GoClaw cron | `Agent-control-os/may-cham` | Bảng điểm + PR | Tự làm; **merge = hỏi trước** |
| Đối chiếu skill bên ngoài | Claude Code | Codex | `doi-chieu/` | Phiếu đối chiếu đã gắn nhãn | Tự làm; **Quân chốt nhãn** |
| Không rõ | Claude | — | Hỏi Quân **một** câu để phân loại | — | — |

## 2. Quy tắc chọn khi nhiều nền tảng cùng làm được

1. **Dữ liệu ở đâu, làm ở đó.** Có MCP nối thẳng nguồn (Pancake, Bluecore, Meta) thì dùng nền tảng có MCP đó.
2. **Cần chạy lúc vắng mặt** → GoClaw cron trước (có trace), Claude scheduled task sau, agent đám mây (Duet, Dots, Grok Bot) cuối cùng vì không có trace đọc được bằng máy.
3. **Cần đo được** → nền tảng lớp A (`nen-tang/README.md`), vì chỉ lớp A chạy được máy chấm.
4. **Rủi ro cao** (tài chính, pháp lý, gửi ra ngoài) → nền tảng có cơ chế xác nhận rõ nhất, và người duyệt cuối là Quân.

## 3. Ví dụ

> "Báo cáo tuần shop bán lẻ, gửi vào nhóm Lark sáng thứ Hai."

Dòng "Vận hành shop Pancake POS" + "Việc nền định kỳ" → GoClaw cron chạy `pancake-suite:weekly`, ghi kết quả vào LarkBase. Bước "gửi vào nhóm" là **hỏi trước** cho tới khi Quân cho phép gửi tự động cho đúng nhóm đó, rồi ghi quyết định vào `DECISIONS.md`.
