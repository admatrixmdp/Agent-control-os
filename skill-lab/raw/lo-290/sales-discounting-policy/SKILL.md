---
name: sales-discounting-policy
description: |
  Chính sách chiết khấu theo tier deal size, volume, multi-year, strategic value với approval routing. Trigger phrases: "chính sách chiết khấu", "discounting policy", "discount approval", "chiết khấu theo tier", "discount governance", "policy giảm giá", "approval discount sales", "discount matrix B2B", "chiết khấu sales", "manage discount". Output là Markdown policy + Excel discount matrix + workflow diagram.
---

# Sales Discounting Policy & Governance

## Mục Tiêu
Định nghĩa policy chiết khấu rõ ràng để AE biết được giảm bao nhiêu không cần hỏi, Manager/Director biết khi nào duyệt — giảm "wild west" discounting và bảo vệ margin.

## Khi Nào Dùng
- Average discount >20% list
- AE inconsistent giảm giá tuỳ deal
- Quarterly margin erosion
- Finance push back về pricing
- M&A merge company có policy khác

## Bước 1: Discount Tier Structure

**Tier 1 — AE Auto-approve (0-10%)**:
- Lý do: standard adjustment
- Cap: 10% list
- Approval: AE self
- Audit log: monthly review

**Tier 2 — Manager (10-20%)**:
- Lý do: competitive, volume, strategic
- Approval: Sales Manager
- SLA: 24h response
- Trade required: multi-year or annual upfront

**Tier 3 — Director (20-30%)**:
- Lý do: enterprise strategic, displace competitor
- Approval: Sales Director + Finance
- SLA: 48h
- Trade required: 3-year minimum + reference

**Tier 4 — VP/CRO (>30%)**:
- Exceptional case
- Sign-off: CRO + CFO
- Trade required: justify ROI

## Bước 2: Volume Tier
Tự động apply:
- <100 user/license: list price
- 100-500: 5% off
- 500-1000: 10% off
- 1000+: 15% off (auto, không cần approval)

## Bước 3: Multi-year Lock
- 2-year: 5% off
- 3-year: 10% off
- 5-year: 15% off (rare)

Cộng với volume discount (stack).

## Bước 4: Approval Workflow

```
AE request → System auto-route by tier
    Tier 1: auto-approve + log
    Tier 2: Manager email/Slack → 24h
    Tier 3: Director + Finance → 48h
    Tier 4: CRO + CFO → 72h
Decision → Notify AE → Update CPQ → Audit log
```

## Bước 5: Discount Tracking & Audit
- Monthly report: avg discount, % deal over X%
- AE leaderboard discount usage
- Quarterly RCA top 10 discount
- Annual policy review

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce CPQ MCP: native approval routing
- Slack MCP: approval workflow
- Drive MCP: policy doc + version
- BI MCP: discount dashboard

**Fallback API:**
```python
# Auto-approval routing logic
def route_discount(deal):
    pct = deal["discount_pct"]
    if pct <= 10: return ("auto", None)
    elif pct <= 20: return ("manager", deal["manager_id"])
    elif pct <= 30: return ("director", DIR_ID)
    else: return ("cro", CRO_ID)

# Trigger Slack approval
def trigger_approval(deal, role, approver_id):
    requests.post(SLACK_API,
        json={"channel": f"@{approver_id}",
              "text": f"Approval request: {deal['name']} discount {deal['discount_pct']}%",
              "attachments": [{"actions": [{"text": "Approve", "value": deal["id"]}]}]})
```

## Bước 7: Output Format
- **File 1**: `discounting_policy.md` — 4 tier + approval matrix
- **File 2**: `discount_matrix.xlsx` — interactive: AE input deal → output policy + needed approval
- **File 3**: `discount_workflow.pptx` — diagram visual
- **File 4**: `discount_audit_template.xlsx` — monthly audit form
- **File 5**: `discount_dashboard.xlsx` — track avg + outlier
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 4 tier rõ ràng với cap
- [ ] Trade required cho mỗi tier
- [ ] Approval SLA defined
- [ ] CPQ system enforce policy
- [ ] Monthly audit + RCA
- [ ] Annual policy review
