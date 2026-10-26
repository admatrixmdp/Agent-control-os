---
name: sales-trade-promotion-plan
description: |
  Plan trade promotion FMCG cho nhà phân phối/retail — mechanic, budget, ROI tracking. Trigger phrases: "trade promotion plan", "khuyến mãi đại lý FMCG", "promo NPP", "trade marketing plan", "khuyến mãi kênh phân phối", "promotion mechanic retail", "trade budget plan", "khuyến mãi bán sỉ", "FMCG promo", "plan promo nhà phân phối". Output là Excel promo calendar + Markdown mechanic + ROI tracker.
---

# Trade Promotion Plan (FMCG)

## Mục Tiêu
Tạo plan trade promotion theo tháng/quý cho NPP/retailer FMCG với mechanic rõ ràng, budget tracked, ROI đo lường — đạt incremental sales lift >15% và ROI >2x.

## Khi Nào Dùng
- Q1/Q2/Q3/Q4 planning
- Trade kèm new product launch
- Counter competitor promo
- Off-season activation
- Inventory clearance

## Bước 1: 6 Promo Mechanic Phổ Biến

**A. Volume discount**: mua X lốc tặng Y%
**B. Tiered rebate**: doanh số tháng vượt target → rebate %
**C. Product bundle**: combo SKU
**D. Display incentive**: NPP đặt POSM → tiền display
**E. Slot/Listing fee**: vào shelf prime location
**F. Joint marketing**: co-fund quảng cáo

Mix 2-3 mechanic per promo.

## Bước 2: Budget Allocation
Trade budget thường 3-8% revenue. Phân:
- 40% volume discount
- 20% rebate
- 15% display
- 10% listing
- 10% joint marketing
- 5% contingency

ROI target ≥ 2x (revenue lift / promo cost).

## Bước 3: Promo Calendar
Excel calendar:
- Cột: Tuần W1-W52
- Hàng: SKU / Channel / Region
- Cell: Mechanic + Budget + Target

Stagger để không over-promo (rủi ro burnout giá).

## Bước 4: Sell-in & Sell-out
- Sell-in: NPP đặt thêm khi promo
- Sell-out: end-consumer mua từ retail
→ Đo cả 2 tránh "load and dump" (NPP đặt mà không sell-out).

KPI:
- Sell-in lift %
- Sell-out lift %
- Inventory level post-promo
- ROI = incremental margin / promo cost

## Bước 5: NPP Communication
- Pre-launch: brief 14 ngày trước
- Material: poster, leaflet, demo video
- T&C: rõ ràng, không gài chữ nhỏ
- Hotline support trade
- Weekly performance update

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- ERP/SAP MCP: pull sell-in/sell-out data
- Salesforce CG (Consumer Goods) MCP: trade promo management
- BI MCP: ROI dashboard
- WhatsApp MCP: communicate NPP

**Fallback API:**
```python
# ROI calculation per promo
def promo_roi(promo):
    baseline = avg_sales(promo["sku"], days=28, exclude_period=promo["dates"])
    promo_sales = sales_during(promo["sku"], promo["dates"])
    incremental = promo_sales - baseline * (promo["days"]/28)
    incremental_margin = incremental * promo["margin_pct"]
    return {
        "incremental_sales": incremental,
        "promo_cost": promo["total_cost"],
        "roi": incremental_margin / promo["total_cost"]
    }
```

## Bước 7: Output Format
- **File 1**: `trade_promo_calendar.xlsx` — 52-week schedule
- **File 2**: `promo_mechanic_library.md` — 6 mechanic + script
- **File 3**: `promo_briefing.docx` — NPP brief template
- **File 4**: `promo_ROI_tracker.xlsx` — per promo ROI live
- **File 5**: `promo_budget_master.xlsx` — annual budget breakdown
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Budget allocation 6 bucket
- [ ] Calendar stagger tránh over-promo
- [ ] Sell-in + sell-out đo cả 2
- [ ] ROI target ≥ 2x
- [ ] NPP brief 14 ngày trước
- [ ] Post-promo review trong 30 ngày
