---
name: sales-multithreading-template
description: |
  Multi-thread enterprise deal — tiếp cận 5-8 stakeholder song song để giảm single-thread risk. Trigger phrases: "multithreading deal", "đa luồng enterprise deal", "tiếp cận nhiều stakeholder", "multi-thread sales", "expand buying committee", "tránh single thread", "multi-coach deal", "stakeholder expansion", "thread enterprise", "multithread playbook". Output là Markdown playbook + Excel thread map + email templates.
---

# Multi-threading Enterprise Deal

## Mục Tiêu
Giảm single-thread risk (deal die khi champion leave) bằng multi-thread 5-8 stakeholder song song mỗi enterprise deal — tăng win rate 30-50%.

## Khi Nào Dùng
- Enterprise deal >$100K
- Sales cycle >3 tháng
- Champion mới join (chưa power)
- Risk M&A KH
- Deal sau win-back

## Bước 1: Identify 5-8 Threads
Per account, map:
- **Champion** (1) — main
- **Co-champion** (1-2) — backup nếu champion leave
- **Economic Buyer** (1)
- **Technical Buyer** (1)
- **User Buyer** (1-2)
- **Coach** (1) — info feeder
- **Executive Sponsor** (1) — VP+

Mỗi thread có owner mình side (AE / SE / Manager / Executive).

## Bước 2: Outreach Each Thread

**Champion**: weekly touch, share roadmap, coaching call

**Economic Buyer**: monthly, exec-to-exec, ROI focus, brief

**Technical Buyer**: bi-weekly, SE-led, deep technical, security

**User Buyer**: bi-weekly, training/onboarding focus, demo

**Coach**: ad-hoc, casual info exchange

**Executive Sponsor**: quarterly, strategic, vision

## Bước 3: Coordination & Hygiene
- CRM tag each contact role + last touch
- Internal Slack channel per deal
- Weekly thread review meeting
- Avoid contradict messaging across threads
- Manager coach AE on multi-thread

## Bước 4: Risk Detection
Monitor:
- Thread silent >2 tuần → ping
- Stakeholder leave → exec escalation
- Conflicting message → align internally
- New stakeholder appear → expand thread
- Stakeholder become Blocker → tách

## Bước 5: Land & Expand Threading
Sau win deal đầu:
- Expand thread sang BU khác
- Map champion's network
- Reference call internal cho prospect mới same company
- White space mapping

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce MCP: contact role + opportunity contact
- LinkedIn MCP: org chart + activity
- Gong MCP: track mention stakeholder trong call
- Slack MCP: deal channel coordination
- Calendar MCP: schedule multi-thread meeting

**Fallback API:**
```python
# Multi-thread health check
def thread_health(opp_id):
    contacts = sf.query(f"""SELECT ContactId, Role, LastActivityDate
        FROM OpportunityContactRole WHERE OpportunityId='{opp_id}'""")["records"]
    health = {}
    for c in contacts:
        days_silent = (date.today() - c["LastActivityDate"]).days
        health[c["Role"]] = "Active" if days_silent < 14 else "Silent"
    # Alert if Champion silent
    if health.get("Champion") == "Silent":
        alert_ae(opp_id, "CHAMPION_SILENT_2W")
    return health
```

## Bước 7: Output Format
- **File 1**: `multithreading_playbook.md` — framework full
- **File 2**: `thread_map_<deal>.xlsx` — 5-8 thread × owner × last touch × status
- **File 3**: `thread_outreach_templates.md` — 6 role × email template
- **File 4**: `thread_coordination_meeting.md` — weekly review agenda
- **File 5**: `thread_health_dashboard.xlsx` — monitor silent threads
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 5-8 thread per enterprise deal
- [ ] Owner mỗi thread assigned
- [ ] Weekly thread review
- [ ] Silent >2 tuần alert
- [ ] Conflicting message aligned internal
- [ ] Land-and-expand plan sau win
