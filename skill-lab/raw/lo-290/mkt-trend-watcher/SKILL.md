---
name: mkt-trend-watcher
description: |
  Theo dõi trend hàng tuần qua Google Trends, TikTok Creative Center, X trending VN/global cho doanh nghiệp Việt Nam. Tự động tổng hợp insight và đề xuất content bám trend. Kích hoạt khi người dùng nói: "theo dõi trend", "Google Trends report", "TikTok trend tuần", "xu hướng marketing", "trend watcher", "bám trend content", "viral trend VN", "trend tuần này". Output là báo cáo HTML weekly + 5 content idea.
---

# Trend Watcher Weekly — Google Trends + TikTok

## Mục Tiêu
Mỗi thứ 2 nhận 1 báo cáo trend tuần để team content/ads/social biết "đu sóng" cái gì, tránh đăng nội dung lạc lõng với thị hiếu.

## Khi Nào Dùng
- Báo cáo trend tuần
- Brief content viral
- Plan campaign theo mùa/sự kiện
- Ra sản phẩm bám trend
- Phản ứng nhanh với hot topic

## Bước 1: Thiết Lập Niche Theo Dõi
Hỏi:
1. Ngành chính
2. 5-10 keyword theo dõi cố định
3. Vùng địa lý (VN / HCM / HN / Asia)
4. Tần suất (weekly/daily)
5. Output gửi đi đâu (Slack/email)
6. Loại trend ưu tiên (sản phẩm, meme, văn hóa, sự kiện)

## Bước 2: Quét Nguồn Trend
- **Google Trends**: rising/breakout query cuối tuần
- **TikTok Creative Center**: top trending sound, hashtag VN
- **X Trending**: top hashtag VN
- **Facebook Ad Library**: ads tăng đột biến
- **YouTube Trending**: top video VN
- **Báo lớn**: tin nóng tuần (VnExpress, CafeF, Vietcetera)

## Bước 3: Tổng Hợp & Sinh Idea
Phân loại trend:
- LONG-LASTING (>1 tháng): đáng đầu tư content/sản phẩm
- WEEKLY HOT (1-4 tuần): kịp ride wave
- 24-48h: phản ứng nhanh meme/sự kiện

Mỗi trend sinh 1-3 content idea cụ thể cho brand: angle, hook, format.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: query Google Trends explore
- WebFetch: scrape TikTok Creative Center
- Slack MCP: gửi daily/weekly digest
- Notion MCP: trend library
- Google Sheets MCP: log trend ride

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Pull Google Trends unofficial
from pytrends.request import TrendReq
pytrends = TrendReq(hl='vi-VN', tz=420)
pytrends.build_payload(['AI doanh nghiệp','khóa học AI'],
  geo='VN', timeframe='now 7-d')
df = pytrends.interest_over_time()
related = pytrends.related_queries()
rising = related['AI doanh nghiệp']['rising']
```

## Bước 5: Output Format
- File HTML báo cáo weekly:
  - Top 5 trend (chart + giải thích)
  - 5-10 content idea
  - Slack digest 5 bullet
- File `.md` cho Notion archive
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Quét đủ 6 nguồn
- [ ] Phân loại theo lifespan
- [ ] >= 5 content idea sẵn sàng triển khai
- [ ] Có nguồn link tham khảo
- [ ] Gửi đúng kênh team
- [ ] Trend không trùng tuần trước
