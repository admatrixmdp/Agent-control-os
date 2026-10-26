---
name: ecom-website-audit
description: >
  Audit toàn diện website thương mại điện tử Việt Nam.
  Dùng skill này khi cần: kiểm tra website, phân tích hiệu suất,
  audit SEO/UX/CRO, phát hiện vấn đề website, đánh giá tính cạnh tranh,
  tạo kế hoạch cải thiện website.
---

# Hướng Dẫn Audit Toàn Diện Website Thương Mại Điện Tử

## 1. AUDIT FRAMEWORK - 8 CHIỀU

Website audit phải bao gồm 8 chiều chính:

```
┌─────────────────────────────────────┐
│    ECOMMERCE WEBSITE AUDIT          │
├─────────────────────────────────────┤
│ 1. TECHNICAL (Kỹ thuật)             │
│ 2. SEO (Tìm kiếm)                   │
│ 3. UX/UI (Trải nghiệm người dùng)   │
│ 4. CONTENT (Nội dung)               │
│ 5. CONVERSION (Chuyển đổi)          │
│ 6. SPEED (Tốc độ)                   │
│ 7. SECURITY (Bảo mật)               │
│ 8. MOBILE (Di động)                 │
└─────────────────────────────────────┘
```

## 2. TECHNICAL AUDIT (Kỹ Thuật)

### 2.1 Broken Links (Liên Kết Hỏng)
- **Check method**: Tools như Screaming Frog, Google Search Console, SEMrush
- **What to look for**:
  - Internal links pointing to 404 pages
  - External links pointing to deleted pages
  - Links with HTTP errors (5xx)
  - Redirect chains (3+ hops)
- **Impact**: User experience xấu, SEO signal yếu
- **Action**:
  - ✅ Xóa hoặc sửa links hỏng
  - ✅ 301 redirect đến page mới nếu content moved
  - ✅ Cập nhật internal links

**Checklist**:
- [ ] Run link crawler (Screaming Frog free version)
- [ ] Check GSC Coverage report for 404 errors
- [ ] Manually verify top 20 internal links
- [ ] Check external links in top 10 pages
- [ ] Monitor 404 requests in server logs

### 2.2 Redirect Chains & Loops (Chuỗi Chuyển Hướng)
- **Problem**: 301 → 301 → 200 (nhiều hơn 1 hop)
- **Impact**: Slow loading, crawl budget waste, link equity loss
- **Solution**:
  - ✅ Direct redirect: Old URL → Final URL (single hop)
  - ✅ Monitor GSC for redirect warnings

**Example**:
```
❌ Bad: /old-page/ → /new-page/ → /final-page/ (3 hops)
✅ Good: /old-page/ → /final-page/ (1 hop)
```

**Tools**:
- Screaming Frog: Redirect detection
- Google Search Console: Redirect warnings
- Redirect Mapper: https://redirect-mapper.com/

### 2.3 Canonical Tags
- **Purpose**: Chỉ định URL chính nếu có duplicate content
- **Check**:
  - [ ] Canonical tags present on all pages
  - [ ] Self-pointing canonicals (page → itself)
  - [ ] No cross-domain canonicals (unless intentional)
  - [ ] Canonical not pointing to different language version (use hreflang instead)
- **Correct implementation**:
  ```html
  <link rel="canonical" href="https://example.vn/ao-thun-nam/">
  ```
- **Common mistakes**:
  - ❌ Pointing to wrong domain
  - ❌ Missing canonical entirely
  - ❌ Canonical to paginated version (should point to page 1)

### 2.4 Hreflang Tags (Multilingual)
- **Needed if**: Website multiple languages/countries
- **Implementation**:
  ```html
  <!-- Vietnamese -->
  <link rel="alternate" hreflang="vi" href="https://example.vn/">
  <!-- English -->
  <link rel="alternate" hreflang="en" href="https://example.com/en/">
  <!-- Default -->
  <link rel="alternate" hreflang="x-default" href="https://example.vn/">
  ```
- **Check**:
  - [ ] Hreflang present for each language
  - [ ] Bidirectional hreflang (A link to B, B link back to A)
  - [ ] No conflicts with canonical tags

### 2.5 Structured Data Validation
- **Schema types needed**:
  - Organization (company info)
  - Product (product details)
  - Review (ratings, reviews)
  - BreadcrumbList (navigation)
  - FAQ (questions)
- **Validation tools**:
  - Google Rich Results Test: https://search.google.com/test/rich-results
  - Schema.org validator
  - Google Search Console > Enhancements
- **Check**:
  - [ ] Organization schema on homepage
  - [ ] Product schema on product pages
  - [ ] Review/AggregateRating on product pages
  - [ ] BreadcrumbList on category/product pages
  - [ ] No validation errors (0 errors goal)

**Example Product Schema**:
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Áo Thun Nam Cotton",
  "description": "Áo thun 100% cotton mát mẻ",
  "image": "https://example.vn/image.jpg",
  "brand": {"@type": "Brand", "name": "Khoáng"},
  "offers": {
    "@type": "Offer",
    "price": "99000",
    "priceCurrency": "VND",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "128"
  }
}
```

### 2.6 Robot.txt & Sitemap
- **robot.txt checks**:
  - [ ] File exists at /robots.txt
  - [ ] Correct syntax (no blocking important resources)
  - [ ] Sitemap reference included
  - [ ] Not blocking any files needed for rendering

**Example robots.txt**:
```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /cart/
Disallow: /search/
Disallow: /?*
Sitemap: https://example.vn/sitemap.xml
```

- **Sitemap checks**:
  - [ ] Sitemap exists, valid XML
  - [ ] Includes all important pages
  - [ ] lastmod dates accurate
  - [ ] Submitted in GSC
  - [ ] Max 50,000 URLs per sitemap (split if needed)

### 2.7 HTTPS & SSL Certificate
- **Checks**:
  - [ ] All pages use HTTPS (green lock in browser)
  - [ ] Certificate valid (not expired)
  - [ ] No SSL warnings
  - [ ] No mixed content (HTTP resources on HTTPS page)
  - [ ] Redirect HTTP → HTTPS works

**Check tools**:
- Browser address bar (look for lock icon)
- SSL Labs: https://www.ssllabs.com/ssltest/
- Google Search Console: Coverage > Page indexing issues

### 2.8 Website Speed & Performance
- **Metrics**:
  - PageSpeed Insights score (mobile > 90)
  - First Contentful Paint (FCP)
  - Largest Contentful Paint (LCP < 2.5s)
  - First Input Delay (FID < 100ms)
  - Cumulative Layout Shift (CLS < 0.1)
  - Time to First Byte (TTFB < 600ms)
- **Tools**:
  - Google PageSpeed Insights
  - GTmetrix
  - WebPageTest
  - Google Search Console > Core Web Vitals

(Detailed speed optimization in section 6)

### 2.9 Crawlability & Indexability
- **Check via GSC**:
  - [ ] Coverage report: Valid pages > 95%
  - [ ] Excluded pages intentional?
  - [ ] Error pages: Fix server errors
  - [ ] Valid but excluded: Review robots rules
- **Check blocking**:
  - [ ] No important resources blocked by robots.txt
  - [ ] No noindex tags on pages to rank
  - [ ] No password protection preventing crawl

**Checklist**:
- [ ] Run GSC Coverage report
- [ ] Check excluded pages reason
- [ ] Run Screaming Frog with JavaScript enabled
- [ ] Verify robots.txt not blocking resources
- [ ] Check for noindex meta tags unintentionally

## 3. SEO AUDIT

### 3.1 On-Page SEO
- **Title Tag**:
  - [ ] Present on all pages
  - [ ] 50-60 characters
  - [ ] Unique per page
  - [ ] Contains primary keyword
  - [ ] No keyword stuffing

- **Meta Description**:
  - [ ] Present on all pages
  - [ ] 150-160 characters
  - [ ] Unique per page
  - [ ] Includes CTA
  - [ ] Compelling, no spam

- **H1 Tag**:
  - [ ] Only 1 H1 per page
  - [ ] Contains primary keyword
  - [ ] Unique across pages
  - [ ] Doesn't duplicate title tag

- **Heading Hierarchy**:
  - [ ] H1 → H2 → H3 (no jumps)
  - [ ] Logical structure
  - [ ] Multiple H2/H3 for long content

- **URL Structure**:
  - [ ] Descriptive keywords
  - [ ] Lowercase, no spaces
  - [ ] Use hyphens (-) to separate words
  - [ ] < 75 characters
  - [ ] Consistent, don't change

- **Content**:
  - [ ] Minimum 300 words (homepage 500+)
  - [ ] Natural keyword placement
  - [ ] LSI keywords included
  - [ ] No duplicate content
  - [ ] Original, not plagiarized

- **Internal Linking**:
  - [ ] 3-5 internal links per page
  - [ ] Descriptive anchor text
  - [ ] Links to relevant pages
  - [ ] No broken internal links

- **Image Optimization**:
  - [ ] Descriptive alt text
  - [ ] Proper file names
  - [ ] Optimized file size
  - [ ] Lazy loading implemented

**Audit Template** (Check top 10 pages):
```
Page | Title | Meta Desc | H1 | URL | Words | Links | Images Alt | Issues
/ao-thun-nam/ | ✅ | ✅ | ✅ | ✅ | 450 | 4 | 8/10 | 2 images missing alt
/ao-thun-nam-cotton/ | ✅ | ✗ | ✅ | ✅ | 280 | 2 | 10/10 | Meta desc too short
```

### 3.2 Keyword Rankings & Visibility
- **Check**:
  - [ ] Rankings for target keywords (use GSC, Ahrefs, SEMrush)
  - [ ] Position distribution (% top 1-3, 4-10, 11-20)
  - [ ] Average ranking position
  - [ ] Trending keywords (gaining/losing positions)
  - [ ] New opportunities (4-10 positions → can be top 3)

**Analysis**:
```
Keyword Ranking Summary:
Position 1-3: 25 keywords (15% of target)
Position 4-10: 45 keywords (26% of target)
Position 11-20: 60 keywords (35% of target)
Below 20: 50 keywords (29% of target)
Total tracked: 180 keywords

Opportunities:
- 45 keywords in 4-10 range: If optimize, can move to top 3
- 60 keywords in 11-20 range: Medium effort to improve
```

### 3.3 Click-Through Rate (CTR) Analysis
- **Low CTR indicates** (< 2%):
  - Poor title/meta description
  - Low authority (position 4-10)
  - Irrelevant to search query
- **Fix**:
  - [ ] Improve title tag (add benefit, power word)
  - [ ] Improve meta description (add CTA)
  - [ ] Improve content to better match intent
  - [ ] Test variations in GSC

**Example**:
```
❌ Current: "Áo thun nam" (Pos 8, CTR 1.2%)
✅ Improved: "Áo Thun Nam Cotton - Giá Rẻ 59K | Khoáng" (Target CTR 3%+)
```

### 3.4 Backlink Profile
- **Quality over quantity**:
  - [ ] Total backlinks: More is better, but quality matters
  - [ ] Referring domains: Diverse sources
  - [ ] Anchor text: Natural distribution
  - [ ] Toxic links: Disavow if spammy

- **Check**:
  - Ahrefs: Domain Rating (DR), Backlink count
  - SEMrush: Authority Score
  - Google Search Console: Top linking sites
- **Analysis**:
  - [ ] Is growth organic?
  - [ ] Are sources relevant?
  - [ ] Is anchor text natural?
  - [ ] Any PBN/spam links?

**Action items**:
- Identify low-quality links → Disavow
- Find high-quality link opportunities → Outreach
- Monitor new backlinks weekly

### 3.5 Competitor Benchmarking (SEO)
- **Compare with 3-5 competitors**:
  - Backlink count & quality
  - Content length (top ranking pages)
  - Keyword target strategy
  - Organic traffic estimate
  - Top pages by traffic

**Competitor Analysis Template**:
```
Competitor | Backlinks | DR/Authority | Est. Traffic | Top Keyword | Strength | Weakness
Competitor A | 1,245 | 42 | 8,500/mo | áo thun nam (Pos 2) | High DA | Limited content
Competitor B | 890 | 38 | 5,200/mo | áo nam (Pos 5) | Medium | No blog
Us | 120 | 18 | 800/mo | - | Growing | Low DA, new site
```

## 4. UX/UI AUDIT

### 4.1 Navigation & Information Architecture
- **Checks**:
  - [ ] Main navigation clear, logical (5-7 items max)
  - [ ] Sub-navigation accessible
  - [ ] Breadcrumb navigation present
  - [ ] Mobile menu functional
  - [ ] Search bar prominent
  - [ ] Logo links to homepage
  - [ ] Footer links organized

**Best practices**:
- Limit menu items to 5-7 (avoid overwhelm)
- Group related items together
- Mobile: Hamburger menu or expandable nav
- Search bar visible on all pages

### 4.2 Product Page Layout
- **Must have elements**:
  - [ ] Product images (min 5, high quality)
  - [ ] Product title & description
  - [ ] Price clearly visible
  - [ ] Add to cart button (prominent, above fold)
  - [ ] In-stock status
  - [ ] Size/color/option selector
  - [ ] Reviews & ratings
  - [ ] Trust signals (warranty, return policy)
  - [ ] Related products recommendations
  - [ ] Product video (if applicable)

**Optimal placement**:
```
┌──────────────────────────────────┐
│ Product Images (left)  │ Title    │
│                        │ Price    │
│                        │ Rating   │
│                        │ Stock    │
│ ◄─ Swipe on mobile ─►  │ Options  │
│                        │ ◈◈ CTA   │
│ Thumbnails             │ Trust    │
└──────────────────────────────────┘
Scroll down:
- Detailed description
- Specifications
- Reviews
- Related products
```

### 4.3 Search & Filter Functionality
- **Check**:
  - [ ] Search bar works correctly
  - [ ] Search results are relevant
  - [ ] Auto-complete/suggestions work
  - [ ] Filters are functional
  - [ ] Filter values make sense
  - [ ] Sort options available (price, popularity, newest)
  - [ ] Filter results update without page reload
  - [ ] Clear filters button present
  - [ ] No option overload (max 5-7 filters visible)

**Best practices**:
- Faceted navigation: Price, Color, Size, Brand, Rating
- Dynamic filters: Show only applicable options
- Clear selections: Highlight active filters
- Result count: Show "Showing 1-20 of 150 results"

### 4.4 Checkout Flow
- **Steps**:
  1. Cart page (review items, update quantity)
  2. Shipping address
  3. Shipping method
  4. Payment
  5. Order review
  6. Confirmation
- **Check**:
  - [ ] Minimal steps (4-6 steps ideal)
  - [ ] Progress indicator visible
  - [ ] Guest checkout option (don't force account)
  - [ ] Pre-filled information (if registered)
  - [ ] Clear error messages
  - [ ] Security badges visible
  - [ ] Return button to shopping at each step
  - [ ] Save address option
  - [ ] Multiple payment methods

**Optimization tips**:
- Reduce steps: Combine related info
- Clear CTAs: "Continue to shipping", "Pay now"
- Show trust: SSL badge, payment logos
- Save info: For repeat purchases
- Mobile optimization: Larger buttons, fewer form fields

### 4.5 Cart Abandonment Prevention
- **Common friction points**:
  - ❌ Shipping cost surprises (only revealed at checkout)
  - ❌ Too many form fields
  - ❌ Account creation forced
  - ❌ Limited payment options
  - ❌ No address auto-complete
  - ❌ Complex checkout flow
  - ❌ No save cart option
  - ❌ No guest checkout

- **Solutions**:
  - ✅ Display shipping cost early (product page or cart)
  - ✅ Guest checkout (optional account)
  - ✅ Multiple payment methods (card, bank transfer, COD, e-wallet)
  - ✅ Address auto-complete
  - ✅ Save cart for later
  - ✅ Exit-intent popup with discount
  - ✅ Email reminders for abandoned carts

### 4.6 Mobile Responsiveness
- **Check**:
  - [ ] Responsive design (test 320px, 768px, 1024px, 1920px)
  - [ ] Touch targets ≥ 48x48px
  - [ ] Text readable (min 16px on mobile)
  - [ ] Images scale properly
  - [ ] No horizontal scrolling
  - [ ] Forms mobile-friendly
  - [ ] Buttons large enough to tap

**Mobile testing**:
- Chrome DevTools device mode
- Google Mobile-Friendly Test
- Test on real devices

## 5. CONVERSION RATE OPTIMIZATION (CRO) AUDIT

### 5.1 Above The Fold Optimization
- **Visible without scrolling**:
  - [ ] Value proposition clear (What's the benefit?)
  - [ ] Hero image/video high quality
  - [ ] CTA button prominent (color contrast, size)
  - [ ] Trust signals visible (reviews, badges)
  - [ ] No clutter, clear message
  - [ ] Mobile-optimized

**Example**:
```
Hero section should convey:
1. WHAT: What product/service
2. WHO: Who it's for
3. WHY: Why choose us
4. CTA: What to do next
```

### 5.2 Trust Signals
- **Implement**:
  - [ ] Customer reviews (with photos)
  - [ ] Star ratings visible
  - [ ] Customer testimonials
  - [ ] Case studies/success stories
  - [ ] Money-back guarantee
  - [ ] Warranty information
  - [ ] SSL certificate badge
  - [ ] Payment security logos
  - [ ] Shipping info (free shipping, fast delivery)
  - [ ] Return policy clear
  - [ ] Contact information prominent
  - [ ] Live chat/support visible
  - [ ] Social proof (# customers served, # of reviews)

**Example trust section**:
```
┌─────────────────────────────────┐
│ ✅ 30-day money-back guarantee  │
│ ⭐ 4.8★ from 2,500+ reviews     │
│ 📦 Free shipping nationwide      │
│ 💬 24/7 customer support         │
│ 🔒 SSL secured checkout          │
└─────────────────────────────────┘
```

### 5.3 CTA Button Optimization
- **Design**:
  - [ ] High contrast color (stand out from page)
  - [ ] Large size (min 48x48px, better 60-70px)
  - [ ] Clear text ("Buy now", "Add to cart", "Get started")
  - [ ] Hover state (change color/shadow)
  - [ ] Not disabled-looking
  - [ ] Strategic placement (above fold, after description)

- **Copy optimization**:
  - ❌ Generic: "Submit", "Click here"
  - ✅ Action-oriented: "Buy now", "Add to cart", "Start free trial"
  - ✅ Benefit-driven: "Get 50% off", "Join 10,000+ customers"

**Best practices**:
- 1 primary CTA per section
- Multiple CTAs on long pages (repeat every 300-400px)
- Mobile: Fixed bottom CTA button

### 5.4 Social Proof & Scarcity
- **Social proof**:
  - [ ] Customer reviews with names/photos
  - [ ] Star ratings
  - [ ] Review count
  - [ ] Success metrics ("10,000+ customers")
  - [ ] Celebrity/influencer endorsements
  - [ ] Awards/certifications
  - [ ] Press mentions
  - [ ] User-generated content

- **Scarcity/Urgency**:
  - [ ] "Only 3 left in stock"
  - [ ] "Sale ends in 2 hours"
  - [ ] "Limited time offer"
  - [ ] Countdown timer (use sparingly)
  - [ ] "Trending" badge on popular products
  - [ ] Exclusive for members

**Psychology**:
- Scarcity: Creates urgency, increases conversion
- Social proof: Builds trust, reduces risk perception
- Combine both for maximum impact

### 5.5 Form Optimization
- **Minimize fields**:
  - [ ] Only essential fields (name, email, address)
  - [ ] Multi-step forms for long forms
  - [ ] Progress indicator
  - [ ] Smart field input (tel, email, date)
  - [ ] Auto-fill/auto-complete
  - [ ] Clear error messages (red, specific)
  - [ ] Success messages

- **Mobile forms**:
  - [ ] Large input fields (min 44px height)
  - [ ] One column layout
  - [ ] Appropriate keyboard (tel, email, number)
  - [ ] No zoom required

### 5.6 Product Recommendation Engine
- **Placement**:
  - After product description ("People also buy")
  - In cart ("Frequently bought together")
  - Homepage ("Trending now", "Best sellers")
  - Related products section
- **Algorithm**:
  - Frequently bought together
  - Similar products (same category)
  - Bestsellers
  - New arrivals
  - Personalized (if logged in)

## 6. SPEED AUDIT

### 6.1 Core Web Vitals
- **LCP (Largest Contentful Paint) < 2.5s**:
  - Optimize hero image (lazy load, responsive images, WebP)
  - Remove render-blocking JS
  - Preload critical resources
  - Server response time < 600ms

- **FID (First Input Delay) < 100ms**:
  - Reduce main thread work
  - Minify/compress JavaScript
  - Remove/defer non-critical JS
  - Code splitting
  - Web Workers for heavy computation

- **CLS (Cumulative Layout Shift) < 0.1**:
  - Set image/video dimensions
  - Avoid injecting content top of page
  - Use font-display: swap
  - Avoid animations that cause reflow

### 6.2 Metrics to Monitor
- **Google PageSpeed Insights**:
  - Mobile score > 90 (goal)
  - Desktop score > 90 (goal)
  - Check both lab data & field data
- **Field data** (real users):
  - Google Search Console > Core Web Vitals
  - Last 28 days of real user data
  - Mobile & desktop separate
- **Lab data** (synthetic):
  - Simulated conditions
  - Faster than real-world
  - Good for testing changes
- **GTmetrix**:
  - More detailed metrics
  - Waterfall chart
  - Video of page load
  - Recommendations

### 6.3 Image Optimization
- **Format**:
  - Modern format: WebP (30% smaller than JPEG)
  - Fallback: JPEG/PNG
  - For icons: SVG (scalable, small)
- **Compression**:
  - Lossy: JPEG, WebP (smaller, slight quality loss)
  - Lossless: PNG, WebP (larger, perfect quality)
  - Tools: TinyPNG, ImageOptim, Sharp
- **Lazy loading**:
  ```html
  <img src="image.jpg" loading="lazy">
  ```
- **Responsive images**:
  ```html
  <img srcset="image-small.jpg 480w, image-large.jpg 1200w" src="image-large.jpg">
  ```
- **Size optimization**:
  - Hero image: < 150KB (optimized)
  - Product images: < 100KB each
  - Thumbnails: < 50KB

### 6.4 CSS & JavaScript Optimization
- **CSS**:
  - Minify CSS
  - Remove unused CSS (PurgeCSS, UnCSS)
  - Critical CSS (inline above-fold CSS)
  - Defer non-critical CSS
  - Avoid @import (slower)

- **JavaScript**:
  - Minify JS
  - Remove unused code
  - Code splitting: Load JS per page
  - Defer non-critical scripts
  - Use async for non-blocking scripts
  - Eliminate long main thread tasks

- **Build tools**:
  - Webpack, Vite, Next.js: Auto-optimize
  - ESLint: Code quality
  - Lighthouse: Performance testing

### 6.5 Caching Strategy
- **Browser caching**:
  ```
  Cache-Control: public, max-age=31536000
  (static assets: 1 year cache)
  ```
- **Server caching**:
  - Gzip compression
  - Server-side caching (Redis, Memcached)
  - Database query caching
- **CDN**:
  - CloudFlare (free tier available)
  - AWS CloudFront
  - Bunny CDN
  - Benefits: Serve content from nearest edge, faster delivery

### 6.6 Third-Party Scripts Impact
- **Audit**:
  - [ ] Identify all 3rd party scripts (GA, ads, chat, etc.)
  - [ ] Measure impact (check Chrome DevTools)
  - [ ] Remove unused scripts
  - [ ] Lazy load non-critical scripts
  - [ ] Use async/defer

**Example**: Intercom chat script adding 200ms → Remove if not critical, or load on user interaction

## 7. SECURITY AUDIT

### 7.1 SSL Certificate
- **Check**:
  - [ ] Certificate installed (HTTPS://)
  - [ ] Certificate valid (not expired)
  - [ ] No mixed content (all resources HTTPS)
  - [ ] Grade A/A+ on SSL Labs test

**Tools**:
- SSL Labs: https://www.ssllabs.com/ssltest/
- Google Chrome: Look for lock icon

### 7.2 Security Headers
- **Implement**:
  ```
  Content-Security-Policy: Prevent XSS attacks
  X-Frame-Options: Prevent clickjacking
  X-Content-Type-Options: Prevent MIME sniffing
  Strict-Transport-Security: Force HTTPS
  Referrer-Policy: Control referrer info
  Permissions-Policy: Control browser features
  ```

**Check**: https://securityheaders.com/

### 7.3 Payment Security
- **PCI-DSS Compliance** (if processing payments):
  - [ ] Use payment gateway (Stripe, PayPal, etc.)
  - [ ] Don't store credit cards (tokenization)
  - [ ] Regular security scans
  - [ ] Firewall configured
  - [ ] SSL certificate valid

- **Payment info**:
  - [ ] Don't ask for CVV in forms (collect during payment)
  - [ ] Payment processor should handle sensitive data
  - [ ] Use established payment gateway (trusted, secure)

### 7.4 Data Protection
- **Privacy policy**:
  - [ ] Privacy policy present & accessible
  - [ ] Explains data collection & usage
  - [ ] GDPR/local law compliant
- **Cookie policy**:
  - [ ] Cookie consent (ask before setting non-essential cookies)
  - [ ] Cookie banner clear, easy to decline
  - [ ] Privacy policy link in cookie banner
- **User data**:
  - [ ] Regular backups
  - [ ] Access logs monitored
  - [ ] Staff training on data security

### 7.5 Malware & Vulnerability Scanning
- **Scan regularly**:
  - Google Safe Browsing: Check if blacklisted
  - Sucuri: Malware scanning
  - OWASP ZAP: Vulnerability testing
  - Wordfence (if WordPress): Security plugin

**Action**:
- [ ] Monthly security scans
- [ ] Fix vulnerabilities immediately
- [ ] Monitor GSC for security issues
- [ ] Email alerts for new threats

## 8. MOBILE AUDIT

### 8.1 Responsive Design
- **Test widths**:
  - 320px (mobile)
  - 480px (larger mobile)
  - 768px (tablet)
  - 1024px (laptop)
  - 1920px (desktop)
- **Tools**:
  - Chrome DevTools: Device mode
  - Mobile device testing
  - Responsive design checkers

### 8.2 Mobile Performance
- **Mobile-first approach**:
  - [ ] Optimize for mobile FIRST (not afterthought)
  - [ ] Mobile PageSpeed > 90
  - [ ] LCP, FID, CLS optimized for mobile
- **Mobile-specific issues**:
  - [ ] No horizontal scrolling
  - [ ] Touch targets ≥ 48x48px
  - [ ] Readable text (min 16px)
  - [ ] Buttons easily tappable
  - [ ] Forms mobile-optimized
  - [ ] Images scale properly

### 8.3 Mobile Checkout
- **Optimization**:
  - [ ] Guest checkout (no account required)
  - [ ] One-page checkout (or minimal steps)
  - [ ] Large input fields (easy to tap)
  - [ ] Phone number autofill
  - [ ] Address autocomplete
  - [ ] Saved payment methods (for repeat customers)
  - [ ] Multiple payment options (card, bank, e-wallet, COD)

### 8.4 App vs Web
- **Mobile app considerations**:
  - [ ] Is app needed? (check usage patterns)
  - [ ] Push notifications strategy
  - [ ] App review/rating strategy
  - [ ] App store optimization (ASO)

## 9. CONTENT AUDIT

### 9.1 Thin Content
- **Identify**:
  - Pages < 300 words (goal: 300+ words)
  - Pages with no unique value
  - Duplicate content across pages
  - Pages with low engagement (high bounce rate)

**Check**:
- [ ] Content length > 300 words minimum
- [ ] Unique per page, not duplicated
- [ ] Provides value (answer user question)
- [ ] Engagement metrics (time on page > 1 min)

### 9.2 Duplicate Content
- **Types**:
  - **Internal**: Same content on multiple URLs
  - **External**: Your content copied by others
  - **Near-duplicate**: Very similar, not exact

- **Check**:
  - Screaming Frog: Duplicate detection
  - Google Search Console: Duplicate pages
  - Copyscape: Check for external copies

- **Fix internal duplicates**:
  - [ ] Consolidate into 1 page
  - [ ] 301 redirect old URLs → new
  - [ ] Add canonical tag
  - [ ] Add unique content to each page

### 9.3 Missing Meta Tags
- **Check**:
  - [ ] Title tag: All pages
  - [ ] Meta description: All pages
  - [ ] Robots meta (noindex if needed)
  - [ ] Viewport meta tag
  - [ ] OG tags (social sharing)

**Audit spreadsheet**:
```
URL | Title | Meta Desc | H1 | Status | Action
/page1 | ✅ | ✅ | ✅ | Good | None
/page2 | ❌ | ✅ | ✅ | Needs title | Add title tag
/page3 | ✅ | ❌ | ✅ | Needs desc | Write description
```

### 9.4 Content Freshness
- **Update strategy**:
  - [ ] Blog posts: Update every 6 months (refresh, add new info)
  - [ ] Product pages: Update price, inventory, new reviews
  - [ ] Category pages: Update yearly
  - [ ] Homepage: Update quarterly

- **Content calendar**:
  - Plan updates 3 months ahead
  - Track update dates
  - Monitor impact on rankings

### 9.5 Content Quality (E-E-A-T)
- **Expertise**: Author knows subject
  - [ ] Author bio present
  - [ ] Credentials/experience shown
  - [ ] Quotes from experts
  - [ ] Data/research cited
- **Authoritativeness**: Website is trusted source
  - [ ] Quality backlinks
  - [ ] Industry mentions
  - [ ] Awards/recognition
- **Trustworthiness**: Users can trust info
  - [ ] Updated regularly (date shown)
  - [ ] Sources cited
  - [ ] Privacy/security practices
  - [ ] Contact info available

## 10. COMPETITIVE BENCHMARKING

### 10.1 Identify Competitors
- **Direct**: Same products, target market
- **Indirect**: Different approach, same audience
- **List**: Top 3-5 main competitors

### 10.2 Compare Metrics
```
Metric | Your Site | Competitor A | Competitor B | Competitor C | Benchmark
Organic traffic | 2,000/mo | 15,000/mo | 8,500/mo | 5,200/mo | 8,000-10k
Backlinks | 120 | 1,250 | 890 | 450 | 500+
Domain Authority | 18 | 45 | 38 | 28 | 35+
Avg ranking pos | 28 | 8 | 12 | 15 | 10-12
Mobile score | 85 | 92 | 88 | 90 | 90+
Pages indexed | 150 | 5,200 | 2,400 | 1,800 | 1,500+
```

### 10.3 Content Gap Analysis
- **Analyze competitor content**:
  - Word count of top pages
  - Keyword targeting strategy
  - Content format (blog, guides, videos)
  - Content freshness
- **Find gaps**:
  - Topics competitors cover but you don't
  - Keywords competitors target but you don't
  - Content formats competitors use but you don't

### 10.4 Feature Comparison
- **Compare website features**:
  - Mobile responsiveness
  - Product filtering
  - Search functionality
  - Review system
  - Live chat
  - Wishlist
  - Size guides
  - Virtual try-on

## 11. PRIORITY MATRIX (IMPACT VS EFFORT)

**Categorize issues**:
```
          Low Effort  │  High Effort
          ─────────────────────────
High      │ QUICK    │ IMPORTANT  │
Impact    │ WINS     │ PROJECTS   │
          ├──────────┼────────────┤
Low       │ FILL-    │ BACKLOG    │
Impact    │ INS      │            │
          ─────────────────────────
```

**Example**:
- **QUICK WINS** (Do first):
  - Fix broken links (2 hours)
  - Optimize title tags (4 hours)
  - Add missing meta descriptions (3 hours)
  - Fix 404 errors (2 hours)

- **IMPORTANT PROJECTS** (Plan for next quarter):
  - Rewrite thin content (20 hours)
  - Mobile checkout optimization (40 hours)
  - Build link building strategy (ongoing)
  - Content marketing program (ongoing)

- **BACKLOG** (Do if have time):
  - Add video to product pages
  - Implement A/B testing
  - Advanced personalization

## 12. ACTION PLAN TEMPLATE

```
Issue | Priority | Owner | Deadline | Status | Est. Hours | Actual Hours
────────────────────────────────────────────────────────────────────────
Fix broken links (22 links) | P1 | Dev | Week 1 | ✅ Done | 2 | 1.5
Optimize title tags (top 20 pages) | P1 | Content | Week 1-2 | In progress | 4 | 2.5
Add missing meta descriptions | P1 | Content | Week 2 | Not started | 3 | 0
Improve mobile checkout | P2 | Dev | Week 3-4 | Planning | 20 | 0
Implement Core Web Vitals optimization | P2 | Dev | Week 5-6 | Not started | 15 | 0
Rewrite 5 thin content pages | P2 | Content | Week 4-8 | Not started | 20 | 0
Build backlink strategy | P2 | SEO | Ongoing | Planning | 5/week | 0
```

## 13. SCORING SYSTEM

**Score tính điểm cho từng chiều (0-100)**:

### 13.1 Technical Score
- Crawlability & Indexing (20 points)
  - 0: Not crawlable / Not indexed
  - 10: Mostly crawlable, some errors
  - 20: Fully crawlable, indexed
- SSL & Security (15 points)
  - 0: No SSL / Security issues
  - 8: SSL only
  - 15: SSL + good security headers
- Performance (20 points)
  - 0: < 50 PageSpeed
  - 10: 50-75 PageSpeed
  - 20: > 90 PageSpeed
- Structured Data (15 points)
  - 0: No schema markup
  - 8: Basic schema (Organization)
  - 15: Complete schema (Product, Review, FAQ)
- Mobile (20 points)
  - 0: Not mobile-friendly
  - 10: Responsive but slow on mobile
  - 20: Responsive + mobile-optimized
- Broken Links & Redirects (10 points)
  - 0: Many broken links / redirect chains
  - 5: Few broken links / some redirect chains
  - 10: No broken links / direct redirects

**Technical Score = Sum of all points**

### 13.2 SEO Score (0-100)
- On-page optimization (25 points)
- Content quality (25 points)
- Backlink profile (25 points)
- Keyword positioning (25 points)

### 13.3 UX/UI Score (0-100)
- Navigation (20 points)
- Product page layout (20 points)
- Mobile UX (20 points)
- Checkout flow (20 points)
- Trust signals (20 points)

### 13.4 CRO Score (0-100)
- CTA optimization (25 points)
- Trust signals & social proof (25 points)
- Scarcity/urgency elements (20 points)
- Form optimization (20 points)
- Page conversion elements (10 points)

### 13.5 Speed Score (0-100)
- PageSpeed Insights mobile score / 90 × 100 = Score

### 13.6 Security Score (0-100)
- SSL certificate (30 points)
- Security headers (30 points)
- Malware scanning (20 points)
- Data protection practices (20 points)

### 13.7 Mobile Score (0-100)
- Responsive design (30 points)
- Mobile performance (30 points)
- Touch-friendly (20 points)
- Mobile checkout (20 points)

## 14. FINAL AUDIT REPORT TEMPLATE

### Executive Summary
- Overall score: 68/100 (Needs improvement)
- Key strengths: Mobile responsive, good content
- Key weaknesses: Low Domain Authority, broken links, slow page speed
- Opportunities: Fix quick wins, improve backlinks, optimize for Core Web Vitals
- Estimated effort: 40 hours to implement priority 1 items
- Estimated impact: 30-50% increase in organic traffic

### Findings by Category

**🔴 Critical Issues (Fix immediately)**:
1. 22 broken internal links (SEO impact, UX poor)
2. Missing title tags on 5 pages (SEO impact)
3. Core Web Vitals below threshold (Ranking impact)

**🟡 Important Issues (Fix this quarter)**:
1. Mobile checkout flow has 6 steps (industry std: 4)
2. Product pages lack review schema
3. Thin content on 10 pages

**🟢 Nice-to-haves**:
1. Add video to product pages
2. Implement chatbot

### Recommendations with Timeline

| Recommendation | Impact | Effort | Timeline | Owner |
|---|---|---|---|---|
| Fix broken links | High | 2h | Week 1 | Dev |
| Add missing titles | High | 4h | Week 1-2 | Content |
| Optimize images | High | 8h | Week 2-3 | Dev |
| Improve mobile checkout | High | 20h | Week 3-4 | Dev |
| Add product reviews | Medium | 5h | Ongoing | Product |
| Blog content (3 posts) | Medium | 20h | Week 5-8 | Content |

### Scoring Summary

| Dimension | Current | Target | Gap | Priority |
|---|---|---|---|---|
| Technical | 62/100 | 85/100 | -23 | HIGH |
| SEO | 45/100 | 75/100 | -30 | HIGH |
| UX/UI | 72/100 | 90/100 | -18 | MEDIUM |
| CRO | 55/100 | 80/100 | -25 | HIGH |
| Speed | 58/100 | 90/100 | -32 | HIGH |
| Security | 75/100 | 95/100 | -20 | MEDIUM |
| Mobile | 78/100 | 95/100 | -17 | MEDIUM |

**Overall Score: 64/100 → Target: 82/100 (18 point improvement)**

### Next Steps
1. **Week 1**: Fix critical issues (broken links, missing titles, 404s)
2. **Week 2-3**: Implement quick wins (title/description optimization, image optimization)
3. **Week 4-6**: Major improvements (mobile checkout, Core Web Vitals, content improvements)
4. **Week 7+**: Long-term improvements (backlink building, content marketing, advanced optimization)

### Monitoring & Follow-up
- Weekly: Check GSC for new errors
- Monthly: Monitor rankings, traffic, Core Web Vitals
- Quarterly: Full audit re-check, compare metrics

---

**Document Version**: 2026.04.03
**Last Updated**: 2026-04-03
**Auditor**: SEO/UX Team
**Confidentiality**: Internal Use Only
