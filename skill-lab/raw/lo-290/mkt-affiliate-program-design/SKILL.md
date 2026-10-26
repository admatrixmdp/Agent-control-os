---
name: mkt-affiliate-program-design
description: |
  Thiết kế chương trình affiliate cho doanh nghiệp Việt Nam — commission rate, tier, T&C, dashboard, tracking link, payout. Tự động sinh tài liệu pháp lý và materials cho affiliate. Kích hoạt khi người dùng nói: "thiết kế affiliate program", "chương trình affiliate", "commission rate affiliate", "tracking affiliate", "T&C affiliate", "tạo affiliate program", "affiliate dashboard", "đăng ký affiliate". Output là Markdown T&C + Excel commission table + onboarding kit.
---

# Thiết Kế Chương Trình Affiliate

## Mục Tiêu
Mở thêm kênh phân phối affiliate đem 15-30% doanh thu/tháng mà không tăng chi phí marketing cố định, chỉ trả khi có sales.

## Khi Nào Dùng
- Sản phẩm có margin >40%
- Đã có thương hiệu, có người muốn giới thiệu
- Khóa học/SaaS/ecom có thể track conversion
- Cần scale nhanh thị trường
- Bổ sung kênh ngoài ads

## Bước 1: Thiết Kế Commission
Hỏi:
1. Sản phẩm + giá + margin
2. Loại hoa hồng (% / cố định / tier)
3. Khả năng trả tối đa (% biên lợi nhuận)
4. Thời gian cookie (7/30/90 ngày)
5. Đối tượng affiliate (KH cũ / blogger / KOL)

Đề xuất:
- Tier 1 (0-5 sales/tháng): 10%
- Tier 2 (6-20): 15%
- Tier 3 (21+): 20% + bonus
- Bonus milestone (50 sales = +1tr)

## Bước 2: Viết T&C
Bao gồm:
- Quy trình đăng ký + duyệt
- Cookie & attribution rule
- Cách track link/coupon
- Quy định nội dung (cấm spam, brand misuse)
- Quy định trả thưởng (min payout, payday, cách trả)
- Quyền hủy/khóa account
- GDPR/PDPL VN compliance

## Bước 3: Tạo Onboarding Kit
- Welcome email
- Tutorial video 10p
- Banner / creative pack (FB/IG/Email)
- Swipe copy (5 mẫu post + 5 mẫu email)
- FAQ 15 câu
- Group cộng đồng

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Tapfiliate/Rewardful/AccessTrade MCP (nếu có): setup chương trình
- Google Sheets MCP: dashboard manual cho affiliate
- Gmail MCP: chuỗi onboarding tự động
- Notion MCP: trang public chương trình
- WebSearch: benchmark commission ngành

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Sinh tracking link rút gọn qua Bitly API
import requests
def make_aff_link(aff_id, product_url):
    url = f'{product_url}?ref={aff_id}'
    r = requests.post('https://api-ssl.bitly.com/v4/shorten',
      headers={'Authorization':f'Bearer {TOKEN}'},
      json={'long_url':url})
    return r.json()['link']
```

## Bước 5: Output Format
- File `.md` T&C đầy đủ
- File `.xlsx` commission table + tier rule
- Folder onboarding kit (creative, swipe copy)
- Landing page affiliate đăng ký
- Tracker dashboard template
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Commission cạnh tranh thị trường
- [ ] T&C rõ ràng, có pháp lý VN
- [ ] Cookie & attribution rule cụ thể
- [ ] Onboarding kit đầy đủ
- [ ] Có tracker dashboard
- [ ] Có quy định chống fraud
- [ ] Min payout & schedule rõ
