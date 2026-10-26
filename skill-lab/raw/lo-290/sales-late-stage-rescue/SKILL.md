---
name: sales-late-stage-rescue
description: |
  Cứu deal late-stage stuck 30+ ngày qua diagnostic, re-qualify, executive escalation, mutual deadline. Trigger phrases: "cứu deal stuck", "rescue late stage deal", "deal late stage không close", "unstuck deal", "deal stalled rescue", "khắc phục deal kẹt", "deal stuck 30 ngày", "late stage intervention", "khẩn cấp đóng deal", "deal recovery". Output là Markdown diagnostic + Excel rescue plan + escalation email.
---

# Late-Stage Deal Rescue Playbook

## Mục Tiêu
Cứu 40-60% deal late-stage stuck >30 ngày bằng diagnostic root cause, re-qualify champion/EB, executive escalation và creating urgency — thay vì "follow-up đến chết".

## Khi Nào Dùng
- Deal trong Negotiation/Verbal >30 ngày
- Champion không response 2 tuần
- Close date slip >2 lần
- EB không respond/meeting
- Competitor surprise enter late

## Bước 1: Diagnostic 8 Question
- Lần cuối nói chuyện EB bao giờ?
- Champion còn ở công ty + still bought-in?
- MAP có sign? Milestone nào missed?
- Có competitor mới enter?
- Internal change phía KH (M&A, CEO change, restructure)?
- Budget bị cut?
- Priority KH shift?
- Legal/Procurement đang stuck ở đâu?

Identify TOP 1-2 root cause.

## Bước 2: 6 Rescue Plays Tuỳ Root Cause

**A. Champion lost** → tìm new champion qua org chart + multithread

**B. EB không engage** → Executive Sponsor mình outreach VP KH peer-to-peer

**C. Budget cut** → reduce scope (POC / Pilot phase 1) thay vì full

**D. Competitor enter** → side-by-side comparison + reference call

**E. Procurement stuck** → CEO/CFO outreach unblock

**F. Priority shift** → revisit pain + new business case match new priority

## Bước 3: Re-qualify Conversation
Champion call 30 phút:
- "Em cần frank — deal này có còn live không?"
- "Top 3 obstacle hiện tại?"
- "Anh cần em hỗ trợ gì?"
- "Realistic close date?"

Nếu Champion không trả lời được → deal đã dead, just don't know.

## Bước 4: Mutual Deadline (Forcing Function)
Tạo urgency có lý do business:
- Pricing valid hết Q3
- Implementation slot cuối quý
- New regulation effective date
- Executive sponsor calendar lock

→ KH phải quyết Y/N trong 14 ngày.

## Bước 5: Executive Escalation
Email VP-to-VP:
- Recap pain + value
- Status update
- 1 specific ask (15 min call, decision update)
- Tone: respectful, not desperate

CC champion để họ thấy momentum.

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce MCP: pull deal history + last activity
- Gong MCP: phân tích last call sentiment
- LinkedIn MCP: tracking stakeholder move
- Calendar MCP: book emergency meeting
- Slack MCP: deal war-room channel

**Fallback API:**
```python
# Detect deal stuck signals
def detect_stuck(opp):
    last_activity_days = (date.today() - opp["LastActivityDate"]).days
    stage_age_days = (date.today() - opp["StageChangeDate"]).days
    signals = []
    if last_activity_days > 14: signals.append("no_activity_2w")
    if stage_age_days > 30: signals.append("stage_30d+")
    if opp["CloseDate"] < date.today(): signals.append("past_close")
    if opp["LossReason__c"] is None and len(signals) >= 2:
        return "ESCALATE_RESCUE"
```

## Bước 7: Output Format
- **File 1**: `rescue_diagnostic.md` — 8 question template
- **File 2**: `rescue_plays.md` — 6 play với script
- **File 3**: `rescue_plan_<deal>.xlsx` — action plan per deal
- **File 4**: `exec_escalation_email.md` — VP-to-VP template
- **File 5**: `mutual_deadline_letter.md` — create urgency
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Diagnostic 8 question completed
- [ ] Root cause identified (1-2)
- [ ] Champion re-quali frank
- [ ] Exec sponsor briefed
- [ ] Mutual deadline có lý do business
- [ ] Decision Y/N trong 14 ngày
- [ ] Nếu N → close-lost với reason rõ
