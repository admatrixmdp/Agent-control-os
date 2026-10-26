---
name: ceo-departmental-scorecard
description: |
  Scorecard chấm điểm các phòng ban hàng tháng — gồm KPI tài chính, vận hành, nhân sự, satisfaction. Ranking từ A đến F với feedback cụ thể cho mỗi phòng.
  Kích hoạt khi người dùng nói: "scorecard phòng ban", "chấm điểm phòng ban", "đánh giá phòng ban", "department scorecard", "ranking phòng ban", "review phòng ban", "performance phòng ban", "monthly department review".
  Output là HTML scorecard + Excel ranking.
---

# CEO Departmental Scorecard — Chấm Điểm Phòng Ban

## Mục Tiêu
Phòng nào đang dẫn dắt, phòng nào tụt? CEO không có thời gian deep-dive từng phòng. Scorecard chuẩn hoá đánh giá để công bằng + tạo cạnh tranh lành mạnh.

## Khi Nào Dùng
- Monthly leadership review
- Trước bonus pool allocation
- Trước promote/giáng GĐ phòng
- All-hands recognition
- Khi nghi ngờ 1 phòng under-perform

## Bước 1: Thiết Lập 5 Dimension
Mỗi phòng chấm 5 dimension (mỗi cái /20 = tổng /100):
1. **Output**: deliver kết quả vs target
2. **Quality**: defect, NPS, churn (tuỳ phòng)
3. **Speed**: cycle time, deadline hit rate
4. **People**: attrition, eNPS, hire rate
5. **Strategic**: contribute initiative công ty

## Bước 2: Tiêu Chí KPI Mỗi Phòng
**Sales**: revenue/quota, win rate, cycle time, attrition AE, deal company-wide
**Marketing**: MQL/target, CAC, brand health, content/team, GTM với Sales
**Product**: NPS, ship velocity, bug rate, eng attrition, OKR product
**Operations**: on-time delivery, defect, OPEX %, team eNPS, process improvement
**Finance**: close speed, audit score, AR days, attrition CFO team, FP&A quality
**HR**: hire vs plan, attrition, eNPS, hiring CT, culture initiative

## Bước 3: Ranking + Feedback
- Total /100 → grade: A(85+), B(70-84), C(55-69), D(40-54), F(<40)
- So sánh với tháng trước (↑↓→)
- Feedback 3-5 dòng cho mỗi phòng:
  - 1 điều làm tốt
  - 1 điều cần cải thiện
  - 1 hành động đề xuất cho tháng tới

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: pull KPI sheet hàng tháng
- HRIS MCP / Notion: pull attrition + eNPS
- HubSpot MCP: pull win rate, CAC
- Linear MCP: pull ship velocity, bug rate
- Slack MCP: post tóm tắt ranking lên #leadership

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tính score
import pandas as pd
df = pd.DataFrame(department_data)
df['total'] = df[['output','quality','speed','people','strategic']].sum(axis=1)
df['grade'] = pd.cut(df['total'], bins=[0,40,55,70,85,100], labels=['F','D','C','B','A'])
df['rank'] = df['total'].rank(ascending=False)
ranking = df.sort_values('total', ascending=False)
```

## Bước 5: Output Format
- HTML dashboard với:
  - Header: ranking table có grade + trend
  - Phần riêng mỗi phòng: 5 dimension radar chart
  - Feedback box mỗi phòng
- Excel `scorecard-YYYY-MM.xlsx` cho follow-up
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ 5 dimension cho mỗi phòng
- [ ] Có so sánh tháng trước
- [ ] Feedback 3-5 dòng cụ thể, không generic
- [ ] Tránh bias (giải thích cách chấm trước)
- [ ] Share preview với GĐ phòng trước public
- [ ] Có quy ước rõ A/B/C/D/F
