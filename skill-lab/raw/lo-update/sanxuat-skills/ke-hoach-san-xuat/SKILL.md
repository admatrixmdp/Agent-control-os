---
name: ke-hoach-san-xuat
description: >
  Lập kế hoạch sản xuất cho SME Việt Nam — bao gồm kế hoạch sản xuất tháng/tuần, tính toán
  năng lực sản xuất, cân đối nguyên vật liệu, lập lịch ca làm việc và theo dõi tiến độ sản
  xuất. Dùng skill này khi người dùng cần: lập MPS (Master Production Schedule), tính năng
  lực sản xuất, cân đối nguyên vật liệu (MRP), lên lịch sản xuất hoặc theo dõi KPI sản xuất.
  Kích hoạt khi nhắc đến: "kế hoạch sản xuất", "lịch sản xuất", "MPS", "MRP", "production
  plan", "năng lực sản xuất", "cân đối nguyên liệu", "lịch ca sản xuất", "tiến độ sản xuất",
  "production schedule", "work order", "lệnh sản xuất", "công suất nhà máy".
---

# Skill: Kế Hoạch Sản Xuất

Bạn là Production Planner chuyên lập kế hoạch sản xuất cho SME Việt Nam.
Mục tiêu là đảm bảo sản xuất đúng số lượng, đúng thời gian với chi phí tối ưu.

---

## A. KẾ HOẠCH SẢN XUẤT THÁNG (MPS)

```
KẾ HOẠCH SẢN XUẤT THÁNG [THÁNG/NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ngày lập: .../.../......  Người lập: .................
Xưởng/Line: ...................  Người duyệt: ..........

TỔNG QUAN:
Tổng ngày sản xuất trong tháng: ...... ngày
Ca sản xuất/ngày: ...... ca × ...... giờ/ca
Tổng giờ máy/người có thể: ...... giờ

KẾ HOẠCH SẢN XUẤT:
Mã SP | Tên SP | ĐVT | Tồn đầu | Đơn hàng | Tồn an toàn | Cần SX | Ca SX | Thời gian hoàn thành
------|--------|-----|---------|---------|------------|--------|-------|--------------------
      |        |     |         |         |            |        |       |
      |        |     |         |         |            |        |       |

TỔNG NĂNG LỰC CẦN: ...... giờ máy/người
TỔNG NĂNG LỰC CÓ: ...... giờ máy/người
□ Đủ năng lực — Thực hiện theo kế hoạch
□ Thiếu năng lực — Phương án: □ Tăng ca  □ Outsource  □ Điều chỉnh kế hoạch

CÂN ĐỐI NGUYÊN VẬT LIỆU CHÍNH:
Nguyên liệu | Đơn vị | Cần cho kế hoạch | Tồn kho | Cần mua thêm | Thời gian order
------------|--------|-----------------|---------|-------------|----------------
            |        |                 |         |             |
```

---

## B. LỆNH SẢN XUẤT (Work Order)

```
LỆNH SẢN XUẤT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Số lệnh: WO-[NĂM][THÁNG]-[SỐ TT]
Ngày phát lệnh: .../.../......  Ngày bắt đầu: .../...
Ngày hoàn thành yêu cầu: .../.../.....
Xưởng: .................  Line/Máy: ................

SẢN PHẨM CẦN SẢN XUẤT:
Mã SP: ............  Tên: .......................
Số lượng: .......... ĐVT: .......................
Tiêu chuẩn chất lượng: .........................

NGUYÊN VẬT LIỆU:
STT | Mã NVL | Tên NVL | ĐVT | SL định mức/đơn vị SP | Tổng SL cần | Kho xuất
----|--------|---------|-----|----------------------|------------|--------
 1  |        |         |     |                      |            |
 2  |        |         |     |                      |            |

PHÂN CÔNG SẢN XUẤT:
Ca | Ngày | Máy/Line | Trưởng ca | Công nhân | SL kế hoạch
---|------|----------|----------|-----------|------------
 1 |      |          |          |           |

KẾT QUẢ THỰC TẾ:
SL hoàn thành: ......  SL đạt QC: ......  SL lỗi: ......
Ngày hoàn thành thực tế: .../.../.....  Trưởng ca ký: ..........
```

---

## C. LỊCH SẢN XUẤT TUẦN (Visual)

```
LỊCH SẢN XUẤT TUẦN [SỐ]/[NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

         | Thứ 2 | Thứ 3 | Thứ 4 | Thứ 5 | Thứ 6 | Thứ 7
---------|-------|-------|-------|-------|-------|------
Ca sáng  |[SP][SL]|      |       |       |       |
Ca chiều |       |       |       |       |       |
Ca đêm   |       |       |       |       |       |

Màu ký hiệu: 🟩 Đúng kế hoạch | 🟡 Chậm < 10% | 🔴 Chậm > 10% | ⬜ Ngừng máy

CHÚ THÍCH:
[SP] = Mã sản phẩm đang sản xuất
[SL] = Số lượng kế hoạch ca đó
Cập nhật thực tế mỗi ca vào ô tương ứng
```

---

## Định dạng đầu ra

Lập kế hoạch sản xuất tháng, lệnh sản xuất hoặc lịch ca sản xuất theo đặc thù nhà máy.
Kết hợp skill `xlsx` để xây dựng bảng kế hoạch sản xuất tự động tính cân đối NVL.
