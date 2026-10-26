---
name: ceo-news-radar
description: |
  Radar tin tức ngành tự động dùng WebSearch — quét báo chí, blog ngành, regulatory mỗi sáng, tóm tắt 5-7 tin quan trọng nhất ảnh hưởng tới doanh nghiệp.
  Kích hoạt khi người dùng nói: "news radar", "tin tức ngành", "radar ngành", "industry news CEO", "tin tức quan trọng hôm nay", "morning news", "newsletter ngành", "daily industry digest".
  Output là email digest + Slack post.
---

# CEO News Radar — Radar Tin Tức Ngành

## Mục Tiêu
CEO cần biết tin ngành quan trọng nhưng không có thời gian lướt 20 site. Radar tự động chọn 5-7 tin có ảnh hưởng nhất + tóm tắt 2 dòng + "why it matters".

## Khi Nào Dùng
- Hàng sáng 6-7h trước khi vào ngày
- Trước họp leadership thứ Hai
- Sau khi đi công tác lâu
- Khi có regulatory change ngành
- Trước họp đối tác lớn

## Bước 1: Cấu Hình Watchlist
- 5-10 keyword ngành (VD: "AI training Việt Nam", "SaaS B2B", "logistics")
- 5-10 đối thủ trực tiếp
- 3-5 regulator/government source (Bộ TT&TT, NHNN)
- 5-10 báo chí ngành (TechCrunch, VnExpress Kinh doanh, Forbes Vietnam)
- 3-5 thought leader (theo dõi blog)

## Bước 2: Quét Hàng Ngày
- WebSearch mỗi keyword trong 24h qua
- WebFetch trang RSS các báo ngành
- Lọc nhiễu: bỏ trùng, bỏ press release tự khen, bỏ tin > 7 ngày
- Score relevance:
  - Tác động trực tiếp (đối thủ, regulator) = 10
  - Trend ngành = 7
  - Tổng quan kinh tế = 4

## Bước 3: Tóm Tắt 5-7 Tin Quan Trọng
Mỗi tin format:
- **Headline** (đã rút gọn, không clickbait)
- **TL;DR** (2 dòng, ai làm gì khi nào)
- **Why it matters** (1 dòng cho CEO)
- **Source link** (URL ngắn)

Phân loại: Critical / Important / Nice-to-know.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: quét tin 24h từng keyword
- WebFetch: lấy nội dung article để tóm tắt
- Gmail MCP: gửi digest email 6h sáng
- Slack MCP: post lên #industry-news
- Notion MCP: lưu archive để tham khảo sau

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# RSS feed tổng hợp
import feedparser
feeds = [
  "https://vnexpress.net/rss/kinh-doanh.rss",
  "https://techcrunch.com/feed/",
  "https://www.forbesvietnam.com.vn/feed"
]
items = []
for f in feeds:
    parsed = feedparser.parse(f)
    items.extend(parsed.entries[:10])
# Lọc 24h, score, lấy top 7
```

## Bước 5: Output Format
- Email digest:
  - Subject: "Radar [Date] | [Top critical]"
  - HTML với 3 phần Critical/Important/Nice
  - 400-600 từ tổng
- Slack post ngắn 200 từ
- Notion archive page hàng ngày
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/radar/YYYY-MM-DD.md`

## Checklist Trước Khi Giao
- [ ] Tối đa 7 tin (đừng spam)
- [ ] Mỗi tin có "why it matters" 1 dòng
- [ ] Source verify (không fake news)
- [ ] Dưới 600 từ
- [ ] Gửi đúng 6h sáng
- [ ] Tin trùng đã dedupe
