---
name: cs-customer-success-onboarding
description: |
  Thiết kế quy trình onboarding cho khách hàng mới — đặc biệt B2B/SaaS — 30/60/90 ngày, milestone, healthcheck, đảm bảo time-to-value nhanh. Dùng skill này khi người dùng yêu cầu: "customer onboarding", "CS onboarding plan", "30 60 90 days", "time to value", "kickoff meeting B2B", "SaaS onboarding flow", "customer success plan", "đón khách hàng mới". Output là Excel timeline + email sequence + slide kickoff.
---

# CS Customer Success Onboarding Designer

## Mục Tiêu
Tạo quy trình onboarding chuẩn 30/60/90 ngày cho KH mới (đặc biệt B2B/SaaS) — giảm time-to-value, tăng tỷ lệ activation > 80%, giảm churn 6 tháng đầu.

## Khi Nào Dùng
- SaaS / B2B mới có CSM team
- KH ký xong nhưng "lạnh", không dùng tới sản phẩm
- Churn 3 tháng đầu cao (>15%)
- Cần training KH dùng feature mới
- Scale từ 10 → 100 khách, không thể onboard tay từng người

## Bước 1: Map Customer Journey 0-90 Ngày
**Day 0 — Kickoff**
- Welcome email từ CSM + lịch kickoff call
- Send onboarding portal link + checklist

**Day 1-7 — Setup & Activation**
- Kickoff call (60 phút): goals, success metrics, team intro
- Hands-on training session 1 (core feature)
- Setup integration / data import
- Milestone: "First Value" — KH đã sử dụng tính năng chính 1 lần

**Day 8-30 — Adoption**
- Weekly check-in 30 phút
- Training session 2 (advanced features)
- Milestone: 80% team đã active, dùng 3+ feature

**Day 31-60 — Expansion**
- Monthly business review
- Khám phá upsell opportunity
- Milestone: ROI report đầu tiên

**Day 61-90 — Growth**
- Quarterly business review (QBR)
- Renewal prep nếu hợp đồng năm
- Milestone: NPS > 8

## Bước 2: Onboarding Checklist Cho KH
Portal/Notion checklist:
- [ ] Tham gia kickoff call
- [ ] Đăng ký 5 users
- [ ] Hoàn thành training video 1
- [ ] Import dữ liệu cơ bản
- [ ] Tạo dashboard đầu tiên
- [ ] Mời 3 đồng nghiệp join
- [ ] Đăng ký webinar tháng

KH hoàn thành → bonus voucher / extra storage.

## Bước 3: Healthcheck & Early Warning
**Healthcheck score (0-100):**
- Login frequency (30%)
- Feature adoption depth (30%)
- Support ticket sentiment (20%)
- Stakeholder engagement (20%)

Score < 60 → CSM intervention (call ngay, không chờ)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Calendar MCP: book kickoff + weekly check-in tự động
- Gmail MCP: gửi email sequence 30/60/90 ngày
- Slack MCP: tạo channel chung CSM ↔ KH (nếu B2B lớn)
- Google Sheets: dashboard health score
- Notion/Drive MCP: portal onboarding cho KH
- WebSearch: best practice Gainsight / Catalyst CS

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tính health score từ product usage + alert nếu thấp
import requests
from datetime import datetime, timedelta
def health_score(customer_id):
    usage = requests.get(f"https://api/usage?cid={customer_id}").json()
    login_30d = usage["login_count_30d"]
    features_used = len(usage["features_used"])
    tickets_neg = usage["negative_tickets_30d"]
    score = (min(login_30d/30, 1)*30 + min(features_used/10, 1)*30
             - tickets_neg*10 + 40)
    if score < 60:
        slack_alert(f"Health low: {customer_id} = {score}")
    return score
```

## Bước 5: Output Format
- **Excel `Onboarding_Plan.xlsx`**: timeline 90 ngày, milestone, owner
- **Email sequence** 8 mail trong 90 ngày (welcome → kickoff → training → QBR)
- **Slide kickoff PPTX** (15 slide): intro team, goals, roadmap
- **Onboarding checklist** Notion/portal cho KH
- **Health score dashboard**
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-customer-success-onboarding/output/`

## Checklist Trước Khi Giao
- [ ] Timeline 30/60/90 ngày có milestone đo được
- [ ] Mỗi giai đoạn có meeting + content
- [ ] Health score công thức rõ
- [ ] Email sequence có placeholder personalize
- [ ] Có early warning + intervention play
- [ ] Slide kickoff template sẵn dùng
