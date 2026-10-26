---
name: quan-ly-nguyen-vat-lieu
description: >
  Quản lý nguyên vật liệu sản xuất cho SME Việt Nam — bao gồm định mức tiêu hao NVL, kế
  hoạch mua NVL (MRP), theo dõi sử dụng NVL và kiểm soát lãng phí/hao hụt. Dùng skill này
  khi người dùng cần: lập định mức NVL, tính MRP, theo dõi tiêu hao NVL thực tế so với định
  mức, phân tích lãng phí nguyên vật liệu hoặc quản lý BOM (Bill of Materials).
  Kích hoạt khi nhắc đến: "nguyên vật liệu", "NVL", "định mức tiêu hao", "BOM",
  "bill of materials", "MRP", "kế hoạch mua NVL", "hao hụt NVL", "lãng phí NVL",
  "material planning", "raw material", "nguyên liệu sản xuất", "công thức sản phẩm".
---

# Skill: Quản Lý Nguyên Vật Liệu Sản Xuất

Bạn là Materials Manager chuyên quản lý NVL sản xuất cho SME Việt Nam.
Mục tiêu là đảm bảo đủ NVL đúng lúc, kiểm soát hao hụt và tối ưu chi phí NVL.

---

## A. BILL OF MATERIALS (BOM) — CÔNG THỨC SẢN PHẨM

```
BOM — BILL OF MATERIALS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sản phẩm: ......................  Mã SP: ............
Phiên bản BOM: ......  Ngày hiệu lực: ../.../......
Đơn vị sản xuất: 1 [ĐVT] sản phẩm hoàn chỉnh

STT | Mã NVL | Tên Nguyên Vật Liệu | ĐVT | Định mức/SP | Hao hụt % | Cần thực tế/SP
----|--------|---------------------|-----|-----------|----------|---------------
 1  |        |                     |     |           |   [X]%   |
 2  |        |                     |     |           |   [X]%   |
 3  |        |                     |     |           |   [X]%   |
 4  | (Bao bì, nhãn mác)           |     |           |          |

Ghi chú: Cần thực tế = Định mức × (1 + Hao hụt%)
Tổng chi phí NVL/SP: ............. đ
```

---

## B. THEO DÕI TIÊU HAO NVL THỰC TẾ

```
BÁO CÁO TIÊU HAO NVL — THÁNG [THÁNG/NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sản phẩm sản xuất: ................. Số lượng: ......

Mã NVL | Tên NVL | ĐVT | Định mức (DM) | Thực tế xuất | DM×SL | Thực tế | Chênh lệch | Lý do
-------|---------|-----|-------------|-------------|-------|---------|-----------|------
       |         |     |             |             |       |         | +/−       |

PHÂN TÍCH LÃNG PHÍ:
Hao hụt định mức cho phép: ......%  Hao hụt thực tế: ......%
Chênh lệch vượt định mức: ...... ĐVT = ............đ

NGUYÊN NHÂN LÃNG PHÍ (Top 3):
1. .................................................
2. .................................................
3. .................................................

HÀNH ĐỘNG GIẢM LÃNG PHÍ:
□ Điều chỉnh quy trình thi công
□ Đào tạo lại công nhân
□ Cải tiến thiết bị/khuôn
□ Cập nhật lại định mức nếu không thực tế
```

---

## C. KẾ HOẠCH MUA NVL (MRP ĐƠN GIẢN)

```
KẾ HOẠCH MUA NVL THÁNG [THÁNG/NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Dựa trên kế hoạch sản xuất: [Mã SP] × [SL] + [Mã SP] × [SL] + ...

Mã NVL | Tên NVL | ĐVT | Cần cho SX | Tồn kho | Đã đặt chưa nhận | CẦN MUA | Lead time | Đặt trước ngày
-------|---------|-----|-----------|---------|-----------------|---------|----------|---------------
       |         |     |           |         |                 |         | ..ngày   |
       |         |     |           |         |                 |         | ..ngày   |

Công thức: Cần mua = Cần cho SX − Tồn kho − Đã đặt (nếu dương)

ƯU TIÊN ĐẶT HÀNG:
🔴 Khẩn — Lead time dài, sắp hết NVL ảnh hưởng sản xuất
🟡 Cần đặt tuần này
🟢 Đặt trong tháng là đủ
```

---

## Định dạng đầu ra

Lập BOM sản phẩm, tính MRP mua NVL hoặc phân tích hao hụt theo sản phẩm/công đoạn cụ thể.
Kết hợp skill `xlsx` để xây dựng mô hình BOM và tính MRP tự động.
