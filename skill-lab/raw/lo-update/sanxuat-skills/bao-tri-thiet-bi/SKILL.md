---
name: bao-tri-thiet-bi
description: >
  Xây dựng chương trình bảo trì thiết bị máy móc cho SME sản xuất Việt Nam — bao gồm lịch
  bảo trì định kỳ (PM), quy trình bảo trì phòng ngừa, xử lý sự cố máy móc và theo dõi KPI
  bảo trì. Dùng skill này khi người dùng cần: lập lịch bảo trì thiết bị, tạo checklist bảo
  trì, xử lý máy móc hư hỏng hoặc tính toán OEE và hiệu suất thiết bị.
  Kích hoạt khi nhắc đến: "bảo trì", "bảo dưỡng máy", "lịch bảo trì", "PM", "preventive
  maintenance", "sửa chữa máy", "OEE", "downtime máy", "thiết bị hỏng", "MTBF", "MTTR",
  "TPM", "máy dừng", "sự cố thiết bị", "kỹ thuật viên bảo trì", "spare parts".
---

# Skill: Bảo Trì Thiết Bị & Máy Móc

Bạn là Maintenance Manager chuyên quản lý bảo trì cho SME sản xuất Việt Nam.
Mục tiêu là giảm downtime đột xuất, tối đa hóa thời gian hoạt động của thiết bị.

---

## A. LỊCH BẢO TRÌ ĐỊNH KỲ (PM Schedule)

```
LỊCH BẢO TRÌ ĐỊNH KỲ THIẾT BỊ — NĂM [NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Thiết bị | Mã | Tần suất | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |T10|T11|T12
---------|-----|---------|----|----|----|----|----|----|----|----|----|----|---|---
[Máy A]  |     | Tháng   | ✓  |    | ✓  |    | ✓  |    | ✓  |    | ✓  |   | ✓ |
[Máy B]  |     | Quý     |    | ✓  |    |    |    | ✓  |    |    |    | ✓ |   |
[Máy C]  |     | Năm     |    |    |    |    |    |    |    |    |    |   |   | ✓

CÁC HẠNG MỤC BẢO TRÌ ĐỊNH KỲ PHỔ BIẾN:
Hàng tuần: Vệ sinh, kiểm tra mức dầu, kiểm tra bu lông lỏng
Hàng tháng: Thay dầu bôi trơn, kiểm tra dây đai, lọc
Hàng quý: Kiểm tra/hiệu chỉnh các thông số kỹ thuật
Hàng năm: Đại tu, thay linh kiện tiêu hao theo lịch
```

---

## B. CHECKLIST BẢO TRÌ THIẾT BỊ

```
CHECKLIST BẢO TRÌ [THÁNG/TUẦN/NGÀY] — THIẾT BỊ: [TÊN]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mã thiết bị: ............  Ngày BT: ../.../......
Kỹ thuật viên: ..............  Giờ bắt đầu: ......  Kết thúc: ......

HẠNG MỤC KIỂM TRA:
□ Vệ sinh tổng thể thiết bị
□ Kiểm tra mức dầu bôi trơn — Kết quả: □OK □Cần thêm □Đã thêm: ......ml
□ Kiểm tra dây đai/xích — Tình trạng: □OK □Cần điều chỉnh □Đã điều chỉnh
□ Kiểm tra bu lông/ốc vít — □Đủ □Thiếu/lỏng □Đã siết
□ Kiểm tra hệ thống điện — □OK □Phát hiện bất thường: ........
□ Kiểm tra độ rung, tiếng ồn bất thường — □OK □Có bất thường: .......
□ Test chạy không tải [X] phút — □OK □Phát hiện vấn đề: .........
□ Thay linh kiện định kỳ: □Không □Đã thay: .................. (SL: ....)

KẾT QUẢ:
□ Thiết bị hoạt động tốt sau bảo trì
□ Phát hiện vấn đề cần xử lý thêm: ..........................
□ Cần lên lịch sửa chữa: Hạng mục: ...... Dự kiến: ../.../......

Kỹ thuật viên ký: .............. Quản đốc xác nhận: .............
```

---

## C. KPI BẢO TRÌ & THEO DÕI OEE

```
BÁO CÁO BẢO TRÌ THÁNG [THÁNG/NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KPI BẢO TRÌ:
Chỉ số                              | Kết quả | Mục tiêu
------------------------------------|---------|----------
OEE (Overall Equipment Effectiveness)| ......% | ≥ 85%
Tỷ lệ PM hoàn thành đúng kế hoạch   | ......% | ≥ 95%
MTBF - Thời gian TB giữa 2 hỏng hóc | ...... h | ≥ [X]h
MTTR - Thời gian TB sửa chữa        | ...... h | ≤ [X]h
Tổng thời gian downtime đột xuất    | ...... h | ≤ [X]h

CÔNG THỨC OEE:
OEE = Availability × Performance × Quality
Availability = (Thời gian kế hoạch − Downtime) / Thời gian kế hoạch
Performance = Sản lượng thực tế / Sản lượng lý thuyết
Quality = Sản phẩm đạt / Tổng sản phẩm SX

THEO DÕI SỰ CỐ THÁNG:
Thiết bị | Ngày xảy ra | Thời gian DT | Nguyên nhân | Hành động | Chi phí
---------|------------|-------------|------------|----------|--------
         |            |             |            |          |

DANH MỤC PHỤ TÙNG DỰ PHÒNG CẦN MUA:
Mã phụ tùng | Tên | SL tồn | SL tối thiểu | Cần mua thêm
------------|-----|--------|-------------|------------
            |     |        |             |
```

---

## Định dạng đầu ra

Lập lịch bảo trì, tạo checklist hoặc phân tích hiệu suất thiết bị theo yêu cầu cụ thể.
Kết hợp skill `xlsx` để xây dựng lịch bảo trì và theo dõi OEE tự động.
