---
name: ceo-linkedin-thought-leader
description: |
  Viết bài LinkedIn cho CEO theo 3 dạng (opinion piece, founder story, framework) — chuẩn LinkedIn algorithm 2026, có hook 5 dòng, format scannable, CTA engage cao.
  Kích hoạt khi người dùng nói: "viết LinkedIn CEO", "bài LinkedIn lãnh đạo", "LinkedIn thought leader", "founder LinkedIn post", "viết post LinkedIn", "LinkedIn content founder", "viral LinkedIn", "viết bài CEO LinkedIn".
  Output là Markdown post + image suggestion.
---

# CEO LinkedIn Thought Leader — Bài LinkedIn Cho CEO

## Mục Tiêu
LinkedIn là kênh #1 cho thought leadership B2B. CEO post đều = recruit talent, attract investor, win deal. Skill này tạo bài theo 3 dạng proven engage cao.

## Khi Nào Dùng
- Tuần 2-3 lần (cadence ổn định)
- Sau milestone công ty (hire, raise, ra mắt)
- Sau learning từ thất bại
- Khi có hot take ngành
- Recruiting drive

## Bước 1: Chọn 1 Trong 3 Dạng

**Dạng 1 - Opinion Piece** (phản biện): "Mọi người nói X nhưng tôi nghĩ Y vì Z"
- Hook: phát biểu controversial
- Body: 3 lý do + 1 caveat
- Engage cao nhất nếu hot take đúng

**Dạng 2 - Founder Story** (kể chuyện): "Năm 2019, tôi đã làm Y và học được X"
- Hook: scene cụ thể
- Body: situation → action → result → lesson
- Build trust + relatability

**Dạng 3 - Framework** (giáo dục): "5 bước tôi dùng để Y"
- Hook: kết quả đạt được
- Body: list bullet có giải thích
- Save & share cao nhất

## Bước 2: Cấu Trúc Bài LinkedIn 2026
```
[Hook 1 dòng — câu shock/đề/thống kê]
[Dòng 2]
[Dòng 3 — context]
[Dòng 4]
"Click thêm"...

[Body chính 150-250 từ]
[Format scannable: dòng đơn, bullet, emoji ít]

[CTA cuối: câu hỏi engage]

#hashtag1 #hashtag2 #hashtag3
```

5 dòng đầu là CỰC quan trọng vì LinkedIn truncate ở đây.

## Bước 3: Quy Tắc Tối Ưu Engagement
- Bài 1200-2000 ký tự (sweet spot)
- Dòng đơn, paragraph 1-2 câu max
- Có ít nhất 1 câu hỏi cuối kêu comment
- Tag tối đa 2-3 người (không spam)
- Đăng 7-9h sáng hoặc 17-19h tối thứ 3-5
- Reply mọi comment trong 1h đầu
- Ảnh kèm tăng reach 2x

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tìm benchmark CEO viết về topic tương tự
- WebFetch: lấy stats data validate hook
- Notion MCP: content calendar LinkedIn
- Canva MCP: tạo image carousel kèm post
- Buffer/Hootsuite (qua API): schedule post

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Đo độ readability hook
text = "First 5 lines here..."
chars = sum(len(line) for line in text.split('\n')[:5])
assert chars <= 200, "Hook quá dài, sẽ bị truncate"
# Đếm hashtag
hashtags = [w for w in text.split() if w.startswith('#')]
assert 3 <= len(hashtags) <= 5
```

## Bước 5: Output Format
- Markdown post sẵn copy-paste vào LinkedIn
- 1-2 image suggestion (Canva brief)
- Comment đầu tiên gợi ý (engage seed)
- Hashtag list (3-5)
- Best posting time (TZ Việt Nam)
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/linkedin/YYYY-MM-DD-[topic].md`

## Checklist Trước Khi Giao
- [ ] Hook 5 dòng đầu < 200 ký tự
- [ ] Tổng bài 1200-2000 ký tự
- [ ] Có CTA câu hỏi cuối
- [ ] 3-5 hashtag relevant
- [ ] Đúng 1 trong 3 dạng
- [ ] Schedule giờ vàng
