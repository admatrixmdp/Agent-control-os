---
name: phan-tich-du-lieu-san-pham
description: >
  Phân tích dữ liệu sản phẩm và hiệu suất R&D cho SME Việt Nam — bao gồm phân tích dữ
  liệu bán hàng sản phẩm, A/B testing, phân tích phản hồi KH, đo lường product-market fit
  và báo cáo KPI R&D. Dùng skill này khi người dùng cần: phân tích hiệu suất sản phẩm,
  thiết kế A/B test, đo product-market fit, phân tích retention, tổng hợp feedback KH
  hoặc lập báo cáo KPI phát triển sản phẩm.
  Kích hoạt khi nhắc đến: "phân tích sản phẩm", "product analytics", "A/B test", "thử
  nghiệm A/B", "product-market fit", "PMF", "retention analysis", "cohort analysis",
  "funnel analysis", "drop-off", "KPI R&D", "metrics sản phẩm", "feature adoption",
  "data-driven product", "phân tích hiệu suất SP".
---

# Skill: Phân Tích Dữ Liệu Sản Phẩm

Bạn là Product Analyst cho SME Việt Nam.
Mục tiêu là ra quyết định phát triển sản phẩm dựa trên dữ liệu thực — không dựa trên giả định.

---

## A. KPI SẢN PHẨM THEN CHỐT

```
BỘ KPI SẢN PHẨM TOÀN DIỆN
━━━━━━━━━━━━━━━━━━━━━━━━━━━

ACQUISITION (Thu hút KH):
□ New users/customers per month
□ Customer Acquisition Cost (CAC)
□ Channel attribution (kênh nào đưa KH đến)

ACTIVATION (Kích hoạt KH):
□ Activation Rate: % KH hoàn thành hành động đầu tiên quan trọng
□ Time to First Value: Thời gian đến lần đầu KH nhận giá trị
□ Onboarding completion rate

RETENTION (Giữ chân KH):
□ D7/D14/D30 Retention Rate (sản phẩm số)
□ Monthly Repeat Purchase Rate (sản phẩm vật lý)
□ Churn Rate: % KH rời đi mỗi tháng
□ Customer Lifetime Value (CLV/LTV)

REVENUE:
□ MRR/ARR (Monthly/Annual Recurring Revenue)
□ Average Order Value (AOV)
□ Revenue per Feature
□ Gross Margin per Product

REFERRAL:
□ NPS (Net Promoter Score)
□ Referral Rate: % KH giới thiệu người mới
□ Viral Coefficient (K-factor)

NORTH STAR METRIC:
Mỗi sản phẩm nên có 1 "North Star" — metric phản ánh giá trị cốt lõi:
□ Facebook: Daily Active Users
□ Uber: Trips completed per week
□ Airbnb: Nights booked
→ Của bạn: "........................................"
```

---

## B. A/B TESTING

```
QUY TRÌNH A/B TEST
━━━━━━━━━━━━━━━━━━━

BƯỚC 1 — XÁC ĐỊNH GIẢ THUYẾT:
"Chúng tôi tin rằng [thay đổi này] sẽ dẫn đến [kết quả] vì [lý do]"
Ví dụ: "Đổi màu nút CTA từ xanh → đỏ sẽ tăng CTR vì màu đỏ tạo urgency"

BƯỚC 2 — THIẾT KẾ TEST:
□ Nhóm A (Control): Phiên bản hiện tại
□ Nhóm B (Variant): Phiên bản thay đổi
□ Chỉ thay đổi 1 yếu tố mỗi lần
□ Chia traffic ngẫu nhiên 50/50

BƯỚC 3 — TÍNH SAMPLE SIZE:
Cần đủ mẫu để có ý nghĩa thống kê (p < 0.05):
□ Tỷ lệ chuyển đổi hiện tại: .......%
□ Cải thiện tối thiểu mong đợi: .......%
□ Sử dụng calculator: stats.idolblog.com hoặc Evan Miller AB Test Calculator

BƯỚC 4 — CHẠY VÀ ĐO LƯỜNG:
□ Chạy đủ thời gian (tối thiểu 1–2 tuần để tránh hiệu ứng ngày trong tuần)
□ Không dừng sớm khi thấy kết quả tích cực — p-hacking
□ Đo Primary metric + Secondary metrics

BƯỚC 5 — ĐÁNH GIÁ:
□ p-value < 0.05: Kết quả có ý nghĩa thống kê
□ Tác động thực tế đủ lớn để triển khai không? (Practical significance)
□ Triển khai variant thắng hoặc học bài và test tiếp

BẢNG THEO DÕI A/B TEST:
Test ID | Tên test | Giả thuyết | Metric | Control | Variant | p-value | Kết quả
--------|----------|-----------|--------|---------|---------|---------|--------
```

---

## C. PHÂN TÍCH PRODUCT-MARKET FIT

```
ĐO LƯỜNG PRODUCT-MARKET FIT (PMF)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHƯƠNG PHÁP SEAN ELLIS (Khảo sát):
Câu hỏi: "Bạn cảm thấy thế nào nếu không thể dùng [sản phẩm] nữa?"
□ Rất thất vọng
□ Thất vọng (nhưng không sao)
□ Không thất vọng (có thể thay thế)

PMF đạt được: ≥ 40% trả lời "Rất thất vọng"
Kết quả: ≥ 40% → Scale; 25–40% → Cải thiện; < 25% → Pivot

PHƯƠNG PHÁP RETENTION CURVE:
□ Plot % retention vs thời gian (tuần/tháng)
□ PMF đạt được: Đường retention ngang bằng (không về 0)
□ Ví dụ: Nếu D90 retention = 20% ổn định → Có PMF cho 20% user
□ Chưa PMF: Đường về gần 0% sau vài tháng

CÁC DẤU HIỆU PMF ĐANG ĐẾN:
□ KH tự quảng bá sản phẩm mà không được yêu cầu
□ Bạn không đủ hàng để đáp ứng đơn hàng tự nhiên
□ Phóng viên, blogger tự viết về sản phẩm
□ NPS ≥ 50
□ Retention curve phẳng ở mức > 20%
□ CAC giảm dần, CLV tăng dần
```

---

## Định dạng đầu ra

Xây dựng bộ KPI sản phẩm, thiết kế A/B test, đo PMF hoặc phân tích retention theo sản phẩm/thị trường cụ thể.
