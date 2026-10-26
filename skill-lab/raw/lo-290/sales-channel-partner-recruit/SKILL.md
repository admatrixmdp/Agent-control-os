---
name: sales-channel-partner-recruit
description: |
  Tuyển đối tác kênh (reseller/distributor/agency) với criteria, outreach, vetting và onboard plan. Trigger phrases: "tuyển đối tác kênh", "channel partner recruit", "recruit reseller", "tuyển distributor", "partner outreach", "vetting đối tác", "channel partner criteria", "tuyển đại lý", "build channel program", "channel sales recruitment". Output là Markdown playbook + Excel partner pipeline.
---

# Channel Partner Recruitment

## Mục Tiêu
Tuyển 5-20 đối tác kênh chất lượng (reseller/SI/agency) đạt 80%+ active selling trong 6 tháng, đóng góp >20% revenue mới — không quantity over quality.

## Khi Nào Dùng
- Mở vertical/region mới chưa có direct sales
- Scale revenue indirect 20-40%
- Sản phẩm cần local SI implement
- Partnership program launch
- Replace partner under-performing

## Bước 1: Partner Profile (ICP đối tác)
Định nghĩa rõ partner lý tưởng:
- Type: Reseller, SI, Agency, OEM, Referral
- Size: 10-100 NV
- Existing portfolio: complementary (không cạnh tranh)
- Customer base: match ICP mình target
- Region/vertical coverage
- Sales motion: outbound mature
- Technical certification track record
- Financial health (avoid struggling)

## Bước 2: Source Partner Candidates (50-100 list)
- Industry events + LinkedIn
- Recommend từ KH (ask "ai integrate cho anh?")
- Competitor partner directory (target nudge sang mình)
- Partner directory: AWS marketplace, Microsoft, Salesforce AppExchange
- Trade association
- Referral từ existing partner

## Bước 3: Vetting 6 Checkpoint
1. Discovery call (45 phút)
2. Capability audit (case study, team, certification)
3. Reference check (3 KH của partner)
4. Financial check (revenue, runway)
5. Commercial alignment (margin, exclusivity)
6. Legal review

3 strike rule: fail 3+ → reject.

## Bước 4: Outreach & Pitch
Outreach personalized:
- "Em theo dõi case study X bên anh chị làm. Em đề xuất 30 phút explore channel partnership."

Pitch deck partner (15 slide):
- Market opportunity
- Why us vs competitors
- Partner economics (margin, MDF, comp)
- Support model (training, marketing, lead share)
- Partnership tier (Silver/Gold/Platinum)

## Bước 5: Commercial Terms
- Margin: 20-35% (volume tier)
- Deal registration (lock deal cho partner đầu tiên submit)
- Lead share % với mình
- MDF (Marketing Development Fund) co-funded
- Exclusivity (rare, chỉ Platinum)
- Annual commit quota

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- LinkedIn MCP: source + research partner
- Salesforce PRM/Allbound MCP: partner CRM
- WebFetch: research partner case study
- DocuSign MCP: partner agreement
- Slack MCP: partner channel ongoing comm

**Fallback API:**
```python
# Score partner candidate
def score_partner(p):
    s = 0
    if p["years_business"] >= 3: s += 10
    if p["customer_base_overlap_icp"] > 0.5: s += 20
    if p["technical_team_size"] >= 5: s += 10
    if p["existing_certs"]: s += 10
    if p["revenue_yr"] > 1_000_000: s += 10
    if not p["competing_product"]: s += 20
    return s
```

## Bước 7: Output Format
- **File 1**: `partner_recruit_playbook.md` — process 6 bước
- **File 2**: `partner_pipeline.xlsx` — 50+ candidate scored
- **File 3**: `partner_pitch_deck.pptx` — 15 slide
- **File 4**: `partner_agreement_template.docx` — commercial terms
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Partner ICP rõ ràng
- [ ] Vetting 6 checkpoint thực hiện đủ
- [ ] Reference check 3 KH
- [ ] Commercial term có deal reg
- [ ] Tier program (Silver/Gold/Platinum)
- [ ] Onboard plan 30-60-90 sẵn sàng
