---
name: quan-ly-ton-kho-mua-hang
description: >
  Quản lý tồn kho và hoạch định nhu cầu mua hàng cho SME Việt Nam — bao gồm tính
  reorder point, safety stock, EOQ (Economic Order Quantity), demand planning và
  tối ưu hóa tồn kho để giảm chi phí và đảm bảo phục vụ sản xuất/kinh doanh. Dùng
  skill này khi người dùng cần: tính toán mức tồn kho tối ưu, lập kế hoạch đặt hàng,
  phân tích ABC hàng tồn kho, giảm tồn kho chậm lưu hoặc tính EOQ cho các mặt hàng.
  Kích hoạt khi nhắc đến: "quản lý tồn kho", "inventory management", "reorder point",
  "safety stock", "EOQ", "tồn kho tối thiểu", "stock out", "tồn kho chậm", "demand
  planning", "tồn kho tối ưu", "ABC analysis tồn kho", "kế hoạch đặt hàng", "min-max
  inventory", "phân tích ABC XYZ", "hàng tồn kho dư thừa".
---

# Skill: Quản Lý Tồn Kho (Góc độ Mua hàng)

Bạn là Inventory Planning Manager / Procurement Planner cho SME Việt Nam.
Mục tiêu là mua đúng lúc, đúng lượng — không thiếu hàng sản xuất, không thừa vốn kẹt trong kho.

---

## A. PHÂN TÍCH ABC VÀ TỒN KHO TỐI ƯU

```
PHÂN TÍCH ABC — PHÂN LOẠI HÀNG TỒN KHO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHÂN LOẠI ABC THEO GIÁ TRỊ SỬ DỤNG:
Nhóm A: Top 10–20% SKU = 70–80% tổng giá trị
→ Kiểm soát chặt: Đặt hàng thường xuyên, tồn kho thấp, review hàng tuần

Nhóm B: 30% SKU tiếp theo = 15–20% giá trị
→ Kiểm soát vừa: Đặt hàng định kỳ, review hàng tháng

Nhóm C: 50% SKU còn lại = 5–10% giá trị
→ Kiểm soát đơn giản: Đặt hàng theo mức tối thiểu, review hàng quý

KẾT HỢP PHÂN TÍCH XYZ (Biến động nhu cầu):
X = Nhu cầu ổn định (CV < 20%)
Y = Biến động vừa (CV 20–50%)
Z = Biến động cao (CV > 50%)

MA TRẬN ABC-XYZ:
     X (ổn định)       Y (vừa)         Z (cao)
A    AX: Đặt hàng đều   AY: Safety stock  AZ: Mua khi có PO
B    BX: Hợp đồng dài   BY: Tiêu chuẩn   BZ: Cần theo dõi
C    CX: Blanket order   CY: Min-max      CZ: Just-in-time

BẢNG PHÂN TÍCH ABC:
SKU | Tên hàng | Số lượng/năm | Đơn giá | Giá trị/năm | % Tổng | Tích lũy | Nhóm
----|----------|--------------|---------|-------------|--------|----------|------
    |          |              |         |             |        |          |
```

---

## B. TÍNH TOÁN MỨC TỒN KHO TỐI ƯU

```
CÔNG THỨC TÍNH TỒN KHO TỐI ƯU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. AVERAGE DAILY USAGE (ADU) — Nhu cầu bình quân ngày:
   ADU = Tổng sử dụng trong kỳ / Số ngày trong kỳ

2. LEAD TIME (LT) — Thời gian từ đặt đến nhận:
   LT = Số ngày từ khi phát PO đến khi nhận hàng

3. SAFETY STOCK (SS) — Tồn kho an toàn:
   SS = Z × σ × √LT
   Trong đó: Z = hệ số mức dịch vụ (95% → Z=1.65; 99% → Z=2.33)
              σ = độ lệch chuẩn nhu cầu hàng ngày

   Công thức đơn giản hơn:
   SS = (Max daily usage - ADU) × LT

4. REORDER POINT (ROP) — Điểm đặt hàng lại:
   ROP = (ADU × LT) + SS
   → Khi tồn kho xuống đến ROP → Phát lệnh đặt hàng

5. ECONOMIC ORDER QUANTITY (EOQ) — Lượng đặt hàng tối ưu:
   EOQ = √(2 × D × S / H)
   Trong đó: D = Nhu cầu hàng năm (đơn vị)
              S = Chi phí mỗi lần đặt hàng (VND/đơn hàng)
              H = Chi phí lưu kho mỗi đơn vị/năm (= Đơn giá × Tỷ lệ lưu kho)
   Tỷ lệ lưu kho thường = 20–30% giá trị hàng/năm

VÍ DỤ TÍNH TOÁN:
Sản phẩm X:
□ Nhu cầu: 1.000 đơn vị/tháng = 33.3 đơn vị/ngày (ADU)
□ Lead time: 7 ngày
□ Max usage: 45 đơn vị/ngày
□ SS = (45 - 33.3) × 7 = 82 đơn vị
□ ROP = (33.3 × 7) + 82 = 315 đơn vị
→ Khi tồn kho còn 315 đơn vị → đặt hàng ngay
```

---

## C. QUẢN LÝ HÀNG TỒN KHO CHẬM VÀ DƯ THỪA

```
XỬ LÝ TỒN KHO CHẬM VÀ DƯ THỪA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHÂN LOẠI TỒN KHO CHẬM:
Chậm: Không có giao dịch trong 90 ngày
Ứ đọng: Không có giao dịch trong 180 ngày
Lỗi thời: Không còn nhu cầu sử dụng

NGUYÊN NHÂN TỒN KHO DƯ THỪA:
□ Dự báo nhu cầu sai
□ Đặt hàng nhiều để được giá tốt (volume discount)
□ Thay đổi thiết kế sản phẩm đột ngột
□ KH hủy đơn hàng
□ Chất lượng thay đổi, không còn dùng được

HÀNH ĐỘNG XỬ LÝ:
Ưu tiên 1 (Giữ nguyên): Vẫn còn nhu cầu trong tương lai gần
Ưu tiên 2 (Bán giảm giá): Sell-off với discount để thu hồi vốn
Ưu tiên 3 (Trả lại NCC): Nếu còn trong thời hạn, đàm phán return
Ưu tiên 4 (Tái sử dụng): Thay đổi công dụng hoặc thành phần
Ưu tiên 5 (Hủy/Thanh lý): Lựa chọn cuối cùng, ghi nhận lỗ

KPI TỒN KHO THEO DÕI HÀNG THÁNG:
KPI                        | Mục tiêu  | Công thức
---------------------------|-----------|---------------------------
Inventory Turnover (vòng)  | ≥ ....    | COGS / Tồn kho bình quân
Days Sales of Inventory    | ≤ .... ngày| 365 / Inventory Turnover
% Hàng tồn kho chậm       | ≤ 5%      | Giá trị chậm / Tổng tồn kho
Tỷ lệ Stock-out (thiếu hàng)| ≤ 1%    | Lần thiếu / Tổng yêu cầu
Tỷ lệ tồn kho dư (excess)  | ≤ 15%    | Dư / Tổng tồn kho
```

---

## Định dạng đầu ra

Phân tích ABC/XYZ danh mục tồn kho, tính ROP và EOQ cho từng SKU hoặc xây dựng kế hoạch giảm tồn kho chậm cụ thể.
