---
name: sales-distributor-onboarding
description: |
  Onboarding nhà phân phối/đại lý mới 30-60-90 ngày — training, certification, first deal coaching. Trigger phrases: "onboard distributor", "onboarding đại lý mới", "đào tạo đối tác mới", "distributor 30 60 90", "channel onboarding", "kích hoạt distributor", "partner enablement", "ramp up distributor", "đào tạo nhà phân phối", "first deal coaching partner". Output là Markdown plan + Excel certification tracker + slide training.
---

# Distributor/Partner Onboarding (30-60-90)

## Mục Tiêu
Đảm bảo distributor mới đạt first deal trong 60 ngày và 100K ARR trong 90 ngày bằng plan onboarding cấu trúc — tránh "sign and pray".

## Khi Nào Dùng
- Distributor mới ký
- Reseller agreement mới
- SI/agency partner kích hoạt
- Re-engage partner đang inactive
- Cross-region expansion partner

## Bước 1: Day 0-30 — Foundation

**Week 1**:
- Welcome call + kickoff
- Tài liệu access (deck, demo env, brand asset)
- Partner portal account setup
- Slack channel chung
- Champion mapping mỗi bên

**Week 2-3**:
- Sales training (2 ngày): pitch, demo, objection
- Product certification level 1 (online quiz)
- Joint shadow call: partner xem AE mình close

**Week 4**:
- Roleplay pitch & demo (record)
- Certification level 2 (hands-on demo)
- Marketing kit + co-branded asset

## Bước 2: Day 31-60 — First Deal

- Partner identifies 5-10 prospect (joint review)
- Joint outreach campaign
- Joint discovery call (mình + partner)
- First demo: partner lead, mình support
- First proposal review (mình QA)
- First close target: Day 60

Goal: 1 deal closed (small ok) trong 60 ngày.

## Bước 3: Day 61-90 — Independence

- Partner solo discovery + demo
- Mình standby phone-a-friend
- Co-marketing webinar / case study
- QBR 1 partner-mình
- Quota commit Year 1 set

## Bước 4: Certification System
3 tier:
- **Bronze** (Day 30): online quiz, basic pitch
- **Silver** (Day 60): demo certified, 1 deal closed
- **Gold** (Day 90): solo close, customer reference

Re-certify mỗi 12 tháng. Tier link với margin (vd Gold = +5% margin).

## Bước 5: Ramp Quota
- Month 1: 0%
- Month 2: 25%
- Month 3: 50%
- Month 4+: 100%

Partner under ramp: weekly checkpoint.

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Allbound/Salesforce PRM MCP: partner portal
- LMS MCP (Lessonly/Mindtickle): certification
- Slack MCP: partner channel
- Calendar MCP: training + checkpoint
- Drive MCP: shared sales kit

**Fallback API:**
```python
# Track partner certification + alert ramp
def track_ramp(partner_id):
    progress = get_lms_progress(partner_id)
    deals = sf.query(f"SELECT Id FROM Opportunity WHERE Partner__c='{partner_id}' AND IsWon=true")
    deal_count = len(deals["records"])
    days_onboarded = (date.today() - partner["start_date"]).days
    
    if days_onboarded > 60 and deal_count == 0:
        alert_channel_manager(partner_id, "BEHIND RAMP")
```

## Bước 7: Output Format
- **File 1**: `partner_onboard_30_60_90.md` — plan đầy đủ
- **File 2**: `certification_tracker.xlsx` — partner × tier × status
- **File 3**: `partner_training_deck.pptx` — 30 slide training
- **File 4**: `first_deal_coaching.md` — coaching playbook
- **File 5**: `partner_ramp_dashboard.xlsx` — track 30/60/90
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Champion mapped 2 bên
- [ ] Certification 3 tier rõ
- [ ] First deal target 60 ngày
- [ ] Ramp quota có
- [ ] Weekly checkpoint cadence
- [ ] QBR 90-day in place
