---
name: ecom-funnel-builder
description: >
  Thiết kế phễu bán hàng e-commerce đa kênh. Bao gồm 5 loại phễu (sản phẩm vật lý, flash sale, lead magnet, retargeting, loyalty), TOFU/MOFU/BOFU, customer journey mapping, touchpoints, metrics, automation triggers, retargeting strategies, phễu Shopee/Lazada, budget allocation, conversion benchmarks VN.

  Dùng skill này khi: "thiết kế phễu bán hàng", "funnel TMĐT", "customer journey", "funnel conversion", "lên kế hoạch phễu", "retargeting strategy"
---

# SKILL: Thiết Kế Phễu Bán Hàng E-commerce Đa Kênh

## I. GIỚI THIỆU

Phễu bán hàng (sales funnel) là journey mà khách hàng đi qua từ lúc biết đến sản phẩm cho đến khi mua hàng. Mục đích: Convert người xem thành khách hàng mua hàng, và tối đa hóa giá trị mỗi khách hàng.

Trong e-commerce, phễu phức tạp hơn vì:
- **Đa kênh**: Facebook, Instagram, TikTok, Shopee, Lazada, Website riêng, Email
- **Nhiều touchpoints**: Ads → Landing page → Checkout → Email → Retargeting
- **Retargeting phức tạp**: Dynamic audiences, behavioral triggers
- **Mobile-first**: 90% traffic từ điện thoại

---

## II. 5 LOẠI PHỄU TMĐT & CẤU TRÚC TOFU/MOFU/BOFU

### Loại Phễu 1: Phễu Sản Phẩm Vật Lý (Physical Product Funnel)

Dùng để: Bán sản phẩm tangible (quần áo, phụ kiện, electronics, beauty)

**Cấu trúc TOFU/MOFU/BOFU**:

```
┌─────────────────────────────────────────────────────┐
│ AWARENESS (TOFU)                                     │
│ Mục đích: Khách biết đến sản phẩm của bạn           │
│                                                      │
│ Channels: Facebook Ads, TikTok Ads, Instagram Ads  │
│ Content: Viral content, trending videos, ads       │
│ Metrics: Reach, CPM, Impressions                   │
│ Conversion: Ad → Click (CTR 2-5%)                 │
└──────────────┬──────────────────────────────────────┘
               │
               ↓
┌─────────────────────────────────────────────────────┐
│ CONSIDERATION (MOFU)                                │
│ Mục đích: Khách xem chi tiết sản phẩm              │
│                                                      │
│ Landing page: Product info, reviews, pricing       │
│ Content: Product video, images, testimonials       │
│ Metrics: Page view, scroll depth, time on page     │
│ Conversion: Click → Product page view (70-80%)    │
└──────────────┬──────────────────────────────────────┘
               │
               ↓
┌─────────────────────────────────────────────────────┐
│ DECISION (BOFU)                                      │
│ Mục đích: Khách quyết định mua hàng                │
│                                                      │
│ Channels: Checkout page, Shopee, Lazada           │
│ Content: Limited offer, social proof, reviews     │
│ Metrics: Add to cart, checkout rate, conversion   │
│ Conversion: Product page → Checkout (1-3%)        │
└──────────────┬──────────────────────────────────────┘
               │
               ↓
    ┌──────────────────────┐
    │ CUSTOMER (POST-SALE) │
    │ Email follow-up      │
    │ Upsell/Cross-sell    │
    │ Loyalty program      │
    └──────────────────────┘
```

**Chi tiết từng giai đoạn**:

**TOFU (Top of Funnel)**:
- **Objective**: Get awareness, clicks
- **Ad spend**: 40-50% of budget
- **Audience**: Cold audience, broad interests
- **Metrics**: CPM $0.50-2, CTR 2-4%
- **Content types**:
  * Teaser videos (trending sounds)
  * Product showcase (quick demos)
  * Educational content
  * Before-after
  * Problem-agitate-solve ads
- **CPA (Cost per add to cart)**: $0.50-2
- **Target**: Get 1000+ people to product page

**MOFU (Middle of Funnel)**:
- **Objective**: Build interest, comparison
- **Landing page**: Optimize for conversions
- **Metrics**: Average CTR to checkout: 5-10%
- **Content**:
  * Detailed product videos (2-3 min)
  * Customer testimonials
  * Product comparisons
  * Detailed specs/benefits
  * FAQ section
  * Social proof (reviews, rating)
- **Reviews importance**: 95% khách đọc reviews trước mua
- **Rating requirement**: 4.5+ stars → higher conversion
- **Target**: 50-100 people add to cart

**BOFU (Bottom of Funnel)**:
- **Objective**: Convert to purchase
- **Checkout optimization**:
  * Minimize form fields (name, email, phone, address)
  * Clear pricing + no hidden fees
  * Multiple payment options (COD, bank transfer, e-wallet)
  * Progress bar (Step 1/2/3)
  * Trust badges (SSL, verified seller)
  * Fast checkout (express option)
- **Metrics**:
  * Checkout rate: 20-40% of add to carts
  * Cart abandonment rate: 60-80%
- **Conversion rate: BOFU** 1-3%
- **Post-purchase**:
  * Order confirmation email
  * Shipping tracking
  * Product care tips
  * Upsell email
  * Review request (after 7 days)

---

### Loại Phễu 2: Phễu Flash Sale (Time-Limited Offer)

Dùng để: Bán hàng nhanh, tạo urgency, move inventory

**Cấu trúc phễu**:

```
┌──────────────────────────────────┐
│ Announcement Phase (3-5 days)     │
│ - Teaser: "Sắp có flash sale"    │
│ - Build anticipation             │
│ - Early bird: limited access      │
└───────────────┬──────────────────┘
                │
                ↓
┌──────────────────────────────────┐
│ Countdown Phase (24-48 hours)     │
│ - Countdown timer                │
│ - Limited quantity remaining      │
│ - Urgency messaging               │
│ - Email reminders                 │
└───────────────┬──────────────────┘
                │
                ↓
┌──────────────────────────────────┐
│ Flash Sale Live Phase             │
│ - Real-time: quantity left        │
│ - Notification push               │
│ - Multiple touchpoints            │
│ - Social media live              │
└───────────────┬──────────────────┘
                │
                ↓
┌──────────────────────────────────┐
│ Upsell Phase (Post-Purchase)      │
│ - "You also bought..."            │
│ - Complementary products          │
│ - Bundle deals                    │
└──────────────────────────────────┘
```

**Metrics Flash Sale**:
- **Conversion rate**: 3-8% (much higher than regular)
- **Average order value**: Often higher due to upsell
- **Inventory turnover**: 10x faster
- **Revenue per day**: 5-10x higher than normal

**Campaign timeline**:
- **Day 1-2**: Announce, build anticipation
- **Day 3-5**: Countdown, email reminders
- **Day 6-7**: FLASH - Live sale
- **Day 8**: Upsell phase, second chance emails

---

### Loại Phễu 3: Phễu Lead Magnet (Lead Generation)

Dùng để: Collect email, build list, nurture leads

**Cấu trúc phễu**:

```
┌──────────────────────┐
│ Ad (Free + Value)    │
│ "Download free      │
│  guide" / "Quiz"    │
└──────┬───────────────┘
       │
       ↓
┌──────────────────────┐
│ Landing page         │
│ Simple form:         │
│ - Email (required)   │
│ - Name (optional)    │
│ - Phone (optional)   │
│ CTA: Get access     │
└──────┬───────────────┘
       │
       ↓
┌──────────────────────┐
│ Deliver resource     │
│ - PDF guide          │
│ - Checklist         │
│ - Video             │
│ - Discount code     │
└──────┬───────────────┘
       │
       ↓
┌──────────────────────┐
│ Email sequence       │
│ - Welcome            │
│ - Value emails       │
│ - Soft sell         │
│ - Hard sell         │
└──────────────────────┘
```

**Lead magnet ideas cho TMĐT VN**:
- "10 cách chọn quần áo phù hợp" (PDF guide)
- "Skincare quiz: Tìm lotion phù hợp cho bạn"
- "Size guide interactive" (tool)
- "Style guide" (PDF)
- "$10 discount code" (free money)
- "7-day email course: How to style"

**Metrics Lead Magnet**:
- **Conversion rate**: 10-20% (higher than product funnel)
- **Cost per lead**: $0.10-0.50
- **Email list growth**: 100-500 leads/week
- **Nurture conversion**: 5-10% lead → customer

**Email sequence (5-7 emails)**:
- **Email 1 (Immediate)**: Deliver resource, thank you
- **Email 2 (Day 2)**: Value email, tips
- **Email 3 (Day 4)**: Value email, case study
- **Email 4 (Day 6)**: Story-driven, social proof
- **Email 5 (Day 8)**: Soft sell, problem/solution
- **Email 6 (Day 10)**: Hard sell, offer, CTA
- **Email 7 (Day 12)**: Final chance, urgency

---

### Loại Phễu 4: Phễu Retargeting (Remarketing)

Dùng để: Convert những khách đã xem nhưng chưa mua

**Cấu trúc phễu**:

```
┌────────────────────────────┐
│ Event 1: Visited website   │
│ Pixeled user               │
│ Action: Retargeting ads    │
└────────┬───────────────────┘
         │
         ↓
┌────────────────────────────┐
│ Event 2: Viewed product    │
│ Category pixel             │
│ Action: Show product ads   │
└────────┬───────────────────┘
         │
         ↓
┌────────────────────────────┐
│ Event 3: Viewed multiple   │
│ products (browsing)        │
│ Action: Carousel ads       │
└────────┬───────────────────┘
         │
         ↓
┌────────────────────────────┐
│ Event 4: Added to cart     │
│ Heavy intent signal        │
│ Action: Incentive ads      │
│ "Use code: SAVE10"        │
└────────┬───────────────────┘
         │
         ↓
┌────────────────────────────┐
│ Event 5: Initiated checkout│
│ Highest intent             │
│ Action: Urgency ads        │
│ "Complete your purchase"  │
└────────┬───────────────────┘
         │
         ↓
┌────────────────────────────┐
│ Event 6: Completed purchase│
│ Action: Thank you ads      │
│ Upsell + Loyalty          │
└────────────────────────────┘
```

**Retargeting audiences by behavior**:

| Behavior | Audience | Bid | Message | Offer |
|----------|----------|-----|---------|-------|
| Viewed site | Very broad | Low | "Come back" | None |
| Viewed 1 product | Specific product | Medium | "Still interested?" | Maybe discount |
| Viewed 3+ products | Browsers | Medium | "Still deciding?" | 10% discount |
| Added to cart | High intent | High | "You left something" | "Secure checkout" |
| Initiated checkout | Very high | Highest | "Complete order now" | "10% off now" |
| Never bought | All | Low | "Browse more" | Free shipping |

**Retargeting metrics**:
- **Conversion rate**: 2-5% (2-3x higher than cold)
- **ROAS**: 3-8:1 (very profitable)
- **Cost per conversion**: $1-3 (vs $5-10 for cold)
- **Frequency capping**: Max 2-3 ads/day per user

**Retargeting duration**:
- **Standard**: 30 days (site visitors)
- **Product viewers**: 60 days
- **Cart abandoners**: 7 days (urgent)
- **Past purchasers**: Ongoing (loyalty)

---

### Loại Phễu 5: Phễu Loyalty (Customer Retention)

Dùng để: Keep customers coming back, increase LTV

**Cấu trúc phễu**:

```
┌─────────────────────────────┐
│ Post-Purchase (Day 1-3)     │
│ - Order confirmation        │
│ - Shipping tracking         │
│ - Product care tips         │
└────────┬────────────────────┘
         │
         ↓
┌─────────────────────────────┐
│ Delivery & Unboxing (Day 3-7)│
│ - Delivery notification     │
│ - Unboxing tips             │
│ - How to use tips           │
└────────┬────────────────────┘
         │
         ↓
┌─────────────────────────────┐
│ Review Request (Day 7-14)   │
│ - "How's your product?"     │
│ - Request review            │
│ - Incentivize ($2 discount) │
└────────┬────────────────────┘
         │
         ↓
┌─────────────────────────────┐
│ Loyalty Program (Ongoing)   │
│ - Points for purchase       │
│ - Points for review         │
│ - Referral rewards          │
└────────┬────────────────────┘
         │
         ↓
┌─────────────────────────────┐
│ Repeat Purchase (Day 30+)   │
│ - "You might need again"    │
│ - Complementary products    │
│ - Exclusive member offers   │
└────────┬────────────────────┘
         │
         ↓
┌─────────────────────────────┐
│ Upgrade/Upsell (Day 60+)    │
│ - Premium version           │
│ - Bundle deals              │
│ - VIP membership            │
└─────────────────────────────┘
```

**Loyalty program mechanics**:
- **Points system**: 1 đồng mua = 1 điểm
- **Rewards**:
  * 10 points = $1 discount
  * 100 points = $10 discount
  * 500 points = $50 discount + free shipping
- **Tier system**: Bronze → Silver → Gold
  * Gold: 10% discount, free shipping, early sale access
- **Referral**: "Refer a friend, get $5 each"

**Retention email sequence**:
- **Email 1 (Day 1)**: Order confirmation + tracking
- **Email 2 (Day 5)**: "How to use" guide, care tips
- **Email 3 (Day 10)**: Review request + incentive
- **Email 4 (Day 20)**: New products, trending
- **Email 5 (Day 30)**: "Time to reorder", reminder
- **Email 6 (Day 45)**: VIP member exclusive offer
- **Email 7 (Day 60)**: Upsell, complementary products

**Retention metrics**:
- **Repeat purchase rate**: % customers who buy again
  * Target: 25-40%
- **Customer lifetime value (LTV)**: Total $ spent
  * Target: 3-5x first purchase value
- **Churn rate**: % customers who stop buying
  * Target: <5%/month
- **NPS (Net Promoter Score)**: How likely to recommend?
  * Target: >50 (good), >70 (excellent)

---

## III. CUSTOMER JOURNEY MAPPING CHI TIẾT

### Customer Journey Map Template

```
┌──────────────────────────────────────────────────────────────┐
│ STAGE 1: AWARENESS (Nhận biết)                               │
├──────────────────────────────────────────────────────────────┤
│ Customer action: Searching, scrolling social media             │
│ Touchpoints: Facebook Ads, TikTok videos, Google search       │
│ Pain points: Too many ads, ads not relevant                   │
│ Emotion: Curious, exploring                                   │
│ Marketing message: "Discover [product], trending now"         │
│ Conversion metric: Click → Landing page (2-5% CTR)           │
│ KPI: CPM $0.5-2, CTR 2-5%, Reach 10,000+                    │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ STAGE 2: CONSIDERATION (Xem xét)                             │
├──────────────────────────────────────────────────────────────┤
│ Customer action: Viewing product, reading reviews              │
│ Touchpoints: Landing page, product page, reviews              │
│ Pain points: Slow loading, unclear info, bad reviews          │
│ Emotion: Interested, but hesitant                             │
│ Marketing message: "See what customers say" + testimonials     │
│ Page elements: Product video, 20+ photos, 50+ reviews        │
│ Conversion metric: Page view → Add to cart (70-80%)          │
│ KPI: Bounce rate <50%, Scroll depth >70%, Time >2 min        │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ STAGE 3: DECISION (Quyết định)                               │
├──────────────────────────────────────────────────────────────┤
│ Customer action: Added to cart, checking out                  │
│ Touchpoints: Checkout page, payment gateway                   │
│ Pain points: Too many form fields, slow, payment issues       │
│ Emotion: Ready to buy, but anxious                            │
│ Marketing message: "Secure checkout, trusted payment"         │
│ Checkout optimization: 1-page, express option, trust badges   │
│ Conversion metric: Add to cart → Purchase (20-40%)           │
│ KPI: Conversion rate 1-3%, AOV $20-100                       │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ STAGE 4: RETENTION (Giữ chân)                                │
├──────────────────────────────────────────────────────────────┤
│ Customer action: Using product, might leave review            │
│ Touchpoints: Email, SMS, loyalty program                      │
│ Pain points: Forgetting product, no incentive to return       │
│ Emotion: Satisfied (hopefully), wants to feel valued          │
│ Marketing message: "We appreciate you, here's a reward"       │
│ Actions: Review requests, loyalty points, member offers       │
│ Conversion metric: Purchase → Repeat purchase (25-40%)        │
│ KPI: Repeat rate 25-40%, LTV 3-5x, NPS >50                  │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ STAGE 5: ADVOCACY (Ủng hộ)                                   │
├──────────────────────────────────────────────────────────────┤
│ Customer action: Recommending to friends, leaving reviews      │
│ Touchpoints: Social media, word-of-mouth, referral            │
│ Pain points: No incentive to refer                            │
│ Emotion: Loyal, brand advocate                                │
│ Marketing message: "Refer a friend, both get $5"              │
│ Actions: Referral program, user-generated content             │
│ Conversion metric: 1 customer → 3-5 new customers            │
│ KPI: Referral rate 10-20%, UGC per month 100+                │
└──────────────────────────────────────────────────────────────┘
```

---

## IV. TOUCHPOINTS & CONVERSION MECHANICS

### Touchpoint 1: Facebook Ads → Landing Page

**Setup**:
- **Ad account**: Business Manager, pixel installed
- **Audience**: Cold (broad interests) + warm (website visitors)
- **Ad creative**: Video or carousel, thumb-stopping
- **CTA button**: "Learn More" or "Shop Now"
- **Destination**: Landing page (NOT website homepage)

**Metrics**:
- **CPM**: Cost per 1000 impressions = $0.5-2 (VN)
- **CTR**: Click-through rate = 2-5% (good)
- **CPC**: Cost per click = $0.10-0.50
- **Conversion**: Clicks → Page view = 95%+ (should be high)

**Optimization**:
- A/B test: 2 ad creatives, track CTR
- If CTR <2%: Change creative, target, or offer
- If CTR >5%: Great, scale up budget

---

### Touchpoint 2: Landing Page → Product Interest

**Landing page structure** (mobile-first):

```
1. HEADER (Sticky)
   - Logo
   - Shopping cart
   - Search bar

2. HERO SECTION (Above fold)
   - Product image/video (40% screen)
   - Main message (40% screen)
   - CTA button: "Add to cart" or "View details"
   - 80% of users should see this without scrolling

3. PROBLEM/BENEFIT SECTION
   - "Why you need this"
   - 3-5 bullet points
   - Icons for each benefit

4. PRODUCT DETAILS SECTION
   - Multiple product images (20+)
   - 360 product view if possible
   - Video: 30-60 seconds showing product

5. SOCIAL PROOF SECTION
   - Star rating (4.5+)
   - Number of reviews (100+)
   - 3-5 best reviews (with name, photo)
   - "95% customers would recommend"

6. FAQ SECTION
   - Size/fit guide
   - Shipping/returns
   - Care instructions
   - Material composition

7. CTA BUTTON (Fixed)
   - "Add to cart" button
   - Follows user while scrolling
   - High contrast color (green/orange)

8. TRUST BADGES
   - Secure (SSL certificate)
   - Money-back guarantee
   - Free returns
   - Verified seller
```

**Metrics**:
- **Page load time**: <3 seconds (critical for mobile)
- **Bounce rate**: <50% (users leaving without action)
- **Scroll depth**: >70% (users scrolling down)
- **Time on page**: >2 minutes (engaged)
- **Add to cart rate**: 5-15% (of page visitors)

---

### Touchpoint 3: Product Page → Add to Cart

**Add to cart optimization**:
- **Price display**: Clear, prominent, no hidden fees
- **Size/color selector**: Easy to use, clear options
- **Quantity**: Default 1, easy to increase
- **Add to cart button**: High contrast, prominent
- **Urgency signals**: "Only 3 left", "Popular", "Last chance"
- **Payment options**: COD, bank transfer, e-wallet, credit card

**Common objections & solutions**:
- "Is this legit?": Add reviews, testimonials, company info
- "Will it fit?": Add size guide, videos, dimensions
- "How long to ship?": Add shipping timeline, tracking
- "Can I return?": Add return policy, guarantee
- "Is it safe to pay?": Add security badges, payment options

**Add to cart rate target**: 5-15% of product page visitors

---

### Touchpoint 4: Shopping Cart → Checkout

**Cart abandonment is 60-80% normal**, so retargeting cart abandoners is CRITICAL.

**Cart optimization**:
- **Display what's in cart**: Clear item names, images, prices
- **Easy to edit**: Remove, change quantity easily
- **Shipping cost**: Show upfront (no surprises at checkout)
- **Apply coupon**: Coupon code field visible
- **Continue shopping**: Link to browse more
- **Checkout button**: Clear, prominent
- **Estimated arrival**: "Will arrive by Friday"

**Cart abandonment recovery**:
- **Email 1 (1 hour)**: "You left something, come back"
- **Email 2 (24 hours)**: "Your cart is waiting, 5% off"
- **Email 3 (48 hours)**: "Last chance, tonight only"
- **Ad retargeting**: Show same product, offer discount

**Checkout rate**: 20-40% of cart abandoners return via email

---

### Touchpoint 5: Checkout → Purchase

**Checkout funnel** (should be 1-page or 3-step max):

**Step 1: Shipping Address**
- Name, email, phone, address
- Prefill if returning customer
- Option to use billing address

**Step 2: Shipping Method**
- Standard (5-7 days): Free or $2
- Express (2-3 days): $5
- Next day: $10

**Step 3: Payment**
- Credit card (Visa, Mastercard)
- Debit card
- Bank transfer
- E-wallet (Momo, ZaloPay)
- COD (Cash on delivery)

**Checkout best practices**:
- **Form fields**: Minimize (only essential)
- **Progress bar**: Show "Step 1/3" completion
- **Trust signals**: "Secure checkout", "Your data is safe"
- **Promo code**: Input field visible
- **Order summary**: Always visible (especially mobile)
- **Backup phone**: Show customer service number
- **Terms checkbox**: Pre-checked if legal (easier conversion)

**Conversion rate (add to cart → purchase)**:
- **Typical**: 20-40% checkout rate
- **Goal**: 40-60% checkout rate

---

### Touchpoint 6: Purchase → Order Confirmation

**Order confirmation email** (sent immediately):
- Order number, items, price
- Estimated delivery date
- Tracking number (when available)
- Link to track order
- Next steps
- Return policy reminder
- Thank you message

**SMS notification** (immediate):
- Brief: "Order confirmed! Track: [link]"
- Delivery: "Package on the way, arrives [date]"
- Delivery: "Package delivered, enjoy!"

---

### Touchpoint 7: Shipping → Delivery

**During shipping**:
- **Email 1 (Day 1)**: "Order shipped, tracking number"
- **SMS reminder**: Brief tracking notification
- **Email 2 (Day 3)**: "Package on the way"

**At delivery**:
- **SMS notification**: "Package delivered"
- **Email notification**: "Your package arrived"

---

### Touchpoint 8: Post-Purchase → Review Request

**Review request timing**:
- **Email 1 (Day 7)**: "How's your order?" with review link
- **Email 2 (Day 14)**: "Write a review, get $2 credit"
- **SMS (Day 10)**: Quick poll: "Satisfied? Rate us"

**Why reviews matter**:
- 95% customers read reviews before buying
- 4.5+ star products convert 40% better
- Review count matters: 50+ reviews = trust

**Incentivize reviews**:
- "$2 discount on next order"
- "Enter raffle for $100 gift card"
- "Exclusive member offer"

---

### Touchpoint 9: Loyalty Program

**Loyalty mechanics**:
- **Earn points**: 1 đồng = 1 điểm
- **Redeem points**: 10 điểm = $1 discount
- **Tier benefits**:
  * Member: Normal points
  * Silver (50+ points): Free shipping
  * Gold (200+ points): 10% all purchases + early access

**Referral program**:
- "Refer a friend, both get $5"
- "Share your unique code: [CODE]"
- Automatic tracking when friend uses code

---

### Touchpoint 10: Repeat Purchase Emails

**Email sequence for repeat purchase**:
- **Email 1 (Day 20)**: "New products you might like"
- **Email 2 (Day 30)**: "Time to reorder? Here's 10% off"
- **Email 3 (Day 45)**: "Members-only offer: 20% off"
- **Email 4 (Day 60)**: "Complete your collection"

**Dynamic content**:
- Show products based on purchase history
- "You bought blue shirt, here's matching pants"
- Personalized recommendations increase conversion 20%

---

## V. METRICS TỪNG GIAI ĐOẠN & BENCHMARKS VIỆT NAM

### Giai đoạn AWARENESS

| Metric | Benchmark VN | Formula | Target |
|--------|-------------|---------|--------|
| CPM | $0.50 - $2.00 | Cost / (Impressions/1000) | <$1.50 |
| Reach | Unlimited | Budget / CPM × 1000 | 10,000+ |
| Impressions | 50,000+ | Actual from platform | 50,000+ |
| CTR | 2% - 5% | Clicks / Impressions × 100 | >3% |
| CPC | $0.10 - $0.50 | Cost / Clicks | <$0.30 |

### Giai đoạn CONSIDERATION

| Metric | Benchmark VN | Formula | Target |
|--------|-------------|---------|--------|
| Bounce rate | 30% - 50% | (Single page views / All sessions) × 100 | <40% |
| Avg session duration | 1.5 - 2.5 min | Total time / Sessions | >2 min |
| Scroll depth | 60% - 80% | Pages scrolled fully / Total pages | >70% |
| Page views per session | 1.5 - 3 | Total page views / Sessions | 2-3 |
| Add to cart rate | 5% - 15% | Cart adds / Page visitors × 100 | 10%+ |

### Giai đoạn DECISION

| Metric | Benchmark VN | Formula | Target |
|--------|-------------|---------|--------|
| Checkout rate | 20% - 40% | Checkouts / Cart adds × 100 | 30%+ |
| Cart abandonment | 60% - 80% | (Carts - Purchases) / Carts × 100 | <70% |
| Conversion rate | 1% - 3% | Purchases / Visitors × 100 | 2%+ |
| AOV (Avg order value) | $20 - $100 | Total revenue / Purchases | $40+ |
| CPA (Cost per acquisition) | $1 - $10 | Ad spend / Purchases | <$5 |

### Giai đoạn RETENTION

| Metric | Benchmark VN | Formula | Target |
|--------|-------------|---------|--------|
| Repeat purchase rate | 20% - 40% | Repeat customers / Total customers × 100 | 30%+ |
| Customer LTV | 3x - 5x AOV | Total revenue from customer / Acquisitions | 4x AOV |
| Review rate | 20% - 40% | Reviews / Orders × 100 | 30%+ |
| NPS (Net Promoter Score) | 30 - 70 | Promoters (9-10) - Detractors (0-6) | >50 |
| Churn rate | 2% - 5%/month | Lost customers / Total customers × 100 | <3%/month |

### Cross-Channel ROAS (Return on Ad Spend)

| Channel | Benchmark VN | Formula | Target |
|---------|-------------|---------|--------|
| Facebook/Instagram | 2:1 - 5:1 | Revenue / Ad spend | 3:1+ |
| TikTok | 2:1 - 6:1 | Revenue / Ad spend | 3:1+ |
| Google Ads | 3:1 - 8:1 | Revenue / Ad spend | 4:1+ |
| Retargeting | 3:1 - 10:1 | Revenue / Ad spend | 5:1+ |
| Email | 20:1 - 40:1 | Revenue / Email send cost | 30:1+ |

---

## VI. AUTOMATION TRIGGERS & WORKFLOWS

### Trigger 1: Page Viewed → Add to cart email

**Condition**: User views product page but doesn't add to cart
**Delay**: 1 hour after page view
**Email content**:
- Product image
- "Still interested?"
- 10% discount code: INTERESTED10
- "Expires tonight"
**Result**: 5-10% convert to cart via email

---

### Trigger 2: Add to Cart → Cart Abandonment Email

**Condition**: Product added to cart but not purchased
**Delay**: 1 hour after add to cart
**Email sequence**:
- **Email 1 (1h)**: "You left something, come back"
- **Email 2 (24h)**: "$5 discount inside"
- **Email 3 (48h)**: "Final chance"
**Result**: 10-15% recover abandoned carts

---

### Trigger 3: Purchase → Post-Purchase Sequence

**Condition**: Order completed
**Email sequence** (automated):
- **Email 1 (1h)**: Order confirmation + tracking
- **Email 2 (Day 3)**: "On the way to you"
- **Email 3 (Day 7)**: "How's your order?" + review request
- **Email 4 (Day 14)**: "Write a review, get $2"
- **Email 5 (Day 20)**: New products, recommendations
- **Email 6 (Day 30)**: "Reorder now, 10% off"
**Result**: Higher LTV, more repeat purchases

---

### Trigger 4: No Purchase in 90 Days → Win-back Campaign

**Condition**: Customer hasn't purchased in 90 days
**Email sequence**:
- **Email 1**: "We miss you, here's 15% off"
- **Email 2 (3 days)**: "New arrivals you'll love"
- **Email 3 (5 days)**: "Final offer: 20% off"
**Result**: Recover lapsed customers

---

### Trigger 5: Multiple Purchases → VIP Status

**Condition**: Customer made 5+ purchases
**Action**:
- Automatic VIP badge in account
- Email: "You're VIP! Enjoy 20% off"
- SMS: "VIP member exclusive: free shipping"
**Result**: Increase loyalty, LTV

---

## VII. RETARGETING STRATEGY CHI TIẾT

### Retargeting Audience Segments

**Segment 1: Site Visitors (All)**
- Audience: Everyone who visited website
- Duration: 30 days
- Bid: Low
- Message: "Come back and browse"
- Budget: 20% of retargeting budget

**Segment 2: Product Page Viewers**
- Audience: Visited specific product page
- Duration: 60 days
- Bid: Medium
- Message: Show same product
- Content: Product image, price, reviews
- Budget: 30% of retargeting budget

**Segment 3: Cart Abandoners**
- Audience: Added to cart but didn't purchase
- Duration: 7 days (urgent)
- Bid: High
- Message: "Complete your checkout"
- Offer: "10% off today"
- Budget: 25% of retargeting budget
- Frequency: 2-3 ads/day (urgent)

**Segment 4: Initiated Checkout**
- Audience: Started checkout but didn't finish
- Duration: 3 days (most urgent)
- Bid: Highest
- Message: "1 step away from order"
- Offer: "Save 15% + free shipping"
- Budget: 15% of retargeting budget
- Frequency: 3-4 ads/day

**Segment 5: Past Customers**
- Audience: Purchased before
- Duration: Ongoing
- Bid: Medium
- Message: "Shop new arrivals"
- Offer: "Member exclusive: 20% off"
- Budget: 10% of retargeting budget
- Frequency: 1-2 ads/day

### Retargeting Ad Formats

**Single Product Ads**:
- Product image
- Price
- "Limited quantity"
- "Shop now" button
- Best for: Viewed specific product

**Dynamic Product Ads**:
- Automatically shows products user viewed
- AI-driven, highest converting
- Facebook/Instagram: Top choice
- ROAS: 5-8:1

**Carousel Ads**:
- 5-10 products in carousel
- Best for: Cart abandoners (show 3+ products)
- Message: "Complete your collection"
- High engagement

**Video Ads**:
- Product demo video (15-30s)
- User testimonials
- Before-after
- Highest engagement rate
- ROAS: 4-6:1

**Collection Ads**:
- Instant checkout from ad
- No click needed
- Mobile-first
- High conversion

---

## VIII. PHỄU CỤ THỂ CHO SHOPEE/LAZADA VS WEBSITE RIÊNG

### Phễu Shopee/Lazada (Marketplace)

**Ưu điểm**:
- Khách đã tin nền tảng
- Thanh toán built-in (COD, e-wallet, credit card)
- Vận chuyển logistics sẵn
- SEO tốt, organic traffic cao
- Rating visible, trust high

**Cấu trúc phễu**:
```
External Ads → Shop page → Product page → Checkout (Shopee handles) → Delivery → Review request
```

**Optimization**:
- **Shop name**: Branded, trustworthy
- **Shop description**: "Official store", ratings, history
- **Product title**: Keyword-rich, 150-160 characters
- **Product description**: Detailed, benefits, specs, how to use
- **Product images**: 9-12 images, high quality, lifestyle shots
- **Video**: 15-30s product demo
- **Price**: Competitive, discount visible
- **Free shipping threshold**: "Free ship on orders >$10"
- **Review strategy**: Encourage reviews via follow-up
- **Promotional badges**: "Official", "On sale", "Hot"

**Promotion strategy**:
- **Flash deals**: 1-2/week on Shopee
- **Voucher code**: "SHOP50K" (discount over $10)
- **Bundle deals**: 3 products together, save 20%
- **Free shipping campaigns**: Boost sales volume

**Metrics**:
- **Shop rating**: Maintain 4.7+
- **Response rate**: <1 hour
- **Return rate**: <2%
- **Review count**: Aim for 100+ reviews/month
- **Conversion**: 2-4% typical for marketplace

---

### Phễu Website Riêng

**Ưu điểm**:
- Full control over branding, pricing, messaging
- Higher margins (no marketplace fee)
- Customer data ownership
- Direct relationship with customers
- Email list building

**Nhược điểm**:
- Need to drive traffic externally (paid ads)
- Checkout friction (not 1-click like Amazon)
- Trust building takes time
- Higher CAC (cost per acquisition)

**Cấu trúc phễu**:
```
Facebook/TikTok Ads → Landing page → Product page → Add to cart → Checkout → Post-purchase email → Loyalty
```

**Optimization**:
- **Landing page**: Mobile-optimized, <3s load time
- **Product page**: 20+ images, video, detailed description
- **Trust signals**: Reviews, testimonials, guarantees
- **Checkout**: Minimize form fields, multiple payment options
- **Email follow-up**: Automated sequences
- **Retargeting**: Heavy use of pixel + ads

**Promotion strategy**:
- **Flash sales**: Higher discount (50-70%) to drive traffic
- **Email list**: 10% discount for email signup
- **Referral program**: "Refer friend, both get $5"
- **Loyalty program**: Points system, tier rewards
- **Seasonal campaigns**: 11.11, Black Friday, Christmas

**Metrics**:
- **Conversion rate**: 1-3% (aim for 2%+)
- **AOV**: $30-50 (higher than marketplace)
- **Email list growth**: 5,000+ subscribers/month
- **Repeat rate**: 25-40% (build loyalty)
- **LTV**: 3-5x AOV

---

## IX. BUDGET ALLOCATION FRAMEWORK

### Total Marketing Budget = $10,000/month (example)

**Break down**:

```
TOTAL BUDGET: $10,000

├─ Paid Ads (60%): $6,000
│  ├─ Cold traffic (40%): $2,400
│  │  ├─ Facebook/Instagram: $1,200 (testing)
│  │  ├─ TikTok: $800
│  │  └─ Google Ads: $400
│  │
│  ├─ Retargeting (35%): $2,100
│  │  ├─ Site visitors: $420
│  │  ├─ Product viewers: $630
│  │  ├─ Cart abandoners: $630
│  │  └─ Checkout abandoned: $420
│  │
│  └─ Loyalty (25%): $1,500
│     ├─ Email sends (minimal cost): $200
│     ├─ SMS campaigns: $300
│     └─ Retarget past customers: $1,000
│
├─ Content Creation (20%): $2,000
│  ├─ Video production: $1,000
│  ├─ Photography: $500
│  ├─ Design/graphics: $300
│  └─ Freelance copywriting: $200
│
├─ Tools & Infrastructure (10%): $1,000
│  ├─ Email platform (Klaviyo): $300
│  ├─ Analytics (Google, Shopify): $200
│  ├─ CRM/SMS platform: $300
│  └─ Design tools (Canva Pro, Adobe): $200
│
└─ Team (10%): $1,000
   ├─ Community manager: $500
   ├─ Analytics/optimization: $300
   └─ Freelance support: $200
```

### Budget Allocation by Funnel Stage

| Stage | Budget % | Focus |
|-------|----------|-------|
| TOFU (Awareness) | 30% | Get traffic, build brand |
| MOFU (Consideration) | 20% | Landing pages, content |
| BOFU (Conversion) | 30% | Retargeting, incentives |
| Retention | 15% | Email, loyalty, repeat |
| Operations | 5% | Tools, team |

### Budget Allocation by Channel (by month)

**Month 1-3 (New store)**:
- Facebook/Instagram: 50% (build reach)
- TikTok: 20% (viral potential)
- Retargeting: 20% (convert early visitors)
- Email/Loyalty: 10%

**Month 4-6 (Growth phase)**:
- Facebook/Instagram: 35% (proven channel)
- TikTok: 20% (continue growth)
- Retargeting: 35% (higher priority, higher ROI)
- Email/Loyalty: 10%

**Month 7+ (Mature phase)**:
- Facebook/Instagram: 25% (maintain)
- TikTok: 15% (opportunistic)
- Retargeting: 45% (main driver)
- Email/Loyalty: 15% (focus on LTV)

---

## X. CONVERSION RATE BENCHMARKS CHO THỊ TRƯỜNG VN

### By Product Category

| Category | BOFU Conversion | Repeat Rate | AOV |
|----------|-----------------|-------------|-----|
| Fashion/Apparel | 1.5-2.5% | 25-35% | $30-50 |
| Beauty/Skincare | 2-3% | 35-50% | $25-40 |
| Electronics | 1-2% | 20-30% | $50-150 |
| Home/Kitchen | 1.5-2.5% | 25-35% | $40-80 |
| Food/Beverage | 2-3% | 40-50% | $15-30 |
| Furniture | 0.8-1.5% | 15-25% | $100-500 |

### By Traffic Source

| Source | Conversion | ROAS | CPA |
|--------|-----------|------|-----|
| Organic (SEO) | 2-4% | 5:1-10:1 | $1-3 |
| Direct | 3-5% | 10:1-20:1 | $0.50-1 |
| Email | 2-3% | 20:1-40:1 | $0.20-0.50 |
| Paid (Cold) | 0.5-1.5% | 1:1-2:1 | $3-8 |
| Paid (Retargeting) | 2-5% | 3:1-8:1 | $1-3 |
| Referral | 1.5-3% | 4:1-8:1 | $2-4 |

### By Device

| Device | Conversion | Bounce Rate | AOV |
|--------|-----------|------------|-----|
| Mobile | 1.5-2% | 45-55% | $20-35 |
| Desktop | 1.5-2.5% | 30-40% | $35-55 |
| Tablet | 1-2% | 40-50% | $25-45 |

---

## XI. OPTIMIZATION FRAMEWORK (CONTINUOUS IMPROVEMENT)

### Weekly Optimization (Every Monday)

1. **Review metrics**:
   - Top 3 performing ads
   - Top 3 worst performing ads
   - Conversion rate trends

2. **Quick wins**:
   - Pause underperforming ads
   - Increase budget to top performers
   - A/B test new creatives

3. **Team sync**:
   - Share learnings
   - Discuss optimizations
   - Plan week ahead

### Monthly Optimization (End of month)

1. **Deep dive analysis**:
   - ROAS by channel
   - Conversion bottlenecks
   - Customer feedback analysis
   - Competitor moves

2. **Testing results**:
   - Which tests won?
   - Implement winners
   - Plan new tests

3. **Budget reallocation**:
   - Shift budget to best performers
   - Test new channels (if budget)
   - Reduce poor channels

### Quarterly Optimization (End of Q)

1. **Strategic review**:
   - Q goals vs actual
   - What worked, what didn't
   - Market changes

2. **Major changes**:
   - New product launches
   - Messaging updates
   - Channel expansions

3. **Forecasting**:
   - Plan Q+1 strategy
   - Budget planning
   - Team planning

---

## XII. PHỄU CHECKLIST

Sử dụng checklist này để audit phễu của bạn:

**TOFU (Awareness)**:
- [ ] Running ads on 2+ channels
- [ ] CTR >2%
- [ ] CPM <$2
- [ ] A/B testing creatives

**MOFU (Consideration)**:
- [ ] Landing page <3s load time
- [ ] Bounce rate <50%
- [ ] Product images 20+
- [ ] Video demo present
- [ ] FAQ section included
- [ ] Reviews/testimonials visible
- [ ] Scroll depth >70%

**BOFU (Conversion)**:
- [ ] Checkout <3 steps
- [ ] Form fields minimized
- [ ] Trust badges visible
- [ ] Multiple payment options
- [ ] Conversion rate 1%+
- [ ] Cart abandonment <70%

**Retention**:
- [ ] Post-purchase email sequence set up
- [ ] Review request emails automated
- [ ] Loyalty program active
- [ ] Repeat purchase rate >25%
- [ ] Email list >5,000
- [ ] NPS >50

**Retargeting**:
- [ ] Pixel installed on all pages
- [ ] Audience segments created
- [ ] Cart abandoners campaign
- [ ] Product viewers campaign
- [ ] Retargeting ROAS >3:1

---

## CONCLUSION

Phễu bán hàng là hành trình của khách hàng từ lúc biết đến sản phẩm cho tới khi mua lặp lại. Bằng cách tối ưu từng touchpoint, measure metrics cẩn thận, và liên tục optimize, bạn sẽ:

- ✓ Tăng conversion rate 2-3x
- ✓ Giảm CAC (cost per acquisition) 30-50%
- ✓ Tăng customer LTV 3-5x
- ✓ Build loyal customer base
- ✓ Scale sustainable growth

Bắt đầu mapping phễu của bạn ngay hôm nay!

