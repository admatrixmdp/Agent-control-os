---
name: sales-meeting-followup-summary
description: |
  Tóm tắt meeting sau call + sinh email next-step với recap pain + agreement + action. Trigger phrases: "tóm tắt meeting", "meeting summary", "post-meeting note", "summary email sau meeting", "tổng kết call KH", "AI meeting recap", "next step email", "summary recap sales", "biên bản họp KH", "auto-summary meeting". Output là Markdown summary + email + CRM activity log.
---

# Post-Meeting Summary & Follow-up Generator

## Mục Tiêu
Tự động tóm tắt meeting trong 5 phút (vs 30 phút thủ công), sinh email follow-up có recap đầy đủ + next step rõ ràng, log CRM activity — tránh "AE quên ghi" miss deal momentum.

## Khi Nào Dùng
- Sau mỗi discovery/demo/negotiation call
- Multi-attendee meeting cần share notes
- Cross-functional internal meeting về deal
- KH meeting có decision quan trọng
- AE on PTO cần handover

## Bước 1: Input Sources
- Call recording / transcript (Gong/Chorus)
- Manual notes AE
- Chat trong call (Zoom)
- Email kèm trước/sau meeting
- Calendar invite description

## Bước 2: Cấu trúc Summary (6 phần)

**1. Meeting metadata**: Date, attendees, duration
**2. Discussion topics** (3-5 bullet)
**3. Key pain points raised** (KH chia sẻ)
**4. Commitments & agreements** (cả 2 phía)
**5. Open questions** (chưa answer)
**6. Next steps** (owner + due)

## Bước 3: Email Follow-up Sinh Tự Động
Subject: "Recap & Next Steps — [meeting topic]"

Body:
```
Cảm ơn anh chị dành 30 phút sáng nay.

Recap nhanh các điểm chính:
• Pain ưu tiên: [1, 2, 3]
• Anh đã share insight về [topic]
• Em đã chia sẻ [solution / case study]

Next steps:
• [Owner mình] — [Action] — [Date]
• [Owner KH] — [Action] — [Date]

Anh confirm helping em book [next meeting].

Em đính kèm [case study / proposal preview].
```

## Bước 3.5: AI-extracted Insights
Từ transcript auto-extract:
- Buying signals (positive language)
- Concerns/objections raised
- Competitor mentions
- Decision criteria revealed
- Stakeholder names mentioned

## Bước 4: CRM Log Tự Động
Activity record có:
- Date / type / duration
- Attendees linked
- Summary body
- Next step due date
- Stage advancement nếu có
- Risk flag nếu detect concern

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Gong/Chorus MCP: transcript + AI summary
- Otter/Fireflies MCP: transcribe + summarize
- Gmail/Outlook MCP: gửi email follow-up
- Salesforce/HubSpot MCP: log activity
- Slack MCP: post to deal channel

**Fallback API:**
```python
# Auto-summary với OpenAI
import openai
transcript = get_gong_transcript(call_id)
summary = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "system", "content": 
        "Tóm tắt sales call thành 6 phần: topics, pain, agreements, questions, next steps."},
        {"role": "user", "content": transcript}]
).choices[0].message.content

# Send email
send_email(recipient=prospect, subject="Recap", body=summary)
# Log CRM
sf.Task.create({"Subject": "Discovery call", "WhatId": opp_id,
    "Description": summary, "ActivityDate": today})
```

## Bước 6: Output Format
- **File 1**: `meeting_summary_<date>.md` — 6 phần đầy đủ
- **File 2**: `followup_email_<date>.md` — email ready send
- **File 3**: `crm_activity.json` — JSON sẵn import CRM
- **File 4**: `insights_extracted.md` — buying signals / concerns
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Summary <500 từ
- [ ] Next step có owner + due date
- [ ] Email gửi trong 2h
- [ ] CRM logged trong 4h
- [ ] Insight buying signal tagged
- [ ] Risk flag nếu có concern
- [ ] Cross-functional share nếu cần
