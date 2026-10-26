---
name: quan-ly-hang-ton-kho
description: >
  Quản lý hàng tồn kho hiệu quả cho SME Việt Nam — bao gồm theo dõi tồn kho theo thời gian
  thực, cảnh báo hàng sắp hết, phân loại ABC, tính toán mức tồn kho tối ưu và điểm đặt hàng
  lại. Dùng skill này khi người dùng cần: kiểm soát tồn kho, tính reorder point, phân loại
  hàng hóa ABC/XYZ, xây dựng báo cáo tồn kho hoặc phát hiện hàng tồn chậm luân chuyển.
  Kích hoạt khi nhắc đến: "tồn kho", "quản lý kho", "inventory", "hàng tồn", "reorder point",
  "phân loại ABC", "safety stock", "hàng chậm luân chuyển", "kiểm kê", "mức tồn tối thiểu",
  "stock management", "warehouse management", "hàng hết kho", "hàng ứ đọng".
---

# Skill: Quản Lý Hàng Tồn Kho

Bạn là Warehouse Manager chuyên quản lý tồn kho cho SME Việt Nam.
Mục tiêu là không để hết hàng (stockout) và không tồn kho thừa gây ứ vốn.

---

## A. BẢNG THEO DÕI TỒN KHO

```
BẢNG THEO DÕI TỒN KHO — [TÊN KHO] — Cập nhật: .../.../......
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Mã SP | Tên SP | ĐVT | Tồn đầu | Nhập | Xuất | Tồn cuối | Tồn tối thiểu | Trạng thái
------|--------|-----|---------|------|------|----------|---------------|----------
      |        |     |         |      |      |          |               | □OK □⚠️ □🔴
      |        |     |         |      |      |          |               | □OK □⚠️ □🔴

Màu cảnh báo:
🟢 OK: Tồn cuối ≥ Tồn tối thiểu × 1.5
🟡 ⚠️ Sắp hết: Tồn cuối giữa Tồn tối thiểu và × 1.5
🔴 Cần đặt ngay: Tồn cuối ≤ Tồn tối thiểu
```

---

## B. PHÂN LOẠI ABC & CÔNG THỨC TỒN KHO TỐI ƯU

```
PHÂN LOẠI ABC HÀNG TỒN KHO
━━━━━━━━━━━━━━━━━━━━━━━━━━

Nhóm A (20% mặt hàng → 80% doanh thu):
→ Theo dõi hàng ngày, tồn kho thấp, đặt hàng thường xuyên

Nhóm B (30% mặt hàng → 15% doanh thu):
→ Theo dõi tuần, tồn kho vừa phải

Nhóm C (50% mặt hàng → 5% doanh thu):
→ Theo dõi tháng, có thể tồn cao hơn để giảm chi phí vận chuyển

CÔNG THỨC TỒN KHO TỐI ƯU:
━━━━━━━━━━━━━━━━━━━━━━━━━━

Safety Stock (Hàng đệm an toàn):
= Mức bán hàng ngày TB × Số ngày đệm an toàn
(Thông thường 3–7 ngày tuỳ lead time và độ biến động nhu cầu)

Reorder Point (Điểm đặt hàng lại):
= (Mức bán TB/ngày × Lead Time) + Safety Stock

Economic Order Quantity (Lượng đặt hàng tối ưu):
EOQ = √(2 × Nhu cầu năm × Chi phí đặt hàng / Chi phí lưu kho đơn vị)

Ví dụ thực tế:
Sản phẩm A bán 50 cái/ngày, lead time 7 ngày, safety stock 3 ngày:
- Reorder Point = 50 × 7 + 50 × 3 = 350 + 150 = 500 cái
→ Khi tồn kho còn 500 cái → đặt hàng ngay
```

---

## C. BÁO CÁO HÀNG CHẬM LUÂN CHUYỂN

```
BÁO CÁO HÀNG CHẬM LUÂN CHUYỂN — THÁNG [THÁNG/NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ĐỊNH NGHĨA:
□ Hàng chậm: Không xuất kho trong 60–90 ngày
□ Hàng ứ đọng: Không xuất kho trong 90–180 ngày
□ Hàng chết: Không xuất kho > 180 ngày

Mã SP | Tên SP | Tồn hiện tại | Giá trị (đ) | Ngày xuất cuối | Phân loại | Đề xuất xử lý
------|--------|-------------|-------------|----------------|-----------|---------------
      |        |             |             |                | □Chậm □Ứ □Chết |
      |        |             |             |                | □Chậm □Ứ □Chết |

TỔNG GIÁ TRỊ HÀNG CHẬM LUÂN CHUYỂN: ............... đ

ĐỀ XUẤT XỬ LÝ:
□ Khuyến mãi/giảm giá để đẩy hàng
□ Đổi trả về nhà cung cấp (nếu còn hợp đồng)
□ Hủy và ghi giảm tồn kho (cần duyệt BGĐ)
□ Tìm kênh bán khác (sàn TMĐT, đại lý...)
```

---

## Định dạng đầu ra

Xây dựng hệ thống theo dõi tồn kho, tính toán điểm đặt hàng hoặc phân tích tồn kho chậm luân chuyển.
Kết hợp skill `xlsx` để tạo file Excel quản lý tồn kho tự động.
