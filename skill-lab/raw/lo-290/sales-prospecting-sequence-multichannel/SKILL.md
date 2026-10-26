---
name: sales-prospecting-sequence-multichannel
description: |
  Cadence prospecting đa kênh 21 ngày — email + LinkedIn + call + video personalized với branching logic. Trigger phrases: "multichannel sequence", "prospecting cadence", "outbound multichannel", "sequence 21 ngày", "cadence email LinkedIn call", "outreach multi-touch", "đa kênh prospecting", "B2B sequence builder", "video sales sequence", "personalized cadence". Output là Markdown cadence + Excel schedule + script library.
---

# Multi-channel Prospecting Sequence (21 Days)

## Mục Tiêu
Tăng meeting-booked rate từ 1% (single channel) → 5-8% (multi-channel) bằng cadence 12 touch 21 ngày qua email + LinkedIn + call + video với branching logic theo behavior.

## Khi Nào Dùng
- Outbound enterprise (deal >$50K)
- ABM top 100 account
- Re-engage cold list lớn
- Launch campaign new product/vertical
- SDR scale prospecting

## Bước 1: 12-Touch Cadence 21 Days

| Day | Channel | Type |
|---|---|---|
| 0 | Email | Personalized intro |
| 1 | LinkedIn | View + like recent post |
| 3 | Phone | Cold call + VM |
| 4 | LinkedIn | Connect note |
| 6 | Email | Bump with case study |
| 8 | Video | 60s Loom video personalized |
| 10 | Phone | Call attempt 2 |
| 13 | LinkedIn DM | Soft CTA share resource |
| 15 | Email | Different angle pain |
| 17 | Phone | Voicemail final |
| 19 | LinkedIn | Comment on their post (genuine) |
| 21 | Email | Breakup polite |

## Bước 2: Video Personalization (Loom)
Touch 8 — video 60s:
- Hook 5s: nhắc tên + công ty
- Insight 30s: 1 quan sát từ website/LinkedIn
- Solution tie 15s: how we can help
- CTA 10s: book link
→ Reply rate video 2-3x email text.

## Bước 3: Branching Logic
Behavior-based:
- **Opened email không reply** → priority call Day 4-6
- **Visited pricing page** → priority call ngay + skip Day 13
- **Replied negative** → tag "not now" → 90 day pause
- **Replied positive** → exit cadence, AE take over
- **Bounced email** → find alternate contact same account

## Bước 4: Multi-thread Same Account
Touch 7 email khác contact:
- "Em đã reach out [original contact], chưa connect được. Có lẽ anh là người phù hợp hơn cho topic [X]?"
- 2-3 contact per account tối đa
- Track không spam cùng person

## Bước 5: A/B Test Continuous
Mỗi 50 sequence test:
- Subject line
- CTA softness (book link vs question)
- Tone (formal vs casual)
- Channel order (call-first vs email-first)

Variant tốt → roll-out.

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Outreach/Salesloft/Apollo MCP: cadence engine
- Loom MCP: video send
- LinkedIn MCP: profile action + DM
- Aircall/Dialpad MCP: phone log
- Salesforce MCP: activity sync
- Slack MCP: AE alert on positive reply

**Fallback API:**
```python
# Outreach enroll prospect
import requests
def enroll_in_cadence(prospect_id, sequence_id):
    r = requests.post("https://api.outreach.io/api/v2/sequenceStates",
        headers={"Authorization": f"Bearer {token}"},
        json={"data": {"type": "sequenceState",
            "relationships": {
                "sequence": {"data": {"type": "sequence", "id": sequence_id}},
                "prospect": {"data": {"type": "prospect", "id": prospect_id}}}}})
    return r.json()

# Branching based on behavior
events = get_engagement(prospect_id)
if any(e["type"] == "pricing_page_view" for e in events):
    schedule_priority_call(prospect_id)
```

## Bước 7: Output Format
- **File 1**: `sequence_21day.md` — 12 touch + script + branching
- **File 2**: `sequence_schedule.xlsx` — auto-trigger calendar
- **File 3**: `email_templates.md` — 5 email body
- **File 4**: `video_script_template.md` — Loom 60s script
- **File 5**: `cadence_performance.xlsx` — track reply, meeting, branch outcome
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 12 touch trải 21 ngày
- [ ] 4 channel ít nhất (E, LI, Call, Video)
- [ ] Branching rule realtime
- [ ] Multi-thread 2-3 contact/account
- [ ] A/B test continuous
- [ ] Unsubscribe respect hard
