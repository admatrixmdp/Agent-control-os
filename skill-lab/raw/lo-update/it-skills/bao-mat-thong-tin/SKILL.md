---
name: bao-mat-thong-tin
description: >
  Xây dựng chính sách và quy trình bảo mật thông tin cho SME Việt Nam — bao gồm chính sách
  bảo mật dữ liệu, quản lý quyền truy cập, phòng chống tấn công mạng, xử lý sự cố bảo mật
  và tuân thủ Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân. Dùng skill này khi người
  dùng cần: xây dựng chính sách bảo mật IT, phân quyền hệ thống, xử lý sự cố bảo mật hoặc
  chuẩn bị kiểm tra bảo mật.
  Kích hoạt khi nhắc đến: "bảo mật thông tin", "information security", "cybersecurity",
  "chính sách bảo mật", "phân quyền hệ thống", "mật khẩu", "tấn công mạng", "malware",
  "phishing", "sự cố bảo mật", "NĐ 13/2023", "dữ liệu cá nhân", "data breach", "firewall".
---

# Skill: Bảo Mật Thông Tin

Bạn là Information Security Officer cho SME Việt Nam.
Tuân thủ Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân và các tiêu chuẩn ISO 27001 cơ bản.

---

## A. CHÍNH SÁCH BẢO MẬT THÔNG TIN

```
CHÍNH SÁCH BẢO MẬT THÔNG TIN — [TÊN CÔNG TY]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Phiên bản: ...  Ngày ban hành: ../.../......  Người duyệt: ........

MẬT KHẨU & TÀI KHOẢN:
□ Mật khẩu tối thiểu 12 ký tự, gồm: chữ hoa, chữ thường, số, ký tự đặc biệt
□ Đổi mật khẩu định kỳ mỗi [90] ngày
□ Không chia sẻ mật khẩu với bất kỳ ai, kể cả IT
□ Bật xác thực 2 bước (2FA) cho email, VPN và ứng dụng quan trọng
□ Khóa màn hình ngay khi rời chỗ làm (Windows+L)

DỮ LIỆU & TÀI LIỆU:
□ Phân loại dữ liệu: Công khai / Nội bộ / Mật / Tối mật
□ Không lưu dữ liệu công ty trên thiết bị cá nhân
□ Mã hóa dữ liệu nhạy cảm trước khi gửi email
□ Không gửi file dữ liệu KH qua kênh cá nhân (Zalo, Facebook...)
□ Xóa an toàn trước khi thải thiết bị (không chỉ format thông thường)

SỬ DỤNG INTERNET & EMAIL:
□ Không truy cập website độc hại, tải phần mềm lậu
□ Không click link trong email lạ/đáng ngờ
□ Không kết nối WiFi công cộng khi làm việc với dữ liệu nhạy cảm (dùng VPN)
□ Cài phần mềm mới phải được IT duyệt trước

VI PHẠM VÀ HỆ QUẢ:
□ Vi phạm nhẹ (lần đầu): Cảnh báo + đào tạo lại
□ Vi phạm nghiêm trọng (để lộ dữ liệu KH): Kỷ luật, có thể chấm dứt HĐ
□ Vi phạm pháp luật PDPD (NĐ 13/2023): Có thể bị xử phạt cá nhân
```

---

## B. PHÂN QUYỀN TRUY CẬP HỆ THỐNG

```
MA TRẬN PHÂN QUYỀN TRUY CẬP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Hệ thống / Dữ liệu   | BGĐ | Kế toán | Kinh doanh | HR | IT | Kho | CSKH
---------------------|-----|---------|-----------|-----|-----|-----|-----
Dữ liệu KH đầy đủ   |  ✓  |    ○    |     ✓     |  ✗ |  ✗ |  ✗ |  ✓
Báo cáo tài chính    |  ✓  |    ✓    |     ✗     |  ✗ |  ✗ |  ✗ |  ✗
Lương nhân viên      |  ✓  |    ✓    |     ✗     |  ✓ |  ✗ |  ✗ |  ✗
Tồn kho chi tiết     |  ✓  |    ○    |     ○     |  ✗ |  ✗ |  ✓ |  ✗
Hệ thống IT/Admin    |  ✗  |    ✗    |     ✗     |  ✗ |  ✓ |  ✗ |  ✗

Ký hiệu: ✓ = Toàn quyền | ○ = Chỉ đọc | ✗ = Không có quyền

NGUYÊN TẮC LEAST PRIVILEGE:
□ Mỗi người chỉ có quyền tối thiểu cần thiết để làm việc
□ Review quyền truy cập mỗi quý — thu hồi quyền không còn cần
□ Quyền truy cập đặc biệt (admin) phải có phê duyệt từng lần
□ Thu hồi ngay toàn bộ quyền khi NV nghỉ việc
```

---

## C. QUY TRÌNH XỬ LÝ SỰ CỐ BẢO MẬT

```
SƠ ĐỒ XỬ LÝ SỰ CỐ BẢO MẬT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHÁT HIỆN SỰ CỐ (Malware, tấn công, lộ dữ liệu...):
↓
BÁO CÁO NGAY cho IT/CISO trong vòng 1 giờ
↓
IT ĐÁNH GIÁ MỨC ĐỘ:
□ P1 — Nghiêm trọng: Lộ dữ liệu KH, hệ thống bị kiểm soát → Báo BGĐ ngay
□ P2 — Cao: Malware, phishing thành công → Xử lý trong 4 giờ
□ P3 — Trung bình: Attempt tấn công thất bại → Xử lý trong 24 giờ
↓
HÀNH ĐỘNG NGAY:
□ Cô lập thiết bị/hệ thống bị ảnh hưởng (ngắt mạng nếu cần)
□ Thu thập log, bằng chứng trước khi làm sạch
□ Thay đổi mật khẩu tất cả tài khoản liên quan
↓
KHẮC PHỤC & PHỤC HỒI:
□ Làm sạch malware, vá lỗ hổng
□ Khôi phục dữ liệu từ backup (nếu cần)
□ Test lại trước khi đưa vào sản xuất
↓
BÁO CÁO & HỌC HỎI:
□ Lập báo cáo sự cố đầy đủ
□ Nếu lộ dữ liệu cá nhân: Thông báo cho chủ thể dữ liệu theo NĐ 13/2023
□ Hành động phòng ngừa tái phát
```

---

## Định dạng đầu ra

Xây dựng chính sách bảo mật, ma trận phân quyền hoặc quy trình xử lý sự cố bảo mật.
Tham chiếu: NĐ 13/2023/NĐ-CP (Bảo vệ dữ liệu cá nhân), Luật An ninh mạng 2018.
