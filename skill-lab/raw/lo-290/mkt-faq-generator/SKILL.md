---
name: mkt-faq-generator
description: |
  Sinh FAQ 15-20 câu cho landing page/product page Việt Nam, xử lý đủ objection mua hàng + có schema FAQ JSON-LD ready cho SEO. Kích hoạt khi người dùng nói: "tạo FAQ", "viết FAQ landing", "FAQ sản phẩm", "FAQ schema", "generate FAQ", "objection FAQ", "FAQ generator", "FAQ section LP". Output là Markdown + JSON-LD schema.
---

# Sinh FAQ Landing/Product 15-20 Câu

## Mục Tiêu
LP nào cũng có FAQ chuẩn xử lý objection + SEO rich snippet, tăng CR 10-25% và mở rộng SERP visibility.

## Khi Nào Dùng
- Build LP mới
- Audit LP cũ không có FAQ
- SP/dịch vụ phức tạp cần educate
- Khóa học / SaaS có giá cao
- Tăng SEO rich result

## Bước 1: Brief Sản Phẩm
Hỏi:
1. Sản phẩm/dịch vụ + giá
2. KH target
3. 3 objection lớn nhất hiện tại (từ sales/CS)
4. Sự kiện đặc biệt (sale, hoàn tiền, bảo hành)
5. Domain landing page

## Bước 2: Mapping 6 Nhóm FAQ
Mỗi LP nên có FAQ phủ:
1. **Giá & thanh toán** (3-4 câu): trả góp, voucher, payment options
2. **Sản phẩm/dịch vụ** (3-4 câu): tính năng, phù hợp ai, khác đối thủ
3. **Giao hàng/triển khai** (2-3 câu): thời gian, phí, khu vực
4. **Bảo hành/đổi trả** (2-3 câu): chính sách, quy trình
5. **Hỗ trợ** (2-3 câu): kênh CS, giờ làm, sau bán
6. **Trust/Uy tín** (2-3 câu): công ty là ai, KH nào dùng, giải thưởng

Tổng 15-20 câu.

## Bước 3: Viết Câu Hỏi + Trả Lời
Quy tắc:
- Câu hỏi viết như KH thực sự hỏi (ngữ tự nhiên)
- Trả lời 50-100 từ, có data cụ thể
- Có CTA nhẹ cuối câu trả lời quan trọng
- Avoid "thường tùy theo" mơ hồ

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tra "People also ask" Google cho topic
- WebFetch: lấy FAQ đối thủ
- CRM/Helpdesk MCP: lấy câu hỏi thực từ CS ticket
- Sheets MCP: lưu FAQ master
- Notion MCP: archive

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Sinh JSON-LD FAQ schema ready chèn vào LP
import json
def gen_faq_schema(faqs):
    schema = {'@context':'https://schema.org','@type':'FAQPage',
      'mainEntity':[]}
    for q, a in faqs:
        schema['mainEntity'].append({
          '@type':'Question','name':q,
          'acceptedAnswer':{'@type':'Answer','text':a}})
    return json.dumps(schema, ensure_ascii=False, indent=2)
```

## Bước 5: Output Format
- File `.md` 15-20 FAQ chia 6 nhóm
- File `.json` FAQ schema JSON-LD chèn vào `<head>`
- HTML accordion snippet ready paste
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 15-20 câu chia 6 nhóm
- [ ] Câu hỏi ngữ tự nhiên KH
- [ ] Trả lời cụ thể, không mơ hồ
- [ ] Có schema JSON-LD
- [ ] HTML accordion sẵn
- [ ] Đã test rich result preview
