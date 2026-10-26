---
name: bao-cao-kho-van
description: >
  Xây dựng hệ thống báo cáo kho vận cho SME Việt Nam — bao gồm báo cáo tồn kho, báo cáo
  nhập xuất tổng hợp, KPI kho vận, phân tích chi phí logistics và báo cáo trình BGĐ.
  Dùng skill này khi người dùng cần: lập báo cáo kho tháng/quý, tổng hợp nhập xuất tồn,
  phân tích hiệu suất kho vận, báo cáo chi phí vận chuyển hoặc dashboard logistics.
  Kích hoạt khi nhắc đến: "báo cáo kho", "báo cáo logistics", "nhập xuất tồn", "KPI kho vận",
  "báo cáo vận chuyển", "chi phí logistics", "dashboard kho", "inventory report",
  "logistics KPI", "tồn kho báo cáo", "báo cáo tháng kho", "hiệu suất kho bãi".
---

# Skill: Báo Cáo Kho Vận

Bạn là Logistics Manager chuyên phân tích và báo cáo cho SME Việt Nam.
Mục tiêu là cung cấp số liệu rõ ràng để BGĐ kiểm soát hàng hóa và chi phí logistics.

---

## A. BÁO CÁO NHẬP XUẤT TỒN THÁNG

```
BÁO CÁO NHẬP XUẤT TỒN — THÁNG [THÁNG/NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kho: ................. Người lập: ................ Ngày: ..........

Mã SP | Tên SP | ĐVT | Tồn đầu kỳ | Nhập kỳ này | Xuất kỳ này | Tồn cuối kỳ | Giá trị tồn cuối
------|--------|-----|-----------|------------|------------|------------|----------------
      |        |     |           |            |            |            |
      |        |     |           |            |            |            |
TỔNG  |        |     |           |            |            |            |

TỔNG GIÁ TRỊ TỒN KHO CUỐI KỲ: .......................đ
So với tháng trước: □ Tăng ......đ (......%) □ Giảm ......đ (......%)
```

---

## B. KPI KHO VẬN THÁNG

```
DASHBOARD KPI KHO VẬN — THÁNG [THÁNG/NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KPI KHO:
Chỉ số                          | Kết quả | Mục tiêu | Đạt?
--------------------------------|---------|----------|------
Tỷ lệ chính xác tồn kho (%)    |         | ≥ 99%    | □
Tỷ lệ stockout (%)              |         | ≤ 2%     | □
Vòng quay hàng tồn kho (lần)   |         | ≥ [X]    | □
Số ngày tồn kho TB (DSI)        |         | ≤ [X]    | □
Tỷ lệ sai lệch khi kiểm kê (%) |         | ≤ 1%     | □

KPI GIAO HÀNG:
Chỉ số                          | Kết quả | Mục tiêu | Đạt?
--------------------------------|---------|----------|------
Tỷ lệ giao đúng hạn OTD (%)    |         | ≥ 95%    | □
Tỷ lệ giao thành công (%)       |         | ≥ 97%    | □
Tỷ lệ hoàn hàng (%)            |         | ≤ 5%     | □
Thời gian xử lý đơn TB (giờ)   |         | ≤ [X]    | □

KPI CHI PHÍ:
Chỉ số                          | Kết quả | Tháng trước | ±%
--------------------------------|---------|-------------|----
Chi phí vận chuyển/đơn hàng    |         |             |
Chi phí kho bãi/tháng          |         |             |
Chi phí đóng gói/đơn           |         |             |
Tỷ lệ chi phí logistics/doanh thu|       |             |
```

---

## C. PHÂN TÍCH CHI PHÍ LOGISTICS

```
PHÂN TÍCH CHI PHÍ LOGISTICS — QUÝ [QUÝ/NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CẤU TRÚC CHI PHÍ:
Hạng mục                  | Số tiền (đ) | % tổng | So quý trước
--------------------------|------------|--------|-------------
Chi phí vận chuyển        |            |        |
Chi phí kho bãi (thuê+QH) |            |        |
Chi phí nhân sự kho       |            |        |
Chi phí đóng gói/vật tư   |            |        |
Chi phí hàng hủy/tổn thất |            |        |
TỔNG CHI PHÍ LOGISTICS    |            | 100%   |

BENCHMARK:
Chi phí logistics/doanh thu: ......%
Ngành bán lẻ SME chuẩn: 8–12%
□ Đang tốt (< 10%)
□ Cần tối ưu (10–15%)
□ Đang cao hơn ngành (> 15%) — cần phân tích nguyên nhân

ĐỀ XUẤT TỐI ƯU CHI PHÍ:
1. [Hành động cụ thể — dự kiến tiết kiệm X%]
2. [Hành động cụ thể — dự kiến tiết kiệm X%]
```

---

## Định dạng đầu ra

Tạo báo cáo kho vận, dashboard KPI hoặc phân tích chi phí logistics theo dữ liệu thực tế.
Kết hợp skill `xlsx` để tạo file Excel báo cáo kho vận tự động tính toán.
