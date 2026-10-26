---
name: ecom-facebook-ads-strategy
description: >
  Chiến lược Facebook/Meta Ads toàn diện cho thương mại điện tử Việt Nam. Hướng dẫn chi tiết về cấu trúc chiến dịch, targeting audience, quản lý ngân sách, tối ưu hóa quảng cáo, và đo lường hiệu suất. Dùng skill này khi cần: lập chiến lược Facebook Ads, tối ưu campaign Meta, quản lý ngân sách quảng cáo Facebook, targeting audience VN, phân tích hiệu suất Facebook Ads.
---

# CHIẾN LƯỢC FACEBOOK/META ADS TOÀN DIỆN CHO TMĐT VIỆT NAM

## 1. CẤU TRÚC CHIẾN DỊCH FACEBOOK ADS

### 1.1 CBO vs ABO - Chọn mô hình nào?

**Campaign Budget Optimization (CBO)**
- **Khi dùng:** Chiến dịch có 3+ ad sets, dự tính chạy dài hạn (7+ ngày), budget lớn (5+ triệu/ngày)
- **Ưu điểm:**
  - Facebook tự điều phối ngân sách giữa ad sets hiệu quả nhất
  - Tối ưu ROAS toàn chiến dịch, không phải từng ad set
  - Giảm CPM trung bình 10-20% so với ABO
  - Học nhanh hơn với diverse audience
- **Nhược điểm:**
  - Khó kiểm soát chi tiêu từng ad set
  - Cần data đủ (50+ conversion/ad set trong 3 ngày để tối ưu tốt)
- **Ngân sách CBO:** 10-50 triệu/ngày cho 3-5 ad sets

**Ad Set Budget Optimization (ABO)**
- **Khi dùng:** Testing phase, budget nhỏ (<3 triệu/ngày), cần kiểm soát từng audience
- **Ưu điểm:**
  - Kiểm soát chi tiêu chính xác cho mỗi ad set
  - Tốt cho A/B testing
  - Rõ ràng xem audience nào convert tốt
- **Nhược điểm:**
  - Facebook không tối ưu giữa ad sets
  - CPM cao hơn CBO
  - Learning phase dài hơn
- **Ngân sách ABO:** 2-5 triệu/ad set/ngày

### 1.2 Cấu trúc 3 cấp: Campaign → Ad Set → Ad

```
Campaign (Cấp 1)
├─ Thông tin: Tên, Mục tiêu, Ngân sách, Lịch chạy
├─ Ad Set 1 - Audience 1 (Cấp 2)
│  ├─ Audience: Core, Custom, Lookalike
│  ├─ Placement: Facebook, Instagram, Messenger, Audience Network
│  ├─ Budget: X triệu/ngày
│  ├─ Schedule: Giờ, ngày chạy
│  └─ Ad 1, Ad 2, Ad 3 (Cấp 3)
│     ├─ Creative: Image, Video, Carousel
│     ├─ Copy: Headline + Primary text
│     └─ CTA: Learn More, Shop Now, Sign Up
├─ Ad Set 2 - Audience 2
│  ├─ Audience: Lookalike 1%
│  ├─ Budget: Y triệu/ngày
│  └─ Ad 4, Ad 5
└─ Ad Set 3 - Audience 3
   ├─ Audience: Retargeting
   └─ Ad 6, Ad 7
```

**Tại sao cấu trúc 3 cấp?**
- Campaign: Dùng để report tổng, A/B test mục tiêu khác nhau
- Ad Set: Dùng để kiểm soát audience, placement, budget, schedule
- Ad: Dùng để test creative, copy, CTA

## 2. MỤC TIÊU CHIẾN DỊCH THEO FUNNEL

### 2.1 Awareness Phase - Tăng nhận biết thương hiệu

**Mục tiêu:** Reach, Impressions, Video Views

**Reach Campaign**
- Mục đích: Tiếp cận số lượng người lớn nhất với giá rẻ
- Tối ưu hóa: Reach (số người)
- Ngân sách: 2-5 triệu/ngày
- Thời gian: 7-14 ngày để xác định creative nào hot
- Metrics cần theo dõi:
  - CPM: 3-8k VND là tốt (VN average 5k)
  - Reach: Bao nhiêu người unique thấy quảng cáo
  - Frequency: Bao nhiêu lần mỗi người thấy (tối ưu: 2-3)
- Creative: Video 15-30s, carousel, community engagement post
- Khi nào chuyển sang Consideration: Khi CPM ổn định, frequency > 3

**Video Views Campaign**
- Mục đích: Tăng video views cho content
- Tối ưu hóa: Video views (3-second view)
- Ngân sách: 1-3 triệu/ngày
- Metrics:
  - CPV: 200-500 VND/view là tốt
  - View rate: % người thấy video của tất cả impressions
  - Play rate: % người click play
- Creative: Video dưới 60s, hook mạnh trong 3 giây
- Dùng cho: Building audience, viral content, pre-engagement

### 2.2 Consideration Phase - Thúc đẩy quan tâm

**Traffic Campaign**
- Mục đích: Đưa người vào website/shop
- Tối ưu hóa: Link clicks
- Ngân sách: 3-8 triệu/ngày
- Thời gian chạy: 7+ ngày (cần conversion data sau)
- Metrics:
  - CPC (Cost Per Click): 2-5k VND là tốt cho TMĐT
  - CTR (Click Through Rate): 1.5-3% là bình thường
  - Landing page quality: Tối ưu để giảm bounce rate
- Landing page cần có:
  - Clear value proposition (tại sao mua ở đây?)
  - Product showcase với images tốt
  - Trust signals: Đánh giá sao, số review, logo brand
  - Fast loading (<3s)
  - Mobile optimized
- Creative: Carousel (3-5 products), video with CTA, testimonial

**Engagement Campaign**
- Mục đích: Tăng like, comment, share trên post
- Tối ưu hóa: Post engagement
- Ngân sách: 500k-2 triệu/ngày
- Metrics:
  - CPE (Cost Per Engagement): 500-1500 VND
  - Engagement rate: Comment + Like + Share / Reach
- Creative: Story content, question posts, user-generated content
- Dùng cho: Community building, social proof, tăng reach organic

### 2.3 Conversion Phase - Thúc đẩy mua hàng

**Conversion Campaign**
- Mục đích: Bán hàng trực tiếp
- Tối ưu hóa: Conversion (Purchase event từ pixel)
- Ngân sách: 5-15 triệu/ngày (scale cao nhất)
- Thời gian: 7+ ngày setup, 3+ ngày learning period
- Metrics:
  - CPA (Cost Per Acquisition): Tương ứng với margin sản phẩm
    - Sản phẩm giá 100-500k: CPA = 5-15% giá sản phẩm
    - Sản phẩm giá 500k-2M: CPA = 3-10% giá sản phẩm
  - ROAS (Return on Ad Spend):
    - Break even: ROAS = 1.5x
    - Tốt: ROAS = 2x
    - Rất tốt: ROAS = 3x+
  - Conversion rate: 1-5% tùy product (điện thoại 1-2%, thời trang 2-4%)
- Cấu hình conversion:
  - Pixel cài trên tất cả trang web
  - Event: ViewContent, AddToCart, Purchase
  - Optimization: Tối ưu cho Purchase event
- Creative: Product showcase, customer testimonial, before-after

**Add To Cart Campaign**
- Mục đích: Khuyến khích thêm sản phẩm vào giỏ
- Tối ưu hóa: Add to cart event
- Ngân sách: 3-8 triệu/ngày
- Khi dùng: Khi conversion rate quá thấp, làm warm up trước purchase campaign
- Metrics:
  - Cost per ATC: 2-8k VND
  - Cart completion rate: % người hoàn tất checkout (target 40-60%)
- Retargeting: Những người add to cart nhưng không mua

**Lead Generation Campaign**
- Mục đích: Thu thập thông tin khách (email, phone, form)
- Tối ưu hóa: Leads (form submission)
- Ngân sách: 1-5 triệu/ngày
- Metrics:
  - Cost per lead: 2-10k VND
  - Form completion rate: 30-50%
- Dùng cho:
  - B2B sales, real estate, education
  - Email list building
  - Phone number collection cho sales call
- Form cần có:
  - Max 2-3 fields (Name + Email + Category)
  - Mobile optimized
  - Clear benefit statement

## 3. AUDIENCE TARGETING CHO THƯƠNG MỚI ĐIỆN TỬ VIỆT NAM

### 3.1 Core Audience - Lõi khách hàng

**Demographics Targeting**
- **Tuổi:** 18-55 (phần lớn TMĐT VN)
  - Online shoppers 18-35: Nhóm chính, tech-savvy, sẵn sàng try new brand
  - 35-45: High income, có con, sẵn sàng chi phí cao hơn
  - 45-55: Ít shopping online, target khi product phù hợp (sức khỏe, nhà)
- **Giới tính:** Flexible, phụ thuộc product
  - Thời trang nữ: Women 18-45
  - Thời trang nam: Men 18-50
  - Home & living: Women 25-50 (quyết định mua chính)
- **Vị trí địa lý:**
  - Toàn quốc: Delivery toàn VN
  - Thành phố lớn (HN, TP.HCM, Đà Nẵng): Income cao, online shopping frequency cao
  - Ngoại thành: Targeting tách riêng, CPA cao hơn do delivery cost

**Interest Targeting**
- Dùng cho: Core audience khi brand new, chưa có conversion data
- Độ cụ thể: 50k-500k người (quá nhỏ <10k: CPM cao)
- Interests phù hợp cho TMĐT:
  - **Fashion:** "Women's fashion", "Shopping", "Instagram"
  - **Electronics:** "Technology", "Smartphones", "Gadgets"
  - **Home:** "Home & Living", "Interior Design", "DIY"
  - **Beauty:** "Beauty", "Cosmetics", "Skincare", "Health & Wellness"
  - **Sports:** "Fitness", "Athleisure", "Sports equipment"
- Interest stacking: Nên combine 2-3 interests để refine audience
  - VD: "Women's fashion" + "Instagram" + "Shopping" = chính xác hơn

**Behavior Targeting**
- **Online shoppers:** Người hay mua hàng online
  - Tăng conversion rate 10-15% so với cả population
- **High spenders:** Người có chi phí online cao
  - Dùng cho: Premium products
- **Mobile users:** Người dùng smartphone nhiều
  - VN: 90% TMĐT qua mobile, nên nearly 100% audience
- **Social media active:** Người active trên social platforms
  - Dùng để exclude low-intent users

### 3.2 Custom Audience - Retargeting khách cũ

**Website Visitors**
- **Tất cả visitors:** 180 ngày
  - Dùng cho: Brand awareness retargeting, general audience
- **Product page viewers:** Người xem sản phẩm (30-45 ngày)
  - Dùng cho: Conversion campaign, incentive offers
- **Checkout viewers:** Người vào page thanh toán nhưng không mua (7-14 ngày)
  - Dùng cho: Abandoned cart recovery, discount offers
  - Messaging: "Hoàn tất đơn hàng của bạn" + discount 5-10%
- **Add to cart (không mua):** 7-30 ngày
  - Messaging: "Sản phẩm trong giỏ của bạn sắp hết hàng"
- **Purchase customers:** Người đã mua (60-180 ngày)
  - Dùng cho: Upsell, cross-sell, loyalty
  - Messaging: "Khách hàng yêu quý" + exclusive offer

**Customer List Upload**
- Upload danh sách email/phone khách cũ
- Facebook match với 60-70% email
- Dùng cho: Retargeting khách existing, win-back campaign
- Quy tắc:
  - Email/phone phải clear (đúng format)
  - Hashed data an toàn
  - Comply với GDPR/local privacy law

**Engagement Audience**
- **Video viewers (3+ giây):** 180 ngày
  - Dùng cho: Conversion campaign sau video view
- **Post engagers:** Người like/comment/share post (180 ngày)
  - Dùng cho: Brand retargeting, community building
- **Page followers:** Followers page (180 ngày)
  - Dùng cho: New product launch, exclusive offers

### 3.3 Lookalike Audience - Mở rộng khách hàng

**Lookalike % Options**

| % | Mô tả | Khi dùng | Conversion rate |
|---|-------|---------|-----------------|
| 1% | Giống nhất source audience | Test, quality focus | 70-80% of source |
| 3% | Balance giữa similarity & size | Chủ yếu dùng | 60-70% of source |
| 5% | Broader, size lớn hơn | Scaling phase | 50-60% of source |
| 10% | Rộng nhất, volume cao | High budget, scaling | 40-50% of source |

**Chiến lược Lookalike cho TMĐT VN**

*Phase 1 - Testing (Budget: 2-3 triệu/ngày)*
- Lookalike 1% from Purchase audience (60-180 ngày)
  - Source: ~1000-5000 customers
  - Size: ~500k-1M people (VN ~10M Facebook users)
  - CPA: Gần bằng retargeting purchase audience
  - Dùng: First scaling test

*Phase 2 - Scaling (Budget: 5-10 triệu/ngày)*
- Lookalike 3% from Purchase audience
  - Vẫn high quality, size 1M+
  - CPA: +30-50% so với lookalike 1%
- Lookalike 1% from Add to cart audience
  - Source: ~5k-20k people
  - Size: ~500k-2M
  - CPA: Cao hơn purchase 20-50%

*Phase 3 - Max scaling (Budget: 15+ triệu/ngày)*
- Lookalike 5% from Purchase audience
  - Size lớn nhất, tập trung volume
  - CPA: +50-80% so với lookalike 1%
- Lookalike 3% from Add to cart
- Lookalike 1-3% from different sources (video viewers, post engagers)

**Best Practices Lookalike**
- Tránh overlap: Nếu chạy lookalike 1% & 3%, nên exclude lookalike 1% trong 3% campaign
- Source quality: Lookalike quality = source audience quality
  - Nếu source 80% bot/fake, lookalike cũng 80% bot
  - Vì vậy clean purchase/engagement data trước
- Exclusion: Nên exclude retargeting audience khỏi lookalike
  - VD: Lookalike 3% - Exclude: Website visitors 180 days
- Test khác nhau: Chạy lookalike từ source khác nhau, measure kết quả

## 4. QUẢN LÝ NGÂN SÁCH VÀ SCALING

### 4.1 Budget Testing - Phase 1 (Tuần 1)

**Mục tiêu:** Tìm profitable audience, determine CPA target

**Budget allocation cho TMĐT mới**
- Tổng budget tuần: 15-25 triệu
- Phân bổ:
  - Core audience (Interests): 5-8 triệu
  - Lookalike 1% (nếu có 100+ conversions): 3-5 triệu
  - Retargeting (website visitors): 2-4 triệu
  - Creative testing: 2-4 triệu (test hình ảnh, video khác)

**Chi tiết từng campaign**

| Campaign | Audience | Budget/ngày | Mục tiêu | KPI |
|----------|----------|------------|---------|-----|
| Awareness | Core interests | 1.5-2M | Reach 500k | CPM <8k |
| Traffic | Core + Lookalike 1% | 2-3M | Clicks 200+ | CPC <5k |
| Conversion | Retargeting | 1-2M | 30+ conversions | CPA <100k |
| Conversion | Lookalike 1% | 2-3M | 40+ conversions | CPA <150k |

**Stopping Rules cho unprofitable campaigns**
- Kill sau 3 ngày nếu:
  - CPA > 2x target CPA (VD: Target 100k, actual 200k+)
  - Conversion rate < 0.5%
  - ROAS < 1.3x
- Kill sau 7 ngày nếu:
  - ROAS < 2x stable (3 ngày)
  - CPA trend không cải thiện

### 4.2 Budget Scaling - Phase 2 (Tuần 2-4)

**Horizontal Scaling - Mở rộng audience**

Khi: Campaign chạy tốt, CPA ổn định, ROAS > 2.5x

Cách: Tăng ad sets, không tăng budget từng ad set

```
Tuần 1:
- Ad Set 1: Lookalike 1% → 3M/ngày
- Ad Set 2: Core interests → 2M/ngày
- Total: 5M/ngày, ROAS 2.8x

Tuần 2 (Horizontal scale):
- Ad Set 1: Lookalike 1% → 3M/ngày (keep)
- Ad Set 2: Core interests → 2M/ngày (keep)
- Ad Set 3: Lookalike 3% → 3M/ngày (NEW)
- Ad Set 4: Custom audience → 2M/ngày (NEW)
- Total: 10M/ngày, ROAS dự tính 2.6x (slight drop OK)
```

Ưu điểm:
- Ít risk, test audience mới cùng lúc
- Maintain ROAS tốt
- Dễ kiểm soát

**Vertical Scaling - Tăng budget từng audience**

Khi: Audience có sẵn convert tốt, ready để tăng volume

Cách: Tăng budget từng ad set + từng ngày

```
Tuần 1:
- Lookalike 1% → 3M/ngày, ROAS 3.2x

Tuần 2 (Vertical scale):
- Lookalike 1% → 5M/ngày (+2M), ROAS expected 3.0x

Tuần 3:
- Lookalike 1% → 8M/ngày (+3M), ROAS expected 2.8x

Tuần 4:
- Lookalike 1% → 12M/ngày (+4M), ROAS expected 2.6x
```

Quy tắc tăng: +50% budget, monitor CPA/ROAS ngày thứ 2-3
- Nếu ROAS drop >20%: Revert và tăng từ từ +30%
- Nếu ROAS stable: Tăng tiếp sau 3-5 ngày

**Khi không nên scale**
- Learning phase chưa xong (<50 conversions)
- ROAS < 2x ổn định
- Frequency > 4 (người thấy quảng cáo quá nhiều)

### 4.3 Budget theo ngày trong tuần

**VN Shopping Behavior Pattern**
- Cao nhất: Thứ 5, 6, 7, CN (weekend shopping)
- Trung bình: Thứ 2, 3
- Chi tiết dự kiến ROI theo ngày:

| Ngày | Traffic | ROAS | CPA | Ghi chú |
|-----|---------|------|-----|---------|
| Thứ 2 | -15% | -10% | +5% | Post-weekend, buying power down |
| Thứ 3 | -10% | -5% | +3% | Bắt đầu recover |
| Thứ 4 | -5% | 0% | 0% | Chuẩn bị weekend |
| Thứ 5 | +10% | +5% | -5% | Weekend start, buying power up |
| Thứ 6 | +15% | +10% | -8% | **Peak day** |
| Thứ 7 | +18% | +12% | -10% | **Peak day** |
| CN | +12% | +8% | -6% | Late weekend |

**Scheduling Strategy**

*Option 1 - Dynamic budget*
- Dùng Tools → Schedule trong Ads Manager
- Set budget tự động cao/thấp theo ngày
- VD: Thứ 2-3: 2M/ngày, Thứ 5-7: 3.5M/ngày
- Pros: Optimize naturally
- Cons: Manual setup, cần review weekly

*Option 2 - Fixed schedule*
- Chạy 24/7 budget fixed
- Pros: Simple, no burnout
- Cons: Suboptimal budget allocation
- Best for: Chạy dài hạn, budget ổn định

**Peak Time Bidding**
- Thứ 5-7: Tăng bid cap +15-20%
- Thứ 2-3: Giảm bid cap -10-15%
- Dùng để giữ vị trí ad khi CPM tăng

## 5. CHIẾN LƯỢC CREATIVE

### 5.1 Image Ads

**Single Image Ad**
- Kích thước: 1200x628px (tỷ lệ 1.91:1) hoặc 1080x1080px (square)
- Dùng khi: Product showcase, clear value, simple message
- Best practice:
  - Sáng, rõ ràng, đối tượng chính giữa khung
  - Max 20% text trên ảnh (nếu quá Facebook sẽ reduce reach)
  - Avoid busy background
  - Include person (CTR +30%) hoặc emotional image
- Copy: Short + benefit-driven
  - "Mua hôm nay, giao ngày mai"
  - "Sale 40% - Hết hàng nhanh"

**Carousel Ads**
- Max 10 cards, min 3 cards
- Dùng khi: Multiple products, story progression, features showcase
- Tỷ lệ: 1:1 hoặc 1.09:1 best performance
- Cấu trúc tốt:
  - Card 1: Hero/main product (best selling)
  - Card 2-3: Variations (colors, sizes)
  - Card 4-5: Features/benefits
  - Card 6-7: Testimonials
  - Card 8+: CTA/offer
- Headline: Khác nhau từng card để test
- CTA: "Shop now" for most cards, "Learn more" for info cards

**Collection Ads**
- Dùng khi: Multiple products, want to keep user on Facebook
- Setup: Cover image + 3-4 product thumbnail
- Conversion: Người click vào ảnh sẽ thấy mobile shop view trên Facebook
- Best for: Brands với nhiều SKU, không muốn user rời khỏi Facebook
- Cảnh báo: CTR thấp hơn link ads, nhưng conversion rate cao hơn

### 5.2 Video Ads

**Video Specs VN Recommended**
- Landscape: 1280x720 (1.78:1)
- Square: 1080x1080 (1:1) - best for mobile feed
- Vertical: 1080x1920 (9:16) - Reels format
- Duration: 15s (short form), 30s (standard), 60s (storytelling)
- File size: <4GB (usually <500MB)
- Codec: H.264 video, AAC audio

**15-second Video (Awareness & Traffic)**
- Hook: 0-3s (capture attention)
  - Open question: "Bạn muốn da mịn như thế này?"
  - Shock number: "Tiết kiệm 5 triệu/năm"
  - Pattern interrupt: Unexpected visual, bright color change
- Body: 3-12s (deliver message)
  - Product demo hoặc benefit showcase
  - 2-3 key points max
- CTA: 12-15s (call to action)
  - Text overlay: "SHOP NOW", "LEARN MORE"
  - Button: Shop, Sign up, etc.
- Sound: Music chủ yếu (90% watch muted) - trending sound từ TikTok/Instagram Reels

**30-second Video (Conversion & Storytelling)**
- Structure:
  - 0-5s: Hook + problem statement
  - 5-20s: Product + solution demo
  - 20-28s: Result + benefit
  - 28-30s: CTA + offer
- Subtitle/text: Bắt buộc (80% watch muted)
- Testimonial video: Customer talking about product (30s tốt nhất)

**60-second Video (Educational & Community)**
- Dùng cho: Tutorial, behind-the-scenes, brand story
- Best for: Engagement campaigns, awareness building
- Retention: 60s video cần strong hook, bảo đảm 50%+ people watch to end
- Tip: Thêm transition/cut đủ frequently để giữ interest

**Video Best Practices VN**
- Hook in 3 seconds: Facebook học 3 sec, nếu không hook sẽ skip
- Captions: 80% Vietnamese users watch without sound
- Motion: Tránh static shots, phải có movement
- Colors: Bright, saturated colors perform better (blue, red, yellow)
- People: Include face, expressions (emotion) - CTR +50%
- Music: Trending local + international songs
- Call-to-action: Explicit, repeat 2x if 30s+

### 5.3 UGC Style Ads (User-Generated Content)

**Định nghĩa:** Ads trông như bình thường người dùng đăng (không quá "marketing")

**Cách setup:**
- Recruit creators: Micro-influencers, real customers
- Brief: "Đăng video tự nhiên về sản phẩm này, sao bạn thích"
- Vibe: Raw, authentic, imperfect okay
- Upload: Người creator tạo video + cấp quyền dùng lại cho brand

**Performance:**
- CTR: +40-60% so với professional ads
- CPA: -20-30% (people trust real users hơn brand)
- ROAS: +50-100% vs polished ads

**Pricing UGC VN**
- Nano creator (1-10K followers): 2-5 triệu/video
- Micro creator (10-100K): 5-20 triệu/video
- Manage via: Facebook Ad Library hoặc hire agency

### 5.4 Before/After Ads (Policy considerations)

**Chính sách Facebook về Before/After:**
- ALLOW: Skincare, fitness transformations (nếu kèm disclaimer)
- CAUTION: Health/beauty claims (cần evidence)
- DENY: Health condition claims không substantiated

**Safe format VN:**
- "6 tuần kết quả" (6-week transformation)
- Kèm hashtag #PaidPartnership
- Disclaimer: "Kết quả có thể khác nhau với mỗi người"
- Avoid: "Chắc chắn", "Đảm bảo", medical claims

## 6. BIDDING STRATEGY

### 6.1 Lowest Cost Bidding

**Khi dùng:**
- Learning phase (<50 conversions)
- Testing audiences
- Budget = priority, profitability = secondary
- Conversion value = consistent

**Cách hoạt động:**
- Facebook finds cheapest conversions possible
- Không set bid cap
- Risk: Low quality conversions, click farm

**Tối ưu:**
- Tập hợp 50+ conversions trước scale
- Monitor Quality Score, ROAS daily
- Cap at 3-7 ngày, switch sang Cost Cap

### 6.2 Cost Cap Bidding

**Khi dùng:**
- Stable CPA target
- Scale phase
- Know what CPA works for margin
- 100+ conversions historical data

**Setup:**
- Cap = target CPA + 10-20% buffer
- VD: Target CPA 100k → Cap 110-120k
- Facebook tối ưu để không exceed, nhưng có thể approach

**Ưu điểm:**
- Predictable cost
- Better ROAS control
- Scaling safe

**Lưu ý:**
- Nếu set cap quá thấp: Low volume
- Nếu set cap quá cao: Pointless (quay về lowest cost)
- Monitor daily, adjust weekly

### 6.3 Bid Cap Bidding

**Khi dùng:**
- Impression/engagement campaign (không conversion)
- Video view campaign
- Reach campaign
- Bidding against other brands (competitive landscape)

**Setup:**
- Cap = maximum you pay per bid
- VD: Reach campaign, cap 5k CPM (won't bid higher)
- Facebook tối ưu giữa cost & volume dưới cap

**Chia type:**
- CPM cap: Set max price per 1000 impressions
- CPC cap: Set max price per click
- CPV cap: Set max price per 3-sec video view

## 7. CAMPAIGN OPTIMIZATION & PERFORMANCE METRICS

### 7.1 Metrics cần theo dõi

| Metric | Target | Nếu cao? | Nếu thấp? |
|--------|--------|---------|----------|
| CPM | 3-8k | Expensive, try different audience | Good |
| CPC | 2-5k | High intent gone, landing page issue | Good |
| CTR | 1.5-3% | Low creative appeal | Acceptable |
| CPA | 5-15% product price | Unprofitable, refine audience | Profitable |
| ROAS | 2.5x+ | Scale up | Refine audience |
| Conversion Rate | 1-5% | Good, check landing page | Check funnel |
| Frequency | 2-4 | Ad fatigue, need fresh creative | Lower reach |
| Cost Per Reach | 50-200 VND | Inefficient | Good |

### 7.2 Campaign Performance Tiers

**Tier 1 - Kill (ROAS < 1.5x sau 3 ngày)**
- Action: Stop spending, archive campaign
- Analysis: Audience mismatch, product/price issue, poor creative
- Next: Pivot audience hoặc creative hoàn toàn

**Tier 2 - Optimize (ROAS 1.5-2x)**
- Action: Pause low-performing ads, replace creative
- Analysis: Right audience, wrong messaging/creative
- Optimize: Headline testing, CTA button, image vs video

**Tier 3 - Scale (ROAS 2-2.5x ổn định 3+ ngày)**
- Action: Increase budget +50%, monitor 2-3 ngày
- Potential: Horizontal scale (new audience) hoặc Vertical (same audience +budget)
- Monitor: ROAS trending để detect fatigue

**Tier 4 - Aggressive Scale (ROAS 2.5x+ ổn định 5+ ngày)**
- Action: Increase budget +100% hoặc more
- Dùng CBO + Cost Cap để maximize
- Monitor: Daily, ready to pull back nếu ROAS drops
- Saturation point: Khi frequency > 5, start creative refresh

### 7.3 Optimization Workflow

**Daily (9 AM)**
- Check previous day performance
- Pause ads with CPA > 1.5x campaign average
- Monitor frequency (if >3.5, pause low-performing ad)
- Check Facebook pixel: Conversion data flowing? Error rate <2%?

**Every 3 days**
- Analyze conversion data
- Adjust bid strategy nếu needed
- A/B test insights: Winning ad version?
- Pause/continue: ROAS below threshold → kill; above threshold → scale

**Weekly (Monday)**
- Full audit: ROAS, CPM, frequency trends
- Creative refresh analysis: Worn-out ads?
- Budget allocation: Reallocate to top performers
- New audience test: Launch 1 new lookalike or demographic

**Monthly**
- Conversion rate trend: Improving or declining?
- ROAS trend: Seasonal impact?
- Audience fatigue: Need refresh?
- Budget planning for next month

## 8. RETARGETING FRAMEWORK

### 8.1 Retargeting Timeline Strategy

**Timeline 1-3 ngày: Abandoned Cart → Urgency**

Campaign: Abandoned cart recovery

Audience: Người vào checkout page nhưng không mua (7-30 ngày)

Message: Urgency + Incentive
- "Hoàn tất đơn hàng của bạn - sản phẩm sắp hết hàng"
- "Đơn hàng của bạn: X VND - Hôm nay giảm thêm 10%"
- Visual: Show exact items in their cart (Dynamic ads)

Creative:
- Dynamic Product Ads (auto-show products they viewed)
- Testimonial video (social proof)
- Urgency messaging: Hết hàng countdown

Offer: 5-10% discount hoặc free shipping

CPA Target: 50-70% of first-purchase CPA (lower risk, closer to convert)

---

**Timeline 3-7 ngày: Product Viewers → Information**

Campaign: Product interest nurturing

Audience: Người xem sản phẩm nhưng không add to cart

Message: Value proposition + Social proof
- "Tại sao 10k+ khách hàng yêu thích [product]?"
- Video: Customer testimonials, product features
- "Xem đánh giá từ khách hàng" (link to reviews)

Creative:
- Testimonial videos
- Review highlights
- Before-after (if applicable)
- Feature breakdown carousel

Offer: Free consultation, product sample, or loyalty points

---

**Timeline 7-14 ngày: Engaged Users → Incentive**

Campaign: Win-back offer

Audience: Người active trên website (click, view) nhưng không convert

Message: Special offer + FOMO
- "Khách VIP: Offer exclusive chỉ cho bạn"
- "Last chance: [Product] - Còn X cái"

Creative:
- Exclusive offer: 15-20% discount
- Limited time: "Sale kết thúc trong 3 ngày"
- Comparison: vs competitors

Offer: Conditional (requires purchase, oder limit)

---

**Timeline 14-30 ngày: All Visitors → Brand**

Campaign: Brand awareness + top of funnel

Audience: Tất cả website visitors (180 ngày)

Message: Giá trị thương hiệu, không sale
- "Khám phá tại sao [brand] khác biệt"
- "Công dân [brand]: Chất lượng, giá tốt"
- Community: "Tham gia cộng đồng 500K+ khách"

Creative:
- Brand story video
- Customer testimonials (not product focused)
- Community posts, user-generated content

Offer: No hard offer, soft CTA (Shop collection)

---

**Timeline 30+ ngày: Last Resort - Suppress**

Nếu người dùng:
- Xem 30+ ngày không convert → Consider suppress
- Xem nhưng clear not target (click through to competitor) → Suppress
- Mobile but slow website → May suppress to reduce frustration

Suppress reason: Ad fatigue, low intent already. Tốt hơn skip người này, focus tài nguyên vào warm audience.

### 8.2 Dynamic Product Ads (DPA)

**Setup:**
- Requires: Facebook Catalog (product feed)
- Pixel: Purchase event + Item ID tracking
- Requirement: 100+ catalog items, active inventory

**Campaign objective:** Conversion (with DPA)

**Audience: Custom Audience**
- Recent shoppers (7-30 days)
- Product viewers but no purchase
- Add-to-cart but no purchase

**Automatic format:**
- Facebook shows relevant products from catalog
- Based on person's browsing history
- VD: Viewed blue shirt → Show blue shirt options, similar items

**Performance:**
- ROAS: 2-4x (often best performer)
- CPA: 20-40% lower than manual ads
- Frequency: Can show 4+ weeks safely (different products)

**Optimization:**
- Keep catalog updated (out of stock → remove)
- Event tracking: Ensure item_id passes through pixel
- Budget: 3-8M/day for ~1000 items

## 9. REPORTING TEMPLATE

### 9.1 Daily Report (Personal)

Chạy mỗi sáng, track quick metrics:

```
Date: 2024-01-15

Campaign Performance:
- Awareness: Reach 45K | CPM 4.2K | Frequency 1.8
- Traffic: Clicks 234 | CPC 3.8K | CTR 2.1%
- Conversion: ATC 28 | Purchase 12 | CPA 125K | ROAS 2.4x
- Retargeting: Clicks 156 | ROAS 3.2x

Ads needing action:
- Ad_VideoV2: CPA 180K (PAUSE)
- Ad_Carousel_Spring: CPA 95K (SCALE +50%)
- Ad_Testimonial_New: Learning phase (MONITOR)

Pixel health:
- Purchase events: 12 / $1.5M revenue
- Pixel delay: <2 hours ✓

Next actions:
- Pause underperforming video
- Increase budget for carousel
- Launch 2 new creative variations
```

### 9.2 Weekly Report (Stakeholder/Client)

Format: Slide/Email, tập trung vào trends + insights

```
WEEKLY SUMMARY - [Week of Jan 8-14]

Overview:
- Total spend: 45M VND
- Total revenue: 120M VND
- ROAS: 2.67x ✓
- Trend: ↑ 15% vs last week

Campaign breakdown:
1. Conversion (purchase) - 25M spend
   - Revenue: 80M (ROAS 3.2x)
   - Status: SCALING ↑ (add budget +30% next week)

2. Traffic - 12M spend
   - Clicks: 1,200 (CPC 10K)
   - Status: Optimizing (test new audience)

3. Awareness - 8M spend
   - Reach: 200K (CPM 5.2K)
   - Status: Steady

Performance insights:
- Testimonial video: Best ROAS 4.1x
- Geographic: HCM performs +40% vs average
- Time: Weekend (Fri-Sun) +25% volume

Recommendations:
- Double budget on testimonial video
- Launch HCM audience expansion
- Schedule more weekend ads

Planned for next week:
- Test lookalike 3% audience
- Refresh carousel creative
- Add product feed for DPA campaign
```

### 9.3 Monthly Report (Strategy/ROI focus)

```
MONTHLY PERFORMANCE - January 2024

Key metrics:
- Total Spend: 180M VND
- Total Revenue: 550M VND
- ROAS: 3.06x (target: 2.5x) ✓
- CPA: 89K (target: 100K) ✓
- Conversion rate: 2.1% (target: 2%) ✓

Spend breakdown:
- Awareness: 30M (17%) - CPM 5.1K
- Traffic: 45M (25%) - CPC 3.9K
- Conversion: 80M (44%) - ROAS 3.4x ✓
- Retargeting: 25M (14%) - ROAS 3.8x ✓

Audience performance:
- Lookalike 1%: ROAS 3.8x (BEST)
- Core interests: ROAS 2.9x (GOOD)
- Retargeting: ROAS 3.8x (BEST)
- Lookalike 3%: ROAS 2.4x (SCALE SLOWER)

Creative performance:
- Video testimonial: ROAS 4.1x +40% vs average
- Carousel: ROAS 2.9x baseline
- Single image: ROAS 2.3x (RETIRE)
- UGC style: ROAS 3.6x (EXPAND)

Month-over-month trend:
- Spend: 180M (↑ 50% vs Dec)
- ROAS: 3.06x (↑ from 2.8x Dec)
- CPA: 89K (↓ from 110K Dec) - Improved targeting

Key learnings:
1. Testimonial video significantly outperforms
2. Weekend days 40% higher volume
3. UGC-style ads winning over professional
4. Retargeting audience exhausting (frequency 4.2)

Recommendations:
1. Allocate 60% budget to testimonial + UGC creative
2. Implement weekly creative refresh for retargeting
3. Scale lookalike 1% audience (current ROAS leader)
4. Test new audience: Competitor followers
5. Implement DPA for product variations

Budget forecast (February):
- Conservative: 180M (maintain ROAS 2.8x)
- Growth: 250M (expect ROAS 2.5x, add volume)
- Aggressive: 350M (scale, prepare for saturation)
```

## 10. COMMON MISTAKES & FIXES

| Mistake | Tác động | Fix |
|---------|----------|-----|
| **CBO with insufficient data** | Learning never finishes, inefficient budget | Use ABO until 50+ conversions/ad set, then CBO |
| **Wrong optimization event** | Optimizing for views instead of purchase | Set conversion event = purchase, not page view |
| **Targeting too broad** | High CPM, low conversion, wasted budget | Narrow down: Age 25-35, City, Interests stack 2-3 |
| **No pixel tracking** | Can't measure ROAS, flying blind | Implement pixel, test purchase event |
| **Wrong audience scope** | CPA inflated due to poor audience match | Segment: Core vs Lookalike vs Retargeting separately |
| **Not scaling winners** | Leaving money on table, competition takes market | Double check ROAS, then scale +50% budget |
| **Ad fatigue (freq > 5)** | ROAS drops, CPA increases, waste spend | Pause tired ads, launch new creative weekly |
| **Static bidding (lowest cost forever)** | Stays cheap but low quality, low intent | Graduate to Cost Cap once 50+ conversions |
| **Exclusions not set** | Showing ads to people who already bought | Exclude purchase audience from acquisition campaigns |
| **Wrong landing page** | High traffic but low conversion | Optimize landing page: Clear CTA, mobile, fast load |
| **Budget too small** | Can't accumulate enough data, high CPM | Min 2-3M/day per campaign for 7+ days |
| **Competing with own ads** | Bidding war, CPM inflates, ROAS drops | Use CBO or exclude similar audiences across campaigns |
| **Ignoring iOS 14+ restrictions** | Can't track properly, data loss, inaccurate reporting | Implement Aggregated Events, use Conversion API |

## 11. IOS 14+ IMPACT & SOLUTIONS

### 11.1 What Changed

**Apple iOS 14.5+ (April 2021):**
- Users can opt-out of tracking (App Tracking Transparency - ATT)
- 80%+ users opt-out
- Facebook pixel partially broken on iOS

**Impact:**
- Conversions not tracked properly
- Audience data incomplete (lookalike, retargeting affected)
- Attribution window reduced
- CPA/ROAS reporting inaccurate

### 11.2 Solutions

**1. Conversion API (Priority)**
- Server-side pixel tracking
- Not blocked by iOS
- More accurate attribution
- Setup: Implement via GTM or developer

**2. Aggregated Event Setup**
- Choose 8 conversion events max
- Prioritize: Purchase > Add to cart > View content
- Facebook learns from aggregated data
- Better for modeling

**3. Broader Attribution Window**
- Default: 1-day click, 1-day view (very restrictive)
- Change to: 28-day click (ads manager setting)
- Better for longer consideration cycles

**4. Audience Adjustment**
- Smaller lookalike audiences (less data, more overlap)
- Focus on: 1st party data (retargeting), CRM email
- Test: A/B test audience sizes

**5. UTM Tracking**
- Add UTM parameters to all links
- Track in Google Analytics (more reliable)
- Use GA for retargeting (Google audience)

## 12. FACEBOOK POLICY COMPLIANCE CHO TMĐT VIETNAM

### 12.1 Restricted Categories

| Category | Rule | Impact |
|----------|------|--------|
| **Health/Medical** | Cannot claim "cure" disease | Skincare OK, medicine NO |
| **Financial** | Cannot guarantee returns | Investment products restricted |
| **Personal Care** | Weight loss claims need evidence | "Lose weight" = denied |
| **Dating** | Cannot discriminate | Age/gender OK, "seduce" NO |
| **Firearms** | Sale-prohibited in VN anyway | Affected = Vietnam sellers |

### 12.2 Ad Copy Rules

**Disallowed phrases:**
- "Click here" → "Shop now"
- "Buy now" in headline (awkward, low CTR anyway)
- "Limited time" without date (update: this is allowed now, but risky)
- Spelling errors, excessive caps
- Misleading claims: "Make $1000/day"

**Quality guidelines:**
- Professional copy, no spam
- Clear value proposition
- Avoid sensationalism
- Accurate product description

### 12.3 Image/Video Rules

**Disallowed content:**
- Explicit violence, hate speech
- Nudity (partial OK in health/fitness context)
- Misinformation
- Before-after without substantiation

**Text overlay rules:**
- Max 20% of image should be text (if more, reach reduced)
- Use Tool: Facebook's "Text Coverage Tool" to check
- Exceptions: Logos, website URLs allowed beyond 20%

### 12.4 Targeting Policy

**Cannot discriminate by:**
- Medical conditions (diabetes, AIDS)
- Race/ethnicity explicitly
- Religion (interest in religion OK, but targeting by ethnicity NO)
- Sexual orientation (interest OK, but targeting for "cure" NO)

**Can target:**
- Age (18-65 OK)
- Location (cities, postal codes)
- Interests (religion, political views, hobbies)
- Behaviors (online shoppers, high income)
- Lookalike audiences

### 12.5 Landing Page Policy

**Requirements:**
- Domain must be public (not Facebook fan page alone)
- Clear business information
- Privacy policy + Terms
- Functional contact/customer service
- Not misleading (ad copy = page content)
- Fast loading (3s+)

**Common denials:**
- Landing page = blank or under construction
- Page doesn't match ad copy
- Fake reviews/testimonials
- Suspicious merchant (no contact info, red flags)

---

## CONCLUSION & NEXT STEPS

Successful Facebook Ads for TMĐT Vietnam requires:

1. **Structure**: Campaign → Ad Set → Ad cấu trúc rõ ràng
2. **Funnel approach**: Awareness → Consideration → Conversion
3. **Testing first**: Start small, validate ROAS before scaling
4. **Audience strategy**: Mix core, custom, lookalike audiences
5. **Creative iteration**: Video > image, testimonial > promotional
6. **Daily optimization**: Monitor metrics, kill losers, scale winners
7. **Scaling discipline**: Horizontal (audience) then vertical (budget)
8. **Compliance**: Follow Facebook policies, iOS 14+ attribution

Timeline dự kiến: 2-4 tuần để có lợi nhuận với ngân sách 10-30 triệu VND.
