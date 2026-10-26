---
name: fin-bank-reconciliation
description: |
  Đối soát ngân hàng tự động giữa sổ kế toán và sao kê - phát hiện chênh lệch, hạch toán bổ sung
  các giao dịch còn thiếu. Trigger phrases: "đối soát ngân hàng", "bank reconciliation",
  "khớp sao kê", "reconcile ngân hàng", "đối chiếu sổ phụ", "BR statement", "chênh lệch sao kê",
  "matching giao dịch", "outstanding check", "deposit in transit". Output là Excel
  reconciliation + báo cáo chênh lệch.
---

# Đối Soát Ngân Hàng Theo Statement

## Mục Tiêu
Tự động hoá việc khớp sao kê NH với sổ TK 112 - tiết kiệm 2-3 ngày công kế toán/tháng,
phát hiện nhanh các giao dịch sót, gian lận, sai số tài khoản, ngăn ngừa thất thoát.

## Khi Nào Dùng
- Cuối mỗi tuần / mỗi tháng đối soát toàn bộ TK ngân hàng
- Sau mỗi đợt chi lớn (payroll, thanh toán batch)
- Khi nghi ngờ có giao dịch lạ hoặc fraud
- Trước khi đóng sổ tháng (mandatory)
- Trước khi kiểm toán

## Bước 1: Thu Thập 2 Nguồn Dữ Liệu
**Sổ kế toán (book):**
- Trích sổ chi tiết TK 112 cho từng tài khoản, theo kỳ
- Cột: ngày, số chứng từ, nội dung, nợ (chi), có (thu), số dư

**Sao kê NH (bank statement):**
- File CSV/Excel/PDF từ Internet Banking
- Cột: ngày, mã GD, nội dung, số tiền, dư

Đảm bảo cùng đầu kỳ - cuối kỳ.

## Bước 2: Matching Tự Động
**Rule matching:**
1. Khớp đúng số tiền + ngày (±2 ngày để tính lag T+1)
2. Khớp số tiền + mã GD/số CT nếu có
3. Khớp số tiền + fuzzy match nội dung (>70% similarity)

**Phân loại sau matching:**
- **Matched**: cả 2 sổ có, khớp → OK
- **Book only (in book, not in bank)**: có trên sổ chưa thấy ở NH
  - Thường là: séc đã viết chưa rút, UNC chưa ngân hàng xử lý
- **Bank only**: NH có mà sổ chưa hạch toán
  - Thường là: phí NH, lãi tiền gửi, thu hộ KH chuyển khoản chưa biết
- **Mismatched**: cả 2 có nhưng số tiền lệch
  - Thường là: ghi sai, fraud, sai tỷ giá

## Bước 3: Hạch Toán Bổ Sung & Reconciliation Statement
**Hạch toán bổ sung "Bank only":**
- Phí NH: Nợ 6427 / Có 112
- Lãi tiền gửi: Nợ 112 / Có 515
- Thu hộ KH chưa rõ: Nợ 112 / Có 131 (chi tiết KH) hoặc 338 tạm chờ
- Phát sinh chênh lệch tỷ giá: Nợ/Có 413

**Reconciliation statement:**
```
Số dư theo sổ kế toán:            X
+ Bank only inflows (chưa ghi):   +A
- Bank only outflows (chưa ghi):  -B
+/- Mismatched adjustments:       ±C
= Số dư điều chỉnh sổ:            X + A - B ± C

Số dư theo sao kê NH:             Y
+ Book only outflows (NH chưa xử lý): +D
- Book only inflows (NH chưa nhận):   -E
= Số dư điều chỉnh NH:            Y + D - E

→ 2 số phải bằng nhau!
```

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Đặt template reconciliation, paste sao kê vào tự matching
- Gmail MCP: Pull sao kê email từ NH gửi tự động
- Google Drive MCP: Lưu sao kê + biên bản reconciliation theo tháng
- WebFetch: Pull sao kê HTML từ Internet Banking nếu có URL công khai

**Fallback bằng API:**
```python
# Pull sao kê tự động qua Open Banking API
import requests
import pandas as pd

r = requests.get(
    "https://openapi.vietcombank.com.vn/v1/accounts/0011000123456/transactions",
    params={"from": "2026-05-01", "to": "2026-05-31"},
    headers={"Authorization": f"Bearer {VCB_TOKEN}"}
)
bank_txns = pd.DataFrame(r.json()["transactions"])

# Load sổ kế toán từ MISA/FAST
book_txns = pd.read_excel("so_112_T05.xlsx")

# Match bằng pandas merge với tolerance
merged = book_txns.merge(
    bank_txns, on="amount", how="outer", indicator=True,
    suffixes=("_book", "_bank")
)
matched = merged[merged["_merge"]=="both"]
book_only = merged[merged["_merge"]=="left_only"]
bank_only = merged[merged["_merge"]=="right_only"]
print(f"Matched: {len(matched)}, Book only: {len(book_only)}, Bank only: {len(bank_only)}")
```

## Bước 5: Output Format
1. **Excel reconciliation** (`bank_recon_<acc>_T05_2026.xlsx`): Sheet "Matched", "BookOnly", "BankOnly", "Mismatched", "Statement" reconciliation chính.
2. **PDF biên bản đối soát** (`reconciliation_T05.pdf`): Mẫu chuẩn có chữ ký KT thanh toán + KTT.
3. **HTML dashboard** (`bank_recon_dashboard.html`): % matched, list issue chưa giải quyết, aging item book-only/bank-only.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/bank/`

## Checklist Trước Khi Giao
- [ ] Đầu kỳ và cuối kỳ trên book khớp với statement
- [ ] 100% giao dịch matched hoặc có giải thích
- [ ] Mọi bank-only đã hạch toán bổ sung
- [ ] Mọi mismatched đã trace nguyên nhân
- [ ] Số dư cuối sau điều chỉnh = số dư sao kê
- [ ] Lưu sao kê gốc + báo cáo recon ≥ 10 năm
