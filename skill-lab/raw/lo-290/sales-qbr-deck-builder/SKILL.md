---
name: sales-qbr-deck-builder
description: |
  Tạo Quarterly Business Review deck cho KH — value delivered, KPI, roadmap, expansion opportunity. Trigger phrases: "QBR deck", "quarterly business review", "tạo deck QBR khách hàng", "QBR template", "review hàng quý KH", "QBR slide", "Q1 review customer", "QBR presentation", "QBR CSM", "build QBR deck". Output là PPT 10-12 slide + Excel KPI tracker.
---

# Quarterly Business Review Deck Builder

## Mục Tiêu
Tạo QBR deck chuyên nghiệp 10-12 slide cho meeting hàng quý với KH, chứng minh value đã deliver + plan tiếp + expansion opportunity — tăng renewal rate + expansion ARR.

## Khi Nào Dùng
- Top 20 KH lớn ARR >$50K
- Quarterly cadence cho enterprise
- Trước renewal 90 ngày (làm QBR khởi động conversation)
- Sau executive change phía KH
- Khi launch feature/module mới

## Bước 1: Cấu trúc 11 Slide

**1. Cover** — logo 2 bên, KH + date + attendees
**2. Agenda** — 5 mục
**3. Last quarter recap** — actions từ QBR trước
**4. Value delivered** — 3-5 metric với baseline → result
**5. Adoption snapshot** — usage trend 12 tuần
**6. Wins** — 2-3 case story trong quý
**7. Roadmap** — feature sắp ra liên quan KH
**8. Areas of opportunity** — expansion / upsell
**9. Champion ask** — what we need from KH
**10. Next quarter plan** — 3-5 priority có owner
**11. Q&A**

## Bước 2: Value Delivered (Slide quan trọng nhất)
Bảng 3 cột:
- KPI (vd hours saved, deal closed)
- Baseline (trước khi dùng tool)
- Result (sau khi dùng)
- $$ value ước lượng

Vd: "Time saved 40h/tuần × $50/h × 52w = $104K/năm"

## Bước 3: Expansion Story (subtle, not pushy)
- Roadmap: 1-2 feature KH chưa unlock
- Usage data: cho thấy KH gần limit
- Peer story: KH cùng size đã upgrade thấy ROI
- Soft CTA: "Em đề xuất review sâu hơn — book follow-up?"

## Bước 4: Champion Ask
3 thứ CSM cần từ KH:
- Reference call / case study consent
- Feedback session với Product
- Intro internal cho team chưa adopt

Trao đổi 2 chiều, không 1 chiều.

## Bước 5: Pre-QBR Prep Checklist
- KPI data pull 2 tuần trước
- Champion review draft 1 tuần trước
- Attendee list confirm 3 ngày trước
- Backup file + room test ngày D

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce/HubSpot MCP: pull account data, opp pipeline
- Product analytics MCP: usage data tự động
- Gainsight MCP: health data + adoption
- PPT/Slides MCP: tạo deck từ template
- Calendar MCP: schedule QBR + room

**Fallback API:**
```python
# Pull data + render PPT
from pptx import Presentation
usage = get_amplitude_data(customer_id, 90)
revenue = get_salesforce_data(customer_id)
ppt = Presentation("qbr_template.pptx")
ppt.slides[3].placeholders[1].text = f"Time saved: {usage['hours_saved']}h"
ppt.slides[4].shapes.add_chart(...)
ppt.save(f"QBR_{customer}_{quarter}.pptx")
```

## Bước 7: Output Format
- **File 1**: `qbr_<customer>_<quarter>.pptx` — 11 slide đầy đủ
- **File 2**: `qbr_kpi_tracker.xlsx` — quarter-on-quarter KPI
- **File 3**: `qbr_prep_checklist.md` — pre/during/post
- **File 4**: `qbr_followup_email.md` — gửi 24h sau
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Value delivered có số liệu thật
- [ ] Champion review draft trước
- [ ] EB attend được mời
- [ ] Expansion story subtle (không pushy)
- [ ] Champion ask 2 chiều
- [ ] Follow-up email trong 24h
