---
name: mkt-pr-crisis-response
description: |
  Plan xử lý khủng hoảng truyền thông 24 giờ cho doanh nghiệp Việt Nam — protocol, thông điệp, phân vai, monitoring. Kích hoạt khi người dùng nói: "khủng hoảng truyền thông", "PR crisis", "xử lý scandal", "crisis response plan", "đối phó khủng hoảng PR", "phản ứng truyền thông xấu", "protocol khủng hoảng", "tuyên bố báo chí". Output là Markdown protocol + bộ statement.
---

# Xử Lý Khủng Hoảng Truyền Thông — 24h Plan

## Mục Tiêu
Khi xảy ra khủng hoảng (sản phẩm lỗi, leadership scandal, leak data, KH tố cáo viral), có protocol rõ trong 24h đầu — không để team panic + nói nhiều thứ mâu thuẫn.

## Khi Nào Dùng
- Đang trong khủng hoảng cần xử lý ngay
- Chuẩn bị playbook trước khi xảy ra
- Sau khủng hoảng để review lesson
- Đào tạo leadership / PR team
- Sau M&A thừa kế khủng hoảng

## Bước 1: Phân Loại Mức Độ
3 mức:
- **L1 (Low)**: 1-2 KH phàn nàn trên social, <100 share. Xử lý CS bình thường.
- **L2 (Medium)**: viral 1k-10k share, báo nhỏ đưa tin, KOL tag. Cần response chính thức.
- **L3 (High)**: trend top trending, báo lớn đưa tin, tag CEO, ảnh hưởng doanh thu/cổ phiếu. Cần war room.

Hỏi user: khủng hoảng đang ở mức nào? đã có gì xảy ra?

## Bước 2: Protocol 6 Giờ Đầu
**Giờ 0-1**: Đánh giá + Triệu tập
- Triệu tập "war room" (CEO, Legal, PR, CS lead, Product)
- Verify facts: cái gì đúng/sai
- Định danh nguồn (KH thật / fake / cạnh tranh)
- Ngừng tất cả ads/post đang lên

**Giờ 1-3**: Tuyên bố ban đầu (Holding Statement)
- 50-100 từ
- Acknowledge có sự việc
- Thể hiện đã biết và đang xử lý
- Hứa cập nhật trong X giờ
- Đăng trên fanpage chính + Twitter/X
- Push lên Zalo OA

**Giờ 3-12**: Investigate + Full Statement
- Đào sâu nguyên nhân
- Soạn statement đầy đủ 300-500 từ:
  - Apology rõ ràng (không "if you were offended")
  - Sự thật cốt lõi
  - Hành động đã/đang/sẽ làm
  - Liên hệ
- Đăng website, mạng xã hội, gửi báo

**Giờ 12-24**: Sustain & Monitor
- Trả lời comment có template duyệt
- Update tin tức mới mỗi 4-6h
- Monitor sentiment + trend
- Booking phỏng vấn báo lớn

## Bước 3: Phân Vai Trách Nhiệm
| Role | Job |
|---|---|
| CEO | Mặt mũi public, ký statement |
| Head PR | Soạn statement, làm việc báo |
| Legal | Review pháp lý |
| CS Lead | Trả lời KH cá nhân, hỗ trợ refund |
| Product | Fix root cause |
| Internal Comms | Thông báo nhân viên |
| Monitoring | Theo dõi social/báo 24/7 |

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch + WebFetch: monitor mention báo chí
- Brand24/Mention MCP: social listening
- Slack MCP: war room channel
- Gmail MCP: gửi statement báo
- Notion MCP: playbook archive
- Twitter/X API: post statement ngay

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Monitor mention realtime
import requests, time
def search_mentions(brand):
    r = requests.get('https://api.twitter.com/2/tweets/search/recent',
      headers={'Authorization':f'Bearer {TOKEN}'},
      params={'query':brand,'max_results':100,
        'tweet.fields':'created_at,public_metrics'})
    return r.json()['data']
# Loop 5 phút/lần
while True:
    new = search_mentions('TAKI Academy')
    high_engagement = [t for t in new if t['public_metrics']['retweet_count']>50]
    if high_engagement: alert_slack(high_engagement)
    time.sleep(300)
```

## Bước 5: Output Format
- File `.md` protocol đầy đủ
- 3 bộ statement template (L1/L2/L3)
- War room contact list
- Monitoring dashboard
- Post-mortem template
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 3 mức L1/L2/L3 rõ
- [ ] Protocol 24h chi tiết
- [ ] Phân vai có contact
- [ ] Statement template 3 độ
- [ ] Monitoring tool setup
- [ ] Đào tạo team trước khi xảy ra
- [ ] Có post-mortem
