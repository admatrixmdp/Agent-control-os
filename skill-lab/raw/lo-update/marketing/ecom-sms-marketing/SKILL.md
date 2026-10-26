---
name: Chiến lược SMS Marketing TMĐT Việt Nam
description: Hướng dẫn SMS Marketing cho thương mại điện tử Việt Nam. Bao gồm tại sao SMS, loại SMS (transactional, promotional, reminder, loyalty), templates tiếng Việt, compliance pháp luật VN, SMS providers VN, Brandname vs Number SMS, segmentation, automation triggers, SMS + Email + Zalo integration, metrics, cost analysis, A/B testing. Dùng khi cần "SMS marketing", "SMS strategy", "abandoned cart SMS", "SMS compliance", "SMS provider"
---

# Chiến lược SMS Marketing cho Thương Mại Điện Tử Việt Nam

## 1. Tại sao SMS là kênh quan trọng cho TMĐT VN

### 1.1 Các con số quan trọng

SMS có những con số ấn tượng về hiệu quả:

**Open rate:** 98%
- Email: 20-25% (người dùng bỏ qua, vào spam)
- SMS: 98% (người mở vì chỉ có tin quan trọng)
- Kết luận: Hầu hết người nhận sẽ thấy tin

**Read rate:** 90% được đọc trong 3 phút
- Email: Trung bình 48 giờ sau nhận
- SMS: 3 phút (rất nhanh)
- Kết luận: Thời gian phản ứng nhanh nhất

**Response rate:** 30-40%
- Email: 1-5%
- SMS: 30-40%
- Kết luận: Khách hàng tương tác cao

**Conversion rate:** 30-45%
- Email: 1-3%
- SMS: 30-45%
- Kết luận: SMS là channel conversion cao nhất

### 1.2 Tại sao SMS phù hợp Việt Nam

**Không cần internet:**
- Việt Nam vẫn có vùng internet chậm
- SMS chỉ cần tin nhắn 3G/4G (hoặc cả 2G)
- Email cần đủ dung lượng mở app
- Giải pháp: SMS tiếp cận khách ngay cả ngoài thành phố

**Phổ biến & tin cậy:**
- Hầu hết người Việt có điện thoại
- Người lớn tuổi (40+) dùng SMS, không dùng Facebook
- TMĐT cần tiếp cận toàn bộ segment
- SMS là cầu nối: trẻ đến già

**Chi phí thấp:**
- SMS: 300-500 VND/tin (0.01-0.02 USD)
- Email: ~0 (nhưng open rate thấp)
- SMS ROI: 40:1 (chi 1 triệu đổi 40 triệu doanh số)

**Immediate action:**
- Flash sale, limited offer: SMS thay vì email
- Khách xem ngay, mua ngay
- Không đợi (kiểm tra email)

**Compliance thuận tiện:**
- Opt-out dễ: Reply "STOP"
- Opt-in dễ: Checkbox ở checkout
- Quản lý: Khách tự quản lý sub/unsub

## 2. Các loại SMS cho TMĐT

Có 4 loại SMS cơ bản cho TMĐT. Mỗi loại có mục đích, timing, content riêng.

### 2.1 Transactional SMS (SMS giao dịch)

**Định nghĩa:** SMS liên quan trực tiếp đến hành động của khách (thanh toán, giao hàng).

**Loại transactional SMS:**

1. **Order confirmation (Xác nhận đơn hàng)**
   - Khi nào: Ngay sau khi khách nhấn "Order"
   - Nội dung: Mã đơn, tổng tiền, ETA giao
   - Độ dài: 1 tin
   - Ví dụ:
   ```
   "Xac nhan don hang #ORD123456. Tong: 500K. Giao 2-3 ngay. Chi tiet: https://link"
   ```
   - Quan trọng: Phải gửi (pháp lý, khách cần chứng minh)
   - Tỷ lệ success: 99%+ (khách chờ SMS này)

2. **Payment confirmation (Thanh toán thành công)**
   - Khi nào: Ngay sau transaction (1-2 giây)
   - Nội dung: Mã thanh toán, số tiền, phương thức
   - Độ dài: 1 tin
   - Ví dụ:
   ```
   "Thanh toan thanh cong 500,000 VND cho don hang #ORD123456. TG: 14:35 19/04/2026. Cam on!"
   ```
   - Chức năng: Tạo tin cậy, xác nhận không mất tiền
   - Tỷ lệ success: Giảm abandoned checkout

3. **Shipping update (Cập nhật vận chuyển)**
   - Khi nào: Khi hàng được gửi, trị đạo, giao
   - Nội dung: Trạng thái, tracking link, ETA
   - Tần suất: 1-3 SMS per order (gửi, trị đạo, giao)
   - Ví dụ:
   ```
   "[Brand] Don hang #ORD123456 dang giao. Track: https://link. Giao hom nay 18h"
   ```
   - Chức năng: Giảm chat support (khách tự biết tình trạng)
   - Tỷ lệ success: Rất cao (khách chủ động theo dõi)

4. **Delivery confirmation (Xác nhận giao hàng)**
   - Khi nào: Sau khi giao hàng thành công
   - Nội dung: "Giao thành công", link đánh giá
   - Độ dài: 1 tin
   - Ví dụ:
   ```
   "[Brand] Don hang #ORD123456 da giao thanh cong. Danh gia de nhan 50K: https://link"
   ```
   - Chức năng: Kích đánh giá (UGC, social proof)
   - Tỷ lệ success: 60-70% đánh giá (nếu có incentive)

5. **Password reset (Đặt lại mật khẩu)**
   - Khi nào: Khách quên password, click "Reset"
   - Nội dung: OTP, link reset
   - Độ dài: 1 tin
   - Ví dụ:
   ```
   "[Brand] Ma OTP: 123456. Co hieu luc 10 phut. Khong chia se voi ai"
   ```
   - Chức năng: Security, identity verification
   - Tỷ lệ success: 100% (bắt buộc)

**Transactional SMS best practices:**
- Gửi ngay (không trễ hơn 5 phút)
- Ghi số điện thoại khách ở đó để verify
- Không bán hàng trực tiếp ở SMS này
- Format: Chuyên nghiệp, cấu trúc rõ ràng
- Không chứa emoji (khiến tin bị cut off)
- Áp dụng cho 100% khách (opt-in không cần, đây là xác nhận)

### 2.2 Promotional SMS (SMS quảng cáo)

**Định nghĩa:** SMS marketing, bán hàng, khuyến mãi.

**Loại promotional SMS:**

1. **Flash sale (Khuyến mãi giới hạn thời gian)**
   - Timing: Sáng 7-8h, trưa 12-13h, tối 19-20h (peak time)
   - Duration: 2-4 giờ (tạo urgency)
   - Content: Giảm giá %, code, link, "Hết hàng mất"
   - Ví dụ:
   ```
   "[Brand] FLASH SALE! Giam 50% tat ca ao phong. Code: FLASH50. Mua: https://link. Chi 2h con"
   ```
   - Length: 1 tin (max 160 ký tự)
   - Tần suất: 3-5 SMS/tuần (không spam)
   - ROI: 300-500% (flash sale drive urgent purchase)
   - Tracking: Unique code (FLASH50) để measure conversion

2. **New product launch (Sản phẩm mới)**
   - Timing: Morning 8-9h (khách check news)
   - Content: "Hàng mới vừa về", teaser, link
   - Độ dài: 1-2 tin
   - Ví dụ:
   ```
   "[Brand] HANG MOI VUA VE! Ao Khoac Mua Long mau 5 mau. Sieu tho, re nhat mua nay. Mua ngay: https://link"
   ```
   - Duration: 1-2 tuần (sau launch, giảm tần suất)
   - ROI: 150-250% (khách mới, high intention)

3. **Discount code (Mã giảm giá)**
   - Timing: Mỗi 5-7 ngày gửi 1 lần
   - Content: "Khoá deal 20%, code SUMMER20"
   - Duration: 5-7 ngày (tạo urgency)
   - Ví dụ:
   ```
   "[Brand] Deal HOT! Giam 20% don hang. Code: SUMMER20. Giao HCM free. Mua day: https://link"
   ```
   - Frequency: 2-3 SMS/tuần (sustainable)
   - ROI: 200-400% (repeat customers)

4. **VIP/Loyalty exclusive (Ưu đãi khách thân)**
   - Timing: Sau khi khách mua, thành VIP
   - Content: "Khách VIP được 30% hôm nay"
   - Độ dài: 1 tin
   - Ví dụ:
   ```
   "Chuc mung! Ban la khach VIP. Nhan 30% hom nay code: VIP30. Chi con 2h. Mua ngay: https://link"
   ```
   - Tần suất: 1-2 SMS/tuần (exclusive)
   - ROI: 400-600% (VIP conversion cao)

5. **Cross-sell / Upsell (Bán chéo / tăng giá trị)**
   - Timing: Sau khi khách mua (next day)
   - Content: "Bạn mua áo, gợi ý quần mix"
   - Độ dài: 1 tin
   - Ví dụ:
   ```
   "Ban vua mua ao somi trang. Ban co can quan den hop? Giam 15% khi mua ca bo. Code: COMBO15"
   ```
   - Tần suất: 1-2 SMS/tuần (khi phù hợp)
   - ROI: 200-350% (khách muốn matched items)

6. **Event/seasonal (Mùa lễ hội, sự kiện)**
   - Timing: Tết, Valentine, Halloween, Giáng sinh
   - Content: "Tết đến, mua quà giảm 40%"
   - Duration: 2-3 tuần (cảnh báo + reminder)
   - Ví dụ:
   ```
   "TET NAY DAT QUA HOT! Ao phong, ao dung giam 40%. Giao nhanh, mua ngay: https://link"
   ```
   - Frequency: 3-5 SMS (teaser, reminder, last call)
   - ROI: 500-800% (seasonal impulse buying)

7. **Referral program (Giới thiệu bạn)**
   - Timing: Ngoại random (khi có campaign)
   - Content: "Giới thiệu bạn được 100K"
   - Độ dài: 1 tin
   - Ví dụ:
   ```
   "Ban tro thanh nhan vien quang cao! Gioi thieu ban be, nhan 100K moi ban. Chi se: https://link"
   ```
   - Tần suất: 1-2 SMS/tháng (không thường xuyên)
   - ROI: 300-400% (viral loop)

**Promotional SMS best practices:**
- Có CTA rõ ràng ("Mua ngay", "Đặt hàng", "Click link")
- Unique tracking code (measure ROI chính xác)
- Mỗi SMS chỉ có 1 offer (không overwhelm)
- Gây urgency (limited time, limited stock)
- Personalization: "Tên khách, mua lần trước"
- Frequency: 2-3 SMS/tuần (nhiều hơn = unsubscribe)
- Tối ưu timing (peak hours)

### 2.3 Reminder SMS (SMS nhắc nhở)

**Định nghĩa:** Nhắc nhở khách một hành động hoặc cơ hội sắp hết.

**Loại reminder SMS:**

1. **Abandoned cart (Giỏ hàng bỏ rơi)**
   - Timing: 1 giờ sau khi khách abandon cart
   - Content: "Quên mua rồi", reminder, ưu đãi
   - Ví dụ:
   ```
   "Ban de trong gio hang ao somi trang 500K. Quay lai mua, giam 10% code QUAYLAI: https://link"
   ```
   - Conversion rate: 20-30% (rất cao)
   - ROI: 1000%+ (doanh số bỏ qua)
   - Tần suất: 1 tin duy nhất (không spam lại)
   - Tip: Thêm incentive (10-15% off) để trigger conversion

2. **Voucher expiring (Voucher sắp hết hạn)**
   - Timing: 2-3 ngày trước hết hạn
   - Content: "Voucher bạn hết hạn ngày 20/4"
   - Ví dụ:
   ```
   "[Brand] Voucher 50K ban het han 20/4. Su dung ngay de khong tro thanh lich su: https://link"
   ```
   - Conversion: 10-20% (khách nhớ lại)
   - ROI: 500% (bảo toàn doanh số)
   - Tần suất: 1-2 SMS (warning + final reminder)

3. **Reorder reminder (Nhắc nhở mua lại)**
   - Timing: 30-45 ngày sau khi khách mua lần trước
   - Content: Sản phẩm tương tự, discount
   - Ví dụ:
   ```
   "Ban mua ao somi trang 30 ngay truoc. Hang vua ve. Quay lai mua, giam 15% code QUAYLAI: https://link"
   ```
   - Conversion: 15-25% (khách familiar)
   - ROI: 300-400% (repeat customer)
   - Tần suất: Tối đa 3 lần/năm (1 lần 4 tháng)
   - Personalization: Mention sản phẩm cũ mua

4. **Birthday/Anniversary (Sinh nhật, ngày kỷ niệm)**
   - Timing: Ngày sinh nhật khách
   - Content: "Chúc mừng sinh nhật, giảm 30%"
   - Ví dụ:
   ```
   "Chuc mung sinh nhat ban! Tong sinh nhat giam 30% code: HAPPYDAY30. Mua ngay: https://link"
   ```
   - Conversion: 25-35% (emotional, personal)
   - ROI: 400-500%
   - Tần suất: 1 lần/năm (automatic)
   - Tip: Phải collect birthdate ở checkout

5. **Event/Webinar reminder (Sự kiện sắp tới)**
   - Timing: 2 ngày trước, ngày event
   - Content: "Webinar về skincare 20h hôm nay"
   - Ví dụ:
   ```
   "Webinar SKINCARE TIPS NHAM TRANG hom nay 20h. Tham gia lay qua 200K. Dang ky: https://link"
   ```
   - Conversion: 30-50% (attendance rate)
   - ROI: Indirect (tuy built brand loyalty)
   - Tần suất: 2-3 SMS (teaser + reminder)

**Reminder SMS best practices:**
- Cá nhân hóa (dùng tên khách)
- Gợi ý discount nếu cần (15-20% để trigger action)
- Rõ deadline (tạo urgency)
- Dùng reminder, không hard sell
- Timing quan trọng (gửi lúc khách sẵn sàng action)

### 2.4 Loyalty SMS (SMS khách thân)

**Định nghĩa:** SMS liên quan đến loyalty program, points, rewards.

**Loại loyalty SMS:**

1. **Points earned (Điểm thưởng mới)**
   - Khi nào: Ngay sau khi khách mua
   - Content: "Bạn vừa kiếm 50 điểm"
   - Ví dụ:
   ```
   "Ban kiếm 50 diem tu don hang #ORD123456. Tong diem: 250. 500 diem = voucher 100K. Nhap: https://link"
   ```
   - Tần suất: Mỗi lần mua
   - Chức năng: Encourage repeat purchase
   - Engagement: +20% (if points visible)

2. **VIP tier upgrade (Nâng hạng)**
   - Khi nào: Khách đạt ngưỡng (VIP, Platinum)
   - Content: "Chúc mừng lên hạng VIP"
   - Ví dụ:
   ```
   "Chuc mung! Ban len VIP tier! Nhan 30% off + free ship + special support. Chi se: https://link"
   ```
   - Tần suất: Whenever upgraded
   - Chức năng: Make khách feel special
   - Loyalty: +30% (feel recognized)

3. **Reward redemption (Đổi điểm thành tiền)**
   - Khi nào: Khi khách đủ điểm để đổi
   - Content: "Bạn đủ điểm để lĩnh voucher"
   - Ví dụ:
   ```
   "Ban da du 500 diem! Doi ngay lay voucher 100K. Chi can bam: https://link"
   ```
   - Tần suất: Khi đủ threshold
   - Chức năng: Motivate redemption (act on reward)
   - Conversion: 60-80% (high redemption rate)

4. **Member exclusive (Ưu đãi riêng)**
   - Khi nào: Member-only sale
   - Content: "Member được hôm nay, vip 40%"
   - Ví dụ:
   ```
   "Chi thanh vien dat! Giam 40% all items. Code: MEMBER40. Co hieu luc 24h. Mua day: https://link"
   ```
   - Tần suất: 1-2 SMS/tuần (exclusive để member feel special)
   - Conversion: 35-50% (member priority)

5. **Loyalty milestone (Cột mốc)**
   - Khi nào: Khách đạt mốc (1 năm, 10 lần mua, 1M tiền)
   - Content: "Cảm ơn khách hàng thân thiết"
   - Ví dụ:
   ```
   "Ban la khach hang nam dau cua chung toi! Cam on! Nhan voucher 500K special gift: https://link"
   ```
   - Tần suất: 1-2 lần/năm (milestone)
   - Chức năng: Deep loyalty, customer delight
   - Lifetime value: +50% (khách quay lại)

**Loyalty SMS best practices:**
- Highlight benefits (điểm, voucher, special treatment)
- Make it easy to use (1-click redemption)
- Celebrate milestone (khách cảm thấy valued)
- Personalization: Tên + loyalty status
- Tần suất: Regular but not overwhelming
- Không bán hàng trực tiếp (softer touch)

## 3. SMS Templates tiếng Việt (Max 160 ký tự/tin)

SMS có giới hạn 160 ký tự. Tiếng Việt có dấu, nên thường là 155 ký tự để safe.

### 3.1 Transactional SMS Templates

**Template 1: Order confirmation**
```
[Brand] XAC NHAN DON HANG #ORD123456
Tong tien: 500K
Giao trong 2-3 ngay
Trang thai: https://link
```
(Length: 90 ký tự)

**Template 2: Payment confirmation**
```
Thanh toan thanh cong 500,000 VND
Don hang #ORD123456
TG: 14:35 19/04/2026
Cam on!
```
(Length: 85 ký tự)

**Template 3: Shipping update**
```
[Brand] Don hang #ORD123456 dang giao
Trai xe se toi 18h hom nay
Trang thai: https://link
Goi co van de call: 0392XXXXXX
```
(Length: 105 ký tự)

**Template 4: Delivery confirmation**
```
Don hang #ORD123456 da giao thanh cong!
Danh gia de nhan qua 50K
Danh gia: https://link
Cam on!
```
(Length: 85 ký tự)

### 3.2 Promotional SMS Templates

**Template 1: Flash sale**
```
[Brand] FLASH SALE! Giam 50% tat ca
Ao phong, ao somi, quan. Code: FLASH50
Chi con 2h, hang gioi han
Mua: https://link
```
(Length: 95 ký tự)

**Template 2: New product**
```
HANG MOI! Ao Khoac Mua Long mau 5
Sieu tho, duoi 300K. Hang co han
Mua ngay: https://link
Free ship HCM/HN
```
(Length: 95 ký tự)

**Template 3: Discount code**
```
Deal HOT! Giam 20% don hang
Code: SUMMER20
Free ship on 200k+
Chi con 5 ngay! Mua: https://link
```
(Length: 90 ký tự)

**Template 4: VIP exclusive**
```
Chuc mung! Ban la VIP member
Nhan 30% hom nay code: VIP30
Chi con 2h, hang gioi han
Mua: https://link
```
(Length: 95 ký tự)

### 3.3 Reminder SMS Templates

**Template 1: Abandoned cart**
```
Ban de trong gio hang ao somi trang 500K
Quay lai mua, giam 10% code: QUAYLAI
Co hieu luc 3 ngay. Mua: https://link
Cam on!
```
(Length: 105 ký tự)

**Template 2: Voucher expiring**
```
Voucher 50K ban het han 20/4
Su dung ngay de khong mat gia
Code: VOUCHER50
Mua: https://link
```
(Length: 90 ký tự)

**Template 3: Reorder reminder**
```
Ban mua ao somi trang 1 thang truoc
Hang vua ve! Giong hang cu ban thich
Giam 15% code: QUAYLAI. Mua: https://link
```
(Length: 100 ký tự)

### 3.4 Loyalty SMS Templates

**Template 1: Points earned**
```
Ban kiếm 50 diem tu don hang #ORD123456
Tong diem: 250/500 (nua dung rui)
500 diem = voucher 100K
Cung co gang!
```
(Length: 105 ký tự)

**Template 2: VIP upgrade**
```
Chuc mung! Ban len VIP tier!
Nhan 30% off + free ship + ho tro 24/7
Uu dai VIP: https://link
Cam on da tin tuong!
```
(Length: 100 ký tự)

**Template 3: Reward redemption**
```
Ban da du 500 diem!
Doi ngay lay voucher 100K
Thoi han: 30 ngay
Doi ngay: https://link
```
(Length: 90 ký tự)

## 4. SMS Compliance & Pháp luật Việt Nam

### 4.1 Luật chống spam Việt Nam

**Luật liên quan:**
- Luật Viễn thông (2009, sửa đổi 2019)
- Quyết định 1873 của UBND (2013) về quản lý tin nhắn quảng cáo
- Điều 76 Luật Giao dịch điện tử (2005)

**Quy định chính:**

1. **Opt-in/Opt-out yêu cầu:**
   - Khách phải chủ động đồng ý nhận SMS
   - Checkbox tại checkout: "Tôi muốn nhận tin khuyến mãi"
   - Mặc định: Unchecked (khách chủ động chọn)
   - Lưu evidence: Lưu screenshot consent

2. **Sender ID (Nguồn gửi):**
   - Quảng cáo: Phải có tên brand (VD: "[BRAND]" hoặc "Brandname")
   - Không dùng số điện thoại riêng để spam
   - Brandname SMS: Brand tên hiển thị, lợi tin phí cao

3. **Giờ gửi SMS:**
   - Cho phép: 7:00 - 21:00 hàng ngày
   - Ngoài giờ: Coi như spam/quấy rối
   - Tip: Gửi 8:00-20:00 (safe buffer)
   - Weekend: Chủ nhật cho phép (không có quy định cụ thể)

4. **Nội dung:**
   - Không spam, lừa đảo, xúc phạm
   - Phải có thông tin liên hệ (hotline)
   - Không fake tin từ cơ quan nhà nước
   - Không chứa malware, link độc hại

5. **Opt-out (Hủy đăng ký):**
   - Khách reply "STOP" hoặc "DUNG": Tự động hủy
   - Phải xử lý trong 24 giờ
   - Không gửi lại sau opt-out
   - Lưu log: Khi nào khách opt-out

6. **Data privacy:**
   - Lưu số điện thoại an toàn (mã hóa)
   - Không bán/chia sẻ số điện thoại cho bên thứ 3
   - GDPR compliance (if customers in EU)

### 4.2 Best practices compliance

**Checklist:**
- [ ] Consent form: "Tôi muốn nhận SMS khuyến mãi"
- [ ] Opt-out easy: "Reply STOP to unsubscribe"
- [ ] Sender ID: Tên brand rõ ràng
- [ ] Giờ gửi: 7:00-21:00
- [ ] Contact info: Hotline/email ở SMS
- [ ] GDPR: If applicable
- [ ] Log: Lưu consent & opt-out date
- [ ] Terms: Terms of service mention SMS policy

**Ví dụ consent text ở checkout:**
```
□ Tôi muốn nhận SMS khuyến mãi, sản phẩm mới, cập nhật đơn hàng từ [Brand].
(Có thể reply STOP để hủy)
```

## 5. SMS Providers Việt Nam

Có nhiều nhà cung cấp SMS gateway ở Việt Nam. Mỗi nhà có ưu điểm khác nhau.

### 5.1 Top SMS Providers VN

**1. eSMS (esms.vn)**
- Giá: 300-500 VND/tin (volume discount)
- Features: Brandname, scheduling, API, report
- Pros: Giá rẻ, support tốt, brand name clear
- Cons: Interface cũ, setup khó
- Best for: TMĐT, nhà bán lẻ
- Setup: 1-2 ngày (phê duyệt brand name)

**2. SpeedSMS (speedsms.vn)**
- Giá: 300-600 VND/tin
- Features: Brandname, API, automation, report
- Pros: Nhanh, support 24/7, brand approval nhanh
- Cons: Giá cao hơn, feature ít hơn
- Best for: TMĐT cần urgency (fast SMS)
- Setup: 1-3 ngày

**3. Vietguys (vietguys.vn)**
- Giá: 400-700 VND/tin
- Features: Brandname, Zalo API, CRM integrate
- Pros: Zalo integration (omnichannel), good for F&B
- Cons: Giá cao, smaller provider
- Best for: Restaurants, café, delivery
- Setup: 2-3 ngày

**4. 360Click SMS**
- Giá: 350-600 VND/tin
- Features: API, Automation, Brandname
- Pros: Powerful API, good for developers
- Cons: Giá vừa phải, support chậm
- Best for: TMĐT tech-savvy, integration heavy
- Setup: 2-3 ngày

**5. Brandname SMS (Vietnamobile, Viettel, MobiFone)**
- Giá: 1000-1500 VND/tin (gấp 2-3x)
- Features: Official brand name display
- Pros: Official, show "Official" badge
- Cons: Đắt, phải submit docs, approval chậm
- Best for: Brands lớn, cần trust (banking)
- Setup: 5-10 ngày (phê duyệt tài liệu)

### 5.2 Chọn SMS Provider phù hợp

**Decision matrix:**

| Tiêu chí | Budget nhỏ | TMĐT vừa | TMĐT lớn |
|----------|-----------|----------|----------|
| Provider | eSMS, SpeedSMS | SpeedSMS, Vietguys | Brandname SMS |
| Giá | 300-400 VND | 400-500 VND | 1000-1500 VND |
| Brandname | Yes | Yes | Official |
| API | Yes | Yes | Yes |
| Support | Email | 24/7 | Dedicated |
| Setup | 1-2 ngày | 1-2 ngày | 5-10 ngày |

**Chọn based on:**
1. **Budget:** Nhỏ → eSMS, lớn → Brandname
2. **Volume:** <10k/tháng → eSMS, >100k → Brandname
3. **Integration:** Cần API → SpeedSMS/360Click
4. **Speed:** Need fast → SpeedSMS
5. **Omnichannel:** SMS + Zalo → Vietguys

## 6. Brandname SMS vs Number SMS

### 6.1 Brandname SMS (Recommended)

**Định nghĩa:** SMS hiển thị tên brand (VD: "[BRAND]") thay vì số điện thoại.

**Ưu điểm:**
- Professional: Không giống scam/spam
- Trust: Customer tin tưởng
- Brand recall: Nhìn liên tục tên brand
- Compliance: Legal, tuân thủ quy định
- Open rate: +10-20% (vs number SMS)

**Nhược điểm:**
- Phải phê duyệt: 1-2 ngày (trễ)
- Giá cao: +50-100% vs number SMS
- Strict guidelines: Nội dung phải chính xác brand

**Setup Brandname SMS:**
```
1. Chọn provider (eSMS, SpeedSMS, etc)
2. Register account + thanh toán
3. Submit brand name + documents:
   - Giấy đăng ký kinh doanh
   - Logo brand
   - Mô tả sản phẩm/dịch vụ
4. Chờ phê duyệt (1-2 ngày)
5. Activate & gửi SMS
```

**Cost:** 400-600 VND/tin (ví dụ eSMS)

### 6.2 Number SMS (Shared/Dedicated)

**Định nghĩa:** SMS gửi từ số điện thoại (Shared: shared across brands, hoặc Dedicated: riêng)

**Ưu điểm:**
- Nhanh: Activate ngay (không phê duyệt)
- Rẻ: 200-300 VND/tin
- Flexible: Thay nội dung dễ dàng

**Nhược điểm:**
- Spam feel: Giống tin nhắn giả
- Low trust: Customer delete ngay
- Low open rate: -20-30%
- May be blocked: Spam filter
- Quay lại số khác: Risk khách block

**Risk:** Nếu content xấu, số bị ban → phải đổi số mới

**Best use case:** Transactional SMS (OTP, xác nhận), không phải marketing

## 7. Customer Segmentation & Targeting

Không nên gửi SMS chung cho tất cả. Segmentation giúp relevance cao, unsubscribe thấp.

### 7.1 Segmentation Strategy

**By purchase history (RFM):**

**R = Recency (gần đây)**
- Hot: Mua trong 7 ngày → Flash sale, new product
- Warm: Mua 8-30 ngày → Reminder, reorder
- Cold: Mua >30 ngày → Win-back, special offer

**F = Frequency (tần suất)**
- High: Mua 5+ lần → VIP offer, exclusive access
- Medium: Mua 2-4 lần → Regular promotion
- Low: Mua 1 lần → Incentive to buy again

**M = Monetary (giá trị)**
- High: Mua >5M → VIP exclusive, early access
- Medium: Mua 1-5M → Regular discount
- Low: Mua <1M → Extra incentive (20% off)

**Segment example:**
- High-value VIP: R=Hot, F=High, M=High → VIP 40% off
- Warm customers: R=Warm, F=Medium → 15% off reminder
- Cold customers: R=Cold, F=Low → Win-back 25% off

### 7.2 Behavioral Segmentation

**By behavior:**
- Cart abandoners: Giỏ rỗi → Reminder + incentive
- Browsers (not buyers): Xem nhiều, mua ít → Incentive + social proof
- Repeat buyers: Mua lần 2+ → Loyalty, VIP
- First-time buyers: Mua lần đầu → Onboarding, next purchase incentive

### 7.3 Demographic Segmentation

**By location:**
- HCM: Free ship HCM → More aggressive offer
- Hà Nội: Free ship HN → More aggressive offer
- Other: Charged ship → Less aggressive discount

**By age:**
- Gen Z (13-25): Trending, social, fun
- Gen Y (26-40): Value, quality, convenience
- Gen X (41-55): Quality, reliability, health
- Baby boomers (55+): Health, safety, community

**By product category interested:**
- Fashion segment: Fashion SMS
- Beauty segment: Beauty + skincare SMS
- Tech segment: Electronics SMS
- No buy yet: Onboarding, general offer

## 8. SMS Automation & Triggers

Automation = Trigger-based SMS (tự động gửi khi điều kiện thỏa).

### 8.1 Main Automation Workflows

**Workflow 1: Abandoned cart flow**
```
Trigger: Khách thêm vào giỏ nhưng không mua (24 giờ)
→ SMS 1: 1 giờ sau abandon (ngay lập tức)
   "Ban de trong gio hang [Product].
    Giam 10% code QUAYLAI: https://link"

→ SMS 2: 24 giờ sau (nếu chưa mua)
   Optional (không spam lại nếu chưa respons)
```

**Workflow 2: Post-purchase flow**
```
Trigger: Khách mua hàng thành công
→ SMS 1: Ngay (0-5 phút)
   "XAC NHAN DON HANG #ORD123456. Tong: 500K. Giao 2-3 ngay"

→ SMS 2: Sau 3 ngày
   "Don hang #ORD123456 dang giao. Track: [link]"

→ SMS 3: Sau 5 ngày (khi giao)
   "Don hang #ORD123456 da giao.
    Danh gia de nhan qua 50K: [link]"

→ SMS 4: Sau 14 ngày
   "Ban thich hang? Gioi thieu ban be, nhan 100K: [link]"

→ SMS 5: Sau 30 ngày
   "Hang vua ve! Giam 15% code QUAYLAI.
    Giao nhanh: [link]"
```

**Workflow 3: Welcome series (new subscriber)**
```
Trigger: Khách opt-in SMS (ở checkout hoặc form)
→ SMS 1: Ngay lập tức
   "Chao mung! Ban da dang ky nhan tin tu [Brand].
    Toi uu nhat: [link]"

→ SMS 2: Sau 1 giờ
   "Khach moi nhan 20% off don hang dau tien.
    Code: WELCOME20. Mua: [link]"

→ SMS 3: Sau 3 giờ
   "Khong co cai ban thich?
    Chat support: https://chat. Giup ban tim!"
```

**Workflow 4: Win-back series (inactive customers)**
```
Trigger: Khách không mua trong 60+ ngày
→ SMS 1:
   "Nhieu hang moi da den!
    Giam 25% cho khach than: [link]"

→ SMS 2: 7 ngày sau
   "Nhung khach cu goi ban!
    Giam 30% hom nay. Code: WELCOME30: [link]"
```

**Workflow 5: VIP tier series**
```
Trigger: Khách đạt VIP (mua >5M hoặc 10 lần)
→ SMS 1:
   "Chuc mung! Ban len VIP.
    Nhan 40% off + priority support: [link]"

→ SMS 2: Hang tuan
   "VIP exclusive: ...hang moi giam 50%"
```

### 8.2 Setting up automation

**Tools:**
- eSMS, SpeedSMS: Cấu hình workflow ở dashboard
- Zapier: Connect SMS provider + e-commerce platform
- Integrations: Shopify → SMS app, WooCommerce → SMS plugin

**Setup steps:**
```
1. Choose trigger (abandoned cart, purchase, etc)
2. Set delay (1 hour, 3 days, etc)
3. Create message template
4. Set audience (all, segment, etc)
5. Test (send to yourself)
6. Enable & monitor
```

**Best practices:**
- Test before launching (send to yourself)
- Start with 1 workflow (e.g., abandoned cart)
- Monitor unsubscribe rate (if >1%, too aggressive)
- A/B test messages (different copy, offer)
- Optimize based on conversion data

## 9. SMS + Email + Zalo Integration (Omnichannel)

Không nên chỉ dùng SMS. Kết hợp SMS + Email + Zalo hiệu quả hơn.

### 9.1 Channel Selection Matrix

**Khi nào dùng kênh nào:**

| Situation | SMS | Email | Zalo |
|-----------|-----|-------|------|
| Flash sale (2h) | ✓ | ✗ | ✓ |
| New product | ~ | ✓ | ✓ |
| Abandoned cart | ✓ | ~ | ✓ |
| Order update | ✓ | ~ | ✗ |
| Detailed content | ✗ | ✓ | ~ |
| Community | ✗ | ✗ | ✓ |
| Promotion | ✓ | ✓ | ✓ |
| Personal message | ~ | ✓ | ✓ |

**Explanation:**
- ✓ = Ideal channel
- ~ = Can use but not ideal
- ✗ = Not recommended

### 9.2 Omnichannel Sequence

**Campaign example: New product launch**

```
Day 0 (Teaser):
- SMS: "Hang moi se ra mat ngay mai"
- Email: Detailed teaser email with images
- Zalo: "Trai cua may tin?"

Day 1 (Launch):
- SMS: "HANG MOI RA MAT! Giam 40% link https://..."
- Email: Product detail, spec, review, discount code
- Zalo: Video unboxing, live demo

Day 2-3 (Reminder):
- SMS: "Hang vua con it. Giam con 1 ngay. https://..."
- Email: Customer testimonial, "others bought"
- Zalo: "Last chance" message

Day 4 (Last call):
- SMS: "Last 12h giam 40%. Con <50 hang. https://..."
- Email: Final reminder, urgency message
- Zalo: Countdown sticker

Day 5 (End):
- Email: "Sale ended" + related product rec
- Zalo: "Thanks for support" + next campaign teaser
```

### 9.3 Channel Integration Best Practices

**Rules:**
1. **Don't spam same message** - Vary content per channel
   - SMS: Short, urgent, direct link
   - Email: Long-form, detailed, storytelling
   - Zalo: Conversational, emoji, interactive

2. **Respect frequency** - Max 3 channels same day
   - Example: SMS + Email OK, SMS + Email + Zalo = too much

3. **Segment by preference** - Some prefer SMS, some email
   - Let customers choose (unsubscribe from channel, not brand)
   - Track preference, adapt

4. **Timing stagger** - Don't send all same time
   - SMS: 19:00 (immediate)
   - Email: 10:00 next day (for reading)
   - Zalo: 14:00 (lunch time)

5. **Attribution tracking** - Know which channel convert
   - UTM: ?utm_medium=sms vs utm_medium=email
   - Discount code: SMS10 vs EMAIL10 vs ZALO10
   - Measure ROI by channel

## 10. SMS Metrics & Analytics

### 10.1 Key Metrics

**Delivery metrics:**
- Delivery rate: % tin nhắn gửi thành công
  - Target: >99%
  - Nếu <95%, có vấn đề (check number quality)

- Bounce rate: % tin bị reject
  - Target: <1%
  - Nếu cao, có số không hợp lệ

**Engagement metrics:**
- Open rate: % người mở SMS (nhìn thấy)
  - Estimated: 95-98% (khó track chính xác)
  - Best case: SMS mở gần 100%

- Click rate: % người click link ở SMS
  - Target: >10%
  - Nếu <5%, message không compelling

- Reply rate: % người reply SMS
  - Target: 5-20% (for interactive SMS)
  - High reply = engaged audience

**Conversion metrics:**
- Conversion rate: % người mua sau click SMS
  - Target: 10-30%
  - Abandoned cart SMS: 20-30%
  - Promo SMS: 5-15%

- Cost per conversion (CPC)
  - Example: SMS cost 500 VND, conversion 10%
  - CPC = 500 / 10% = 5,000 VND per buyer
  - Target: <50k VND (for acceptable ROI)

- ROI: (Sales - SMS cost) / SMS cost
  - Target: >20x (at least)
  - Example: SMS cost 1M, sales 30M → ROI = 2900%

**Unsubscribe metrics:**
- Opt-out rate: % người reply "STOP"
  - Target: <0.5%
  - Nếu >1%, frequency/timing/content có issue

- Hard bounce: % số không hợp lệ
  - Target: <1%

### 10.2 Calculating ROI

**Formula:**
```
Revenue from SMS campaign = Sales attributed to SMS
Cost = (# SMS sent × price per SMS) + management cost
ROI = (Revenue - Cost) / Cost × 100%
```

**Example:**
```
Campaign: Flash sale SMS
SMS sent: 50,000
Price per SMS: 400 VND
Total SMS cost: 50,000 × 400 = 20M VND

Results:
Click rate: 15% = 7,500 clicks
Conversion rate: 20% = 1,500 buyers
Average order value: 500K
Total revenue: 1,500 × 500K = 750M VND

ROI = (750M - 20M) / 20M × 100% = 3,650%
```

### 10.3 Dashboard & Tracking

**Essential metrics to track:**
- Daily: # SMS sent, delivery rate, click rate
- Weekly: Conversion rate, ROI, unsubscribe rate
- Monthly: Trend analysis, compare campaigns

**Tools:**
- eSMS dashboard: Native analytics
- Google Analytics: Tag SMS links with UTM
- Spreadsheet: Manual tracking per campaign
- Integrations: Zapier → Google Sheets auto-log

**Example tracking spreadsheet:**
```
Campaign | Date | SMS Sent | Click | Click% | Sales | Sales$ | Cost$ | ROI
Flash50  | 4/19 | 50k     | 7.5k  | 15%   | 1.5k  | 750k  | 20k   | 3650%
SUMMER20 | 4/20 | 40k     | 4.2k  | 10.5% | 630   | 315k  | 16k   | 1869%
LOYALTY  | 4/21 | 10k     | 2.1k  | 21%   | 350   | 175k  | 4k    | 4275%
```

## 11. A/B Testing SMS

### 11.1 What to test

**1. Message copy (CTA):**
```
Version A: "Mua ngay: https://link"
Version B: "Chi con 2h, mua day: https://link"
Split: 50-50, measure click rate
Winner: Version B (higher urgency)
```

**2. Offer (discount amount):**
```
Version A: "Giam 10%"
Version B: "Giam 20%"
Measure: Click rate, conversion rate, revenue
Trade-off: Higher discount = more clicks but lower margin
```

**3. Timing (khi gửi):**
```
Version A: Gửi 19:00 (tối)
Version B: Gửi 12:00 (trưa)
Measure: Click rate over 24 hours
Context: Phụ thuộc loại sản phẩm, audience
```

**4. Length (câu ngắn vs dài):**
```
Version A: "Giam 50% ao somi. https://link"
Version B: "Giam 50% TAT CA ao somi, ao phong. Code: FLASH50. Chi 2h. https://link"
Measure: Click rate, cost per click
Observation: Longer SMS may have higher CTR (info complete)
```

**5. Emoji (dùng hay không):**
```
Version A: "Giam 50% https://link"
Version B: "🔥 Giam 50% 🔥 https://link"
Measure: Open rate (hard to measure), click rate
Note: Some numbers may block emoji, be careful
```

### 11.2 A/B test process

**Step 1: Choose variable to test**
- Pick one thing (not multiple)
- Example: Offer amount (10% vs 20%)

**Step 2: Create versions**
- Version A (control): Current best practice
- Version B (test): New hypothesis
- Make versions different but comparable

**Step 3: Split audience**
- Split: 50-50 or 70-30 (test smaller first)
- Randomize: Make sure random, not biased
- Size: Min 1,000 per variation (for statistical significance)

**Step 4: Measure results**
- Metric: Click rate or conversion rate
- Duration: 24-48 hours (enough data)
- Document: Save results

**Step 5: Implement winner**
- Use higher-performing version
- Document for future reference
- Do next test

### 11.3 Example A/B test

```
Campaign: Flash sale SMS
Hypothesis: "Shorter message with higher urgency gets more clicks"

Version A (Control):
"FLASH SALE! Giam 50% tat ca ao phong. Code: FLASH50. Chi con 2h. Mua: https://bit.ly/flash50"
(Length: 120 ký tự)

Version B (Test):
"GIAM 50% CHI 2H! Mua: https://bit.ly/flash50"
(Length: 45 ký tự)

Audience: 10,000 random followers
Split: 5,000 Version A, 5,000 Version B

Results:
Version A: 750 clicks (15% CTR)
Version B: 525 clicks (10.5% CTR)

Winner: Version A
Learning: Detailed message outperforms short message
(People need context for decision)

Next test: Test different discount % (40% vs 50%)
```

## 12. Cost Analysis & ROI Calculation

### 12.1 SMS Pricing Models

**Model 1: Pay-per-SMS**
- Cost: 300-600 VND/tin
- Volume discount: 1,000+ = cheaper
- Best for: Low-volume (< 50k/month)
- Calculation: 10,000 SMS × 400 VND = 4M VND

**Model 2: Monthly package**
- Package: 100,000 SMS/month = 25M VND
- Effective rate: 250 VND/SMS
- Commitment: Fixed monthly cost
- Best for: Medium-volume (50k-500k/month)

**Model 3: Prepaid credit**
- Buy: 1M VND credit
- Rate: 400 VND/SMS = 2,500 SMS
- Validity: 6-12 months
- Best for: Businesses adjusting usage

### 12.2 ROI Calculation Examples

**Example 1: Flash sale SMS**
```
Scenario: E-commerce bán thời trang

SMS sent: 100,000
Price per SMS: 400 VND
Total cost: 40M VND

Performance:
Open rate: 95%+ (estimate, not tracked)
Click rate: 15% = 15,000 clicks
Conversion rate: 20% = 3,000 buyers
Average order value: 500K VND
Total revenue: 1.5B VND

Profit: 1.5B - 40M = 1.46B VND
ROI: (1.46B / 40M) × 100% = 3,650%
```

**Example 2: Abandoned cart reminder**
```
Scenario: E-commerce, mid-size

SMS sent: 50,000 (people with abandoned carts)
Price per SMS: 400 VND
Total cost: 20M VND
Incentive (code): 15% off (cost: 2% margin loss)

Performance:
Click rate: 25% = 12,500 clicks (high for reminder)
Conversion rate: 30% = 3,750 buyers (high intent)
Average order value: 200K (lower tier customers)
Total revenue: 750M VND
Margin loss from discount: 750M × 2% = 15M VND

Net revenue: 750M - 15M = 735M VND
Profit: 735M - 20M = 715M VND
ROI: (715M / 20M) × 100% = 3,575%

Note: Margin loss is lower than gain → Profitable
```

**Example 3: Regular promotional SMS**
```
Scenario: Regular weekly promo to subscribers

SMS sent: 200,000 (all subscribers)
Price per SMS: 300 VND (volume discount)
Total cost: 60M VND/week

Performance:
Click rate: 8% = 16,000 clicks
Conversion rate: 10% = 1,600 buyers
Average order value: 300K
Total revenue: 480M VND
Margin: 30% = 144M VND (profit)

Weekly profit: 144M - 60M = 84M VND
Monthly profit: 84M × 4 = 336M VND

ROI: 400% (revenue-based) or 140% (margin-based)
```

### 12.3 Break-even analysis

**When is SMS profitable?**

Formula:
```
Break-even Click Rate = SMS Cost / (Conversion Rate × AOV × Margin%)
```

Example:
```
SMS cost: 40M VND (100k SMS @ 400 VND)
Conversion rate: 10%
AOV: 300K
Margin: 30%

Profit per conversion: 300K × 30% = 90K
Cost per conversion needed: 40M / ? = 90K max
Click rate needed: 40M / (0.1 × 300K × 0.3) = 44,000 clicks needed
For 100K SMS: 44,000 / 100,000 = 44% click rate needed

Actual expectation: 10-20% CTR is realistic
So break-even at 10% CTR: 10,000 clicks × 10% = 1,000 conversion
Revenue: 1,000 × 300K = 300M VND
Profit: 300M × 30% = 90M VND ✓ (Profitable)
```

---

