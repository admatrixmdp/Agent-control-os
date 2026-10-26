---
name: mkt-tiktok-content-planner
description: |
  Lập kế hoạch content TikTok 30 ngày cho doanh nghiệp Việt Nam, gồm hook 3s, ý tưởng video, audio trending, hashtag, lịch đăng giờ vàng. Tự động chia 4 trụ cột Educate/Entertain/Inspire/Sell. Kích hoạt khi người dùng nói: "plan content TikTok", "lịch TikTok 30 ngày", "kế hoạch TikTok tháng", "content TikTok shop", "ý tưởng video TikTok", "TikTok content strategy", "lên kế hoạch TikTok", "lịch đăng TikTok". Output là Excel 30 dòng + brief 30 video.
---

# Plan Content TikTok 30 Ngày

## Mục Tiêu
Đảm bảo tài khoản TikTok đăng 1-2 video/ngày trong 30 ngày không bí ý tưởng, có hook viral và bám trend, tăng 50-100% reach so với đăng tự phát.

## Khi Nào Dùng
- Mới mở TikTok cho thương hiệu
- TikTok Shop cần content liên tục
- Account đang chững reach
- Chuẩn bị campaign lớn
- Cần brief cho creator/freelancer

## Bước 1: Brief Brand & Audience
Hỏi:
1. Ngành + sản phẩm
2. Persona TikTok (tuổi/giới/insight)
3. Tài khoản hiện có / mới
4. Mục tiêu (followers/views/sales)
5. Nhân sự quay (founder/KOC/team)
6. Ngân sách creator

## Bước 2: Phân Bổ 30 Video
Tỷ lệ:
- 12 video Educate (tips/how-to)
- 9 video Entertain (skit, POV, trend)
- 6 video Inspire (story khách hàng, behind the scene)
- 3 video Sell (review sản phẩm + link shop)

## Bước 3: Sinh Brief Từng Video
Mỗi video brief:
- Số thứ tự + ngày đăng + giờ vàng (12h, 19h, 21h)
- Hook 3s (câu hook viral)
- Plot 15-30s
- Audio trending (tìm trên Creative Center)
- Hashtag (mix big + niche)
- CTA cuối (comment/follow/shop)
- Props/đạo cụ
- Outfit/setting
- Caption + first comment

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tra TikTok Creative Center, top sound VN
- WebFetch: lấy hashtag trending từ TikTok Discover
- Google Sheets MCP: đẩy lịch lên Sheet team xem chung
- Notion MCP: tạo task quay từng video
- Google Drive MCP: lưu brief file

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Crawl Creative Center trending sound (semi-public)
import requests
url = 'https://ads.tiktok.com/business/creativecenter/inspiration/popular/music/pc/en'
r = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
# Parse HTML lấy top 100 sound + view count
```

## Bước 5: Output Format
- File `.xlsx`:
  - Sheet 1: Lịch 30 ngày
  - Sheet 2: 30 brief chi tiết
  - Sheet 3: Hashtag bank
  - Sheet 4: Audio trending bank
- Folder shotlist tham khảo (tuỳ chọn)
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 30 video phân bổ đủ 4 trụ cột
- [ ] Mỗi video có hook 3s rõ
- [ ] Mỗi video có audio gợi ý
- [ ] Lịch giờ vàng theo audience
- [ ] Caption + hashtag ready
- [ ] Có brief đủ chi tiết để creator quay luôn
