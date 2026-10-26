---
name: sales-executive-briefing
description: |
  Briefing executive-level 3 slide cho CEO/CFO/Board meeting về deal/strategy/customer. Trigger phrases: "executive briefing", "brief CEO deal", "exec summary deal", "C-level briefing slide", "board update deal", "briefing 3 slide", "exec note sales", "summary deal cho sếp", "leadership update sales", "executive memo deal". Output là PPT 3 slide + Markdown talking points.
---

# Executive Briefing (3-Slide Format)

## Mục Tiêu
Brief CEO/CFO/Board về deal/strategy/customer trong 3 slide / 5 phút talking — đủ context để quyết định, không lan man — đây là format leadership prefer thực tế.

## Khi Nào Dùng
- CEO request status deal lớn
- Board meeting quarterly review
- Crisis update (deal at risk)
- Strategic partnership discussion
- Customer escalation cần leadership action

## Bước 1: 3-Slide Structure

**Slide 1 — Situation (1 phút)**:
- Headline: 1 câu bottom-line
- 3 bullet context (KH, deal size, timeline)
- 1 metric quan trọng

**Slide 2 — Issue & Options (3 phút)**:
- Top 1-2 issue
- 3 option (each: pros, cons, $$ impact)
- Recommendation

**Slide 3 — Ask & Next Step (1 phút)**:
- Specific ask từ exec (decision, resource, action)
- Next step + owner + deadline
- Backup contact

## Bước 2: Writing Rules
- Headline mỗi slide = full sentence (không "Status")
- Max 5 bullet/slide
- Max 30 từ/bullet
- 1 chart hoặc table per slide
- Numbers > adjectives ("$2M at risk" > "significant")

## Bước 3: Talking Points (1 trang)
Riêng 1 trang note 5-phút speak:
- Opening (15s): TLDR
- Slide 1 detail (1 phút)
- Slide 2 deep + recommendation (3 phút)
- Slide 3 ask (1 phút)
- Q&A prepared (5 câu)

## Bước 4: Pre-brief & Calibration
- Send 24h trước meeting
- Pre-call champion exec để align
- Anticipate 5 câu hỏi + answer
- Backup deck (Appendix) detail nếu CEO deep-dive

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- PPT MCP: tạo deck
- Salesforce MCP: pull deal data realtime
- BI MCP: chart embed
- Email/Outlook MCP: send pre-brief
- Calendar MCP: book meeting

**Fallback API:**
```python
# Auto-generate exec briefing
from pptx import Presentation
ppt = Presentation("exec_brief_template.pptx")
deal = sf.Opportunity.get(deal_id)
# Slide 1
ppt.slides[0].placeholders[0].text = f"{deal['Name']} - ${deal['Amount']/1000:.0f}K at risk"
ppt.slides[0].placeholders[1].text = bullets[0]
# Slide 2 - options
for i, opt in enumerate(options):
    ppt.slides[1].placeholders[i].text = f"{opt['name']}: {opt['impact']}"
# Slide 3 - ask
ppt.slides[2].placeholders[0].text = ask
ppt.save("exec_brief.pptx")
```

## Bước 6: Output Format
- **File 1**: `exec_brief_<topic>.pptx` — 3 slide chính
- **File 2**: `talking_points.md` — 5 phút script
- **File 3**: `backup_appendix.pptx` — 10 slide detail
- **File 4**: `anticipated_qa.md` — 5 câu CEO sẽ hỏi
- **File 5**: `prebrief_email.md` — send 24h trước
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đúng 3 slide
- [ ] Headline mỗi slide = bottom-line statement
- [ ] Numbers cụ thể (không adjective)
- [ ] Recommendation rõ
- [ ] Ask cụ thể từ exec
- [ ] Q&A prepared
- [ ] Pre-brief 24h trước
