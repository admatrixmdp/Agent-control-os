---
name: mkt-webinar-script
description: |
  Viết script webinar 60 phút cho doanh nghiệp B2B/B2C Việt Nam — cấu trúc Hook → Giá trị → Story → Pitch → Q&A → CTA, có timestamp và slide cue. Kích hoạt khi người dùng nói: "viết script webinar", "kịch bản webinar 60 phút", "script masterclass", "script training online", "viết bài giảng webinar", "viết script bán hàng webinar", "webinar funnel", "viết script livestream bán hàng". Output là Markdown có timestamp + slide outline.
---

# Script Webinar 60 Phút — Hook → Giá trị → CTA

## Mục Tiêu
Webinar có tỷ lệ stay-to-end >40%, conversion ra mua hàng/booking 5-15%, không "bán quá lộ liễu" mà người xem vẫn thấy giá trị.

## Khi Nào Dùng
- Bán khóa học/coaching online
- Demo SaaS B2B
- Nuôi lead cao cấp (high-ticket)
- Launch sản phẩm cần educate dài
- Workshop free funnel

## Bước 1: Brief Webinar
Hỏi:
1. Sản phẩm/khóa học cần bán
2. Giá + offer webinar
3. Persona dự
4. Đường dẫn vào webinar (FB ads/email/affiliate)
5. Mục tiêu (số người mua / booking)
6. Tài liệu chuyên môn host
7. Kênh: Zoom / Live FB / GoToWebinar

## Bước 2: Cấu Trúc 60 Phút
- **0-5p**: Welcome + Hook ("Bạn sẽ học gì 60p tới")
- **5-10p**: Story / authority của host (tại sao nghe)
- **10-25p**: Phần 1 - Frame mới (educate sâu, giá trị thật)
- **25-40p**: Phần 2 - Demo / case study / framework
- **40-50p**: Phần 3 - Pitch sản phẩm: vì sao đây là cách nhanh nhất + offer giới hạn
- **50-55p**: Q&A live xử lý objection
- **55-60p**: CTA cuối + scarcity

## Bước 3: Viết Chi Tiết Script
Mỗi block có:
- Lời nói chính của host
- Slide cue (slide số mấy, nội dung)
- Engagement prompt (poll, comment, react)
- Anchor (câu chốt quan trọng nhấn mạnh)
- Pattern interrupt mỗi 8-10p (story/poll/case)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Zoom MCP / Webinar platform: schedule webinar
- Email MCP: chuỗi reminder T-7/T-1/T-1h
- Google Slides MCP: tạo slide deck từ outline
- Notion MCP: webinar playbook
- WebSearch: số liệu để chèn vào script

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tạo webinar Zoom qua API
import requests
r = requests.post('https://api.zoom.us/v2/users/me/webinars',
  headers={'Authorization':f'Bearer {TOKEN}'},
  json={'topic':'Webinar Launch X','type':5,
    'start_time':'2026-06-10T19:00:00','duration':60,
    'settings':{'practice_session':True,'hd_video':True}})
```

## Bước 5: Output Format
- File `.md` script đầy đủ có timestamp
- Slide outline 25-35 slide
- Email reminder 3 phiên bản
- Q&A FAQ chuẩn bị sẵn
- Replay description + CTA
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Hook 5p đầu giữ người xem
- [ ] Có 3 pattern interrupt
- [ ] Offer chỉ pitch sau phút 40
- [ ] Scarcity hợp lý
- [ ] Q&A xử lý 5 objection lớn
- [ ] CTA cuối rõ ràng + link demo/mua
- [ ] Slide deck outline đính kèm
