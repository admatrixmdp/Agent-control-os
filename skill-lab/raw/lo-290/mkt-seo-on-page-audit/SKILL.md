---
name: mkt-seo-on-page-audit
description: |
  Audit SEO on-page chi tiết cho website doanh nghiệp bằng cách dùng WebFetch crawl và phân tích title, meta, heading, schema, internal link, tốc độ, mobile-friendly. Tự động chấm điểm 0-100 và xuất danh sách lỗi ưu tiên fix. Kích hoạt khi người dùng nói: "audit SEO on-page", "kiểm tra SEO website", "phân tích SEO", "rà lỗi SEO", "đánh giá SEO trang", "SEO checklist", "audit on-page", "soi SEO website". Output là báo cáo HTML có điểm số và bảng action.
---

# Audit SEO On-page Website

## Mục Tiêu
Trong 15 phút quét toàn bộ trang quan trọng (homepage, category, top 10 blog) và đưa ra danh sách lỗi ưu tiên fix theo impact (cao/trung/thấp), giúp tăng organic traffic 20-40% trong 90 ngày.

## Khi Nào Dùng
- Trước khi triển khai SEO mới
- Tụt hạng đột ngột không rõ lý do
- Sau khi redesign website
- Trước khi migrate sang domain mới
- Kiểm tra định kỳ hàng quý

## Bước 1: Thu Thập URL Cần Audit
Hỏi user: domain chính, 10-20 URL ưu tiên (homepage, top category, top blog). Nếu không có, dùng WebFetch lấy sitemap.xml.

## Bước 2: Crawl Và Trích Xuất Yếu Tố
Với mỗi URL kiểm tra 18 điểm:
- Title (50-60 ký tự, có keyword chính)
- Meta description (140-160 ký tự, có CTA)
- H1 duy nhất chứa keyword
- H2/H3 hợp lý
- URL ngắn, chứa keyword
- Alt text ảnh
- Internal link >= 3
- External link đến nguồn uy tín
- Schema markup
- Canonical
- Open Graph
- Mobile viewport
- HTTPS
- Tốc độ (LCP, CLS)
- Tỷ lệ keyword (1-2%)
- Độ dài bài (>800 từ cho blog)
- Lỗi 404, redirect chain
- Sitemap + robots.txt

## Bước 3: Chấm Điểm Và Phân Loại Lỗi
Mỗi tiêu chí 0/5/10 điểm. Tổng 180 quy về 100. Lỗi xếp 3 mức:
- CRITICAL (đỏ): no H1, no title, no canonical, slow LCP
- HIGH (cam): meta thiếu, alt thiếu, internal link ít
- MEDIUM (vàng): keyword không tối ưu, schema thiếu

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebFetch: crawl từng URL lấy HTML
- WebSearch: kiểm tra URL có index không (`site:domain.com`)
- Google Drive MCP: lưu báo cáo
- Notion MCP: tạo task fix cho dev/content

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Lấy Core Web Vitals từ PageSpeed Insights API
import requests
url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'
r = requests.get(url, params={
  'url':'https://abc.vn','category':'performance','strategy':'mobile',
  'key':'YOUR_API_KEY'
}).json()
lcp = r['lighthouseResult']['audits']['largest-contentful-paint']['displayValue']
cls = r['lighthouseResult']['audits']['cumulative-layout-shift']['displayValue']
```

## Bước 5: Output Format
- File HTML báo cáo `SEO_Audit_<domain>_<date>.html` với:
  - Trang bìa điểm tổng + biểu đồ radar
  - Bảng chi tiết từng URL
  - Top 20 action priority kèm guide fix
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ tối thiểu 10 URL audit
- [ ] Đã chấm điểm 0-100
- [ ] Có ít nhất 20 action item
- [ ] Phân loại theo impact rõ ràng
- [ ] Có hướng dẫn fix kèm theo
- [ ] Báo cáo HTML render đẹp trên mobile
