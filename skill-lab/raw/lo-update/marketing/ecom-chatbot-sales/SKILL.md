---
name: Chatbot & Bán Hàng Tự Động TMĐT
description: >
  Xây dựng chatbot bán hàng tự động trên Facebook Messenger, Zalo, Website và Instagram.
  10 kịch bản chatbot bắt buộc, mẫu câu trả lời tiếng Việt, automation rules, KPI tracking.
  Áp dụng cho shop nhỏ đến lớn, từ B2C đến B2B.

  Dùng skill này khi: "xây dựng chatbot bán hàng", "chatbot messenger", "zalo bot",
  "automate bán hàng chat", "tư vấn sản phẩm tự động", "chốt đơn chat",
  "flow chatbot ecommerce", "automations selling", "bot bán hàng"
---

# Chatbot & Bán Hàng Tự Động cho TMĐT Việt Nam

## 1. Tổng Quan Chatbot TMĐT

### 1.1 Tại Sao Chatbot Quan Trọng
- **Phục vụ 24/7**: Khách hàng mua hàng lúc nào, bot trả lời lúc đó
- **Giảm tải sale**: Bot xử lý 80% câu hỏi, sale team focus vào close deal
- **Tăng conversion**: Phản hồi nhanh (< 1 phút) tăng 47% conversion
- **Tiết kiệm chi phí**: Một bot thay 2-3 nhân viên chat, chi phí 10% mức lương
- **Dữ liệu quý**: Biết khách nào quan tâm sản phẩm gì, sẽ target quảng cáo

### 1.2 Độ Tin Cậy Bot vs Human
| Chỉ tiêu | Bot | Human | Lợi ích |
|---------|-----|-------|--------|
| Response time | < 1 phút | 5-30 phút | Bot 5-30x nhanh |
| Đồng nhất thông tin | 100% | 70% | Tránh nhầm lẫn |
| Có sẵn 24/7 | Có | Không | Phục vụ giờ rảnh |
| Upsell/Cross-sell | Theo rule | Manual | Bot không quên |
| Escalation to human | Có thể | N/A | Best of both worlds |

## 2. Kịch Bản Chatbot Theo Từng Kênh

### 2.1 Facebook Messenger Bot

**Setup ban đầu:**
```
1. Tạo Facebook page (nếu chưa có)
2. Vào App Dashboard > Messenger > Setup
3. Kết nối page với bot platform (ManyChat, Pancake, Chatfuel)
4. Cho phép bot gửi tin tự động (Message Tags: Marketing, Transactional)
```

**Welcome Flow (Kịch bản chào hỏi):**
```
Khách inbox lần đầu:
├─ Bot: "Xin chào! 👋 Welcome đến [Tên Shop]"
├─ "Chúng mình bán [Loại SP], chuyên [Đặc điểm]"
├─ Hiển thị 3 nút lựa chọn:
│  ├─ "Xem sản phẩm bán chạy 🔥"
│  ├─ "Khuyến mãi hôm nay 💝"
│  └─ "Hỗ trợ / Liên hệ 💬"
└─ Auto-tag: Khách mới, chưa mua (New Customer)
```

**Product Catalog Flow:**
```
Khách bấm "Xem sản phẩm":
├─ Bot: "Bạn muốn xem loại sản phẩm nào?"
├─ Đưa ra 5 danh mục (VD: Áo, Quần, Giày, Phụ kiện, Top bán chạy)
├─ Khách chọn danh mục (VD: Áo)
│  └─ Bot gửi 3-4 sản phẩm tiêu biểu với:
│     ├─ Ảnh sản phẩm
│     ├─ Tên + Mô tả ngắn (50 ký tự max)
│     ├─ Giá (in đậm)
│     ├─ Số sao + đánh giá
│     └─ 2 nút: "Xem chi tiết 👀" | "Mua ngay 💳"
├─ Nếu "Xem chi tiết":
│  └─ Bot gửi link Shopee/Lazada hoặc trang chi tiết
├─ Nếu "Mua ngay":
│  └─ Bot hỏi: "Bạn muốn mua mấy cái?"
│     └─ Hỏi size/màu (nếu có)
│        └─ Bot xác nhận & lấy địa chỉ
└─ Auto-tag: Quan tâm [Loại SP]
```

**FAQ Auto-Response:**
```
Keyword matching → Câu trả lời tự động:

1. Hỏi giá / "bao nhiêu tiền" → Gửi bảng giá
2. Hỏi size / "size nào" → Gửi size chart + cách đo
3. Hỏi màu sắc → Gửi ảnh các màu + tên chính xác
4. Hỏi giao hàng / "ship bao lâu" → "TP HCM: 1-2 ngày, HN: 2-3 ngày..."
5. Hỏi đổi trả → "30 ngày đổi trả miễn phí nếu lỗi từ shop"
6. Hỏi bảo hành → "[Sản phẩm]: Bảo hành 12 tháng"
7. Hỏi mã voucher → Gửi danh sách voucher có sẵn
8. Hỏi thanh toán → "Hỗ trợ: COD, Chuyển khoản, [Nền tảng thanh toán]"
9. Hỏi review → Gửi link review trên Shopee/Lazada/Website
10. Hỏi theo dõi đơn → "Bạn có đơn nào chưa? Cho mình mã đơn"
```

**Order Tracking Flow:**
```
Khách: "Đơn hàng của tôi ở đâu?"
├─ Bot: "Cho mình mã đơn (VD: [Shop]123456)"
├─ Khách nhập mã đơn
├─ Bot kết nối database → Lấy dữ liệu:
│  ├─ ✅ Đã xác nhận (16:30 hôm qua)
│  ├─ 🚚 Đang giao (Giao dự kiến ngày mai 14:00-17:00)
│  ├─ 📦 Hoặc: Chưa xác nhận (Chúng mình sẽ xác nhận trong 2 giờ)
├─ Nút: "Liên hệ support 📞" | "Cảm ơn 👍"
└─ Auto-tag: Theo dõi đơn [Mã đơn]
```

### 2.2 Zalo OA Chatbot

**Setup:**
```
1. Tạo Zalo Official Account (OA) - tên shop
2. Verify OA bằng: GPKD, hóa đơn điện, ảnh chân dung chủ
3. Kết nối OA với bot platform hoặc API Zalo
4. Setup menu (tối đa 4 menu chính)
5. Kích hoạt Zalo Pixel để tracking
```

**Menu Design (4 menu chính):**
```
📱 Sản Phẩm      💰 Khuyến Mãi      📦 Hỗ Trợ      👤 Tài Khoản
└─ Xem tất cả    └─ Flash sale      └─ FAQ         └─ Đơn hàng
└─ Top bán chạy  └─ Combo giảm giá  └─ Giao hàng   └─ Chủ đề
└─ Mới về        └─ Free ship       └─ Đổi trả     └─ Đăng xuất
└─ Sale          └─ Khách VIP       └─ Bảo hành
                                     └─ Liên hệ
```

**Auto-Reply & Broadcast Timing:**
```
Auto-Reply (Khách nhập lần đầu):
"Xin chào! 👋 Cảm ơn bạn theo dõi [Shop].
Chúng tôi hỗ trợ: 7:00-22:00 hàng ngày.
Bạn có thể dùng menu trên hoặc chat trực tiếp.
👉 Chat ngay để nhận tư vấn"

Broadcast Timing (Tần suất):
- Thứ 2-5: 1 bản tin / ngày (16:00-18:00)
- Thứ 6: 2 bản tin (12:00 sale flash + 18:00 weekend)
- Thứ 7-8: 1 bản tin (10:00 promotion)
- Tối: 20:00-22:00 (Highest engagement)
- Tránh: 7:00-9:00, 12:00-13:00 (Khách bận)

Broadcast Content Types:
1. Flash sale (08:00-10:00, ngắn gọn, CTA clear)
2. New product (Thứ 2 hàng tuần)
3. Customer story (Thứ 4, ảnh + review)
4. Kiến thức (Thứ 5, VD: "Cách chọn size chuẩn")
5. Khuyến mãi định kỳ (20-25-30)
```

**Segmentation cho Zalo:**
```
Phân nhóm theo hành vi:
├─ Tier 1 - Khách VIP (Mua > 5 lần OR Mua > 2M):
│  └─ Tần suất: 3-4 tin/tuần (Exclusive offer trước)
├─ Tier 2 - Khách thường xuyên (Mua 2-4 lần):
│  └─ Tần suất: 2 tin/tuần (Khuyến mãi tiêu chuẩn)
├─ Tier 3 - Khách cũ (Mua 1 lần cách đây 30-60 ngày):
│  └─ Tần suất: 1-2 tin/tuần (Re-engagement, flash sale)
├─ Tier 4 - Khách mới (Follow < 7 ngày, chưa mua):
│  └─ Tần suất: 2 tin/tuần (Giới thiệu, ưu đãi new customer)
└─ Tier 5 - Inactive (Không mua, Follow > 6 tháng):
   └─ Tần suất: 1 tin/2 tuần (Re-activation campaign)
```

### 2.3 Website Chat Bot (Tawk.to, Tidio, Subiz)

**Widget Setup:**
```
- Đặt ở góc phải hoặc trái (Phải phổ biến hơn)
- Mở lúc khách vào trang (delay 3-5 giây để khách không bị sốc)
- Hiển thị tên + ảnh agent (Build trust)
- Mở tự động khi khách ở trang chi tiết sản phẩm
```

**Chat Flow trên Website:**
```
Khách vào website:
├─ Bot hiển thị (sau 5 giây):
│  ├─ "Xin chào! 👋 Có gì có thể giúp bạn?"
│  ├─ 3 nút nhanh:
│  │  ├─ "Xem collection 👗" → Catalog
│  │  ├─ "Mua hàng 💳" → How to order
│  │  └─ "Hỏi thêm ❓" → Chat with agent
│
├─ Khách xem sản phẩm trên trang chi tiết:
│  ├─ Bot: "Sản phẩm này hot 🔥 Mình còn 5 cái size L"
│  ├─ "Bạn muốn book giữ không?"
│  └─ Nút: "Book giữ" | "Hỏi thêm"
│
├─ Khách add to cart nhưng không checkout:
│  ├─ Bot (sau 2 phút): "Có gì cần giúp về sản phẩm này?"
│  ├─ Nút: "Hỏi về size/màu" | "Hỏi giao hàng" | "Checkout"
│
└─ Khách ở trang checkout > 1 phút mà chưa submit:
   ├─ Bot: "Cần hỗ trợ thanh toán không?"
   └─ Offer: "Dùng code SAVE10 giảm 10% nó!"
```

**Live Chat Handoff (Khi cần human):**
```
Bot điều kiện escalate:
1. Khách yêu cầu nói chuyện với người (keyword: "nói với người", "support")
2. Bot không trả lời được (timeout 30 giây, khách gửi message)
3. Đơn hàng có vấn đề (Return, Complaint, Special request)
4. Giờ cao điểm (Mặc định escalate nếu bot response > 30s)

Escalation message:
"Để bạn được tư vấn tốt hơn, mình chuyển bạn sang agent.
Chờ chút nhé - agent sắp online 😊"
```

### 2.4 Instagram DM Automation

**Setup:**
```
1. Liên kết Instagram business account với Facebook page
2. Dùng ManyChat / Pancake / Chatfuel để tự động Instagram DM
3. Setup webhook để nhận DM notification
```

**Instagram Bot Behavior:**
```
DM + Comment Automation:
├─ Khách: DM "Hi" / Comment "Mua"
├─ Bot auto-reply (trong 1 phút):
│  ├─ DM: "Xin chào! 👋 Cảm ơn bạn quan tâm 💕"
│  ├─ "Bạn muốn xem sản phẩm nào? Mình có:"
│  └─ Gửi 3-4 link sản phẩm hot
│
├─ Khách reply DM:
│  └─ Sau 1 tiếng, nếu khách chưa reply lần 2:
│     └─ Bot: "[Sản phẩm tên] bán hết nhanh lắm 🔥
│        Bạn có muốn mình book giữ không?"

Comment automation:
├─ Khách comment "Giá bao nhiêu?"
├─ Bot reply comment: "Vào DM mình giải đáp nhé 📱"
└─ Auto-send DM thêm link sản phẩm
```

## 3. 10 Flow Chatbot Bắt Buộc Cho TMĐT

### Flow 1: Welcome & Greeting

**Khi nào trigger:** Khách inbox/chat lần đầu, Follow OA, Vào website

**Nội dung:**
```
Bot: "Xin chào [Tên khách - nếu có]! 👋"
Bot: "Chào mừng đến [Tên shop]"
Bot: "Chúng tôi chuyên: [Mô tả ngắn loại hàng]"
Bot: "Hôm nay có khuyến mãi gì đặc biệt? 👇"

Nút CTA:
├─ "🛍️ Xem sản phẩm"
├─ "🎁 Khuyến mãi hôm nay"
└─ "❓ Hỏi ngay"

Tagging: Khách mới, Kênh [Messenger/Zalo/Website], Ngày follow
```

**Ví dụ thực tế:**
```
Bot: "Xin chào Hương! 👋
Welcome đến PANG - Shop thời trang nữ chuyên áo blouse, váy liền!"

"Hôm nay có:
✨ Flash sale 40% từ 16:00 hôm nay
✨ Combo áo quần giảm thêm 10%
✨ Free ship toàn quốc (hóa đơn > 200K)

👇 Bạn muốn làm gì?
```
```

### Flow 2: Product Recommendation (Hỏi nhu cầu → Gợi ý)

**Khi nào trigger:** Khách bấm "Xem sản phẩm" hoặc "Mình muốn..."

**Quy trình:**
```
Bot: "Bạn muốn tìm loại sản phẩm nào?"

Step 1: Hỏi loại sản phẩm
├─ "👕 Áo"
├─ "👖 Quần"
├─ "👗 Váy"
├─ "👟 Giày"
└─ "💎 Phụ kiện"

Step 2: Hỏi size/style (nếu relevant)
├─ VD áo: Size (XS, S, M, L, XL, XXL) + Style (Đơn giản, Họa tiết, Xuyên thấu)
├─ VD quần: Size + Kiểu (Ôm, Rộng, Cropped, Dài)

Step 3: Hỏi giá mong muốn
├─ "Dưới 200K"
├─ "200K - 500K"
├─ "500K - 1M"
└─ "Trên 1M"

Step 4: Gợi ý sản phẩm
├─ Dựa trên answers → recommend 3-5 sản phẩm phù hợp
├─ Hiển thị: Ảnh + Tên + Giá + Sao (nếu có review)
├─ Nút: "Xem chi tiết" | "Mua ngay" | "Thích nhưng chưa mua"

Tagging: Quan tâm [Loại SP], Style [Style], Budget [Giá], Ngày
```

**Ví dụ thực tế:**
```
Bot: "Bạn muốn tìm áo hay quần?"
Khách: "Áo"
Bot: "Áo kiểu nào? Đơn giản, Họa tiết hay Xuyên thấu?"
Khách: "Đơn giản thôi"
Bot: "Budget bao nhiêu?
├─ Dưới 200K (Áo basic)
├─ 200-500K (Áo chất lượng cao)
└─ Trên 500K (Premium)"
Khách: "200-500K"
Bot: "Perfect! Bạn có size favorite không?
├─ XS / S / M / L / XL / XXL"
Khách: "M"

→ Bot gợi ý 5 áo M, giá 200-500K, đơn giản:
  [Ảnh + Tên Áo A] 299K ⭐⭐⭐⭐⭐ (127 reviews)
  [Ảnh + Tên Áo B] 349K ⭐⭐⭐⭐ (89 reviews)
  ...
  👉 "Xem chi tiết" | "Mua ngay" | "Thích hơn cái khác"
```

### Flow 3: Price Inquiry & Quotation

**Khi nào trigger:** "Giá bao nhiêu?" / "Có giảm giá không?" / Khách hỏi cụ thể 1 sản phẩm

**Nội dung:**
```
Bot: "Sản phẩm bạn hỏi là gì? Cho mình tên hoặc link"

Nếu khách dán link:
├─ Bot parse link → Lấy sản phẩm
├─ Hiển thị: Tên + Hình + Giá gốc + Giá sale + % giảm

Nếu khách nói tên:
├─ Bot tìm trong database
├─ Nếu tìm được:
│  ├─ Hiển thị sản phẩm + Giá
│  └─ "Có giảm giá không? Hiện tại còn [Số lượng]"
└─ Nếu không tìm được:
   ├─ "Mình không tìm thấy. Bạn có link không?"
   └─ Escalate to agent

Nút: "Checkout ngay" | "Cần tư vấn thêm" | "Book giữ"

Tagging: Hỏi giá [Sản phẩm], Budget confirm, Ngày
```

**Ví dụ:**
```
Khách: "Áo Pang trắng bao nhiêu tiền?"
Bot: "Áo Pang white cream 👕
├─ Giá gốc: 399K
├─ Giá sale: 279K (Giảm 30%)
├─ Size còn: S, M, L, XL, XXL ✅
├─ Review: ⭐⭐⭐⭐⭐ 156 reviews
├─ Shipping: Miễn phí (Order > 200K)

👇 Bạn muốn làm gì?
├─ 💳 Checkout ngay
├─ ❓ Hỏi về size/chất liệu
├─ 📍 Book giữ giúp"

→ Nếu book giữ:
   Bot: "Được! Mình book giữ 2 giờ cho bạn.
   Trong lúc này bạn có thể thanh toán hoặc liên hệ lại.
   Book ID: [ID_123]"
```

### Flow 4: Order Placement via Chat

**Khi nào trigger:** "Mình muốn mua" / "Checkout" / Khách đủ thông tin

**Quy trình đặt hàng:**
```
Step 1: Xác nhận sản phẩm + số lượng
Bot: "Bạn muốn mua cái nào? (Kèm số lượng + size/màu)"
Khách: "2 cái áo trắng M, 1 váy đen S"
Bot: "OK! Mình confirm:
  ✓ Áo Pang white M x2 = 558K
  ✓ Váy Luna black S x1 = 349K
  = Tổng: 907K
  ✓ Miễn phí ship (>200K)"

Step 2: Lấy thông tin khách
├─ Tên khách đầy đủ
├─ Số điện thoại
├─ Địa chỉ giao hàng
└─ Email (nếu có)

Step 3: Xác nhận thông tin
Bot: "Mình xác nhận đơn của bạn:
  📦 Áo Pang white M x2 + Váy Luna black S x1
  👤 [Tên khách]
  📱 [SĐT]
  📍 [Địa chỉ]
  💰 907K (Free ship)
  ✓ Hợp lệ?"
Khách: "Đúng"

Step 4: Hỏi hình thức thanh toán
├─ "💳 Thanh toán online (Ngân hàng)"
├─ "💰 COD (Trả tiền khi nhận)"
├─ "📱 Zalo Pay / Momo / Shopeepay"

Step 5: Xác nhận đơn hàng
├─ Bot generate Mã đơn: PANG_20250403_12345
├─ "Cảm ơn bạn! Đơn hàng của bạn đã được xác nhận ✅
│  Mã đơn: PANG_20250403_12345
│  Dự kiến giao: 2025-04-04 hoặc 2025-04-05
│  Bạn sẽ nhận SMS cập nhật."
├─ Nút: "Theo dõi đơn" | "Cảm ơn 👍"
└─ Tagging: Khách đã mua, Mã đơn [PANG_...], Ngày, Giá trị

Step 6: Auto follow-up sequence
├─ +1 giờ: "Đơn của bạn đã được xác nhận. Chuẩn bị gói..."
├─ +6 giờ: "Đơn của bạn đã gửi. Dự kiến giao [ngày]..."
├─ +2 ngày: "Kiểm tra: Bạn nhận được hàng chưa?"
└─ +3 ngày: "Đánh giá đơn hàng + Ảnh sản phẩm được không?"
```

**Ví dụ thực tế:**
```
Khách: "Mình muốn mua 1 áo trắng size M với 1 váy đen size S"

Bot: "OK! Mình xác nhận:
👕 Áo Pang white M x1 = 279K (sale from 399K)
👗 Váy Luna black S x1 = 349K
💰 Tổng: 628K
🎁 Free ship toàn quốc

Hợp lệ không? 👇
├─ ✅ Xác nhận
└─ 🔄 Sửa lại"

Khách: "✅ Xác nhận"

Bot: "Tên đầy đủ của bạn là gì?"
Khách: "Phương Anh"

Bot: "SĐT nhận hàng?"
Khách: "0912345678"

Bot: "Địa chỉ giao hàng?"
Khách: "Tòa 45, Phổ Quang, Phú Nhuận, TP HCM"

Bot: "Xác nhận thông tin:
📦 Áo Pang white M + Váy Luna black S
👤 Phương Anh
📱 0912345678
📍 Tòa 45, Phổ Quang, Phú Nhuận, TP HCM
💰 628K (Free ship)
✓ Đúng không?"

Khách: "Đúng"

Bot: "Bạn thanh toán như thế nào?
├─ 💳 Thanh toán online (Ngân hàng)
├─ 💰 COD (Trả tiền khi nhận)
└─ 📱 Momo"

Khách: "COD"

Bot: "✅ Cảm ơn! Đơn hàng của bạn đã xác nhận:
🎫 Mã đơn: PANG_20250403_98765
📦 Áo + Váy
💰 628K
🚚 Dự kiến giao: 2025-04-04 đến 17:00
💳 Thanh toán: COD

Bạn sẽ nhận SMS cập nhật từ shipper.
Cảm ơn bạn! 🙏"
```

### Flow 5: Shipping Tracking

**Khi nào trigger:** "Đơn hàng của tôi ở đâu?" / "Mình muốn tracking" / Khách cung cấp mã đơn

**Quy trình:**
```
Bot: "Bạn cho mình mã đơn để kiểm tra nhé.
(VD: PANG_20250403_98765)"

Khách nhập mã đơn
↓
Bot query database / API Shopee / Lazada / GHN
↓
Hiển thị trạng thái:

✅ Đơn hàng đã được xác nhận
  ├─ Thời gian: 14:30 hôm qua (2025-04-02)
  ├─ Trạng thái: Chuẩn bị gói

🚚 Đơn hàng đang vận chuyển
  ├─ Shipper: [Tên shipper] - 0812345678
  ├─ Dự kiến giao: Hôm nay 10:00 - 17:00
  ├─ Vị trí cuối cùng: Ga phân loại Q1
  └─ Nút: "Gọi shipper" | "Chat shipper"

📦 Đơn hàng đã được giao
  ├─ Thời gian: 15:45 hôm qua (2025-04-03)
  ├─ Ký nhận: Phương Anh
  ├─ Vị trí: 45 Phổ Quang, Q.Phú Nhuận
  └─ Nút: "Đánh giá đơn" | "Báo vấn đề"

❌ Đơn hàng có vấn đề
  ├─ Vấn đề: Shipper chưa nhận được
  ├─ Liên hệ: Support team sẽ gọi bạn trong 1 giờ
  └─ Nút: "Chat support ngay"
```

**Ví dụ:**
```
Khách: "PANG_20250403_98765 ở đâu?"

Bot: "🚚 Đơn hàng của bạn đang vận chuyển:

👕 Áo Pang white M + Váy Luna black S
💰 628K (COD)

📍 Vị trí: Đang được giao (Trên đường)
🚗 Shipper: Bạch Dương - 0912345678
⏰ Dự kiến giao: Hôm nay 14:00 - 17:00
📞 Gọi shipper để xác nhận

👇 Bạn có thể:
├─ 📞 Gọi shipper
├─ 💬 Chat shipper
└─ ❓ Chat support nếu có vấn đề"
```

### Flow 6: FAQ Auto-Response

**Keyword-based auto-replies:**

```
[KEYWORD] → [AUTO RESPONSE]

1. "GIÁO / GIAO" → Ship response
   "Chúng tôi ship toàn quốc 🚚
   ├─ TP HCM + Bình Dương + Đồng Nai: 1-2 ngày (Free ship > 200K)
   ├─ HN + Tỉnh lân cận: 2-3 ngày (Free ship > 200K)
   ├─ Tỉnh khác: 3-5 ngày (Tính phí)
   ├─ Hòa Bình / Điện Biên: 5-7 ngày
   └─ Giá ship cụ thể? Cho địa chỉ mình tính."

2. "SIZE / CÂN / ĐO / LỰA" → Size chart response
   "[Ảnh size chart]
   📏 Cách đo chính xác:
   ├─ Bust: Quanh ngực (đo phủ áo bình thường)
   ├─ Waist: Quanh eo
   ├─ Length: Từ vai tới gấu áo

   🔍 Size recommend:
   ├─ Mình nặng 50kg → S hoặc M
   ├─ Mình nặng 60kg → M hoặc L
   ├─ Mình nặng 70kg → L hoặc XL

   💬 Nếu chưa chắc, chat mình. Mình tư vấn size chuẩn nhất!"

3. "MÀU / COLOR / HÌNH" → Color options response
   "[Gửi ảnh tất cả các màu sắc]
   🎨 Chúng tôi có:
   ├─ White cream (Trắng kem - lạnh)
   ├─ Black (Đen - basic)
   ├─ Navy (Xanh đen - thanh lịch)
   ├─ Khaki (Kaki - ấm)
   ├─ Rose (Hồng pastel - nữ tính)
   └─ Burgundy (Nâu đỏ - sang)

   👉 Màu nào bạn thích? Mình còn hàng!"

4. "CHẤT LIỆU / VẢI / CHÍNH" → Material response
   "✨ Chất liệu Áo Pang:
   ├─ Vải: 65% Linen + 35% Rayon (Thành phố)
   ├─ Độ mềm: Mềm vừa (Không xộc / Không nặng)
   ├─ Co giãn: 10-15% (Vừa vặn, ôm nhẹ)
   ├─ Giặt: Máy 30°, Phơi ngoài áng nắng
   ├─ Độ bền: Có thể mặc 50+ lần (Chất cao cấp)
   └─ Không phai, không co rút nếu giặt đúng cách"

5. "ĐỔI / HỎ / TRẢ / RETURN" → Return policy
   "✅ Chính sách đổi trả PANG:
   ├─ Thời gian: 30 ngày tính từ mua
   ├─ Lý do: Hỏng, khuyết tật (Lỗi shop)
   ├─ Size không vừa / Ko thích (Khách chịu ship về)
   ├─ Cách thực hiện:
   │  1. Chat + Gửi ảnh chi tiết
   │  2. Shop kiểm duyệt (24h)
   │  3. Gửi lại địa chỉ & Label
   │  4. Khách gửi về
   │  5. Shop nhận → Đổi / Refund (5-7 ngày)
   └─ Hotline: 0912345678 (9-21h hàng ngày)"

6. "BẢO HÀNH / WARRANTY" → Warranty response
   "🛡️ Bảo hành & Hỗ trợ:
   ├─ Bảo hành sản phẩm: 12 tháng (Hỏng, khuyết tật)
   ├─ Miễn phí:
   │  ├─ Khâu lỏng
   │  ├─ Khóa bị mất
   │  ├─ May sai
   │  └─ Vải lỗi
   ├─ Có tính phí: Giặt không sạch, cổ bị giãn từ use
   └─ Liên hệ: support@pang.vn hoặc 0912345678"

7. "THANH TOÁN / PAYMENT / CHUYỂN" → Payment methods
   "💳 Phương thức thanh toán:
   ├─ 💰 COD (Trả tiền khi nhận) - Toàn quốc
   ├─ 🏦 Chuyển khoản:
   │  ├─ Vietcombank: 1012345678 (Tên Shop PANG)
   │  ├─ Techcombank: 0987654321 (Tên chủ)
   │  └─ Ngân hàng khác: Liên hệ tư vấn
   ├─ 📱 Ví điện tử: Momo, ZaloPay, ShopeePay
   ├─ 💳 Thẻ tín dụng / Debit (Qua Shopee/Lazada)
   └─ 📲 Tài khoản ngân hàng digital: OCB, VPBank, Agribank"

8. "KHUYẾN MÃI / VOUCHER / CODE / DISCOUNT" → Promo list
   "[Bảng khuyến mãi hiện tại]
   🎁 Khuyến mãi hôm nay (2025-04-03):
   ├─ SAVE10: Giảm 10% (Min 200K)
   ├─ COMBO20: Mua 2 cái giảm 20%
   ├─ FREESHIP: Free ship order > 300K
   ├─ NEWCUST: 15% cho khách mới
   └─ VIP30: 30% cho VIP member

   ⏰ Flash sale: 16:00-18:00 giảm 40% một số sp
   💬 Chat mình để lấy mã tốt nhất!"

9. "REVIEW / ĐÁNH GIÁ" → Review instructions
   "⭐ Đánh giá sản phẩm:
   ├─ Trên Shopee/Lazada: Vào 'Đơn hàng' → 'Đánh giá'
   ├─ Trên Website: Mục 'Review' sản phẩm
   ├─ Thưởng:
   │  ├─ Review có ảnh: +5 point (500đ = 1 point)
   │  ├─ Review video: +10 point
   │  ├─ Review 5 sao: +2 point
   │  └─ Dùng point để mua tiếp
   └─ 📸 Ảnh chân thật > Ảnh chỉnh sửa. Cảm ơn!"

10. "CONTACT / HỖ TRỢ / SUPPORT / HOTLINE" → Contact info
    "📞 Liên hệ hỗ trợ PANG:
    ├─ 💬 Chat: [Kênh này]
    ├─ 📱 Zalo: [Link Zalo OA]
    ├─ 📧 Email: support@pang.vn
    ├─ ☎️ Hotline: 0912345678
    ├─ ⏰ Giờ làm: 7:00 - 22:00 (Hàng ngày)
    └─ 📍 Showroom: [Địa chỉ shop]

    Response time:
    ├─ 7:00-21:00: Trả lời trong 15 phút
    └─ 21:00-7:00: Trả lời sáng hôm sau"
```

### Flow 7: Abandoned Cart Reminder

**Khi nào trigger:** Khách add to cart nhưng không checkout trong 1-2 giờ

**Chuỗi reminder:**
```
0h - Khách add to cart, không checkout
↓
+1 giờ - First reminder:
Bot: "Bạn để giỏ hàng trong 1 giờ rồi 😊
[Hiển thị sản phẩm]
👉 Bạn có muốn checkout không?
├─ Bạn lo gì? Hỏi price / Size / Chất lượng?
└─ Hoặc checkout ngay, dùng code SAVE10 giảm 10%"

+6 giờ - Second reminder (nếu chưa checkout):
Bot: "Áo này chỉ còn [X cái] thôi 🔥
[Ảnh sản phẩm]
Bạn còn muốn giữ không?
├─ 💳 Checkout (Free ship nếu > 200K)
├─ ❓ Hỏi thêm
└─ 💔 Bỏ qua"

+24 giờ - Final reminder:
Bot: "Áo/váy bạn yêu thích giảm giá thêm 10% nữa!
[Sản phẩm + Giá new]
⏰ Hết hạn trong 2 giờ nữa
→ 💳 Checkout ngay code SAVE10"

+48 giờ - Inactive (Không reminder thêm)
```

**Ví dụ:**
```
Khách: [Vào website] → [Add áo trắng M] → [Quay về, không checkout]

+1h:
Bot: "Bạn để giỏ hàng 1 giờ rồi 😊
👕 Áo Pang white M
💰 279K (sale from 399K)
Free ship nếu mua thêm

Bạn có muốn checkout không?
├─ 💳 Checkout ngay
├─ ❓ Hỏi về size/chất lượng
└─ 💔 Không muốn"

[Khách không reply]

+6h:
Bot: "Áo này chỉ còn 5 cái thôi 🔥
Bạn còn muốn giữ không?
├─ 💳 Checkout (Free ship)
└─ ❓ Hỏi thêm"

[Khách không reply]

+24h:
Bot: "Áo bạn yêu thích + Sale thêm 10%!
👕 Áo Pang white M: 251K (from 279K)
⏰ Hết offer trong 2h
→ Code: SAVE10
👉 https://[link checkout]"
```

### Flow 8: Re-engagement (Khách cũ 30-60-90 ngày)

**Khi nào trigger:** Khách mua > 30 ngày / > 60 ngày / > 90 ngày mà chưa quay lại

**Chuỗi re-engagement:**
```
30 ngày chưa mua - Tier A (Hot):
Bot: "Hương, bao lâu rồi không thấy bạn! 🥺
Mình có sản phẩm mới bạn nên xem:
[3 sản phẩm hot mới]
👉 + Flash sale hôm nay 40% (16:00-18:00)
+ Code RETURN20 cho khách cũ"

60 ngày chưa mua - Tier B (Warm):
Bot: "Hương, chúng mình nhớ bạn 💕
Mình có cái gì hay:
[2 sản phẩm best-seller]
+ Combo deal giảm 25%
+ Free ship toàn quốc
→ Comeback?"

90 ngày chưa mua - Tier C (Cold):
Bot: "Hương, khách như bạn quý lắm!
Chúng mình có offer đặc biệt cho bạn:
+ COMEBACK30 (Giảm 30%)
+ Tặng thêm 1 phụ kiện (Free)
⏰ Hôm nay + Ngày mai thôi
→ Vào shop xem?"
```

**Ví dụ thực tế:**
```
Khách Hương: Mua lần cuối 35 ngày trước

Trigger:
Bot: "Hương, bao lâu rồi không thấy bạn! 🥺
Mình có sản phẩm mới bạn nên xem:
1. Áo linen wash blue (Mới về) - 299K
2. Váy hoa nắng (Bán chạy 4.9⭐) - 349K
3. Quần linen cream (Top 1 tuần) - 279K

Hôm nay còn:
✨ Flash sale 40% (16:00-18:00)
✨ Code RETURN20 giảm 20%
✨ Free ship > 200K

👉 Comeback lại với mình nha! 💕"

Khách click "Xem sản phẩm":
→ Bot gợi ý, escalate sale nếu khách hỏi
```

### Flow 9: Feedback Collection

**Khi nào trigger:** Khách nhận hàng (sau 1-2 ngày)

**Quy trình:**
```
Bot: "Hương, nhận hàng rồi không?"
Nút: "Có rồi 📦" | "Chưa nhận" | "Có vấn đề ⚠️"

Nếu "Có rồi":
├─ Bot: "Sản phẩm bạn có thích không?
│         5 sao = Rất thích, 1 sao = Không thích"
├─ Khách chọn sao
│
├─ Nếu 4-5 sao (Positive):
│  ├─ Bot: "Tuyệt vời! Có thể review lên Shopee/Website không?
│  │         Mình sẽ tặng thêm 5% voucher lần sau! 🎁"
│  ├─ Nút: "Review ngay" | "Không" | "Để sau"
│  └─ Tagging: Khách hài lòng
│
└─ Nếu 1-3 sao (Negative):
   ├─ Bot: "Xin lỗi! Có gì chưa tốt không?
   │        Chúng mình có thể cải thiện"
   ├─ Khách gõ feedback
   └─ Tagging: Khách không hài lòng + Escalate support

Nếu "Chưa nhận":
├─ Bot: "Dự kiến nhận lúc nào? Mình track giúp"
└─ Tagging: Chưa giao, tracking

Nếu "Có vấn đề":
├─ Bot: "Vấn đề gì? Hỏng / Không vừa / Khác?"
└─ Escalate to support team (Priority: HIGH)
```

**Ví dụ:**
```
Bot (sau 2 ngày khách order): "Hương, nhận hàng rồi không? 📦
├─ ✅ Có rồi
├─ ⏳ Chưa nhận
└─ ⚠️ Có vấn đề"

Khách: "Có rồi"

Bot: "Sản phẩm bạn có thích không?
[Hiển thị 5 sao rating] ⭐⭐⭐⭐⭐"

Khách: "5 sao"

Bot: "Tuyệt vời! 🎉 Cảm ơn bạn rất nhiều!
Có thể review trên Shopee / Website không?
Mình sẽ tặng 5% voucher (50K) lần mua sau!
├─ 📱 Review ngay
├─ ⏱️ Để sau
└─ 💔 Không"

Khách: "Review ngay"

Bot: "Cảm ơn! Bạn là người tuyệt vời 🙏
Voucher 50K sẽ được gửi vào inbox Zalo/Email trong 2h
Bạn có thế dùng cho lần mua tiếp theo!"
```

### Flow 10: Upsell/Cross-sell Post-Purchase

**Khi nào trigger:** Khách vừa thanh toán hoặc nhận hàng

**Quy trình:**
```
Upsell (Upgrade to premium):
├─ Khách mua: Áo basic 279K
├─ Bot: "Áo bạn mua rất đẹp!
│         Bạn có biết mình có Áo premium (Linen cao cấp) không?
│         + Chất tốt hơn 30% (Thoáng, mầm mộc)
│         + Bền 2x lâu hơn
│         + Chỉ tăng 50K (329K)
│         + UPGRADE30 giảm 30K nếu mua hôm nay"
├─ Nút: "Upgrade" | "Không cần"
└─ Tagging: Interested premium

Cross-sell (Sản phẩm đi kèm):
├─ Khách mua: Áo trắng
├─ Bot: "Áo này đẹp nhất khi kết hợp với:
│         👖 Quần beige (299K) - Combo giảm 20%
│         OR 👗 Váy xanh (349K) - Buy 2, save 15%"
├─ Nút: "Xem combo" | "Thêm 1 cái" | "Bỏ qua"
└─ Tagging: Interested combo

Bundle recommendation:
├─ Khách mua: 1 cái áo
├─ Bot: "Bạn muốn combo 3 cái giảm 25% không?
│         1. Áo trắng (Bạn đã mua)
│         2. Quần kem
│         3. Váy hoa
│         Combo: 800K (from 930K) - Save 130K!"
└─ Nút: "Thêm combo" | "Không"
```

**Ví dụ:**
```
Khách mua 1 áo trắng M (279K) thành công

Bot (30 phút sau): "Áo bạn mua rất thịnh hành! 👕
Nếu bạn thích, có 3 cách mix:

1️⃣ Với quần:
👖 Quần beige linen (299K)
👉 Bundle áo + quần: 520K (save 58K, -10%)

2️⃣ Với váy:
👗 Váy xanh pastel (349K)
👉 Bundle áo + váy: 580K (save 48K, -8%)

3️⃣ Full combo (Tư vấn):
[Gửi 3 outfit examples]
Bạn muốn thêm gì?"

Nút: "Xem combo" | "Hỏi tư vấn mix" | "Không"

Khách: "Xem combo"

Bot: "Combo áo + quần - 520K (save 58K)
├─ 👕 Áo Pang white M
├─ 👖 Quần beige L
├─ 🎁 Tặng thêm belt
└─ 👉 Mua ngay?"
```

## 4. Mẫu Câu Trả Lời Tiếng Việt Theo Tình Huống

### 4.1 Chào Hỏi (Thân thiện + Chuyên nghiệp)

```
❌ Tránh: "Hi. Tôi có thể giúp gì cho bạn không?"

✅ Tốt: "Xin chào! 👋 Chào mừng đến [Shop]!
        Hôm nay mình có khuyến mãi gì cho bạn?"

✅ Tốt hơn: "Xin chào Hương! 👋 Chào mừng quay lại [Shop]!
           Hôm nay cô gái xinh đẹp quay lại với chúng tôi?
           Có gì có thể giúp cô không?"
```

### 4.2 Tư Vấn Sản Phẩm (Chi tiết + Ảnh)

```
❌ Tránh: "Áo này tốt. Giá 299K."

✅ Tốt: "Áo Pang white 👕
         Giá: 299K (sale from 399K)
         Size: XS-XXL
         Review: 4.9⭐ (156 bài)
         Bạn muốn xem không?"

✅ Tốt hơn: "Áo Pang white - tuyệt chiếc! 👕

           ✨ Chất: Linen 65% + Rayon 35% (Thoáng, mịn)
           ✨ Màu: Trắng kem (Lạnh lùng, không chói)
           ✨ Fit: Ôm nhẹ, không xộc, không quá sát
           ✨ Giá: 299K (sale 40% từ 399K)
           ✨ Review: 4.9⭐ 156 bình luận

           👰 Thích hợp: Nữ văn phòng, tiệc tối, holiday
           👜 Mix với: Quần beige, váy xanh, sandal trắng

           Bạn thích không? Có khó khăn gì không?"
```

### 4.3 Xử Lý Khiếu Nại (Empathy + Giải pháp)

```
❌ Tránh: "Cái áo đó khó trả lại. Lỗi ở đâu?"

✅ Tốt: "Xin lỗi bạn! Áo bị gì thế?
         Chúng tôi sẽ sửa hoặc đổi cho bạn."

✅ Tốt hơn: "Xin lỗi rất nhiều! 😞
           Mình thật sự tiếc khi sản phẩm không như bạn kỳ vọng.

           Bạn vui lòng cho mình biết:
           - Vấn đề cụ thể gì? (Hỏng / Ko vừa / Khác?)
           - Bạn chụp ảnh được không? (Để chúng tôi xem rõ)
           - Bạn muốn đổi hay refund?

           Chúng tôi sẽ xử lý ngay trong 24h.
           Cảm ơn bạn vì tin tưởng chúng tôi! 🙏"
```

### 4.4 Chốt Đơn (Urgency + Confirmation)

```
❌ Tránh: "Bạn có muốn mua không?"

✅ Tốt: "Đơn hàng của bạn:
         👕 Áo + 👖 Quần = 520K
         Free ship. Bạn checkout được không?"

✅ Tốt hơn: "Bạn quyết định rồi! 🎉
           Đây là combo HOT nhất tuần này:
           👕 Áo Pang white M
           👖 Quần beige L
           = 520K (save 58K)

           ⏰ Flash sale hết lúc 18:00 hôm nay
           📍 Chỉ còn 8 combo (Trending)
           🚚 Free ship (Giao 2 ngày)

           Bạn sẵn sàng checkout chưa?
           👉 [Link checkout]

           Hoặc bạn có câu hỏi nào không?"
```

### 4.5 Không Có Hàng (Alternative + Waitlist)

```
❌ Tránh: "Hết hàng. Sorry."

✅ Tốt: "Áo trắng M hết hàng rồi.
         Bạn muốn L không, hay chờ về hàng?"

✅ Tốt hơn: "Áo Pang white M hết hàng rồi 😞
           Nhưng mình có 3 lựa chọn tốt:

           1️⃣ Size L: Ôm hơn M một chút (Still available)
              Bạn là 50kg, L sẽ rộng nhẹ - rất thịnh hành!

           2️⃣ Màu khác, size M:
              - Áo navy M (Chuyên sâu, hơn)
              - Áo khaki M (Ấm áp hơn)
              (Cùng giá 299K, cùng chất)

           3️⃣ Chờ về hàng:
              Mình sẽ back order, hàng về tuần sau
              Bạn muốn book giữ không? (Giữ 2 tuần)

           Bạn chọn cái nào? 🤔"
```

## 5. Automation Rules (Tự Động Hóa)

### 5.1 Auto-tag Khách Theo Hành Vi

```
Tagging system:
├─ Khách mới (New customer)
│  ├─ Condition: Follow < 7 ngày + Chưa mua
│  ├─ Action: Gửi Welcome + Special offer new customer
│  └─ Auto-tag: "New Customer"
│
├─ Quan tâm sản phẩm (Product interest)
│  ├─ Condition: Click / Xem sản phẩm > 3 lần
│  ├─ Product category: "Áo" / "Quần" / "Váy" / "Phụ kiện"
│  └─ Auto-tag: "Interested - [Category]"
│
├─ High-value customer (Khách VIP)
│  ├─ Condition: Total purchased > 2M OR Repeat purchase > 5
│  ├─ Action: VIP treatment, exclusive offers
│  └─ Auto-tag: "VIP Customer"
│
├─ Cold lead (Khách lạnh)
│  ├─ Condition: Follow > 90 ngày + Chưa mua
│  ├─ Action: Re-engagement campaign
│  └─ Auto-tag: "Cold Lead"
│
├─ Abandoned cart
│  ├─ Condition: Add to cart > 1 giờ + Không checkout
│  ├─ Action: Reminder sequence
│  └─ Auto-tag: "Abandoned Cart"
│
├─ Purchase frequency
│  ├─ 1 purchase: "One-time buyer"
│  ├─ 2-4 purchases: "Repeat customer"
│  ├─ 5+ purchases: "Loyal customer"
│  └─ Monthly purchase: "Active subscriber"
│
└─ Churn risk
   ├─ Condition: Last purchase > 60 ngày + Was active
   ├─ Action: Win-back campaign
   └─ Auto-tag: "At risk - churn"
```

### 5.2 Auto-assign Cho Sales Team

```
Assignment rules:
├─ Lead assignment:
│  ├─ IF: Khách bấm "Chat with agent" → Assign to available agent
│  ├─ IF: Khách nhập yêu cầu custom → Assign to senior sales
│  └─ IF: Khách có complaint → Assign to support manager
│
├─ Round-robin (Phân bổ công bằng):
│  ├─ Agent A: Chat 1, 3, 5, 7... (Odd numbers)
│  ├─ Agent B: Chat 2, 4, 6, 8... (Even numbers)
│  └─ Avoid overload: Max 5 chats / agent at once
│
├─ Skill-based routing:
│  ├─ Komplaint: Assign to "Complaint specialist"
│  ├─ B2B inquiry: Assign to "B2B sales manager"
│  ├─ Tech question: Assign to "Product specialist"
│  └─ General: Assign to "Sales team"
│
└─ Time-based assignment:
   ├─ 7:00-12:00: Team A
   ├─ 12:00-18:00: Team B
   └─ 18:00-22:00: Team C (Night shift)
```

### 5.3 Auto Follow-up Sequence

```
Timeline:
├─ +1 giờ (sau khi khách tương tác):
│  └─ Bot: "Cảm ơn bạn! Bạn có thêm câu hỏi không?"
│
├─ +6 giờ (nếu chưa order):
│  └─ Bot: "Sản phẩm bạn hỏi còn stock. Book giữ?"
│
├─ +24 giờ (nếu chưa order):
│  └─ Bot: "Flash sale hôm nay, áo giảm thêm 10%"
│
├─ +3 ngày (nếu chưa order):
│  └─ Bot: "Bạn có muốn thử size khác không? Free return"
│
├─ +7 ngày (nếu chưa order):
│  └─ Bot: "Cuối cùng: Code FINAL15 giảm 15%. Hôm nay thôi!"
│
└─ +14 ngày (Ngưng follow-up):
   └─ Tag as "Lost lead" → Exclude from follow-up
```

### 5.4 Trigger-based Messaging

```
Automations:
├─ Birthday month:
│  ├─ Trigger: Khách nhập ngày sinh = tháng này
│  ├─ Day of birthday: Bot gửi "Chúc mừng sinh nhật!"
│  └─ Offer: "Sinh nhật bạn, mình tặng 20% voucher"
│
├─ Re-order reminder:
│  ├─ Trigger: Khách mua mỹ phẩm/hóa mỹ phẩm (consumable)
│  ├─ Timeline: +45 ngày (Estimation của sản phẩm hết)
│  └─ Message: "Sắp hết, bạn cần order thêm không?"
│
├─ Stock alert:
│  ├─ Trigger: Sản phẩm yêu thích khách back in stock
│  ├─ Notification: Bot gửi "Cái mà bạn chờ đó, back stock rồi!"
│  └─ Offer: "Buy now, still available"
│
├─ Order anniversary:
│  ├─ Trigger: X ngày từ lần mua cuối
│  ├─ 30 days: "Chắc bạn cần thêm gì? Mình có COMEBACK20"
│  ├─ 60 days: "Mình nhớ bạn! COMEBACK25"
│  └─ 90 days: "Bạn ở đâu? COMEBACK30 cho bạn!"
│
└─ Flash sale notification:
   ├─ Trigger: Flash sale starts (Admin trigger)
   ├─ Segmentation: VIP first (1h trước), then all customers
   └─ Message: "Flash sale 40% in 2h. Items: [Top 3 SP]"
```

## 6. KPI Chatbot & Measurement

### 6.1 Metrics Quan Trọng

```
| Metric | Target | Formula | Importance |
|--------|--------|---------|------------|
| Response time | < 1 min | (Total response time) / (Total messages) | 🔴 High |
| Resolution rate | > 85% | (Resolved chats) / (Total chats) | 🔴 High |
| Conversion rate | > 8% | (Orders from chat) / (Chat sessions) | 🔴 High |
| CSAT | > 4/5 | (Sum of ratings) / (Total rated) | 🟠 Medium |
| Message frequency | 2-4 msgs | Avg messages per chat | 🟠 Medium |
| Escalation rate | < 15% | (Escalated) / (Total) | 🟠 Medium |
| Bot message accuracy | > 95% | (Correct answers) / (Total answers) | 🟢 Low |
| Chat volume | +20% MoM | (Chats this month) vs (Last month) | 🟢 Low |
```

### 6.2 Dashboard Tracking

```
Daily metrics (report cấp shop owner):
├─ Tổng chats hôm nay: X
├─ Orders from chat: X (+Y% vs ngày hôm qua)
├─ Revenue from chat: [Value]
├─ Avg response time: X phút
├─ Top 3 products asked: [List]
├─ Top 3 questions: [List]
└─ Alerts: [Issues to fix]

Weekly metrics:
├─ Total chats: X
├─ Orders from chat: X
├─ Conversion rate: X%
├─ Avg CSAT: X/5
├─ Top performing time: [Time range]
├─ Best channels: [Messenger/Zalo/Website]
└─ Issues & solutions

Monthly metrics (Strategy review):
├─ Growth: vs last month
├─ Revenue contribution: Chat vs other channels
├─ Customer segmentation: New / Repeat / VIP
├─ Top products: Categories, trending items
├─ Seasonal trends: Pattern analysis
├─ Competitor benchmarks: If available
└─ Recommendations: What to improve
```

## 7. Tools Phổ Biến Ở Việt Nam

```
Platform | Strengths | Weakness | Cost | Best for |
|----------|-----------|----------|------|----------|
| Pancake | Easy, Vietnamese team | Limited features | $20-100 | Shopee/Lazada sellers |
| ManyChat | Powerful automation | Pricey for SMB | $50-500 | Scale-up with budget |
| Chatfuel | No-code builder | Limited support | $20-100 | DIY startups |
| Haravan Chat | Native Shopify integration | Limited Zalo support | Bundled | Haravan stores |
| Subiz | Vietnamese app | Limited FB integration | $50-300 | Omnichannel support teams |
| Zalo Native | Built-in OA bot | Limited customize | Free | Zalo OA basic automation |
| Tidio | Affordable, easy | Limited Vietnamese support | $20-100 | Multilingual stores |
| Drift | Enterprise features | Expensive for SMB | $100-1000 | High-volume operations |

Recommendation:
├─ Small shop (< 100 orders/month): Pancake / Zalo native
├─ Mid shop (100-500 orders/month): ManyChat + Pancake
├─ Large shop (500+ orders/month): Subiz + ManyChat
└─ Enterprise: Custom API integration
```

## 8. Template: Chatbot Script Map (Flowchart)

```
Chatbot Entry Points:
│
├─ Messenger
│  ├─ [WELCOME] → [PRODUCT CATALOG] → [CHECKOUT] → [ORDER CONFIRM]
│  ├─ [FAQ BOT] → [AUTO RESPONSE]
│  └─ [ESCALATE TO AGENT]
│
├─ Zalo OA
│  ├─ [MENU CLICK] → [AUTO REPLY]
│  ├─ [BROADCAST] → [CLICK] → [PRODUCT]
│  └─ [CHAT] → [CHATBOT] or [HUMAN]
│
├─ Website Chat
│  ├─ [ENTER SITE] → [BOT GREETING] (after 5s)
│  ├─ [VIEW PRODUCT] → [BOT SUGGEST]
│  ├─ [ADD TO CART] → [BOT REMINDER] (+1h)
│  └─ [CHECKOUT PAGE] → [BOT OFFER CODE]
│
└─ Instagram DM
   ├─ [DM TEXT] → [AUTO REPLY + PRODUCT]
   ├─ [COMMENT] → [REPLY + DM LINK]
   └─ [STORY CLICK] → [DM BROADCAST]

Detailed Flow Example (Messenger):
│
Start: Khách inbox
│
├─ Is new customer?
│  ├─ YES → Welcome + Special offer new customer
│  │         └─ [3 nút: Xem SP / Khuyến mãi / Hỏi]
│  └─ NO → Regular greeting
│          └─ [3 nút: Xem SP / Khuyến mãi / Hỏi]
│
├─ Customer choice:
│  ├─ [Xem SP] → Show catalog
│  │             ├─ Customer picks category
│  │             ├─ Show products
│  │             └─ [Xem chi tiết] or [Mua ngay]
│  │
│  ├─ [Khuyến mãi] → Show today's deals
│  │                 └─ [Mua ngay]
│  │
│  └─ [Hỏi] → FAQ or escalate to agent?
│             ├─ [Keyword match] → Auto FAQ answer
│             └─ [No match] → Escalate to agent
│
├─ Checkout flow:
│  ├─ Ask product + quantity
│  ├─ Ask size/color
│  ├─ Ask shipping address
│  ├─ Ask payment method
│  └─ Confirm + Order ID sent
│
└─ Follow-up:
   ├─ +1h: Confirm order
   ├─ +6h: Shipping update
   ├─ +2d: Delivery status
   └─ +3d: Feedback request
```

## 9. Best Practices & Pitfalls

**✅ Tốt:**
- Phản hồi nhanh (< 1 phút)
- Câu trả lời ngắn gọn (Max 100 từ/tin)
- Ảnh đẹp, thumbnail rõ
- CTA button clear ("Mua ngay" > "Bạn muốn gì?")
- Personalize (Gọi tên khách, nhớ history)
- Escalate to human when needed
- Collect feedback & improve
- A/B test messages

**❌ Tránh:**
- Response chậm (> 5 phút)
- Pesan dài, lủng củng
- Quá nhiều text, ít ảnh
- Unclear CTA
- Generic, không personal
- Bot tội lỗi (Khách hỏi cái không xoay sở)
- Spam nhiều message
- Bỏ bê follow-up

---

**Để sử dụng skill này tốt nhất:**
1. Chọn platform phù hợp (Messenger > Zalo > Website based on your audience)
2. Setup 3 flows cốt lõi trước (Welcome, Product, Checkout)
3. A/B test messages & timing
4. Monitor KPI hàng tuần
5. Optimize dần dần (Add more flows, improve messaging)
6. Train team trên customer service best practices
