---
name: sales-churn-risk-detector
description: |
  Phát hiện sớm KH có nguy cơ churn qua signal usage, engagement, sentiment để CSM/AM can thiệp. Trigger phrases: "phát hiện churn", "churn risk", "early warning churn", "KH nguy cơ rời", "phát hiện sớm khách hàng churn", "churn signal", "predictive churn", "churn alert", "rủi ro mất khách", "churn detector". Output là Excel risk dashboard + Markdown playbook can thiệp.
---

# Customer Churn Risk Detector

## Mục Tiêu
Phát hiện KH có nguy cơ churn 60-90 ngày trước hết hạn qua 12 signal, gửi alert CSM can thiệp đúng lúc — giảm churn rate 30-50%.

## Khi Nào Dùng
- CSM team quản lý >50 KH
- Renewal đang đến 90 ngày tới
- NPS giảm cụm KH
- Sau M&A KH có CEO mới
- Sau khi mất 2-3 KH lớn liên tiếp

## Bước 1: Define 12 Risk Signal

**Usage signals (4)**:
1. Active user giảm >30% MoM
2. Feature core usage <50% baseline
3. Login >14 ngày không
4. API call giảm >40%

**Engagement signals (4)**:
5. Support ticket >5/tháng (tăng)
6. NPS <30 hoặc giảm
7. QBR cancel/no-show
8. Champion leave công ty

**Commercial signals (2)**:
9. Payment late >30 ngày
10. Discount request mid-contract

**External signals (2)**:
11. KH layoff/M&A
12. Competitor sign deal (PR news)

## Bước 2: Weight & Score
Mỗi signal: weight 1-5 theo severity.
Score = sum(weight × triggered)
- 0-5: Green (low risk)
- 6-12: Yellow (monitor)
- 13-20: Orange (intervention)
- >20: Red (escalation CRO)

Realtime refresh qua dashboard.

## Bước 3: Intervention Playbook per Risk

**Yellow**: CSM email "check-in" + offer training
**Orange**: CSM call + QBR sớm + RCA + action plan
**Red**: CSM + AE + Manager joint call + executive sponsor + retention offer

Mỗi level có template + SLA hành động.

## Bước 4: Save Track (Outcome theo dõi)
Sau intervention 30/60/90 ngày:
- Saved (signal về Green): success
- Still risk: escalate higher level
- Churned: post-mortem

Aggregate save rate quarterly.

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Gainsight/ChurnZero MCP: native risk engine
- Salesforce MCP: customer health field
- Product analytics MCP (Amplitude/Mixpanel): usage data
- Slack MCP: alert CSM realtime
- Zendesk MCP: support ticket signal

**Fallback API:**
```python
# Churn risk score
def churn_score(customer):
    score = 0
    if customer["mau_decline_pct"] > 30: score += 5
    if customer["core_feature_usage"] < 0.5: score += 4
    if customer["days_since_login"] > 14: score += 3
    if customer["nps_latest"] < 30: score += 4
    if customer["champion_active"] == False: score += 5
    if customer["payment_late_days"] > 30: score += 3
    # ... 
    return score

# Alert if Red
if score > 20:
    requests.post(SLACK_WEBHOOK, json={"text":
        f"🚨 RED RISK: {customer['name']} score {score}"})
```

## Bước 6: Output Format
- **File 1**: `churn_risk_dashboard.xlsx` — list KH + score + trend
- **File 2**: `churn_signal_definitions.md` — 12 signal rules
- **File 3**: `intervention_playbook.md` — 4 level + template + SLA
- **File 4**: `save_track_log.xlsx` — outcome 30/60/90 ngày
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 12 signal có data source
- [ ] Weight calibrated với historical churn
- [ ] Refresh daily/realtime
- [ ] SLA hành động mỗi level
- [ ] Save rate track quarterly
- [ ] Quarterly recalibrate weights
