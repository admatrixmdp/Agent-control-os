---
name: sales-mutual-action-plan
description: |
  Tạo Mutual Action Plan (MAP) với KH — timeline, milestone, owner cả 2 bên để align close date. Trigger phrases: "mutual action plan", "MAP sales", "close plan với KH", "joint plan customer", "deal close roadmap", "tạo MAP enterprise deal", "action plan đôi bên", "close timeline KH", "implementation plan deal", "go-live plan". Output là Excel MAP timeline + Docx signed copy.
---

# Mutual Action Plan (MAP) Builder

## Mục Tiêu
Tăng forecast accuracy enterprise deal lên >85% bằng MAP — document timeline + milestone + owner 2 bên (sales + KH) ký xác nhận, tránh "deal slip" không kiểm soát.

## Khi Nào Dùng
- Enterprise deal cycle >60 ngày
- Champion verified
- KH muốn go-live date cụ thể
- Multiple stakeholder cần align
- Sau Demo / trước Proposal

## Bước 1: Co-create với Champion
KHÔNG đơn phương AE viết. Phải:
- Book 30-45 phút với Champion
- Bring template draft
- Co-edit live
- Champion confirm owner KH-side mỗi milestone

## Bước 2: 8 Milestone Phổ Biến
1. Discovery complete + business case agreed
2. Technical review / Security review
3. Procurement engaged
4. Legal redline complete
5. EB approval meeting
6. Contract signed
7. Implementation kickoff
8. Go-live

Mỗi milestone có:
- Date target
- Owner (KH + AE side)
- Deliverable
- Dependency
- Risk

## Bước 3: 2-Column Timeline (KH side + Our side)
Layout Excel:
- Cột A: Milestone
- Cột B: Target date
- Cột C: KH owner + due
- Cột D: Our owner + due
- Cột E: Status (planned/in-progress/done/blocked)
- Cột F: Notes

Update weekly review.

## Bước 4: Risk & Dependency
Mỗi milestone có:
- Dependency upstream (cần gì trước)
- Risk likelihood + impact
- Mitigation plan

Vd: "Legal redline phụ thuộc Security review xong trong 2 tuần. Risk: legal backlog. Mitigation: SVP-level escalation contact ready."

## Bước 5: Sign-off + Cadence
- Champion + AE ký initial vào MAP
- Weekly checkpoint 15 phút (Champion + AE)
- Reschedule milestone phải document lý do
- Slip >5 ngày 2 lần → escalate

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce/HubSpot MCP: link MAP vào opportunity
- DocuSign MCP: sign MAP
- Calendar MCP: schedule weekly checkpoint
- Slack MCP: shared channel KH-AE update
- Drive MCP: shared MAP doc live edit

**Fallback API:**
```python
# Sync MAP status vào CRM
sf.Opportunity.update(opp_id, {
    "MAP_Milestones_Complete__c": completed_count,
    "MAP_Total__c": total,
    "Next_Milestone__c": next_one["name"],
    "Next_Due__c": next_one["due"],
    "MAP_Health__c": "Green" if no_slip else "Yellow"
})
```

## Bước 7: Output Format
- **File 1**: `MAP_<customer>_<date>.xlsx` — 8 milestone × timeline
- **File 2**: `MAP_<customer>_signed.pdf` — sign-off Champion + AE
- **File 3**: `MAP_weekly_template.md` — checkpoint format
- **File 4**: `MAP_risk_log.xlsx` — risk + mitigation
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Co-created với Champion (không 1 chiều)
- [ ] 2 owner mỗi milestone (KH + AE)
- [ ] Champion sign-off
- [ ] Weekly checkpoint cadence
- [ ] Risk + mitigation rõ
- [ ] Slip escalation rule
