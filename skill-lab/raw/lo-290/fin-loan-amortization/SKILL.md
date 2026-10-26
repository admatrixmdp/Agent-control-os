---
name: fin-loan-amortization
description: |
  Lập lịch trả nợ vay theo tháng - tách rõ gốc, lãi, dư nợ còn lại cho các phương án trả
  (đều, gốc cố định, linh hoạt). Trigger phrases: "lịch trả nợ", "amortization schedule",
  "trả nợ vay", "tính lãi vay", "lịch trả gốc lãi", "loan calculator", "kế hoạch trả nợ",
  "PMT loan", "lãi suất ngân hàng", "dư nợ vay". Output là Excel lịch trả nợ + HTML
  dashboard.
---

# Lịch Trả Nợ Vay Theo Tháng (Gốc + Lãi)

## Mục Tiêu
Lập sẵn lịch trả nợ chính xác từng đồng cho mọi khoản vay - tránh quên kỳ trả, biết trước
chi phí lãi cả đời vay, so sánh nhanh các phương án để chọn tối ưu cho cashflow.

## Khi Nào Dùng
- Trước khi ký hợp đồng vay so sánh ngân hàng
- Sau giải ngân lập lịch trả chính thức
- Khi xét tái cấu trúc nợ, trả nợ trước hạn
- Khi cần tích hợp lịch trả vào cashflow forecast
- Báo cáo nợ vay cho HĐQT định kỳ

## Bước 1: Thu Thập Thông Số Khoản Vay
- Tên khoản vay, ngân hàng, hợp đồng số
- Số tiền giải ngân (principal)
- Lãi suất: cố định hay thả nổi (base rate + biên)
- Kỳ hạn (12, 36, 60, 120 tháng)
- Phương án trả: Niên kim (PMT), Gốc đều, Cuối kỳ (bullet), Linh hoạt
- Ngày giải ngân, ngày trả trong tháng
- Phí: phí thu xếp (front-end fee), phí cam kết, phí trả trước hạn

## Bước 2: Xây Lịch Trả Theo Phương Án

**Phương án 1: Niên kim (trả đều cả gốc + lãi)**
```
PMT = P × r × (1+r)^n / [(1+r)^n - 1]
```
- r = lãi tháng = APR/12
- n = số tháng
- Mỗi kỳ: lãi = dư nợ × r; gốc = PMT - lãi; dư nợ mới = dư nợ - gốc

**Phương án 2: Gốc đều (gốc cố định, lãi giảm dần)**
- Gốc mỗi kỳ = P/n
- Lãi mỗi kỳ = dư nợ × r
- Tổng trả giảm dần theo thời gian
- → Áp lực dòng tiền cao đầu kỳ nhưng tổng lãi thấp hơn niên kim

**Phương án 3: Bullet (trả lãi định kỳ, gốc cuối kỳ)**
- Áp dụng cho trái phiếu, vay ngắn hạn

## Bước 3: Phân Tích & So Sánh
**Số liệu key:**
- Tổng lãi trả cả đời vay
- EMI (Equated Monthly Installment)
- Effective interest rate (EIR) - cộng tất cả phí
- Lãi trên tổng trả (%)
- Cashflow impact theo từng tháng

**So sánh:**
| Phương án | Tổng trả | Lãi cả đời | Áp lực dòng tiền |
|-----------|----------|------------|------------------|
| Niên kim 5 năm | 1.32B | 320M | Đều 22tr/tháng |
| Gốc đều 5 năm | 1.30B | 300M | 38tr T1 → 17tr T60 |
| Bullet 5 năm | 1.50B | 500M | 8tr/tháng + 1B cuối |

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Lịch trả nợ sống, link với cashflow forecast
- Google Calendar MCP: Đặt reminder ngày trả nợ trước 3 ngày
- Gmail MCP: Gửi NV thanh toán + KTT confirm mỗi kỳ trả
- WebSearch: Tra lãi suất ngân hàng cập nhật (VCB, BIDV, MB...)

**Fallback bằng API:**
```python
# Tính amortization schedule + xuất Excel
import numpy as np
import numpy_financial as npf
import pandas as pd

P = 1_000_000_000
annual_rate = 0.10
months = 60
r = annual_rate / 12

pmt = -npf.pmt(r, months, P)
schedule = []
balance = P
for t in range(1, months+1):
    interest = balance * r
    principal = pmt - interest
    balance -= principal
    schedule.append({"month": t, "pmt": pmt, "principal": principal,
                     "interest": interest, "balance": max(balance, 0)})
df = pd.DataFrame(schedule)
df.to_excel("loan_schedule.xlsx", index=False)
```

## Bước 5: Output Format
1. **Excel lịch trả** (`loan_<bank>_<year>.xlsx`): Sheet "Schedule" lịch 60-120 dòng, "Comparison" so sánh 3 phương án, "Summary" tổng quan + ratio.
2. **HTML dashboard** (`loan_dashboard.html`): Bar chart stacked gốc-lãi theo tháng, line chart dư nợ giảm dần, gauge % đã trả.
3. **PDF báo cáo HĐQT** (`loan_status.pdf`): Tổng dư nợ tất cả khoản vay + lịch trả 12 tháng tới.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/loans/`

## Checklist Trước Khi Giao
- [ ] Lãi suất khớp hợp đồng (chú ý lãi danh nghĩa vs lãi thực)
- [ ] Lịch trả khớp ngày giải ngân + ngày trả thực tế
- [ ] Đã tính EIR (cộng phí)
- [ ] Có cảnh báo trước 5 ngày cho NV thanh toán
- [ ] Đã sync với cashflow forecast 13 tuần
- [ ] Backup mỗi lần thay đổi lãi suất thả nổi
