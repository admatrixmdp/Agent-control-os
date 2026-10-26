---
name: fin-dcf-valuation
description: |
  Định giá doanh nghiệp theo phương pháp DCF (Discounted Cash Flow) - tính Enterprise Value
  và Equity Value cho mục đích M&A, gọi vốn, IPO. Trigger phrases: "định giá DCF",
  "DCF valuation", "discounted cash flow", "định giá doanh nghiệp", "enterprise value",
  "valuation model", "FCFF FCFE", "terminal value", "WACC calculation", "valuation cho M&A".
  Output là Excel DCF model + PDF valuation memo.
---

# Định Giá Doanh Nghiệp DCF (Discounted Cash Flow)

## Mục Tiêu
Tính giá trị nội tại của doanh nghiệp dựa trên dòng tiền tương lai chiết khấu về hiện tại.
Đây là phương pháp được giới đầu tư PE, VC, IB tin tưởng nhất. Output để negotiate
M&A, gọi vốn, ESOP pricing.

## Khi Nào Dùng
- Chuẩn bị gọi vốn Series A/B (PE/VC)
- Đàm phán M&A (mua/bán doanh nghiệp)
- IPO equity story
- Định giá ESOP / stock option NV
- Định giá fair value cho mua/bán cổ phần nội bộ

## Bước 1: Xây Dự Phóng FCFF 5-10 Năm
**Free Cash Flow to Firm (FCFF):**
```
FCFF = EBIT × (1-t) + D&A - ΔWC - CapEx
```

Phân tích:
- **Explicit forecast** 5-7 năm (growth cao, có thể model chi tiết)
- **Terminal year** 1 năm steady state
- **Growth giả định** phải hợp lý (không vượt GDP dài hạn)

## Bước 2: Tính WACC (Cost of Capital)
**WACC = (D/V × Kd × (1-t)) + (E/V × Ke)**

**Cost of Debt (Kd):**
- Lãi suất vay thực tế của công ty hiện tại
- Nếu không có, dùng spread theo credit rating

**Cost of Equity (Ke) - CAPM:**
```
Ke = Rf + Beta × MRP + size premium + country premium
```
- Rf: lãi suất TPCP 10 năm VN (~3.5%)
- MRP: Market Risk Premium (~7%)
- Beta: từ Damodaran theo ngành
- Size premium: +2-5% cho SME
- Country risk: VN ~3%

Ke SME VN thường: 15-22%
WACC SME VN: 12-18%

## Bước 3: Chiết Khấu Về Hiện Tại
**Enterprise Value:**
```
EV = Σ FCFF_t / (1+WACC)^t + TV / (1+WACC)^n

TV (Terminal Value) = FCFF_(n+1) / (WACC - g)
```
g = growth dài hạn ≤ GDP (3-5%)

**Equity Value:**
```
Equity = EV - Net Debt + Excess Cash - Minority Interest
Value per share = Equity / Total shares (fully diluted)
```

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebFetch: Pull beta ngành từ Damodaran NYU
- WebSearch: Tra lãi suất TPCP VN, MRP từ FiinGroup
- Google Sheets MCP: Build model + share confidential
- Google Drive MCP: Lưu valuation memo cho data room

**Fallback bằng API:**
```python
# Tính DCF + sensitivity table
import numpy_financial as npf
import numpy as np

fcff = [50, 70, 95, 120, 145]  # Tỷ VND, year 1-5
wacc = 0.14
g = 0.04
tv = fcff[-1] * (1+g) / (wacc - g)
cf_with_tv = fcff[:-1] + [fcff[-1] + tv]
ev = npf.npv(wacc, [0] + cf_with_tv)
net_debt = 100  # tỷ
equity_value = ev - net_debt
shares = 10  # triệu
price = equity_value * 1000 / shares  # VND/cp

print(f"EV: {ev:,.0f} tỷ")
print(f"Equity: {equity_value:,.0f} tỷ")
print(f"Price/share: {price:,.0f} VND")

# Sensitivity 2D: WACC × g
sens = np.zeros((5, 5))
waccs = [0.12, 0.13, 0.14, 0.15, 0.16]
gs = [0.02, 0.03, 0.04, 0.05, 0.06]
for i, w in enumerate(waccs):
    for j, gg in enumerate(gs):
        tv_s = fcff[-1] * (1+gg) / (w - gg)
        cf_s = fcff[:-1] + [fcff[-1] + tv_s]
        sens[i,j] = npf.npv(w, [0]+cf_s) - net_debt
print(sens)
```

## Bước 5: Output Format
1. **Excel DCF model** (`DCF_<company>_2026.xlsx`): Sheet "Assumption", "Operating model", "FCFF", "WACC", "DCF_summary", "Sensitivity 2D", "Football field" (so các phương pháp).
2. **PDF valuation memo** (`valuation_memo.pdf`): 10-15 trang theo chuẩn IB - exec summary, methodology, key assumptions, results, sensitivity, risks.
3. **PPTX** (`valuation_deck.pptx`): 10 slide presenting cho HĐQT/NĐT.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/dcf/`

## Checklist Trước Khi Giao
- [ ] FCFF tính đúng (không double-count D&A)
- [ ] WACC ≥ cost of debt (basic sanity)
- [ ] g ≤ GDP dài hạn (3-5% VN)
- [ ] Terminal value ≤ 70% của Enterprise Value
- [ ] Có ít nhất 2 phương pháp khác để cross-check (comps, transaction)
- [ ] Sensitivity 2D cho WACC × g + cho 2 driver chính
