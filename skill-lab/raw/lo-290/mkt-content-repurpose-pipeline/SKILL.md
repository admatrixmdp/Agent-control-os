---
name: mkt-content-repurpose-pipeline
description: |
  Pipeline tái sử dụng 1 video gốc/blog → 10+ định dạng content cho doanh nghiệp Việt Nam (Reel, TikTok, Tweet thread, Carousel, Email, Newsletter, Podcast, Blog). Kích hoạt khi người dùng nói: "repurpose content", "tái sử dụng content", "1 video 10 dạng", "biến content thành đa kênh", "content pipeline", "multiply content", "content recycling", "tận dụng content cũ". Output là folder asset + lịch phát.
---

# Pipeline Tái Sử Dụng Content (1 → 10+)

## Mục Tiêu
Một sản phẩm content (video YouTube 30p / podcast 60p / blog 2000 từ) sinh ra 10+ asset cho FB, IG, TikTok, X, LinkedIn, Email, Pinterest, Reddit — tiết kiệm 70% chi phí sản xuất.

## Khi Nào Dùng
- Team content nhỏ cần scale output
- Vừa quay được video dài
- Sau podcast/webinar/livestream
- Bài blog top traffic muốn squeeze thêm
- Tận dụng content cũ chưa khai thác

## Bước 1: Brief Content Gốc
Hỏi:
1. Loại content gốc (video dài / podcast / blog / webinar)
2. URL/link asset
3. Chủ đề + key takeaway
4. Audience + brand voice
5. Kênh muốn phân phối (chọn từ FB/IG/TikTok/X/LinkedIn/Email/Pinterest)
6. Timeline phát (1 tuần / 1 tháng)

## Bước 2: Map 10+ Định Dạng Output
Từ 1 video 30 phút:
1. 5-8 Reels/TikTok 30-60s (cut highlight)
2. 1 YouTube Shorts
3. 2-3 carousel Instagram (insight chính)
4. 1 X thread 10 tweet
5. 1 LinkedIn long-form post
6. 1 blog 1500 từ
7. 1 newsletter email
8. 5-10 quote graphic
9. 1 audio podcast version
10. 1 SlideShare deck

## Bước 3: Pipeline Sản Xuất
Quy trình:
- Transcribe video gốc (Whisper)
- Highlight key moment (timestamps)
- Sinh outline cho từng format
- Brief designer/editor cho từng asset
- Schedule phát theo lịch optimal mỗi kênh

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebFetch: kéo transcript YouTube
- Whisper API connector: transcribe podcast
- Descript/Opus Clip MCP: auto-cut short clips
- Notion MCP: content pipeline board
- Buffer/Hootsuite MCP: schedule đa kênh
- Google Drive MCP: lưu asset

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Auto-transcribe + highlight via Whisper + LLM
from openai import OpenAI
from anthropic import Anthropic
o = OpenAI(); a = Anthropic()
with open('video.mp3','rb') as f:
    tr = o.audio.transcriptions.create(model='whisper-1', file=f).text
prompt = f'Tìm 8 highlight viral 30-60s từ transcript này:\n{tr}'
r = a.messages.create(model='claude-opus-4-5', max_tokens=2000,
  messages=[{'role':'user','content':prompt}])
```

## Bước 5: Output Format
- Folder asset chia theo định dạng
- File `.xlsx` lịch phát (kênh, ngày, asset, status)
- Brief từng asset cho team execute
- Tracker engagement sau phát
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 10+ định dạng đã list
- [ ] Mỗi định dạng có brief riêng
- [ ] Lịch phát theo giờ vàng từng kênh
- [ ] Asset ready để team execute
- [ ] Tracker engagement
- [ ] Có format primary + supporting
