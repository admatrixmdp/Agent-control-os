# DECISIONS — harness

Quyết định riêng của harness. Đi theo thư mục khi tách repo.

| Ngày | Bối cảnh | Lựa chọn | Chọn | Lý do | Đảo ngược được |
|---|---|---|---|---|---|
| 2026-10-27 | Khung tham chiếu kiến trúc harness | Tự nghĩ / chép nguyên một harness có sẵn / ADAPT bài Harness Engineering (arXiv 2609.00006) | **ADAPT** | Bài là bản đồ giải phẫu 11 harness từ mã nguồn; lấy khung 7 phân hệ và mẫu thiết kế, không lấy sản phẩm | C |
| 2026-10-27 | Lõi chạy harness | Viết lõi mới mỏng / dùng nền tảng đang chạy | **GoClaw/Goso** (Quân chốt) | Đã chạy thật với khách; sửa dần theo 7 phân hệ thay vì viết lại | C |
| 2026-10-27 | Chỗ đặt cấu trúc harness | Repo riêng / thư mục trong Agent-control-os | **`harness/` trong Agent-control-os**, tách khi đủ dày (Quân chốt) | Còn mỏng, chưa có mã; giữ một chỗ điều phối; luật tách ở `RANH-GIOI.md` | C |
| 2026-10-27 | Bản đồ chi tiết nền tảng lõi ↔ 7 phân hệ | Đưa vào repo / giữ ngoài repo | **Không đưa vào repo** (Quân chốt) | — | C |
| 2026-10-27 | Cách truy xuất | Tìm theo vector / truy xuất tất định | **Tất định cho dữ liệu có cấu trúc** (đơn, khách, sản phẩm); vector chỉ cho văn bản tự do | 11/11 harness trong bài không dùng vector để tìm mã; truy vấn có cấu trúc chính xác hơn với dữ liệu nghiệp vụ | C |
| 2026-10-27 | Ngưỡng giới hạn và duyệt | Đặt số ngay / đo trước | **Đo 2 tuần mức nền rồi mới đặt** | Đặt trước thì đoán; luật quá chặt làm agent hỏi liên tục | C |
