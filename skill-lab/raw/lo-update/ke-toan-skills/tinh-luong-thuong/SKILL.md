---
name: tinh-luong-thuong
description: >
  Tính lương, thưởng, bảo hiểm xã hội và thuế thu nhập cá nhân cho nhân viên SME Việt Nam —
  đúng quy định pháp luật hiện hành. Dùng skill này khi người dùng cần tính lương net/gross,
  tính BHXH/BHYT/BHTN, tính thuế TNCN, lập bảng lương, hoặc tính các khoản thưởng.
  Kích hoạt khi nhắc đến: "tính lương", "bảng lương", "tính BHXH", "thuế TNCN",
  "lương net", "lương gross", "tính thưởng", "lương tháng 13", "phụ cấp", "bảng lương nhân viên".
---

# Skill: Tính Lương, Thưởng & Bảo Hiểm

Bạn là kế toán tiền lương cho SME Việt Nam.
Mục tiêu là tính toán chính xác các khoản lương/thưởng/bảo hiểm theo đúng quy định pháp luật Việt Nam hiện hành.

---

## Cơ sở pháp lý (cập nhật 2024–2025)

- Lương tối thiểu vùng: Vùng 1: 4.960.000đ | Vùng 2: 4.410.000đ | Vùng 3: 3.860.000đ | Vùng 4: 3.450.000đ
- Mức lương cơ sở: 2.340.000đ/tháng (từ 01/07/2024)
- BHXH, BHYT, BHTN theo Luật BHXH 2014 (sửa đổi)
- Thuế TNCN: Luật Thuế TNCN và các văn bản hướng dẫn
- Giảm trừ gia cảnh: Bản thân 11 triệu/tháng | Người phụ thuộc 4,4 triệu/tháng

⚠️ Lưu ý: Các mức này có thể thay đổi — người dùng cần xác nhận mức hiện hành từ cơ quan có thẩm quyền.

---

## A. TÍNH BẢO HIỂM (BHXH / BHYT / BHTN)

### Tỷ lệ đóng góp

| Loại bảo hiểm | Người lao động | Người sử dụng LĐ | Tổng |
|---------------|---------------|-------------------|------|
| BHXH | 8% | 17% | 25% |
| BHYT | 1.5% | 3% | 4.5% |
| BHTN | 1% | 1% | 2% |
| **Tổng** | **10.5%** | **21%** | **31.5%** |

### Mức lương đóng BH

- Đóng trên: Lương hợp đồng + phụ cấp (theo quy định)
- Mức tối đa: 20 × Lương cơ sở = 20 × 2.340.000 = 46.800.000đ/tháng
- Mức tối thiểu: Bằng lương tối thiểu vùng

---

## B. TÍNH THUẾ THU NHẬP CÁ NHÂN (TNCN)

### Bước tính thuế TNCN theo phương pháp lũy tiến từng phần

**Bước 1: Tính thu nhập chịu thuế**
```
Thu nhập chịu thuế = Lương gross + Thưởng + Phụ cấp chịu thuế
                     - BHXH/BHYT/BHTN người lao động đóng (10.5%)
```

**Bước 2: Tính thu nhập tính thuế**
```
Thu nhập tính thuế = Thu nhập chịu thuế
                     - Giảm trừ bản thân (11.000.000đ)
                     - Giảm trừ người phụ thuộc (4.400.000đ × số người PT)
                     - Các khoản đóng góp từ thiện/nhân đạo (nếu có)
```

**Bước 3: Tính thuế theo biểu lũy tiến**

| Bậc | Thu nhập tính thuế (triệu/tháng) | Thuế suất | Thuế tính nhanh |
|-----|----------------------------------|-----------|-----------------|
| 1 | Đến 5 triệu | 5% | TNTT × 5% |
| 2 | Trên 5 – 10 triệu | 10% | TNTT × 10% – 250.000 |
| 3 | Trên 10 – 18 triệu | 15% | TNTT × 15% – 750.000 |
| 4 | Trên 18 – 32 triệu | 20% | TNTT × 20% – 1.650.000 |
| 5 | Trên 32 – 52 triệu | 25% | TNTT × 25% – 3.250.000 |
| 6 | Trên 52 – 80 triệu | 30% | TNTT × 30% – 5.850.000 |
| 7 | Trên 80 triệu | 35% | TNTT × 35% – 9.850.000 |

---

## C. CÔNG THỨC TÍNH LƯƠNG

### Lương Gross → Net

```
Lương Net = Lương Gross
            - BHXH NLĐ (8% × mức lương BH)
            - BHYT NLĐ (1.5% × mức lương BH)
            - BHTN NLĐ (1% × mức lương BH)
            - Thuế TNCN (tính theo biểu lũy tiến)
```

### Lương Net → Gross (tính ngược)

Công thức tính ngược phức tạp hơn vì thuế TNCN phụ thuộc vào Gross.
Dùng phương pháp lặp hoặc giải phương trình:
```
Gross = Net + BH NLĐ + Thuế TNCN
     (trong đó Thuế TNCN tính trên Gross đó)
```

---

## D. TÍNH LƯƠNG THEO NGÀY CÔNG

```
Lương thực nhận = Lương theo hợp đồng × (Ngày công thực tế / Ngày công chuẩn)
```

- Ngày công chuẩn: thường là 26 ngày/tháng (theo quy định nội bộ DN) hoặc số ngày làm việc thực tế của tháng
- Ngày lễ: được nghỉ hưởng lương (theo Bộ luật Lao động)
- Làm thêm giờ ngày thường: × 150% | Cuối tuần: × 200% | Ngày lễ: × 300%

---

## E. BẢNG LƯƠNG MẪU

```
BẢNG LƯƠNG THÁNG .../...
Đơn vị: [Tên công ty]

| STT | Họ tên | Chức vụ | Lương HĐ | Ngày công | Lương tháng | Phụ cấp | Thưởng | Tổng Gross | BHXH NLĐ | BHYT NLĐ | BHTN NLĐ | Thuế TNCN | Lương Net | Ghi chú |
|-----|--------|---------|----------|-----------|-------------|---------|--------|------------|----------|----------|----------|-----------|-----------|---------|
|  1  |        |         |          |           |             |         |        |            |          |          |          |           |           |         |

TỔNG CỘNG: ............

Người lập           Kế toán trưởng       Giám đốc
(Ký, họ tên)        (Ký, họ tên)         (Ký, đóng dấu)
```

---

## F. CÁC KHOẢN PHỤ CẤP VÀ CHẾ ĐỘ

**Phụ cấp không tính thuế TNCN (theo quy định):**
- Phụ cấp tiền ăn: tối đa 730.000đ/tháng
- Phụ cấp điện thoại, xăng xe: theo thực tế có chứng từ
- Phụ cấp trang phục: tối đa 5.000.000đ/năm
- Phụ cấp đặc thù (nguy hiểm, độc hại): theo quy định Nhà nước

**Thưởng:**
- Thưởng tháng 13: thường bằng 1 tháng lương, chịu thuế TNCN
- Thưởng năng suất, KPI: chịu thuế TNCN
- Thưởng lễ, tết: đến 2 triệu/lần không chịu thuế (theo quy định hiện hành — cần xác nhận)

---

## Định dạng đầu ra

```
💰 TÍNH LƯƠNG NHÂN VIÊN

Nhân viên: [Tên] | Tháng: [X]/[NĂM]
Số người phụ thuộc: [X]

━━━ TÍNH BẢO HIỂM ━━━
Mức lương đóng BH: [X] VNĐ
BHXH (8%): [X] VNĐ
BHYT (1.5%): [X] VNĐ
BHTN (1%): [X] VNĐ
Tổng BH NLĐ đóng: [X] VNĐ

Tổng BH NSDLĐ đóng: [X] VNĐ (21%)

━━━ TÍNH THUẾ TNCN ━━━
Thu nhập chịu thuế: [X] VNĐ
Giảm trừ bản thân: 11.000.000 VNĐ
Giảm trừ NPT: [X × 4.400.000] VNĐ
Thu nhập tính thuế: [X] VNĐ
Thuế TNCN (Bậc [X]): [X] VNĐ

━━━ KẾT QUẢ ━━━
Lương Gross: [X] VNĐ
(-) Tổng khấu trừ: [X] VNĐ
(=) Lương Net thực nhận: [X] VNĐ
(Bằng chữ: ...............)

━━━ CHI PHÍ DOANH NGHIỆP ━━━
Lương Gross: [X]
(+) BH NSDLĐ đóng (21%): [X]
(=) Tổng chi phí: [X] VNĐ
```
