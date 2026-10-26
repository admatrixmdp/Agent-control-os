---
name: sales-followup-cadence
description: |
  Cadence follow-up 14 ngày multi-touch (email + call + LinkedIn) cho lead chưa response, tối ưu reply rate. Trigger phrases: "cadence follow up", "follow-up sequence", "14-day cadence", "multi-touch follow up", "nurture cadence sales", "follow up khách lạnh", "sequence outreach", "cadence cho SDR", "follow-up touchpoint", "build cadence sales". Output là Markdown cadence + Excel sequence schedule.
---

# Multi-channel Follow-up Cadence (14 days)

## Mục Tiêu
Tăng reply rate từ 5% (1 touch) → 15-20% (multi-touch cadence) bằng chuỗi 8 touch trong 14 ngày qua email + call + LinkedIn với angle khác nhau mỗi touch.

## Khi Nào Dùng
- Cold outbound mới
- Lead inbound chưa response sau 48h
- KH no-show meeting
- Reactivate lead cũ
- Penetrate new account (multiple contacts)

## Bước 1: 8-Touch Cadence Template

| Day | Channel | Type | Angle |
|---|---|---|---|
| 0 | Email | Intro | Pain + soft CTA |
| 1 | LinkedIn | View profile | Familiarity |
| 3 | Phone | Cold call | Voicemail + text |
| 5 | Email | Bump | Case study same-industry |
| 7 | LinkedIn | Connect note | Reference content |
| 9 | Phone | Call attempt 2 | Different time |
| 12 | Email | Different angle | Different pain or PoV |
| 14 | Email | Breakup | Polite goodbye |

## Bước 2: Mỗi Touch Có Angle Khác

**Touch 1 (Email)**: pain ưu tiên #1
**Touch 5 (Email)**: peer proof + case study
**Touch 7 (LinkedIn)**: reference recent post
**Touch 12 (Email)**: different pain hoặc industry trend
**Touch 14 (Breakup)**: ego + yes/no question

Tránh "just following up" = lười + spam.

## Bước 3: Personalization 2 Tầng
- **Layer 1 (cadence-level)**: theo industry, persona, pain
- **Layer 2 (contact-level)**: 1-2 dòng cá nhân riêng (LinkedIn post, công ty news)

Touch 1, 5, 12 PHẢI có layer 2. Còn lại có thể batch.

## Bước 4: Response Branch
Khi KH response:
- **Positive**: pause cadence, AE take over
- **Negative**: tag "not now" → 90 day nurture
- **Out of office**: pause 7 ngày
- **Not the right person**: ask referral → restart cadence với contact mới
- **Unsubscribe**: hard stop + flag

## Bước 5: Performance Tracking
KPI mỗi cadence:
- Open rate per touch
- Reply rate per touch
- Meeting booked rate
- Optimum touch để response (touch 3-5 thường)
- Time-to-reply

A/B test subject line, CTA, send time.

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Outreach/Salesloft/Apollo MCP: native cadence
- Gmail/Outlook MCP: send + track open/click
- LinkedIn MCP: profile view + connect + message
- Phone (Aircall/Dialpad) MCP: log call attempt
- Salesforce MCP: sync activity

**Fallback API:**
```python
# Outreach cadence enroll
import requests
r = requests.post("https://api.outreach.io/api/v2/sequenceStates",
    headers={"Authorization": f"Bearer {token}"},
    json={"data": {"type": "sequenceState",
        "relationships": {
            "sequence": {"data": {"type": "sequence", "id": seq_id}},
            "prospect": {"data": {"type": "prospect", "id": prosp_id}}}}})
```

## Bước 7: Output Format
- **File 1**: `cadence_14day.md` — 8 touch schedule + script mỗi touch
- **File 2**: `cadence_schedule.xlsx` — sequence list with timing + owner
- **File 3**: `cadence_email_templates.md` — 5 email body
- **File 4**: `cadence_performance.xlsx` — track KPI weekly
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 8 touch trong 14 ngày, multi-channel
- [ ] Mỗi touch có angle khác (không "just following up")
- [ ] Layer 1 + Layer 2 personalize
- [ ] Response branch rõ ràng
- [ ] Unsubscribe hard stop
- [ ] A/B test 2 variants
- [ ] Performance review weekly
