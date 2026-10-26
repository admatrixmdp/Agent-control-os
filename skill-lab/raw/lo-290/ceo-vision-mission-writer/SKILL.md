---
name: ceo-vision-mission-writer
description: |
  Viết tầm nhìn (vision), sứ mệnh (mission), và giá trị cốt lõi (core values) cho doanh nghiệp — theo công thức proven của Patagonia/Stripe, không sáo rỗng, có khả năng test "5 năm sau còn đúng?".
  Kích hoạt khi người dùng nói: "viết vision", "viết mission", "tầm nhìn sứ mệnh", "core values", "giá trị cốt lõi", "vision mission writer", "vision statement", "viết tuyên ngôn công ty".
  Output là Markdown document + 1 trang poster.
---

# CEO Vision Mission Writer — Viết Tầm Nhìn Sứ Mệnh

## Mục Tiêu
Vision/Mission sáo rỗng (kiểu "trở thành công ty hàng đầu") không ai dùng. Skill này tạo ra V/M/V (vision, mission, values) cô đọng có khả năng định hướng quyết định và hiring 5+ năm.

## Khi Nào Dùng
- Mới thành lập công ty
- Sau pivot lớn về mô hình/ngành
- Trước round funding lớn cần "tell the story"
- Khi văn hoá đi xuống cần re-anchor
- Trước annual all-hands

## Bước 1: Phỏng Vấn Founder/CEO
10 câu hỏi để extract:
1. "Tại sao công ty này tồn tại?"
2. "Nếu công ty biến mất ngày mai, thế giới mất gì?"
3. "Ai là người được hưởng lợi nhất?"
4. "5 năm tới, công ty thay đổi điều gì lớn nhất?"
5. "Trong 10 năm, người ta sẽ nhớ công ty vì điều gì?"
6. "3 hành vi bạn không tha thứ ở nhân viên?"
7. "3 hành vi bạn sẽ promote ngay?"
8. "Khách hàng nói gì khi nói tốt về bạn?"
9. "Đối thủ làm cái gì bạn từ chối làm dù lời?"
10. "Nếu chỉ có 1 câu để định nghĩa, đó là gì?"

## Bước 2: Cấu Trúc 3 Thành Phần
**Vision** (10 năm): trạng thái thế giới khi mission thành công. 1 câu ≤ 15 từ.
VD: "Mỗi doanh nghiệp Việt biết dùng AI để vận hành."

**Mission** (hôm nay): công ty làm gì để tiến đến vision. 1-2 câu ≤ 25 từ.
VD: "Cung cấp đào tạo AI thực chiến và công cụ no-code để chủ DN tự động hoá vận hành."

**Core Values** (5-7 giá trị): hành vi cụ thể, có thể test khi hiring/firing.
- Không dùng từ trừu tượng (integrity, excellence)
- Dùng phrase actionable: "Ship every Friday", "Default to transparency"

## Bước 3: Test Chất Lượng
- **Specificity test**: nếu thay tên công ty khác vẫn đúng → quá vague
- **5 năm test**: 5 năm nữa còn đúng không?
- **Decision test**: gặp lựa chọn khó, V/M/V có giúp chọn không?
- **Hire/fire test**: có dùng để promote/sa thải được không?
- **Customer test**: khách hàng có hiểu trong 10 giây không?

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tham khảo vision/mission của Patagonia, Stripe, Tesla
- WebFetch: lấy V/M/V đối thủ để tránh trùng
- Notion MCP: lưu V/M/V có version history
- Canva MCP: tạo poster đẹp để treo văn phòng
- Slack MCP: post v final lên #general

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Generate poster bằng PIL
from PIL import Image, ImageDraw, ImageFont
img = Image.new('RGB', (1080, 1080), 'white')
d = ImageDraw.Draw(img)
d.text((100, 200), "VISION", font=font_big, fill='black')
d.text((100, 300), vision_text, font=font_med, fill='gray')
img.save('/tmp/vmv-poster.png')
```

## Bước 5: Output Format
- Markdown document `vmv-[company]-vN.md`
- 1-page PDF "credo" để in & treo
- Poster PNG/PDF cho lobby & Slack header
- Slide deck 5 trang để present all-hands
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Vision ≤ 15 từ
- [ ] Mission ≤ 25 từ
- [ ] 5-7 core values dạng hành vi
- [ ] Pass 5 test chất lượng
- [ ] Có ví dụ ứng dụng V/M/V trong quyết định
- [ ] Đã consult ít nhất 5 lãnh đạo chủ chốt
