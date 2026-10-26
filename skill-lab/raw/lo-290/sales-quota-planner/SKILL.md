---
name: sales-quota-planner
description: |
  Phân bổ chỉ tiêu sales theo territory, segment, AE — đảm bảo công bằng & đạt được, có ramp cho NV mới. Trigger phrases: "phân bổ quota", "quota planning", "chia chỉ tiêu sales", "territory quota", "ramp quota", "tính KPI sales tháng", "quota calculator", "phân bổ doanh số", "chia mục tiêu sales", "annual quota planning". Output là Excel quota model + Markdown methodology doc.
---

# Sales Quota Planner

## Mục Tiêu
Phân bổ quota cho 20-100 AE theo top-down (CFO target) + bottom-up (territory potential) cân bằng, có ramp 3-6 tháng cho NV mới, đạt 80%+ AE hit quota.

## Khi Nào Dùng
- Annual planning đầu năm
- Mid-year adjustment khi thị trường shift
- Sau M&A/restructure
- Khi mở thêm headcount sales
- Sau khi >50% AE miss quota >2 quý liền

## Bước 1: Top-down Target (CFO/CRO)
Pull số:
- Company revenue target
- Sales contribution (% inbound/outbound)
- New vs renewal split
- New logo target $ + count
- Expansion target $

Phân bổ theo BU/region/segment.

## Bước 2: Bottom-up Potential
Theo territory:
- TAM (Total Addressable Market) số KH × ARPA
- SAM = TAM × penetrable %
- Win rate giả định × deal size × cycle months
- Capacity model: 1 AE chạy được X deal/quý

Vd: AE chạy 20 deal/quý × 25% win × $30K = $150K/quý → quota $600K/năm.

## Bước 3: Cân bằng Top-down vs Bottom-up
- Gap = Top-down - Bottom-up
- Nếu Gap >20%: cần tăng headcount HOẶC giảm target HOẶC tăng productivity
- Nếu Gap <0%: Bottom-up dư, có thể stretch quota +10%
- Document assumption + scenario

## Bước 4: Phân bổ Cá nhân + Ramp
- Tenured AE (>12 tháng): full quota
- New AE: ramp
  - Tháng 1-3: 25% quota
  - Tháng 4-6: 50% quota
  - Tháng 7+: 100% quota
- AE đặc biệt (named account): quota theo account, không generic

## Bước 5: Comp Plan Alignment
Quota + comp plan check:
- OTE / quota = 12-25% (industry standard)
- Accelerator >100% (vd 150% commission rate)
- Decelerator <60% (vd 50% rate)
- SPIF cho deal đặc biệt (new logo, multi-year)

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce MCP: pull historical pipeline + win rate
- ZoomInfo/Apollo MCP: TAM data theo segment
- Excel/Sheets MCP: build model collaborative
- Slack MCP: communicate quota allocation

**Fallback API:**
```python
# Tính quota AE theo capacity
def calc_quota(territory_tam, win_rate, avg_deal, deals_per_qtr):
    annual_capacity = deals_per_qtr * 4 * win_rate * avg_deal
    # Stretch 10%
    return annual_capacity * 1.1

# Ramp factor
def ramp(month_tenure):
    if month_tenure < 3: return 0.25
    if month_tenure < 6: return 0.5
    return 1.0
```

## Bước 7: Output Format
- **File 1**: `quota_plan_<year>.xlsx` — sheet AE / Territory / Top-down / Bottom-up / Final quota / Ramp / Comments
- **File 2**: `quota_methodology.md` — doc giải thích assumption, scenario
- **File 3**: `territory_map.pptx` — visual phân bổ theo region
- **File 4**: `comp_plan_check.xlsx` — OTE / quota ratio mỗi AE
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Top-down + bottom-up reconcile <20% gap
- [ ] Ramp đầy đủ cho new AE
- [ ] OTE/quota 12-25%
- [ ] 80%+ AE achievable (không quá stretch)
- [ ] Document assumption rõ
- [ ] CRO + CFO approve trước khi communicate
