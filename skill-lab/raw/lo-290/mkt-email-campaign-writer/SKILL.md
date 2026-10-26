---
name: mkt-email-campaign-writer
description: |
  Viết chuỗi email marketing 5-7 email cho campaign nurture/launch/promo của doanh nghiệp Việt Nam. Tự động cấu trúc theo customer journey, có subject line A/B, preview text, body và CTA rõ ràng. Kích hoạt khi người dùng nói: "viết email marketing", "chuỗi email nurture", "email sequence", "viết email campaign", "viết email launch", "viết email promo", "email automation", "viết chuỗi email bán hàng". Output là Markdown + bảng kế hoạch gửi.
---

# Viết Chuỗi Email Marketing 5-7 Email

## Mục Tiêu
Tăng tỷ lệ open >35%, click >5%, conversion >2% cho campaign email bằng cách áp dụng framework đã chứng minh, cá nhân hóa từng email theo customer journey.

## Khi Nào Dùng
- Ra mắt sản phẩm/dịch vụ mới
- Nurture lead từ form đăng ký tải tài liệu
- Re-engage khách hàng ngủ đông 90+ ngày
- Promo Black Friday / sale tháng
- Chuỗi onboarding sau khi đăng ký

## Bước 1: Brief Campaign
Hỏi:
1. Loại campaign (launch/nurture/promo/onboarding/winback)
2. Sản phẩm + USP
3. Đối tượng nhận (segment + insight)
4. Mục tiêu (mua/đăng ký/tải/booking)
5. Số email (5/7) + khoảng cách (1 ngày/3 ngày)
6. Offer + deadline
7. Tone giọng (thân mật/chuyên nghiệp)

## Bước 2: Map Hành Trình Theo Email
Ví dụ launch 7 email:
- Email 1: Teaser (D-7)
- Email 2: Story/Why (D-5)
- Email 3: Lift the curtain (D-3)
- Email 4: Launch (D0) - mở bán
- Email 5: Social proof (D+1)
- Email 6: FAQ/objection (D+3)
- Email 7: Last chance (D+5)

## Bước 3: Viết Từng Email
Mỗi email cần:
- 3 subject line A/B (<40 ký tự, có emoji nếu phù hợp)
- Preview text 80-100 ký tự
- Thân email 150-300 từ
- 1 CTA chính + 1 P.S.
- Personalization token ({{ten}}, {{cong_ty}})

Subject line dùng các formula:
- Câu hỏi: "Bạn đã thử cách này chưa?"
- Số liệu: "3 cách tăng 2x doanh thu trong 30 ngày"
- Tò mò: "Điều ít ai nói về..."
- Lợi ích: "Tiết kiệm 5h/tuần với..."

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Gmail MCP: tạo draft từng email
- Mailchimp/Brevo MCP (nếu có): tạo campaign sẵn schedule
- Google Drive MCP: lưu file copy + bảng kế hoạch
- Notion MCP: lưu vào database Email Library
- WebSearch: tra subject line trending mùa hiện tại

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tạo campaign Brevo (Sendinblue)
import sib_api_v3_sdk
api = sib_api_v3_sdk.EmailCampaignsApi(...)
campaign = sib_api_v3_sdk.CreateEmailCampaign(
  name='Launch Email 1', subject=subject,
  sender={'name':'TAKI','email':'hi@taki.vn'},
  html_content=html, recipients={'listIds':[5]},
  scheduled_at='2026-06-01T08:00:00+07:00')
api.create_email_campaign(campaign)
```

## Bước 5: Output Format
- File `.md` chứa 5-7 email với phân tách rõ
- Bảng kế hoạch gửi: ngày, giờ, segment, KPI mục tiêu
- File `.html` template responsive sẵn để paste vào ESP
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Mỗi email có 3 subject line A/B
- [ ] Có preview text
- [ ] CTA rõ ràng, link chứa UTM
- [ ] Email mobile-friendly (1 cột)
- [ ] Tone giọng nhất quán
- [ ] Đã thử trên Litmus/Email on Acid (nếu có)
- [ ] Tuân thủ chống spam (unsubscribe, địa chỉ)
