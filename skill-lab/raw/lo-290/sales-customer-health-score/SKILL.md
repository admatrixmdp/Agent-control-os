---
name: sales-customer-health-score
description: |
  Health score KH B2B kết hợp usage, sentiment, engagement, commercial để CSM ưu tiên action. Trigger phrases: "customer health score", "chấm điểm sức khoẻ KH", "health score B2B", "đánh giá khách hàng hiện hữu", "monitor account health", "health card customer", "AM scorecard", "build health score", "CSM dashboard health", "customer success metric". Output là Excel scoring model + dashboard.
---

# Customer Health Score Builder

## Mục Tiêu
Tạo health score 0-100 cho 50-500 KH dùng để CSM ưu tiên thời gian, leadership monitor portfolio, và trigger workflow tự động — green/yellow/red.

## Khi Nào Dùng
- CSM/AM portfolio >50 KH
- Lead chỉ số NRR / GRR
- Trước annual planning
- Implement Gainsight/ChurnZero
- Khi Board hỏi "tình hình KH thế nào"

## Bước 1: 4 Trục Health
- **Usage (25 điểm)**: feature adoption, DAU/MAU, depth
- **Engagement (25 điểm)**: QBR attendance, email, training
- **Sentiment (25 điểm)**: NPS, CSAT, support ticket sentiment
- **Commercial (25 điểm)**: payment, expansion signal, renewal commit

Tổng /100.

## Bước 2: Định lượng mỗi Sub-score

**Usage**:
- Active user % vs license: 10
- Core feature 80% adoption: 10
- Integration alive: 5

**Engagement**:
- QBR attended 4/4 quý: 10
- Champion meet quarterly: 8
- Webinar/training: 7

**Sentiment**:
- NPS >50: 15, 30-50: 10, <30: 0
- Support ticket trend: 10

**Commercial**:
- Payment on-time: 10
- Multi-product: 5
- Expansion signal: 5
- Renewal commit: 5

## Bước 3: Classification
- 80-100: Green (advocate)
- 60-79: Yellow (monitor)
- 40-59: Orange (intervene)
- <40: Red (escalate)

Each classification có default action.

## Bước 4: Visualization Dashboard
- Heat map portfolio
- Trend line per KH 12 tuần
- Distribution histogram
- Alert list change >10 điểm WoW

CSM 1-1 weekly dùng dashboard.

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Gainsight/Totango MCP: native health
- Salesforce MCP: custom health field
- Product analytics (Mixpanel/Amplitude) MCP: usage data
- Zendesk MCP: support sentiment
- Looker/Tableau MCP: dashboard

**Fallback API:**
```python
# Health score calculation
def health_score(c):
    usage = (c["active_users"]/c["licenses"])*10 + \
            (c["core_feature_adoption"]>0.8)*10 + (c["integration_alive"])*5
    engagement = (c["qbr_attended_yr"]>=4)*10 + (c["champion_meet_quarter"])*8 + (c["training_yr"]>=2)*7
    sentiment = (15 if c["nps"]>50 else 10 if c["nps"]>30 else 0) + \
                (10 - min(c["ticket_count_3mo"], 10))
    commercial = (c["payment_ontime"])*10 + (c["product_count"]>=2)*5 + \
                 (c["expansion_signal"])*5 + (c["renewal_commit"])*5
    return usage + engagement + sentiment + commercial
```

## Bước 6: Output Format
- **File 1**: `health_score_model.xlsx` — 50+ KH, score, sub-score, trend
- **File 2**: `health_definitions.md` — định nghĩa rõ ràng
- **File 3**: `health_dashboard.pptx` — exec view monthly
- **File 4**: `csm_action_playbook.md` — action mỗi classification
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 4 trục cân bằng
- [ ] Sub-score có data source
- [ ] Refresh weekly minimum
- [ ] Classification rõ default action
- [ ] Dashboard exec view sẵn sàng
- [ ] Quarterly recalibrate
