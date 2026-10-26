---
name: sales-postsale-handover
description: |
  Handover Sales → Customer Success chi tiết sau closed-won — context, commitment, risk để CSM onboard tốt. Trigger phrases: "handover sales CS", "post-sale handover", "sales to CSM transition", "onboarding handover", "kickoff customer success", "chuyển KH cho CS", "handover sau closed won", "internal kickoff KH mới", "sales success handoff", "transition AE CSM". Output là Markdown handover doc + Excel checklist + kickoff agenda.
---

# Post-Sale Sales → CSM Handover

## Mục Tiêu
Đảm bảo CSM nhận KH mới với 100% context (deal, commitment, risk, stakeholder) để onboard thành công trong 30 ngày, tránh "AE bán xong biến mất" gây churn năm 1.

## Khi Nào Dùng
- Mỗi deal closed-won
- Renewal team takeover từ AE
- Re-segment portfolio
- AE move team / leave
- Implementation handover sau go-live

## Bước 1: Internal Handover Meeting (45 phút)
AE + CSM + SE meet trong 7 ngày sau close. Agenda:

**A. Deal context (10 phút)**:
- KH overview, vertical, size
- Why bought, alternatives considered
- Key pain solving

**B. Commitment recap (15 phút)**:
- What was promised in sales process
- Specific deliverable, timeline
- Pricing, terms, SLA
- Verbal commitments không trong contract

**C. Stakeholder transfer (10 phút)**:
- Champion + EB + buying committee
- Personal context each person
- Communication preference

**D. Risk & opportunity (5 phút)**:
- Top 3 risk implementation
- Expansion signal (BU, multi-product)
- Red flag KH (slow legal, low IT capacity)

**E. Next step (5 phút)**:
- CSM intro email plan
- Kickoff meeting date
- AE shadow first 30 ngày

## Bước 2: Handover Doc 2 Trang
Document gồm:
- **Account 360**: company, deal terms, products
- **Stakeholders**: 5-8 people + role + relationship
- **Sold Solution**: use cases, scope, integration
- **Commitments**: in-contract + verbal
- **Timeline**: implementation milestone
- **Risk register**: 5 risk + mitigation
- **Expansion radar**: signal mua thêm
- **Champion notes**: personal context

## Bước 3: External Kickoff Meeting
2 tuần sau close, KH meeting (60 phút):
- CSM intro
- KH team intro
- Goals + success criteria
- Implementation timeline
- Communication cadence
- Escalation path

AE shadow, không lead.

## Bước 4: AE Shadow Period (30 ngày)
- AE attend weekly CSM-KH call
- AE available phone-a-friend
- AE help solve early issue
- AE introduce add-on if signal

After 30 ngày, AE step out.

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce/HubSpot MCP: account ownership transfer
- Gainsight/Totango MCP: KH onboard
- Slack MCP: account channel handover
- Calendar MCP: book kickoff meeting
- Drive MCP: handover doc shared

**Fallback API:**
```python
# Auto-handover sau close
def handover(opp_id):
    opp = sf.Opportunity.get(opp_id)
    if opp["StageName"] == "Closed Won":
        # Transfer ownership
        sf.Account.update(opp["AccountId"], {"OwnerId": CSM_ID})
        # Create handover task
        sf.Task.create({"Subject": "CSM Handover Meeting",
            "WhatId": opp["AccountId"], "OwnerId": CSM_ID,
            "ActivityDate": (date.today()+timedelta(7)).isoformat()})
        # Gainsight create CTA
        create_gainsight_cta(account_id=opp["AccountId"], type="Onboard")
```

## Bước 6: Output Format
- **File 1**: `handover_doc_<customer>.md` — 2 trang full context
- **File 2**: `handover_checklist.xlsx` — 30-item check
- **File 3**: `kickoff_agenda_external.md` — 60-phút agenda KH
- **File 4**: `internal_handover_meeting_notes.md` — 45-phút internal
- **File 5**: `ae_shadow_30day_plan.md` — shadow period plan
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Internal handover trong 7 ngày
- [ ] Handover doc 2 trang đầy đủ
- [ ] Verbal commit document
- [ ] External kickoff trong 2 tuần
- [ ] AE shadow 30 ngày
- [ ] CSM acknowledge nhận đủ context
- [ ] Owner transfer trong CRM
