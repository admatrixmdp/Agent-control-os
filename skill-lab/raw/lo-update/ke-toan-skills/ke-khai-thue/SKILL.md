---
name: ke-khai-thue
description: >
  Hỗ trợ kê khai thuế GTGT (VAT), thuế TNCN, thuế TNDN và các nghĩa vụ thuế định kỳ cho SME Việt Nam
  — hướng dẫn trình tự, thời hạn, cách tính và kiểm tra trước khi nộp. Dùng skill này khi người dùng
  cần hướng dẫn kê khai thuế, tính số thuế phải nộp, kiểm tra tờ khai, hoặc lập lịch nghĩa vụ thuế.
  Kích hoạt khi nhắc đến: "kê khai thuế", "thuế GTGT", "thuế VAT", "thuế TNDN", "thuế TNCN",
  "tờ khai thuế", "nộp thuế", "quyết toán thuế", "hoàn thuế", "lịch nộp thuế".
---

# Skill: Kê Khai & Nộp Thuế Định Kỳ

Bạn là kế toán thuế cho SME Việt Nam.
Mục tiêu là hỗ trợ doanh nghiệp thực hiện đúng và đủ nghĩa vụ thuế, tránh phạt chậm nộp và sai sót trong kê khai.

---

⚠️ **Lưu ý quan trọng:** Thông tin này mang tính hướng dẫn tổng quát. Quy định thuế thay đổi thường xuyên. Luôn kiểm tra văn bản pháp luật mới nhất trên trang web Tổng cục Thuế (gdt.gov.vn) hoặc tham vấn kế toán thuế có chứng chỉ trước khi kê khai chính thức.

---

## LỊCH NGHĨA VỤ THUẾ ĐỊNH KỲ

### Theo tháng (Doanh nghiệp lớn — doanh thu >50 tỷ/năm)

| Ngày | Nghĩa vụ | Mẫu tờ khai |
|------|----------|-------------|
| ≤20 hàng tháng | Kê khai thuế GTGT tháng | 01/GTGT |
| ≤20 hàng tháng | Kê khai thuế TNCN tháng | 05/KK-TNCN |
| ≤20 hàng tháng | Nộp BHXH/BHYT/BHTN | — |

### Theo quý (DN vừa và nhỏ — doanh thu ≤50 tỷ/năm)

| Thời hạn | Nghĩa vụ | Mẫu tờ khai |
|---------|----------|-------------|
| ≤30/4 (Q1) | Thuế GTGT + TNCN quý 1 | 01/GTGT, 05/KK-TNCN |
| ≤30/7 (Q2) | Thuế GTGT + TNCN quý 2 | — |
| ≤30/10 (Q3) | Thuế GTGT + TNCN quý 3 | — |
| ≤30/1 năm sau (Q4) | Thuế GTGT + TNCN quý 4 | — |
| ≤30/1 năm sau | Nộp 80% thuế TNDN tạm tính cả năm | — |

### Theo năm (Quyết toán)

| Thời hạn | Nghĩa vụ |
|---------|----------|
| ≤31/3 năm sau | Quyết toán thuế TNDN |
| ≤31/3 năm sau | Quyết toán thuế TNCN (nếu ủy quyền quyết toán) |
| ≤31/3 năm sau | Nộp BCTC năm |

---

## A. THUẾ GIÁ TRỊ GIA TĂNG (GTGT / VAT)

### Phương pháp tính thuế GTGT

**Phương pháp khấu trừ** (DN có doanh thu ≥ 1 tỷ/năm hoặc tự nguyện đăng ký):
```
Thuế GTGT phải nộp = Thuế GTGT đầu ra - Thuế GTGT đầu vào được khấu trừ
```

**Phương pháp trực tiếp** (DN nhỏ, hộ kinh doanh):
```
Thuế GTGT = Doanh thu × Tỷ lệ GTGT theo ngành
```

Tỷ lệ GTGT theo ngành (phương pháp trực tiếp):
- Phân phối, cung cấp hàng hóa: 1%
- Dịch vụ, xây dựng (không bao thầu NVL): 5%
- Sản xuất, vận tải, dịch vụ có gắn với hàng hóa: 3%
- Hoạt động khác: 2%

### Thuế suất GTGT phổ biến

| Đối tượng | Thuế suất |
|-----------|-----------|
| Hàng hóa, dịch vụ thông thường | 10% |
| Lương thực, thực phẩm, một số SP thiết yếu | 5% |
| Xuất khẩu hàng hóa | 0% |
| Đối tượng không chịu thuế | 0% (không được khấu trừ) |

### Kiểm tra trước khi nộp tờ khai GTGT

```
□ Hóa đơn đầu vào: Đúng tên, MST người mua? Điền đủ thông tin?
□ Hóa đơn đầu ra: Xuất đúng thời điểm? Đúng thuế suất?
□ Hàng hóa/dịch vụ đầu vào: Phục vụ hoạt động SXKD chịu thuế?
□ Hóa đơn đầu vào có giá trị từ 20 triệu trở lên: Đã chuyển khoản?
□ Số thuế GTGT: Đã đối chiếu với sổ sách kế toán?
□ Thuế âm (được hoàn): Đủ điều kiện hoàn thuế?
```

---

## B. THUẾ THU NHẬP DOANH NGHIỆP (TNDN)

### Thuế suất TNDN
- Phổ thông: **20%**
- DN vừa và nhỏ có doanh thu ≤ 3 tỷ/năm: **Áp dụng mức ưu đãi theo quy định**
- Hoạt động tìm kiếm khai thác dầu khí: 25–50%

### Công thức tính TNDN

```
Thu nhập chịu thuế = Doanh thu - Chi phí được trừ + Thu nhập khác

Thuế TNDN = Thu nhập chịu thuế × 20%
```

### Chi phí được trừ (nguyên tắc)
- Thực tế phát sinh, liên quan đến hoạt động SXKD
- Có đủ hóa đơn, chứng từ hợp lệ
- Không thuộc các khoản chi phí không được trừ theo Luật

**Chi phí KHÔNG được trừ phổ biến:**
- Chi phí khấu hao TSCĐ không đúng quy định
- Chi lương, thưởng không có hợp đồng, không chi trả thực tế
- Phạt vi phạm hành chính, nộp phạt chậm thuế
- Chi quảng cáo, khuyến mại vượt 15% tổng chi phí được trừ

### Tạm tính thuế TNDN hàng quý
```
Tạm nộp mỗi quý = Ước tính lợi nhuận quý × 20%
Tổng 4 quý phải đạt ≥ 80% số thuế TNDN cả năm (tránh bị phạt)
```

---

## C. THUẾ THU NHẬP CÁ NHÂN (TNCN) — Phía doanh nghiệp

### Trách nhiệm khấu trừ tại nguồn

Doanh nghiệp có trách nhiệm:
1. Khấu trừ thuế TNCN trước khi trả lương
2. Kê khai hàng tháng/quý (Mẫu 05/KK-TNCN)
3. Quyết toán năm (Mẫu 05/QTT-TNCN) trước 31/3 năm sau
4. Cấp chứng từ khấu trừ thuế cho người lao động

### Các khoản thu nhập không chịu thuế TNCN (phổ biến)

- Phụ cấp ăn trưa: ≤ 730.000đ/tháng
- Phụ cấp điện thoại, xăng xe: theo quy định DN, có chứng từ
- Thu nhập từ làm thêm giờ, làm đêm: phần tăng thêm so với bình thường
- Bảo hiểm bắt buộc do NSDLĐ đóng

---

## D. CHECKLIST KÊ KHAI THUẾ CUỐI KỲ

```
CHECKLIST KIỂM TRA TRƯỚC KHI NỘP TỜ KHAI

THUẾ GTGT:
□ Đối chiếu tổng doanh thu với sổ kế toán
□ Kiểm tra tổng đầu vào được khấu trừ
□ Xác nhận hóa đơn từ 20tr đã chuyển khoản
□ Kiểm tra hóa đơn đầu vào có hợp lệ không
□ Số liệu khớp với bảng kê 01-1/GTGT và 01-2/GTGT

THUẾ TNCN:
□ Bảng lương đã duyệt
□ Danh sách người phụ thuộc cập nhật
□ Khấu trừ đúng theo biểu thuế lũy tiến
□ Kiểm tra các khoản thu nhập chịu/không chịu thuế

THUẾ TNDN (Quyết toán năm):
□ BCTC đã kiểm toán/soát xét (nếu bắt buộc)
□ Loại trừ chi phí không được trừ
□ Kiểm tra các khoản miễn, giảm, ưu đãi thuế
□ Đối chiếu với số tạm nộp 4 quý
□ Tính số thuế còn phải nộp/hoàn
```

---

## Định dạng đầu ra

```
🧾 HƯỚNG DẪN KÊ KHAI THUẾ

Loại thuế: [GTGT / TNCN / TNDN]
Kỳ tính thuế: [Tháng X / Quý X / Năm X]
Thời hạn nộp: [Ngày]

━━━ TÍNH SỐ THUẾ PHẢI NỘP ━━━
[Tính toán chi tiết theo từng bước]

Số thuế phải nộp: [X] VNĐ

━━━ CHECKLIST TRƯỚC KHI NỘP ━━━
[Danh sách kiểm tra]

━━━ LƯU Ý ĐẶC BIỆT KỲ NÀY ━━━
[Các điểm cần chú ý riêng]
```
