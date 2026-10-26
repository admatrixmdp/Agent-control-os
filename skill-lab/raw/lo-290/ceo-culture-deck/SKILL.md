---
name: ceo-culture-deck
description: |
  Tạo culture deck nội bộ kiểu Netflix/HubSpot — 20-30 slides về giá trị, hành vi, hệ thống quản lý, cách hire/fire/promote, dùng cho onboarding & recruiting branding.
  Kích hoạt khi người dùng nói: "culture deck", "deck văn hoá công ty", "slide văn hoá công ty", "Netflix culture deck", "company values deck", "onboarding deck", "culture book", "deck giới thiệu văn hoá".
  Output là file .pptx 20-30 slides + PDF public.
---

# CEO Culture Deck — Deck Văn Hoá Công Ty

## Mục Tiêu
Netflix culture deck được xem 20+ triệu lượt, recruit hàng nghìn người. Culture deck tốt = vũ khí employer branding mạnh nhất. Skill này tạo deck chuẩn từ V/M/V đã có.

## Khi Nào Dùng
- Onboarding nhân viên mới
- Recruiting branding (post LinkedIn)
- All-hands annual
- Trước round Series B+ (signal cho VC)
- Khi attrition cao cần re-anchor

## Bước 1: Input Cần Có
- Vision/Mission/Values đã viết
- 3-5 real stories minh hoạ values
- Hệ thống reward/promotion hiện tại
- Cách công ty hire/fire khác biệt
- Vibe muốn truyền: bold/warm/serious

## Bước 2: Cấu Trúc 25 Slides Chuẩn
1. Cover ("How We Work")
2-3. Why we exist (vision + mission)
4-5. Our journey (timeline)
6-10. 5 core values, mỗi value 1 slide:
   - Value + tagline
   - Câu hỏi test value (VD: "Bạn từ chối khách to vì xung đột value chưa?")
   - 1 real story minh hoạ
11-13. How we hire (job → interview → offer)
14-16. How we work (meetings, async, time-off)
17-18. How we grow (promotion, feedback)
19-20. How we pay (salary band, equity, bonus)
21-22. How we exit (firing, severance)
23. What we don't do (anti-values)
24. Join us (CTA)
25. Cover sau

## Bước 3: Quy Tắc Storytelling
- Mỗi value có 1 real story (không hypothetical)
- Honest về cái khó: "We work hard. Hours long, expectations high."
- Dùng "we", "us" — không "the company"
- Show, don't tell: thay vì "We value transparency" → "Every Friday we publish revenue + burn to all team"
- Có ảnh thật team — không stock photo

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Canva MCP: dùng template culture deck đẹp
- Google Drive MCP: pull ảnh team từ folder marketing
- Notion MCP: lưu version history, collect story từ team
- Slack MCP: poll team chọn favorite values
- WebSearch: tham khảo Netflix/HubSpot/GitLab culture deck

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Slide với hình + tagline
from pptx import Presentation
from pptx.util import Inches
prs = Presentation()
for value in values:
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    slide.shapes.title.text = value['name'].upper()
    slide.placeholders[1].text = value['tagline']
    slide.shapes.add_picture(value['photo'], Inches(7), Inches(1.5), Inches(5), Inches(5))
prs.save('/tmp/culture-deck.pptx')
```

## Bước 5: Output Format
- File `.pptx` 20-30 slides ratio 16:9
- PDF public version để chia sẻ LinkedIn
- 1-page summary "Cliff Notes" cho onboarding
- Speaker notes 100 từ/slide cho all-hands present
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/culture-deck-vN.pptx`

## Checklist Trước Khi Giao
- [ ] Đủ 20-30 slides theo cấu trúc
- [ ] Mỗi value có real story
- [ ] Có "what we don't do" (anti-values)
- [ ] Toàn ảnh thật, không stock
- [ ] Có CTA recruiting cuối
- [ ] Đã review với 3-5 lãnh đạo cũ trước public
