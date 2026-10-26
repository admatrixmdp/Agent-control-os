---
name: mkt-product-description-shopify
description: |
  Viết mô tả sản phẩm cho Shopify/Shopee/Lazada/Tiki/TikTok Shop chuẩn SEO + conversion, tiếng Việt. Hook + feature + benefit + spec + FAQ + CTA. Kích hoạt khi người dùng nói: "viết mô tả sản phẩm", "product description Shopify", "viết description Shopee Lazada", "mô tả sản phẩm SEO", "viết content sản phẩm", "viết bullet sản phẩm", "viết description ecom", "product copy". Output là Markdown copy theo từng template platform.
---

# Mô Tả Sản Phẩm Shopify/Shopee/Lazada/TikTok Shop

## Mục Tiêu
Mỗi SP có mô tả chuẩn cấu trúc, SEO-friendly, CR cao — tăng CR sàn 20-50% so với mô tả copy-paste từ supplier.

## Khi Nào Dùng
- Upload SP mới hàng loạt
- Audit SP cũ đang CR thấp
- Mở rộng sang sàn mới
- Refresh mô tả định kỳ
- Cộng tác viên/agency

## Bước 1: Brief Sản Phẩm
Hỏi:
1. Tên sản phẩm + giá
2. Đối tượng KH chính
3. USP (3 điểm)
4. Spec kỹ thuật
5. Đối thủ sàn (gia tham khảo)
6. Keyword chính SEO
7. Platform đăng (Shopify / Shopee / Lazada / Tiki / TTS)
8. Hình ảnh có sẵn

## Bước 2: Cấu Trúc Mô Tả
**Phần 1 - Hook 50 từ**: vấn đề KH gặp + sản phẩm giải quyết.

**Phần 2 - Tính năng & Lợi ích** (5-7 bullet):
- Feature → Benefit (vd: "Pin 5000mAh → Dùng cả ngày không lo hết")
- Tránh kỹ thuật khó hiểu

**Phần 3 - Thông số kỹ thuật**: bảng đầy đủ (kích thước, trọng lượng, chất liệu, xuất xứ, bảo hành).

**Phần 4 - Cam kết** (USP): bảo hành, đổi trả, giao hàng nhanh.

**Phần 5 - FAQ** (3-5 câu): xử lý objection (giao bao lâu, đổi trả, có hóa đơn không).

**Phần 6 - Cách dùng / Combo**: video unboxing, hướng dẫn.

**Phần 7 - CTA**: "Đặt ngay - Giao 2h trong nội thành"

## Bước 3: Tối Ưu Theo Platform
- **Shopify**: HTML giàu (có heading, ảnh giữa text, video). 800-1500 từ.
- **Shopee**: 300-500 từ, emoji nhiều, line break ngắn, từ khóa đầu title.
- **Lazada**: tương tự Shopee, focus voucher + freeship.
- **Tiki**: tone chuyên nghiệp hơn, đầu tư bảng spec.
- **TikTok Shop**: 200-300 từ, hook viral, CTA mua kèm video clip ngắn.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Shopify/Shopee/Lazada/TikTok Shop API connector: bulk upload
- WebSearch: tra giá đối thủ + review
- WebFetch: lấy spec từ supplier
- Sheets MCP: master SKU + description
- Google Drive MCP: archive

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Bulk update mô tả Shopify
import requests
for product_id, desc in product_descriptions.items():
    r = requests.put(f'https://yourshop.myshopify.com/admin/api/2024-04/products/{product_id}.json',
      headers={'X-Shopify-Access-Token':TOKEN,'Content-Type':'application/json'},
      json={'product':{'id':product_id,'body_html':desc}})
```

## Bước 5: Output Format
- File `.md` mô tả theo từng platform
- File `.xlsx` master SKU + description ready bulk upload
- Hình ảnh được gợi ý chèn
- Title SEO + meta description
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ 7 phần
- [ ] Feature → Benefit rõ
- [ ] SEO keyword trong title + bullet đầu
- [ ] FAQ xử lý objection
- [ ] Tối ưu theo platform
- [ ] Mobile readable (line break ngắn)
- [ ] CTA rõ
