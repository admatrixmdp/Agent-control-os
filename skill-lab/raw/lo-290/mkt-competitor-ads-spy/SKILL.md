---
name: mkt-competitor-ads-spy
description: |
  Spy quảng cáo đối thủ qua Facebook Ads Library + WebFetch và tổng hợp insight creative, copy, offer. Kích hoạt khi người dùng nói: "spy ads đối thủ", "Facebook Ads Library", "phân tích ads đối thủ", "competitor ads analysis", "rip ads đối thủ", "xem ads competitor", "ads spy tool", "creative đối thủ". Output là Excel ads inventory + báo cáo insight.
---

# Spy Ads Đối Thủ — FB Ads Library + WebFetch

## Mục Tiêu
Trong 1-2h biết đối thủ đang chạy gì, hook nào, offer nào, ngân sách rough → lấy insight cho creative team không phải bịa "ý tưởng từ trên trời".

## Khi Nào Dùng
- Chuẩn bị campaign mới
- Đối thủ launch sản phẩm mới
- Brand mới vào thị trường VN
- Cần inspiration creative
- Audit chiến lược competitive

## Bước 1: Liệt Kê Đối Thủ
Hỏi:
1. 3-5 đối thủ direct
2. 2-3 brand cùng style/audience khác ngành (cross-pollination)
3. URL Page FB / IG / TikTok / website
4. Thị trường (VN / Asia / Global)
5. Loại ads quan tâm (video / image / carousel / Reels)

## Bước 2: Crawl Ads Library
Với mỗi đối thủ, dùng WebFetch:
- `https://www.facebook.com/ads/library/?country=VN&active_status=active&ad_type=all&search_type=page&q=<brand>`
- Lấy tất cả ads đang active
- Lưu: thumbnail, copy, CTA, ngày chạy

Phân loại:
- Awareness (top of funnel)
- Consideration (case study, testimonial)
- Conversion (offer cụ thể)
- Retargeting

## Bước 3: Tổng Hợp Insight
Phân tích pattern:
- Hook đầu video (3s đầu nói gì)
- Format (UGC / studio / animation)
- Offer (discount/bonus/guarantee)
- CTA (xem thêm / mua ngay / đăng ký)
- Style copy (formal / casual / fear / aspirational)

Sinh 10-20 insight + 5 creative idea áp dụng cho brand mình.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebFetch: crawl FB Ads Library + TikTok Creative Center
- WebSearch: tìm thêm campaign news, PR
- Notion MCP: lưu Ads Library nội bộ
- Google Drive MCP: lưu screenshot/thumbnail
- Slack MCP: chia sẻ daily inspiration

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Crawl FB Ads Library
import requests
from bs4 import BeautifulSoup
def get_ads_library(brand, country='VN'):
    url = f'https://www.facebook.com/ads/library/async/search_ads/'
    params = {'q':brand,'country':country,'active_status':'active'}
    r = requests.get(url, params=params, headers={'User-Agent':'Mozilla/5.0'})
    return r.json() if r.ok else None
```

## Bước 5: Output Format
- File `.xlsx` ads inventory: brand, ad, hook, copy, CTA, ngày start
- Báo cáo HTML insight + 10 ý tưởng creative
- Folder screenshot ads tham khảo
- Mood board cho creative team
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ 3-5 đối thủ
- [ ] Tổng 50+ ads crawled
- [ ] Phân loại theo funnel
- [ ] Hook pattern tổng kết rõ
- [ ] 10+ insight có data
- [ ] 5 creative idea áp dụng được
