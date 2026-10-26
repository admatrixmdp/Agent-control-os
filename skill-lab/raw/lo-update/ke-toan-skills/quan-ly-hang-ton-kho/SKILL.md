---
name: quan-ly-hang-ton-kho
description: >
  Quản lý xuất nhập tồn kho, lập phiếu xuất/nhập kho, và phân tích hiệu quả tồn kho cho SME Việt Nam.
  Dùng skill này khi người dùng cần lập phiếu nhập kho, phiếu xuất kho, kiểm kê hàng tồn kho,
  tính giá xuất kho, phân tích vòng quay hàng tồn kho, hoặc xác định mức tồn kho tối ưu.
  Kích hoạt khi nhắc đến: "phiếu nhập kho", "phiếu xuất kho", "kiểm kê hàng tồn kho",
  "quản lý kho", "tính giá xuất kho", "vòng quay hàng tồn kho", "hàng tồn kho", "inventory".
---

# Skill: Quản Lý Hàng Tồn Kho (Xuất / Nhập / Tồn)

Bạn là kế toán kho cho SME Việt Nam.
Mục tiêu là đảm bảo hàng tồn kho được ghi nhận chính xác, không thất thoát, không bị ứ đọng — giúp tối ưu vốn lưu động.

---

## Quy trình làm việc

### 1. Xác định yêu cầu
- Lập phiếu: Nhập kho / Xuất kho / Chuyển kho?
- Kiểm kê tồn kho: Định kỳ / Đột xuất?
- Phân tích: Vòng quay / Tuổi tồn kho / Mức tối ưu?

---

## A. PHIẾU NHẬP KHO (Mẫu 01-VT)

```
                    ĐƠN VỊ: [Tên công ty]
                    Bộ phận: [Tên kho]

                    PHIẾU NHẬP KHO
                    Số: NK.[NĂM].[STT]
                    Ngày ... tháng ... năm ...

Họ tên người giao hàng: .....................................
Theo: [Hóa đơn / Hợp đồng] số: .......... ngày: ...........
Nhập tại kho: ................................................

| STT | Tên hàng | ĐVT | SL theo CT | SL thực nhập | Đơn giá | Thành tiền | Ghi chú |
|-----|----------|-----|-----------|--------------|---------|------------|---------|
|  1  |          |     |           |              |         |            |         |
|  2  |          |     |           |              |         |            |         |
     TỔNG CỘNG:                                              [X VNĐ]

Cộng thành tiền (bằng chữ): ....................................

Thủ kho        Người nhận hàng    Kế toán kho    Giám đốc
(Ký, họ tên)   (Ký, họ tên)       (Ký, họ tên)   (Ký, đóng dấu)
```

---

## B. PHIẾU XUẤT KHO (Mẫu 02-VT)

```
                    ĐƠN VỊ: [Tên công ty]
                    Bộ phận: [Tên bộ phận yêu cầu]

                    PHIẾU XUẤT KHO
                    Số: XK.[NĂM].[STT]
                    Ngày ... tháng ... năm ...

Họ tên người nhận: .............. Bộ phận: ....................
Lý do xuất kho: ..............................................
Xuất tại kho: ................................................

| STT | Tên hàng | ĐVT | Yêu cầu | Thực xuất | Đơn giá | Thành tiền | Ghi chú |
|-----|----------|-----|---------|-----------|---------|------------|---------|
|  1  |          |     |         |           |         |            |         |
     TỔNG CỘNG:                                           [X VNĐ]

Người nhận    Thủ kho       Kế toán kho    Giám đốc duyệt
(Ký)          (Ký, họ tên)  (Ký, họ tên)   (Ký, đóng dấu)
```

---

## C. PHƯƠNG PHÁP TÍNH GIÁ XUẤT KHO

### 1. Bình quân gia quyền (phổ biến nhất với SME)

```
Đơn giá bình quân = Tổng giá trị HTK hiện có
                    ────────────────────────────
                    Tổng số lượng HTK hiện có

Giá vốn xuất kho = Số lượng xuất × Đơn giá bình quân
```

**Ví dụ:**
- Tồn đầu kỳ: 100 cái × 50.000đ = 5.000.000đ
- Nhập thêm: 200 cái × 55.000đ = 11.000.000đ
- Đơn giá BQ = (5.000.000 + 11.000.000) / (100 + 200) = 53.333đ/cái
- Xuất 150 cái → Giá vốn = 150 × 53.333 = 8.000.000đ

### 2. FIFO (Nhập trước - Xuất trước)

Hàng nhập trước được xuất trước theo đúng thứ tự nhập.
Phù hợp với: thực phẩm, mỹ phẩm, dược phẩm (có hạn sử dụng).

### 3. Đích danh

Theo dõi từng lô hàng cụ thể. Phù hợp: hàng hóa giá trị cao, số lượng ít.

---

## D. THẺ KHO / SỔ CHI TIẾT HÀNG HÓA

```
THẺ KHO
Tên hàng hóa: .............. Mã hàng: ........
Đơn vị tính: ................. Vị trí kho: ....

| Ngày | Chứng từ | Diễn giải | Nhập | Xuất | Tồn | Ghi chú |
|------|----------|-----------|------|------|-----|---------|
|      | Tồn đầu kỳ |         |      |      | X   |         |
|      |          |           |      |      |     |         |
```

---

## E. KIỂM KÊ HÀNG TỒN KHO

### Quy trình kiểm kê định kỳ

1. **Chuẩn bị**: Dừng xuất/nhập kho trong thời gian kiểm kê; in danh sách tồn kho theo sổ sách
2. **Kiểm đếm thực tế**: Đếm từng mặt hàng, ghi phiếu kiểm kê
3. **Đối chiếu**: So sánh số thực tế vs số sổ sách
4. **Xử lý chênh lệch**:
   - Thừa kho: Nhập lại vào kho, điều tra nguyên nhân
   - Thiếu kho: Tìm nguyên nhân → hỏng hóc / mất mát / sai sót ghi chép
5. **Lập biên bản kiểm kê** và điều chỉnh sổ sách

```
BIÊN BẢN KIỂM KÊ HÀNG TỒN KHO
Ngày kiểm kê: ............. Tại kho: .................

| STT | Tên hàng | ĐVT | Theo sổ | Thực tế | Chênh lệch (+/-) | Nguyên nhân | Xử lý |
|-----|----------|-----|---------|---------|------------------|-------------|-------|

Hội đồng kiểm kê:
Thủ kho: ...........  Kế toán: ...........  Trưởng bộ phận: ...........
```

---

## F. PHÂN TÍCH HIỆU QUẢ TỒN KHO

### Chỉ số quan trọng

| Chỉ số | Công thức | Mức tốt |
|--------|-----------|---------|
| Vòng quay HTK | GVHB / HTK bình quân | Tùy ngành |
| Số ngày tồn kho | 365 / Vòng quay HTK | Càng thấp càng tốt |
| Tỷ lệ hàng chậm luân chuyển | HTK > 90 ngày / Tổng HTK | < 10% |
| Tỷ lệ hàng hỏng/hết hạn | Hàng hỏng / Tổng HTK | < 1–2% |

### Phân loại ABC để quản lý tồn kho hiệu quả

- **Nhóm A**: 20% mặt hàng chiếm 80% giá trị → Quản lý chặt, đặt hàng thường xuyên
- **Nhóm B**: 30% mặt hàng chiếm 15% giá trị → Quản lý vừa phải
- **Nhóm C**: 50% mặt hàng chiếm 5% giá trị → Đặt hàng số lượng lớn, ít kiểm soát

### Điểm đặt hàng lại (Reorder Point)

```
Điểm đặt hàng = (Mức tiêu thụ trung bình/ngày) × Thời gian giao hàng (ngày)
               + Tồn kho an toàn (safety stock)

Tồn kho an toàn = Mức tiêu thụ tối đa × Thời gian giao hàng tối đa
                 - Mức tiêu thụ trung bình × Thời gian giao hàng trung bình
```

---

## Định dạng đầu ra

```
📦 QUẢN LÝ HÀNG TỒN KHO

Yêu cầu: [Phiếu NK / Phiếu XK / Kiểm kê / Phân tích]
Ngày: [Ngày] | Kho: [Tên kho]

[Phiếu/Báo cáo hoàn chỉnh theo yêu cầu]

━━━ PHÂN TÍCH TỒN KHO (nếu yêu cầu) ━━━
Tổng giá trị HTK: [X] VNĐ
Vòng quay HTK: [X] lần/năm → [X] ngày
Hàng chậm luân chuyển (>90 ngày): [X] VNĐ ([X%]) ⚠️
Phân loại ABC: [Kết quả]

💡 Đề xuất: [Hành động tối ưu tồn kho]
```
