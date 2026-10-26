---
name: ceo-board-deck
description: |
  Tạo deck báo cáo Hội Đồng Quản Trị (HĐQT) 15-20 slides chuẩn — gồm executive summary, financial, OKR, chiến lược, rủi ro, ask. Format chuyên nghiệp dùng cho board meeting hàng quý.
  Kích hoạt khi người dùng nói: "deck HĐQT", "board deck", "slide báo cáo hội đồng", "deck cho board", "tài liệu HĐQT quý", "slide cho cuộc họp board", "deck cổ đông", "board pack".
  Output là file .pptx 15-20 slides.
---

# CEO Board Deck — Deck Báo Cáo HĐQT

## Mục Tiêu
Mỗi quý CEO phải đứng trước HĐQT 60-90 phút. Deck phải vừa cô đọng, vừa show được tiến độ, vừa xin được vốn/quyết định. Skill này tạo deck chuẩn 15-20 slide trong 30 phút thay vì 2 ngày.

## Khi Nào Dùng
- Board meeting quý (Q1/Q2/Q3/Q4)
- Trước extraordinary board meeting (M&A, vốn)
- Annual board off-site
- Khi có thành viên board mới cần onboarding

## Bước 1: Hỏi Input Chính
1. Quý báo cáo + năm
2. Doanh thu/lợi nhuận/burn quý
3. 3 thành tựu lớn nhất
4. 3 vấn đề lớn nhất
5. Ask cần xin board (vốn, quyết định, kết nối)
6. Tone: confident vs cautious

## Bước 2: Cấu Trúc 15-20 Slide Chuẩn
1. Cover (quý, ngày, agenda)
2. Executive summary (1 slide, 3 highlight + 3 lowlight)
3-4. Financial: P&L summary + Cash position
5. KPI dashboard (north-star + 5 metrics)
6. OKR progress (Q này)
7-8. Sales & Marketing (funnel + pipeline)
9. Product roadmap
10. Operations & quality
11. People & culture (headcount, attrition)
12. Strategic initiatives update
13-14. Risk register + mitigation
15. Competitive landscape
16-17. Next quarter plan + OKR
18. Asks & decisions needed
19. Appendix
20. Q&A

## Bước 3: Quy Tắc Trình Bày
- 1 slide = 1 message
- Số phải lớn (44pt+), context nhỏ hơn
- Dùng màu công ty + xanh/đỏ cho positive/negative
- Tránh slide chữ đặc — max 50 từ/slide
- Mọi slide tài chính có nguồn ở footer
- Slide rủi ro phải có owner + mitigation

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: pull số tài chính từ Sheets monthly close
- Notion MCP: lấy OKR + risk register
- Linear MCP: lấy roadmap product
- Gmail MCP: gửi deck cho board members + tracking open
- Canva MCP: nếu công ty có brand kit trên Canva, dùng `create-design-from-brand-template`

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tạo pptx bằng python-pptx
from pptx import Presentation
from pptx.util import Inches, Pt
prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[5])
slide.shapes.title.text = "Q2 2026 Board Review"
prs.save('/tmp/board-deck.pptx')
```

## Bước 5: Output Format
- File `.pptx` 15-20 slides, ratio 16:9
- Tên: `board-deck-Q#-YYYY-v#.pptx`
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`
- Kèm 1 file PDF preview để gửi trước
- Speaker notes có sẵn cho từng slide (50-80 từ)

## Checklist Trước Khi Giao
- [ ] Đủ 15-20 slides, không thừa không thiếu
- [ ] Mọi số tài chính có nguồn
- [ ] Risk section có owner + mitigation
- [ ] Slide Asks rõ ràng: xin gì, từ ai, deadline
- [ ] Speaker notes đầy đủ
- [ ] Không có lỗi chính tả tên thành viên board
