---
name: ceo-leadership-feedback-360
description: |
  Quy trình feedback 360 độ cho lãnh đạo (CEO, CXO, GĐ phòng) — design câu hỏi, gửi anonymous survey cho cấp trên/cấp dưới/peer, tổng hợp insight, coaching plan.
  Kích hoạt khi người dùng nói: "feedback 360", "360 review", "đánh giá lãnh đạo 360", "360 degree feedback", "leadership review", "feedback đa chiều", "360 survey", "đánh giá CEO".
  Output là PDF feedback report + coaching plan.
---

# CEO Leadership Feedback 360 — Đánh Giá 360 Cho Lãnh Đạo

## Mục Tiêu
CEO/CXO ít khi nhận feedback thật vì power dynamic. 360 anonymous = mirror đáng tin cậy. Skill này chạy 360 trong 2 tuần thay vì thuê consultant 30M.

## Khi Nào Dùng
- CEO annual self-review
- Trước promote CXO
- Sau khi attrition cấp dưới cao
- Coaching plan cho leader struggling
- Mid-year leadership development

## Bước 1: Thiết Kế Survey
Mỗi leader có 8-12 rater:
- 1-2 cấp trên (manager / board)
- 3-5 cấp dưới direct report
- 3-5 peers (cùng level)
- 1-2 self

Câu hỏi 5 nhóm (mỗi nhóm 5-8 câu Likert 1-5):
1. **Vision & Strategy**: clarity, prioritization
2. **Execution**: shipping results, decision speed
3. **People**: hire, coach, fire, delegate
4. **Communication**: clear, listen, transparent
5. **Self-awareness**: blind spots, ego, growth

+ 3 câu open-ended:
- "Continue doing"
- "Stop doing"
- "Start doing"

## Bước 2: Send Anonymous
- Dùng Google Form/Typeform anonymous
- Lock IP/email từ result
- Gửi với cover letter từ HR (không CEO tự gửi)
- 7-10 ngày complete
- Reminder day 5, 8

## Bước 3: Synthesize Insight
- Trung bình mỗi câu (1-5)
- Standard deviation (sự đồng thuận)
- Compare self vs others (blind spot khi self cao mà others thấp)
- Top 3 strengths (avg ≥ 4.3)
- Top 3 areas (avg < 3.5)
- Verbatim quote (dedupe, anonymize)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Forms (qua Drive MCP): tạo survey + collect anonymous
- Notion MCP: 360 report database
- Gmail MCP: gửi invitation rater + reminder
- Lattice/15Five MCP: nếu công ty đã có HRIS
- Calendar MCP: schedule debrief 1-1 với leader

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Analysis Likert + open
import pandas as pd
df = pd.read_csv('survey_responses.csv')
strengths = df[df['avg_score'] >= 4.3].sort_values('avg_score', ascending=False).head(3)
gaps = df[df['avg_score'] < 3.5].sort_values('avg_score').head(3)
# Blind spot
self_row = df[df['rater_type'] == 'self']
others_avg = df[df['rater_type'] != 'self'].groupby('question')['score'].mean()
blind_spots = self_row[self_row['score'] - others_avg > 1.0]
```

## Bước 5: Output Format
- PDF 360 report 8-12 trang (CONFIDENTIAL):
  - Executive summary
  - Score by category radar chart
  - Self vs others comparison
  - Top 3 strengths với quote
  - Top 3 areas với quote
  - 90-day coaching plan
- Debrief deck cho 1-1 với coach
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/360-[name]-YYYY.pdf` (encrypted)

## Checklist Trước Khi Giao
- [ ] Đủ 8-12 rater per leader
- [ ] Survey hoàn toàn anonymous
- [ ] Verbatim đã anonymize
- [ ] Blind spot identified
- [ ] 90-day plan cụ thể
- [ ] Có coach/mentor follow up
- [ ] File confidential, access ≤ 3 người
