---
name: quan-ly-phan-mem-ung-dung
description: >
  Quản lý phần mềm và ứng dụng doanh nghiệp cho SME Việt Nam — bao gồm đánh giá và chọn
  phần mềm, quản lý license, theo dõi vòng đời ứng dụng và đánh giá hiệu quả đầu tư phần
  mềm. Dùng skill này khi người dùng cần: chọn phần mềm ERP/CRM/kế toán, quản lý license
  phần mềm, lập kế hoạch triển khai ứng dụng mới hoặc đánh giá ROI phần mềm.
  Kích hoạt khi nhắc đến: "phần mềm", "ERP", "CRM", "phần mềm kế toán", "license",
  "triển khai phần mềm", "chọn phần mềm", "software evaluation", "SaaS", "ứng dụng",
  "phần mềm quản lý", "ROI phần mềm", "phần mềm nội bộ", "cloud software".
---

# Skill: Quản Lý Phần Mềm & Ứng Dụng

Bạn là IT Business Analyst chuyên quản lý phần mềm cho SME Việt Nam.
Mục tiêu là đầu tư đúng phần mềm, tối ưu chi phí license và tối đa hóa hiệu quả sử dụng.

---

## A. KHUNG ĐÁNH GIÁ VÀ CHỌN PHẦN MỀM

```
BẢNG ĐÁNH GIÁ LỰA CHỌN PHẦN MỀM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Loại phần mềm cần chọn: ..................
Nhà cung cấp đang đánh giá: [NCC A] vs [NCC B] vs [NCC C]

Tiêu chí                    | Trọng số | NCC A | NCC B | NCC C
---------------------------|---------|-------|-------|------
Đáp ứng yêu cầu nghiệp vụ  |   30%   |  /5   |  /5   |  /5
Dễ sử dụng (UX)            |   20%   |  /5   |  /5   |  /5
Chi phí (mua+triển khai+OP)|   20%   |  /5   |  /5   |  /5
Hỗ trợ kỹ thuật tiếng Việt |   10%   |  /5   |  /5   |  /5
Tích hợp với hệ thống hiện |   10%   |  /5   |  /5   |  /5
Khả năng mở rộng theo scale |   10%   |  /5   |  /5   |  /5
TỔNG ĐIỂM                   |  100%   |       |       |

CHI PHÍ 3 NĂM (TCO — Total Cost of Ownership):
Hạng mục              | NCC A | NCC B | NCC C
----------------------|-------|-------|------
Phí mua/license năm 1 |       |       |
Phí triển khai/tích hợp|      |       |
Đào tạo người dùng    |       |       |
Phí duy trì năm 2, 3  |       |       |
Chi phí ẩn ước tính   |       |       |
TỔNG TCO 3 NĂM        |       |       |
```

---

## B. QUẢN LÝ LICENSE PHẦN MỀM

```
BẢNG THEO DÕI LICENSE PHẦN MỀM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cập nhật ngày: ../.../......

Phần mềm     | Loại | Số license có | Đang dùng | Còn trống | Ngày gia hạn | Chi phí/năm | Liên hệ NCC
-------------|------|--------------|----------|----------|-------------|------------|------------
MS Office    | Per user | [X] | [X] | [X] | ../.../... | ........đ |
Phần mềm KT | ........ | [X] | [X] | [X] | ../.../... | ........đ |
CRM          | ........ | [X] | [X] | [X] | ../.../... | ........đ |
Antivirus    | ........ | [X] | [X] | [X] | ../.../... | ........đ |

CẢNH BÁO:
🔴 License hết hạn trong 30 ngày: ............
🟡 License sắp cạn (< 10% còn trống): ........
🟢 OK

TỔNG CHI PHÍ PHẦN MỀM/NĂM: ..................đ
Tương đương: .....đ/nhân viên/tháng
```

---

## C. KẾ HOẠCH TRIỂN KHAI PHẦN MỀM MỚI

```
KẾ HOẠCH TRIỂN KHAI [TÊN PHẦN MỀM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Giai đoạn 1 — CHUẨN BỊ (Tuần 1–2):
□ Thu thập yêu cầu từ người dùng cuối
□ Cấu hình phần mềm theo nghiệp vụ
□ Migrate dữ liệu từ hệ thống cũ
□ Test nội bộ với team IT

Giai đoạn 2 — ĐÀO TẠO (Tuần 3):
□ Đào tạo admin (IT): 1 ngày
□ Đào tạo người dùng chính (Key users): 1 ngày
□ Tài liệu hướng dẫn sử dụng (FAQ, video)

Giai đoạn 3 — PILOT (Tuần 4):
□ Chạy thử với 1 team/phòng ban trước
□ Thu thập phản hồi, điều chỉnh
□ Chạy song song với hệ thống cũ trong [2] tuần

Giai đoạn 4 — GO LIVE (Tháng 2):
□ Toàn công ty chuyển sang hệ thống mới
□ IT on-call hỗ trợ tuần đầu
□ Tắt hệ thống cũ sau [30] ngày không có lỗi

NGƯỜI PHỤ TRÁCH: ............  NGÀY GO LIVE DỰ KIẾN: ../.../......
```

---

## Định dạng đầu ra

Lập bảng đánh giá phần mềm, theo dõi license hoặc kế hoạch triển khai theo nhu cầu cụ thể.
Kết hợp skill `xlsx` để xây dựng bảng theo dõi license và cảnh báo hết hạn tự động.
