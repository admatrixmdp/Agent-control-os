---
name: Tối Ưu Checkout & Giảm Bỏ Giỏ
description: >
  Chiến lược tối ưu hóa checkout flow, giảm tỷ lệ bỏ giỏ hàng từ 70-80% xuống 20-30%.
  Dùng khi cần: "giảm cart abandonment", "tối ưu checkout", "checkout flow", "trust signals",
  "payment optimization", "abandoned cart recovery", "checkout page design", "COD integration",
  "freeship strategy", "checkout mobile"
---

# CHECKOUT OPTIMIZATION - TOÀN DIỆN

## THỰC TRẠNG: TỶ LỆ BỎ GIỎ HÀNG TMĐT VIỆT NAM

### Số liệu:
- **TMĐT VN trung bình:** 70-80% bỏ giỏ hàng (abandoned cart rate)
- **Ngành tốt nhất:** 40-50% (các brand lớn, đã optimize)
- **Ngành kém nhất:** 85-90% (startup, mobile-first, payment limited)
- **Mobile:** 83-85% (gấp đôi desktop 40-45%)

### So sánh global:
- Global average: 70%
- VN không thua global → VN e-commerce vẫn chưa optimize tốt

---

## 15 LÝ DO KHÁCH BỎ GIỎ HÀNG - GIẢI PHÁP CHI TIẾT

### LÝ DO #1: Chi phí vận chuyển quá cao

**Vấn đề:**
- Khách add sản phẩm 250k
- Đến checkout, phí ship 100k
- Total 350k → Khách sốc, bỏ đơn

**Giải pháp:**

**1. Hiển thị ship fee sớm (Pre-checkout)**
```
Trước khi click "Thanh toán":
- Cart page: "Freeship cho đơn >300k"
- Auto-calculate: "Địa chỉ giao: [City] → Ship: 50k"
- Add to cart popup: "Cộng freeship 0đ"
```

**2. Freeship threshold strategy**
- Tính toán chiếc sắp hết: freeship threshold = 20% order value
- Ví dụ: AOV = 300k → Freeship threshold = 350k
- Message: "Thêm 100k nữa → Freeship (tiết kiệm 60k)"

**3. Dynamic shipping tiers**
```
- Dưới 200k: Ship 50k
- 200-500k: Ship 30k
- Trên 500k: Freeship

Display as: "Freeship cho đơn >500k"
```

**4. Express shipping vs standard**
```
Tiêu chuẩn:
- Standard (3-5 ngày): Freeship
- Express (1-2 ngày): +30k

Khách sẽ chọn standard nhiều hơn
```

**5. Shipping progress bar**
```
Hiển thị trong cart:
┌─────────────────────────┐
│ Freeship khi mua 350k   │
│ [███████░░░░░] 250k/350k│
│ Thêm 100k nữa nhé!      │
└─────────────────────────┘

Nếu đã freeship:
[███████████] 500k ✓ Freeship!
```

**Impact:**
- Giảm cart abandonment: 15-20%
- Tăng AOV: 10-15%

---

### LÝ DO #2: Phải tạo tài khoản (Registration friction)

**Vấn đề:**
- Checkout flow: Đăng nhập → Tạo mật khẩu → Xác nhận email → Thanh toán
- Khách sốc, bỏ giỏ: 20-25% bỏ vì lý do này

**Giải pháp:**

**1. Guest checkout (bắt buộc có)**
```
Checkout page option:
[ ] Tạo tài khoản
[✓] Mua không tài khoản (guest)

Guest checkout sẽ:
- Nhập email
- Nhập số điện thoại
- Nhập địa chỉ
- Thanh toán
- XOng (không cần login)
```

**2. Social login**
```
"Hoặc đăng nhập bằng:"
[Facebook] [Google] [Apple ID]

Tự động điền:
- Tên
- Email
- Ảnh đại diện (nếu có)
```

**3. One-click checkout**
```
Nếu khách đã mua trước:
"Mua lại nhanh? Click để dùng địa chỉ trước"
[✓] Dùng địa chỉ cũ [Thay đổi]
[✓] Dùng payment cũ [Thay đổi]
```

**Impact:**
- Guest checkout: Giảm 15-20% cart abandonment
- Social login: Giảm 30 giây process time

---

### LÝ DO #3: Checkout flow quá phức tạp (Too many steps)

**Vấn đề:**
- Checkout 5 bước: Shipping → Billing → Confirm → Payment → Order complete
- Khách bỏ ở bước 2-3

**Giải pháp:**

**1. One-page checkout**
```
Một page duy nhất, hiển thị:
- Tóm tắt sản phẩm (bên phải)
- Form nhập liệu (bên trái):
  * Email & phone
  * Địa chỉ giao
  * Địa chỉ hóa đơn (nếu khác)
  * Payment method
  * Coupon
- CTA: [Đặt hàng ngay]
```

**2. Progress indicator rõ ràng**
```
Step 1: Thông tin giao hàng [✓ DONE]
Step 2: Thanh toán [● CURRENT]
Step 3: Hoàn thành [○ PENDING]

Số % hoàn thành: 67%
```

**3. Auto-fill & smart defaults**
```
- Điền sẵn email từ cart
- Điền sẵn phone từ account
- Địa chỉ dropdown (khách tìm nhanh)
- Thanh toán: Default = COD (phổ biến nhất VN)
```

**4. Mobile-friendly checkout**
```
- Button kích thước: 48x48px (iOS standard)
- Input field: Full width (no side scrolling)
- Dropdown thay text input (khi có sẵn options)
- Numeric keypad cho phone (type="tel")
```

**Impact:**
- One-page vs multi-page: -30% abandonment
- Mobile optimization: -25% abandonment

---

### LÝ DO #4: Không tin bảo mật thanh toán

**Vấn đề:**
- Khách sợ: Hack card, lộ thông tin, lừa đảo
- 15-20% khách bỏ vì lý do này

**Giải pháp:**

**1. Trust badges (visible)**
```
Checkout page hiển thị:
🔒 SSL Secured (256-bit encryption)
✓ PCI DSS Compliant
🛡 Your payment is secure
💳 Your card info is not stored

Logo: Visa, Mastercard, SSL badge
```

**2. Transparent payment process**
```
Hiển thị:
"Thanh toán an toàn qua [Payment provider]
Chúng tôi không lưu trữ thông tin thẻ của bạn.
[Chính sách bảo mật]"
```

**3. Money-back guarantee**
```
"Không hài lòng?
Hoàn tiền 100% trong 30 ngày.
Không hỏi tại sao."
```

**4. Trust signals ở cart page (sớm)**
```
Trước đến checkout, khách đã thấy:
✓ 1000+ reviews (5 sao)
✓ Được mua lại 5000 lần
✓ Hỗ trợ 24/7
✓ Đổi/trả miễn phí
✓ Công ty thành lập 2020 [Link về us]
```

**Impact:**
- Bảo mật signal: -10% abandonment
- Trust score cao: +5% conversion

---

### LÝ DO #5: Thiếu payment methods (Limited options)

**Vấn đề:**
- Shop chỉ nhận: Transfer bank
- Khách muốn: COD (không có)
- Khách bỏ giỏ

**Giải pháp:**

**1. COD (Cash on Delivery) - BẮT BUỘC**
```
Tại VN, 60-70% khách thích COD.
Payment option:
[✓] Trả tiền khi nhận (COD) - Khuyến nghị
[ ] Chuyển khoản
[ ] Thẻ tín dụng (Visa/Mastercard)
```

**2. E-wallet integration**
```
Phổ biến ở VN:
- Momo (800M user)
- ZaloPay (200M user)
- VNPay
- VNPT Pay
- ShopeePay

Display:
[ ] Momo (Quét mã QR hoặc app)
[ ] ZaloPay
[ ] VNPay
```

**3. Bank transfer**
```
Hiển thị:
- Danh sách bank hỗ trợ
- Số tài khoản
- Tên người nhận
- Reference code (auto-generate)

Ideal: Auto-detect bank app + auto-fill
```

**4. Installment (Trả góp)**
```
"Không có tiền? Trả góp 0% lãi suất!"

Ví dụ:
- Dưới 1M: Trả góp 2-3 tháng
- 1-2M: Trả góp 3-6 tháng
- Trên 2M: Trả góp 6-12 tháng

Partner: Kredivo, Home Credit, SCB
```

**5. "Buy now, pay later" (BNPL)**
```
Mô hình:
- Khách nhận hàng
- Trả tiền sau 7 ngày
- Không lãi (nếu đúng hạn)

Phổ biến với: Gen Z, high AOV
```

**Impact:**
- COD: +20% conversion (VN market)
- 5+ payment methods: -15% abandonment
- BNPL: +10-15% tỷ lệ khách cao tuổi

---

### LÝ DO #6: Giá tăng lên khi checkout (Price creep)

**Vấn đề:**
- Khách thấy giá 250k ở product page
- Đến checkout: 250k + 50k ship + 20k tax = 320k
- Khách sốc, bỏ giỏ

**Giải pháp:**

**1. Transparent pricing từ sớm**
```
Product page:
[Giá: 250k]
+ Ship: ~50k (tùy địa chỉ)
+ Tax: 0k (đã bao gồm)
≈ Total: 300k

Không bao giờ "surprise charge"
```

**2. Add coupon field ở sớm**
```
Cart page:
[Tóm tắt sản phẩm]
Subtotal: 250k
Shipping: 50k
[________] Coupon code? (SUMMER, FIRST30, etc)

Khách sẽ check coupon trước checkout
```

**3. Tax transparency**
```
Hiển thị:
Subtotal: 250k
Tax (nếu có): 0k [Tại sao?]
Total: 250k

VN: Hầu hết B2C không tính VAT
Nếu tính → giải thích (B2B, doanh nghiệp)
```

**4. Show savings**
```
Original price: 300k
Your price: 250k
You save: 50k (17% OFF!)
```

**Impact:**
- Transparent pricing: -20% abandonment
- Show savings: +5% conversion

---

### LÝ DO #7: Thời gian giao hàng quá lâu

**Vấn đề:**
- Khách: "Khi nào nhận được hàng?"
- Shop: "3-5 ngày"
- Khách: "Quá lâu", bỏ giỏ

**Giải pháp:**

**1. Estimated delivery date rõ ràng**
```
Checkout page:
Bạn sẽ nhận hàng: [Thứ Tư, 15 Tháng 4]
(Tính từ hôm nay)

Hoặc:
Estimated delivery: 2-3 ngày
Nhanh hơn? +30k cho express (1-2 ngày)
```

**2. Countdown timer (tạo urgency)**
```
"Order trong 2 giờ nữa → Giao vào 14/4"
(Sau 2 giờ → Giao vào 15/4)

Hoặc:
"Order hôm nay, giao trong 24h!"
(Dành cho same-city)
```

**3. Phân loại shipping tốc độ**
```
[ ] Standard (3-5 ngày) - FREE
[ ] Express (1-2 ngày) - +30k
[ ] Super express (same day) - +60k

Display: "Bạn sẽ nhận: [Date]"
```

**4. Regional clarity**
```
Khách nhập địa chỉ → System auto-detect:
"Hà Nội: Giao 1-2 ngày"
"Hồ Chí Minh: Giao 2-3 ngày"
"Tỉnh khác: Giao 3-5 ngày"
```

**Impact:**
- Delivery transparency: -10% abandonment
- Express shipping availability: +8% conversion

---

### LÝ DO #8: Không hỗ trợ COD (Only prepay)

**Vấn đề (đã mention ở #5 nhưng cần emphasis):**
- 60-70% khách VN chỉ muốn COD
- Nếu không có → 70% bỏ giỏ

**Giải pháp:**
- BẮT BUỘC hỗ trợ COD
- Default selection = COD
- Highlight: "Trả tiền khi nhận"

**Impact:**
- COD availability: +20-30% conversion (so với prepay-only)

---

### LÝ DO #9: Coupon không hoạt động / Khó nhập

**Vấn đề:**
- Khách có code giảm giá
- Nhập coupon → "Code hết hạn" hoặc "Lỗi hệ thống"
- Khách bỏ giỏ

**Giải pháp:**

**1. Coupon input optimization**
```
[ __________ ] Coupon code?
[Áp dụng]

Hoặc auto-apply (tốt hơn):
Coupon code: [__________]
Auto-apply when valid ✓

UX tốt hơn: Auto detect + format auto
```

**2. Clear coupon validation**
```
Nếu invalid:
❌ "SUMMER50" hết hạn (hết từ 10/4)
✓ Thử code khác: FIRST30 (giảm 30k)

Không phải: "Code không tồn tại" (khô khan)
```

**3. Visible coupon availability**
```
Hiển thị active coupon trước checkout:
"Mã giảm giá có sẵn:
💰 FIRST30: -30k (lần mua đầu)
💰 SUMMER: -50k (đơn >500k)
💰 FRIEND: -20k (giới thiệu)"
```

**4. Auto-apply best coupon**
```
Nếu khách có multiple coupon:
"Bạn có 2 coupon. Áp dụng cái tốt nhất:
SUMMER (-50k) [Dùng cái khác]"
```

**Impact:**
- Coupon UX improvement: -12% abandonment
- Visible coupon: +8% coupon redemption rate

---

### LÝ DO #10: Mobile-unfriendly checkout

**Vấn đề:**
- Desktop version auto-scale xuống mobile
- Button quá nhỏ, form quá rộng
- 83-85% mobile abandonment

**Giải pháp:**

**1. Thumb-friendly design**
```
- Button size: Min 48x48px (iOS guideline)
- Spacing: Min 16px giữa elements
- No pinch-to-zoom form fields
- Fullwidth input (96-100% screen width)
```

**2. Mobile form optimization**
```
Desktop:
[Name________________] [Phone________________]

Mobile:
[Name____________________]
[Phone___________________]

One column layout, not side-by-side
```

**3. Numeric/email keyboard**
```
<input type="tel" placeholder="0912345678">
→ Numeric keypad appears

<input type="email" placeholder="name@example.com">
→ Email keyboard with @

<input type="date">
→ Date picker
```

**4. Collapse address form**
```
[Tỉnh/Thành phố: [=====dropdown=====] ]
[Quận/Huyện: [=====dropdown=====] ]
[Xã/Phường: [=====dropdown=====] ]
[Số nhà/Đường: [____________________] ]

Nên dùng dropdown + text, không text alone
```

**5. Floating action button**
```
Mobile:
- Floating button "Thanh toán" (bottom right, sticky)
- Hiển thị giá current + button
- Không cần scroll qua form mới thấy button
```

**Impact:**
- Mobile optimization: -25% mobile abandonment
- Thumb-friendly: +12% mobile completion rate

---

### LÝ DO #11: No social proof / Reviews lại (Perceived risk)

**Vấn đề:**
- Khách không biết sản phẩm thực tế như thế nào
- Sợ mua sẽ "lỗi đơn"

**Giải pháp:**

**1. Reviews trên product & cart page**
```
Product page:
⭐⭐⭐⭐⭐ 4.8/5 (1,247 reviews)
"Hàng đẹp, giao nhanh, lần sau mua lại" - Hoa Hồng
"Đúng hình, đúng chất lượng!" - Minh Anh

Cart page:
[Product info]
⭐ 4.8/5 - 1,247 people bought this
```

**2. "Verified purchase" badge**
```
⭐⭐⭐⭐⭐ "Rất tốt!"
Nguyễn Văn A ✓ Verified Purchase
```

**3. Recent activity**
```
"47 people bought this in last 24 hours"
"100 views today, 5 in cart"
```

**4. Video reviews/unboxing**
```
Checkout page:
[Video] "Unboxing + Review - 3 sao"
"Chất lượng tốt, ship nhanh"
```

**Impact:**
- Social proof on checkout: -15% abandonment
- Video reviews: +8% conversion

---

### LÝ DO #12: Unexpected additional fees (Tax, VAT, etc.)

**Vấn đề:**
- Khách thấy final price ở checkout lần đầu tiên
- "Sao lại có thêm phí?"
- Bỏ giỏ

**Giải pháp:**

**1. Transparent all-in pricing**
```
Product page:
Giá: 250k (đã bao gồm VAT, nếu có)
Không có phí ẩn

Cart page:
Subtotal: 250k
Ship: 50k
TAX: 0k ← Clarify "đã bao gồm trong giá"
TOTAL: 300k
```

**2. Fee breakdown**
```
Checkout:
Subtotal: 250k
Shipping (TP.HCM): 50k
Insurance (optional): 10k [Tại sao?]
---
TOTAL: 310k

Giải thích từng fee rõ ràng
```

**Impact:**
- Transparent fee: -15% abandonment

---

### LÝ DO #13: Khách chưa sẵn sàng tâm lý (Too early to commit)

**Vấn đề:**
- Khách chỉ "browse", chưa decide
- Add giỏ tạm, sẽ comeback sau
- Quay lại quá lâu → Bỏ (không nhớ, hoặc đã thay đổi ý)

**Giải pháp (ở cart page, trước checkout):**

**1. Wishlist/Save for later**
```
[Thêm vào giỏ hàng]
[Lưu để xem sau] ← Separate action

Khách có thể save mà không commit
```

**2. Comparison tool**
```
"Đang chọn giữa 2 sản phẩm?
[Sản phẩm A] vs [Sản phẩm B]
Compare →"
```

**3. Size/fit assistant**
```
"Bạn không chắc size?"
[Đo size nhanh] ← Interactive tool
→ Recommend size
```

**Impact:**
- Wishlist: Khách sẽ comeback, -5% cart abandonment
- Giảm stress: -10% ngay cả nếu chưa chốt

---

### LÝ DO #14: Competitor remarketing pressure

**Vấn đề:**
- Khách đang xem ở shop A
- Thấy ads shop B rẻ hơn
- Switch tab, bỏ shop A

**Giải pháp:**

**1. Competitor price match**
```
"Thấy giá rẻ hơn ở shop khác?
[Report] → Chúng tôi sẽ match giá"
```

**2. Unique value prop clarity**
```
Hiển thị rõ:
"Tại sao chọn mình vs shop khác:
✓ Giao nhanh nhất (24h)
✓ Bảo hành 1 năm (shop khác 30 ngày)
✓ Hỗ trợ 24/7 vs AI"
```

**3. Urgency + scarcity**
```
"Còn 3 cái cuối
Có 5 người khác đang xem"

(Nếu thực tế - không spam)
```

**Impact:**
- Clear differentiation: -8% abandonment

---

### LÝ DO #15: Technical issues (Slow page, SSL error, etc.)

**Vấn đề:**
- Checkout page load quá lâu (> 3s)
- SSL error
- Form submission fail
- Khách bỏ

**Giải pháp:**

**1. Page speed optimization**
```
Target: < 2s load time (mobile)
- Compress images
- Minimize CSS/JS
- CDN for static assets
- Lazy load non-critical content

Tool: Google PageSpeed Insights
```

**2. Form submission reliability**
```
UX:
- Loading indicator khi submit
- Error message rõ ràng nếu fail
- Auto-retry logic
- Save progress (không bao giờ mất data)
```

**3. Error recovery**
```
Nếu error:
"❌ Lỗi thanh toán
Vui lòng:
[Thử lại] [Thay đổi payment method] [Chat hỗ trợ]"

Không phải: "Error" (khô khan)
```

**Impact:**
- < 2s load: +5-10% conversion
- Good error handling: -5% frustration exit

---

## CART PAGE OPTIMIZATION

### Layout tối ưu:

```
[Header: Giỏ hàng]

[Left: Product list]
[Product 1] [x]     250k    [Qty: 1] ✓
[Product 2] [x]     500k    [Qty: 1] ✓

Add coupon: [________] [Apply]

[Right: Summary]
Subtotal:      250k
Shipping:      50k
Coupon:        -0k [Add code]
───────────────────
TOTAL:         300k

[CTA: Thanh toán ngay] ← Big, contrasting color

Continue shopping? [Mua thêm]

[Below: Trust signals]
✓ 100% bảo mật
✓ Miễn phí đổi trong 30 ngày
✓ Đổi tiền nếu không thích
```

### Upsell opportunities ở cart page:

**1. Frequently bought together**
```
Khách có: Áo khoác
Suggest: "Người mua áo khoác thường mua:
🛒 Quần tây (480k)
🛒 Giày (500k)

Thêm combo? [Yes] [No]"
```

**2. Volume discount incentive**
```
Khách có 1 sản phẩm:
"Mua 2 cái → Giảm 10%/cái
Mua 3+ cái → Giảm 15%/cái

Số lượng: [1▼]"
```

**3. Gift wrapping**
```
[☐] Gói quà đẹp (+20k)
   "Để lại lời nhắn cho người nhận"
```

**Impact:**
- Upsell ở cart: +10-15% AOV

---

## CHECKOUT FORM OPTIMIZATION

### Required vs Optional fields:

**Bắt buộc:**
- Tên
- Phone
- Email
- Địa chỉ giao
- Payment method

**Tùy chọn:**
- Địa chỉ hóa đơn (checkbox: "Giống địa chỉ giao")
- Note đặc biệt (Leave at door, etc.)
- Gift message

**Không nên hỏi:**
- Birthday (trừ gift card)
- Occupation
- Income
- Bất cứ thứ gì không cần delivery

---

## TRUST SIGNALS PLACEMENT

### Ở cart page:
```
[Top of page]
✓ SSL Secured 🔒
✓ 50,000+ Happy Customers
✓ 4.8⭐ Rating
```

### Ở checkout page:
```
[Left column - Product review]
⭐⭐⭐⭐⭐ "Chất lượng tuyệt vời!"
"Giao nhanh, packaging đẹp"

[Right column - Payment]
🔒 Your payment is secure
✓ No hidden fees
✓ Money-back guarantee
[SSL badge] [Verified by VeriSign]
```

### Ở summary:
```
Subtotal: 250k
Shipping: 50k
─────────────
TOTAL: 300k

✓ Đảm bảo 100% an toàn
✓ Hoàn tiền nếu không thích
✓ Chat 24/7 hỗ trợ
```

---

## MOBILE CHECKOUT CHECKLIST

### Design:
- [ ] 1-column layout
- [ ] Large buttons (48x48px min)
- [ ] Full-width inputs
- [ ] Proper keyboard types (tel, email)
- [ ] Sticky floating button

### Performance:
- [ ] < 2 second load time
- [ ] No redirects (minimize HTTP requests)
- [ ] Compress images
- [ ] Lazy load

### Functionality:
- [ ] Guest checkout available
- [ ] Auto-fill from profile
- [ ] Address auto-complete
- [ ] Payment method selector
- [ ] Progress indicator

---

## ABANDONED CART RECOVERY SEQUENCE

### Email 1 (1 hour after abandon)
```
Subject: "Quên 250k trong giỏ hàng? 🛒"
Body:
Hi [Name],

Chúng tôi thấy bạn vừa để giỏ hàng:
[Product thumbnail] Áo khoác Nike - 250k

[Recover cart link - personalized]

Có vấn đề gì không?
- Hỏi về vận chuyển? Chat 24/7
- Coupon không hoạt động? [Fix]
- Thay đổi ý định? [Save for later]

Hãy hoàn tất đơn hàng trước khi hết hàng!

[Single CTA: Complete your purchase]
```

### SMS 1 (3 hours after, if has phone)
```
"Bạn vừa để sản phẩm trong giỏ.
Order ngay freeship + quà tặng!
[Link]"
```

### Email 2 (24 hours after)
```
Subject: "Giảm thêm 100k cho đơn hàng của bạn 💝"
Body:
Hi [Name],

Chúng tôi không muốn bạn bỏ qua cơ hội này.

Nếu bạn hoàn tất đơn hàng trong 24h:
✓ Giảm thêm 100k
✓ Freeship
✓ Quà tặng

[Recover cart with incentive]

Valid until: [24h countdown]
```

### Email 3 (3 days after, if still abandoned)
```
Subject: "Hàng sắp hết 😱"
Body:
Hi [Name],

Sản phẩm Áo khoác Nike mà bạn xem:
⚠️ Chỉ còn 1 cái cuối
⚠️ Khách khác đang xem

Quyết định nhanh?

[Recover with URGENCY messaging]

"Không còn giảm giá, nhưng freeship + quà"
```

### Retargeting ads (24h-7d after)
```
Facebook/Google/TikTok:
Visual: Product image
Copy: "Quên rồi?
Áo khoác Nike 250k
Giảm thêm 100k nếu order trong 24h
[Recover link]"
```

---

## KPI THEO DÕI

### Metrics:
1. **Cart abandonment rate** (Target: < 40%)
   - Formula: (Total carts created - Total purchases) / Total carts created
   - VN average: 70%, good: 40-50%

2. **Checkout completion rate** (Target: > 60%)
   - Từ cart page → thanh toán thành công
   - Measure at each step (cart → shipping → payment → confirm)

3. **Average cart value** (Track by device, region)

4. **Payment method distribution**
   - % COD vs prepay vs e-wallet
   - Nếu COD < 40% → Có vấn đề UX

5. **Cart recovery rate** (Target: 10-15%)
   - Số khách comeback từ email/SMS recovery

6. **Mobile vs desktop completion rate**
   - Track separately

---

## AUDIT CHECKLIST: CHECKOUT PAGE

### Design & UX:
- [ ] One-page or 2-step max
- [ ] Clear progress indicator
- [ ] Mobile-responsive
- [ ] < 2s load time
- [ ] Large CTA button (48px+)

### Form:
- [ ] Min required fields
- [ ] Guest checkout option
- [ ] Auto-fill enabled
- [ ] Social login available
- [ ] Address auto-complete

### Pricing transparency:
- [ ] No price surprises at checkout
- [ ] Shipping cost visible early
- [ ] Tax/fees breakdown clear
- [ ] Coupon field visible

### Trust:
- [ ] SSL badge visible
- [ ] Trust seals displayed
- [ ] Money-back guarantee
- [ ] Reviews/social proof
- [ ] Support contact (chat/phone)

### Payment:
- [ ] COD available + default
- [ ] E-wallet (Momo, ZaloPay, VNPay)
- [ ] Credit card (Visa, Mastercard)
- [ ] Installment option
- [ ] Clear payment icons

### Security:
- [ ] No card data storage (PCI compliance)
- [ ] HTTPS enabled
- [ ] Privacy policy link
- [ ] Data protection message

### Mobile:
- [ ] Thumb-friendly buttons
- [ ] Full-width inputs
- [ ] Proper keyboards (tel, email)
- [ ] No pinch-to-zoom
- [ ] Floating action button

