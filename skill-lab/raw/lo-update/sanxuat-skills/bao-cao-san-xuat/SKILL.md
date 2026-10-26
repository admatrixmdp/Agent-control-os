---
name: bao-cao-san-xuat
description: >
  Xây dựng hệ thống báo cáo sản xuất cho SME Việt Nam — bao gồm báo cáo ca/ngày/tháng,
  KPI sản xuất, phân tích năng suất, hiệu suất thiết bị và trình bày kết quả cho BGĐ.
  Dùng skill này khi người dùng cần: lập báo cáo sản xuất ca, báo cáo tháng, tính năng suất
  lao động, OEE, phân tích downtime hoặc dashboard sản xuất.
  Kích hoạt khi nhắc đến: "báo cáo sản xuất", "năng suất sản xuất", "KPI sản xuất",
  "báo cáo ca", "báo cáo nhà máy", "production report", "OEE báo cáo", "hiệu suất sản xuất",
  "output sản xuất", "tỷ lệ hoàn thành kế hoạch", "production KPI", "báo cáo xưởng".
---

# Skill: Báo Cáo Sản Xuất

Bạn là Production Manager chuyên phân tích và báo cáo sản xuất cho SME Việt Nam.
Mục tiêu là cung cấp số liệu chính xác, kịp thời để BGĐ ra quyết định sản xuất.

---

## A. BÁO CÁO CA SẢN XUẤT

```
BÁO CÁO CA SẢN XUẤT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ngày: ../.../......  Ca: □ Sáng □ Chiều □ Đêm
Trưởng ca: ............  Xưởng/Line: ............
Giờ làm việc: ...... đến ......  Tổng giờ: ......

SẢN LƯỢNG:
Sản phẩm | Kế hoạch ca | Thực tế | Đạt QC | Lỗi | Tỷ lệ đạt%
---------|------------|---------|--------|-----|------------
         |            |         |        |     |

TỔNG KẾT CA:
□ Tỷ lệ hoàn thành kế hoạch: ......%
□ Tỷ lệ sản phẩm đạt chất lượng: ......%
□ Downtime máy móc: ...... phút | Nguyên nhân: .............
□ Vắng mặt NV: ...... người | Nguyên nhân: ................

SỰ KIỆN ĐÁNG LƯU Ý:
□ Sự cố máy: .............................................
□ Vấn đề chất lượng: .....................................
□ Thiếu NVL: .............................................
□ An toàn lao động: ......................................

Trưởng ca ký: .............. Quản đốc nhận bàn giao: ..........
```

---

## B. BÁO CÁO SẢN XUẤT THÁNG

```
BÁO CÁO SẢN XUẤT THÁNG [THÁNG/NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KPI SẢN XUẤT:
Chỉ số                           | Kết quả | Mục tiêu | Đạt?
---------------------------------|---------|----------|------
Tỷ lệ hoàn thành KH sản lượng   |       % | ≥ 95%    | □
OEE (Overall Equip. Efficiency)  |       % | ≥ 85%    | □
Tỷ lệ lỗi sản phẩm              |       % | ≤ [X]%   | □
Năng suất lao động (SP/người/ca) |         | ≥ [X]    | □
Tỷ lệ sử dụng NVL vs định mức   |       % | ≤ 102%   | □
Số sự cố an toàn lao động       |         | = 0      | □

SẢN LƯỢNG THEO SẢN PHẨM:
Sản phẩm | KH tháng | Thực tế | Tỷ lệ | Lũy kế YTD | KH YTD | %YTD
---------|---------|---------|-------|-----------|--------|------
         |         |         |     % |           |        |     %

PHÂN TÍCH DOWNTIME:
Nguyên nhân     | Số lần | Tổng giờ | % tổng DT | Hành động
----------------|--------|----------|-----------|----------
Hỏng máy đột xuất |      |          |           |
Thiếu NVL       |        |          |           |
Đổi sản phẩm    |        |          |           |
Vệ sinh/5S      |        |          |           |

CHI PHÍ SẢN XUẤT:
□ Chi phí NVL/SP: ........đ vs Định mức: ........đ
□ Chi phí lao động/SP: ...đ vs Định mức: .......đ
□ Chi phí điện/SP: .......đ
□ Tổng giá thành SX/SP: ..đ vs Kế hoạch: ......đ
```

---

## Định dạng đầu ra

Tạo báo cáo ca/tháng, dashboard KPI sản xuất hoặc phân tích năng suất theo dữ liệu thực tế.
Kết hợp skill `xlsx` để xây dựng bảng báo cáo sản xuất tự động với biểu đồ trực quan.
Kết hợp skill `pptx` để tạo slide báo cáo sản xuất trình BGĐ.
