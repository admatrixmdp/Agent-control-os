---
name: mkt-referral-program
description: |
  Thiết kế chương trình giới thiệu khách (Give X Get Y) cho doanh nghiệp Việt Nam — incentive 2 phía, share asset, tracker, fraud rule. Kích hoạt khi người dùng nói: "chương trình giới thiệu", "referral program", "give X get Y", "khách giới thiệu khách", "share to earn", "MGM mua hộ giới thiệu", "thiết kế referral", "referral incentive". Output là Markdown rule + asset chia sẻ.
---

# Chương Trình Giới Thiệu — Give X Get Y

## Mục Tiêu
Đạt CAC bằng 1/3 chi phí ads, tỷ lệ KH cũ giới thiệu >15%, mở rộng tệp viral organic.

## Khi Nào Dùng
- Đã có KH hài lòng (NPS >50)
- Sản phẩm dễ chia sẻ trên social
- Margin >40% đủ chia incentive
- Chuẩn bị campaign mới
- Khởi động cộng đồng KH

## Bước 1: Brief Sản Phẩm
Hỏi:
1. Sản phẩm + giá + margin
2. NPS hiện tại
3. Loại incentive đề xuất (voucher / cashback / quà / điểm)
4. Ngân sách incentive/ref
5. Kênh chia sẻ (Zalo, FB, link, mã)
6. Mục tiêu (số ref/tháng)
7. Đối tượng được giới thiệu (KH cũ / tất cả)

## Bước 2: Thiết Kế Incentive
**Công thức Give X Get Y**:
- Người giới thiệu: nhận 10-20% giá đơn (voucher / cash)
- Người được giới thiệu: nhận giảm 10% đơn đầu

Variants test:
- Tiền mặt vs voucher
- Tỷ lệ % vs cố định
- Tier (giới thiệu càng nhiều thưởng càng cao)
- Milestone (3 ref = quà đặc biệt)

## Bước 3: Asset Chia Sẻ + Anti-Fraud
**Asset**: 
- Link cá nhân hóa + mã ref
- Banner Zalo/FB share
- Caption sẵn 3 mẫu
- Email/SMS gợi ý
- Landing page riêng

**Anti-fraud**:
- Yêu cầu thanh toán thành công mới active reward
- Block self-referral (cùng IP/SDT/email)
- Max ref/người/tháng
- Manual review nếu >X ref/ngày

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- ReferralCandy / Friendbuy MCP (nếu có)
- Shopify/WooCommerce: tích hợp plugin referral
- Email/Zalo OA MCP: gửi mã ref tự động
- Google Sheets MCP: tracker ref
- Slack MCP: notify ref mới

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Sinh mã ref và webhook track conversion
import hashlib
def gen_ref_code(customer_id):
    return 'REF' + hashlib.md5(str(customer_id).encode()).hexdigest()[:6].upper()

# Webhook khi đơn thành công
def on_order_paid(order):
    if order.get('referral_code'):
        ref_customer = find_by_ref(order['referral_code'])
        reward(ref_customer, amount=order['total']*0.15)
        reward(order['customer_id'], voucher_code='WELCOME10')
```

## Bước 5: Output Format
- File `.md` rule chương trình
- File `.xlsx` matrix incentive
- Asset pack share (banner, caption, email)
- Landing page mời bạn
- Tracker dashboard
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Incentive 2 phía cân đối
- [ ] Asset chia sẻ dễ dùng
- [ ] Anti-fraud rule rõ
- [ ] Tracking attribution chính xác
- [ ] Có chuỗi email/SMS nhắc
- [ ] ROI dương trong 90 ngày
- [ ] T&C minh bạch
