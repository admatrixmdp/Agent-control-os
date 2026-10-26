---
name: sales-renewal-playbook
description: |
  Playbook gia hạn KH B2B với cadence 90/60/30/0 ngày, health check, value review và uplift pricing strategy. Trigger phrases: "playbook renewal", "gia hạn hợp đồng KH", "renewal strategy", "kế hoạch tái ký", "uplift giá renewal", "tránh churn renewal", "QBR renewal", "tái ký SaaS", "renewal cadence", "chăm sóc gia hạn". Output là Markdown playbook + Excel renewal tracker + email templates.
---

# Renewal Playbook (90/60/30/0 days)

## Mục Tiêu
Tăng renewal rate >95% và NRR >115% bằng cadence chủ động 90 ngày trước hết hạn, value review định kỳ và uplift pricing có lý do business.

## Khi Nào Dùng
- CSM/AM quản lý portfolio >50 KH
- KH SaaS subscription sắp hết hạn
- Multi-year contract năm cuối
- Sau M&A/CEO change phía KH
- Khi rate uplift áp dụng toàn portfolio

## Bước 1: Renewal Health Check (Day -90)
Pull data:
- Usage trend 6 tháng (active user, feature adoption)
- Support ticket volume + sentiment
- NPS / CSAT score
- Champion còn ở công ty không
- Trigger (M&A, layoff, new CEO)

Chấm Health Score: Green (renew chắc) / Yellow (cần đầu tư) / Red (nguy cơ churn).

## Bước 2: Cadence 4 Mốc

**Day -90: Value Review meeting**
- Trình bày outcome KH đạt được (số đo)
- Trình bày feature mới sẽ có 12 tháng tới
- Hỏi: "Anh có roadmap nào em chưa biết để align?"

**Day -60: Renewal Proposal**
- Gửi quote renewal có:
  - Uplift 5-8% (justify bằng CPI + value mới)
  - Multi-year discount nếu KH ký 2-3 năm
  - Cross-sell/upsell add-on
- Schedule meeting review trong 7 ngày

**Day -30: Negotiation**
- Address objection chính (giá uplift / feature thiếu)
- Đưa concession có lý do (extend 3 tháng free / training thêm)
- Get verbal commit

**Day 0: Renewal Closed**
- Counter-signed contract trong CRM
- Hand-off CSM mới (nếu có)
- Internal celebration + post-mortem nếu khó khăn

## Bước 3: Uplift Strategy
- Standard: 5-7% YoY (kèm CPI explanation)
- Premium tier (Best customer): 3-5%
- Risk tier (Red health): 0% uplift + add value
- Multi-year lock-in: 0% năm 2-3 nếu ký 3 năm

Đính kèm 1 trang "Value delivered last 12 months" justify uplift.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce/HubSpot MCP: pull renewal date, ARR, opportunity
- Gainsight/ChurnZero MCP: pull health score, usage
- Gmail/Calendar MCP: gửi renewal email + book meeting
- Slack MCP: alert CSM team về Red account

**Fallback API:**
```python
# Pull renewals due in 90 days
from datetime import date, timedelta
soql = f"""SELECT Id, Name, EndDate, ARR__c, HealthScore__c
    FROM Contract WHERE EndDate >= {date.today()} 
    AND EndDate <= {date.today()+timedelta(days=90)}"""
renewals = sf.query(soql)["records"]
for r in renewals:
    print(f"{r['Name']} - {r['EndDate']} - Health: {r['HealthScore__c']}")
```

## Bước 5: Output Format
- **File 1**: `renewal_playbook.md` — 4 mốc playbook đầy đủ
- **File 2**: `renewal_tracker.xlsx` — Account / EndDate / ARR / Health / Owner / Stage / Uplift% / Status
- **File 3**: `renewal_emails.md` — 4 email template cho 4 mốc
- **File 4**: `value_review_template.pptx` — 5 slide value review deck
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Renewal flag bật Day -90 không trễ
- [ ] Health Score chấm rõ Green/Yellow/Red
- [ ] Uplift có business justification
- [ ] Champion còn active (verify trước Day -60)
- [ ] Multi-year option luôn được đề xuất
- [ ] Hand-off CSM nếu owner đổi
