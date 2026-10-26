---
name: mkt-abandoned-cart-email
description: |
  Chuỗi 3 email cứu giỏ hàng bỏ cho ecom Việt Nam (Shopify/Sapo/Haravan) — recover 10-15% đơn bỏ. Subject + body + CTA chuẩn pattern đã chứng minh. Kích hoạt khi người dùng nói: "email cứu giỏ hàng", "abandoned cart email", "giỏ hàng bỏ", "abandoned cart sequence", "khôi phục giỏ hàng", "cart recovery", "email reminder giỏ hàng", "Shopify cart recovery". Output là Markdown + HTML template.
---

# Email Cứu Giỏ Hàng Bỏ (3 Email)

## Mục Tiêu
Mỗi tháng cứu thêm 10-15% đơn hàng abandon (đang chiếm 60-80% traffic ecom), tăng doanh thu mà không tốn ads spend.

## Khi Nào Dùng
- Ecom có tracking abandon cart
- Có hệ thống email automation
- Cart abandon rate >50%
- KH dùng email/Zalo/SMS để verify
- Setup lần đầu hoặc audit chuỗi cũ

## Bước 1: Brief Ecom
Hỏi:
1. Platform (Shopify/Sapo/Haravan/WooCommerce)
2. AOV trung bình
3. Sản phẩm chính (giá rẻ/cao)
4. Margin để cho discount
5. Số cart abandon/ngày
6. Đã có chuỗi cũ chưa

## Bước 2: Cấu Trúc 3 Email
**Email 1 (T+1h): Reminder nhẹ**
- Subject: "Quên gì đó rồi sao?" hoặc "Sản phẩm của bạn vẫn đợi"
- Body: ảnh sản phẩm + giá + nút "Hoàn tất đơn"
- Không discount
- Lý do: KH có thể chỉ bận, nhắc nhẹ đủ

**Email 2 (T+24h): Social proof + Q&A**
- Subject: "Khách hàng nói gì về [SP]?"
- Body: 2-3 testimonial + FAQ về shipping/return
- Vẫn không discount
- Lý do: xử lý objection trust

**Email 3 (T+72h): Last call + Discount**
- Subject: "Còn 24h - Giảm 10% cho đơn này"
- Body: voucher code + countdown + sản phẩm gợi ý thêm
- Discount 10-15% (tối thiểu để chuyển đổi)
- Lý do: chốt deal

## Bước 3: Personalization & Edge Case
Personalize:
- Tên KH
- Sản phẩm trong cart (ảnh, tên, giá)
- Tổng tiền
- Free shipping threshold (nếu thiếu X để free ship)

Edge case:
- Hết hàng → đề xuất sản phẩm tương đương
- Đã mua sau → ngắt chuỗi
- Là KH VIP → discount cao hơn

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Shopify/Sapo MCP: trigger cart abandoned
- Klaviyo/Omnisend MCP: flow automation
- Zalo OA MCP: ZNS song song với email
- SMS gateway: bổ sung lúc T+24h
- Sheets MCP: tracker

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Webhook Shopify abandoned checkout
from flask import Flask, request
app = Flask(__name__)
@app.route('/webhook/abandoned', methods=['POST'])
def on_abandoned():
    chk = request.json
    schedule_email(chk['email'], delay='1h', tpl='email1', cart=chk['line_items'])
    schedule_email(chk['email'], delay='24h', tpl='email2')
    schedule_email(chk['email'], delay='72h', tpl='email3',
      discount_code=generate_code(chk['id']))
    return '',200
```

## Bước 5: Output Format
- File `.md` 3 email đầy đủ (3 subject A/B mỗi)
- File `.html` template responsive
- Flow chart automation
- Tracker recovery rate
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 3 email đúng timing 1h/24h/72h
- [ ] Personalization product token
- [ ] Discount chỉ ở email cuối
- [ ] Có Zalo/SMS bổ sung
- [ ] Tracker recovery rate
- [ ] Đã test end-to-end với cart thật
- [ ] Edge case (hết hàng, đã mua) xử lý
