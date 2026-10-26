---
name: ceo-monthly-allhands-deck
description: |
  Tạo deck All-Hands tháng 20-25 slides cho CEO trình bày trước toàn công ty — gồm wins, numbers, what's next, Q&A. Format engage, không khô khan.
  Kích hoạt khi người dùng nói: "all-hands deck", "deck all hands tháng", "town hall deck", "deck toàn công ty", "monthly all-hands", "deck CEO toàn công ty", "company-wide meeting deck", "all-hands presentation".
  Output là file .pptx 20-25 slides.
---

# CEO Monthly All-Hands Deck — Deck Họp Toàn Công Ty Tháng

## Mục Tiêu
All-Hands monthly là moment CEO có 200 nhân viên focus 60 phút. Deck tốt = align toàn công ty, build morale. Skill này tạo deck chuẩn trong 1h thay vì 1 ngày.

## Khi Nào Dùng
- Hàng tháng (tuần đầu tháng mới)
- Sau quarter close (Q1, Q2, Q3, Q4)
- Sau milestone lớn
- Trước thay đổi tổ chức
- Khi tinh thần xuống cần reset

## Bước 1: Thu Thập Materials Tháng
- Top 5 wins phòng ban
- 3 số tài chính (chia sẻ được)
- Customer story tháng (1-2)
- New hires (ảnh + 1 dòng)
- Anniversaries (ai làm bao năm)
- Recognition (peer-nominated)
- OKR progress tổng
- What's next tháng tới
- Q&A đã thu thập từ form

## Bước 2: Cấu Trúc 22 Slide Chuẩn
1. Cover ("All-Hands Tháng [X]/[năm]")
2. Agenda
3. State of the Company (1 slide với 3 số lớn)
4. OKR progress dashboard
5-8. Wins by department (Sales / Marketing / Product / Ops)
9. Customer spotlight (story 1)
10. Customer spotlight (story 2)
11. People update: new hires
12. People update: anniversaries
13. Shout-out / recognition wall
14. Culture moment (ảnh team event)
15-17. What's next: 3 ưu tiên tháng tới
18. Strategic context (1 slide CEO thought)
19. Q&A intro (top 5 questions submitted)
20-21. Q&A live
22. Closing ("Thank you, see you tháng tới")

## Bước 3: Quy Tắc Trình Bày
- 70% là celebrate, 20% strategy, 10% concern
- Số PHẢI có context (vs tháng trước, vs plan)
- New hire có ảnh + cá tính (không khô)
- Customer story dùng video clip nếu có
- Slide không quá 30 từ
- Có ít nhất 1 moment hài
- Mở mic Q&A trước, prepare answer cho top 5

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Canva MCP: template all-hands có sẵn
- Google Drive MCP: pull số tháng từ Sheets
- Slack MCP: collect shout-out từ #kudos, Q&A từ form
- Notion MCP: pull customer story
- Gmail MCP: gửi recap email sau cuộc

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Pull Slack shout-out tháng
import requests
r = requests.get(
  "https://slack.com/api/conversations.history",
  params={"channel": "C_KUDOS", "oldest": month_start_ts},
  headers={"Authorization": f"Bearer {token}"}
)
messages = r.json()['messages']
top_kudos = sorted(messages, key=lambda m: len(m.get('reactions', [])), reverse=True)[:10]
```

## Bước 5: Output Format
- File `.pptx` 20-25 slides ratio 16:9
- Speaker notes 60-80 từ/slide
- Recap email Markdown sau cuộc cho người vắng
- Notion page lưu archive
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/allhands-YYYY-MM.pptx`

## Checklist Trước Khi Giao
- [ ] Đủ 20-25 slides
- [ ] 70% celebrate, không bi quan
- [ ] Top 5 Q&A đã prepare answer
- [ ] New hires có ảnh
- [ ] Có ít nhất 1 video/animation
- [ ] Đã rehearse với 1 leader xem flow
- [ ] Gửi calendar invite trước 1 tuần
