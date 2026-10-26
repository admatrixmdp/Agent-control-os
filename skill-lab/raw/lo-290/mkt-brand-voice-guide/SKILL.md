---
name: mkt-brand-voice-guide
description: |
  Soạn brand voice guideline cho doanh nghiệp Việt Nam — gồm 4 trục tone, do/don't, example trên mỗi kênh, glossary. Kích hoạt khi người dùng nói: "brand voice guide", "tone of voice", "guideline giọng nói thương hiệu", "tone brand", "writing guideline", "viết brand voice", "guideline copywriting", "voice & tone". Output là PDF guide + Markdown copy.
---

# Brand Voice Guide — Do/Don't + Example

## Mục Tiêu
Mọi người viết content/email/CS đều có cùng "giọng", brand nhất quán cross-channel, giảm 60% thời gian QA copy.

## Khi Nào Dùng
- Brand mở rộng team content
- Outsource content cho agency/freelancer
- Tái định vị brand
- Sau khi viết positioning xong
- Onboard content writer mới

## Bước 1: Brief Brand Voice
Hỏi:
1. Tính cách brand (3-5 tính từ)
2. Nếu brand là người, ai là celeb VN gần nhất?
3. Audience giao tiếp (tuổi, formal/casual)
4. Brand không bao giờ là gì (anti-persona)
5. Sản phẩm/kênh chính
6. Ngôn ngữ (VI / EN / song ngữ)

## Bước 2: 4 Trục Voice Spectrum
Mỗi trục 1-5 scale:
- **Formal ←→ Casual**
- **Serious ←→ Playful**
- **Expert ←→ Friend**
- **Conservative ←→ Bold**

Chọn vị trí cho brand. Ví dụ Tech B2B SaaS: Casual 4, Playful 2, Friend 3, Bold 4.

## Bước 3: Soạn Do/Don't + Example Per Channel
Mỗi kênh (FB, IG, TikTok, Email, Website, CS chat, Slide bán hàng) có:
- Tone phù hợp kênh
- 5 ví dụ DO (câu nên dùng)
- 5 ví dụ DON'T (câu cấm dùng)
- Format style (emoji, dấu câu, viết hoa)
- Glossary từ ngữ brand quen dùng / né tránh
- POV (xưng "mình"/"chúng tôi"/"TAKI"...)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Notion MCP: trang Brand Voice public
- Google Drive MCP: lưu PDF guide
- Slack MCP: pin để team xem
- WebSearch: tham khảo guide best-in-class (Mailchimp, Slack, Atlassian)
- Figma MCP: brand mood board visual

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Build guide HTML từ template Jinja
import jinja2
template = open('voice_guide_template.html').read()
html = jinja2.Template(template).render(
  brand_name=name, spectrum=spectrum_data,
  do_donts=channels_dodont, glossary=glossary)
open('outputs/brand_voice_guide.html','w').write(html)
```

## Bước 5: Output Format
- File PDF `Brand_Voice_Guide_<brand>.pdf`
- File `.md` để paste Notion
- Cheat sheet 1 trang cho writer
- Audio guide ngắn 5p (tùy chọn)
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 4 trục voice xác định rõ
- [ ] Do/Don't mỗi kênh >=5 ví dụ
- [ ] Glossary >=20 từ
- [ ] Có cheat sheet 1 trang
- [ ] Đã test với writer/agency
- [ ] Quote founder approve
