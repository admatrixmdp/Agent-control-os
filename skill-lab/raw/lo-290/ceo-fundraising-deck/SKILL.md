---
name: ceo-fundraising-deck
description: |
  Tạo pitch deck gọi vốn Series A/B 12-15 slides chuẩn quốc tế — gồm problem, solution, traction, market, team, ask. Phù hợp pitch VC Việt Nam + SEA.
  Kích hoạt khi người dùng nói: "pitch deck", "deck gọi vốn", "fundraising deck", "Series A deck", "Series B deck", "raise vốn startup", "VC deck", "tạo pitch deck", "kêu gọi đầu tư".
  Output là file .pptx 12-15 slides.
---

# CEO Fundraising Deck — Pitch Deck Gọi Vốn Series A/B

## Mục Tiêu
Pitch deck quyết định 80% việc có gặp được VC lần 2. Skill này tạo deck 12-15 slides theo template proven của a16z/YC/Sequoia, vừa đủ ngắn để VC đọc trong 5 phút.

## Khi Nào Dùng
- Mở round Series A/B
- Bridge round trước Series chính
- Strategic round với corporate
- Convert SAFE/note thành round
- Re-deck sau khi feedback từ 10 VC đầu

## Bước 1: Thu Thập Story Materials
- 1 câu mô tả công ty (elevator pitch)
- Problem CEO nhìn thấy (founder market fit)
- Số traction 12 tháng gần nhất
- TAM/SAM/SOM
- Team key (3-5 người)
- Số raise + use of funds
- Round trước (size, lead, valuation)

## Bước 2: 12 Slide Format Chuẩn
1. Cover (logo, 1 dòng tagline)
2. Problem (3 bullet, có số đau)
3. Solution (sản phẩm + 1 hình)
4. Why now (3 trend hội tụ)
5. Market (TAM/SAM/SOM, bottom-up)
6. Product (screenshot/demo)
7. Traction (revenue chart, hockey stick)
8. Business model (pricing + unit economics)
9. Go-to-market (kênh chính)
10. Competition (2x2 matrix)
11. Team (4-6 người có credentials)
12. Ask (size raise + use + milestone đạt được)
+ Optional: 13-15 (deep dive metric, roadmap, financials)

## Bước 3: Quy Tắc Slide Design
- 1 slide = 1 message
- Headline câu khẳng định, không câu hỏi
- Mỗi số có context (vs ngành, vs năm trước)
- Hockey stick chart bắt buộc cho traction
- TAM phải bottom-up + có nguồn
- Team có logo công ty trước

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Canva MCP: dùng template VC deck có sẵn
- Google Drive MCP: pull data financial từ Sheets
- WebSearch: lấy TAM data từ Statista, similar comps
- Notion MCP: lưu deck version + VC feedback
- Gmail MCP: track deck open qua DocSend integration

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
from pptx import Presentation
from pptx.util import Inches, Pt
prs = Presentation()
prs.slide_width = Inches(13.33)
prs.slide_height = Inches(7.5)
# Slide 7 - Traction
slide = prs.slides.add_slide(prs.slide_layouts[5])
slide.shapes.title.text = "$1M ARR in 12 months"
# Add chart hockey stick...
prs.save('/tmp/pitch-deck.pptx')
```

## Bước 5: Output Format
- File `.pptx` 12-15 slides ratio 16:9
- 1 version PDF để gửi (không edit được)
- Tên: `pitchdeck-[company]-SeriesA-vN.pptx`
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`
- Speaker notes cho từng slide (60-100 từ)

## Checklist Trước Khi Giao
- [ ] Có đủ 12 slide bắt buộc
- [ ] Traction slide có hockey stick chart thật
- [ ] TAM bottom-up + có nguồn
- [ ] Team slide có logo công ty trước
- [ ] Ask rõ ràng: $X for Y months to reach Z
- [ ] Đã test gửi DocSend xem trang nào VC dừng lâu
