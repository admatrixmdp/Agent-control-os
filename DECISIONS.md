# DECISIONS

| Ngày | Bối cảnh | Lựa chọn | Chọn | Lý do | Đảo ngược được |
|---|---|---|---|---|---|
| 2026-10-24 | Đóng gói vòng lặp cải tiến skill | (a) repo trung tâm chứa mọi eval; (b) mỗi repo tự có máy chấm; (c) eval theo skill, máy chấm một chỗ | (c) | Skill mang eval theo khi cài; sửa máy chấm một lần cho mọi repo | C |
| 2026-10-26 | Chuẩn định dạng eval toàn hệ | Khung Company-suite-os (`tinh-huong/ky-vong`) vs khung kế toán (`phai_co/khong_duoc_co/hanh_vi/can_cu/nguoi_duyet`) | Khung kế toán | Đầy đủ hơn: có chuỗi bắt buộc / cấm, căn cứ, người duyệt | C |
| 2026-10-26 | Chỗ đặt máy chấm dùng chung | `core-process` vs repo riêng vs skill trong Company-suite-os | **Agent-control-os** | `core-process` là công cụ giao việc viết code, có mục đích riêng; repo điều phối là chỗ đúng của động cơ dùng chung (sửa đề xuất ngày 24/10) | C |
| 2026-10-26 | Kho 290 skill cần nghiên cứu | Cùng repo điều phối vs repo `skill-lab` riêng | `skill-lab` riêng (đề xuất, chờ Quân chốt) | Repo điều phối phải nhỏ, tin cậy cao; 290 skill là dữ liệu lớn, tin cậy thấp, có rủi ro chỉ dẫn ẩn | C |
| 2026-10-26 | Điều khiển agent đám mây (Duet, Dots, Muse, Grok Bot) | Cài skill trực tiếp vs qua MCP | Qua MCP + dán luật | Không nền tảng nào có API điều khiển hay nạp SKILL.md từ repo | C |
| 2026-10-26 | pstack | Cài nguyên gói vs ADAPT | ADAPT | Giá trị ở phương pháp; nội dung chủ yếu cho viết code; chi phí token ~gấp đôi | C |
| 2026-10-26 | Giám khảo eval | Cùng mô hình chạy vs mô hình khác | Mô hình khác (mặc định Sonnet chấm Opus) | Giảm tự chấm cho mình | C |
