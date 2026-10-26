---
name: ecom-google-ads-strategy
description: >
  Chiến lược Google Ads toàn diện cho thương mại điện tử Việt Nam. Hướng dẫn chi tiết về Google Shopping, Search Ads, Performance Max, quản lý từ khóa, tracking conversion, và tối ưu hóa chất lượng. Dùng skill này khi cần: lập chiến lược Google Ads, setup Google Shopping, quản lý Search campaign, tối ưu Quality Score, quản lý từ khóa Google Ads.
---

# CHIẾN LƯỢC GOOGLE ADS CHO TMĐT VIỆT NAM

## 1. GIỚI THIỆU GOOGLE ADS CHO TMĐT

### 1.1 Google Ads vs Facebook Ads

| Aspect | Google Ads | Facebook Ads |
|--------|-----------|------------|
| **Intent** | High intent (searching) | Awareness → Interest |
| **Traffic model** | Pull (user searches) | Push (we interrupt) |
| **Best for** | Sales, lead gen | Brand awareness, retargeting |
| **ROAS** | 2-4x (high intent) | 2-3x (depends on product) |
| **CPA** | Often higher | Often lower (awareness first) |
| **Learning curve** | Medium | Easy |
| **Best product fit** | Commercial products | All, especially lifestyle |

**Strategy:** Google Ads focus trên high-intent traffic (người tìm kiếm sẵn), Facebook focus trên awareness + retargeting.

### 1.2 Campaign Types Tổng quan

| Type | Mục đích | Inventory | Bid strategy |
|------|---------|-----------|------------|
| **Shopping** | Bán sản phẩm trực tiếp | Product feed | Maximize revenue |
| **Search** | High-intent text search | Keywords | Target CPA |
| **Performance Max** | All Google channels (auto) | Assets | Maximize conversions |
| **Display** | Brand awareness, retargeting | GDN sites | Bidding flexible |
| **YouTube** | Video ads, awareness | YouTube | CPV bidding |
| **Discovery** | Native ads format | YouTube, Gmail, Discover | Target CPA |

**Recommended mix cho TMĐT VN:**
- Shopping: 40% (highest ROAS)
- Search: 35% (high-intent)
- Performance Max: 15% (testing, new products)
- YouTube/Display: 10% (awareness, remarketing)

## 2. GOOGLE SHOPPING SETUP CHECKLIST

### 2.1 Google Merchant Center Setup (Prerequisite)

**Step 1: Create Merchant Center account**
- Go: merchants.google.com
- Verify: Business name, address, website
- Country: Việt Nam (for VN sellers)

**Step 2: Link to Google Ads**
- Merchant Center → Settings → Linked accounts
- Link to Google Ads account
- Accept terms

**Step 3: Setup Primary Feed**
- Create feed: Type = File upload or scheduled
- Format: CSV/XML (CSV easier for beginners)
- Upload location: Merchant Center → Products
- File schedule: Daily, hourly, or on-demand

**Step 4: Verify ownership**
- Website HTML tag (preferred)
- Or: DNS record
- Verification needed for: Product feed activation

### 2.2 Product Feed Optimization

**Required Fields (Core)**

| Field | Format | Example | Notes |
|-------|--------|---------|-------|
| **id** | Text, unique | SKU_001 | Must be unique per product |
| **title** | Text, max 150 | Samsung Galaxy A12 64GB | Include brand + model + specs |
| **description** | Text, max 5000 | Full details | SEO-optimized, benefit-driven |
| **link** | URL | https://shop.vn/galaxy-a12 | Unique per variant |
| **image_link** | URL | https://img.vn/phone1.jpg | Clean, high-res (800x600 min) |
| **price** | Decimal | 5000000 | In VND |
| **currency** | Currency code | VND | Must match |
| **availability** | Enum | in stock / out of stock | Update when stock changes |
| **brand** | Text | Samsung | Help with matching |
| **product_type** | Text | Electronics > Phones | Hierarchy helps users filter |

**Recommended Extra Fields (Conversion boosters)**

| Field | Example | Why important |
|-------|---------|--------------|
| **gtin** | 8801643065433 | Product barcode, matches user searches |
| **mpn** | SM-A125F | Manufacturer part number |
| **color** | Black, Silver | Filter attribute |
| **size** | L, M, S | For clothing |
| **gender** | Male, Female, Unisex | For apparel |
| **age_group** | Adult, Kids | For clothing |
| **material** | Cotton, Polyester | For apparel/textiles |
| **condition** | New, Refurbished | New assumed if blank |
| **custom_label_0** | Best sellers | For filtering/reporting |

**Best Practices**

- **Title optimization:**
  - Format: [Brand] [Model] [Key specs]
  - Include trendy keywords: "Gaming", "5G", "AMOLED"
  - Avoid: Excessive caps, repetition, special characters
  - Example bad: "SAMSUNG SAMSUNG GALAXY 5G SMARTPHONE PHONE"
  - Example good: "Samsung Galaxy A52 5G Smartphone 128GB (Black)"

- **Description strategy:**
  - 1st paragraph: Main benefit
  - 2nd paragraph: Features
  - 3rd paragraph: Specs
  - Include: Price promise, warranty, shipping time
  - Example:
    ```
    Enjoy vibrant visuals with the 6.5" AMOLED display.
    Dual 48MP camera with night mode for crisp photos.
    Specifications: 5G, 6GB RAM, 128GB storage, 4500mAh battery.
    Free shipping nationwide. 1-year manufacturer warranty included.
    ```

- **Images:**
  - Min 800x600px (Google prefers 1200x900+)
  - Background: White or clean (avoid busy)
  - Product: Center, fill 80% frame
  - Multiple angles: Top, side, detail shots
  - No watermarks/logos blocking product
  - Format: JPG/PNG

- **Price accuracy:**
  - Must match website price exactly
  - Include all fees (not hidden at checkout)
  - Currency: VND with no special symbols
  - Update daily (stock/price changes)

- **Availability status:**
  - "in stock": Ready to ship
  - "out of stock": Zero inventory
  - "preorder": Coming soon (low priority)
  - Update: Real-time sync from inventory

### 2.3 Feed Rules & Supplemental Feeds

**Feed Rules** (Modify data without reuploading)

Use when: You want to change price, exclude products, adjust title

Example scenarios:
- Add 15% markup to all prices: Create rule "Price * 1.15"
- Exclude out of stock: Create rule "If availability = out of stock, then exclude"
- Append shipping info: Add " - Free shipping VN" to all titles

**Supplemental Feeds** (Add to main feed)

Use when: Different products for different regions/languages

Example:
- Main feed: 5000 products (all VN)
- Supplemental 1: 200 premium products (HCM promotion)
- Supplemental 2: 500 clearance products (last-minute deals)

### 2.4 Shopping Feed Monitoring

**Weekly checklist:**
- [ ] 0 disapproved products (check "Diagnostics")
- [ ] Price, inventory updated <24hrs
- [ ] No "invalid" fields (Merchant Center alerts)
- [ ] Coverage: 95%+ of main products listed
- [ ] Performance: Top 20% products have >100 impressions

**Common disapprovals & fixes:**

| Issue | Reason | Fix |
|-------|--------|-----|
| "Mismatched title/link" | Title doesn't match product | Match exactly with website |
| "Unacceptable image" | Blurry, watermarked, wrong product | Use clean, clear 800x600+ image |
| "Missing price" | Price field empty | Fill all products |
| "Disapproved country" | Shipping restricted | Add shipping costs/exclusions |
| "Duplicate GTIN" | Same barcode, different product | Fix GTIN or leave blank |

## 3. SHOPPING CAMPAIGN STRUCTURE

### 3.1 Campaign Setup

**Campaign Type:** Shopping (don't use "Smart Shopping")

**Campaign name convention:**
```
[Campaign type] - [Product category] - [Audience]

Examples:
- Shopping - Electronics - VN All
- Shopping - Fashion - HCM Premium
- Shopping - Clearance - All VN
```

**Settings:**
- Countries: Vietnam
- Networks: Google Shopping Network only (exclude Search Partners for Shopping)
- Languages: Vietnamese, English (if targeting both)

### 3.2 Campaign Structure Strategy

**Option A - By Product Category (Recommended for 1000+ products)**

```
Account
├── Campaign: Electronics
│   ├── Shopping ad group: Phones
│   │   └── Auto bidding by: Product GTIN
│   ├── Shopping ad group: Laptops
│   └── Shopping ad group: Accessories
├── Campaign: Fashion
│   ├── Shopping ad group: Women's apparel
│   ├── Shopping ad group: Men's apparel
│   └── Shopping ad group: Accessories
└── Campaign: Home & Living
    ├── Shopping ad group: Kitchen
    ├── Shopping ad group: Bedroom
    └── Shopping ad group: Furniture
```

**Benefits:**
- Budget control per category
- Performance tracking isolated
- Can pause struggling category

**Option B - By Commercial Value (Recommended for high-value sellers)**

```
Account
├── Campaign: Premium (High margin 40%+)
│   ├── Ad group: Best sellers
│   └── Ad group: High AOV
├── Campaign: Standard (Margin 20-40%)
│   ├── Ad group: Volume movers
│   └── Ad group: New products
└── Campaign: Clearance (Margin <20%)
    └── Ad group: Overstock
```

**Benefits:**
- Different bidding for each tier
- Premium products: Aggressive bid
- Clearance: Minimal bid to clear

### 3.3 Bidding Strategy for Shopping

**Strategy 1: Maximize Conversions (Volume focus)**
- Best for: High inventory, need volume
- Google optimizes: Maximum sales/revenue
- Budget: 10M+ VND/day (need 30+ conversions/day)
- Target: Revenue priority

**Strategy 2: Target ROAS (Margin-focused) - RECOMMENDED**
- Set target: 2.5x (if 100k product → expect 250k value)
- Calculate target from margin:
  - Product cost: 100k
  - Target margin: 40% = 40k profit
  - Product price: 150k
  - ROAS target: 150k / 50k ad spend = 3x
- Best for: Profit optimization

**Strategy 3: Maximize Clicks (Traffic focus)**
- Aggressive bidding for clicks
- Best for: New products (building data)
- Risk: CPL too high

**Strategy 4: Target CPA (Fixed cost per sale)**
- Set CPA: 15-30k VND (depends on margin)
- Google optimizes to hit CPA
- Best for: Fixed profit targets
- Requires: 10+ conversions in ~5 days to learn

### 3.4 Shopping Campaign Segmentation (Advanced)

**Segment 1: Brand Keywords (High intent, owned traffic)**
- Products matching branded searches
- Bid: 30-50% higher (owned territory)
- Exclude: Competitor brand searches

**Segment 2: Category Keywords (High intent, category)**
- Phones, laptops, shoes generic searches
- Bid: Medium, competitive
- Example: "Android phone", "gaming laptop"

**Segment 3: Competitor Keywords (Audience capture)**
- Competitor product searches (if allowed)
- Bid: Moderate, lower margin
- Example: "iPhone alternative" → show Samsung/Xiaomi

## 4. SEARCH ADS STRATEGY

### 4.1 Campaign Structure by Category

**Setup:**

```
Account
├── Campaign: Brand keywords
│   ├── Ad group: Brand primary
│   ├── Ad group: Brand + modifier
│   └── Ad group: Competitor mention
├── Campaign: Category - Electronics
│   ├── Ad group: Phones
│   ├── Ad group: Laptops
│   └── Ad group: Accessories
└── Campaign: Category - Fashion
    ├── Ad group: Women's
    ├── Ad group: Men's
    └── Ad group: Accessories
```

### 4.2 Keyword Match Types Strategy

**Broad Match** (Machine learning)
- Keyword: "laptop"
- Matches: laptop, laptops, best laptop, laptop review, laptop gaming
- CTR: Highest
- CPA: Often highest (low quality)
- Use: Testing, new categories

**Phrase Match** (Order matters)
- Keyword: "gaming laptop"
- Matches: best gaming laptop, gaming laptop 15 inch, gaming laptop store
- Doesn't match: laptop gaming, gaming computer
- CTR: Medium
- CPA: Medium
- Use: Main keywords (70% of budget)

**Exact Match** (Exact query)
- Keyword: [gaming laptop]
- Matches: gaming laptop, gaming laptops (close variation)
- Doesn't match: laptop gaming, best gaming laptop
- CTR: Lower but qualified
- CPA: Lowest (high intent)
- Use: Top keywords (20% budget)

**Broad Match Modified** (DEPRECATED in 2021, converted to phrase)
- Old format: +keyword +matching
- Now: Use phrase match [keyword]

### 4.3 Keyword Research for VN TMĐT

**Tools:**
- Google Keyword Planner (free, in Google Ads)
- Semrush (international tool, works for VN)
- SEMrush, Ahrefs (paid, worth for bigger budgets)

**Search intent types:**

| Intent | Example | CTR | CPA | Volume |
|--------|---------|-----|-----|--------|
| Commercial | "mua điện thoại giá rẻ" | High | Low | High |
| Local | "cửa hàng điện thoại gần đây" | Med | Med | Low |
| Informational | "điện thoại nào tốt nhất" | High | High | Very high |
| Brand | "iphone giá bao nhiêu" | Medium | Low | Medium |

**Build keyword list structure:**

```
Brand keywords (40% budget)
- iPhone 15, iPhone 15 pro, iPhone 15 price
- Samsung Galaxy, Galaxy A52, Galaxy Note

High-intent commercial (35% budget)
- Buy phone online Vietnam
- Smartphone giá rẻ, điện thoại dưới 5 triệu
- Game phone, camera phone

Category + modifier (20% budget)
- Android phone, 5G phone, phone under 200k
- Budget phone, phone sale Vietnam

Informational (5% budget, lower priority)
- Best phone 2024, phone review
- (Often high cost, lower conversion)
```

**Recommended VN keywords for common categories:**

*Electronics:*
- "mua điện thoại online", "smartphone giá rẻ", "điện thoại 5G"
- "laptop gaming", "laptop dưới 10 triệu", "laptop học tập"
- "tablet giá tốt", "iPad Việt Nam"

*Fashion:*
- "quần áo nữ", "áo sơ mi nam", "giày thể thao"
- "thời trang công sở", "quần jean nam", "váy đầm nữ"

*Home & Living:*
- "tủ lạnh", "máy giặt", "nồi cơm"
- "tấm thảm", "gối ngủ", "rèm cửa"

### 4.4 Negative Keyword Management

**Goal:** Prevent low-intent searches (waste budget)

**Negative keyword types:**

*Product-specific negatives:*
- If selling laptop, exclude: -free, -cheap, -crack, -download
- Rationale: People searching these want pirated software

*Commercial negatives:*
- If selling products, exclude: -used, -second hand, -refurbished (if new only)
- Rationale: Different market, much lower price point

*VN-specific negatives:*
- -cách, -cách làm (means "how to" in Vietnamese)
- -diy, -tự làm (DIY content, not buying)
- -bị hỏng, -bảo hành (warranty/repair, not new purchase)

*Shared negative lists (Best practice):*
- Create: Shared negative list "Common low-intent"
- Add: -free, -download, -tutorial, -review -buy, -guide
- Apply to: All campaigns for efficiency

### 4.5 Responsive Search Ads (RSA)

**Setup:**
- Headline 1 (required): Brand or main benefit
  - "Samsung Galaxy A12 - Giá tốt nhất" (50 chars max)
- Headline 2: Product feature
  - "Camera 48MP, Pin 5000mAh" (50 chars max)
- Headline 3: Offer/CTA
  - "Mua ngay - Giao hôm nay" (30 chars max)
- Description 1: Benefit
  - "Mua điện thoại giá rẻ tại cửa hàng uy tín. Giao hôm nay, bảo hành 12 tháng."
- Description 2: Social proof + offer
  - "10,000+ khách hàng hài lòng. Free shipping toàn Việt Nam. Sale 15% hôm nay!"

**Best practice:**
- Create 15 unique headlines, 4 unique descriptions
- Let Google test combinations
- Monitor: Which headlines/descriptions appear most in winning ads
- Iterate: Refresh monthly, add seasonal headlines

**Example RSA for Fashion brand:**

Headlines:
1. "Women's Summer Collection 2024" (required)
2. "50% Off Selected Items" (pin to position 1 for sale)
3. "Free Shipping All Orders"
4. "100% Cotton, Sustainable Fashion"
5. "Available Sizes XS to XXXL"
6. "Latest Trends from Europe"
7. "Fast Checkout, Same Day Ship"
8. "Quality Guaranteed - 30 Day Returns"
9. "Join 100k Happy Customers"
10. "Shop Now - Limited Time Sale"
11. "Premium Fabrics, Affordable Price"
12. "Style Your Unique Look"
13. "New Arrivals Weekly"
14. "Secure Payment, Easy Returns"
15. "Trending Styles for 2024"

Descriptions:
1. "Discover the latest women's fashion trends. Quality fabrics, affordable prices. Free delivery nationwide. Limited time offer!"
2. "Shop premium women's clothing online. Sustainable materials, ethical production. 30-day return guarantee. Order now!"
3. "100k+ happy customers trust our brand. Fast shipping to all of Vietnam. Authentic products with manufacturer warranty."
4. "Summer collection now available. Fresh styles from Europe. Exclusive online discounts. Limited stock, order today!"

### 4.6 Ad Extensions (Critical for CTR+)

**Sitelink Extensions**
- Links to specific pages: Collection pages, category pages
- Example:
  - Home > New Arrivals
  - Home > Sale
  - Home > Gift Guide
  - Home > Reviews
- Best for: Highlighting key offerings
- CTR impact: +10-20%

**Callout Extensions**
- Bullet points, no links
- Example:
  - Free shipping nationwide
  - 30-day return policy
  - 12-month warranty
  - 24/7 customer support
- Best for: Competitive advantages
- CTR impact: +5-10%

**Structured Snippet**
- Category header + values
- Example:
  - Header: "Brands"
  - Values: Apple, Samsung, Sony, LG
  - OR Header: "Types"
  - Values: Gaming, Budget, Professional, Work from home
- Best for: Showing variety
- CTR impact: +5-10%

**Price Extensions**
- Show product prices
- Example:
  - iPhone 15 - 25,000,000 VND
  - iPhone 14 - 20,000,000 VND
  - iPhone 13 - 15,000,000 VND
- Best for: Price comparisons
- CTR impact: +5-15%

**Promotion Extensions**
- Highlight ongoing sales
- Example:
  - "Summer Sale - 20% Off"
  - "Free Shipping All Orders"
  - "Bundle Deal: Buy 2 Get 1 Free"
- Best for: Limited-time offers
- CTR impact: +10-20%

**Setup priority:**
1. Sitelink (mandatory)
2. Callout (add top competitive advantages)
3. Price (if selling multiple price points)
4. Structured Snippet (if variety important)
5. Promotion (if on sale)

## 5. PERFORMANCE MAX CAMPAIGNS

### 5.1 What is Performance Max?

**Automated campaign type:**
- Runs across: Google Search, Display, Gmail, YouTube, Maps
- You control: Budget + assets
- Google controls: Bidding, placement, format optimization
- Best for: Scale campaigns, maximum reach

### 5.2 Asset Group Setup (Core)

**Asset types:**
1. **Headlines** (3-15)
   - Create: 8-10 unique, benefit-driven
   - Length: 30 chars max
   - Examples:
     - "Authentic Samsung Phones"
     - "Lowest Price Guarantee"
     - "Same Day Delivery"
     - "Official Retailer"

2. **Descriptions** (2-5)
   - Length: 90 chars max
   - Examples:
     - "Buy authentic phones with warranty. Fast shipping nationwide."
     - "Shop latest models. Expert advice available. Easy returns."

3. **Images** (3-5)
   - Formats: 1.5:1, 1:1, 4:5
   - Specs: Min 600x314, 600x600, 450x1000
   - Content: Product lifestyle, use-cases, testimonials

4. **Videos** (optional but recommended)
   - Length: 15-30 seconds
   - Content: Product features, testimonial, benefit demo
   - Formats: 16:9, 1:1, 9:16

5. **Logo** (optional)
   - 1:1 ratio, 128x128px min
   - Brand logo

6. **Business name** (required)
   - Brand or store name

### 5.3 Audience Signals (Guide ML)

**What:** Provide audience hints (Google does targeting)

**Setup:**
- Remarketing audiences: Past visitors (if available)
- In-market audiences: People researching your category
- Affinity audiences: People interested in your category long-term
- Custom intent: Keywords for people you want to reach
- Demographics: Age, gender, location (optional hints)

**Example setup:**
- Remarketing: Website visitors 30 days
- In-market: "Electronics shoppers", "Laptop buyers"
- Custom intent: "gaming laptop", "laptop dưới 10 triệu", "buy laptop online"
- Location: Vietnam (all or cities if premium)

### 5.4 Asset Group Strategy

**Strategy 1: Multiple Asset Groups by segment**
```
Performance Max Campaign: Electronics
├── Asset Group 1: Phones (focus keywords: phones, smartphones)
├── Asset Group 2: Laptops (focus keywords: laptop, computer)
└── Asset Group 3: Accessories (focus keywords: charger, case)
```

Benefits: Google learns audience separately per segment

**Strategy 2: Single focused Asset Group**
```
Performance Max Campaign: All Products
├── Asset Group 1: Everything (all products)
   - Audience signals: Broad (phones, laptops, etc.)
   - Max reach, Google optimizes
```

Benefits: Simplicity, larger training data

### 5.5 Performance Max Optimization

**Initial phase (Week 1-2):**
- Bid strategy: "Maximize conversions" (volume to learn)
- Budget: 5-10M VND/day minimum
- Monitor: Conversion events tracking properly
- Don't change: Assets every day

**Growth phase (Week 3-4):**
- Switch to: "Target CPA" or "Target ROAS" (if profitable)
- Scale: Increase budget +50% if ROAS > 2.5x
- Refresh: Update assets (images, videos) weekly if low ROAS

**Maturity phase (Week 5+):**
- Optimize: A/B test assets (try new images monthly)
- Scaling: Horizontal (add asset groups) or vertical (increase budget)
- Monitor: Conversion rate, ROAS trend

## 6. DISPLAY & YOUTUBE CAMPAIGNS

### 6.1 Display Campaign (Brand awareness + Retargeting)

**When to use:**
- Awareness phase: Reach broad audience
- Retargeting: Show ads to past website visitors
- Mid-funnel: Nurture interested prospects

**Campaign settings:**
- Network: Display Network (entire GDN)
- Placement: Automatic (Google chooses from 2M+ sites)
- Format: Text, image, responsive

**Targeting options:**

| Option | Use case | Example |
|--------|----------|---------|
| **Audience** | Reach specific people | In-market audiences, affinity, remarketing |
| **Placement** | Target specific sites | YouTube channels, news sites, blogs |
| **Keywords** | Context matching | Articles about your product |
| **Topics** | Broad category targeting | "Phones & Telecom" topic |
| **Demographic** | Age, gender, parental status | Women 25-45 |

**Recommended: Remarketing**
```
Audience: Website visitors (past 30 days)
Budget: 2-5M VND/day
Goal: Remind them, encourage return
Creative: Soft "Come back" message, not hard sell
```

### 6.2 YouTube Ads (Video content + TrueView)

**Ad formats:**

1. **Skippable In-stream (TrueView)** - Most common
   - User can skip after 5 seconds
   - Pay only if watched 30s or more
   - Best for: Long-form storytelling
   - Duration: 12-60 seconds optimal

2. **Non-skippable In-stream**
   - User must watch full ad (max 20s)
   - CPV higher but guaranteed views
   - Best for: Quick product demo
   - Duration: 15-20s max

3. **Bumper Ads**
   - 6-second unskippable
   - CPM-based pricing
   - Best for: Brand reminder
   - Duration: Exactly 6s

4. **In-feed Video Ads**
   - Appear in YouTube search results
   - Thumbnail + title shown
   - Click to expand/watch
   - Best for: High-intent, product-specific

**Targeting on YouTube:**
- Keywords: Search terms
- Placements: Specific channels/videos
- Audiences: In-market, affinity, remarketing
- Demographics: Age, gender, interests
- Exclude: Competitors, low-quality channels

**Best practices:**
- Hook first 3 seconds (people scroll fast)
- Vertical text overlay (80% watch muted)
- CTA at end (clickable link to landing page)
- Frequency cap: 3-4 times per user per day

## 7. CONVERSION TRACKING SETUP (CRITICAL)

### 7.1 Google Tag Manager Implementation

**Setup:**
1. Create GTM account (tagmanager.google.com)
2. Create GTM container (Web)
3. Install GTM code on all pages: Head section
4. Add Google Analytics 4 tag to GTM
5. Create conversion trigger: Purchase event
6. Test: Preview mode → trigger purchase on test order

**Tag structure for TMĐT:**

```
Tags:
├── GA4 Configuration Tag
├── GA4 Purchase Event Tag (triggers: Purchase)
├── GA4 Add to Cart Tag (triggers: Add to cart)
├── GA4 View Item Tag (triggers: View product)
└── Google Ads Conversion Tag (triggers: Purchase)

Triggers:
├── Page view
├── Add to cart (JavaScript event)
├── Purchase (confirmation page: /thank-you)
└── Form submission

Variables:
├── Data layer variable: transactionId
├── Data layer variable: transactionValue
├── Data layer variable: itemName
└── JS variable: userId
```

### 7.2 E-Commerce Event Tracking

**Critical events:**

| Event | When | Data to track |
|-------|------|--------------|
| **view_item** | Product page load | product_id, product_name, value, category |
| **add_to_cart** | Click add button | product_id, value, quantity |
| **begin_checkout** | Enter payment page | value, items, coupon |
| **add_payment_info** | Select payment method | payment_type (COD, card, bank) |
| **purchase** | Order confirmed | transaction_id, value, items, tax, shipping |

**Implementation example (JavaScript):**

```javascript
// When user clicks "Add to Cart"
gtag('event', 'add_to_cart', {
  items: [{
    item_id: "SKU_001",
    item_name: "Samsung Galaxy A12",
    price: 5000000,
    quantity: 1
  }],
  value: 5000000,
  currency: "VND"
});

// When order confirmed (on thank you page)
gtag('event', 'purchase', {
  transaction_id: "T_12345",
  value: 5000000,
  currency: "VND",
  tax: 500000,
  shipping: 50000,
  items: [{
    item_id: "SKU_001",
    item_name: "Samsung Galaxy A12",
    price: 5000000,
    quantity: 1,
    category: "Electronics > Phones"
  }],
  user_id: "USER_001" // Optional but recommended
});
```

### 7.3 Enhanced Conversions (PII hashing)

**Purpose:** Help Google match offline conversions to users

**Data to hash:**
- Email (most reliable)
- Phone number
- First name + last name + country
- Address

**Setup:**
- Google Ads → Conversions → Create conversion
- Turn on: "Enhanced conversions"
- Select: Email + phone fields from form
- Google: Automatically hashes, secures data

**Privacy compliance:**
- GDPR compliant (Google handles hashing)
- Clear consent: "We'll use data to match your purchase"
- ROI: 15-25% ROAS improvement from better matching

### 7.4 Conversion Value Rules (Advanced)

**Purpose:** Adjust conversion value based on conditions

**Example:**
- Base product price: 1M
- If customer from HCM: Value = 1M (high AOV area)
- If customer from rural: Value = 1M * 1.2 (shipping cost)
- If purchased electronics: Value = 1M * 0.9 (lower margin)

**Setup:**
- Google Ads → Tools → Conversions → [Conversion] → Conversion value rules
- Rule: If [condition] then value = [amount]

**Practical for VN TMĐT:**
- Regional pricing adjustments
- Product category margins
- Seasonal adjustments

## 8. LANDING PAGE QUALITY SCORE

### 8.1 Quality Score Components

**Quality Score (1-10) determined by:**

| Factor | Weight | How to improve |
|--------|--------|----------------|
| **Click-through rate (CTR)** | 40% | Better headlines, relevant keywords |
| **Ad relevance** | 30% | Match ad copy to keyword |
| **Landing page quality** | 30% | Fast load, mobile, clear CTA |

### 8.2 Landing Page Checklist

**1. Relevance**
- [ ] Page title matches ad headline
- [ ] Content matches keyword intent
- [ ] Product shown matches what user searched
- [ ] No "bait and switch" (ad says phone, page sells laptop)

**2. Speed**
- [ ] Page loads <3 seconds (use PageSpeed Insights)
- [ ] Images optimized (compress)
- [ ] Lazy load images below fold
- [ ] Server fast (CDN, hosting quality)

**3. Mobile optimization**
- [ ] 50% of Vietnam traffic mobile
- [ ] Text readable (font >12px)
- [ ] Buttons clickable (48x48px minimum)
- [ ] Responsive layout (no horizontal scroll)

**4. Security**
- [ ] HTTPS (not HTTP) - Google requirement
- [ ] No security warnings
- [ ] Safe payment forms

**5. Trust signals**
- [ ] Company logo, contact info top
- [ ] Customer reviews (with star rating)
- [ ] Trust badges (secure payment, warranty)
- [ ] Clear return policy
- [ ] Contact form / customer service number

**6. Clear CTA (Call-to-action)**
- [ ] Primary CTA visible above fold
- [ ] Action words: "Buy Now", "Add to Cart", "Get Quote"
- [ ] Color stands out (contrast)
- [ ] Size: Large enough for mobile click

**7. Product information**
- [ ] High-quality images (multiple angles)
- [ ] Price clearly shown
- [ ] In-stock indicator
- [ ] Shipping info, delivery time
- [ ] Detailed specs/features

**Example: Quality landing page flow**

```
Header:
- Logo, search, cart, account

Hero section (above fold):
- Product image (80% of screen width)
- Product name + price
- Star rating (e.g., 4.8/5 stars, 2,340 reviews)
- "Add to Cart" button (prominent, green)
- Free shipping banner

Product details:
- Images: 5+ product angles
- Description: Features, benefits
- Specs table: Dimensions, weight, colors
- Reviews section: Top reviews

Trust section:
- "10,000+ happy customers"
- "30-day money-back guarantee"
- "Free shipping nationwide"
- Trust badges (secure payment, warranty)

Footer:
- Contact info
- Return policy
- Warranty info
```

## 9. KEYWORD RESEARCH TOOLS FOR VN MARKET

### 9.1 Free Tools

**Google Keyword Planner**
- Free with Google Ads account
- Show: Search volume, competition, avg CPC
- VN market: Good data for Vietnamese terms
- Limitation: Ranges not exact numbers (Low/Medium/High)

**Google Trends**
- See: Search trend over time
- Seasonal patterns: Phones more searched year-end
- Compare keywords: "Laptop" vs "Gaming laptop"
- VN setting: trends.google.com (set to Vietnam)

**Google Search Suggest**
- Type keyword in Google search
- See: Related suggestions (actual searches)
- Free data: Real user search behavior
- Use: End of keyword for long-tail keywords

### 9.2 Paid Tools (Worth for bigger budgets 10M+)

**Semrush, Ahrefs, Moz**
- All have Vietnam keyword data
- Show: Exact search volume, CPC, competition
- Provide: Keyword difficulty score

## 10. REPORTING & OPTIMIZATION CADENCE

### 10.1 Daily Report

```
Date: 2024-01-15
Budget spent: 5M VND
Performance vs target:
- Conversions: 23 (target 25) -8%
- Conv value: 2.3M (target 2.5M) -8%
- ROAS: 2.45x (target 2.5x) -2%

Ad groups needing action:
- Phones - High ROAS (3.2x): SCALE budget +30%
- Laptops - Low ROAS (1.8x): OPTIMIZE ad copy
- Accessories - New: MONITOR (learning phase)

Quality Score alerts:
- Electronics > Phones: Quality Score 7 (from 8) - DIAGNOSE
  → Low CTR, test new headlines

Pixel health:
- Purchase events: 23 received
- Delay: <4 hours ✓

Next actions:
1. Scale Phones campaign +30% budget
2. Pause laptop ads with <1.5x ROAS
3. Debug QS 7 (low CTR issue)
4. Test 3 new laptop headlines
```

### 10.2 Weekly Deep Dive

```
Week of: Jan 8-14, 2024

Performance Summary:
- Total spend: 35M VND
- Conv value: 92.5M VND
- ROAS: 2.64x (target 2.5x) ✓
- Trend: ↑ 8% vs last week

Campaign Analysis:
Campaign: Shopping
- Spend: 14M (40%)
- Revenue: 52M (ROAS 3.71x) ✓✓
- Top performer: Electronics
- Recommendation: Scale +50% budget

Campaign: Search
- Spend: 12M (34%)
- Revenue: 28M (ROAS 2.33x)
- Top performer: Brand keywords (4.2x)
- Issue: Competitor keywords low ROAS (1.5x)
- Recommendation: Increase brand keyword budget, reduce competitor

Campaign: Display
- Spend: 6M (17%)
- Clicks: 450
- CPC: 13.3K
- Conv rate: 1.2% (low)
- Issue: Retargeting audience low performing
- Recommendation: Increase frequency cap to 3x (currently 5x)

Performance Max:
- Spend: 3M (9%)
- Learning phase
- Conversions: 8
- Monitor: Need 50+ conversions before scaling

Keyword insights:
- Top 10 keywords: 65% of revenue
- Long-tail keywords: 30% of revenue
- Brand keywords: 80% ROAS
- Non-brand: 60% ROAS

Ad copy winners:
- Headline: "Free Shipping" (CTR +15%)
- CTA: "Buy Now" (CTR +12%)
- Mention: "Limited stock" (ROAS +8%)

Next week priorities:
1. Scale Shopping campaign (working best)
2. Optimize Search non-brand (low ROAS)
3. Refresh Display retargeting creative
4. Launch 2nd Performance Max for new products
5. A/B test new headlines for low-performing keywords
```

### 10.3 Monthly Strategy Review

```
January 2024 Performance:

Executive Summary:
- Total budget: 140M VND (+40% vs Dec)
- Total revenue: 468M VND (ROAS 3.34x, target 2.5x) ✓✓
- New customer acquisition: 2,340 (cost: 59.8k/customer)
- Return customer repeat: 28% (vs 25% target)

Channel Performance:
1. Google Shopping: 167M revenue (36% of total)
   - ROAS: 3.71x (best performer)
   - Recommendation: Allocate 50% of new budget here

2. Google Search: 198M revenue (42% of total)
   - ROAS: 2.64x (solid)
   - Brands 4.0x, Non-brand 2.2x
   - Need to optimize non-brand keywords

3. Display & Remarketing: 68M revenue (15% of total)
   - ROAS: 2.13x (lagging)
   - Creative needs refresh

4. Performance Max: 35M revenue (7% of total)
   - New channel, learning phase
   - Conversion: 18
   - Scale after 50+ conversions

Regional performance:
- HCM: 45% of revenue (ROAS 3.8x) ✓ Highest
- Hanoi: 35% of revenue (ROAS 3.2x)
- Others: 20% of revenue (ROAS 2.8x)
- Recommendation: Increase HCM bid adjustment +15%

Product category performance:
- Electronics: 520M revenue (ROAS 3.6x)
- Fashion: 180M revenue (ROAS 2.8x)
- Home: 95M revenue (ROAS 2.2x)
- Recommendation: Scale electronics, optimize fashion

Competitive analysis:
- Market growth: +25% YoY
- Your growth: +40% YoY (outpacing market)
- Brand share: Estimated 8% (vs 5% competitor average)

Month-over-month trends:
- Jan ROAS 3.34x (vs Dec 2.98x): +12% improvement
- Jan CPA 59.8k (vs Dec 78.2k): -23% improvement (better targeting)
- Frequency: Stable at 2.1x

Insights:
1. Shopping dominates profitability (3.71x ROAS)
2. Search non-brand underperforming (need keyword audit)
3. HCM market premium pricing (higher ROAS)
4. Video/Performance Max nascent but promising
5. Customer retention improving (28% repeat)

Recommendations for February:
1. Allocate 50% new budget to Shopping channel
2. Negative keyword audit on Search (remove waste)
3. Increase bid adjustment for HCM (+15%)
4. Reduce budget for Home category (2.2x ROAS <2.5x threshold)
5. Double Performance Max budget (once 50+ conversions)
6. A/B test new Shopping creative (lifestyle images)
7. Implement conversion value rules by region

Budget forecast (February):
- Conservative: 140M (maintain ROAS 3.2x)
- Growth: 200M (expect ROAS 3.0x, saturation slight)
- Aggressive: 250M (expect ROAS 2.8x, saturation more)
```

## 11. GOOGLE ADS FOR VIETNAMESE MARKET SPECIFICS

### 11.1 Market characteristics

**Search behavior VN:**
- 80%+ via mobile
- Popular search terms: "giá", "bao nhiêu", "ở đâu", "mua", "bán", "hàng", "chất lượng"
- Price-sensitive: Many include price in searches
- Local language: Vietnamese for 95%+ of searches

**Search intent examples:**

| English | Vietnamese | Intent |
|---------|-----------|--------|
| "Buy phone" | "Mua điện thoại" | Commercial |
| "Phone price" | "Giá điện thoại" | Commercial |
| "Phone shop" | "Cửa hàng bán điện thoại" | Local |
| "Best phone 2024" | "Điện thoại tốt nhất 2024" | Informational |
| "Android phone" | "Điện thoại Android" | Category |

### 11.2 Regional differences

**HCM** (Highest purchasing power)
- Higher ROAS (3.8x average)
- Premium products perform better
- Weekend concentration
- Delivery same-day expected

**Hanoi** (Strong market, growing)
- Medium ROAS (3.2x average)
- Mix of price-conscious + premium
- Weekday shopping stronger
- 1-2 day delivery acceptable

**Da Nang & Regional** (Emerging)
- Lower ROAS (2.8x average)
- Price-sensitive shoppers
- Delivery 2-3 days acceptable
- Seasonal: Higher during holidays

**Tier 2-3 cities** (Volume opportunity)
- ROAS lower (2.2x) but high volume potential
- Very price-sensitive
- Long tail keywords dominate
- Shipping cost significant

### 11.3 Payment methods VN

**COD (Cash on Delivery)** - 70% of orders
- Most trusted, highest conversion
- Ads should highlight: "Giao hôm nay - Trả khi nhận"
- Landing page: No required payment upfront

**Bank transfer** - 20% of orders
- Popular with repeat customers
- Ads mention: "Chuyển khoản nhanh chóng"

**E-wallets (Momo, Zalo Pay)** - 10% of orders
- Growing fast, especially young demographic
- Ads: Show all payment options

**Card payment** - <5% of orders
- Trust issues, fraud concerns
- Avoid emphasizing card payments in ads

### 11.4 Seasonal campaigns

**Tet (Lunar New Year) - End Jan/Feb**
- Traffic spike: +100% vs normal
- Conversion spike: +50% (gift buying)
- Budget: 3x normal
- Products: Gift items, premium products, electronics
- Messaging: "Quà Tết", "Tặng ngay", "Năm mới"

**Mid-Autumn Festival (Aug-Sep)**
- Traffic spike: +50%
- Target: Gifts, traditional items
- Budget: 2x normal

**11/11 Mega Sale (Nov 11)**
- Unofficial but huge in VN
- Traffic spike: +200%
- Conversion: Heavy discounts expected
- Budget: 4x normal
- Messaging: Big discount numbers

**12/12 Sale (Dec 12)**
- Similar to 11/11, slightly smaller
- Budget: 3x normal

**Back to school (Aug-Sep)**
- Electronics, stationery, clothing
- Budget: 2x normal
- Target: Parents searching for school supplies

### 11.5 Cultural considerations

**Language nuances:**
- Use "VND" not "đ" symbol in ads (clearer)
- Tone: Casual, conversational (not stiff)
- Avoid: Formal corporate language
- Include: Local slang if authentic

**Trust signals for VN:**
- "Hàng chính hãng" (Authentic)
- "Bảo hành" (Warranty) - Very important
- "Đổi trả dễ dàng" (Easy return)
- "10,000+ khách hàng hài lòng" (Customer testimonials)
- "Được nhiều người tin tưởng" (Trusted by many)

**Payment assurance:**
- Emphasize: Giao hôm nay trả khi nhận (COD reassurance)
- "Không cần trả tiền trước"
- "Có thể kiểm hàng trước khi trả tiền"

---

## CONCLUSION

Successful Google Ads for Vietnam TMĐT requires:

1. **Google Shopping dominates** (highest ROAS 3.7x), allocate 40%+ budget
2. **Local keyword research** in Vietnamese, price-sensitive searches
3. **Regional optimization** (HCM premium, others price-conscious)
4. **Mobile first** (80%+ traffic mobile)
5. **COD reassurance** (highest conversion payment method)
6. **Fast conversion tracking** (Pixel + GTM + Enhanced conversions)
7. **Regular optimization** (daily monitoring, weekly deep dive, monthly strategy review)

Hiệu suất dự kiến: ROAS 2.5-3.5x với setup đúng chuẩn và tối ưu liên tục.
