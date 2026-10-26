---
name: Phân Tích Dữ Liệu & Dashboard TMĐT
description: >
  Xây dựng KPI framework, dashboard templates, và phân tích chi tiết cho TMĐT Việt Nam.
  Bao gồm: Traffic analysis, Conversion funnel, Revenue metrics, Marketing ROI,
  Retention analytics, Platform-specific insights (GA4, Shopee, Lazada, Facebook, TikTok).
  Báo cáo theo tần suất, Cohort analysis, RFM segmentation, Unit economics.

  Dùng skill này khi: "phân tích dữ liệu tmđt", "dashboard ecommerce",
  "kpi tracking", "google analytics", "shopee analytics", "conversion rate",
  "roas", "cac", "customer lifetime value", "báo cáo hàng tuần", "metrics"
---

# Phân Tích Dữ Liệu & Dashboard cho TMĐT Việt Nam

## 1. KPI Framework cho TMĐT

### 1.1 Traffic Metrics (Lưu Lượng & Hành Vi Khách)

```
| Metric | Định Nghĩa | Công Thức | Target (B2C) | Tầm Quan Trọng |
|--------|-----------|----------|--------------|---|
| Sessions | Lần khách visit website | Google Analytics | +15-20% MoM | 🔴 High |
| Users | Số người duy nhất | Unique visitors | +10-15% MoM | 🔴 High |
| Page Views | Tổng lượt xem trang | Sum(page views) | +20-30% MoM | 🟠 Medium |
| Bounce rate | % khách vào 1 trang rồi đi | (Bounced / Sessions) | < 40% (Target) | 🟠 Medium |
| Avg session duration | Thời gian trung bình trên site | Total duration / Sessions | > 2-3 phút | 🟢 Low |
| Traffic sources | Nguồn khách đến | Organic / Paid / Social / Direct | Channel ranking | 🟠 Medium |
| Top landing page | Trang khách vào nhiều nhất | Page with most entries | Optimization target | 🟢 Low |
| Top exit page | Trang khách ra nhiều nhất | Page with most exits | Issue to fix | 🟢 Low |

**Traffic Sources Breakdown (Mục tiêu allocation):**
├─ Organic search (Google): 35-45% (Free, high quality)
├─ Social media (FB, Zalo, TikTok): 25-35% (Paid ads)
├─ Direct: 10-15% (Khách biết brand)
├─ Email: 5-10% (Newsletter, remarketing)
├─ Affiliate: 5-10% (Influencer, partnership)
└─ Referral: 5-10% (Word of mouth)

**Channel Performance Example (Weekly tracking):**
Tuần 1 (1-7 April):
├─ Organic: 2,500 sessions, Bounce 35%, Avg duration 3:45
├─ Facebook Ads: 1,800 sessions, Bounce 42%, Avg duration 2:30
├─ TikTok Ads: 800 sessions, Bounce 50%, Avg duration 1:50
├─ Email: 300 sessions, Bounce 20%, Avg duration 5:20 (Highest quality)
└─ Direct: 400 sessions, Bounce 15%, Avg duration 4:10

Analysis:
├─ Email = Best quality (Lowest bounce, highest engagement)
├─ Organic next = Good quality
├─ TikTok = High volume but low quality (Fix: targeting or creative)
└─ Action: Increase email + organic budget
```

### 1.2 Conversion Metrics (Chuyển Đổi)

```
| Metric | Định Nghĩa | Công Thức | Target B2C | Note |
|--------|-----------|----------|-----------|------|
| Add to cart rate | % khách thêm sản phẩm vào giỏ | (ATC / Sessions) | 8-12% | Key indicator |
| Checkout rate | % khách bắt đầu thanh toán | (Checkouts / ATC) | 60-75% | Drop-off point |
| Purchase rate | % khách hoàn thành mua | (Orders / Sessions) | 0.8-2% | Revenue driver |
| Conversion rate | % khách mua / Tổng khách | (Orders / Sessions) | 0.8-2% | Overall metric |
| Cart abandonment rate | % khách bỏ giỏ hàng | (ATC - Orders) / ATC | 60-70% (High!) | Recovery opportunity |
| Average order value | Giá trị đơn hàng trung bình | Total revenue / Orders | [By industry] | Revenue lever |
| Revenue per visitor | Doanh thu / Khách | Total revenue / Users | Rising trend | Efficiency |

**Conversion Funnel (Ví dụ thực tế):**
100 khách visit
├─ 25 khách xem sản phẩm chi tiết (Conversion: 25%)
├─ 10 khách thêm vào giỏ (ATC rate: 10%)
├─ 8 khách vào checkout (Checkout rate: 80%)
├─ 1-2 khách mua (Purchase rate: 12.5-25%)
└─ **FINAL conversion rate: 1-2%**

**Phân Tích Drop-off:**
Vấn đề #1: Giữa xem sản phẩm → ATC (25% → 10%)
├─ Lý do: Người không rõ size, còn chần chừ
├─ Solution: Better size chart, customer reviews, chatbot tư vấn

Vấn đề #2: Giữa ATC → Checkout (10% → 8%)
├─ Lý do: Khách thay đổi ý định
├─ Solution: Pop-up giảm giá, retargeting ads

Vấn đề #3: Giữa Checkout → Purchase (8% → 1%)
├─ Lý do: Hóa đơn quá cao, thanh toán phức tạp
├─ Solution: Rút gọn form, add more payment methods, free shipping

**Weekly Conversion Tracking:**
```
Date Range: 1-7 April
├─ Sessions: 5,800
├─ ATCs: 580 (10%)
├─ Checkouts: 464 (80% of ATC)
├─ Orders: 58 (1% conversion rate)
├─ Revenue: 15.2M
├─ Cart abandonment: 516 (89% of ATCs)
└─ Action: Focus on checkout/abandonment recovery
```

### 1.3 Revenue Metrics (Doanh Thu & Lợi Nhuận)

```
| Metric | Định Nghĩa | Công Thức | Target | Priority |
|--------|-----------|----------|--------|----------|
| Gross merchandise value (GMV) | Tổng giá trị đơn (pre-discount) | Sum(price x qty) | +20% MoM | 🔴 High |
| Revenue | Tổng tiền thu được | GMV - Returns - Discounts | +20% MoM | 🔴 High |
| Average order value (AOV) | Giá trị đơn trung bình | Revenue / Orders | ₫800K-1.2M | 🔴 High |
| Revenue per user | Doanh thu / Khách | Revenue / Users | Rising | 🟠 Medium |
| Revenue per session | Doanh thu / Lần visit | Revenue / Sessions | Rising | 🟠 Medium |
| Profit margin | Lợi nhuận sau chi phí | (Revenue - COGS - OpEx) / Revenue | 20-35% | 🔴 High |
| Gross margin | Lợi nhuận trước chi phí | (Revenue - COGS) / Revenue | 50-70% | 🟠 Medium |
| Average selling price (ASP) | Giá bán trung bình | Σ(price) / items sold | By category | 🟢 Low |

**Revenue Breakdown (Monthly):**
March 2025:
├─ GMV (before discount): 450M
├─ Discounts & promotions: -45M (-10%)
├─ Net revenue: 405M
├─ Returns: -20M (-5%)
├─ **Actual revenue: 385M**
├─ COGS: -150M (-39%)
├─ Platform fees (Shopee, Lazada): -35M (-9%)
├─ Shipping cost: -40M (-10%)
├─ Packaging: -10M (-3%)
├─ Ads & marketing: -60M (-15%)
├─ Salaries & operations: -50M (-13%)
└─ **Net profit: 40M (10.4% margin)**

**Levers to increase revenue:**
├─ AOV increase: 10% → 860K → +5.3% revenue
├─ Conversion increase: 1% → 1.1% → +10% revenue
├─ Traffic increase: 5,000 → 5,500 → +10% revenue
├─ Repeat purchase: 20% → 25% → +5.3% revenue
└─ Best ROI: Traffic + Conversion combo
```

### 1.4 Marketing Metrics (Chi Phí & ROI)

```
| Metric | Định Nghĩa | Công Thức | Benchmark | Target |
|--------|-----------|----------|-----------|--------|
| Cost per click (CPC) | Chi phí per click ads | Ad spend / Clicks | 500-2000đ | Decreasing |
| Cost per impression (CPM) | Chi phí per 1000 impressions | (Ad spend / Impressions) x 1000 | 20-80K | Decreasing |
| Click-through rate (CTR) | % người click ads | (Clicks / Impressions) | 0.5-3% | Increasing |
| Cost per acquisition (CPA) | Chi phí trên mỗi khách mua | Ad spend / Orders | 150-500K | Decreasing |
| Return on ad spend (ROAS) | Doanh thu / Ad spend | Revenue / Ad spend | 3:1 to 5:1 | Increasing |
| Advertising cost of sales (ACoS) | Ad spend / Revenue | Ad spend / Revenue | 15-25% | Decreasing |
| Payback period | Số ngày để tiền ads về lại | Ad spend / Daily profit | < 30 ngày | Shorter |

**Monthly Ad Spend Analysis:**
April 2025 Ad Budget: 60M
├─ Facebook Ads: 25M
│  ├─ Spend: 25M
│  ├─ Sales: 80M
│  ├─ ROAS: 3.2:1 ✅ (Good)
│  └─ ACoS: 31% (High, optimize)
│
├─ Google Ads: 15M
│  ├─ Spend: 15M
│  ├─ Sales: 90M
│  ├─ ROAS: 6:1 ✅ (Excellent)
│  └─ ACoS: 17% (Great)
│
├─ TikTok Ads: 12M
│  ├─ Spend: 12M
│  ├─ Sales: 30M
│  ├─ ROAS: 2.5:1 ❌ (Poor)
│  └─ ACoS: 40% (Too high)
│
└─ Zalo Ads: 8M
   ├─ Spend: 8M
   ├─ Sales: 32M
   ├─ ROAS: 4:1 ✅ (Good)
   └─ ACoS: 25% (Acceptable)

**Action Items:**
├─ Scale Google Ads (+50% budget, best ROAS)
├─ Increase Facebook Ads (+20%, optimize ACoS)
├─ Pause or redesign TikTok (Poor ROAS)
└─ Test Zalo (Early stage, promising)
```

### 1.5 Retention & Loyalty Metrics

```
| Metric | Định Nghĩa | Công Thức | Target | Importance |
|--------|-----------|----------|--------|-----------|
| Repeat purchase rate | % khách mua lần 2+ | (Repeat customers / Total customers) | 25-35% | 🔴 High |
| Customer retention rate | % khách giữ lại qua tháng | (Retained customers / Last month) | 80%+ | 🔴 High |
| Churn rate | % khách bỏ | 1 - Retention rate | 0-20% | 🔴 High |
| Customer lifetime value (LTV) | Tổng doanh thu 1 khách | Repeat order value x Avg repeat frequency / Churn | 2-5M | 🔴 High |
| Payback period | Thời gian lấy lại CAC | CAC / (Monthly profit per customer) | < 6 months | 🟠 Medium |
| NPS (Net promoter score) | Khách recommend (1-10) | (Promoters - Detractors) / Total | > 50 | 🟠 Medium |
| Customer satisfaction (CSAT) | Hài lòng sản phẩm/dịch vụ | Avg rating / 5 | > 4/5 | 🟠 Medium |
| Product return rate | % đơn bị trả lại | (Returns / Orders) | < 5-10% | 🟠 Medium |

**Cohort Analysis (Khách theo tháng đăng ký):**
```
Cohort (Month) | Month 0 | Month 1 | Month 2 | Month 3 | Retention |
|---|---|---|---|---|---|
| Jan 2025 | 800 | 320 (40%) | 160 (20%) | 96 (12%) | 12% (Bad) |
| Feb 2025 | 950 | 380 (40%) | 190 (20%) | ? | Still growing |
| Mar 2025 | 1,100 | 440 (40%) | ? | ? | Early stage |
| Apr 2025 | 1,250 | ? | ? | ? | First month |

Analysis:
├─ Retention is stable (~20% after 2 months, 12% after 3)
├─ But too LOW! Industry avg is 30-40%
├─ Issue: Product quality? Customer service? Follow-up?
└─ Action: Improve customer experience
```

**LTV vs CAC Analysis:**
```
LTV = Average order value x Repeat purchase frequency / Churn rate
    = 900K x 2.5 / 0.15
    = 15M (per customer lifetime)

CAC = Total marketing spend / New customers acquired
    = 60M / 250
    = 240K (per new customer)

LTV / CAC ratio = 15M / 240K = 62.5x (Excellent!)
Target: > 3:1 (Yours is 62.5:1, so GREAT)
```

### 1.6 Operations Metrics

```
| Metric | Định Nghĩa | Công Thức | Target | Note |
|--------|-----------|----------|--------|------|
| Order fulfillment time | Thời gian from order → ship | Order date to ship date | < 24h | Logistic KPI |
| On-time delivery rate | % đơn giao đúng hạn | (On-time / Total) | > 95% | Shipper KPI |
| Defect/damage rate | % hàng bị hỏng khi giao | (Damaged / Total) | < 1% | Quality |
| Return/refund rate | % khách yêu cầu trả | (Returns / Orders) | 3-8% | By category |
| Refund processing time | Thời gian process refund | Approve to refund date | < 5 days | Service |
| Inventory turnover | Tốc độ hàng được bán | COGS / Avg inventory | 4-8x/year | Stock |
| Stockout rate | % sản phẩm hết hàng | (Stockouts / Order requests) | < 2% | Loss |
| Warehouse efficiency | Chi phí kho / GMV | Warehouse cost / GMV | < 3-5% | Cost |

**Return Reason Breakdown (April):**
Total returns: 24 (2% of 1,200 orders) ✅ Good rate
├─ Size not fit (10, 42%): Issue = Size chart unclear
├─ Quality issue (6, 25%): Issue = QC problem or shipping damage
├─ Wrong product (4, 17%): Issue = Warehouse picking error
├─ Changed mind (3, 13%): Normal, can't prevent
└─ Out of stock (1, 4%): Listing not updated

**Actions:**
├─ Improve size chart (Better photos, more details)
├─ Increase QC checks (Random sampling 10%)
├─ Train warehouse staff (Picking accuracy)
└─ Faster refund (Currently 4 days, target 2 days)
```

## 2. Dashboard Templates Theo Vai Trò

### 2.1 CEO Dashboard (Điều Hành Tổng)

**Frequency:** Daily check-in (5 min), Weekly review (30 min)

**Key Metrics (Real-time):**
```
┌─────────────────────────────────────────────────┐
│ 📊 CEO DASHBOARD - April 3, 2025                │
├─────────────────────────────────────────────────┤
│                                                 │
│ 💰 Revenue (Today)          135.2M ↑5% (vs YD)  │
│ 🎯 Revenue (MTD)            2.85B ↑12% (vs LM) │
│ 📈 Growth rate              12% (Target: 15%)  │
│                                                 │
│ 🛍️ Orders (Today)            180 ↑8%           │
│ 💳 Conversion rate           1.2% (Target: 2%) │
│ 👥 New customers             45 (25% of total) │
│                                                 │
│ 📊 Profit margin             11.2% (Target 15%)│
│ 💸 Ad spend                  5.2M (8% of rev)  │
│ 📉 CAC                       231K (vs LM: 245K)│
│ 📈 ROAS (Ads)                4.2:1 ↑ 0.3      │
│                                                 │
│ 🔴 Issues / Alerts:                            │
│    • TikTok ROAS dropped to 2.1:1 (Below 3:1) │
│    • Return rate 2.5% (Target: 2%)             │
│    • Zalo OA followers slow growth              │
│                                                 │
└─────────────────────────────────────────────────┘

Drill-down options:
├─ Revenue detail by channel / category / product
├─ Conversion funnel by device / traffic source
├─ Profitability by product / category
├─ Marketing ROI by platform
└─ Staff performance (sales, support, logistics)
```

### 2.2 Marketing Dashboard

**Frequency:** Daily (Ads), Weekly (Strategic review)

```
┌──────────────────────────────────────────────────┐
│ 📢 MARKETING DASHBOARD - April 2025              │
├──────────────────────────────────────────────────┤
│                                                  │
│ TRAFFIC SOURCES                                  │
│ ├─ Organic search: 2,500 (43%, ↑5%)             │
│ ├─ Facebook Ads: 1,800 (31%, ↑2%)               │
│ ├─ TikTok Ads: 800 (14%, ↓10%) ⚠️               │
│ └─ Email: 300 (5%, ↑15%)                        │
│                                                  │
│ AD PERFORMANCE (Today spend: 5.2M)               │
│ Platform | Spend | Clicks | CPC | ROAS | ACoS |
│ ---------|-------|--------|-----|------|-------|
│ Google   | 2.0M  | 2,400  | 833 | 6.1  | 16%   │
│ Facebook | 1.8M  | 1,800  | 1K  | 3.2  | 31%   │
│ Zalo     | 0.8M  | 640    | 1.3K| 4.0  | 25%   │
│ TikTok   | 0.6M  | 800    | 750 | 2.1  | 48%   │
│                                                  │
│ CAMPAIGN PERFORMANCE (Top 5)                     │
│ Campaign | Impr. | Clicks | CTR | Conv. | ROI  │
│ ---------|-------|--------|-----|-------|------|
│ Spring 25| 800K  | 8,400  | 1%  | 84    | 5.2x │
│ AOV up   | 600K  | 5,400  | 0.9%| 62    | 4.8x │
│ New users| 500K  | 4,200  | 0.8%| 50    | 3.2x │
│ Retarget | 400K  | 3,200  | 0.8%| 180   | 8.1x │
│ Email    | -     | 300    | -   | 45    | 9.2x │
│                                                  │
│ EMAIL PERFORMANCE                                │
│ Campaign | Sent | Open% | Click% | Conversion  │
│ ---------|------|-------|--------|-------------|
│ Newsletter| 5K  | 28%   | 4.2%   | 1.8%        │
│ Abandoned| 2K  | 42%   | 8.5%   | 3.2%        │
│ Reorder  | 1K  | 35%   | 6.1%   | 2.1%        │
│                                                  │
│ BUDGET ALLOCATION (Monthly: 60M)                 │
│ Facebook Ads: 25M (42%, down from 45%)          │
│ Google Ads: 18M (30%, up from 25%)              │
│ TikTok: 10M (17%, pause/test mode)              │
│ Zalo: 7M (11%, scale up)                        │
│                                                  │
│ 📋 Action Items:                                 │
│    • Pause TikTok until ROAS improves to 3:1    │
│    • Reallocate 5M from TikTok → Google         │
│    • Scale email (9.2x ROI is best)             │
│    • A/B test new Facebook creative             │
│                                                  │
└──────────────────────────────────────────────────┘
```

### 2.3 Operations Dashboard

**Frequency:** Daily (Morning & Evening check)

```
┌──────────────────────────────────────────────────┐
│ 📦 OPERATIONS DASHBOARD - April 3, 2025          │
├──────────────────────────────────────────────────┤
│                                                  │
│ ORDERS STATUS (Today)                            │
│ ├─ New orders: 180 (18:00 update)               │
│ ├─ Processing: 85 (Avg process time: 3.2h)     │
│ ├─ Shipped: 95 (Avg shipping delay: -0.5h ✅)  │
│ └─ Delivered: 42 (Success rate: 98.2%)          │
│                                                  │
│ LOGISTICS PERFORMANCE                            │
│ ├─ On-time delivery: 98.2% ✅ (Target: 95%)    │
│ ├─ Damaged during shipping: 0.3% (Target < 1%)│
│ ├─ Return rate: 2.1% (Target: < 3%)            │
│ ├─ Avg fulfillment time: 14.2h (Target: < 24h)│
│                                                  │
│ INVENTORY SUMMARY                                │
│ Category | Total | Sold (MTD) | Turnover | Alert│
│ ---------|-------|----------|----------|-------|
│ Áo       | 450   | 320 (71%)  | 4.1x     |      │
│ Quần     | 380   | 210 (55%)  | 3.2x     |      │
│ Váy      | 290   | 240 (83%)  | 5.1x     | 🔴Low│
│ Phụ kiện | 150   | 80 (53%)   | 3.1x     |      │
│                                                  │
│ 🔴 Low stock items:                              │
│    • Váy hoa (20 cái, selling 8/day)            │
│    • Quần kem XL (15 cái, selling 5/day)        │
│    → Need reorder in 2-3 days                   │
│                                                  │
│ SUPPORT METRICS                                  │
│ ├─ Chat response time: 2.1 min (Target: 1 min) │
│ ├─ Resolution rate: 87% (Target: 90%)          │
│ ├─ CSAT: 4.3/5 (4.2 yesterday)                  │
│ ├─ Open tickets: 12 (8 new, 4 pending)         │
│                                                  │
│ 🔴 Pending issues:                               │
│    • Customer A: Damaged áo (Waiting refund)    │
│    • Customer B: Wrong size (Waiting return)    │
│    • Customer C: Chốt order chưa gửi            │
│                                                  │
│ COST ANALYSIS (Today)                            │
│ ├─ COGS: 52.5M (39% of revenue)                 │
│ ├─ Platform fees: 10.8M (8%)                    │
│ ├─ Shipping cost: 12.2M (9%)                    │
│ ├─ Packaging: 2.7M (2%)                         │
│ └─ Margin after COGS: 58M (43%)                 │
│                                                  │
└──────────────────────────────────────────────────┘
```

### 2.4 Product Dashboard

**Frequency:** Weekly + Real-time alerts

```
┌──────────────────────────────────────────────────┐
│ 📊 PRODUCT DASHBOARD - Week of April 1-7, 2025   │
├──────────────────────────────────────────────────┤
│                                                  │
│ TOP 10 BEST SELLERS (By revenue)                 │
│ Rank | Product | Sales | Revenue | Review | ROI │
│ -----|---------|-------|---------|--------|-----|
│ 1    | Áo trắng| 92    | 25.8M   | 4.9⭐ | +28%│
│ 2    | Váy hoa | 78    | 27.3M   | 4.8⭐ | +35%│
│ 3    | Quần kem| 65    | 18.5M   | 4.7⭐ | +18%│
│ 4    | Áo navy | 58    | 16.2M   | 4.6⭐ | -5% │
│ 5    | Váy đen | 48    | 16.8M   | 4.8⭐ | +22%│
│ ... | ... | ... | ... | ... | ... |
│ 10   | Belt    | 28    | 5.6M    | 4.4⭐ | +8% │
│                                                  │
│ WORST PERFORMERS (Slow movers)                   │
│ Product | Sales | Revenue | Review | Action     │
│ --------|-------|---------|--------|------------|
│ Áo denim| 5     | 1.2M    | 4.2⭐ | Discount? │
│ Quần short| 8   | 1.6M    | 3.9⭐ | Seasonal  │
│ Phụ kiện| 12    | 2.4M    | 3.8⭐ | Bundling  │
│                                                  │
│ PRICE ELASTICITY ANALYSIS                        │
│ Current pricing - Which products to discount?    │
│ Product | Price | Sales/wk | If -10% | Benefit  │
│ --------|-------|----------|---------|----------|
│ Váy hoa | 349K  | 78       | ~88     | +12.8%   │
│ Áo navy | 319K  | 58       | ~62     | +6.9%    │
│ Quần kem| 299K  | 65       | ~68     | +4.6%    │
│ → Discount váy hoa (highest elasticity)        │
│                                                  │
│ CATEGORY PERFORMANCE                             │
│ Category | % of Sales | Margin | Growth | Status│
│ ---------|-----------|--------|--------|--------|
│ Áo       | 38%       | 52%    | +8%    | Stable │
│ Quần     | 28%       | 48%    | +6%    | OK     │
│ Váy      | 22%       | 50%    | +15%   | 🔥Hot  │
│ Phụ kiện | 12%       | 60%    | -2%    | Decline│
│                                                  │
│ 💡 Recommendations:                              │
│    • Invest in Váy (Fastest growth)              │
│    • Relaunch Phụ kiện (Focus bundle)            │
│    • Keep top 3 in stock (High velocity)         │
│    • A/B test colors for slow movers             │
│                                                  │
└──────────────────────────────────────────────────┘
```

## 3. Phân Tích Dữ Liệu Từng Nền Tảng

### 3.1 Google Analytics 4 (GA4)

**Setup cho TMĐT:**
```
1. Create GA4 property + Web stream
2. Install GA4 measurement ID code trên website
3. Setup key events:
   ├─ view_item: Khách xem trang sản phẩm
   ├─ add_to_cart: Khách thêm giỏ
   ├─ begin_checkout: Khách bắt đầu thanh toán
   ├─ purchase: Khách thanh toán thành công
   ├─ refund: Khách refund
   └─ view_promotion: Khách thấy banner khuyến mãi

4. Setup conversions:
   └─ purchase = Primary conversion goal

5. Link GA4 with Google Ads + Shopee/Lazada (nếu API có)
```

**Key Reports trong GA4:**
```
1. Acquisition Overview:
   ├─ Traffic source: Organic / Paid / Social / Direct / Email
   ├─ Channel grouping: Google Ads / Facebook / ...
   ├─ Campaign performance: Which campaign brings most traffic
   └─ Source/Medium: google / organic, facebook / paid, ...

2. Engagement Report:
   ├─ Pages & screens: Top landing pages, exit pages
   ├─ Events: Add to cart, view item, etc
   ├─ Scroll depth: Khách scroll sâu bao nhiêu
   ├─ Scroll: % khách scroll, avg scroll %
   └─ Time on page: Khách ở lâu bao lâu

3. Conversion Report:
   ├─ Conversion funnel: view → ATC → checkout → purchase
   ├─ Goal: Macro (purchase) + Micro (view_item, ATC)
   ├─ Conversion rate by source
   ├─ Conversion path: User journey to purchase
   └─ Time to conversion: Ngày từ first click to purchase

4. Audience Reports:
   ├─ User demographics: Age, gender, location
   ├─ User acquisition: New vs returning
   ├─ Retention cohort: Repeat visit behavior
   ├─ User lifetime: Subscription/repeat purchase tracking
   └─ Segments: Create custom audiences

Example GA4 Report:
Date Range: April 1-7, 2025
Users: 5,800
New users: 3,100 (53%)
Sessions: 6,200
Engagement rate: 72%
Avg session duration: 2:45
Bounce rate: 28%
Conversions: 58 (0.94% conversion rate)
Conversion value: 15.2M

Top channels:
├─ google / organic: 2,100 users, 45 conversions (2.1% CVR)
├─ facebook / paid: 1,300 users, 15 conversions (1.2% CVR)
├─ email / marketing: 280 users, 12 conversions (4.3% CVR) ⭐
├─ direct: 400 users, 8 conversions (2.0% CVR)
└─ Other: 1,720 users, 8 conversions (0.47% CVR)

Action: Scale email (Best CVR), optimize facebook ads
```

### 3.2 Shopee Analytics

**Available Metrics:**
```
1. Store overview:
   ├─ Monthly shop visit: Total customer visits
   ├─ Monthly sales: Revenue từ Shopee
   ├─ Monthly GMV: Gross merchandise value
   ├─ Rating: Shop rating (1-5 sao)
   └─ Response rate: Chat response time

2. Traffic Analytics:
   ├─ Traffic source: Homepage, Search, Collection, ...
   ├─ Search term: Khách search cái gì
   ├─ Popular search terms: Trending keywords
   └─ Traffic by device: Mobile vs desktop

3. Product Performance:
   ├─ Sales by product: Quantity + Revenue
   ├─ Views by product: Khách xem
   ├─ Conversion rate by product: (Sales / Views)
   ├─ Product rating: Average stars + # reviews
   ├─ Search rank: Position when searched keyword

4. Marketing Tools:
   ├─ Shopee Ads: Spend, clicks, sales, ROAS
   ├─ Vouchers: Discount codes, redemption rate
   ├─ Flash sale: One-time promotions, results
   ├─ Combo deals: Bundle sales
   └─ Free shipping: Threshold-based offers

Shopee Report Example (April):
├─ Store visits: 25,000 (+15% vs March)
├─ Sales: 80 orders, 150M revenue
├─ GMV: 180M (before discount)
├─ Conversion rate: 0.32% (low! Investigate)
├─ Avg order value: 1.875M (high, good)
├─ Response rate: 95% (Good)
├─ Rating: 4.7⭐ (Good)

Top 5 products:
├─ Áo trắng: 25 sales, 7.475M, 4.9⭐
├─ Váy hoa: 20 sales, 6.98M, 4.8⭐
├─ Quần kem: 15 sales, 4.485M, 4.7⭐
├─ Áo navy: 12 sales, 3.828M, 4.6⭐
└─ Váy đen: 8 sales, 2.792M, 4.8⭐

Shopee Ads performance:
├─ Daily budget: 2M
├─ Daily clicks: 1,200
├─ CPC: 1,667đ
├─ Daily sales: 10M
├─ ROAS: 5:1 (Excellent!)
├─ ACoS: 20% (Good)

Action: Keep Shopee Ads as top channel, scale budget
```

### 3.3 Lazada Analytics

**Available Metrics (Similar to Shopee):**
```
Dashboard:
├─ Orders: Total orders + Revenue
├─ Traffic: Store visits + Page views
├─ Conversion: Sales / Visits rate
├─ Vouchers: Discount code performance
├─ Lazada Flash/LazFlash: Promotion results

Lazada Report (April):
├─ Store visits: 18,000 (-5% vs March)
├─ Sales: 55 orders, 105M revenue
├─ Conversion rate: 0.30% (Lower than Shopee)
├─ Avg order value: 1.91M
├─ Rating: 4.6⭐

Top products on Lazada:
├─ Áo trắng: 18 sales, 5.382M
├─ Váy hoa: 12 sales, 4.188M
├─ Quần kem: 10 sales, 2.99M
...

⚠️ Issue: Lazada conversion lower than Shopee
├─ Possible cause: Price not competitive on Lazada
├─ Or: Product listing less optimized
└─ Action: Compare prices, update photos/descriptions
```

### 3.4 Facebook Ads Manager

**Key Reports:**
```
Breakdown by:
├─ Campaign: Overall performance
├─ Ad set: Targeting performance
├─ Ad: Creative performance (Which image/video best)
└─ Action: Which audience converts best

Main metrics:
├─ Impressions: # times ad shown
├─ Clicks: # people clicked
├─ CTR: % people who clicked
├─ CPC: Cost per click
├─ Amount spent: Total ad spend
├─ Conversions: # purchases
├─ Cost per conversion: Ad spend / Conversions
├─ ROAS: Revenue / Ad spend
├─ ACoS: Ad spend / Revenue (%)

Facebook Campaign Report (April):
Campaign: "Spring 25 Collection"
├─ Budget: 25M (April)
├─ Impressions: 800,000
├─ Clicks: 8,400 (1% CTR)
├─ CPC: 2,976đ
├─ Conversions (purchases): 84
├─ Cost per conversion: 297,619đ
├─ Revenue generated: 80M
├─ ROAS: 3.2:1
├─ ACoS: 31%

By audience segment:
├─ Women 25-34, Interest fashion: 35% of conversions ⭐
├─ Women 35-44: 28% of conversions
├─ Women 18-24: 22% of conversions
└─ Other: 15% of conversions

By placement:
├─ Feed: 50% of conversions (Best)
├─ Stories: 30% of conversions
├─ Reels: 15% of conversions
├─ Other: 5% of conversions

By creative:
├─ Video (Carousel): 40% conversions, $2.8K CTR ⭐
├─ Static image 1: 35% conversions
├─ Static image 2: 20% conversions
├─ Video 2: 5% conversions

Action: Scale "Women 25-34 + Feed + Carousel Video" combo
```

### 3.5 TikTok Analytics

**Available Metrics:**
```
Creator Fund / Business account:
├─ Video views: Total views across videos
├─ Followers: Account growth
├─ Engagement: Likes, comments, shares
├─ Engagement rate: (Engagement / Views)
├─ Followers growth: New followers per day
├─ Top performing videos: Highest views/engagement

TikTok Ads Manager (Nếu chạy ads):
├─ Campaign performance: Impressions, clicks, conversions
├─ Click through rate (CTR)
├─ Cost per click (CPC)
├─ Conversions (Using TikTok Pixel)
├─ Cost per acquisition (CPA)
└─ Return on ad spend (ROAS)

TikTok Report (April):
Organic:
├─ Total video views: 250,000
├─ Avg video views: 8,300
├─ Engagement rate: 3.2%
├─ Followers added: +450 (Good growth)
├─ Top video: "DIY outfit styling" - 45K views

TikTok Ads:
├─ Campaign: "Summer collection teaser"
├─ Budget: 10M (for April)
├─ Impressions: 500K
├─ Clicks: 4,200
├─ CTR: 0.84%
├─ CPC: 2,380đ
├─ Conversions (tracked via pixel): 30
├─ CPA: 333K
├─ Revenue: 30M
├─ ROAS: 3:1 (not great, should be 5:1+)

⚠️ Issues:
├─ ROAS too low (3:1 vs target 5:1)
├─ CPA too high (333K vs 200K target)
├─ CTR declining week over week
└─ Action: Redesign creative, test new audience

Better approach:
├─ TikTok Shop integration (Native checkout)
└─ Shoppable videos (Direct link to product)
```

## 4. Báo Cáo Theo Tần Suất

### 4.1 Daily Report (Morning - 10 phút)

**Format: Chat message hoặc Slack notification**

```
📊 Daily Report - April 3, 2025

💰 Revenue (Today)
├─ Target: 120M | Actual: 135M ✅ (+12.5%)
├─ Orders: 180 (+8% vs yesterday)
├─ AOV: 750K (vs 730K yesterday)

📈 Top Products (Today)
1. Áo trắng: 35 sales, 10.3M revenue
2. Váy hoa: 28 sales, 9.8M revenue
3. Quần kem: 22 sales, 6.6M revenue

🎯 Conversion
├─ Traffic: 11.2K sessions (+5%)
├─ CVR: 1.61% (vs 1.49% yesterday)

⚠️ Alerts
├─ Váy đen stock: 12 cái (selling 8/day, reorder!)
├─ Support tickets pending: 3 (All < 1h old)
└─ No major issues

Target Progress: Revenue 2.85B / 2.5B (Feb target) = 114% ✅
```

### 4.2 Weekly Report (Monday - 30 phút)

**Format: Google Sheets / Excel / PDF**

```
WEEKLY REPORT - Week of April 1-7, 2025

📊 OVERVIEW
└─ Revenue: 960M | Target: 875M | Growth: +9.7% ✅

TRAFFIC & CONVERSION
├─ Total sessions: 42,500
├─ New users: 18,200 (43%)
├─ Conversion rate: 1.37%
├─ Customers acquired: 420
├─ CAC: 202K (Good!)

REVENUE BREAKDOWN
├─ Shopee: 320M (33%)
├─ Lazada: 280M (29%)
├─ Website: 200M (21%)
├─ Zalo: 160M (17%)

MARKETING PERFORMANCE
├─ Total ad spend: 35M
├─ ROAS (weighted): 4.1:1
├─ Best channel: Email (8.9x ROAS)
├─ Worst channel: TikTok (2.3x ROAS)

PRODUCT PERFORMANCE
├─ Best seller: Áo trắng (185 units)
├─ Best margin: Phụ kiện (60% margin)
├─ Most returned: Quần short (4% return rate)

OPERATIONS
├─ Order fulfillment: 95% < 24h (Target: 100%)
├─ On-time delivery: 97.8% (Target: 95%)
├─ Return rate: 2.1% (Target: < 3%)

CUSTOMER SATISFACTION
├─ CSAT: 4.4/5
├─ NPS: 52 (Good!)
├─ Chat response time: 2.3 min

💡 ACTION ITEMS FOR NEXT WEEK
├─ Reorder low-stock items
├─ Redesign TikTok ads (ROAS too low)
├─ A/B test new email template
└─ Optimize Lazada pricing
```

### 4.3 Monthly Report (1st of month - 2 hours)

**Format: Comprehensive deck or document**

**Part 1: Executive Summary**
```
MARCH 2025 PERFORMANCE

KPIs:
├─ Revenue: 28.5B | Target: 25B | YoY growth: +18% ✅
├─ Profit: 3.2B (11.2% margin)
├─ Customers: 15,400 (New: 8,200, Repeat: 7,200)
├─ CAC: 218K | LTV: 14.8M | LTV/CAC: 68x ✅
├─ Conversion rate: 1.45% (Target: 1.5%)

Growth vs targets:
├─ Revenue: +14% (Target: +12%) ✅
├─ Profit: +12% (Target: +10%) ✅
├─ Traffic: +20% (Target: +15%) ✅
└─ Conversion: -0.05pp (Target: flat) ❌

Key achievements:
├─ Launched new product line (Váy summer) - 8K sales
├─ Grew email subscribers to 45K (from 35K)
├─ ROAS improvement: 3.8 → 4.1x
└─ Return rate down to 2.1% (from 2.5%)

Key challenges:
├─ TikTok ROAS decline (3.2x → 2.3x)
├─ Facebook ACoS increase (28% → 31%)
└─ Inventory stockout: Váy hoa (last week)
```

**Part 2: Detailed Analytics**

```
TRAFFIC & CONVERSIONS
├─ Total sessions: 185,000 (+20% vs Feb)
├─ New users: 92,000 (+22%)
├─ Returning users: 93,000 (+18%)
├─ Conversion rate: 1.45% (vs 1.40% Feb) ⬆️
├─ Orders: 2,680 (+15% vs Feb)
├─ Cart abandonment: 89% (High - needs fixing)

REVENUE ANALYSIS
├─ GMV: 30.2B (before discount)
├─ Discounts: -2.8B (9.3%)
├─ Net sales: 27.4B
├─ Returns/refunds: -1.2B (4.4%)
├─ Revenue: 26.2B
├─ COGS: -10.2B (39%)
├─ Gross profit: 16B (61%)
├─ Operating expenses: -13B (50% of gross profit)
├─ Net profit: 3B (11.5%)

REVENUE BY CHANNEL
├─ Shopee: 8.5B (31%)
├─ Lazada: 7.8B (28%)
├─ Website: 6.2B (22%)
├─ Zalo: 3.7B (13%)
├─ Other: 0.8B (3%)

MARKETING SPEND & ROI
├─ Total spend: 3.9B (15% of revenue)
├─ Facebook Ads: 1.5B | Revenue: 4.5B | ROAS: 3.0x | ACoS: 33%
├─ Google Ads: 1.0B | Revenue: 5.8B | ROAS: 5.8x | ACoS: 17%
├─ Email: 0.15B | Revenue: 1.8B | ROAS: 12x | ACoS: 8%
├─ TikTok: 0.65B | Revenue: 1.5B | ROAS: 2.3x | ACoS: 43%
├─ Zalo Ads: 0.5B | Revenue: 1.6B | ROAS: 3.2x | ACoS: 31%
└─ Influencer: 0.1B | Revenue: 0.5B | ROAS: 5x | ACoS: 20%

PRODUCT PERFORMANCE
Top 10 best sellers:
├─ Áo trắng: 420 units, 118M revenue, 4.9⭐
├─ Váy hoa: 380 units, 132.5M revenue, 4.8⭐
├─ Quần kem: 320 units, 95.8M revenue, 4.7⭐
├─ Áo navy: 280 units, 89.2M revenue, 4.6⭐
├─ Váy đen: 210 units, 73.5M revenue, 4.8⭐
...

Worst performers:
├─ Áo denim: 25 units, 5.6M revenue, 4.2⭐ (Seasonal?)
├─ Quần short: 45 units, 8.1M revenue, 3.9⭐ (Timing?)
└─ Phụ kiện (low priority): 95 units, 7.6M revenue, 3.8⭐

CUSTOMER METRICS
├─ Total customers: 15,400 (+12% vs Feb)
├─ New customers: 8,200 (+18%)
├─ Repeat customers: 7,200 (+5%)
├─ Repeat purchase rate: 46.8% (Target: 50%)
├─ Avg customer value: 1.88M
├─ LTV: 14.8M (vs CAC 218K)

RETENTION COHORTS
Cohort (month) | Month 0 | Month 1 | Month 2 | Month 3 |
|---|---|---|---|---|
Jan | 1,800 | 720 (40%) | 360 (20%) | 216 (12%) |
Feb | 2,000 | 800 (40%) | 400 (20%) | - |
Mar | 2,200 | 880 (40%) | - | - |

→ Retention is stable at 40% month 1, 20% month 2
→ Target should be 45%+ (Need to improve)

OPERATIONS
├─ Orders fulfilled < 24h: 95% (Target: 100%)
├─ On-time delivery: 97.8% (Target: 95%)
├─ Return rate: 2.3% (Target: < 3%)
├─ Refund processing: 3.2 days (Target: 2 days)
├─ Support CSAT: 4.4/5
├─ NPS: 51 (Good)
```

**Part 3: Insights & Recommendations**

```
💡 KEY INSIGHTS

1️⃣ Revenue growth is accelerating
   ├─ Month-on-month: +14% (strong!)
   ├─ Year-on-year: +18%
   ├─ Driven by: Traffic growth + Repeat purchase increase
   └─ Momentum: Continues (Early April +12% already)

2️⃣ Marketing efficiency is improving
   ├─ Overall ROAS: 4.1x (was 3.8x in Feb)
   ├─ Best channel: Email (12x ROAS, only 3.8% of budget)
   ├─ CAC trending down: 220K → 218K
   └─ ROAS distribution: Email >> Google > Zalo > Facebook > TikTok

3️⃣ Repeat purchase rate is key opportunity
   ├─ Current: 46.8%
   ├─ Benchmark: 50%+ (High growth stores)
   ├─ Value: 5% improvement = +800K revenue potential
   └─ Actions: Better post-purchase experience, loyalty program

4️⃣ TikTok underperforming significantly
   ├─ ROAS: 2.3x (vs 5:1 target)
   ├─ ACoS: 43% (vs 20% target)
   ├─ Burn rate: 0.65B/month (too much)
   └─ Action: Redesign or pause

5️⃣ Inventory management needs improvement
   ├─ Váy hoa: Stockout last week (Lost 15K+ revenue)
   ├─ Quần short: Slow moving (Reconsider SKU)
   └─ Action: Forecast by product, use safety stock

📋 RECOMMENDATIONS FOR APRIL

HIGH PRIORITY (Do this month):
├─ Scale Google Ads (+30% budget from TikTok)
├─ Expand email program (12x ROI, underutilized)
├─ Improve repeat purchase rate:
│  ├─ Create loyalty program (5% discount for repeat)
│  ├─ Post-purchase sequence (Day 1, 7, 30)
│  └─ Seasonal recommendations
├─ Fix TikTok or reallocate (ROAS too low)
└─ Better inventory forecasting (Prevent stockouts)

MEDIUM PRIORITY (Next 2 months):
├─ Improve Facebook ACoS (31% → 25%)
├─ Optimize product mix (Phase out slow movers)
├─ Add new payment methods (More checkout options)
├─ Implement chatbot on website (Reduce cart abandonment)
├─ Create VIP customer program (High value retention)
└─ A/B test pricing strategy

LONG TERM (Quarterly goals):
├─ Expand to new platforms (Tiktok Shop, etc)
├─ Build owned audience (Email to 100K)
├─ Improve supply chain efficiency
├─ Launch private label products (Better margins)
└─ Consider franchise/wholesale model
```

## 5. Phân Tích Nâng Cao

### 5.1 Cohort Analysis (Theo Tháng Mua Đầu)

```
Cohort Analysis Table:
Cohort | Total | Month 1 | Month 2 | Month 3 | Month 4 | Month 5 |
|---|---|---|---|---|---|---|
Jan | 2,000 | 800 (40%) | 400 (20%) | 240 (12%) | 144 (7.2%) | 86 (4.3%) |
Feb | 2,400 | 960 (40%) | 480 (20%) | 288 (12%) | ? | ? |
Mar | 2,800 | 1,120 (40%) | 560 (20%) | ? | ? | ? |

Reading:
├─ Jan cohort: 2,000 new customers
├─ Month 1 (Feb): 800 khách quay lại (40% retention)
├─ Month 2 (Mar): 400 khách quay lại (20% of original, 50% of month 1)
├─ Month 3 (Apr): 240 khách quay lại
└─ Trend: Declining but stabilizing (7-4% after month 2)

Interpretation:
├─ First month retention (40%) is standard
├─ Second month drops to 50% (Normal)
├─ Third month stabilizes at 60% of month 2 (Good)
├─ Goal: Improve month 1 retention from 40% → 50%+

How to improve:
├─ Better onboarding (Welcome sequence)
├─ Free gift with first purchase (Surprise & delight)
├─ Post-purchase communication (Order updates, tips)
├─ Loyalty program (Reward repeat purchase)
├─ Exclusive offers for repeat customers
└─ Product quality guarantee (Reduce returns)
```

### 5.2 RFM Analysis (Recency, Frequency, Monetary)

**Purpose: Segment customers into value tiers**

```
RFM Definition:
├─ R (Recency): Days since last purchase (0 = today, 365 = 1 year ago)
├─ F (Frequency): # of purchases (lifetime)
└─ M (Monetary): Total spent (lifetime)

Scoring (1-5, 5 = best):
├─ R: 1 (365+ days ago) to 5 (0-30 days)
├─ F: 1 (1 purchase) to 5 (10+ purchases)
├─ M: 1 (< 500K spent) to 5 (> 5M spent)

RFM Segments:
```
| Segment | Criteria | Action | Priority |
|---------|----------|--------|----------|
| Champions | R 4-5, F 4-5, M 4-5 | Loyalty rewards, VIP treatment | 🔴 High |
| Loyal customers | R 3-5, F 3-5, M 3-5 | Exclusive offers, referral | 🔴 High |
| Potential loyalists | R 4-5, F 2-3, M 2-3 | Personalized recommendations | 🟠 Medium |
| At risk | R 2-3, F 2-5, M 2-5 | Win-back campaigns | 🟠 Medium |
| Can't lose them | R 1-2, F 5, M 5 | Urgent re-engagement | 🔴 High |
| Hibernating | R 1, F any, M any | Seasonal reactivation | 🟢 Low |
| New customers | R 5, F 1, M 1-2 | Onboarding, nurture | 🟠 Medium |
| Lost | R 1, F 1, M 1 | Don't spend on, focus elsewhere | 🟢 Low |

Example:
Customer A: R=5 (bought 5 days ago), F=8 (8 purchases), M=18M
→ RFM score: 5+8+18 (high) → CHAMPION
→ Action: Invite to VIP program, exclusive pre-launch

Customer B: R=2 (30 days without purchase), F=1 (1 purchase), M=1.2M
→ RFM score: 2+1+1.2 (low) → AT RISK / NEW CUSTOMER
→ Action: Send "Welcome back" + 15% discount email

Customer C: R=1 (180 days), F=5 (5 purchases), M=8M
→ RFM score: 1+5+8 (high recency is bad, but high frequency/monetary)
→ CAN'T LOSE THEM
→ Action: URGENT - Personal email from CEO, special offer
```

### 5.3 Attribution Modeling

**Purpose: Understand which touchpoint deserves credit for purchase**

```
Attribution Models:

1. FIRST-TOUCH ATTRIBUTION (100% credit to first touchpoint)
   Customer journey:
   ├─ Day 1: See Facebook ad → Click → Browse
   ├─ Day 3: Search Google → Click → Browse
   ├─ Day 5: Click email link → Purchase
   └─ Credit: 100% to Facebook (first touch)

   Problem: Facebook didn't close the sale
   Use case: Awareness campaigns

2. LAST-TOUCH ATTRIBUTION (100% credit to last touchpoint)
   Same journey:
   └─ Credit: 100% to Email (last touch)

   Problem: Ignores the other touchpoints that led to purchase
   Use case: Conversion tracking (but misleading)

3. LINEAR ATTRIBUTION (Equal credit to all touchpoints)
   Same journey, 3 touchpoints:
   ├─ Facebook: 33%
   ├─ Google: 33%
   └─ Email: 33%

   Problem: Assumes equal importance (not true)
   Use case: Fair distribution baseline

4. TIME-DECAY ATTRIBUTION (More credit to recent touchpoints)
   Same journey:
   ├─ Facebook (Day 1): 10% (oldest)
   ├─ Google (Day 3): 30% (middle)
   └─ Email (Day 5): 60% (most recent)

   Assumption: Touchpoint closer to conversion is more important
   Use case: Conversion-focused understanding

5. POSITION-BASED / U-SHAPED ATTRIBUTION (Credit to first & last)
   Same journey:
   ├─ Facebook (first): 40%
   ├─ Google (middle): 20%
   └─ Email (last): 40%

   Logic: First touch creates awareness, last touch closes
   Use case: Most realistic for most businesses

6. MACHINE LEARNING / DATA-DRIVEN ATTRIBUTION (Google's recommended)
   Google analyzes historical data:
   ├─ Which touchpoints convert best
   ├─ Weight assigned based on real impact
   └─ Example result:
      ├─ Facebook: 25% (Awareness, but lower conversion rate)
      ├─ Google: 45% (High conversion rate)
      └─ Email: 30% (Best conversion rate, but dependent on earlier touchpoints)

GA4 attribution models:
You can select in GA4 → Reports → Attribution
├─ Last click (default in GA3, but less accurate)
├─ First touch
├─ Linear
├─ Position-based
└─ Time-decay (GA4 default)

How to use in practice:
├─ Awareness campaigns: Use first-touch attribution
├─ Optimization: Use last-touch or position-based
├─ Budget allocation: Use data-driven/ML attribution
└─ Most reliable: Test all, compare results
```

### 5.4 Unit Economics

**Purpose: Understand profitability per customer/unit**

```
UNIT ECONOMICS FORMULA:

Monthly metrics:
├─ Orders: 2,680
├─ Revenue: 26.2B
├─ COGS: 10.2B (39%)
├─ Gross profit: 16B (61%)
├─ Gross profit per order: 16B / 2,680 = 5.97M

│
│ MINUS: Variable costs per order
│
├─ Platform fees (Shopee, Lazada): 2.3B → Per order: 857K
├─ Shipping cost: 2.8B → Per order: 1.04M
├─ Packaging & handling: 0.6B → Per order: 224K
├─ Payment processing: 0.4B → Per order: 149K
├─ Customer support: 0.5B → Per order: 186K
│
├─ Variable cost per order: 2.46M
├─ Contribution margin per order: 5.97M - 2.46M = 3.51M (13% of AOV)

│
│ MINUS: Fixed costs (amortized per order)
│
├─ Salaries & team: 5B/month → Per order: 1.87M
├─ Rent, utilities: 0.5B/month → Per order: 186K
├─ Software & tools: 0.3B/month → Per order: 112K
├─ Marketing (if allocated): 3.9B → Per order: 1.45M
│
├─ Fixed cost per order: 3.61M
├─ Net profit per order (before allocation): 3.51M - 3.61M = -0.1M ❌

⚠️ ISSUE: Fixed cost allocation is too high!
This is why you can't track profit per order easily.

BETTER APPROACH: Contribution margin analysis
├─ Revenue per order: 9.77M
├─ COGS: -3.81M
├─ Platform fees: -0.86M
├─ Shipping: -1.04M
├─ Packaging: -0.22M
├─ Payment processing: -0.15M
├─ Customer support: -0.19M
│
├─ Contribution margin: 3.5M (36% of AOV) ✅
│
├─ This contribution pays for fixed costs:
│   └─ Fixed cost per order: 3.61M (39% of AOV)
│
├─ Result: Operating loss of -0.11M per order
│
├─ BUT: Accumulated contribution across all orders (2,680 x 3.5M) = 9.38B
├─ Fixed costs: 6.7B
├─ Net profit: 9.38B - 6.7B = 2.68B ✅ (Positive!)

INTERPRETATION:
├─ Each order contributes 3.5M to fixed costs & profit
├─ With fixed costs of 6.7B, need 1,914 orders to break even
├─ Have 2,680 orders, so profit = (2,680 - 1,914) x 3.5M = 2.68B
├─ Add back COGS profit, actual profit is 3.2B ✅

UNIT ECONOMICS DASHBOARD:
│
├─ AOV: 9.77M
├─ COGS %: 39%
├─ Gross margin: 61%
├─ Variable cost %: 25%
├─ Contribution margin: 36%
├─ Contribution per order: 3.5M
├─ Variable cost per order: 2.46M
├─ CAC: 0.22M (Marketing + acquisition)
├─ CAC payback: 1.3 months (Excellent!)
├─ LTV (3 months repeat): 15M
├─ LTV / CAC: 68x (Excellent!)

What does it mean:
├─ Healthy business: Contribution margin > 20% ✅ (You're at 36%)
├─ CAC payback < 6 months ✅ (You're at 1.3 months)
├─ LTV/CAC > 3:1 ✅ (You're at 68:1)
└─ All green lights! 🚀
```

### 5.5 Basket Analysis (Sản phẩm mua cùng)

```
Purpose: Understand which products are frequently bought together
→ Use for bundle offers, recommendations, merchandising

Frequently co-purchased pairs (March 2025):
├─ Áo trắng + Quần kem: 85 co-purchases (18% of áo trắng buyers)
│  └─ Bundle discount potential: 20% combo
│
├─ Váy hoa + Thắt lưng: 42 co-purchases (11% of váy hoa buyers)
│  └─ Bundle potential: Khó, belt giá cao
│
├─ Quần kem + Áo navy: 38 co-purchases (12% of quần kem buyers)
│  └─ Bundle potential: Good match
│
├─ Áo basic + Phụ kiện: 28 co-purchases (6% of áo buyers)
│  └─ Bundle potential: Lợi nhuận cao (60% margin phụ kiện)
│
└─ Váy đen + Giày (external product): 15 co-purchases
   └─ Partnership opportunity: Cross-promote with shoe brand

3-product baskets:
├─ Áo + Quần + Áo khác: 22 (6% of 3+ item orders)
├─ Váy + Belt + Bag: 15 (4% of 3+ item orders)
└─ Mixed colors/sizes: Common (Good for repeat purchase)

ACTION ITEMS:
├─ Create bundle: Áo + Quần = Save 15%
├─ Recommend after: "Frequently bought together"
├─ Suggest complements: At checkout
├─ Influencer bundles: Partner with fashion bloggers
└─ Email recommendations: Based on purchase history
```

## 6. Benchmarks TMĐT Việt Nam (Theo Ngành)

```
| Metric | Fashion | Electronics | Food | Books | Beauty |
|--------|---------|-------------|------|-------|--------|
| Conversion rate | 1.5-2.5% | 0.8-1.5% | 2-3% | 0.5-1% | 2-3% |
| AOV | 800-1.2M | 3-8M | 300-500K | 200-400K | 500-800K |
| Cart abandon | 60-75% | 70-85% | 55-70% | 50-65% | 60-75% |
| Return rate | 2-5% | 5-8% | 1-3% | 2-4% | 3-6% |
| Repeat rate | 30-40% | 20-35% | 25-40% | 35-50% | 40-50% |
| Email CVR | 2-4% | 1-2% | 2-3% | 1-2% | 2-3% |
| Organic %sales | 30-40% | 35-45% | 25-35% | 30-40% | 25-35% |
| Paid % sales | 35-50% | 40-60% | 40-60% | 25-40% | 45-65% |
| Avg margin | 40-50% | 15-25% | 50-70% | 20-35% | 50-70% |
| Shipping cost% | 8-12% | 10-15% | 15-20% | 10-15% | 5-8% |

Use these to benchmark YOUR store:
├─ If your conversion > benchmark: Optimize AOV
├─ If conversion < benchmark: Fix product pages, reduce friction
├─ If margin < benchmark: Review pricing or COGS
└─ If return rate > benchmark: Quality or expectations issue
```

---

## 7. Action Framework: Data → Insight → Action → Measure

```
WEEKLY ANALYTICS WORKFLOW:

STEP 1: COLLECT (Monday morning)
├─ Pull dashboard data for week 1-7 April
├─ Check GA4, Shopee, Lazada, Facebook Ads
├─ Export to sheets for analysis
└─ Time: 30 min

STEP 2: ANALYZE (Monday 10am)
├─ Calculate week-over-week changes
├─ Compare vs target/last month
├─ Identify anomalies
│  ├─ Traffic up 25%? Why?
│  ├─ CVR down 0.5%? Why?
│  ├─ Revenue up but profit down? Cost issue?
│
├─ Drill down into channels/products
└─ Time: 45 min

STEP 3: INSIGHT (Monday 11am)
├─ Summarize findings:
│  ├─ What went well (celebrate!)
│  ├─ What went poorly (investigate)
│  └─ What's the story in data?
│
├─ Examples:
│  ├─ "Email is best ROI but we spend only 5% of budget"
│  ├─ "TikTok declining, Facebook stable, Google up"
│  ├─ "Váy hola trending (+30% week-over-week)"
│  └─ "Repeat rate still below target (46% vs 50%)"
│
└─ Time: 30 min

STEP 4: ACTION (Monday 1pm)
├─ Decide on 3-5 actions:
│  ├─ HIGH impact: Scale email, pause TikTok
│  ├─ MEDIUM: Reorder stock, optimize Facebook
│  └─ LOW: Test new emails, update product photos
│
├─ Assign owners & deadlines:
│  ├─ "Alice: Email campaign by Wed"
│  ├─ "Bob: TikTok analysis by Friday"
│  └─ "Charlie: Inventory reorder by Tuesday"
│
├─ Expected outcome:
│  ├─ Email scale: +10% revenue potential
│  ├─ Stock fix: Prevent 5K+ lost sales
│  └─ Facebook: -5% ACoS potential
│
└─ Time: 30 min

STEP 5: MEASURE (Next Monday)
├─ Track whether actions were taken
├─ Measure impact:
│  ├─ Did email scale happen? (Yes/No)
│  ├─ What was revenue impact?
│  ├─ Was TikTok paused? (How long?)
│  └─ Did repeat rate improve?
│
├─ Adjust if needed:
│  ├─ If no improvement, try different approach
│  ├─ If improvement slower than expected, accelerate
│  └─ If faster improvement, scale more
│
└─ Time: 30 min (included in weekly review)
```
