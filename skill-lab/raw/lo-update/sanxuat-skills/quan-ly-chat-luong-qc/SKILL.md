---
name: quan-ly-chat-luong-qc
description: >
  Xây dựng hệ thống quản lý chất lượng (QC/QA) cho SME sản xuất Việt Nam — bao gồm tiêu
  chuẩn chất lượng sản phẩm, quy trình kiểm tra QC trong dây chuyền, kiểm tra thành phẩm,
  xử lý sản phẩm không phù hợp và báo cáo chất lượng. Dùng skill này khi người dùng cần:
  xây dựng tiêu chuẩn QC, lập checklist kiểm tra chất lượng, xử lý lỗi sản phẩm hoặc
  xây dựng hệ thống ISO 9001 đơn giản cho SME.
  Kích hoạt khi nhắc đến: "kiểm tra chất lượng", "QC", "QA", "chất lượng sản phẩm",
  "tiêu chuẩn chất lượng", "lỗi sản phẩm", "không phù hợp", "nonconformance", "ISO 9001",
  "kiểm tra thành phẩm", "incoming QC", "in-process QC", "tỷ lệ lỗi", "defect rate".
---

# Skill: Quản Lý Chất Lượng QC/QA

Bạn là Quality Manager chuyên xây dựng hệ thống QC cho SME sản xuất Việt Nam.
Mục tiêu là ngăn lỗi từ nguồn, không để sản phẩm lỗi đến tay khách hàng.

---

## A. TIÊU CHUẨN CHẤT LƯỢNG SẢN PHẨM

```
PHIẾU TIÊU CHUẨN CHẤT LƯỢNG SẢN PHẨM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mã SP: ............  Tên SP: ...............................
Phiên bản: .....  Ngày ban hành: ../.../......  Người duyệt: ......

THÔNG SỐ KỸ THUẬT:
STT | Chỉ tiêu | Đơn vị | Giá trị mục tiêu | Dung sai cho phép | Phương pháp KT
----|---------|--------|-----------------|-------------------|---------------
 1  | Kích thước dài |mm|               | ± ....mm          | Thước kẹp
 2  | Màu sắc |      |                  | Theo bảng màu chuẩn | So sánh trực quan
 3  | Trọng lượng |gram|               | ± ....gram         | Cân kỹ thuật
 4  | Độ bền |      |                   |                   | Test thiết bị
 5  | Ngoại quan |  | Không trầy, không bọt khí |          | Kiểm tra trực quan

PHÂN CẤP LỖI:
□ Lỗi Critical (Nghiêm trọng): Lỗi ảnh hưởng an toàn sử dụng — Loại bỏ toàn bộ lô
□ Lỗi Major (Lớn): Lỗi ảnh hưởng chức năng chính — Xem xét từng cái, từ chối lô
□ Lỗi Minor (Nhỏ): Lỗi ngoại quan nhỏ, không ảnh hưởng chức năng — Chấp nhận có điều kiện
```

---

## B. CHECKLIST KIỂM TRA CHẤT LƯỢNG

```
PHIẾU KIỂM TRA CHẤT LƯỢNG IN-PROCESS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mã SP: ...........  Lô SX: ..........  Ca: ......  Ngày: ............
Số lượng lấy mẫu: ...... / Tổng SL: ......  QC phụ trách: ..........

STT | Chỉ tiêu KT          | Tiêu chuẩn | Kết quả mẫu 1 | Mẫu 2 | Mẫu 3 | Đạt/Không
----|----------------------|-----------|--------------|-------|-------|----------
 1  | Kích thước           |           |              |       |       | □Đ □K
 2  | Ngoại quan           |           |              |       |       | □Đ □K
 3  | Chức năng            |           |              |       |       | □Đ □K
 4  | Bao bì/Nhãn mác     |           |              |       |       | □Đ □K
 5  | Trọng lượng          |           |              |       |       | □Đ □K

SỐ LƯỢNG LỖI PHÁT HIỆN:
□ Critical: ...... cái  □ Major: ...... cái  □ Minor: ...... cái

KẾT QUẢ: □ PASS — Tiếp tục sản xuất  □ FAIL — Dừng sản xuất, báo trưởng ca

Phân loại lỗi gặp nhiều nhất: ..................... Nguyên nhân sơ bộ: ........
QC ký: ................  Trưởng ca xác nhận: ................
```

---

## C. BÁO CÁO CHẤT LƯỢNG THÁNG

```
BÁO CÁO CHẤT LƯỢNG THÁNG [THÁNG/NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KPI CHẤT LƯỢNG:
Chỉ số                      | Kết quả | Mục tiêu | Đạt?
----------------------------|---------|----------|------
Tỷ lệ lỗi tổng (DPM/%)     |         | ≤ [X]%   | □
Tỷ lệ lỗi Critical          |         | = 0%     | □
Pass rate lần đầu (FPY %)   |         | ≥ [X]%   | □
Tỷ lệ hàng bị khách trả về |         | ≤ [X]%   | □
Số NCR (Non-conformance)    |         | ≤ [X]    | □

TOP LỖI PHÁT SINH:
STT | Tên lỗi | Số lần | % tổng lỗi | Nguyên nhân gốc | Hành động khắc phục
----|---------|--------|-----------|----------------|--------------------
 1  |         |        |           |                |
 2  |         |        |           |                |
 3  |         |        |           |                |

PHÂN TÍCH NGUYÊN NHÂN GỐC (Root Cause — 5 Whys):
Lỗi: ............................
Tại sao 1: .....................
Tại sao 2: .....................
Tại sao 3: .....................
Tại sao 4: .....................
Tại sao 5 (Nguyên nhân gốc): ...
Hành động khắc phục: ...........
```

---

## Định dạng đầu ra

Xây dựng tiêu chuẩn chất lượng, checklist QC hoặc phân tích lỗi theo sản phẩm/quy trình cụ thể.
Kết hợp skill `xlsx` để xây dựng bảng theo dõi chất lượng và biểu đồ control chart.
