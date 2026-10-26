---
name: sales-deal-review-template
description: |
  Template review deal nội bộ giữa AE & Manager — 12 câu hỏi qualify deep, risk identification, action plan tuần tới. Trigger phrases: "deal review template", "review deal nội bộ", "1-1 sales manager", "deal coaching", "review forecast deal", "pipeline review template", "review weekly deal", "deal inspection", "sales 1-1 template", "soạn review deal". Output là Markdown template + Excel deal scorecard.
---

# Deal Review Template (Manager-AE 1-1)

## Mục Tiêu
Trang bị Manager template review deal 15-20 phút mỗi deal để qualify thật, phát hiện risk sớm và đưa action cụ thể — thay vì "deal status update" mơ hồ.

## Khi Nào Dùng
- Weekly 1-1 Manager-AE
- Pipeline review monthly
- Deal forecast commit (cuối tháng/quý)
- Stuck deal >2 tháng cần unstuck
- Deal lớn cần escalate

## Bước 1: Pre-review Checklist (AE chuẩn bị)
AE gửi trước 2h:
- Deal name + ARR + close date + stage
- Current next step + due date
- 2 risk lớn nhất
- 1 ask cho Manager

Không có file này → reschedule.

## Bước 2: 12 Câu Hỏi Manager Hỏi

**Qualify (MEDDIC)**:
1. EB tên ai? Đã gặp chưa? Lần cuối khi nào?
2. KH đo thành công bằng metric gì cụ thể?
3. Decision criteria 3 cái là gì?
4. Decision process qua bao nhiêu bước? Đang ở bước nào?
5. Champion ai? Họ có Power + Pain + Plan không?

**Pain & Value**:
6. Pain ranked ưu tiên là gì?
7. Cost of inaction (CoI) KH chia sẻ bao nhiêu?
8. ROI đã calc chưa? KH có buy in không?

**Competitive**:
9. Đối thủ là ai? Strength/weakness?
10. KH so sánh trên tiêu chí gì?

**Close Plan**:
11. Next step ai làm gì khi nào?
12. Top 2 risk close date + mitigation?

## Bước 3: Deal Scorecard (chấm 0-3 mỗi item)
Tổng /36:
- 30-36: Commit forecast
- 22-29: Best case
- 15-21: Pipeline
- <15: Disqualify hoặc demote stage

## Bước 4: Action Plan tuần tới
3 action cụ thể với owner-deadline:
- AE: nghĩa vụ tuần này
- Manager: support nào
- Cross-functional: SE/CSM/Legal cần gì

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce/HubSpot MCP: pull deal, activity, next step
- Gong MCP: pull call signal (talk ratio, next-step mentions)
- Slack MCP: post review summary vào deal channel
- Calendar MCP: book follow-up checkpoint

**Fallback API:**
```python
# Pull deal + activity 30 ngày
deal = sf.Opportunity.get(deal_id)
activities = sf.query(f"""SELECT Subject, ActivityDate FROM Task
    WHERE WhatId = '{deal_id}' AND ActivityDate >= LAST_N_DAYS:30""")
# Flag stale: no activity 14+ days
if max([a["ActivityDate"] for a in activities["records"]]) < datetime.now()-timedelta(14):
    print("STALE - escalate")
```

## Bước 6: Output Format
- **File 1**: `deal_review_template.md` — 12 câu + scorecard + action template
- **File 2**: `deal_scorecard.xlsx` — tự tính tổng + recommendation
- **File 3**: `deal_review_meeting_notes.md` — form notes Manager fill trong call
- **File 4**: `pipeline_review_summary.xlsx` — aggregate weekly: all deals reviewed + actions
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] AE chuẩn bị pre-review trước 2h
- [ ] 12 câu hỏi đủ, không skip MEDDIC
- [ ] Scorecard chấm 0-3, không định tính
- [ ] 3 action có owner-deadline
- [ ] Update CRM stage + close date sau review
- [ ] Manager note coaching point cho AE
