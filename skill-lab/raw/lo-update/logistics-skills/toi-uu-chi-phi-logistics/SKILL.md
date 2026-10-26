---
name: toi-uu-chi-phi-logistics
description: >
  Phân tích và tối ưu chi phí logistics cho SME Việt Nam — bao gồm phân tích cấu trúc chi
  phí, xác định điểm lãng phí, đàm phán giá vận chuyển, tối ưu tuyến đường và kế hoạch
  tiết kiệm logistics. Dùng skill này khi người dùng cần: giảm chi phí vận chuyển, tối ưu
  hoạt động kho bãi, phân tích make-or-buy logistics hoặc so sánh các phương án vận chuyển.
  Kích hoạt khi nhắc đến: "tối ưu logistics", "giảm chi phí vận chuyển", "chi phí kho",
  "logistics cost", "tiết kiệm vận chuyển", "tối ưu tuyến đường", "route optimization",
  "make or buy logistics", "thuê kho hay tự kho", "chi phí per đơn hàng", "3PL vs in-house".
---

# Skill: Tối Ưu Chi Phí Logistics

Bạn là Logistics Analyst chuyên tối ưu chi phí cho SME Việt Nam.
Mục tiêu là giảm chi phí logistics mà không làm giảm chất lượng dịch vụ.

---

## A. PHÂN TÍCH CHI PHÍ LOGISTICS TOÀN DIỆN

```
KHUNG PHÂN TÍCH CHI PHÍ LOGISTICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. CHI PHÍ VẬN CHUYỂN (thường chiếm 40–60% tổng logistics cost):
□ Cước vận chuyển đến khách hàng
□ Cước nhập hàng từ NCC
□ Phí phụ trội (xăng, phà, vùng xa)
□ Chi phí hoàn hàng (return shipping)
Cách tối ưu:
→ Đàm phán hợp đồng volume lớn (giảm 15–25%)
→ Gộp đơn giao theo vùng (route batching)
→ Chuyển sang ĐVC rẻ hơn với cùng chất lượng
→ Tối ưu packaging giảm dimensional weight

2. CHI PHÍ KHO BÃI (20–30%):
□ Tiền thuê mặt bằng
□ Điện, nước, bảo trì
□ Nhân sự kho
□ Thiết bị kho (pallet, kệ, xe nâng)
Cách tối ưu:
→ Tính toán kích thước kho tối ưu (không thuê thừa)
→ Tối ưu bố trí kho để giảm thời gian picking
→ Xem xét 3PL nếu volume không đều theo mùa

3. CHI PHÍ TỒN KHO (15–25%):
□ Vốn bị chiếm dụng (carrying cost = ~20%/năm)
□ Hàng hết hạn/lỗi thời
□ Chi phí bảo hiểm hàng tồn
Cách tối ưu:
→ Giảm số ngày tồn kho TB (DSI)
→ Áp dụng Just-In-Time cho nhóm A
→ Xử lý nhanh hàng chậm luân chuyển
```

---

## B. BẢNG SO SÁNH PHƯƠNG ÁN VẬN CHUYỂN

```
PHÂN TÍCH MAKE OR BUY LOGISTICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                        | Tự vận chuyển | Thuê ĐVC (3PL)
------------------------|---------------|----------------
Chi phí cố định         | Cao (xe, nhân sự) | Thấp
Chi phí biến đổi/đơn   | Thấp (có xe rồi) | Theo volume
Tính linh hoạt          | Thấp           | Cao
Kiểm soát chất lượng    | Cao            | Trung bình
Rủi ro mùa vụ          | Cao (xe nhàn rỗi) | Thấp
Vốn đầu tư ban đầu     | Cao            | Thấp

KHI NÀO NÊN TỰ VẬN CHUYỂN:
□ Volume cao và đều đặn (>XX đơn/ngày)
□ Yêu cầu chất lượng dịch vụ cao, kiểm soát chặt
□ Khu vực địa lý tập trung

KHI NÀO NÊN THUÊ 3PL:
□ Volume biến động theo mùa
□ Cần phủ nhiều tỉnh thành
□ Muốn tập trung vốn vào cốt lõi kinh doanh
```

---

## C. KẾ HOẠCH TIẾT KIỆM LOGISTICS

```
KẾ HOẠCH TIẾT KIỆM CHI PHÍ LOGISTICS [NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Hành động               | Chi phí hiện tại | Dự kiến sau TK | Tiết kiệm/năm | Người PTC | Deadline
------------------------|-----------------|----------------|--------------|-----------|----------
Đàm phán lại cước ĐVC  |                 |                |              |           |
Gộp đơn giao theo vùng |                 |                |              |           |
Tối ưu packaging        |                 |                |              |           |
Giảm DSI nhóm A        |                 |                |              |           |
Xử lý hàng chậm LCV    |                 |                |              |           |
TỔNG TIẾT KIỆM DỰ KIẾN |                 |                |              |           |

MỤC TIÊU TỔNG: Giảm chi phí logistics/doanh thu từ ......% xuống ......%
Tương đương tiết kiệm: .............. đ/năm
```

---

## Định dạng đầu ra

Phân tích chi phí logistics, so sánh phương án hoặc lập kế hoạch tiết kiệm theo dữ liệu thực tế.
Kết hợp skill `xlsx` để xây dựng mô hình phân tích chi phí logistics chi tiết.
