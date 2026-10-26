---
name: mkt-loyalty-program-design
description: |
  Thiết kế loyalty program cho doanh nghiệp Việt Nam — tier (Silver/Gold/Platinum), points, redemption catalog, communications. Tự động tính ROI và đề xuất rule. Kích hoạt khi người dùng nói: "thiết kế loyalty program", "chương trình khách hàng thân thiết", "membership tier", "tích điểm đổi quà", "loyalty rule", "hạng thành viên", "chương trình thân thiết", "VIP program". Output là Markdown rule + Excel point matrix.
---

# Thiết Kế Loyalty Program

## Mục Tiêu
Tăng repeat rate 30-50%, AOV 10-20%, customer lifetime value 2-3x thông qua loyalty program thiết kế đúng tâm lý khách hàng VN.

## Khi Nào Dùng
- Ecom/F&B/retail có >1.000 KH
- Tỷ lệ KH cũ <30% (cần đẩy retention)
- Margin đủ chia thưởng 3-7%
- Có hệ thống tracking đơn (POS/website)
- Chuẩn bị mùa sale lớn

## Bước 1: Brief Business
Hỏi:
1. Ngành + giá trung bình đơn
2. Tần suất mua/khách/năm
3. Margin trung bình
4. Quy mô KH hiện có
5. Hệ thống điểm bán hàng (POS/web/app)
6. Mục tiêu (retention/AOV/recommend)
7. Ngân sách quà thưởng/năm

## Bước 2: Thiết Kế Tier + Point
Đề xuất 3 tier:
- Silver: mua 0-5tr/năm — tích 1 điểm / 10.000đ
- Gold: 5-20tr — tích 1.5 điểm / 10.000đ + birthday gift
- Platinum: 20tr+ — tích 2 điểm + early access + dedicated CS

Quy đổi: 100 điểm = 50.000đ trừ đơn (~5% cashback).

## Bước 3: Catalog Redemption + Communications
**Redemption**:
- Trừ đơn (mặc định)
- Đổi quà từ catalog (sản phẩm low-cost margin cao)
- Donate (tăng cảm xúc tích cực)
- Trải nghiệm (event VIP, workshop)

**Communications**:
- Welcome email khi đạt tier
- Email tháng số điểm
- Reminder điểm sắp hết hạn
- Birthday voucher
- Anniversary

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Shopify/KiotViet/Sapo MCP: setup loyalty trên platform
- Email MCP: chuỗi automation theo tier
- Google Sheets MCP: dashboard điểm/quà
- Notion MCP: trang public loyalty rule
- Zalo OA MCP: gửi notification

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Cộng điểm tự động khi có đơn từ Shopify webhook
from flask import Flask, request
app = Flask(__name__)
@app.route('/webhook/orders', methods=['POST'])
def order_paid():
    order = request.json
    points = int(order['total_price']/10000)
    # Update customer.metafields.points
    return '',200
```

## Bước 5: Output Format
- File `.md` rule chương trình (FAQ-style)
- File `.xlsx` point matrix + redemption catalog
- Email automation flow (5-7 email)
- ROI calculator (point liability vs incremental revenue)
- Landing page loyalty
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Tier rõ + threshold dễ hiểu
- [ ] Point: VND ratio đơn giản
- [ ] Catalog redemption hấp dẫn
- [ ] Email automation đầy đủ
- [ ] ROI dương trong 6 tháng
- [ ] Quy định điểm hết hạn rõ
- [ ] Có cơ chế chống abuse
