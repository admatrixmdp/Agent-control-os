---
name: fin-investor-cap-table
description: |
  Quản lý cap table (cơ cấu cổ đông) qua các vòng gọi vốn, tính dilution pre/post money,
  SAFE/convertible note conversion, ESOP pool. Trigger phrases: "cap table", "cơ cấu cổ đông",
  "dilution gọi vốn", "pre-money post-money", "SAFE convertible", "ESOP pool",
  "round modeling", "term sheet analysis", "ownership table", "vốn cổ phần".
  Output là Excel cap table dynamic + PDF round summary.
---

# Cap Table & Dilution Pre/Post Money

## Mục Tiêu
Founder/CFO cần "kiểm soát quyền sở hữu" qua các vòng gọi vốn - tránh tình trạng "tỉnh dậy"
thấy mình còn dưới 20% sau Series B. Cap table chuẩn còn là điều kiện đầu tiên VC/PE xem
trước khi đầu tư.

## Khi Nào Dùng
- Trước khi đàm phán term sheet vòng mới
- Khi cấp ESOP cho NV mới
- Khi convertible note đến due cần chuyển đổi
- Báo cáo HĐQT/cổ đông thay đổi cơ cấu
- Chuẩn bị due diligence của NĐT

## Bước 1: Khởi Tạo Cap Table Ban Đầu
**Pre-investment ownership:**
| Cổ đông | Loại CP | Số CP | % | Investment | PPS |
|---------|---------|-------|---|------------|-----|
| Founder A | Common | 600,000 | 60% | - | - |
| Founder B | Common | 300,000 | 30% | - | - |
| Friend/Family | Common | 100,000 | 10% | 500M | 5,000 |
| **Total** | | **1,000,000** | **100%** | | |

**Authorized vs Outstanding vs Fully diluted:**
- Authorized: tối đa được phép phát hành (theo điều lệ)
- Outstanding: đã phát hành thực tế
- Fully diluted: outstanding + options + warrants + convertible nếu convert

## Bước 2: Mô Phỏng Vòng Gọi Vốn Mới
**Term sheet input:**
- Pre-money valuation: $5M
- Investment: $1M
- Post-money: $6M
- Investor share % = 1M / 6M = 16.67%

**ESOP top-up (thường VC yêu cầu):**
- ESOP pool sau vòng = 10-15% fully diluted
- Top-up trước khi đầu tư (founder dilute) hay sau (cả 2 dilute)

**Mới CP phát hành:**
```
PPS (Price per share) = Pre-money / (Existing shares + ESOP top-up shares)
New shares to investor = Investment / PPS
```

**Post-money cap table:**
| Cổ đông | Pre | Pre % | Post | Post % | Dilution |
|---------|-----|-------|------|--------|----------|
| Founder A | 600k | 60% | 600k | 50% | -10pp |
| Founder B | 300k | 30% | 300k | 25% | -5pp |
| F&F | 100k | 10% | 100k | 8.3% | -1.7pp |
| ESOP new | - | - | 100k | 8.3% | new |
| Investor | - | - | 100k | 8.3% | new |

## Bước 3: SAFE & Convertible Note Conversion
**SAFE (Simple Agreement for Future Equity):**
- Không phải debt, không có interest, không expiry
- Convert tại vòng tiếp theo với valuation cap / discount

**Convertible Note:**
- Là debt, có lãi suất 5-8%, có maturity 18-24 tháng
- Auto-convert tại "qualified financing"

**Conversion calc:**
```
Conversion price = MIN(
    Vòng next PPS × (1 - Discount %),
    Valuation cap / Pre-money shares
)
SAFE shares = SAFE amount / Conversion price
```

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Cap table sống, founder + CFO + investor view
- Google Drive MCP: Lưu term sheet, SHA, SSA mỗi vòng
- Gmail MCP: Gửi cổ đông snapshot cap table sau mỗi vòng
- WebSearch: Tra benchmark dilution ngành (TechCrunch, Carta data)

**Fallback bằng API:**
```python
# Tính waterfall thanh khoản (liquidation preference)
import pandas as pd

cap_table = pd.DataFrame([
    {"holder": "Founder A", "shares": 600_000, "type": "common", "inv": 0, "pref_mult": 0},
    {"holder": "Founder B", "shares": 300_000, "type": "common", "inv": 0, "pref_mult": 0},
    {"holder": "Series A", "shares": 100_000, "type": "preferred", "inv": 1_000_000, "pref_mult": 1.0},
    {"holder": "Series B", "shares": 80_000, "type": "preferred", "inv": 5_000_000, "pref_mult": 1.0}
])

exit_value = 20_000_000  # $20M exit
# Step 1: Pay liquidation preference (Series B first, then A - LIFO)
remaining = exit_value
for _, row in cap_table[cap_table.type=="preferred"].iloc[::-1].iterrows():
    pref = row["inv"] * row["pref_mult"]
    pay = min(remaining, pref)
    remaining -= pay
    print(f"{row['holder']} gets {pay:,} as pref")
# Step 2: Distribute remaining pro-rata to all common
total_shares = cap_table["shares"].sum()
for _, row in cap_table.iterrows():
    share = remaining * row["shares"] / total_shares
    print(f"{row['holder']}: pro-rata {share:,.0f}")
```

## Bước 5: Output Format
1. **Excel cap table** (`captable_<company>_v3.xlsx`): Sheet "Current", "RoundModeling" simulate vòng tới, "ESOPSchedule", "WaterfallExit", "SAFEs".
2. **PDF round summary** (`series_A_summary.pdf`): 4-5 trang trình cổ đông cũ approve vòng mới.
3. **HTML interactive** (`captable_widget.html`): Sliders để founder thử các kịch bản dilution.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/captable/`

## Checklist Trước Khi Giao
- [ ] Tổng % luôn = 100.00%
- [ ] Phân biệt rõ Common vs Preferred
- [ ] Fully diluted bao gồm tất cả options/warrants/SAFE
- [ ] Liquidation preference đúng thứ tự (LIFO theo vòng)
- [ ] Có scenario waterfall cho exit thấp/trung/cao
- [ ] Founder hiểu rõ % mình sẽ có sau vòng (key number)
