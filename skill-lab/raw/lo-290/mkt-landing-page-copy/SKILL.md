---
name: mkt-landing-page-copy
description: |
  Viết copy landing page conversion-focused cho sản phẩm/dịch vụ/khóa học Việt Nam. Tự động sinh đủ 8 section (hero, problem, solution, social proof, feature, FAQ, CTA, footer) theo framework PAS/AIDA. Kích hoạt khi người dùng nói: "viết landing page", "copy landing", "viết LP bán hàng", "viết trang đích", "landing page bán khóa học", "copy chuyển đổi cao", "viết content LP", "viết sales page". Output là HTML preview + Markdown copy.
---

# Viết Copy Landing Page Conversion

## Mục Tiêu
Sinh đầy đủ 8 section copy landing page trong 20 phút, có CTA rõ, social proof, ngôn ngữ chạm pain point khách hàng VN, đạt conversion 5-15% (cao hơn trung bình ngành).

## Khi Nào Dùng
- Ra mắt sản phẩm/khóa học mới
- Chạy chiến dịch ads cần LP riêng
- Redesign LP cũ đang tệ (<2% CR)
- A/B test variant
- Cần copy cho funnel cold/warm/hot

## Bước 1: Brief Sản Phẩm
Hỏi:
1. Sản phẩm + giá + USP
2. Khách hàng mục tiêu + pain point chính
3. Đối thủ chính + cách họ pitch
4. 3 lợi ích lớn nhất
5. Social proof có sẵn (số KH, review, logo, KOL)
6. Offer/bonus + deadline
7. Mục tiêu chính LP (đăng ký/mua/tư vấn)

## Bước 2: Chọn Framework
- PAS (Problem-Agitate-Solution): sản phẩm giải pain rõ ràng
- AIDA: sản phẩm cần educate
- BAB (Before-After-Bridge): khóa học, dịch vụ chuyển hóa
- 4U headline (Useful, Urgent, Unique, Ultra-specific)

## Bước 3: Viết 8 Section
1. **Hero**: H1 4U + sub-headline 15-20 từ + CTA primary + ảnh/video
2. **Problem**: 3 pain point + emoji + minh họa
3. **Solution**: giới thiệu sản phẩm + cách hoạt động 3 bước
4. **Feature/Benefit**: 6-9 box (icon + tiêu đề + 2 dòng mô tả)
5. **Social Proof**: số liệu lớn + 5-8 testimonial + logo KH + screenshot review
6. **Offer**: gói giá + bonus + đảm bảo hoàn tiền + countdown
7. **FAQ**: 8-10 câu xử lý objection (giá, thời gian, hiệu quả, hoàn tiền)
8. **CTA cuối + Footer**: tái khẳng định lợi ích + CTA + ảnh founder/team

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tra giá đối thủ, testimonial market
- WebFetch: lấy copy LP đối thủ làm tham khảo
- Google Drive MCP: lưu file HTML + Markdown
- Notion MCP: lưu vào database "LP Copy Library"
- Figma MCP (nếu có): đẩy text vào file thiết kế

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Sinh preview HTML từ Markdown
import markdown, jinja2
tmpl = open('lp_template.html').read()
html = jinja2.Template(tmpl).render(
  hero_h1=hero, sections=sections_md, cta=cta_text)
open('outputs/lp_preview.html','w').write(html)
```

## Bước 5: Output Format
- File `.md` chứa copy text theo section (cho dev paste vào CMS)
- File `.html` preview render đẹp để demo cho sếp/khách
- File `.docx` cho khách review
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ 8 section
- [ ] Hero CTA "above the fold"
- [ ] Mỗi feature có benefit-led copy (không kỹ thuật)
- [ ] Có >=5 testimonial cụ thể
- [ ] FAQ xử lý đủ 5 objection lớn
- [ ] CTA xuất hiện tối thiểu 4 lần
- [ ] Có scarcity/urgency hợp lý
