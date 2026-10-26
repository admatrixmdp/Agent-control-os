---
name: mkt-twitter-thread-writer
description: |
  Viết Twitter/X thread 8-12 tweet viral cho founder/brand Việt Nam (tiếng Việt hoặc tiếng Anh), tối ưu để retweet và follow. Tự động cấu trúc Hook → Stakes → Insight → Story → CTA. Kích hoạt khi người dùng nói: "viết Twitter thread", "viết X thread", "thread viral", "viết chuỗi tweet", "viết tweet dài", "X content founder", "Twitter B2B", "viết thread founder". Output là Markdown numbered tweet.
---

# Viết Twitter/X Thread 8-12 Tweet Viral

## Mục Tiêu
Sản xuất thread giữ chân người đọc đến cuối (completion rate >40%), tăng follower 50-200/thread tốt, biến X thành kênh xây personal brand cho founder/exec VN.

## Khi Nào Dùng
- Founder xây tệp 10k-100k follow
- B2B SaaS đẩy thought leadership
- Cộng đồng dev/marketer/builder
- Sau khi đạt milestone đáng share
- Repurpose nội dung từ blog/podcast

## Bước 1: Brief Thread
Hỏi:
1. Chủ đề chính
2. POV độc đáo
3. Đối tượng (founder/dev/marketer VN hay global)
4. Ngôn ngữ (VI/EN)
5. Mục tiêu (follow/click/engage)
6. Số tweet mong muốn (8/10/12)
7. CTA cuối (sub newsletter, follow, link blog)

## Bước 2: Cấu Trúc Thread
- Tweet 1 (Hook): câu shock + promise + emoji nhẹ. <280 ký tự nhưng impact mạnh.
- Tweet 2-3 (Stakes): tại sao quan trọng + context
- Tweet 4-9 (Insights): mỗi tweet 1 idea/example/framework
- Tweet 10-11 (Story): minh họa thật của bạn
- Tweet cuối (CTA): "Nếu bạn thấy hữu ích, RT tweet 1 và follow @user để xem thêm"

## Bước 3: Viết Từng Tweet
Quy tắc:
- Mỗi tweet 1 ý duy nhất
- Câu ngắn, có khoảng trắng giữa các dòng
- Số liệu cụ thể, không chung chung
- Tránh hashtag (giảm engagement trên X)
- Có ít nhất 2 contrarian take
- Tweet 7-8 nên là tweet có khả năng quote nhất

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tra số liệu, ví dụ thực tế
- WebFetch: lấy nội dung blog gốc để repurpose
- Twitter/X MCP (nếu có): schedule thread qua Typefully/Tweet Hunter
- Google Drive MCP: lưu draft
- Notion MCP: archive thread library

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Post thread qua Twitter API v2
import tweepy
client = tweepy.Client(consumer_key=CK, consumer_secret=CS,
  access_token=AT, access_token_secret=ATS)
prev_id = None
for tweet_text in thread:
    res = client.create_tweet(text=tweet_text,
      in_reply_to_tweet_id=prev_id)
    prev_id = res.data['id']
```

## Bước 5: Output Format
- File `.md` numbered 1/n, 2/n, ...
- Character count mỗi tweet
- Hình ảnh gợi ý cho tweet 1 và tweet cuối
- 3 phiên bản tweet 1 để A/B
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Hook tweet 1 mạnh, <280 ký tự
- [ ] Mỗi tweet 1 ý
- [ ] Có 2 contrarian take
- [ ] Có 1-2 ví dụ cá nhân/case
- [ ] CTA cuối có RT + follow
- [ ] Đã preview trên mobile X
