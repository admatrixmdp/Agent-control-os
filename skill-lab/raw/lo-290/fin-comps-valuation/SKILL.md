---
name: fin-comps-valuation
description: |
  Định giá doanh nghiệp theo phương pháp so sánh (Trading Comps + Transaction Comps) -
  dùng các bội số EV/EBITDA, P/E, EV/Revenue của doanh nghiệp niêm yết tương đồng.
  Trigger phrases: "định giá so sánh", "comps valuation", "EV/EBITDA multiple",
  "P/E multiple", "trading comps", "transaction comps", "định giá theo bội số",
  "peer group analysis", "football field", "công ty tương đồng". Output là Excel comps
  table + PDF memo.
---

# Định Giá Doanh Nghiệp Theo Phương Pháp So Sánh (Comps)

## Mục Tiêu
Định giá nhanh bằng cách so với "hàng xóm" - lấy multiples của doanh nghiệp niêm yết hoặc
giao dịch M&A gần đây áp vào KPI của mình. Phương pháp này market-based, hợp để cross-check
DCF và hợp dùng đàm phán M&A.

## Khi Nào Dùng
- Cross-check kết quả DCF
- Đàm phán mua/bán DN tham khảo market multiples
- Lập football field cho IPO equity story
- Định giá nhanh khi không có model chi tiết
- Báo cáo NĐT định kỳ thay đổi multiples ngành

## Bước 1: Chọn Peer Group
**Tiêu chí chọn peers:**
- Cùng ngành (SIC code)
- Cùng quy mô (revenue, EBITDA - trong khoảng 0.3-3x)
- Cùng geography / thị trường
- Cùng business model (B2B vs B2C, asset-heavy vs light)
- Cùng giai đoạn tăng trưởng

**Số lượng:** 5-10 công ty là vừa, tránh quá ít (mẫu yếu) hoặc quá nhiều (loãng).

**Nguồn:**
- HOSE/HNX/UPCoM cho VN
- Sàn quốc tế cho ngành VN chưa niêm yết
- VCSC/SSI/HSC research reports

## Bước 2: Tính Các Bội Số (Multiples)
**Trading Multiples** (từ giá cổ phiếu):
| Multiple | Công thức | Khi nào dùng |
|----------|-----------|--------------|
| EV/Revenue | EV / DT | Công ty chưa có lãi |
| EV/EBITDA | EV / EBITDA | Phổ biến nhất, comparable across capital structure |
| EV/EBIT | EV / EBIT | Khi D&A khác nhau lớn |
| P/E | Price / EPS | Truyền thống, áp dụng cho công ty ổn định |
| P/B | Price / Book value | Banking, real estate |
| PEG | P/E / Growth | Growth companies |

**EV (Enterprise Value)** = Market Cap + Debt - Cash + Minority interest

**Multiples bias:**
- LTM (Last Twelve Months) - dữ liệu thực
- NTM (Next Twelve Months) - forward, phản ánh kỳ vọng
- Forward multiples thường thấp hơn LTM nếu growth dương

## Bước 3: Áp Vào Doanh Nghiệp Mình
**Tính dải giá:**
1. Lấy median + mean của peer multiples (loại outlier)
2. Nhân với KPI mình → EV implied
3. Trừ Net Debt → Equity Value
4. Chia số cp → Price per share

**Transaction Comps** (từ deal M&A):
- Premium 20-40% so trading multiples
- Theo deal database: VPS, FiinPro, S&P Capital IQ
- Phù hợp khi có giao dịch ngành ≤ 24 tháng

**Football Field** - tổng hợp các phương pháp:
```
DCF:         100-130 tỷ ███████
Trading P/E:  80-110 tỷ █████
Trading EV/EBITDA: 90-120 tỷ █████
M&A Comps:  110-150 tỷ ██████
→ Convergence range: 100-120 tỷ
```

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebFetch: Pull market cap, P/E của peers từ Cafef, VietStock
- WebSearch: Tin M&A deal recent trong ngành
- Google Sheets MCP: Build comps table sống, refresh tuần/tháng
- Google Drive MCP: Lưu source data + screenshots cho audit trail

**Fallback bằng API:**
```python
# Pull multiples từ Vietstock/Cafef API
import requests
import pandas as pd

peers = ["MWG", "FRT", "DGW", "PET"]
data = []
for ticker in peers:
    r = requests.get(f"https://api.vietstock.vn/finance/{ticker}/multiples")
    m = r.json()
    data.append({
        "ticker": ticker,
        "ev_ebitda": m["ev_ebitda_ttm"],
        "p_e": m["pe_ttm"],
        "ev_revenue": m["ev_revenue_ttm"]
    })
df = pd.DataFrame(data)

# Tính median/mean (loại top + bottom)
def trimmed_avg(s):
    s_sorted = sorted(s)[1:-1] if len(s)>3 else s
    return sum(s_sorted)/len(s_sorted)

multiples = {
    "ev_ebitda": trimmed_avg(df["ev_ebitda"]),
    "p_e": trimmed_avg(df["p_e"])
}

# Apply to my company
my_ebitda = 50_000_000_000
my_net_debt = 100_000_000_000
implied_ev = multiples["ev_ebitda"] * my_ebitda
implied_equity = implied_ev - my_net_debt
print(f"Implied Equity Value: {implied_equity/1e9:,.0f} tỷ")
```

## Bước 5: Output Format
1. **Excel comps table** (`comps_<company>_2026.xlsx`): Sheet "Trading_comps", "Transaction_comps", "Multiples_calc", "FootballField", "PeerAnalysis" (compare profitability, growth).
2. **PDF valuation memo** (`comps_memo.pdf`): 8-10 trang, methodology, peer selection rationale, results, sensitivity.
3. **PPTX football field** (`football_field.pptx`): 1-2 slide visual cho HĐQT.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/comps/`

## Checklist Trước Khi Giao
- [ ] Peer group có ≥ 5 công ty đủ tương đồng
- [ ] Đã loại outlier (multiples cao/thấp bất thường)
- [ ] EV tính đúng (không lẫn market cap)
- [ ] Có cả trading + transaction comps (nếu có deal)
- [ ] So sánh DCF range với comps range
- [ ] Có disclosure: nguồn dữ liệu, ngày cập nhật
