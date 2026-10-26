---
name: mkt-ugc-collection-campaign
description: |
  Thiết kế campaign thu UGC (user-generated content) cho doanh nghiệp Việt Nam — mechanic, incentive, hashtag, T&C, đăng tải lại. Kích hoạt khi người dùng nói: "campaign UGC", "thu UGC khách hàng", "user generated content", "concours ảnh khách", "khuyến khích KH chụp ảnh", "UGC reward", "UGC contest", "social proof từ KH". Output là Markdown plan + asset launch.
---

# Campaign Thu UGC Từ Khách Hàng

## Mục Tiêu
Mỗi tháng thu được 100-500 UGC từ KH thật, biến thành tài sản marketing không tốn chi phí sản xuất, tăng trust và CR landing/ads 30-50%.

## Khi Nào Dùng
- Ecom/F&B/beauty có sản phẩm đẹp
- Chuẩn bị Black Friday / Tết
- Lần đầu launch UGC strategy
- Cần social proof cho LP
- Tăng engagement social

## Bước 1: Brief Campaign
Hỏi:
1. Sản phẩm + audience
2. Incentive (giảm giá / quà / voucher / spotlight)
3. Thời gian campaign (2-4 tuần)
4. Hashtag riêng
5. Kênh thu (IG/TikTok/website form)
6. Mục tiêu số UGC

## Bước 2: Mechanic & T&C
**Mechanic** đơn giản 3 bước:
1. Mua sản phẩm
2. Đăng ảnh/video kèm #hashtag + tag brand
3. Nhận voucher 100k hoặc tham gia rút thăm quà lớn

**T&C**:
- Quyền sử dụng UGC vĩnh viễn (granted khi tham gia)
- Cấm content unsafe (rượu, vũ khí, nội dung không phù hợp)
- Phải mua thật + tag brand đúng
- Thời gian + đại lý rõ
- Quy trình trao thưởng (1 tuần sau campaign end)

## Bước 3: Asset Launch
- Landing page campaign
- Post launch FB/IG/TikTok
- Email + Zalo thông báo cho KH cũ
- 5 mẫu UGC demo (seeding với KOC nhỏ)
- Frame Photoshop để KH áp dụng
- Email duyệt + cảm ơn

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- IG Graph API: search hashtag thu UGC
- Yotpo/Bazaarvoice MCP (nếu có)
- Google Forms MCP: form submit UGC
- Notion MCP: database UGC + status
- Gmail MCP: gửi voucher tự động

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Crawl post có hashtag qua Instagram Graph API
import requests
def search_hashtag(tag, ig_user_id, token):
    h = requests.get('https://graph.facebook.com/v18.0/ig_hashtag_search',
      params={'user_id':ig_user_id,'q':tag,'access_token':token}).json()
    hid = h['data'][0]['id']
    media = requests.get(f'https://graph.facebook.com/v18.0/{hid}/recent_media',
      params={'user_id':ig_user_id,
        'fields':'id,caption,media_url,permalink,username',
        'access_token':token}).json()
    return media['data']
```

## Bước 5: Output Format
- File `.md` campaign plan + T&C
- Asset pack launch (banner, email, post)
- Landing page wireframe
- UGC tracker (link, KH, reward status)
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Mechanic 3 bước dễ
- [ ] T&C có quyền sử dụng UGC
- [ ] Hashtag riêng + dễ nhớ
- [ ] Asset launch sẵn sàng
- [ ] Quy trình duyệt + trao thưởng rõ
- [ ] Tracker UGC + tỉ lệ duyệt
