---
name: ceo-quarter-priorities
description: |
  Xác định Top 3 ưu tiên quý cho CEO/công ty kèm OKR cụ thể — chọn ít, sâu, đo lường được. Có template review hàng tuần để track không trượt.
  Kích hoạt khi người dùng nói: "top 3 quý", "quarter priorities", "ưu tiên quý CEO", "Q goals", "3 ưu tiên quý này", "quarter focus", "quarterly priorities", "OKR quý".
  Output là Markdown plan + Notion database.
---

# CEO Quarter Priorities — Top 3 Ưu Tiên Quý

## Mục Tiêu
CEO có 10 việc muốn làm quý này → cuối quý không xong cái nào. Skill này force focus 3 priority, mọi ngày CEO biết mình đang work on priority hay distraction.

## Khi Nào Dùng
- Đầu quý (tuần 1)
- Sau khi raise vốn (define use of funds)
- Sau pivot
- Khi cảm thấy "bận nhưng không tiến"
- Sau performance review CEO

## Bước 1: Brainstorm 10-15 Initiative Candidates
Từ:
- Strategic roadmap năm
- Risk register (top risk cần mitigate)
- Feedback team (1-1)
- Customer asks (top 3)
- Founder personal goal

Liệt kê 10-15 cái có thể làm quý này.

## Bước 2: Forced Ranking → Top 3
Mỗi candidate score 3 chiều:
- **Impact**: nếu thành công, ảnh hưởng business thế nào (1-10)
- **Effort**: bao nhiêu công sức (1-10, càng thấp càng tốt)
- **Reversibility**: nếu sai có cứu được không (1-10, càng thấp càng "must get right")

Score = Impact / Effort × Reversibility.
Top 3 = 3 cái cao nhất.

KEY: nói KHÔNG với 7-12 cái còn lại. Đưa vào "Parking lot Q sau".

## Bước 3: OKR Cho Mỗi Priority
Mỗi priority có:
- **Objective**: câu định tính (qualitative)
- **3-5 Key Results**: số đo lường được
- **Owner CXO**: 1 người duy nhất
- **Weekly check-in**: thứ Hai 9h

VD:
- Objective: "Mở thành công thị trường Hà Nội"
- KR1: 50 khách trả phí từ HN
- KR2: Doanh thu HN ≥ 15% tổng
- KR3: Hire GĐ Bắc + 5 sales
- Owner: COO

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Notion MCP: database "Q Priorities" có status weekly
- Linear MCP: tạo cycle/project tương ứng từng priority
- Slack MCP: tạo channel #q-priorities-checkin
- Calendar MCP: weekly check-in recurring
- Gmail MCP: gửi recap mỗi cuối tuần

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Forced ranking
import pandas as pd
candidates = pd.DataFrame(initiatives)
candidates['score'] = candidates['impact'] / candidates['effort'] * candidates['reversibility']
top3 = candidates.nlargest(3, 'score')
parking = candidates.nsmallest(len(candidates)-3, 'score')
```

## Bước 5: Output Format
- Markdown plan với 3 priority + OKR
- Notion database "Q Priorities" có cột status weekly
- 1-page poster cho văn phòng
- Weekly check-in template
- "What we said NO to" list (parking lot)
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/q-priorities-Q#-YYYY.md`

## Checklist Trước Khi Giao
- [ ] Đúng 3 priority, không hơn
- [ ] Mỗi priority có OKR đầy đủ
- [ ] Mỗi priority có 1 CXO owner duy nhất
- [ ] Parking lot ≥ 7 items đã reject
- [ ] Weekly check-in đã đặt calendar
- [ ] CEO confirm sẵn sàng nói "no" với rest
