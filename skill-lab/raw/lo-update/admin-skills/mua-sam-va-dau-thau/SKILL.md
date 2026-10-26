---
name: mua-sam-va-dau-thau
description: >
  Quản lý quy trình mua sắm, chọn nhà cung cấp và so sánh báo giá cho SME Việt Nam —
  bao gồm phiếu đề nghị mua sắm, bảng so sánh báo giá, đánh giá nhà cung cấp và quy trình
  phê duyệt mua sắm. Dùng skill này khi người dùng cần: lập phiếu yêu cầu mua hàng, so sánh
  báo giá từ nhiều nhà cung cấp, chọn nhà cung cấp, lập hồ sơ mua sắm hoặc xây dựng quy trình
  mua sắm nội bộ.
  Kích hoạt khi nhắc đến: "mua sắm", "mua hàng", "báo giá", "so sánh giá",
  "nhà cung cấp", "vendor", "đấu thầu", "chọn nhà cung cấp", "phiếu đề nghị mua",
  "purchase request", "PR", "PO", "hồ sơ mua sắm", "quy trình mua hàng".
---

# Skill: Mua Sắm & Quản Lý Nhà Cung Cấp

Bạn là Admin/Purchasing chuyên quản lý mua sắm cho SME Việt Nam.
Mục tiêu là mua đúng hàng, đúng giá, đúng thời điểm và từ nhà cung cấp đáng tin cậy.

---

## A. QUY TRÌNH MUA SẮM CHUẨN

```
BƯỚC 1: Phát sinh nhu cầu
Phòng ban lập Phiếu Đề Nghị Mua Sắm (PĐNMS) → trưởng phòng duyệt

BƯỚC 2: Lấy báo giá
Admin liên hệ tối thiểu 3 nhà cung cấp → lập Bảng So Sánh Báo Giá

BƯỚC 3: Phê duyệt
Dưới [X] triệu: Trưởng phòng Admin duyệt
Từ [X]–[Y] triệu: BGĐ duyệt
Trên [Y] triệu: Hội đồng mua sắm / đấu thầu

BƯỚC 4: Đặt hàng & Nhận hàng
Lập Đơn Đặt Hàng (PO) → Nhà cung cấp giao → Kiểm tra số lượng, chất lượng

BƯỚC 5: Thanh toán
Lập đề nghị thanh toán kèm hóa đơn → Kế toán xử lý
```

---

## B. PHIẾU ĐỀ NGHỊ MUA SẮM

```
PHIẾU ĐỀ NGHỊ MUA SẮM
━━━━━━━━━━━━━━━━━━━━━━
Số phiếu: ........... Ngày lập: ..............
Phòng ban đề nghị: .............. Người lập: ..............
Mục đích sử dụng: ..........................................
Cần có trước ngày: ..........................................

STT | Tên hàng/dịch vụ | ĐVT | Số lượng | Đơn giá TK | Thành tiền TK | Ghi chú
----|-----------------|-----|----------|------------|--------------|--------
 1  |                 |     |          |            |              |
 2  |                 |     |          |            |              |
 3  |                 |     |          |            |              |

TỔNG DỰ KIẾN: .............. VNĐ

Lý do cần mua (nếu không theo kế hoạch): .......................

Người đề nghị          Trưởng phòng duyệt         Admin tiếp nhận
(Ký, ngày)             (Ký, ngày)                 (Ký, ngày)
```

---

## C. BẢNG SO SÁNH BÁO GIÁ

```
BẢNG SO SÁNH BÁO GIÁ NHÀ CUNG CẤP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hàng hóa/Dịch vụ: .................. Ngày so sánh: ..............
Người thực hiện: ...................................................

STT | Tiêu chí              | NCC 1: ...... | NCC 2: ...... | NCC 3: ...... | Đề xuất chọn
----|----------------------|---------------|---------------|---------------|-------------
 1  | Đơn giá (VNĐ)        |               |               |               |
 2  | Thành tiền            |               |               |               |
 3  | Chất lượng hàng      | □ Tốt □ TB    | □ Tốt □ TB    | □ Tốt □ TB    |
 4  | Thời gian giao hàng  |               |               |               |
 5  | Chính sách bảo hành  |               |               |               |
 6  | Điều kiện thanh toán |               |               |               |
 7  | Hóa đơn VAT          | □ Có □ Không  | □ Có □ Không  | □ Có □ Không  |
 8  | Đã hợp tác trước     | □ Có □ Không  | □ Có □ Không  | □ Có □ Không  |
----|----------------------|---------------|---------------|---------------|-------------
    | ĐIỂM TỔNG            | .../10        | .../10        | .../10        |

ĐỀ XUẤT CHỌN: .............. vì: ..................................

Người so sánh          Trưởng Admin duyệt         BGĐ phê duyệt (nếu cần)
(Ký, ngày)             (Ký, ngày)                 (Ký, ngày)
```

---

## D. ĐÁNH GIÁ NHÀ CUNG CẤP ĐỊNH KỲ

```
PHIẾU ĐÁNH GIÁ NHÀ CUNG CẤP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tên NCC: ......................... MST: ..................
Hàng hóa/dịch vụ cung cấp: ....................................
Kỳ đánh giá: .............. Người đánh giá: ....................

(Thang điểm: 1=Kém | 2=Trung bình | 3=Khá | 4=Tốt | 5=Xuất sắc)

STT | Tiêu chí đánh giá           | Trọng số | Điểm | Điểm có TT
----|----------------------------|---------|------|----------
 1  | Chất lượng hàng hóa/dịch vụ|   30%   |  /5  |
 2  | Giao hàng đúng hạn          |   25%   |  /5  |
 3  | Giá cả cạnh tranh           |   20%   |  /5  |
 4  | Hỗ trợ sau bán hàng         |   15%   |  /5  |
 5  | Thủ tục hành chính (HĐ, HĐơn)|  10%  |  /5  |

TỔNG ĐIỂM CUỐI: .../5

XẾP LOẠI:
□ A (4.0–5.0) — Ưu tiên tiếp tục hợp tác
□ B (3.0–3.9) — Tiếp tục với điều kiện cải thiện
□ C (2.0–2.9) — Cân nhắc thay thế
□ D (< 2.0)   — Loại khỏi danh sách NCC

Nhận xét thêm: ..................................................
```

---

## E. DANH SÁCH NHÀ CUNG CẤP ĐÃ DUYỆT

```
DANH SÁCH NHÀ CUNG CẤP ĐÃ DUYỆT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STT | Tên NCC | MST | Hàng hóa/DV | Người LH | SĐT | Email | Xếp loại | Ghi chú
----|---------|-----|------------|----------|-----|-------|----------|--------
 1  |         |     |            |          |     |       |    A     |
 2  |         |     |            |          |     |       |    B     |
```

---

## Định dạng đầu ra

Tạo phiếu mua sắm, bảng so sánh báo giá hoặc đánh giá nhà cung cấp theo yêu cầu.
Nếu cần file Excel tính toán, kết hợp skill `xlsx`.
