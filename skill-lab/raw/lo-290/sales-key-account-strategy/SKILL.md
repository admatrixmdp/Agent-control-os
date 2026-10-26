---
name: sales-key-account-strategy
description: |
  Chiến lược Key Account top 20 — wallet share, governance, joint business plan, executive engagement. Trigger phrases: "key account strategy", "KA top 20 strategy", "chiến lược KH lớn", "joint business plan", "key account management", "strategic account", "KAM playbook", "key account governance", "executive sponsor KH", "key account growth". Output là Docx strategy + Excel KA dashboard + JBP slide.
---

# Key Account Strategy (Top 20)

## Mục Tiêu
Tăng wallet share top 20 KH từ 15% → 30-40% bằng strategy framework gồm joint business plan, executive governance, multi-product penetration trong 12-18 tháng.

## Khi Nào Dùng
- Annual KA planning
- Top 20 KH chiếm 60-80% revenue
- Sau win deal lớn cần plan growth
- Re-segment portfolio
- Khi assign Key Account Manager mới

## Bước 1: Identify Top 20 (Pareto)
Tiêu chí ranking:
- Current ARR
- 3-year growth potential
- Strategic value (reference, vertical anchor)
- Influence (industry voice)
- Renewal lock-in

Bỏ "too small to bother" + "too big to lose grip".

## Bước 2: Wallet Share Analysis
Mỗi KA:
- Current spend với mình
- Estimated total spend category (qua research, finance disclosure)
- Wallet share = current / total
- Gap = total - current
- White space mapping by BU/product

## Bước 3: Joint Business Plan (JBP)
Co-create với KH:
- Shared vision 3 năm
- KPI cả 2 bên đo
- Initiative roadmap (product launch, integration, co-marketing)
- Executive sponsor each side
- Quarterly governance

JBP signed = lock-in 2-3 năm.

## Bước 4: Multi-product Penetration
- Map BU/department chưa mua
- Land & expand: bắt đầu 1 use case → scale
- Cross-sell roadmap có target ARR
- AE+CSM+SE joint plan
- 18-month milestone

## Bước 5: Executive Governance
- Executive Sponsor mình (VP+) match VP KH
- Quarterly EBR (Executive Business Review)
- Annual offsite/dinner
- Crisis call hotline
- Reference & advocacy program

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce MCP: KA dashboard
- LinkedIn MCP: executive relationship map
- WebFetch: KH 10-K, annual report, strategy doc
- Calendar MCP: executive sponsor cadence
- Slack MCP: KA dedicated channel

**Fallback API:**
```python
# Wallet share calc
def wallet_share(ka):
    current = ka["current_arr"]
    industry_avg_spend = ka["revenue"] * INDUSTRY_PCT_FOR_CATEGORY
    share = current / industry_avg_spend
    gap = industry_avg_spend - current
    return {"share_pct": share*100, "gap_$": gap,
            "growth_target_12mo": gap * 0.3}  # target 30% of gap
```

## Bước 7: Output Format
- **File 1**: `KA_strategy_<account>.docx` — 15 trang full strategy
- **File 2**: `KA_dashboard.xlsx` — 20 KA × metric × owner
- **File 3**: `joint_business_plan.pptx` — JBP slide cho KH
- **File 4**: `wallet_share_analysis.xlsx` — gap + growth target
- **File 5**: `executive_governance_calendar.xlsx` — EBR + offsite cadence
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Top 20 selection có data
- [ ] Wallet share calc cho từng
- [ ] JBP co-created Champion
- [ ] Executive Sponsor mapped 2 bên
- [ ] Multi-product roadmap 18 tháng
- [ ] Quarterly EBR cadence
