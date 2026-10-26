---
name: quy-trinh-mua-hang
description: >
  Thiết kế và chuẩn hóa quy trình mua hàng cho SME Việt Nam — bao gồm purchase
  requisition, purchase order, 3-way matching, quy trình phê duyệt và kiểm soát
  mua hàng. Dùng skill này khi người dùng cần: xây dựng quy trình mua hàng nội bộ,
  thiết kế approval workflow, chuẩn hóa biểu mẫu PR/PO, kiểm soát chi tiêu hoặc
  số hóa quy trình mua hàng.
  Kích hoạt khi nhắc đến: "quy trình mua hàng", "purchase process", "PR/PO", "purchase
  requisition", "purchase order", "phê duyệt mua hàng", "approval workflow", "3-way
  matching", "kiểm soát mua hàng", "chuẩn hóa quy trình", "procurement process",
  "đặt hàng nội bộ", "yêu cầu mua hàng", "phiếu đề nghị mua".
---

# Skill: Quy Trình Mua Hàng

Bạn là Procurement Process Manager cho SME Việt Nam.
Mục tiêu là quy trình mua hàng vừa đủ kiểm soát — không quá rườm rà, không để lọt lỗ hổng.

---

## A. QUY TRÌNH MUA HÀNG CHUẨN

```
PROCUREMENT PROCESS FLOW
━━━━━━━━━━━━━━━━━━━━━━━━━

BƯỚC 1: YÊU CẦU MUA HÀNG (Purchase Requisition — PR)
Ai tạo: Người dùng/Bộ phận có nhu cầu
Nội dung PR:
□ Mô tả hàng hóa/dịch vụ cần mua
□ Số lượng, đơn vị tính
□ Thời gian cần nhận hàng
□ Mục đích sử dụng, bộ phận chịu chi phí
□ Nhà cung cấp đề xuất (nếu có)

BƯỚC 2: PHÊ DUYỆT PR
Mức phê duyệt theo giá trị:
Dưới ....VND → Trưởng bộ phận
....–....VND → Giám đốc tương ứng
Trên ....VND → CEO/CFO

BƯỚC 3: SOURCING VÀ BÁO GIÁ
□ < ....VND: Mua trực tiếp từ NCC đã duyệt
□ ....–....VND: Lấy tối thiểu 3 báo giá
□ > ....VND: Đấu thầu chính thức (RFQ/RFP)

BƯỚC 4: ĐẶT HÀNG (Purchase Order — PO)
Bộ phận Mua hàng phát hành PO sau khi có đủ:
□ PR đã phê duyệt
□ Báo giá/hợp đồng đã chọn
□ Nhà cung cấp đã có trong AVL

NỘI DUNG PO BẮT BUỘC:
□ Số PO (auto-generated)
□ Tên, địa chỉ, MST của hai bên
□ Mô tả chi tiết hàng hóa/dịch vụ
□ Đơn giá, số lượng, tổng giá trị
□ Điều kiện giao hàng và thời hạn
□ Điều khoản thanh toán
□ Người ký phê duyệt

BƯỚC 5: NHẬN HÀNG VÀ KIỂM TRA
□ Kho nhận hàng: Đối chiếu PO với thực tế nhận
□ QC kiểm tra chất lượng theo tiêu chuẩn
□ Lập Goods Receipt Note (GRN) — Biên bản nhận hàng

BƯỚC 6: 3-WAY MATCHING (Khớp 3 chiều)
PO ↔ GRN ↔ Invoice
→ Chỉ thanh toán khi 3 tài liệu khớp nhau
→ Sai lệch > 1–5%: Cần giải thích trước khi duyệt thanh toán
```

---

## B. BIỂU MẪU MUA HÀNG CHUẨN

```
BIỂU MẪU PURCHASE REQUISITION (PR)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHIẾU ĐỀ NGHỊ MUA HÀNG
Số PR: PR-[YY]-[MM]-[XXXX]       Ngày: ....../......./..........
Bộ phận: ........................  Người đề nghị: ......................

STT | Tên hàng/Dịch vụ | ĐVT | Số lượng | Đơn giá ước tính | Nhà CC đề xuất
----|------------------|-----|----------|-----------------|---------------
 1  |                  |     |          |                 |
 2  |                  |     |          |                 |

Thời gian cần nhận: ....................................
Mục đích sử dụng: .......................................
Tài khoản chi phí: ......................................
Ghi chú: ................................................

Người đề nghị: .......... Trưởng BP: .......... Phê duyệt: ..........
Ngày: ................ Ngày: ................ Ngày: ................

BIỂU MẪU PURCHASE ORDER (PO):
Số PO: PO-[YY]-[MM]-[XXXX]      Ngày phát hành: ....../......./..........
Nhà cung cấp: ............... | MST: ............... | Địa chỉ: ...............

CHI TIẾT ĐẶT HÀNG:
STT | Mô tả hàng hóa | ĐVT | Số lượng | Đơn giá | Thành tiền
----|----------------|-----|----------|---------|----------
    |                |     |          |         |
                                      TỔNG CỘNG:

Điều kiện giao hàng: .....................................
Thời hạn giao hàng: ......................................
Địa điểm nhận hàng: ......................................
Điều khoản thanh toán: ...................................
Số tài khoản ngân hàng: ..................................

Người phê duyệt: .................. Chức danh: .............. Ngày: .......
```

---

## C. KIỂM SOÁT VÀ CẢI TIẾN QUY TRÌNH

```
KIỂM SOÁT NỘI BỘ VÀ KPI QUY TRÌNH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KIỂM SOÁT GIAN LẬN VÀ RỦI RO:
□ Phân quyền rõ ràng: Người đề nghị ≠ Người phê duyệt ≠ Người nhận hàng
□ Rotation: Không để 1 người phụ trách 1 NCC quá 3 năm liên tục
□ Audit trail: Mọi thay đổi PO đều phải có lý do và chữ ký
□ Báo giá ngẫu nhiên: Kiểm tra giá thị trường đột xuất
□ Conflict of interest: Nhân viên khai báo quan hệ với NCC

ĐI VÒNG (MAVERICK SPENDING) PHÒNG NGỪA:
□ Mua hàng không qua Procurement → Vi phạm quy chế
□ Trả NCC trước khi có PO → Không được chấp thuận
□ Mua từ NCC chưa được duyệt → Cần giải trình và bổ sung AVL

KPI QUY TRÌNH MUA HÀNG:
KPI                           | Mục tiêu  | Đo bằng cách
------------------------------|-----------|---------------------------
Thời gian xử lý PR → PO       | ≤ 2 ngày  | Timestamp trong hệ thống
Tỷ lệ PO không có PR          | ≤ 1%      | Audit hàng tháng
Tỷ lệ Invoice khớp PO         | ≥ 95%     | 3-way matching report
Maverick spending (% tổng)    | ≤ 5%      | Spend report
Thời gian thanh toán NCC       | Đúng hạn  | Aging report AP

SỐ HÓA QUY TRÌNH MUA HÀNG:
Cấp độ 1 — Excel/Google Sheet: PR, PO template + email phê duyệt
Cấp độ 2 — ERPNext (miễn phí): Quy trình tự động + approval workflow
Cấp độ 3 — Phần mềm chuyên dụng: Misa, SAP, Oracle (cho doanh nghiệp lớn)
→ SME dưới 100 nhân viên: Cấp độ 1–2 là đủ
```

---

## Định dạng đầu ra

Thiết kế quy trình mua hàng end-to-end với approval levels, chuẩn hóa biểu mẫu PR/PO hoặc xây dựng hệ thống kiểm soát nội bộ mua hàng.
