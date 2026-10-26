---
name: mkt-banner-prompt-midjourney
description: |
  Viết prompt Midjourney/Imagen/Flux để tạo banner marketing chuyên nghiệp cho doanh nghiệp Việt Nam (banner FB, IG carousel, sale poster, web hero). Kích hoạt khi người dùng nói: "prompt Midjourney banner", "AI tạo banner", "prompt Imagen banner", "banner marketing AI", "prompt poster sale", "prompt thiết kế banner", "AI image prompt cho marketing", "Midjourney prompt VN". Output là Markdown prompt set.
---

# Prompt Midjourney/Imagen Cho Banner MKT

## Mục Tiêu
Tự thiết kế được banner đẹp bằng AI trong 15 phút thay vì đợi designer 3-5 ngày, chi phí gần 0đ, brand-consistent.

## Khi Nào Dùng
- Brand chưa có designer in-house
- Cần banner gấp trong ngày
- A/B test nhiều creative
- Banner mùa (Tết, BFCM, 8/3)
- Banner cho ads test

## Bước 1: Brief Banner
Hỏi:
1. Loại banner (FB cover 820x312, FB post 1200x630, IG carousel 1080x1080, web hero 1920x600)
2. Sản phẩm + USP
3. Tone (premium / vui tươi / minimal / Tết / Gen Z)
4. Brand color (hex code)
5. Phong cách (photorealistic / illustration / 3D / collage)
6. Có cần model / sản phẩm thật / cảnh nền
7. Headline + tagline text (overlay)

## Bước 2: Cấu Trúc Prompt Midjourney
Format chuẩn:
```
[chủ đề chính], [phong cách], [color palette], [lighting], 
[composition], [camera/lens], [aspect ratio] --ar 16:9 --v 6.1 --style raw
```

Ví dụ:
```
Vibrant promotional banner for Vietnamese AI training course,
modern flat illustration style, orange #F97316 and deep blue #1E40AF palette,
bright soft lighting, central composition with confident female entrepreneur 
using laptop, motivational and clean, minimal background with subtle AI circuit pattern,
photographic quality, --ar 16:9 --v 6.1 --style raw --no text
```

## Bước 3: Sinh 5-10 Prompt Variants
Cho mỗi banner mục tiêu:
- Variant 1: photorealistic
- Variant 2: illustration
- Variant 3: 3D render
- Variant 4: minimal/typography focused
- Variant 5: collage/scrapbook

Mỗi variant 3-5 prompt khác nhau để batch generate.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Midjourney via Discord MCP / Imagen API
- Flux API connector
- Canva MCP: chỉnh text overlay sau khi có ảnh
- Google Drive MCP: lưu banner
- Notion MCP: prompt library

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Gen ảnh qua Stability AI / Imagen / OpenAI Images
import requests
def gen_image(prompt, ar='16:9'):
    r = requests.post('https://api.stability.ai/v2beta/stable-image/generate/ultra',
      headers={'Authorization':f'Bearer {KEY}','Accept':'image/*'},
      files={'none':''},
      data={'prompt':prompt,'aspect_ratio':ar,'output_format':'png'})
    open(f'banner_{idx}.png','wb').write(r.content)
```

## Bước 5: Output Format
- File `.md` 5-10 prompt variants
- Batch generated PNG (chia subfolder theo banner type)
- Hướng dẫn chèn text overlay (Canva/Figma)
- Brand kit guideline áp dụng
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 5+ variant per banner
- [ ] Aspect ratio đúng platform
- [ ] Brand color trong prompt
- [ ] --no text để add bằng Canva
- [ ] Có version photo realistic + illustration
- [ ] Lưu library prompt thành công để reuse
