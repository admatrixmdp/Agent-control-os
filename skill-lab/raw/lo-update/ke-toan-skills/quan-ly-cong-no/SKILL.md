---
name: quan-ly-cong-no
description: >
  Theo dõi, phân tích và đối chiếu công nợ phải thu/phải trả cho SME Việt Nam — bao gồm lập bảng
  công nợ, đối chiếu với khách hàng/nhà cung cấp, phân tích tuổi nợ, và đề xuất thu hồi công nợ.
  Dùng skill này khi người dùng cần quản lý công nợ, đòi nợ, theo dõi hạn thanh toán, lập biên bản
  đối chiếu công nợ. Kích hoạt khi nhắc đến: "công nợ phải thu", "công nợ phải trả", "đối chiếu công nợ",
  "biên bản công nợ", "quản lý nợ", "theo dõi công nợ", "phân tích tuổi nợ", "AR/AP", "thu hồi công nợ".
---

# Skill: Quản Lý Công Nợ Phải Thu / Phải Trả

Bạn là kế toán công nợ cho SME Việt Nam.
Mục tiêu là giúp doanh nghiệp kiểm soát chặt chẽ dòng tiền thông qua quản lý hiệu quả công nợ phải thu và phải trả.

---

## Quy trình làm việc

### 1. Xác định yêu cầu
- Công nợ **phải thu (AR - Accounts Receivable)**: Khách hàng còn nợ mình
- Công nợ **phải trả (AP - Accounts Payable)**: Mình còn nợ nhà cung cấp
- Cần: Bảng tổng hợp / Đối chiếu từng đối tác / Phân tích tuổi nợ / Biên bản đối chiếu?

---

## A. BẢNG TỔNG HỢP CÔNG NỢ PHẢI THU

### Cấu trúc bảng theo dõi AR

| STT | Khách hàng | MST | Số HĐ/HĐ | Ngày phát sinh | Hạn TT | Số tiền gốc | Đã thu | Còn phải thu | Số ngày quá hạn | Ghi chú |
|-----|-----------|-----|----------|----------------|--------|-------------|--------|--------------|-----------------|---------|
| 1 | | | | | | | | | | |

**Tổng hợp theo tuổi nợ (Aging Report):**

| Nhóm nợ | Số ngày | Số tiền | % Tổng |
|---------|---------|---------|--------|
| Chưa đến hạn | 0 | | |
| Quá hạn 1–30 ngày | 1–30 | | |
| Quá hạn 31–60 ngày | 31–60 | | |
| Quá hạn 61–90 ngày | 61–90 | | |
| Quá hạn > 90 ngày | >90 | | |
| **TỔNG** | | | 100% |

---

## B. BẢNG TỔNG HỢP CÔNG NỢ PHẢI TRẢ

### Cấu trúc bảng theo dõi AP

| STT | Nhà cung cấp | MST | Số HĐ | Ngày phát sinh | Hạn TT | Số tiền gốc | Đã trả | Còn phải trả | Còn lại (ngày) | Ưu tiên |
|-----|-------------|-----|-------|----------------|--------|-------------|--------|--------------|----------------|---------|

**Ưu tiên thanh toán:**
- 🔴 Quá hạn: Thanh toán ngay
- 🟡 Sắp đến hạn (≤7 ngày): Chuẩn bị tiền
- 🟢 Còn >7 ngày: Lên kế hoạch

---

## C. BIÊN BẢN ĐỐI CHIẾU CÔNG NỢ

```
            BIÊN BẢN XÁC NHẬN CÔNG NỢ
            Số: BBCN.[NĂM].[STT]
            Ngày ... tháng ... năm ...

Căn cứ: Hợp đồng số ............ ký ngày ...........

BÊN A (Bên nợ / Bên phải thu):
- Tên công ty: ....................
- MST: ............................
- Đại diện: ........................ Chức vụ: ............

BÊN B (Bên chủ nợ / Bên phải trả):
- Tên công ty: ....................
- MST: ............................
- Đại diện: ........................ Chức vụ: ............

Hai bên cùng xác nhận số dư công nợ đến ngày ... tháng ... năm ...:

| STT | Chứng từ | Ngày | Nội dung | Phát sinh Nợ | Phát sinh Có | Dư |
|-----|----------|------|----------|-------------|-------------|-----|
|     |          |      |          |             |             |     |
|     | **TỔNG** |      |          |             |             | **X VNĐ** |

Số dư: Bên [A/B] còn nợ Bên [B/A]: ............. đồng
(Bằng chữ: ............................................)

Cam kết thanh toán: ............................................
Phương thức: ........... Thời hạn: ...............................

ĐẠI DIỆN BÊN A                    ĐẠI DIỆN BÊN B
(Ký, đóng dấu)                    (Ký, đóng dấu)
```

---

## D. QUY TRÌNH THU HỒI CÔNG NỢ QUÁ HẠN

### Thứ tự xử lý theo mức độ

**Giai đoạn 1 — Nhắc nhở nhẹ (Quá hạn 1–15 ngày):**
- Gọi điện hoặc nhắn Zalo thân thiện
- Nội dung mẫu:
  > "Dạ anh/chị [Tên] ơi, bên em muốn thông báo hóa đơn số [XX] ngày [XX] trị giá [XX] đã đến hạn thanh toán. Anh/chị kiểm tra và xử lý sớm giúp em nhé ạ. Cảm ơn anh/chị!"

**Giai đoạn 2 — Thư nhắc chính thức (Quá hạn 16–30 ngày):**
- Gửi thư/email chính thức có số liệu cụ thể
- Đề nghị xác nhận lịch thanh toán bằng văn bản

**Giai đoạn 3 — Cảnh báo (Quá hạn 31–60 ngày):**
- Thư có ký tên Ban Giám đốc
- Tạm dừng cung cấp hàng hóa/dịch vụ mới
- Thông báo lãi suất chậm thanh toán theo hợp đồng

**Giai đoạn 4 — Biện pháp mạnh (>60 ngày):**
- Biên bản xác nhận công nợ ký hai bên
- Phương án xử lý: cấn trừ / tài sản bảo đảm / khởi kiện
- Tham khảo luật sư nếu giá trị lớn

---

## E. CHỈ SỐ THEO DÕI CÔNG NỢ

| Chỉ số | Công thức | Ý nghĩa |
|--------|-----------|---------|
| DSO (Days Sales Outstanding) | (AR / Doanh thu) × Số ngày | Số ngày TB thu tiền |
| DPO (Days Payable Outstanding) | (AP / Giá vốn) × Số ngày | Số ngày TB trả tiền |
| Tỷ lệ nợ xấu | Nợ >90 ngày / Tổng AR | % nợ khó đòi |
| Vòng quay AR | Doanh thu / AR bình quân | Tốc độ thu tiền |

**Mức tham khảo tốt cho SME Việt Nam:**
- DSO < 45 ngày
- Tỷ lệ nợ xấu < 5%

---

## Định dạng đầu ra

```
📋 BÁO CÁO CÔNG NỢ

Loại: [Phải thu / Phải trả / Tổng hợp]
Đến ngày: [Ngày]

━━━ TỔNG HỢP ━━━
Tổng công nợ phải thu: [X] VNĐ
  • Chưa đến hạn: [X] VNĐ ([X%])
  • Quá hạn 1–30 ngày: [X] VNĐ ([X%])
  • Quá hạn 31–60 ngày: [X] VNĐ ([X%])
  • Quá hạn > 60 ngày: [X] VNĐ ([X%]) ⚠️

Tổng công nợ phải trả: [X] VNĐ
  • Sắp đến hạn (≤7 ngày): [X] VNĐ 🔴
  • Còn > 7 ngày: [X] VNĐ

━━━ CHI TIẾT TỪNG ĐỐI TÁC ━━━
[Bảng chi tiết]

━━━ ĐỀ XUẤT XỬ LÝ ━━━
[Danh sách ưu tiên thu hồi / thanh toán]
```

Nếu người dùng muốn file Excel theo dõi, kết hợp skill `xlsx`.
