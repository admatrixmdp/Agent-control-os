# DECISIONS

| Ngày | Bối cảnh | Lựa chọn | Chọn | Lý do | Đảo ngược được |
|---|---|---|---|---|---|
| 2026-10-24 | Đóng gói vòng lặp cải tiến skill | (a) repo trung tâm chứa mọi eval; (b) mỗi repo tự có máy chấm; (c) eval theo skill, máy chấm một chỗ | (c) | Skill mang eval theo khi cài; sửa máy chấm một lần cho mọi repo | C |
| 2026-10-26 | Chuẩn định dạng eval toàn hệ | Khung Company-suite-os (`tinh-huong/ky-vong`) vs khung kế toán (`phai_co/khong_duoc_co/hanh_vi/can_cu/nguoi_duyet`) | Khung kế toán | Đầy đủ hơn: có chuỗi bắt buộc / cấm, căn cứ, người duyệt | C |
| 2026-10-26 | Chỗ đặt máy chấm dùng chung | `core-process` vs repo riêng vs skill trong Company-suite-os | **Agent-control-os** | `core-process` là công cụ giao việc viết code, có mục đích riêng; repo điều phối là chỗ đúng của động cơ dùng chung (sửa đề xuất ngày 24/10) | C |
| 2026-10-26 | Kho skill bên ngoài (510 skill Taki) | Cùng repo điều phối vs repo `skill-lab` riêng | **Thư mục `skill-lab/` trong Agent-control-os** (Quân chốt) | Một chỗ cho toàn bộ điều phối; cách ly bằng luật: không manifest, không đọc khi làm việc thường, `raw/` bất biến | C |
| 2026-10-26 | Điều khiển agent đám mây (Duet, Dots, Muse, Grok Bot) | Cài skill trực tiếp vs qua MCP | Qua MCP + dán luật | Không nền tảng nào có API điều khiển hay nạp SKILL.md từ repo | C |
| 2026-10-26 | pstack | Cài nguyên gói vs ADAPT | ADAPT | Giá trị ở phương pháp; nội dung chủ yếu cho viết code; chi phí token ~gấp đôi | C |
| 2026-10-26 | Giám khảo eval | Cùng mô hình chạy vs mô hình khác | Mô hình khác (mặc định Sonnet chấm Opus) | Giảm tự chấm cho mình | C |
| 2026-10-26 | Gắn nhãn đối chiếu | Độ giống chữ (TF-IDF) vs agent đọc nghĩa | Agent đọc nghĩa; TF-IDF chỉ đưa ứng viên thô | Skill ngoài tên tiếng Anh, nội bộ tên tiếng Việt → độ giống chữ gợi ý 465/510 là "mới", sai rõ | C |
| 2026-10-26 | File slide 67 MB "AI AGENT CEO" | Đưa vào repo vs tóm tắt | Tóm tắt ở `tham-khao/ai-agent-ceo-taki.md` | Vượt ngưỡng 10 MB; 56/57 slide là ảnh | C |
| 2026-10-26 | Đánh dấu skill ngoài đã xử lý (Quân chốt: skill không đạt đưa vào archive) | (a) dời file từ `raw/` sang thư mục archive; (b) giữ file gốc, ghi sổ `trang-thai.yaml` + phiếu `luu-tru/` | **(b)** | (a) phạm quyết định `raw/` bất biến; (b) giữ nguyên gốc, một sổ trạng thái, script tự bỏ qua skill đã lưu trữ | C |
| 2026-10-26 | Chốt nhãn skill ngoài | Chỉ đọc văn bản vs đọc + chạy thử | Chạy thử trước khi chốt nhãn "giá trị cao" (đề xuất, chờ Quân chốt) | Lô thử 1: `sales-late-stage-rescue` gắn "cao" khi đọc, chạy thử thua cả bản không skill; `sales-lead-scoring-engine` xếp shop 6 tỷ trên tài khoản 150 tỷ | C |
