---
name: sales-sdr-handover
description: |
  Checklist handover SDR → AE đảm bảo lead qualified đầy đủ context, không drop ball. Trigger phrases: "SDR AE handover", "handover lead SDR", "chuyển lead cho AE", "SDR to AE checklist", "lead handover SOP", "quy trình chuyển lead", "transition SDR AE", "MQL handover", "qualified lead handover", "sales handover process". Output là Markdown SOP + Excel handover form + Slack template.
---

# SDR-to-AE Handover Checklist

## Mục Tiêu
Đảm bảo 100% lead qualified được AE nhận với đầy đủ context để hold demo trong 24h — giảm meeting no-show và tăng demo-to-deal conversion.

## Khi Nào Dùng
- SDR set meeting với AE
- MQL/SAL chuyển từ Marketing
- Round-robin assignment AE
- AE on PTO cần backup
- Cross-region routing

## Bước 1: SDR Qualify Criteria (BANT-lite)
Trước khi handover, SDR confirm:
- **Budget**: KH có ý niệm ngân sách (không cần con số chính xác)
- **Authority**: contact có role decide hoặc influencer
- **Need**: pain confirm + use case match ICP
- **Timeline**: KH muốn solve trong 90 ngày
- **Fit**: company match ICP (size, industry, geo)

Nếu thiếu 2 → re-nurture, không handover.

## Bước 2: Handover Form (10 field bắt buộc)
1. Company + size + industry
2. Contact name + title + email + mobile + LinkedIn
3. Pain ranked top 3
4. Trigger event KH chia sẻ
5. Current tool/process
6. Budget signal (open/confirmed/ngầm)
7. Decision process + timeline
8. Buying committee (ai khác cần invite demo)
9. Notes call/email history
10. Meeting time confirmed + agenda đã share

## Bước 3: 24h SLA AE Acknowledge
AE phải:
- Acknowledge nhận lead trong 4h
- Research thêm KH trước meeting
- Confirm meeting với KH (re-invite)
- Update CRM stage thành "Discovery scheduled"

Manager dashboard track SLA breach.

## Bước 4: No-show Recovery
Nếu KH no-show:
- AE liên hệ trong 30 phút (text + call)
- SDR back-up reach out cùng kênh
- 3 attempt trong 48h
- Nếu vẫn không response → demote lead về SDR nurture

## Bước 5: Quality Feedback Loop
AE feedback SDR sau 7 ngày:
- Lead quality score 1-5
- Lý do disqualify nếu DQ
- Coaching SDR cụ thể

Aggregate weekly để tune qualify criteria.

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce/HubSpot MCP: auto-create opportunity từ MQL
- Calendar MCP: book meeting + invite multiple attendees
- Slack MCP: notify AE + post handover summary
- Gong MCP: link call recording SDR đã làm

**Fallback API:**
```python
# Auto create opp + assign + notify
opp_id = sf.Opportunity.create({"AccountId": acct_id,
    "Name": f"{company} - Discovery", "StageName": "Discovery",
    "CloseDate": (datetime.now()+timedelta(60)).isoformat(),
    "OwnerId": ae_id})
# Slack notify
requests.post(SLACK_WEBHOOK, json={"text": 
    f"New handover: {company} → @{ae_name}. Meeting Thứ 3 10h.",
    "attachments": [{"text": handover_notes}]})
```

## Bước 7: Output Format
- **File 1**: `sdr_ae_handover_form.md` — 10 field template
- **File 2**: `handover_SOP.md` — quy trình + SLA + escalation
- **File 3**: `handover_quality_log.xlsx` — log feedback AE→SDR weekly
- **File 4**: `slack_handover_template.md` — message format chuẩn
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] BANT-lite check đủ 4 chiều
- [ ] 10 field handover form không thiếu
- [ ] SLA 4h AE acknowledge
- [ ] No-show recovery quy trình rõ
- [ ] Weekly quality loop SDR-AE
- [ ] Manager dashboard track SLA
