---
name: cs-social-media-listening
description: |
  Hệ thống lắng nghe mention thương hiệu trên Facebook / Instagram / TikTok / Google Review — phân loại tích cực/tiêu cực/cần phản hồi, alert team CS xử lý nhanh. Dùng skill này khi người dùng yêu cầu: "social listening", "monitor brand mention", "theo dõi FB comment", "alert tiêu cực social", "TikTok mention brand", "phản hồi review online", "social CS monitoring", "crisis early warning". Output là dashboard + Slack alert + Excel report.
---

# CS Social Media Listening System

## Mục Tiêu
Theo dõi mọi mention thương hiệu (post, comment, review, hashtag) trên FB/IG/TikTok/Google → phân loại sentiment → alert team CS xử lý trong < 1h. Phát hiện crisis sớm trước khi viral.

## Khi Nào Dùng
- Brand bị review tiêu cực không ai biết → viral
- Comment chửi trên FB không ai trả lời
- Cạnh tranh tag tên brand → cần phản ứng
- Influencer/KOL nhắc đến → cần thank-you / engage
- Crisis management — early warning

## Bước 1: Liệt Kê Source Cần Monitor
| Source | Cách monitor | Frequency |
|---|---|---|
| Facebook Page (own) | Webhook real-time | Tức thời |
| Facebook Group | Manual + scraper | 2h/lần |
| Instagram (own + tagged) | API + Mention | 2h/lần |
| TikTok mention | TikTok API + hashtag | 4h/lần |
| Google Review | Google My Business API | Daily |
| Shopee/Lazada Review | Partner API | Daily |
| Báo điện tử | Google Alert + News API | Daily |
| Diễn đàn (Voz, Tinhte) | Manual + Brand24 | Daily |

## Bước 2: Phân Loại & Priority
**Sentiment classification:**
- Positive (khen) → engage thank-you, retweet
- Neutral (hỏi) → trả lời FAQ
- Negative (chê) → CS xử lý, có thể escalate
- Crisis (chửi + viral risk) → alert PR + Leadership

**Priority score:**
- Tier KOL/báo lớn → +50
- Sentiment Negative → +30
- Engagement > 1000 like/share → +20
- Tag tên CEO / brand cụ thể → +20

Score > 70 → Crisis alert ngay.

## Bước 3: SLA Phản Hồi Theo Sentiment
| Sentiment | SLA | Owner |
|---|---|---|
| Positive | 24h | Marketing |
| Neutral | 4h | CS Lv1 |
| Negative | 1h | CS Lv2 |
| Crisis | 15 phút | PR + Head CS + CEO |

Cuối tuần report: bao nhiêu mention, % trả lời đúng SLA, top 5 case nóng.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Slack MCP: alert channel #social-listening real-time
- Gmail MCP: gửi daily digest cho Marketing + CS Manager
- Google Sheets: log mọi mention + sentiment + handle
- WebSearch: monitor news mention brand
- WebFetch: kéo nội dung post/review để phân tích context
- Browser MCP (Claude in Chrome): screenshot post viral

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Pull mention FB + classify + alert
import requests, openai
FB_TOKEN = "..."
def scan_fb_mentions():
    r = requests.get(f"https://graph.facebook.com/v18.0/me/tagged?access_token={FB_TOKEN}")
    for post in r.json().get("data", []):
        sentiment = classify_sentiment(post["message"])
        score = priority_score(post, sentiment)
        log_to_sheet(post, sentiment, score)
        if score > 70:
            slack_alert_crisis(post)

def classify_sentiment(text):
    # Dùng OpenAI/Claude classify
    resp = openai.ChatCompletion.create(model="gpt-4",
        messages=[{"role": "user", "content": f"Phân loại sentiment: {text}. Trả lời: Positive/Neutral/Negative/Crisis"}])
    return resp.choices[0].message.content.strip()
```

## Bước 5: Output Format
- **Excel `Social_Listening.xlsx`**: mention log + sentiment + handle status
- **HTML dashboard** live: count theo source, sentiment chart, top mention
- **Slack alert template** cho từng level
- **Markdown crisis playbook**: ai liên hệ ai, phát ngôn mẫu
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-social-media-listening/output/`

## Checklist Trước Khi Giao
- [ ] Monitor đủ 5+ source
- [ ] Sentiment classify tự động > 80% chính xác
- [ ] SLA mỗi level rõ ràng
- [ ] Crisis playbook có người ký
- [ ] Dashboard real-time
- [ ] Daily digest email lúc 9h sáng
