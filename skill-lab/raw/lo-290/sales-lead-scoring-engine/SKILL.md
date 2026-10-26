---
name: sales-lead-scoring-engine
description: |
  Engine chấm lead nâng cao kết hợp rule-based + AI signal (intent, fit, engagement) sinh score 0-100 sort priority. Trigger phrases: "lead scoring engine", "chấm điểm lead AI", "advanced lead scoring", "AI lead score", "scoring model B2B", "rank lead theo intent", "engine chấm lead", "scoring nâng cao", "predictive lead scoring", "ưu tiên lead tự động". Output là Excel scoring model + Python script + dashboard.
---

# Advanced Lead Scoring Engine (Rule + AI)

## Mục Tiêu
Tự động chấm lead 0-100 kết hợp Fit score (ICP match) + Intent score (behavioral + 3rd party intent) để SDR luôn work top 20% lead priority cao nhất, tăng conversion 2-3x.

## Khi Nào Dùng
- Volume lead >500/tháng quá tải SDR
- Conversion lead-to-meeting <5%
- Có 3rd party intent (Bombora, G2, 6sense)
- Cần ABM scoring cho top account
- Sau audit lead quality

## Bước 1: Hai trục Fit + Intent (2x2 Matrix)

**Fit Score (0-50)** — ICP match:
- Industry match: 10
- Company size: 10
- Geo: 5
- Tech stack: 10
- Title/role: 15

**Intent Score (0-50)** — buying signal:
- High-intent action: demo request 25, pricing 15, ROI calc 10
- Website behavior: 5+ visit 10, time on site >5min 5
- Email engagement: click 5, multi open 3
- 3rd party intent: G2 review 15, Bombora topic 10
- Recent trigger: funding 10, exec hire 5

**Quadrant action**:
- Hot (Fit>30 + Intent>30): SDR call trong 1h
- Warm (Fit>30 + Intent<30): nurture + SDR email 24h
- Speculative (Fit<30 + Intent>30): SDR review + qualify carefully
- Cold (Fit<30 + Intent<30): marketing nurture / drop

## Bước 2: Negative Scoring (Disqualify)
Hard reject (set to 0):
- Competitor domain
- Free email + small role
- Geo not supported
- Student / .edu

Soft penalty (-X):
- Title intern / assistant: -20
- Bounced email: -30
- Unsubscribed: -100

## Bước 3: Model Training (nếu có data)
Nếu >12 tháng data:
- Feature: 30+ feature mỗi lead
- Label: converted to closed-won (Y/N)
- Model: Random Forest / XGBoost
- Validate: precision@top20% lead

Hybrid: rule-based + model-based, weight 50:50.

## Bước 4: Routing Rule
Sau scoring:
- Hot → SDR queue auto-call trong 1h
- Warm → SDR email queue 24h
- Speculative → SDR review hourly
- Cold → Marketing nurture sequence

Score refresh: realtime (event-based) cho behavior, daily cho fit.

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- HubSpot/Marketo MCP: lead scoring native
- 6sense/Demandbase MCP: AI intent data
- Salesforce MCP: lead routing rules
- Slack MCP: alert hot lead realtime
- Bombora MCP: intent topic feed

**Fallback API:**
```python
# Hybrid scoring engine
def score(lead, intent_data):
    fit = 0
    if lead["industry"] in ICP_INDUSTRY: fit += 10
    if lead["size"] in ICP_SIZE: fit += 10
    if any(t in lead["title"] for t in ["VP","Director","Head"]): fit += 15
    # ... 
    intent = 0
    if "demo_request" in lead["events"]: intent += 25
    if intent_data.get("g2_review_visit"): intent += 15
    if lead["funding_30d"]: intent += 10
    # Negative
    if any(c in lead["email"] for c in COMPETITOR_DOMAINS): return 0
    return min(fit + intent, 100)

for lead in leads:
    s = score(lead, get_intent(lead["company_id"]))
    update_crm_score(lead["id"], s)
```

## Bước 6: Output Format
- **File 1**: `scoring_rules.xlsx` — 40 rules + weight + negative
- **File 2**: `scoring_engine.py` — script tính score
- **File 3**: `scoring_dashboard.xlsx` — leaderboard hot/warm/cold
- **File 4**: `model_validation.md` — accuracy/precision report
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Fit + Intent 2 trục riêng (không gộp)
- [ ] Negative scoring loại hết noise
- [ ] Refresh realtime + daily
- [ ] Routing rule trigger SDR action
- [ ] Hot lead SLA 1h
- [ ] Recalibrate quarterly với data conversion
