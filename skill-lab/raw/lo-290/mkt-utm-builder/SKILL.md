---
name: mkt-utm-builder
description: |
  Tạo UTM chuẩn cho campaign marketing theo template thống nhất, lưu vào Sheet/Notion để team dùng chung và đo lường chính xác trên GA4. Kích hoạt khi người dùng nói: "tạo UTM", "UTM builder", "đặt UTM chuẩn", "naming convention UTM", "UTM template", "UTM marketing", "UTM cho campaign", "tracking link UTM". Output là Excel sheet + tool HTML.
---

# UTM Builder Chuẩn Naming Convention

## Mục Tiêu
Mọi link campaign đều có UTM chuẩn, đặt tên thống nhất giữa các kênh, giúp GA4/Looker đo lường chính xác và team report nhanh.

## Khi Nào Dùng
- Trước khi launch campaign mới
- Áp chuẩn cho toàn team marketing
- Cần audit báo cáo GA4 vì source/medium loạn
- Onboard team mới
- Tích hợp với CRM (lead source)

## Bước 1: Đặt Naming Convention
Quy tắc:
- Chữ thường, không dấu, dùng `-` hoặc `_`
- Không khoảng trắng

Template:
- `utm_source`: kênh phát hành (facebook, google, zalo, email, tiktok)
- `utm_medium`: loại (cpc, social, email, referral, organic, affiliate)
- `utm_campaign`: <năm><tháng>_<chiendich>_<segment>
  Ví dụ: `202606_launchx_smeowner`
- `utm_content`: variant (creative_a, headline_b, video_15s)
- `utm_term`: keyword (chỉ paid search)

## Bước 2: Build Tool Sinh UTM
Form đơn giản: chọn source, medium, nhập campaign, content. Auto sinh full URL + short URL.

Validate:
- Không có khoảng trắng
- Không trùng campaign tên đã có
- Có cảnh báo nếu thiếu field

## Bước 3: Quản Lý Trong Sheet Tập Trung
Mỗi row 1 link. Cột:
- Date tạo
- Người tạo
- Campaign
- Source/Medium/Campaign/Content/Term
- Full URL
- Short URL
- Note
- Đường dẫn đích

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: lưu master UTM sheet
- Bitly/Rebrandly MCP: short URL
- Notion MCP: trang internal documentation
- Slack MCP: bot sinh UTM in channel
- GA4 MCP: kiểm tra UTM đã track chưa

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Sinh UTM + short link
from urllib.parse import urlencode
import requests
def build_utm(base, source, medium, campaign, content='', term=''):
    params = {'utm_source':source,'utm_medium':medium,
      'utm_campaign':campaign}
    if content: params['utm_content']=content
    if term: params['utm_term']=term
    return f'{base}?{urlencode(params)}'

def shorten(url):
    r = requests.post('https://api-ssl.bitly.com/v4/shorten',
      headers={'Authorization':f'Bearer {TOKEN}'}, json={'long_url':url})
    return r.json()['link']
```

## Bước 5: Output Format
- File `.xlsx` template UTM master (có data validation dropdown)
- HTML tool form đơn giản
- Markdown SOP cho team
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Naming convention thống nhất
- [ ] Có data validation tránh lỗi
- [ ] Short URL kèm theo
- [ ] Sheet master share cho team
- [ ] SOP onboard sẵn
- [ ] Đã test trên GA4 thấy đúng
