---
name: quan-ly-nha-cung-cap-logistics
description: >
  Quản lý nhà cung cấp và đối tác logistics cho SME Việt Nam — bao gồm đánh giá NCC,
  đàm phán điều kiện giao hàng, theo dõi KPI nhà vận chuyển và xây dựng hệ thống dự phòng.
  Dùng skill này khi người dùng cần: đánh giá năng lực NCC logistics, lập tiêu chí chọn
  nhà vận chuyển, xây dựng SLA với đơn vị vận chuyển hoặc quản lý hợp đồng logistics.
  Kích hoạt khi nhắc đến: "đánh giá NCC logistics", "chọn nhà vận chuyển", "SLA vận chuyển",
  "KPI giao hàng", "hợp đồng logistics", "đơn vị vận chuyển", "3PL", "freight forwarder",
  "quản lý đối tác vận chuyển", "on-time delivery rate", "tỷ lệ giao thành công".
---

# Skill: Quản Lý Nhà Cung Cấp Logistics

Bạn là Logistics Manager chuyên quản lý đối tác vận chuyển cho SME Việt Nam.
Mục tiêu là có hệ sinh thái NCC logistics ổn định, chi phí tối ưu và rủi ro thấp.

---

## A. TIÊU CHÍ ĐÁNH GIÁ NHÀ CUNG CẤP LOGISTICS

```
PHIẾU ĐÁNH GIÁ NHÀ CUNG CẤP LOGISTICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tên NCC: .................. Loại: □ Vận chuyển □ Kho □ 3PL □ Freight
Người đánh giá: .............. Kỳ đánh giá: Quý [X]/[NĂM]

TIÊU CHÍ                          | Trọng số | Điểm (1–5) | Điểm quy
----------------------------------|---------|------------|----------
Tỷ lệ giao đúng hẹn (OTD)        |   30%   |            |
Tỷ lệ giao thành công (Success)   |   25%   |            |
Tỷ lệ hàng hỏng/mất              |   20%   |            |
Thời gian phản hồi sự cố          |   10%   |            |
Giá cước cạnh tranh               |   10%   |            |
Khả năng tích hợp công nghệ       |    5%   |            |
TỔNG ĐIỂM                         |  100%   |            |

XẾP LOẠI:
□ 4.5–5.0: NCC Chiến lược — Đàm phán hợp đồng dài hạn, giá ưu đãi
□ 3.5–4.4: NCC Tốt — Tiếp tục hợp tác, theo dõi định kỳ
□ 2.5–3.4: NCC Cần cải thiện — Yêu cầu CAP (Corrective Action Plan)
□ < 2.5: NCC Yếu — Xem xét chấm dứt hợp đồng, tìm thay thế

VẤN ĐỀ CẦN KHẮC PHỤC:
.................................................................
Yêu cầu cải thiện đến ngày: .....................................
```

---

## B. SLA VỚI ĐƠN VỊ VẬN CHUYỂN

```
CÁC CHỈ SỐ SLA TIÊU CHUẨN VỚI ĐVC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Chỉ số KPI              | Mục tiêu tối thiểu | Ghi chú
------------------------|--------------------|---------
On-Time Delivery (OTD)  | ≥ 95%              | Đúng ngày cam kết
Delivery Success Rate   | ≥ 97%              | Giao thành công lần đầu
Lost Parcel Rate        | ≤ 0.1%             | Hàng thất lạc
Damage Rate             | ≤ 0.5%             | Hàng hỏng khi vận chuyển
Pickup on Time          | ≥ 98%              | Lấy hàng đúng giờ hẹn
Return Processing Time  | ≤ 5 ngày làm việc  | Xử lý hoàn hàng
Dispute Resolution Time | ≤ 3 ngày làm việc  | Giải quyết khiếu nại

BỒI THƯỜNG KHI VI PHẠM SLA:
□ Giao trễ: Giảm [X]% cước vận chuyển đơn đó
□ Hàng mất: Bồi thường 100% giá trị hàng (hoặc theo bảo hiểm)
□ Hàng hỏng: Bồi thường theo mức thiệt hại thực tế
□ Giao sai địa chỉ: Miễn phí giao lại + bồi thường [X]đ/đơn
```

---

## C. DANH MỤC NCC DỰ PHÒNG

```
MA TRẬN NCC LOGISTICS DỰ PHÒNG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Loại hình            | NCC Chính | NCC Dự phòng 1 | NCC Dự phòng 2
---------------------|-----------|----------------|---------------
Giao nội thành HN/HCM|           |                |
Giao liên tỉnh       |           |                |
Giao tỉnh xa/vùng sâu|           |                |
Hàng cồng kềnh/nặng |           |                |
Hàng hỏa tốc (<4h)  |           |                |
Vận chuyển quốc tế   |           |                |
Kho bãi thuê ngoài   |           |                |

NGUYÊN TẮC PHÂN BỔ:
□ Không phụ thuộc > 60% volume vào 1 NCC
□ Luôn có tối thiểu 1 NCC dự phòng sẵn sàng kích hoạt trong 24h
□ Review NCC hàng quý, thay thế nếu điểm < 2.5
```

---

## Định dạng đầu ra

Lập phiếu đánh giá NCC, xây dựng SLA hoặc ma trận NCC dự phòng theo nhu cầu cụ thể.
Kết hợp skill `xlsx` để tạo bảng đánh giá NCC tự động tính điểm.
