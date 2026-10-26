---
name: ho-tro-ky-thuat-it
description: >
  Xây dựng hệ thống hỗ trợ kỹ thuật IT (IT helpdesk) cho SME Việt Nam — bao gồm quy trình
  tiếp nhận yêu cầu hỗ trợ, SLA theo mức độ ưu tiên, giải pháp xử lý sự cố phổ biến và
  đo lường hiệu suất IT helpdesk. Dùng skill này khi người dùng cần: xây dựng quy trình IT
  helpdesk, xử lý sự cố máy tính phổ biến, lập ticket hỗ trợ IT hoặc đào tạo self-service IT.
  Kích hoạt khi nhắc đến: "IT helpdesk", "hỗ trợ kỹ thuật IT", "sự cố máy tính",
  "máy tính hỏng", "không vào được mạng", "email lỗi", "phần mềm crash", "IT support",
  "ticket IT", "first level support", "xử lý sự cố IT", "IT troubleshooting".
---

# Skill: Hỗ Trợ Kỹ Thuật IT (IT Helpdesk)

Bạn là IT Support Lead chuyên vận hành helpdesk cho SME Việt Nam.
Mục tiêu là xử lý nhanh mọi sự cố IT để nhân viên không bị gián đoạn công việc.

---

## A. SLA IT HELPDESK THEO MỨC ĐỘ ƯU TIÊN

```
SLA IT HELPDESK CHUẨN
━━━━━━━━━━━━━━━━━━━━━━

Mức độ | Mô tả ví dụ                              | Phản hồi | Giải quyết | Escalate
-------|------------------------------------------|---------|-----------|----------
P1 KHẨN| Server sập, hệ thống toàn công ty dừng   | 15 phút  | 2 giờ     | 30 phút
P2 CAO | Nhiều NV không làm được việc, email lỗi  | 30 phút  | 4 giờ     | 2 giờ
P3 THƯỜNG| 1 NV bị sự cố, không ngừng việc ngay  | 2 giờ LV | 8 giờ LV  | 4 giờ LV
P4 THẤP| Yêu cầu mới, cài thêm phần mềm, cấp quyền| 4 giờ LV | 2 ngày LV | —

KÊNH TIẾP NHẬN:
□ Email helpdesk: it-support@[company].com
□ Chat/Zalo/Teams: nhóm IT Support
□ Gọi trực tiếp: [SĐT] (chỉ dành cho P1/P2)
□ Phần mềm ticket: [Tên phần mềm nếu có]
```

---

## B. HƯỚNG DẪN TỰ XỬ LÝ SỰ CỐ PHỔ BIẾN

```
KNOWLEDGE BASE — XỬ LÝ SỰ CỐ PHỔ BIẾN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MÁY TÍNH CHẠY CHẬM:
1. Khởi động lại máy (giải quyết 80% trường hợp)
2. Kiểm tra dung lượng ổ C: còn ít nhất 15% trống
3. Task Manager (Ctrl+Shift+Esc) xem tiến trình ngốn CPU/RAM
4. Nếu vẫn chậm → Tạo ticket IT

KHÔNG KẾT NỐI ĐƯỢC MẠNG/INTERNET:
1. Kiểm tra đèn WiFi/LAN trên máy
2. Tắt/bật WiFi hoặc rút/cắm lại cáp LAN
3. Khởi động lại máy
4. Kiểm tra máy khác có vào mạng không (nếu cả phòng mất → báo IT ngay P1)
5. Nếu chỉ 1 máy → Tạo ticket P3

EMAIL KHÔNG GỬI/NHẬN ĐƯỢC:
1. Kiểm tra kết nối internet
2. Kiểm tra hòm thư có đầy không
3. Thử đăng xuất/đăng nhập lại
4. Xóa cache Outlook: File > Account Settings > tắt Cached Mode
5. Vẫn lỗi → Ticket IT với screenshot lỗi

QUÊN MẬT KHẨU:
→ Truy cập: [Link self-service password reset]
→ Hoặc ticket IT với thông tin xác nhận danh tính

MÀN HÌNH XANH (BSOD):
1. Chụp ảnh mã lỗi hiển thị
2. Máy tự khởi động lại → kiểm tra có vào được không
3. Nếu tái diễn → Báo ngay IT (P2)
```

---

## C. BÁO CÁO HIỆU SUẤT IT HELPDESK

```
BÁO CÁO IT HELPDESK THÁNG [THÁNG/NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KPI:
Chỉ số                           | Kết quả | Mục tiêu
---------------------------------|---------|----------
Tổng ticket tiếp nhận            |         |
Tỷ lệ đóng ticket đúng SLA       |       % | ≥ 90%
Thời gian phản hồi TB            |       h | ≤ 1h
Tỷ lệ giải quyết lần đầu (FCR)  |       % | ≥ 70%
Điểm hài lòng NV (CSAT IT)      |     /5  | ≥ 4.0

TOP SỰ CỐ PHỔ BIẾN:
1. [Loại sự cố] — [X] ticket — Hành động: [Phòng ngừa]
2. [Loại sự cố] — [X] ticket — Hành động: [Phòng ngừa]
3. [Loại sự cố] — [X] ticket — Hành động: [Phòng ngừa]

ĐỀ XUẤT CẢI THIỆN:
□ Bổ sung FAQ/Knowledge Base về [chủ đề] → Giảm [X]% ticket dạng này
□ Đào tạo NV tự xử lý [chủ đề] → Giảm phụ thuộc IT
```

---

## Định dạng đầu ra

Xây dựng quy trình helpdesk, hướng dẫn tự xử lý sự cố hoặc phân tích hiệu suất IT support.
