---
name: fin-audit-prep
description: |
  Chuẩn bị tài liệu kiểm toán cuối năm (BCTC) - PBC list, sample audit trail, reconciliation
  schedule, đối chiếu xác nhận công nợ. Trigger phrases: "chuẩn bị kiểm toán",
  "audit preparation", "PBC list", "tài liệu kiểm toán", "year-end audit",
  "kiểm toán BCTC", "thư xác nhận công nợ", "audit working paper",
  "audit confirmation", "audit checklist". Output là Excel PBC tracker + folder data
  room.
---

# Chuẩn Bị Tài Liệu Kiểm Toán Cuối Năm

## Mục Tiêu
Giảm thời gian kiểm toán từ 3 tháng xuống 4-6 tuần bằng cách chuẩn bị 100% PBC list
trước khi auditor vào, có data room ngăn nắp, tránh "câu giờ" mỗi lần auditor hỏi thêm
tài liệu. Tiết kiệm phí kiểm toán + giảm rủi ro modified opinion.

## Khi Nào Dùng
- Tháng 12 - Tháng 3 mỗi năm cho kiểm toán BCTC
- Khi có kiểm toán giữa kỳ (interim audit)
- Trước due diligence M&A
- Trước IPO (kiểm toán nhiều năm liền)
- Khi đổi auditor cần handover

## Bước 1: Nhận PBC List & Phân Công
**PBC (Prepared By Client) list** thường có 80-150 items, chia theo cycle:
- **Cash cycle**: sao kê, recon, cash count
- **Revenue cycle**: revenue recognition, AR aging, sample invoice + delivery + shipment
- **Purchase cycle**: AP aging, sample invoice + GR + payment
- **Inventory cycle**: kiểm kê, sample costing, NRV check
- **PPE cycle**: FA register, depreciation, addition/disposal docs
- **Payroll cycle**: lương, BHXH, NV mới/nghỉ
- **Tax cycle**: VAT, CIT, TNCN files
- **Equity & debt**: hợp đồng vay, biên bản HĐQT
- **Related party**: list, transactions, balance, signed disclosure
- **Subsequent events** sau cut-off

**Phân công matrix:**
| Item | Owner | Deadline | Status | Note |
|------|-------|----------|--------|------|

## Bước 2: Build Data Room (Folder Structure)
```
/AUDIT_2025/
├── 01_Cash_and_Bank/
│   ├── 01_Bank_statements/
│   ├── 02_Reconciliations/
│   └── 03_Confirmations/
├── 02_AR_Revenue/
│   ├── 01_AR_aging/
│   ├── 02_Confirmations_sent/
│   ├── 03_Samples (auditor will select)
│   └── 04_Provision_doubtful/
├── 03_Inventory/
├── 04_PPE/
├── 05_AP_Expenses/
├── 06_Equity_Debt/
├── 07_Payroll/
├── 08_Tax/
├── 09_Related_party/
├── 10_Legal_Contingent/
└── 11_BCTC_draft/
```

Mỗi folder có README.md ghi nội dung + người liên hệ.

## Bước 3: Schedule Quan Trọng
**Lead schedule** cho mỗi khoản mục chính:
- Số dư đầu năm (audited prior year)
- Phát sinh trong năm (debit, credit)
- Số dư cuối năm
- Cross-reference với BCTC + sổ cái + sub-ledger

**Reconciliation:**
- Sub-ledger với GL (AR sub vs GL 131)
- BS với GL trial balance
- BCTC kiểm toán năm trước với GL đầu năm nay

**Confirmations:**
- Thư xác nhận ngân hàng (gửi cho 100% TK)
- Thư xác nhận công nợ AR top 80% giá trị
- Thư xác nhận AP top 80%
- Thư xác nhận luật sư (legal letter)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: Build data room có cấu trúc, phân quyền auditor (view only)
- Gmail MCP: Auto-gửi thư xác nhận công nợ + thư ngân hàng hàng loạt
- Google Sheets MCP: PBC tracker sống, auditor + client xem cùng
- WebSearch: Tra chuẩn mực VAS, IFRS có cập nhật mới ảnh hưởng năm tài chính

**Fallback bằng API:**
```python
# Auto-gửi thư xác nhận AR top 80% giá trị
import requests
import pandas as pd

ar = pd.read_excel("ar_aging_yearend.xlsx")
ar = ar.sort_values("balance", ascending=False)
ar["cumsum_pct"] = ar["balance"].cumsum() / ar["balance"].sum()
top_80 = ar[ar["cumsum_pct"] <= 0.80]

for _, customer in top_80.iterrows():
    requests.post(
        "https://api.gmail.com/send",
        json={
            "to": customer["contact_email"],
            "subject": f"Thư xác nhận công nợ tại 31/12/2025 - {customer['name']}",
            "body": f"Kính gửi {customer['name']},\n"
                    f"Để phục vụ kiểm toán BCTC năm 2025, "
                    f"vui lòng xác nhận số dư công nợ tại 31/12/2025: "
                    f"{customer['balance']:,}đ\n"
                    f"Vui lòng phản hồi trước 15/01/2026...",
            "attachments": ["confirmation_letter_template.pdf"]
        },
        headers={"Authorization": f"Bearer {TOKEN}"}
    )
```

## Bước 5: Output Format
1. **Excel PBC tracker** (`PBC_tracker_2025.xlsx`): Sheet "Master" 150 items, "Status_summary" gauge % hoàn thành, "Audit_queries" log câu hỏi auditor.
2. **Folder data room** (Drive folder): Cấu trúc 11 folder như trên, có 200-500 tài liệu PDF.
3. **PDF audit memo** (`audit_memo_yearend.pdf`): Tổng quan các vấn đề trọng yếu (significant transactions, estimates, judgments) trước khi auditor bắt đầu.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/audit/`

## Checklist Trước Khi Giao
- [ ] PBC list 100% items có owner + deadline
- [ ] Data room đã set quyền auditor view, log access
- [ ] Lead schedule cho top 10 khoản mục BCTC
- [ ] Đã gửi 100% confirmation thư trước cut-off + 15 ngày
- [ ] BCTC draft đã prepare, không chờ auditor mới làm
- [ ] Có người làm "audit coordinator" full-time trong kỳ
