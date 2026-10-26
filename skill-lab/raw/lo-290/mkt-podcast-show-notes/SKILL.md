---
name: mkt-podcast-show-notes
description: |
  Soạn show notes podcast chuẩn cho doanh nghiệp/founder Việt Nam — gồm timestamp các chương, key quotes, resources mentioned, guest bio và CTA. Tự động transcribe và phân chương. Kích hoạt khi người dùng nói: "viết show notes podcast", "tóm tắt podcast", "timestamp podcast", "soạn show notes", "podcast description", "viết description tập podcast", "key quotes podcast", "podcast SEO description". Output là Markdown ready paste lên Spotify/Apple/Substack.
---

# Show Notes Podcast — Timestamp + Quotes + CTA

## Mục Tiêu
Mỗi tập podcast có show notes chuyên nghiệp giúp SEO, discoverability, tăng CTR vào website/sản phẩm. Tiết kiệm 1-2h biên tập cho host.

## Khi Nào Dùng
- Sau khi quay xong podcast/livestream
- Repurpose podcast cũ chưa có show notes
- Đẩy SEO Spotify/Apple Podcasts
- Cần tóm tắt cho email list/newsletter
- Phân phối lại lên blog text

## Bước 1: Thu Thập Asset
Hỏi:
1. File audio/transcript (hoặc link YouTube để pull)
2. Thông tin guest (tên, chức vụ, công ty, link mạng xã hội)
3. Sản phẩm/sách của guest cần promote
4. CTA tập (sub, đăng ký event, link blog)
5. Episode number + tựa đề

## Bước 2: Phân Chương + Timestamp
Phân thành 6-12 chương theo flow:
- 00:00 Intro + giới thiệu guest
- 02:30 Câu chuyện đầu sự nghiệp
- 08:15 Bài học lớn nhất
- ...
Mỗi chương có 1 dòng tóm tắt ngắn.

## Bước 3: Trích 5-10 Key Quotes
Chọn câu mạnh nhất từ transcript, format dạng quote block, ghi rõ giây xuất hiện. Đây là phần được share nhiều nhất.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebFetch: kéo transcript YouTube
- Whisper API connector: transcribe audio
- Spotify for Podcasters MCP (nếu có): update episode description
- Google Drive MCP: lưu show notes
- Notion MCP: archive episode database
- WebSearch: tra link sách/sản phẩm guest đề cập

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Transcribe bằng Whisper API
from openai import OpenAI
client = OpenAI()
with open('podcast.mp3','rb') as f:
    tr = client.audio.transcriptions.create(
      model='whisper-1', file=f, response_format='verbose_json',
      timestamp_granularities=['segment'])
for seg in tr.segments[:5]:
    print(seg['start'], seg['text'])
```

## Bước 5: Output Format
- File `.md` show notes hoàn chỉnh:
  - Episode title + cover image brief
  - Episode description SEO 150 từ
  - Guest bio
  - Timestamp chapters
  - Key quotes
  - Resources & links
  - CTA
- Thread X repurpose 8 tweet
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Timestamp chính xác (kiểm tra ngẫu nhiên 3 chương)
- [ ] 5-10 key quotes
- [ ] Đủ guest bio + link
- [ ] Resources có link
- [ ] CTA rõ ràng
- [ ] SEO keyword chính trong description
- [ ] Đã chunk repurpose social
