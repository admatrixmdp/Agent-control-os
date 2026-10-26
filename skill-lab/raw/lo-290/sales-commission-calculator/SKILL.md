---
name: sales-commission-calculator
description: |
  Tính hoa hồng sales tự động theo plan (base + accelerator + SPIF + clawback) từ data deal đã closed. Trigger phrases: "tính hoa hồng sales", "commission calculator", "sinh báo cáo hoa hồng", "calc commission AE", "tính comp sales tháng", "hoa hồng theo plan", "commission accelerator", "clawback commission", "payout sales", "tính lương sales". Output là Excel payout sheet + PDF mỗi AE.
---

# Sales Commission Calculator

## Mục Tiêu
Tự động tính hoa hồng cho 20-100 AE từ data CRM, áp dụng đúng rules (base rate, accelerator, SPIF, clawback) trong <1h thay vì 2-3 ngày Excel thủ công.

## Khi Nào Dùng
- Cuối tháng/quý payout cycle
- Plan thay đổi cần backtest
- AE dispute payout
- Onboarding AE mới cần preview
- Audit Finance/Internal Audit

## Bước 1: Định nghĩa Plan Components
Mỗi plan có:
- **Base rate** (vd 8% revenue)
- **Quota period** (monthly/quarterly/annual)
- **Accelerator**: vượt 100% → 1.5x, vượt 150% → 2x
- **Decelerator**: <60% → 0.5x
- **SPIF**: bonus đặc biệt (new logo +$2K, multi-year +5%)
- **Clawback**: nếu KH churn <90 ngày → đòi lại commission
- **Cap**: max payout

## Bước 2: Pull Data Deal Closed
Từ CRM:
- Closed-won deal trong period
- Amount + ARR + new vs expansion
- Close date + AE owner + product
- KH churn date (cho clawback)

Cleanse data:
- Loại deal không qualify
- Split commission nếu multi-AE
- Convert currency nếu cần

## Bước 3: Tính Payout từng AE
Pseudo flow:
```
attainment = closed_revenue / quota
if attainment < 0.6: rate = base * 0.5
elif attainment <= 1.0: rate = base * 1.0
elif attainment <= 1.5: rate = base * 1.5
else: rate = base * 2.0

commission = closed_revenue * rate
+ SPIF (new logo, multi-year, etc.)
- Clawback (KH churn early)
≤ Cap
```

## Bước 4: AE Statement (PDF mỗi người)
Mỗi AE có 1 PDF gồm:
- Quota / Attainment %
- Deal list (Name, ARR, Close date, Commission)
- SPIF earned
- Clawback (nếu có)
- Total payout + bank info
- Dispute window 7 ngày

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce/HubSpot MCP: pull closed deal
- CaptivateIQ/Spiff MCP: nếu có tool chuyên
- Email MCP: gửi statement riêng từng AE
- Sheets MCP: collaborative review với Finance

**Fallback API:**
```python
# Tính commission
import pandas as pd
deals = sf.query("""SELECT Amount, OwnerId, CloseDate, NewLogo__c 
    FROM Opportunity WHERE IsClosed=true AND IsWon=true 
    AND CloseDate >= THIS_MONTH""")
df = pd.DataFrame(deals["records"])
def calc(ae_id, ae_df, quota):
    rev = ae_df["Amount"].sum()
    att = rev / quota
    rate = 0.5 if att<0.6 else 1.0 if att<=1.0 else 1.5 if att<=1.5 else 2.0
    commission = rev * 0.08 * rate
    new_logo_count = ae_df["NewLogo__c"].sum()
    commission += new_logo_count * 2000  # SPIF
    return min(commission, 50000)  # Cap
```

## Bước 6: Output Format
- **File 1**: `commission_payout_<period>.xlsx` — master sheet all AE
- **File 2**: `commission_statement_<AE>.pdf` — riêng mỗi AE
- **File 3**: `commission_audit_log.xlsx` — log mỗi rule applied + override
- **File 4**: `payroll_export.csv` — sẵn import payroll system
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Quota + plan version đúng tại thời điểm
- [ ] Currency convert chính xác
- [ ] SPIF có evidence (new logo confirm, multi-year quote)
- [ ] Clawback check 90 ngày sau close
- [ ] Cap apply nếu có
- [ ] Finance + HR review trước payroll cut-off
- [ ] AE acknowledge statement trong 7 ngày
