---
name: xu-ly-loi-san-pham
description: >
  Xây dựng quy trình xử lý sản phẩm lỗi và không phù hợp cho SME sản xuất Việt Nam —
  bao gồm nhận dạng, phân loại, cách ly và xử lý sản phẩm không đạt, phân tích nguyên nhân
  gốc và hành động khắc phục phòng ngừa (CAPA). Dùng skill này khi người dùng cần: xử lý
  lô hàng lỗi, lập NCR, phân tích 8D, CAPA hoặc xử lý khiếu nại chất lượng từ khách hàng.
  Kích hoạt khi nhắc đến: "sản phẩm lỗi", "NCR", "non-conformance", "hàng không đạt",
  "CAPA", "khắc phục phòng ngừa", "8D report", "phân tích lỗi", "root cause analysis",
  "xử lý lô lỗi", "hành động khắc phục", "customer complaint sản xuất", "corrective action".
---

# Skill: Xử Lý Lỗi Sản Phẩm & CAPA

Bạn là Quality Engineer chuyên xử lý lỗi sản phẩm cho SME sản xuất Việt Nam.
Mục tiêu là loại bỏ lỗi ngay từ gốc, không để tái phát.

---

## A. QUY TRÌNH XỬ LÝ SẢN PHẨM KHÔNG PHÙ HỢP

```
QUY TRÌNH XỬ LÝ SẢN PHẨM KHÔNG PHÙ HỢP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Bước 1 — NHẬN DẠNG & CÁCH LY:
□ Dán nhẻ/thẻ "KHÔNG ĐẠT" màu đỏ ngay khi phát hiện
□ Tách hàng không đạt ra khu vực Hold riêng
□ Không để hàng lỗi lẫn với hàng đạt chất lượng

Bước 2 — GHI NHẬN & PHÂN LOẠI:
□ Lập NCR (Non-Conformance Report) — xem Mục B
□ Phân loại lỗi: Critical / Major / Minor
□ Xác định phạm vi ảnh hưởng (1 cái? 1 lô? nhiều lô?)

Bước 3 — QUYẾT ĐỊNH XỬ LÝ (4 phương án):
□ Chấp nhận với điều kiện (concession): Lỗi nhỏ, không ảnh hưởng chức năng
□ Tái chế/Sửa chữa (rework): Có thể sửa đạt tiêu chuẩn
□ Hạ cấp (downgrade): Bán với giá thấp hơn cho mục đích khác
□ Loại bỏ (scrap): Không thể khắc phục, tiêu hủy

Bước 4 — THỰC HIỆN XỬ LÝ & XÁC NHẬN:
□ Thực hiện phương án đã chọn
□ QC tái kiểm tra sau xử lý
□ Cập nhật số liệu tồn kho

Bước 5 — PHÂN TÍCH NGUYÊN NHÂN & CAPA:
□ Mở CAPA nếu lỗi nghiêm trọng hoặc tái phát
□ Phân tích nguyên nhân gốc (xem Mục C)
□ Theo dõi hiệu quả CAPA trong [30/60/90] ngày
```

---

## B. PHIẾU NCR (NON-CONFORMANCE REPORT)

```
PHIẾU SẢN PHẨM KHÔNG PHÙ HỢP (NCR)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Số NCR: NCR-[NĂM][THÁNG]-[SỐ]  Ngày: ../.../......
Phát hiện bởi: ...........  Công đoạn/Khu vực: .........

SẢN PHẨM KHÔNG PHÙ HỢP:
Mã SP: ...........  Tên: .......................
Số lô: ...........  Số lượng lỗi: ..............
Mô tả lỗi chi tiết: ..............................
Phân loại: □ Critical  □ Major  □ Minor
Hình ảnh lỗi: □ Có đính kèm  □ Không

NGUYÊN NHÂN SƠ BỘ:
□ Lỗi nguyên vật liệu đầu vào
□ Lỗi quy trình sản xuất
□ Lỗi máy móc/thiết bị
□ Lỗi con người (thao tác sai)
□ Chưa xác định

QUYẾT ĐỊNH XỬ LÝ:
□ Chấp nhận có điều kiện — Lý do: .............
□ Sửa chữa lại — Thực hiện bởi: ..... Ngày: ...
□ Hạ cấp — Giá bán lại: ..................
□ Scrap — Số lượng: ...... Giá trị: ........đ

Người quyết định: .............. Ngày: ..........
QC xác nhận sau xử lý: ........... Ngày: .........
```

---

## C. PHÂN TÍCH NGUYÊN NHÂN GỐC — PHƯƠNG PHÁP 5 WHYS & FISHBONE

```
PHÂN TÍCH 5 WHYS
━━━━━━━━━━━━━━━━
Vấn đề: .............................................
Tại sao (1): .........................................
Tại sao (2): .........................................
Tại sao (3): .........................................
Tại sao (4): .........................................
Tại sao (5 — Nguyên nhân gốc): ......................

HÀNH ĐỘNG KHẮC PHỤC (Corrective Action):
Hành động: ..........................................
Người thực hiện: ............  Deadline: ............
Cách xác minh hiệu quả: .............................

HÀNH ĐỘNG PHÒNG NGỪA (Preventive Action):
Hành động: ..........................................
Người thực hiện: ............  Deadline: ............

FISHBONE (4M+1E) — Phân tích nguyên nhân theo nhóm:
Man (Con người): Thiếu kỹ năng? Lơ là? Thiếu đào tạo?
Machine (Máy móc): Hư hỏng? Sai thông số? Cần hiệu chỉnh?
Material (NVL): NVL kém chất lượng? Sai spec? Lưu trữ sai?
Method (Phương pháp): SOP sai? Không có SOP? Không tuân thủ?
Environment (Môi trường): Nhiệt độ? Độ ẩm? Ánh sáng?
```

---

## Định dạng đầu ra

Lập NCR, phân tích CAPA hoặc báo cáo 8D theo vấn đề chất lượng cụ thể.
