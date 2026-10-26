---
name: mkt-review-acquisition
description: |
  Chiến dịch xin review Google Business / Shopee / Lazada / TikTok Shop sau khi KH nhận hàng. Tự động gửi email/SMS/Zalo cá nhân hóa kèm link review trực tiếp. Kích hoạt khi người dùng nói: "xin review khách", "review acquisition", "tăng review Google", "tăng review Shopee Lazada", "xin đánh giá KH", "chiến dịch lấy review", "kéo review 5 sao", "review marketing". Output là Markdown plan + template message.
---

# Chiến Dịch Xin Review Google/Shopee/Lazada

## Mục Tiêu
Đạt 200+ review 4-5 sao/tháng trên Google Business + sàn TMĐT, tăng CR Google Maps và sàn 20-40%.

## Khi Nào Dùng
- F&B/retail có store vật lý
- Ecom đang đẩy Shopee/Lazada/TikTok Shop
- Doanh nghiệp dịch vụ B2B/B2C
- Sau khi giao hàng / hoàn thành dịch vụ
- Bị review tiêu cực cần đẩy review tích cực

## Bước 1: Brief Channel
Hỏi:
1. Nền tảng review (Google Business / Shopee / Lazada / TikTok Shop / TripAdvisor / Foody)
2. Số đơn/tháng
3. Hệ thống liên hệ KH (Zalo/SMS/email)
4. Incentive (voucher 10k? quà nhỏ?)
5. Mục tiêu rating + số review
6. Bài học từ review tiêu cực hiện tại

## Bước 2: Xây Flow Tự Động
Timing:
- F&B: 1-2h sau dùng món
- Ecom: 3-5 ngày sau nhận hàng (đã dùng thử)
- B2B service: 7-14 ngày sau hoàn thành

3 touchpoint:
1. T+1: Zalo cảm ơn + link review
2. T+3: SMS nhắc nếu chưa review
3. T+7: Email lần cuối + ưu đãi đặc biệt

## Bước 3: Soạn Template Cá Nhân Hóa
**Zalo/SMS** (160 ký tự):
"Cảm ơn anh/chị {ten} đã mua {sp}! Nếu hài lòng, để lại 5* tại {link}. Trừ ngay 30k đơn sau khi đánh giá: {voucher}"

**Email** dài hơn 200-300 từ với:
- Lời cảm ơn cá nhân
- Tóm tắt đơn hàng
- Lý do review giúp brand
- Link 1-click đến review form
- Voucher reward
- P.S. xin feedback cải tiến nếu chưa hài lòng (tránh review tiêu cực public)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Zalo OA MCP: gửi ZNS auto theo trạng thái đơn
- Shopify/Sapo MCP: trigger flow sau "delivered"
- Gmail MCP: email reminder
- Google Business MCP: lấy short URL review
- Sheets MCP: tracker review collected

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tạo link review Google Maps short
import requests
def get_review_link(place_id):
    return f'https://search.google.com/local/writereview?placeid={place_id}'

# Gửi Zalo ZNS qua API ZNS
r = requests.post('https://business.openapi.zalo.me/message/template',
  headers={'access_token':TOKEN},
  json={'phone':customer_phone,'template_id':TPL_ID,
    'template_data':{'name':name,'product':product,'link':link}})
```

## Bước 5: Output Format
- File `.md` campaign plan + flow chart
- Template message 3 phiên bản
- Tracker review collected + rating average
- Quy trình xử lý review tiêu cực
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Flow tự động theo trạng thái đơn
- [ ] Template cá nhân hóa biến
- [ ] Incentive hợp lệ (không bị phạt sàn)
- [ ] Quy trình xử lý 1-3 sao
- [ ] Tracker rating average
- [ ] Đã test end-to-end
