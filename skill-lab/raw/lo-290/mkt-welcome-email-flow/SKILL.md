---
name: mkt-welcome-email-flow
description: |
  Chuỗi email chào mừng Day 0-7-14-30 cho KH/lead mới đăng ký doanh nghiệp Việt Nam — onboarding, value education, first conversion. Kích hoạt khi người dùng nói: "welcome email flow", "chuỗi email chào mừng", "email onboarding", "welcome series", "email cho khách mới", "nurture flow", "first email sequence", "drip campaign chào mừng". Output là Markdown + HTML template.
---

# Chuỗi Email Chào Mừng Day 0-7-14-30

## Mục Tiêu
Biến lead mới đăng ký thành customer trong 30 ngày với chuỗi welcome chuẩn — Day 0 chào, Day 1 educate, Day 3 social proof, Day 7 demo, Day 14 case, Day 30 reactivate.

## Khi Nào Dùng
- Lead form trên LP
- Người tải lead magnet
- Người đăng ký newsletter
- Khách mới mua lần đầu
- User mới signup SaaS

## Bước 1: Brief Audience
Hỏi:
1. Sản phẩm/dịch vụ
2. Điểm vào (form/lead magnet/purchase/signup)
3. Cold/warm
4. Mục tiêu (mua/dùng/refer)
5. Có sales team follow không
6. Tone brand

## Bước 2: Cấu Trúc 5-7 Email
**Day 0**: Welcome + Quick Win
- Subject: "Chào mừng {ten}! Bắt đầu trong 5 phút"
- Lời chào founder + 1 quick win áp dụng ngay
- Link tài nguyên gift
- Set expectation (sẽ nhận gì 30 ngày tới)

**Day 1**: Founder Story
- Why we built this
- Mission + values
- Đặt câu hỏi "Bạn đang gặp vấn đề gì?"

**Day 3**: Social Proof
- 2-3 case study ngắn + số liệu
- Trust badge (KH, giải thưởng)
- CTA mềm đăng ký demo / mua thử

**Day 7**: Educate Sâu
- 1 framework / cheatsheet / how-to
- Position brand như expert
- Mời participate community

**Day 14**: Case Study Đầy Đủ
- Câu chuyện 1 KH thành công
- Đo lường cụ thể
- CTA mua / call sales

**Day 21** (option): Objection Handler
- FAQ + so sánh với đối thủ
- Đảm bảo hoàn tiền

**Day 30**: Last Push + Reactivate
- Offer giới hạn cuối
- Nếu vẫn không mua → segment qua list nurture dài hạn

## Bước 3: Trigger & Segment
Trigger flow theo:
- Source (form A / B / lead magnet C)
- Persona auto-tag từ form
- Behavior (mở email/click → branch khác nhau)

Skip rule: nếu mua → skip phần sell; nếu unsubscribe → stop.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Klaviyo/Mailchimp/Brevo MCP: setup automation
- Zalo OA MCP: ZNS song song
- CRM MCP (HubSpot): trigger từ form
- Sheets MCP: tracker
- Notion MCP: copy library

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Trigger welcome flow khi có lead mới
from flask import Flask, request
app = Flask(__name__)
@app.route('/webhook/lead', methods=['POST'])
def new_lead():
    lead = request.json
    queue.enqueue('send', lead['email'], 'welcome_day0', delay=0)
    queue.enqueue('send', lead['email'], 'founder_story', delay=86400)
    queue.enqueue('send', lead['email'], 'social_proof', delay=86400*3)
    # ...
    return '',200
```

## Bước 5: Output Format
- File `.md` 5-7 email đầy đủ
- File `.html` template responsive
- Flow chart
- Tracker open/click/CR per email
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 5-7 email đúng timing
- [ ] Personalization token
- [ ] Branch theo behavior
- [ ] Skip rule sau mua
- [ ] Có CTA tăng dần
- [ ] Tracker đầy đủ
- [ ] Đã preview mobile
