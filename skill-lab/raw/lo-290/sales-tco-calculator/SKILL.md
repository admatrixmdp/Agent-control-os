---
name: sales-tco-calculator
description: |
  Tính TCO (Total Cost of Ownership) so sánh giải pháp 3-5 năm cho KH với hidden cost full. Trigger phrases: "tính TCO", "TCO calculator", "total cost of ownership", "so sánh TCO vendor", "tính tổng chi phí 3 năm", "TCO comparison", "TCO sales tool", "build vs buy TCO", "TCO breakdown", "compare cost solution". Output là Excel TCO model + PDF comparison sheet.
---

# TCO (Total Cost of Ownership) Calculator

## Mục Tiêu
So sánh giải pháp của mình vs đối thủ vs "do nothing" trên TCO 3-5 năm bao gồm hidden cost, giúp KH thấy giá list không phản ánh giá thật — đặc biệt khi đối thủ chiếm lợi thế "rẻ hơn upfront".

## Khi Nào Dùng
- Đối thủ tung giá thấp 30-50%
- KH so sánh build in-house vs buy
- Renewal đòi giảm giá
- KH skeptical về investment
- CFO/Procurement đòi cost breakdown

## Bước 1: Liệt kê 7 Component TCO

**A. License/Subscription** (visible):
- Subscription năm 1-5
- Per-user/per-feature scale

**B. Implementation** (visible):
- Professional services
- Data migration
- Integration build

**C. Training** (often hidden):
- Initial training
- Onboard new hire ongoing
- Train-the-trainer

**D. Internal Resources** (hidden):
- IT/Ops time setup + maintain
- Admin time daily
- Champion/program manager 0.2 FTE

**E. Infrastructure** (hidden):
- Server/cloud cost (nếu on-prem)
- Bandwidth
- Backup/DR

**F. Risk & Compliance** (hidden):
- Security audit
- Compliance certification
- Data breach insurance delta

**G. Switching/Exit cost** (hidden):
- Migration out
- Re-training nếu fail

## Bước 2: 5-Year Projection
Mỗi component × 5 năm:
- Year 1: implementation heavy
- Year 2-3: stable
- Year 4-5: refresh/expand cost

Discount rate 10% → NPV.

## Bước 3: 3-Scenario Comparison
- **Our Solution**: TCO 5y = $X
- **Competitor**: TCO 5y = $Y (thường +20-30% vì hidden cost)
- **Do Nothing/In-house**: TCO 5y = $Z (cost of inaction + build cost)

Visual: bar chart 3 cột, breakdown component.

## Bước 4: Sensitivity Analysis
Thay đổi assumption ±20%:
- User count
- Feature scope
- Discount rate
- Implementation overrun

→ Show TCO range, không 1 số duy nhất.

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- WebFetch: pull competitor pricing public + Forrester TEI
- Salesforce MCP: link TCO model vào opportunity
- Excel MCP: build interactive model
- WebSearch: tìm hidden cost report

**Fallback API:**
```python
# TCO model
def tco(license_yr1, impl, training, fte_hours_admin, hourly, growth_pct, years=5):
    breakdown = []
    for y in range(1, years+1):
        license = license_yr1 * (1 + growth_pct) ** (y-1)
        impl_y = impl if y == 1 else 0
        train = training * (1 if y == 1 else 0.2)
        internal = fte_hours_admin * 12 * hourly
        breakdown.append({"year": y, "total": license+impl_y+train+internal})
    npv = sum([b["total"]/(1.1**b["year"]) for b in breakdown])
    return breakdown, npv
```

## Bước 6: Output Format
- **File 1**: `tco_model_<customer>.xlsx` — interactive 7 component × 5 năm
- **File 2**: `tco_comparison.pdf` — 3 scenario side-by-side, 2 trang
- **File 3**: `tco_assumption.md` — document toàn bộ assumption
- **File 4**: `tco_summary_slide.pptx` — 1 slide cho exec meeting
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ 7 component (visible + hidden)
- [ ] 5-year projection + NPV
- [ ] 3 scenario (mình / đối thủ / build)
- [ ] Sensitivity ±20% chạy
- [ ] Assumption transparent
- [ ] Visual chart dễ đọc
- [ ] Champion review trước EB
