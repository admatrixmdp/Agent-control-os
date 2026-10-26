---
name: mkt-youtube-script-writer
description: |
  Viết script video YouTube dài 8-15 phút cho kênh doanh nghiệp/founder Việt Nam, tối ưu retention với hook 15s, pattern interrupt, B-roll cue và CTA. Kích hoạt khi người dùng nói: "viết script YouTube", "viết kịch bản video YouTube", "viết long-form YouTube", "viết script video 10 phút", "kịch bản kênh YouTube công ty", "viết content YouTube", "viết video founder", "script YouTube SEO". Output là Markdown có timestamp + bảng shotlist.
---

# Viết Script Video YouTube 8-15 Phút

## Mục Tiêu
Sản xuất script video dài hấp dẫn giữ retention >50% (benchmark YouTube), giúp kênh đạt YPP nhanh và xây thẩm quyền thương hiệu/cá nhân.

## Khi Nào Dùng
- Founder kênh personal cần long-form
- Brand muốn tutorial/educational chuyên sâu
- Đẩy SEO YouTube cho keyword cao
- Repurpose từ podcast/webinar
- Chuẩn bị batch quay 5-10 video

## Bước 1: Brief Video
Hỏi:
1. Chủ đề + keyword chính
2. Đối tượng (level người xem)
3. Mục tiêu (educate/sell/inspire/grow)
4. Độ dài mong muốn (8/10/12/15p)
5. POV/USP của host
6. Tài liệu tham khảo nội bộ
7. CTA cuối (sub/khóa học/download)

## Bước 2: Cấu Trúc Script
- **0:00-0:15 Hook**: câu nói gây tò mò + promise điều gì
- **0:15-0:45 Stakes**: tại sao quan trọng + intro host
- **0:45-1:30 Roadmap**: 3-5 điểm sẽ cover
- **Phần thân (6-10p)**: chia 3-5 chương, mỗi chương 90s-2p, có pattern interrupt mỗi 45s
- **CTA mid-roll (giữa video)**: nhắc sub/like
- **Conclusion (1-2p)**: recap + CTA chính + teaser video tiếp

## Bước 3: Viết Chi Tiết
- Câu nói < 15 từ
- Mỗi 45s phải có chuyển cảnh / B-roll / animation / on-screen text
- Chèn cue [B-ROLL: ...], [ZOOM IN], [TEXT OVERLAY: ...]
- Tránh đoạn talking head >30s liên tục
- Có ít nhất 3 storytelling/example trong video

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tra số liệu + ví dụ thực tế
- WebFetch: phân tích top 5 video YouTube đang rank keyword
- Google Drive MCP: lưu script + shotlist
- Notion MCP: pipeline sản xuất YouTube
- YouTube Data API connector: kéo title/desc top video

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Lấy thông tin top video competing keyword
from googleapiclient.discovery import build
yt = build('youtube','v3', developerKey=API_KEY)
res = yt.search().list(q='đào tạo AI doanh nghiệp',
    part='snippet', type='video', maxResults=10,
    order='viewCount', regionCode='VN').execute()
```

## Bước 5: Output Format
- File `.md` script đầy đủ có timestamp
- File `.xlsx` shotlist (cảnh / B-roll / props / location)
- Title 5 phương án + Description SEO + Tags + Thumbnail brief
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Hook 15s đủ gây tò mò
- [ ] Roadmap rõ trước phút 1:30
- [ ] Pattern interrupt mỗi 45s
- [ ] Có 3 storytelling
- [ ] CTA giữa + cuối video
- [ ] Title + thumbnail brief đính kèm
- [ ] Description có timestamp + link
