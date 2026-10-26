---
name: ecom-seo-optimizer
description: >
  Tối ưu SEO toàn diện cho website thương mại điện tử Việt Nam.
  Dùng skill này khi cần: tối ưu SEO website, kiểm tra SEO kỹ thuật,
  tối ưu trang sản phẩm, chiến lược SEO sàn TMĐT (Shopee, Lazada, TikTok Shop),
  xây dựng chiến lược liên kết, cải thiện Core Web Vitals, audit SEO toàn bộ website.
---

# Hướng Dẫn Tối Ưu SEO Website Thương Mại Điện Tử

## 1. KIỂM TRA DANH SÁCH SEO KỸ THUẬT (Technical SEO Checklist)

### 1.1 Tốc Độ Tải Trang (Site Speed)
- **Google PageSpeed Insights**: Kiểm tra điểm trên mobile (mục tiêu: >90)
- **GTmetrix**: Phân tích chi tiết hiệu suất, xác định bottleneck
- **WebPageTest**: Test tốc độ từ nhiều vị trí địa lý
- **Mục tiêu Core Web Vitals**:
  - LCP (Largest Contentful Paint): < 2.5 giây
  - FID (First Input Delay): < 100ms
  - CLS (Cumulative Layout Shift): < 0.1
- **Tối ưu hình ảnh**: Nén ảnh, dùng WebP format, Lazy loading
- **Minify CSS/JS**: Giảm kích thước file
- **Enable gzip compression**: Nén dữ liệu truyền tải
- **Caching strategy**: Cache static assets, Browser caching
- **CDN**: Sử dụng Content Delivery Network (CloudFlare, AWS CloudFront)
- **Remove render-blocking resources**: Dùng async, defer cho JS

### 1.2 Mobile-Friendly Optimization
- **Responsive design**: Kiểm tra trên các kích thước màn hình khác nhau (320px, 768px, 1024px, 1920px)
- **Mobile First Indexing**: Tối ưu phiên bản mobile trước, desktop thứ hai
- **Viewport meta tag**: `<meta name="viewport" content="width=device-width, initial-scale=1">`
- **Touch-friendly elements**: Nút bấm tối thiểu 48x48px
- **Readable text**: Kích thước chữ tối thiểu 16px trên mobile
- **Avoid interstitials**: Tránh pop-up, modal che toàn bộ nội dung
- **Form optimization**: Input fields phù hợp mobile (tel, email, number)
- **Test với Google Mobile-Friendly Test Tool**

### 1.3 SSL/HTTPS Certificate
- **Cài đặt SSL certificate**: Tất cả trang phải có HTTPS (https://)
- **Thêm câu lệnh redirect**: Redirect HTTP sang HTTPS tự động
- **Kiểm tra Mixed Content**: Loại bỏ tài nguyên HTTP trong HTTPS page
- **Update sitemap**: Cập nhật URL sang HTTPS
- **Google Search Console**: Xác nhận property trên cả HTTP và HTTPS

### 1.4 Sitemap.xml
- **Tạo sitemap.xml**: Liệt kê tất cả URL quan trọng
- **Cấu trúc**:
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
      <loc>https://example.vn/sanpham/ao-thun</loc>
      <lastmod>2026-04-03</lastmod>
      <changefreq>weekly</changefreq>
      <priority>0.8</priority>
    </url>
  </urlset>
  ```
- **Sitemap hình ảnh**: Bao gồm tất cả hình ảnh sản phẩm
- **Video sitemap**: Nếu có video sản phẩm
- **Submit**: Gửi sitemap vào Google Search Console và Bing Webmaster Tools

### 1.5 Robots.txt
- **Tạo tệp robots.txt** ở root domain:
  ```
  User-agent: *
  Allow: /
  Disallow: /admin/
  Disallow: /cart/
  Disallow: /checkout/
  Disallow: /search/
  Disallow: /filter/
  Disallow: /?*
  Sitemap: https://example.vn/sitemap.xml
  ```
- **Block trang riêng**: Admin, thank you page, checkout page
- **Allow công cụ tìm kiếm quan trọng**: Google, Bing, Yandex
- **Kiểm tra**: Google Search Console > Robots.txt Tester

### 1.6 Schema Markup (Structured Data)
- **Cài đặt JSON-LD**: `<script type="application/ld+json">`
- **Schema types quan trọng**:
  - **Organization**: Thông tin công ty (tên, logo, địa chỉ, liên hệ)
  - **Product**: Tên sản phẩm, mô tả, hình ảnh, giá
  - **Review**: Đánh giá sao, số lượng review
  - **BreadcrumbList**: Cấu trúc phân cấp trang
  - **FAQ**: Câu hỏi thường gặp
  - **LocalBusiness**: Thông tin cửa hàng địa phương
- **Kiểm tra**: Google Rich Results Test, Schema.org validator

## 2. TỐI ƯU ON-PAGE SEO

### 2.1 Title Tag
- **Độ dài tối ưu**: 50-60 ký tự (hiển thị đầy đủ trên Google)
- **Công thức**: [Từ khóa chính] | [Tính năng/Lợi ích] | [Brand]
- **Ví dụ**:
  - ❌ Sai: "Áo thun"
  - ✅ Đúng: "Áo Thun Nam Cotton Cao Cấp - Mưa Hàng Hiệu | Khoáng"
- **Yêu cầu**:
  - Có từ khóa chính ở đầu
  - Độc nhất cho từng trang
  - Không keyword stuffing
  - Thêm brand name ở cuối

### 2.2 Meta Description
- **Độ dài tối ưu**: 150-160 ký tự (full hiển thị)
- **Công thức**: [Lợi ích] + [Chi tiết] + [CTA]
- **Ví dụ**:
  - ❌ Sai: "Áo thun nam"
  - ✅ Đúng: "Áo thun nam 100% cotton, thấm mồ hôi, không bai dãn. Giá chỉ từ 59K. Giao hàng miễn phí toàn quốc. Mua ngay!"
- **Yêu cầu**:
  - Có CTA rõ ràng (Mua, Xem, Tìm hiểu...)
  - Độc nhất, không trùng lặp
  - Bao gồm giá/khuyến mãi nếu có
  - Tự nhiên, không spam

### 2.3 H1-H6 Tag Structure
- **H1**: 1 cái cho mỗi trang, chứa từ khóa chính
  ```html
  <h1>Áo Thun Nam Cotton Cao Cấp Mưa Hàng Hiệu</h1>
  ```
- **H2-H6**: Phân chia logic nội dung
  ```html
  <h2>Tính Năng Nổi Bật</h2>
  <h3>Chất Liệu Cotton Tự Nhiên</h3>
  <h3>Thiết Kế Hiện Đại</h3>
  <h2>Hướng Dẫn Chọn Size</h2>
  <h2>Khách Hàng Nói Gì</h2>
  ```
- **Không dùng để styling**: Dùng CSS cho định dạng
- **Logic phân cấp**: H1 → H2 → H3 (không nhảy cấp)

### 2.4 URL Structure
- **Đơn giản, dễ đọc**:
  - ❌ example.vn/product?id=12345&category=45
  - ✅ example.vn/ao-thun-nam-cotton
- **Yêu cầu**:
  - Chứa từ khóa chính
  - Dùng dấu gạch ngang (-) phân tách từ
  - Độ dài < 75 ký tự
  - Không dùng ký tự đặc biệt
  - Viết thường (lowercase)
  - Cố định, không thay đổi
- **Cấu trúc danh mục**: /danh-muc/ao-thun-nam-cotton
- **301 redirect**: Nếu thay đổi URL cũ

### 2.5 Internal Linking
- **Anchor text tự nhiên**:
  - ❌ "Click here"
  - ✅ "Áo thun nam cao cấp"
- **Linking hierarchy**:
  - Trang chủ (Home) → Danh mục (Category) → Sản phẩm (Product)
  - Liên kết từ trang cao hơn → trang thấp hơn
- **Số lượng link**: 3-5 internal link mỗi trang
- **Tránh**:
  - Quá nhiều link (page bloat)
  - Link từ footer không liên quan
  - Anchor text quá khác so với nội dung trang đích
- **Breadcrumb navigation**: Giúp user và bot hiểu cấu trúc

### 2.6 Image Alt Text
- **Quy tắc viết alt text**:
  ```html
  ❌ <img src="image.jpg" alt="image">
  ✅ <img src="image.jpg" alt="Áo thun nam cotton trắng form rộng khoáng">
  ```
- **Bao gồm**: Mô tả sản phẩm + từ khóa nếu thích hợp
- **Độ dài**: 5-10 từ, không quá dài
- **Lợi ích**:
  - SEO image search
  - Accessibility (người khiếm thị dùng screen reader)
  - Page speed (browser biết size ảnh trước khi load)
- **Image file name**: Sử dụng descriptive names
  - ❌ image123.jpg
  - ✅ ao-thun-nam-cotton-trang.jpg

## 3. TỐI ƯU TRANG SẢN PHẨM (Product Page SEO)

### 3.1 Product Schema Markup
```json
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "Áo Thun Nam Cotton Cao Cấp",
  "image": "https://example.vn/images/ao-thun.jpg",
  "description": "Áo thun nam 100% cotton, mát mẻ, thấm mồ hôi",
  "brand": {
    "@type": "Brand",
    "name": "Khoáng"
  },
  "offers": {
    "@type": "Offer",
    "price": "99000",
    "priceCurrency": "VND",
    "availability": "https://schema.org/InStock",
    "url": "https://example.vn/ao-thun-nam-cotton"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "128"
  }
}
```

### 3.2 Review & Rating Schema
```json
{
  "@type": "Review",
  "reviewRating": {
    "@type": "Rating",
    "ratingValue": "5",
    "bestRating": "5"
  },
  "author": {
    "@type": "Person",
    "name": "Nguyễn Văn A"
  },
  "reviewBody": "Chất lượng tốt, giá rẻ, giao hàng nhanh!",
  "datePublished": "2026-04-01"
}
```
- **Hiển thị review ngay trong kết quả Google** (Rich snippet)
- **Tối thiểu 5 review** để hiển thị rating
- **Cập nhật định kỳ**: Xóa review giả, chỉ giữ review thực từ khách

### 3.3 FAQ Schema
```json
{
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Áo thun này có thích hợp cho mùa hè không?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Có, áo thun 100% cotton rất thích hợp cho mùa hè, thấm mồ hôi tốt"
      }
    }
  ]
}
```
- **Bao gồm 5-10 câu hỏi phổ biến** về sản phẩm
- **Giúp SEO**: Hiển thị Q&A snippet trên Google
- **Cải thiện CTR**: Rich snippet cao hơn plain text

### 3.4 Breadcrumb Schema
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Trang Chủ",
      "item": "https://example.vn"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Áo Nam",
      "item": "https://example.vn/ao-nam"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Áo Thun",
      "item": "https://example.vn/ao-nam/ao-thun"
    }
  ]
}
```

### 3.5 Product Page Content Best Practices
- **Mô tả sản phẩm chi tiết**: 300-500 từ
  - Tính năng + Lợi ích
  - Chất liệu, size, màu sắc có sẵn
  - So sánh với sản phẩm tương tự
- **Heading H1**: Tên sản phẩm + tính năng chính
- **Bảng size**: Dễ dàng, bao gồm chiều cao + cân nặng tương ứng
- **Hình ảnh chất lượng cao**: Tối thiểu 5-10 ảnh từ các góc độ khác nhau
- **Video sản phẩm**: Giúp giảm bounce rate, tăng conversion
- **Trust signals**:
  - Chứng chỉ, giải thưởng
  - Số năm kinh doanh
  - Số lượng khách hàng
- **CTA rõ ràng**: "Thêm vào giỏ", "Mua ngay", "Liên hệ tư vấn"

## 4. TỐI ƯU TRANG DANH MỤC (Category Page SEO)

### 4.1 Category Page Structure
- **H1**: Tên danh mục + từ khóa chính
  - ❌ "Áo Nam"
  - ✅ "Áo Nam - Thời Trang Nam Cao Cấp Giá Rẻ"
- **Meta Description**: Bao gồm số sản phẩm, USP
  - "Khám phá 500+ mẫu áo nam cao cấp giá rẻ. Chất liệu tốt, thiết kế hiện đại. Giao hàng miễn phí. Mua ngay!"
- **Category description**: 150-300 từ, bao gồm:
  - Tổng quan về danh mục
  - Các loại sản phẩm trong danh mục
  - Tính năng, lợi ích
  - Brand/nhà cung cấp
- **Filters tối ưu**: Giá, Kích cỡ, Màu sắc, Brand
  - Đảm bảo URL khác nhau cho mỗi filter
  - Dùng parameter hoặc slug structure

### 4.2 Internal Linking trên Category Page
- **Link từ category đến product**: Các sản phẩm nổi bật
- **Link từ category đến blog posts**: Hướng dẫn chọn size, styling tips
- **Pagination**: SEO-friendly pagination
  - ❌ rel="next/prev" (lỗi thời)
  - ✅ Mỗi trang có URL duy nhất, internal link đến trang khác

### 4.3 Faceted Navigation
- **Vấn đề**: Quá nhiều URL trùng lặp khi dùng filter
- **Giải pháp**:
  - Dùng canonical tag để chỉ định trang chính
  - Dùng robots meta tag để prevent indexing (nếu cần)
  - Hoặc dùng parameter handling trong GSC

## 5. SEO CHO CÁC SÀN TMĐT

### 5.1 Shopee SEO Optimization
- **Tối ưu tiêu đề danh sách (Listing Title)**:
  - Độ dài: 80-120 ký tự (full hiển thị trên mobile)
  - Công thức: [Loại sản phẩm] [Tính năng] [Brand/Model] [Khuyến mãi]
  - Ví dụ: "Áo Thun Nam Cotton Cao Cấp Mưa Hàng Hiệu - Mát Mẻ Thấm Mồ Hôi - Giảm 30%"
  - Đặt từ khóa quan trọng ở đầu
- **Hashtag Shopee**: 3-5 hashtag thích hợp
  - Dùng hashtag trending, phổ biến
  - Liên quan trực tiếp đến sản phẩm
  - Ví dụ: #áothunngoại #thạichất #giảmgiá #shopeemallforus
- **Mô tả sản phẩm chi tiết**:
  - 500+ ký tự, bao gồm: Mô tả, Tính năng, Hướng dẫn chọn size, Bảo hành/Đổi trả
  - Sử dụng bullet points, dễ scan
- **Ảnh sản phẩm**:
  - Tối thiểu 10 ảnh, tối đa 20 ảnh
  - Ảnh đầu tiên là ảnh sản phẩm rõ nhất, không logo/watermark
  - Kích thước: 1024x1024px hoặc lớn hơn
  - Bao gồm các góc độ: trước, sau, cạnh, chi tiết
- **Video sản phẩm**: Tăng CTR đáng kể, Shopee ưu tiên video
- **Giá cạnh tranh**: Sử dụng Shopee Analytics để biết giá trung bình
- **Rating & Review**:
  - Khuyến khích khách hàng để review (coupon/discount)
  - Trả lời comment/review nhanh chóng
  - Xử lý review âm tính, giải quyết khiếu nại

### 5.2 Lazada SEO Optimization
- **Tối ưu Product Title**:
  - Độ dài: < 120 ký tự
  - Công thức: [Danh mục] [Brand] [Mô tả chính] [Tính năng nổi bật]
  - Ví dụ: "Áo Thun Nam Cotton - Mưa Hàng Hiệu - Mát Mẻ Thấm Mồ Hôi - 100% Cotton"
  - Từ khóa ở đầu, tự nhiên, không keyword stuffing
- **Loại sản phẩm (Category)**: Chọn đúng loại, Lazada sẽ gợi ý các thuộc tính
- **Attributes cần thiết**:
  - Size/Kích thước
  - Màu sắc
  - Brand
  - Chất liệu
  - Độ bền
  - Dòng sản phẩm
- **Mô tả sản phẩm**:
  - Ít nhất 200 từ
  - Bao gồm: Điểm bán, Thông số kỹ thuật, Hướng dẫn sử dụng, Chính sách đổi trả
  - Dễ đọc, không chữ quá nhỏ, không màu chữ lạ
- **Hình ảnh**:
  - Ít nhất 9 ảnh (Lazada hiển thị 9 ảnh đầu tiên)
  - Nên 15-20 ảnh để cover tất cả angle/màu/size
  - Ảnh chất lượng cao, kích thước lớn
- **Giá & Khuyến mãi**:
  - Đặt giá cạnh tranh so với competitor
  - Dùng flash sale, voucher để tăng bán hàng
  - Lazada ưu tiên list có khuyến mãi trong search
- **Delivery & Seller Performance**:
  - Giao hàng nhanh, gói gọn gàng
  - Tỉ lệ hủy đơn thấp
  - Tỉ lệ return thấp
  - Response time nhanh

### 5.3 TikTok Shop SEO Optimization
- **Product Title**:
  - Độ dài: 20-60 ký tự
  - Ngắn gọn, catchy, dễ nhớ
  - Ví dụ: "Áo Thun Nam Cotton Cao Cấp - Hot Trend"
- **Hashtag TikTok**:
  - 5-10 hashtag phổ biến
  - Mix: Broad (100M+ views) + Niche (1-10M views) + Micro (< 1M)
  - Ví dụ: #áothun #thátrang #shopping #Vietnam
- **Video product showcasing**:
  - Tạo video 15-60 giây showcase sản phẩm
  - Dùng trending sounds, effects
  - Highlighting: Chất liệu, Fitting, Styling ideas
- **Product image**:
  - Ảnh sắc nét, có người mặc thử (nếu quần áo)
  - Lifestyle image (không chỉ flat lay)
- **Description**:
  - Bao gồm CTA (Like, Comment, Buy)
  - Nêu bật main features
  - Giá cạnh tranh, promo
  - Link shop/store dễ tìm

## 6. CHIẾN LƯỢC CONTENT SEO

### 6.1 Blog SEO Strategy
- **Blog content mapping**: Mỗi blog post target một nhóm từ khóa specific
  - Ví dụ: Blog "Cách chọn áo thun nam" → Long-tail keywords
- **Blog post structure**:
  - Title: 50-60 ký tự, có từ khóa
  - Meta description: 155-160 ký tự
  - Intro: 150-200 từ, trả lời câu hỏi user
  - H2-H3: Chia nhỏ nội dung, dễ scan
  - 2000+ từ: Target organic traffic cao
  - Conclusion + Internal links: Link đến product/category pages
- **Content pillar strategy**:
  - 1 pillar content dài (3000-5000 từ) về 1 topic chính
  - 10+ cluster content (1500-2000 từ) xoay quanh pillar
  - Link từ cluster → pillar (topical authority)
- **Keyword distribution**:
  - Primary keyword: H1 + intro + 1-2 lần trong content
  - Secondary keywords: H2-H3 + 2-3 lần trong content
  - LSI keywords: Từ liên quan (Google tự suggest)

### 6.2 FAQ Page SEO
- **Page structure**:
  - H1: "Câu Hỏi Thường Gặp Về [Sản Phẩm/Danh Mục]"
  - FAQ schema markup (JSON-LD)
  - 10-15 Q&A pairs
  - Internal links trong mỗi answer
- **FAQ content**:
  - Trả lời từ user intent (Google Search Console data)
  - Q&A phải cung cấp giá trị
  - Tự nhiên, không spam
  - Bao gồm: Size, Giá, Shipping, Return, Warranty...

### 6.3 Buying Guide SEO
- **Ví dụ**: "Hướng Dẫn Chọn Áo Thun Nam Phù Hợp"
- **Content**:
  - Tính năng quan trọng (Chất liệu, Fit, Brand)
  - Hướng dẫn size + bảng size detail
  - So sánh sản phẩm
  - Giá trị so sánh (VFM - Value for Money)
  - Gợi ý theo use case
- **Internal links**: Link đến sản phẩm cụ thể recommend

## 7. LOCAL SEO CHO TMĐT CÓ CỬA HÀNG OFFLINE

### 7.1 Google Business Profile
- **Tạo/xác nhận GBP**: https://business.google.com
- **Thông tin cần thiết**:
  - Tên cửa hàng, địa chỉ, số điện thoại
  - Giờ mở cửa, ngày nghỉ, ngày đặc biệt
  - Website, email
  - Loại cửa hàng (Retail)
- **Chuẩn hóa tên cửa hàng**: Giống nhau trên tất cả platform
- **Danh mục chính + phụ**: Ví dụ: Cửa hàng bán quần áo, Cửa hàng thợ may
- **Mô tả cửa hàng**: 750 ký tự, bao gồm: History, Specialties, Why visit
- **Hình ảnh**:
  - Logo cửa hàng
  - Ảnh bên ngoài cửa hàng
  - Ảnh bên trong cửa hàng
  - Ảnh sản phẩm (trong cửa hàng)
  - Ảnh team staff

### 7.2 Local Citation (NAP Consistency)
- **NAP = Name, Address, Phone**
- **Chuẩn hóa trên các platform**:
  - Google Business Profile
  - Yelp, Tripadvisor
  - Local directory (Vàng Pages, Loc Vietnam)
  - Website (footer, contact page)
  - Social media (Facebook, Instagram)
- **Format địa chỉ nhất quán**:
  - ✅ 123 Đường Nguyễn Huệ, Quận 1, TP.HCM, 700000
  - ❌ 123 Nguyen Hue, District 1, HCM City

### 7.3 Local Keywords
- **Target**: "[Sản phẩm] + [Vị trí]"
  - Ví dụ: "Cửa hàng áo thun nam Hà Nội", "Áo cotton cao cấp TP.HCM"
- **On-page**: Thêm vị trí vào title, H1, content
- **Schema markup**: LocalBusiness schema + Address schema
- **Reviews**: Terimakasih, tanggapi semua review (baik/xấu)

### 7.4 Local Link Building
- **Join local directory**: Vàng Pages Vietnam, Loc Vietnam, Foody
- **Local partnership**: Link từ các trang liên quan địa phương
- **Sponsorship**: Sponsor sự kiện local, tiệc từ thiện
- **Local press**: PR với báo địa phương, magazine

## 8. LINK BUILDING STRATEGIES CHO TMĐT VIỆT NAM

### 8.1 Guest Post
- **Tìm target blogs**:
  - Industry blogs: Blog về fashion, retail, ecommerce
  - Authority domains: DA > 30, Traffic > 10k/tháng
  - Relevance: Cùng industry, audience similar
  - Công cụ: Ahrefs, SEMrush, Moz (kiểm tra DA)
- **Outreach**:
  - Viết pitch email cá nhân
  - Gợi ý 3-5 chủ đề blog bạn có thể viết
  - Bao gồm: Chủ đề, outline, USP
  - Follow-up 1-2 tuần nếu không reply
- **Guest post content**:
  - 1500-2500 từ, chất lượng cao
  - 1-2 internal link về website của bạn
  - Author bio: Tên, công ty, link website
  - Relevant keywords trong content

### 8.2 Broken Link Building
- **Quy trình**:
  1. Tìm broken link trên relevant website (công cụ: Ahrefs, SEMrush)
  2. Tạo content similar + better hơn trang gốc
  3. Liên hệ webmaster: Gợi ý link của bạn thay thế
- **Ví dụ**:
  - Tìm: "Hướng dẫn chọn áo thun" (broken)
  - Tạo: "Hướng dẫn chọn áo thun nam 2026 - Complete Guide"
  - Pitch: "Mình thấy link này broken, tôi có content tương tự, nếu có thể..."

### 8.3 PR & Press Release
- **Nội dung PR phù hợp**:
  - Product launch baru
  - Kemitraan strategis
  - Pencapaian milestone (1 juta customer, memperluas warehouse)
  - CSR initiative
  - Award/recognition
- **Distribution**:
  - PR agency Vietnam
  - Online PR platform (PRlog, press-release.vn)
  - Media relationship: Báo online, Tạp chí
- **Link từ PR**: Báo, magazine mention brand + link

### 8.4 Forum & Community Engagement
- **Join relevant forum/community**:
  - Reddit (r/Vietnam, r/EastAsiaEconomics)
  - Quora Vietnam
  - Facebook groups (tuy FB link nofollow, nhưng authority increase)
  - VietNamNet forum, Diễn Đàn Việt
- **Cách tiếp cận**:
  - Đúc kết kinh nghiệm, share valuable insight
  - Trả lời câu hỏi user
  - Link website chỉ khi thực sự relevant
  - Tránh spam, self-promotion quá

### 8.5 Social Signals
- **Facebook**:
  - Share content, engage audience
  - FB post không phải dofollow link, nhưng indirect ranking factor
  - Tăng brand awareness, traffic
- **TikTok/Instagram**:
  - Video content viral
  - Link trong bio (Instagram link)
  - TikTok shop integration
- **YouTube**:
  - Video product review, tutorial
  - Dofollow link từ description
  - Playlist, series untuk more watch time

## 9. CORE WEB VITALS OPTIMIZATION

### 9.1 LCP (Largest Contentful Paint) - Mục tiêu < 2.5s
- **Largest element**: Hero image, video, text block lớn
- **Optimize**:
  - **Lazy load non-critical images**: Chỉ load hình visible
  - **Nén hình ảnh**: Dùng WebP, TinyPNG
  - **Remove render-blocking JS/CSS**: Async, defer, critical CSS
  - **Server response time**: Faster hosting, caching
  - **Preload critical resources**:
    ```html
    <link rel="preload" as="image" href="hero.jpg">
    <link rel="preload" as="font" href="font.woff2" type="font/woff2">
    ```

### 9.2 FID (First Input Delay) - Mục tiêu < 100ms
- **Input delay**: Thời gian từ user click → browser response
- **Optimize**:
  - **Reduce main thread work**: Minify JS, remove unused code
  - **Code splitting**: Load JS progressively
  - **Web Workers**: Offload heavy JS từ main thread
  - **Long task optimization**: Break long JS tasks thành smaller chunks
  - **Reduce 3rd party script**: Google Analytics, ads script, chat widget

### 9.3 CLS (Cumulative Layout Shift) - Mục tiêu < 0.1
- **Layout shift**: Unexpected movement của content (ảnh load chậm, font swap, ads inject)
- **Optimize**:
  - **Set size container**: Hình ảnh + video định kích thước trước
    ```html
    <img src="..." width="400" height="300">
    <video width="400" height="225"></video>
    ```
  - **Avoid injecting content top of page**: Ad, banner không inject vào top
  - **Font-display: swap**: Font fallback tránh FOIT (Flash of Invisible Text)
  - **Avoid animations trigger reflow**: Dùng transform + opacity thay vì margin/padding
  - **Lazy load content**: Load ads, recommender chỉ khi visible

### 9.4 Web Vitals Testing
- **Google PageSpeed Insights**: https://pagespeed.web.dev
- **Google Search Console**: Insights > Core Web Vitals (real user data)
- **Web Vitals extension**: Chrome extension realtime monitoring
- **Lighthouse**: Built-in Chrome DevTools

## 10. SEO AUDIT TEMPLATE CHI TIẾT (50+ CHECKPOINTS)

### 10.1 Technical SEO (15 checkpoints)
- [ ] HTTPS enabled, HTTP redirect to HTTPS
- [ ] Sitemap.xml created & submitted GSC
- [ ] Robots.txt properly configured
- [ ] Mobile-friendly (Google Mobile Test: PASS)
- [ ] Viewport meta tag present
- [ ] Canonical tags correct (no self-pointing wrong canonicals)
- [ ] Hreflang tags for multi-language (if applicable)
- [ ] 404 pages handled gracefully
- [ ] No broken links (0-5 acceptable)
- [ ] Redirect chains < 2 hops
- [ ] No mixed content warnings
- [ ] Schema markup implemented (Organization, Product, Review)
- [ ] Structured data valid (0 errors)
- [ ] Robots.txt not blocking resources
- [ ] Server response time < 600ms

### 10.2 On-Page SEO (12 checkpoints)
- [ ] H1 tag present, contains primary keyword
- [ ] Title tag 50-60 characters, unique
- [ ] Meta description 155-160 characters, unique
- [ ] Primary keyword in first 100 words
- [ ] Natural keyword distribution (LSI keywords)
- [ ] Internal links (3-5 per page)
- [ ] Image alt text descriptive
- [ ] Heading hierarchy correct (H1 → H2 → H3)
- [ ] URL structure clean, descriptive
- [ ] No duplicate content (manual check)
- [ ] Content length adequate (300+ words minimum)
- [ ] Readability score (Flesch Reading Ease > 60)

### 10.3 Mobile & Speed (10 checkpoints)
- [ ] Mobile responsive design
- [ ] PageSpeed Insights Mobile score > 90
- [ ] LCP < 2.5 seconds
- [ ] FID < 100ms
- [ ] CLS < 0.1
- [ ] Images optimized & lazy-loaded
- [ ] CSS minified & unused CSS removed
- [ ] JS minified & code-split
- [ ] Caching strategy implemented (Browser, Server)
- [ ] CDN enabled

### 10.4 Content Quality (8 checkpoints)
- [ ] Content is original, not plagiarized (copy.ai, Turnitin)
- [ ] Content provides value, answers user intent
- [ ] Grammar & spelling correct
- [ ] Content updated recently (< 6 months)
- [ ] E-E-A-T signals present (Expertise, Authority, Trust)
- [ ] External links to authoritative sources
- [ ] Table of contents for long-form content (> 3000 words)
- [ ] Multimedia (video, infographic) included

### 10.5 User Experience (10 checkpoints)
- [ ] Navigation logical, easy to find
- [ ] Search functionality working
- [ ] Product filters functional
- [ ] Breadcrumb navigation present
- [ ] Footer links organized
- [ ] Call-to-action buttons prominent
- [ ] Trust signals visible (reviews, testimonials, security badges)
- [ ] Contact information easy to find
- [ ] No intrusive interstitials/pop-ups
- [ ] Font size readable (minimum 16px on mobile)

### 10.6 Conversion & Ecommerce (8 checkpoints)
- [ ] Product pages have clear pricing
- [ ] Add-to-cart button visible above the fold
- [ ] Product images high-quality, multiple angles
- [ ] Product reviews/ratings visible
- [ ] Shipping info clearly stated
- [ ] Return policy visible
- [ ] Checkout process minimal steps (< 5 steps)
- [ ] Trust badges (SSL, payment methods, return guarantee)

### 10.7 Security (5 checkpoints)
- [ ] SSL certificate valid (no warnings)
- [ ] Security headers implemented (CSP, X-Frame-Options)
- [ ] No malware detected (Google Safe Browsing)
- [ ] Password fields have autocomplete disabled
- [ ] PCI-DSS compliance (if handling payments)

### 10.8 Competitors Benchmarking (5 checkpoints)
- [ ] Backlinks: Compare with 3 competitors
- [ ] Content length: Analyze top 3 ranking pages
- [ ] Keyword targeting: Identify gaps
- [ ] Backlink quality: Check competitor sources
- [ ] Unique features: What competitors lack

## 11. GOOGLE SEARCH CONSOLE SETUP & MONITORING

### 11.1 GSC Configuration
- **Tạo tài khoản**:
  1. https://search.google.com/search-console
  2. Add property: URL prefix (https://example.vn) hoặc Domain (example.vn)
  3. Verify ownership: HTML tag, HTML file, DNS record, Google Analytics
- **Submit sitemap**:
  - Left menu: Sitemaps
  - Paste sitemap URL: https://example.vn/sitemap.xml
  - Submit
- **Request indexing**:
  - Inspect URL tool (top)
  - "Request Indexing" nếu URL mới
- **Remove pages**:
  - Inspect URL tool
  - Select "Remove" nếu page outdated, low-quality

### 11.2 GSC Monitoring
- **Performance Report**:
  - Clicks: Số lần user click từ Google
  - Impressions: Số lần URL appear Google SERP
  - CTR: Click-through rate (Mục tiêu: > 3-5%)
  - Position: Ranking trung bình (Mục tiêu: Top 3)
- **Query Filter**:
  - Sort by clicks, impressions, CTR
  - Identify high-impression-low-click keywords: Improve title/description
  - Identify ranking 4-10 keywords: Optimize content, earn more backlinks
- **Pages Report**:
  - Identify pages with most impressions/clicks
  - Pages < 2% CTR: Optimize title/description
  - Pages with errors: Fix technical issues

### 11.3 Coverage Report
- **Đánh giá** tình trạng indexing:
  - Valid: Pages được index
  - Excluded: Pages Google bỏ qua (intentional)
  - Error: Pages có vấn đề (4xx, 5xx, robots blocked)
  - Valid (with warning): Pages indexed nhưng có issue
- **Loại exclude phổ biến**:
  - Blocked by noindex
  - Blocked by robots.txt
  - Noindex search parameter
  - Duplicate (canonical to different domain)
  - Duplicate (submitted as canonical)
- **Fix**:
  - Remove robots.txt block nếu cần index
  - Add canonical tags correct
  - Fix server errors

### 11.4 Enhancements Report
- **Monitoring rich results**: Product, Review, FAQ, BreadcrumbList
- **Cải thiện**: Structured data errors
- **Excluded items**: Schema markup present nhưng không generate snippet (fix errors)

### 11.5 Link Report
- **Top linking sites**: Websites linking tới bạn
- **Top linked pages**: Trang của bạn được link nhiều nhất
- **Link text**: Anchor text most common
- **Action**:
  - Identify high-authority backlinks
  - Monitor new/lost links
  - Disavow spammy links (if domain is spammed)

## 12. COMMON SEO MISTAKES CHO WEBSITE VIỆT NAM

### 12.1 Technical Mistakes
- ❌ **Mixed HTTP/HTTPS**: Một số resource HTTPS, một số HTTP
- ❌ **No mobile optimization**: Website không responsive
- ❌ **Slow loading**: > 3 giây, không optimize Core Web Vitals
- ❌ **Broken internal links**: Linking đến 404 pages
- ❌ **Duplicate content**: Cùng content trên nhiều URL
- ❌ **Poor mobile UX**: Button quá nhỏ, font quá nhỏ
- ✅ **Fix**: Audit regularly, monitor GSC, use PageSpeed Insights

### 12.2 On-Page Mistakes
- ❌ **Thin content**: < 300 từ, không giá trị
- ❌ **Keyword stuffing**: Lặp từ khóa quá nhiều lần
- ❌ **Missing meta tags**: Không có title/description
- ❌ **No internal links**: Isolate pages (orphaned)
- ❌ **Poor heading structure**: H1 nhiều, jumps H1→H4
- ❌ **Ads blocking content**: Interstitials che content chính
- ✅ **Fix**: Content planning, natural keyword placement, proper structure

### 12.3 Content Mistakes
- ❌ **Duplicate content across categories**: Mô tả sản phẩm giống hệt
- ❌ **No unique value**: Copy nội dung từ supplier description
- ❌ **Outdated content**: Blog post 2020 không update
- ❌ **Low expertise/authority**: Không showcase expertise, no author bio
- ❌ **Plagiarism**: Copy từ competitor direct
- ✅ **Fix**: Original content, regular updates, E-E-A-T signals

### 12.4 Link Building Mistakes
- ❌ **Paid links from low-quality sites**: Spam sites, PBN (Private Blog Networks)
- ❌ **Unnatural anchor text**: 100% exact match keywords
- ❌ **Too many links in short time**: Sudden spike = Google penalty
- ❌ **Ignoring relevance**: Links từ completely unrelated sites
- ❌ **No link diversity**: Tất cả từ comment, forum (low-quality)
- ✅ **Fix**: Natural link building (guest posts, PR, partnerships), diverse sources

### 12.5 E-commerce Mistakes
- ❌ **Thin product descriptions**: < 100 từ, just copy supplier text
- ❌ **No product schema**: Google không hiểu product, price, rating
- ❌ **Poor product images**: 1 ảnh, chất lượng thấp
- ❌ **No customer reviews**: Lack social proof, low conversion
- ❌ **Unfriendly filters**: Create thousands of URL variations (duplicate content)
- ❌ **No FAQ**: Not addressing customer concerns
- ✅ **Fix**: Unique descriptions, schema markup, high-quality images, encourage reviews

## 13. MONTHLY SEO REPORTING TEMPLATE

### 13.1 Performance Metrics
| Metric | This Month | Last Month | Change | Target |
|--------|-----------|-----------|--------|--------|
| Organic Traffic | 5,432 | 4,890 | +11% | 6,500 |
| Keyword Rankings | 287 | 256 | +12% | 350 |
| Top 3 Rankings | 45 | 38 | +18% | 60 |
| Top 10 Rankings | 120 | 108 | +11% | 150 |
| Backlinks | 156 | 145 | +8% | 200 |
| Referring Domains | 42 | 40 | +5% | 50 |

### 13.2 Top Performers
- **Top 5 Pages by Traffic**
- **Top 10 Keywords by Clicks**
- **Top Backlinks (by traffic)**
- **Best Performing Content (> 1000 sessions)**

### 13.3 Areas for Improvement
- **Keywords ranking 4-10**: Opportunity to improve to top 3
- **Low CTR keywords (< 2%)**: Improve title/description
- **Pages with errors**: GSC coverage report
- **Broken links**: Monitor & fix
- **Competitors gaining ground**: Analyze their strategy

### 13.4 Content Audit
- **New content created**: 2 blog posts, 1 buying guide
- **Content updated**: 5 product pages, 1 category page
- **Content removed**: None
- **Content performance**: Blog post X: 1,245 sessions, 3.5 avg position

### 13.5 Link Building Activities
- **New backlinks**: 8 (4 guest posts, 2 PR mentions, 2 directory listings)
- **Lost backlinks**: 0
- **Top new backlinks**:
  - Website A (DA 45): Guest post topic "..."
  - Website B (DA 38): PR mention

### 13.6 Technical SEO
- **Core Web Vitals**: LCP 2.1s (✅), FID 95ms (✅), CLS 0.08 (✅)
- **Crawl errors**: 0
- **Index coverage**: 98%
- **Mobile usability issues**: 0
- **Security issues**: None

### 13.7 Recommendations
1. **Priority 1**: [Issue] → [Expected impact] → [Timeline]
2. **Priority 2**: [Issue] → [Expected impact] → [Timeline]
3. **Priority 3**: [Issue] → [Expected impact] → [Timeline]

### 13.8 Next Month Goals
- Increase organic traffic to 6,500 sessions (+20% from baseline)
- Rank 10+ keywords in top 3 (+25%)
- Acquire 10+ quality backlinks
- Update 3 underperforming content pages
- Launch 2 new blog posts targeting long-tail keywords

---

**Document Version**: 2026.04.03
**Last Updated**: 2026-04-03
**Author**: SEO Team
**Confidentiality**: Internal Use Only
