---
name: fin-financial-model-3statement
description: |
  Xây mô hình tài chính 3 báo cáo (P&L, Balance Sheet, Cashflow) liên kết động cho lập kế hoạch
  5 năm, gọi vốn, đánh giá kịch bản. Trigger phrases: "mô hình tài chính 3 báo cáo",
  "3-statement model", "financial model", "fundraising model", "mô hình 5 năm",
  "integrated financial model", "model dự phóng", "long range plan", "FP&A model",
  "model gọi vốn". Output là Excel model + PPTX investor deck.
---

# Mô Hình Tài Chính 3 Báo Cáo Liên Kết (P&L - BS - CF)

## Mục Tiêu
Xây "trái tim tài chính" của doanh nghiệp - 1 file Excel duy nhất tham số hoá, thay đổi 1 biến
là 3 báo cáo update liên hoàn. Dùng cho: lập kế hoạch năm, gọi vốn, M&A, làm strategy.
Chuẩn investment banking đưa về cho SME.

## Khi Nào Dùng
- Đầu năm xây kế hoạch tài chính
- Chuẩn bị pitch deck gọi vốn (Series A/B/C)
- Đánh giá kịch bản M&A
- Stress test trước khủng hoảng
- Báo cáo HĐQT plan 3-5 năm

## Bước 1: Thiết Kế Cấu Trúc Model
**6 sheet chuẩn:**
1. **Cover & Assumption** - tham số đầu vào (revenue growth, GM%, OpEx%, CapEx, WC days, WACC, tax)
2. **P&L** - 5 năm forecast theo tháng/quý/năm
3. **Balance Sheet** - cuối mỗi kỳ
4. **Cash Flow** - HĐKD, HĐĐT, HĐTC
5. **Working Capital schedule** - AR/AP/Inventory days drive WC
6. **Debt schedule** - các khoản vay với interest expense

Nguyên tắc: KHÔNG hardcode trong báo cáo - mọi số đều link về Assumption.

## Bước 2: Build P&L Driver-Based
**Revenue:**
- Driver: # KH × ARPU × retention rate (SaaS)
- Hoặc: Volume × Price (sản xuất, F&B)
- Tách kênh: B2B/B2C, online/offline, region

**COGS:**
- Variable: % revenue (Material, freight)
- Semi-fixed: lương SX, khấu hao máy

**OpEx:**
- S&M: % revenue (digital), absolute (offline)
- R&D: % revenue hoặc headcount × cost
- G&A: tăng theo headcount + inflation

**EBITDA → EBIT → EBT → Net Income**

## Bước 3: Liên Kết BS & CF
**Balance Sheet (cân bằng cuối kỳ):**
- AR = Revenue × DSO/365
- Inventory = COGS × Inv_days/365
- AP = COGS × DPO/365
- Fixed Assets = Prior FA + CapEx - Depreciation
- Cash = balancing item (từ CF)
- Debt = từ debt schedule
- Equity = Prior + Net Income - Dividend

**Cash Flow:**
```
CFO = Net Income + D&A - ΔWC
CFI = -CapEx + Asset Sale
CFF = ΔDebt + Equity raised - Dividend
Net cash = CFO + CFI + CFF
Ending cash = Opening + Net cash
```

→ **Check khoá**: Ending cash trên CF = Cash trên BS; BS Assets = Liabilities + Equity

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Build model collaborative, team Finance edit cùng
- Google Drive MCP: Lưu version theo quý + investor-facing pack
- WebSearch: Tra benchmark ngành (growth rate, margin) từ Vietstock, FiinGroup
- WebFetch: Pull WACC industry từ Damodaran NYU site

**Fallback bằng API:**
```python
# Stress test 1000 kịch bản Monte Carlo bằng Python
import numpy as np
rng = np.random.default_rng(42)

def model_year(rev_growth, gm, opex_pct, wacc):
    rev = 100_000_000_000 * (1 + rev_growth)
    cogs = rev * (1 - gm)
    opex = rev * opex_pct
    ebit = rev - cogs - opex
    return ebit

results = []
for _ in range(1000):
    rev_g = rng.normal(0.20, 0.10)
    gm = rng.normal(0.40, 0.05)
    opex = rng.normal(0.25, 0.03)
    wacc = 0.13
    ebit = model_year(rev_g, gm, opex, wacc)
    results.append(ebit)

print(f"P10 EBIT: {np.percentile(results, 10)/1e9:.1f}B")
print(f"P50 EBIT: {np.percentile(results, 50)/1e9:.1f}B")
print(f"P90 EBIT: {np.percentile(results, 90)/1e9:.1f}B")
print(f"P(EBIT < 0): {(np.array(results)<0).mean():.1%}")
```

## Bước 5: Output Format
1. **Excel model** (`fin_model_<company>_2026_2030.xlsx`): 6+ sheet như trên, có data validation, conditional formatting, named ranges, no hardcode.
2. **PPTX investor deck** (`investor_deck.pptx`): 15-20 slide - story, market, traction, financials, ask.
3. **PDF teaser** (`teaser_1pager.pdf`): 1 trang highlight cho gửi NĐT vòng đầu.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/model/`

## Checklist Trước Khi Giao
- [ ] BS cân (Assets = Liab + Equity) mọi kỳ
- [ ] Cash trên CF = Cash trên BS
- [ ] Mọi cell có hardcode đều highlight vàng (audit trail)
- [ ] Có 3 kịch bản Base/Bull/Bear với switch
- [ ] Sensitivity 2D cho 2 biến quan trọng nhất
- [ ] Documentation tab giải thích key assumptions
