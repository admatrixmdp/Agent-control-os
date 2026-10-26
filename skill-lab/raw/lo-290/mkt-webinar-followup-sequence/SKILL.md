---
name: mkt-webinar-followup-sequence
description: |
  Chuỗi 5 email follow-up sau webinar cho doanh nghiệp Việt Nam — thank you, replay, case study, FAQ, last chance — tăng conversion sau webinar 2-3x. Kích hoạt khi người dùng nói: "email follow-up webinar", "chuỗi email sau webinar", "webinar follow-up", "email sau live", "post-webinar email", "nurture sau webinar", "webinar conversion email", "5 email sau webinar". Output là Markdown + HTML template.
---

# Chuỗi 5 Email Follow-up Sau Webinar

## Mục Tiêu
Phục hồi 30-50% người tham dự không mua tại webinar bằng chuỗi 5 email trong 7 ngày — biến webinar từ event "1 lần" thành funnel.

## Khi Nào Dùng
- Sau webinar bán khóa học/dịch vụ
- Sau livestream chốt đơn
- Sau workshop free funnel
- Sau demo SaaS đông người
- Chuỗi launch sản phẩm

## Bước 1: Brief Webinar
Hỏi:
1. Sản phẩm/khóa học
2. Số người dự / no-show
3. Offer + giá + deadline
4. CR tại webinar (% mua live)
5. Đối tượng (cold/warm)
6. Replay link
7. CTA cuối (đặt cọc / call sales)

## Bước 2: Cấu Trúc 5 Email
**Email 1 (T+1 ngày): Thank you + Replay**
- Cảm ơn tham dự / xin lỗi không dự
- Link replay (xem trước thời gian X)
- Gift sau webinar (PDF, checklist)
- CTA mềm "Bắt đầu thử"

**Email 2 (T+2): Case study**
- Câu chuyện thành công của 1 KH
- Kết quả cụ thể
- CTA: book demo / mua

**Email 3 (T+3): FAQ + Objection**
- 5-7 FAQ xử lý objection (giá, thời gian, kỹ thuật)
- Money-back guarantee
- CTA: chat ngay

**Email 4 (T+5): Scarcity + Bonus**
- Còn X chỗ / X giờ
- Thêm bonus đặc biệt cho người mua trong 48h
- Counter động

**Email 5 (T+7): Last chance**
- Chỉ còn 24h
- Tóm tắt offer
- 1 quote KH
- CTA cuối

## Bước 3: Personalization & A/B
Chia segment:
- Attended + mua → email cảm ơn riêng (skip chuỗi nurture)
- Attended chưa mua → full chuỗi
- No-show → email 1 thêm replay link nổi bật

A/B subject line + CTA position.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Mailchimp/Brevo/Klaviyo MCP: automation flow
- Gmail MCP: gửi cá nhân hóa (small batch)
- Webinar platform MCP (Zoom/GoToWebinar): pull attendance list
- Sheets MCP: tracker
- Notion MCP: copy library

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tạo automation flow Klaviyo
import requests
flow = {'name':'Webinar Followup','triggers':[{
  'type':'list_added','list_id':'WEBINAR_ATTENDEES'}],
  'actions':[
    {'type':'wait','duration':1440},  # 1 ngày
    {'type':'send_email','template_id':TPL_THANK_YOU},
    {'type':'wait','duration':1440},
    {'type':'send_email','template_id':TPL_CASE_STUDY},
    # ...
  ]}
requests.post('https://a.klaviyo.com/api/flows',
  headers={'Authorization':f'Klaviyo-API-Key {API_KEY}'},
  json={'data':flow})
```

## Bước 5: Output Format
- File `.md` 5 email đầy đủ (3 subject A/B mỗi email)
- File `.html` template responsive
- Flow chart automation
- Tracker open/click/CR
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 5 email đúng thứ tự T+1,2,3,5,7
- [ ] Subject A/B mỗi email
- [ ] Segment attended vs no-show
- [ ] Có scarcity hợp lý
- [ ] CTA rõ từng email
- [ ] Personalization token
- [ ] Tracker dashboard
