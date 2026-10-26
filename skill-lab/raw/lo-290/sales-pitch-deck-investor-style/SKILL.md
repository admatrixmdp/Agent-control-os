---
name: sales-pitch-deck-investor-style
description: |
  Pitch deck mạnh kiểu founder/investor — story-driven, vision, big idea cho enterprise C-level. Trigger phrases: "pitch deck investor style", "founder-style pitch", "executive pitch deck", "vision deck C-level", "big idea pitch", "narrative deck sales", "story-driven sales deck", "CEO pitch deck", "deck kiểu startup pitch", "category-defining pitch". Output là PPT 10 slide + speaker note.
---

# Investor-Style Pitch Deck (C-level Sales)

## Mục Tiêu
Tạo pitch deck mạnh kiểu founder (vision + narrative + big idea) cho meeting C-level — khác sales deck thông thường, gây "wow" trong 10 phút đầu, tạo mind-share để KH theo đuổi mình thay vì ngược lại.

## Khi Nào Dùng
- Meeting CEO/CIO/CFO enterprise
- Event keynote pitch
- Category creation - giáo dục thị trường
- Major launch product/strategic move
- Partnership/M&A discussion

## Bước 1: 10-Slide Investor-style Flow

1. **Vision** — câu mở cực lớn, 1 câu định nghĩa thế giới mới
2. **Problem** — paint pain đau như mất tiền
3. **Why now** — 3 tailwind làm pain trở nên crisis
4. **Old way** — cách cũ tại sao thất bại
5. **Insight** — moment "aha" — cách mới phải nghĩ
6. **Solution** — mình là cách mới đó, 1 hình ảnh
7. **Why us** — tại sao mình win the category
8. **Traction** — proof: logo, growth, NPS
9. **The future** — vision 5-10 năm chung
10. **The ask** — CTA: partnership / trial / pilot

## Bước 2: Story Arc Rules
- Slide 1: phải "hook" — câu/visual gây dừng tim
- Slide 5: "aha moment" — KH nhận ra insight
- Slide 9: "vision" — KH muốn join journey
- Slide 10: CTA cụ thể, không vague

## Bước 3: Visual & Design
- Full-bleed image quality cao
- Max 7 từ/slide (extreme minimalism)
- 1 font, 1 color brand + black
- Animation tối thiểu
- Không bullet liệt kê — chỉ statement đơn

## Bước 4: Speaker Notes Đầy Đủ
2-5 phút speak mỗi slide. Note có:
- Story personal/anecdote
- Data point liên kết
- Câu chuyển slide tự nhiên
- Trial close 1-2 lần xuyên suốt

## Bước 5: Audience Calibration
Trước meeting:
- Research C-level (LinkedIn, speech, interview)
- Customize Vision slide với reference của họ
- Anticipate 5 câu hỏi C-level sẽ hỏi
- Backup detail (deck Appendix) cho deep-dive

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- PPT/Keynote MCP: tạo deck
- Unsplash/Pexels MCP: hero image
- WebFetch: research C-level statement
- Salesforce MCP: log C-level meeting outcome
- LinkedIn MCP: stakeholder insight

**Fallback API:**
```python
# Pull C-level public statements
import requests
def research_cxo(name, company):
    r = requests.get(f"https://api.linkedin.com/v2/profile-search",
        params={"name": name, "company": company}).json()
    posts = scrape_linkedin_posts(r["id"], limit=10)
    interviews = search_youtube(f"{name} {company} interview")
    return {"posts": posts, "interviews": interviews,
            "vision_quotes": extract_quotes(posts + interviews)}
```

## Bước 7: Output Format
- **File 1**: `pitch_deck_<cxo>.pptx` — 10 slide investor-style
- **File 2**: `speaker_notes.md` — 5 phút/slide script
- **File 3**: `appendix_deck.pptx` — 20 slide backup detail
- **File 4**: `cxo_research_brief.md` — pre-meeting intel
- **File 5**: `anticipated_qa.md` — 5 câu + answer
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 10 slide flow vision-led
- [ ] <7 từ/slide
- [ ] Speaker note 2-5 phút/slide
- [ ] Insight slide có "aha" moment
- [ ] CTA slide cuối cụ thể
- [ ] Backup appendix cho detail
- [ ] Customized cho CXO cụ thể
