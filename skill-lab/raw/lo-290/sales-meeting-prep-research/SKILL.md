---
name: sales-meeting-prep-research
description: |
  Research KH trước meeting — pull data web, LinkedIn, news, financial để AE chuẩn bị insight cá nhân hoá. Trigger phrases: "research khách trước meeting", "meeting prep", "pre-call research", "prep cho sales meeting", "research prospect", "pre-meeting brief", "tìm hiểu KH trước call", "discovery pre-call research", "background check KH", "research B2B sales". Output là Markdown brief 1 trang + Excel insight log.
---

# Pre-Meeting Customer Research

## Mục Tiêu
Tạo brief 1 trang KH trong 15-20 phút trước meeting, cung cấp 5-7 insight cá nhân hoá để AE pitch trúng pain + tăng credibility từ phút đầu.

## Khi Nào Dùng
- Cold call/discovery với prospect lạ
- Demo enterprise có C-level dự
- Renewal QBR với KH lớn
- Event meeting kín
- Roadshow regional

## Bước 1: 6 Source Research

**A. Company website** (3 phút):
- About / Mission
- Products / Services portfolio
- News / Blog 6 tháng gần
- Customer logos hiển thị

**B. LinkedIn Company** (3 phút):
- Headcount trend (growth %)
- Recent post / leadership update
- Industries served
- Tech stack mentioned

**C. LinkedIn People** (3 phút):
- Attendee LinkedIn (role, tenure, prev companies)
- Recent post của họ (3 post)
- Mutual connection
- Education / interests

**D. News & PR** (3 phút):
- Funding announcement
- Executive hire/leave
- M&A activity
- Lawsuit / regulation
- Awards / certifications

**E. Financial** (3 phút):
- Revenue (if public)
- 10-K nếu listed
- Crunchbase funding
- Annual report

**F. Industry context** (2 phút):
- Vertical trend
- Top competitors KH
- Recent disruptions

## Bước 2: 5-7 Insight Distillation
Từ research, distill:
- **Trigger event**: 1-2 lý do KH có thể mua
- **Pain hypothesis**: 2-3 pain probable
- **Stakeholder angle**: bias / interest của EB
- **Competitor reference**: ai họ likely so sánh
- **Conversation starter**: 1-2 topic break ice
- **Avoid topic**: chủ đề nhạy cảm (layoff, lawsuit)

## Bước 3: 1-page Brief Template
```
COMPANY: [Tên] — [Industry, Size, Geo]
ATTENDEES: [Name | Role | LinkedIn signal]

TRIGGER EVENT
• [Event 1 with date]

PAIN HYPOTHESIS
• [Top 3]

OUR ANGLE
• [Reframe based on insight]

ICEBREAKERS
• [Personal/professional reference]

AVOID
• [Sensitive topic]

REFERENCES TO SHARE
• [Case study same vertical]
```

## Bước 4: Save & Reuse
- Lưu vào CRM custom field
- Update sau meeting với "what was confirmed/wrong"
- Reuse cho follow-up meeting cùng KH

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- WebFetch: website + news article
- LinkedIn MCP: profile + company
- Crunchbase MCP: funding data
- Salesforce MCP: lưu brief vào activity
- WebSearch: industry trend, recent news

**Fallback API:**
```python
# Auto pre-call brief
import requests
def build_brief(company, attendees):
    brief = {}
    # Company news
    news = requests.get(f"https://newsapi.org/v2/everything",
        params={"q": company, "from": last_180_days, "apiKey": NEWS_KEY}).json()
    brief["news"] = [n["title"] for n in news["articles"][:5]]
    # LinkedIn attendees
    for a in attendees:
        a["recent_posts"] = scrape_linkedin_posts(a["url"])[:3]
    return brief
```

## Bước 6: Output Format
- **File 1**: `prep_brief_<account>.md` — 1 trang template
- **File 2**: `prep_research_log.xlsx` — log insight + outcome
- **File 3**: `prep_checklist.md` — 6 source checklist
- **File 4**: `prep_examples.md` — 3 ví dụ filled brief
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 6 source covered
- [ ] 5-7 insight actionable
- [ ] Trigger event identified
- [ ] Icebreaker tự nhiên không gượng
- [ ] Avoid topic flagged
- [ ] Brief <1 page (không dài)
- [ ] Update sau meeting với reality
