---
name: sales-mql-sql-criteria
description: |
  Định nghĩa rõ MQL/SQL/SAL — tiêu chí, scoring, ownership giữa Marketing và Sales. Trigger phrases: "định nghĩa MQL SQL", "MQL SQL criteria", "tiêu chí MQL", "marketing qualified lead", "sales accepted lead", "SAL definition", "scoring lead Marketing Sales", "handover marketing sales", "lead funnel definition", "lead stage definition". Output là Markdown definition doc + Excel criteria + workflow diagram.
---

# MQL / SAL / SQL Criteria Builder

## Mục Tiêu
Chấm dứt war Marketing-Sales bằng định nghĩa rõ ràng MQL/SAL/SQL kèm scoring rule + ownership matrix — giúp marketing biết "lead nào đẩy", sales biết "lead nào nhận".

## Khi Nào Dùng
- Sales complain "lead Marketing rác"
- Marketing complain "Sales không follow up"
- Quarterly planning Marketing-Sales SLA
- Implement MAP/CRM mới
- Re-design funnel sau pivot ICP

## Bước 1: Định nghĩa 3 Stage

**MQL (Marketing Qualified Lead)**:
- Score >50 (rule + behavior)
- Fit ICP (firmographic match)
- Behavior: 2+ content download OR 1 demo request OR 1 contact form
- Marketing own → handover SDR

**SAL (Sales Accepted Lead)**:
- SDR review + accept trong 24h
- Confirm có thông tin liên lạc đúng
- Confirm không phải competitor / student / current customer
- SDR own → outreach 14 ngày cadence

**SQL (Sales Qualified Lead)**:
- SDR đã quali BANT-lite qua call/email
- Có pain + use case + decision authority
- Đã book meeting với AE
- AE own → discovery → opportunity

## Bước 2: Lead Scoring Engine
Score MQL:
- **Demographic** (max 30):
  - Title VP+/Director: 15, Manager: 10, IC: 5
  - Company size match ICP: 15
  - Industry match: 10
- **Behavior** (max 40):
  - Demo request: 40
  - Pricing page visit: 20
  - 3+ content download: 15
  - Webinar attendance: 10
  - Email click: 5
- **Negative** (-X):
  - Competitor domain: -50
  - Student/.edu: -30
  - Current customer: -50

MQL khi tổng >50.

## Bước 3: Ownership & SLA Matrix
- MQL → SDR: SLA accept 24h, outreach 5 ngày, 14-day cadence
- SAL → SDR: 14-day work, after that pass back Marketing nurture
- SQL → AE: SLA discovery meeting hold trong 7 ngày
- Recycled lead (SDR DQ): back to Marketing nurture với note lý do

## Bước 4: Reporting & Calibration
KPI Marketing-Sales:
- MQL → SAL conversion (target >80%)
- SAL → SQL (>30%)
- SQL → Closed-won (>20%)
- Lead-to-revenue time
- SAL rejection reason aggregation

Monthly calibration meeting: tune criteria nếu conversion lệch.

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- HubSpot/Marketo MCP: lead scoring engine
- Salesforce MCP: stage workflow + ownership
- Slack MCP: real-time MQL alert SDR
- BI MCP (Looker/Tableau): conversion dashboard

**Fallback API:**
```python
# HubSpot score update + MQL workflow trigger
import requests
def score_lead(lead):
    s = 0
    if "VP" in lead["title"] or "Director" in lead["title"]: s += 15
    if lead["company_size"] in ["50-200","200-1000"]: s += 15
    if lead["last_form"] == "demo_request": s += 40
    if "@gmail.com" in lead["email"]: s -= 20
    return s

if score >= 50:
    requests.patch(f"https://api.hubapi.com/contacts/v1/contact/vid/{vid}",
        json={"properties": [{"property": "lifecyclestage", 
              "value": "marketingqualifiedlead"}]})
```

## Bước 6: Output Format
- **File 1**: `MQL_SQL_definitions.md` — doc 4 trang đầy đủ
- **File 2**: `lead_scoring_rules.xlsx` — bảng scoring rules + version control
- **File 3**: `lead_workflow.pptx` — diagram visual funnel
- **File 4**: `SLA_dashboard.xlsx` — track SLA compliance weekly
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Marketing + Sales đồng ký SLA
- [ ] Scoring có cả positive + negative
- [ ] Ownership rõ mỗi stage
- [ ] Recycled workflow defined
- [ ] Calibration monthly bật
- [ ] Dashboard transparent 2 side
