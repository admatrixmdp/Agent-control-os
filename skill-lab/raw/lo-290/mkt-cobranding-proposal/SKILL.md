---
name: mkt-cobranding-proposal
description: |
  Soạn đề xuất hợp tác cobrand giữa doanh nghiệp Việt Nam với đối tác — value proposition, mechanic, KPI, contract draft. Kích hoạt khi người dùng nói: "viết cobrand proposal", "đề xuất hợp tác thương hiệu", "co-marketing proposal", "deck cobranding", "partnership marketing", "đề xuất cobrand", "co-promotion deal", "viết proposal partnership". Output là Slide PPTX + Markdown contract draft.
---

# Đề Xuất Hợp Tác Cobrand

## Mục Tiêu
Mỗi tháng pitch được 5-10 cobrand deal có khả năng đóng, tăng reach + lower CAC bằng cách dùng tệp KH lẫn nhau.

## Khi Nào Dùng
- Cùng audience, không cạnh tranh
- Có sản phẩm bổ trợ
- Cần mở rộng tệp nhanh
- Tổ chức event/gift box chung
- Trao đổi nội dung/email list

## Bước 1: Brief Partner
Hỏi:
1. Brand của mình + tệp KH
2. Partner mục tiêu + tệp KH
3. Loại hợp tác (gift box, email swap, event chung, sản phẩm chung, content)
4. Mục tiêu (reach, lead, sales, brand)
5. Giá trị mình mang lại
6. Giá trị nhận về
7. Thời gian cam kết

## Bước 2: Soạn Value Proposition
**Win-Win logic**:
- Mình có gì partner thiếu (tệp / chuyên môn / kênh)
- Partner có gì mình thiếu
- Khách hàng cuối được lợi gì
- Tại sao bây giờ (timing)

Format 3 bullet rõ ràng.

## Bước 3: Thiết Kế Mechanic + Deck
**Mechanic**: chi tiết cách hoạt động.
Ví dụ Gift Box Tết:
- 1.000 box, mỗi box có sản phẩm A của mình + B của partner
- Phân phối 50/50 qua tệp KH mỗi bên
- Đo bằng coupon code + UTM riêng
- KPI: 200 ref/bên, CR >5%

**Deck pitch 10 slide**:
1. Cover
2. About us
3. About you (partner)
4. Why partner
5. Audience overlap
6. Proposed mechanic
7. KPI + measurement
8. Timeline
9. Investment from both
10. Next steps + contact

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: research partner (số liệu công khai)
- WebFetch: lấy info partner từ website/LinkedIn
- Slides/PPTX MCP: tạo deck
- Gmail MCP: gửi pitch + theo dõi reply
- Notion MCP: partnership pipeline
- DocuSign MCP (nếu có): ký MOU

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tự sinh slide PPTX
from pptx import Presentation
from pptx.util import Inches, Pt
prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = 'Cobrand Proposal: TAKI x Partner'
slide.placeholders[1].text = 'Win-Win partnership 2026'
# ... add slides for Audience, Mechanic, KPI...
prs.save('outputs/cobrand_proposal.pptx')
```

## Bước 5: Output Format
- File `.pptx` deck 10 slide
- File `.md` MOU draft 2 trang
- Email pitch + follow-up template
- KPI tracking sheet
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Value prop rõ Win-Win
- [ ] Mechanic chi tiết đo được
- [ ] Audience overlap có số liệu
- [ ] KPI 2 phía cân bằng
- [ ] Timeline + cam kết rõ
- [ ] MOU draft sẵn sàng
- [ ] Contact + next steps cụ thể
