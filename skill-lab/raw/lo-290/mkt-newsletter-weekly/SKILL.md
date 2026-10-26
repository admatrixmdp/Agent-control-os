---
name: mkt-newsletter-weekly
description: |
  Soạn newsletter hàng tuần cho doanh nghiệp Việt Nam: curate 5-7 link giá trị + 1 insight độc quyền + 1 CTA. Tự động kéo tin tức trong tuần, tóm tắt và biên tập theo brand voice. Kích hoạt khi người dùng nói: "viết newsletter tuần", "soạn newsletter", "bản tin tuần", "curate newsletter", "viết bản tin tuần công ty", "weekly digest", "newsletter B2B", "viết bản tin gửi khách hàng". Output là HTML email + Markdown.
---

# Newsletter Tuần — Curate + Insight + CTA

## Mục Tiêu
Duy trì kết nối với danh sách email 1-4 lần/tháng bằng newsletter có giá trị thực sự, mở đầu tăng trust, không phải spam, đạt open rate >40%.

## Khi Nào Dùng
- Doanh nghiệp B2B/SaaS muốn nuôi lead dài hạn
- Founder muốn xây personal brand
- Cộng đồng học viên/khách hàng cần update tuần
- Bổ sung kênh giữ chân ngoài social
- Cross-promote content tuần qua

## Bước 1: Brief Brand & Audience
Hỏi:
1. Ngách + audience
2. Tone (chuyên gia / thân mật / hài)
3. 3-5 nguồn tin yêu thích (báo, blog, twitter)
4. Insight cá nhân tuần này
5. CTA tuần (event, sản phẩm, post)
6. Khung giờ phát hành (vd sáng thứ 2)

## Bước 2: Curate 5-7 Link
Dùng WebSearch + WebFetch lấy 15-20 tin trong tuần (Mon-Fri).
Lọc giữ 5-7 link đạt:
- Relevant audience
- Hữu ích thực sự (không clickbait)
- Chưa lan tỏa hết (chưa ai cũng share)
Mỗi link viết 2-3 dòng "tại sao đáng đọc".

## Bước 3: Viết Insight Độc Quyền
Block "Suy nghĩ tuần này" 150-250 từ chia sẻ góc nhìn cá nhân hoặc bài học từ công việc tuần qua. Đây là phần khác biệt giúp newsletter có chất riêng, KH theo dõi vì content này chứ không vì link curate.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tra tin tức ngách trong 7 ngày qua
- WebFetch: lấy tóm tắt từng bài
- Gmail MCP / Mailchimp MCP: tạo campaign sẵn schedule sáng thứ 2
- Notion MCP: lưu archive newsletter
- Google Drive MCP: lưu HTML
- RSS Feed Reader MCP: tự động kéo feed

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tự động kéo RSS feed nguồn yêu thích
import feedparser
feeds = ['https://vnexpress.net/rss/kinh-doanh.rss',
         'https://cafef.vn/cong-nghe.rss',
         'https://vietcetera.com/vn/rss']
items = []
for f in feeds:
    for e in feedparser.parse(f).entries[:10]:
        items.append({'title':e.title,'link':e.link,'summary':e.summary,
          'published':e.published})
items.sort(key=lambda x: x['published'], reverse=True)
top_curated = items[:7]
```

## Bước 5: Output Format
- File `.html` newsletter responsive ready paste vào ESP
- File `.md` để paste vào Substack/Beehiiv/Ghost
- Subject line A/B 2 phiên bản + preview text
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 5-7 link curated chất lượng
- [ ] 1 insight độc quyền 150-250 từ
- [ ] 1 CTA duy nhất rõ ràng
- [ ] Subject A/B 2 phiên bản
- [ ] Đã preview trên Gmail/Outlook
- [ ] Có link unsubscribe
- [ ] Lịch gửi cố định (vd 7h sáng thứ 2)
