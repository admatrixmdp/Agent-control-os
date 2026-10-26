---
name: mkt-instagram-reel-script
description: |
  Viết script Instagram Reel 15-30 giây với hook viral, transition cue, on-screen text cho doanh nghiệp Việt Nam. Tự động sinh 10 phương án hook + chọn hook tốt nhất. Kích hoạt khi người dùng nói: "viết script Reel", "viết Reel IG", "script Reel 15s 30s", "Reel viral hook", "kịch bản Reel Instagram", "viết Reel sản phẩm", "Reel content idea", "Reel hook viral". Output là Markdown + bảng shotlist từng giây.
---

# Script Instagram Reel 15-30s Viral Hook

## Mục Tiêu
Sản xuất Reel có khả năng viral cao: hook giữ chân 70%+ sau 3s, on-screen text rõ, CTA cuối, phù hợp thuật toán IG 2026.

## Khi Nào Dùng
- Brand mới chuyển sang Reels
- Cần content batch 10-30 Reels
- Đẩy reach hữu cơ không chạy ads
- Repurpose từ TikTok sang IG
- Launch sản phẩm cần Reel demo

## Bước 1: Brief Reel
Hỏi:
1. Mục tiêu (educate/entertain/sell)
2. Sản phẩm/topic
3. Độ dài (15/30s)
4. Tài nguyên (sản phẩm thực, model, location)
5. Audio (trending/voiceover/no sound)
6. Brand color overlay

## Bước 2: Sinh 10 Hook
Áp dụng các formula:
- "Tôi đã thử... và đây là điều xảy ra"
- "3 lỗi ai cũng mắc khi..."
- "Bạn biết... nhưng không biết..."
- "POV: bạn là..."
- "Lý do bạn vẫn..."
- Số liệu shock: "90% doanh nghiệp..."
- Câu hỏi: "Bạn có biết...?"
Chọn 1 hook mạnh nhất.

## Bước 3: Script Per Second
| Giây | Visual | Text overlay | Voiceover |
|---|---|---|---|
| 0-3 | Hook visual | Hook text | Hook line |
| 3-8 | Setup | ... | ... |
| 8-25 | Payoff | ... | ... |
| 25-30 | CTA | "Follow để xem tiếp" | CTA voice |

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tra audio trend IG VN
- WebFetch: phân tích Reel top niche
- Google Drive MCP: lưu shotlist
- Notion MCP: pipeline Reel
- Meta Graph API connector (nếu có): schedule post

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Schedule Reel qua Meta Graph API
import requests
r = requests.post(f'https://graph.facebook.com/v18.0/{ig_id}/media',
  data={'media_type':'REELS','video_url':video_url,
        'caption':caption,'access_token':TOKEN})
container_id = r.json()['id']
requests.post(f'https://graph.facebook.com/v18.0/{ig_id}/media_publish',
  data={'creation_id':container_id,'access_token':TOKEN})
```

## Bước 5: Output Format
- File `.md` script + shotlist từng giây
- 10 hook variations để A/B
- Caption + 15-20 hashtag mix
- CTA chính + sticker gợi ý
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Hook đủ mạnh trong 3s đầu
- [ ] Transition rõ mỗi 3-5s
- [ ] Có on-screen text suốt video
- [ ] CTA cuối rõ ràng
- [ ] Audio chọn từ trending
- [ ] Caption tối ưu SEO IG
