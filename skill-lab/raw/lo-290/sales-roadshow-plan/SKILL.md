---
name: sales-roadshow-plan
description: |
  Plan roadshow tỉnh — chuỗi 5-15 thành phố gặp đại lý/khách hàng, agenda, logistics, KPI. Trigger phrases: "plan roadshow", "roadshow tỉnh", "tour đại lý", "kế hoạch roadshow", "tổ chức roadshow B2B", "field event plan", "regional roadshow", "sales tour tỉnh", "channel partner roadshow", "agency tour Việt Nam". Output là Excel logistics + Markdown agenda + PPT deck.
---

# Sales Roadshow Planner (5-15 Cities)

## Mục Tiêu
Lên kế hoạch roadshow tỉnh 5-15 thành phố trong 4-6 tuần, gặp 200-1000 đại lý/KH, kết hợp brand-build + lead gen + relationship — đạt cost-per-lead <$50.

## Khi Nào Dùng
- Launch sản phẩm mới ra tỉnh
- Recruit đại lý cấp 2 batch lớn
- Brand activation regional
- Re-engage đại lý cũ sau COVID
- Educate channel về policy mới

## Bước 1: City Selection
Score 15-30 thành phố theo:
- Market size (population, GDP/capita)
- Existing distributor coverage
- Strategic priority (vertical)
- Logistics cost (flight/drive)
- Past event ROI

Pick top 5-15.

## Bước 2: Agenda Mỗi Stop (4-6 giờ)

**Buổi sáng (registration + main session 9-12h)**:
- 9:00 Welcome + coffee
- 9:30 Opening keynote (Vision + Market opportunity)
- 10:15 Product demo + Q&A
- 11:00 Local case study (đại lý cùng tỉnh đã thành công)
- 11:30 Policy + commercial terms
- 12:00 Networking lunch

**Buổi chiều (1-on-1 + signing 13-17h)**:
- 13:00 1-on-1 meeting potential dealer
- 15:00 Contract signing ceremony
- 16:00 Photo + PR
- 17:00 Wrap

## Bước 3: Logistics Checklist
- Venue (hotel ballroom 100-300 seat)
- AV (mic, projector, internet, recording)
- Catering (lunch + 2 coffee break)
- Print material (one-pager, contract, brochure)
- Booth setup
- Local team coordination
- Hotel transport speaker
- Photographer + video
- PR + press release

Budget breakdown each city: $5-15K.

## Bước 4: Pre-event Marketing
- LinkedIn event create + boost
- Local Facebook ad
- Direct invite top 200 dealer existing
- Local KOL partner
- Press release local media
- Email campaign 4-2-1 tuần trước

Target: 60-80% RSVP rate, 80% show-up.

## Bước 5: KPI & Tracking
Per stop:
- # attendees (target 100-200)
- # new dealer signed (target 10-20)
- # leads collected
- # 1-on-1 meeting booked
- ARR signed at event
- CPL = total cost / leads

Total roadshow KPI rollup weekly.

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Calendar MCP: book + sync team schedule
- Eventbrite/Luma MCP: registration + check-in
- Salesforce MCP: lead capture + tag campaign
- Slack MCP: regional team coordination
- WebSearch: venue rating + booking
- WhatsApp Business MCP: local dealer comm

**Fallback API:**
```python
# Eventbrite create event for each city
import requests
for city in cities:
    r = requests.post("https://www.eventbriteapi.com/v3/events/",
        headers={"Authorization": f"Bearer {token}"},
        json={"event": {"name": {"text": f"Roadshow {city}"},
            "start": {"timezone": "Asia/Ho_Chi_Minh", "utc": city["date"]},
            "capacity": 200, "venue_id": city["venue_id"]}})
    city["event_id"] = r.json()["id"]
```

## Bước 7: Output Format
- **File 1**: `roadshow_master_plan.xlsx` — 15 city × timeline × budget × KPI
- **File 2**: `roadshow_agenda.md` — agenda chuẩn each stop
- **File 3**: `roadshow_deck.pptx` — 30 slide keynote
- **File 4**: `roadshow_logistics_checklist.md` — 50-item checklist
- **File 5**: `roadshow_lead_tracker.xlsx` — track lead + conversion
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] City selection có data-driven
- [ ] Agenda 4-6h fit attention span
- [ ] Budget per city <$15K
- [ ] RSVP rate >60%
- [ ] KPI per stop track real-time
- [ ] Post-event follow-up 7 ngày
