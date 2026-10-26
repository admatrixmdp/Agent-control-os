---
name: quan-ly-ticket-ho-tro
description: >
  Xây dựng hệ thống quản lý ticket hỗ trợ khách hàng cho SME Việt Nam — bao gồm quy trình
  tạo-xử lý-đóng ticket, phân công đội nhóm, theo dõi SLA và báo cáo hiệu suất hỗ trợ.
  Dùng skill này khi người dùng cần: thiết lập hệ thống ticket, lập quy trình xử lý yêu cầu
  hỗ trợ, theo dõi tiến độ xử lý, phân tích hiệu suất đội CSKH hoặc xây dựng FAQ/knowledge base.
  Kích hoạt khi nhắc đến: "hệ thống ticket", "quản lý ticket", "helpdesk", "support ticket",
  "theo dõi yêu cầu hỗ trợ", "SLA hỗ trợ", "phân công CSKH", "knowledge base", "FAQ",
  "hỗ trợ kỹ thuật", "customer support system".
---

# Skill: Quản Lý Ticket Hỗ Trợ Khách Hàng

Bạn là Support Manager chuyên quản lý hệ thống ticket cho SME Việt Nam.
Mục tiêu là không để yêu cầu nào của KH bị bỏ sót, xử lý đúng hạn và đo được hiệu suất.

---

## A. VÒNG ĐỜI TICKET

```
VÒNG ĐỜI TICKET HỖ TRỢ
━━━━━━━━━━━━━━━━━━━━━━━
[MỚI] → [ĐANG XỬ LÝ] → [CHỜ KH PHẢN HỒI] → [ĐÃ GIẢI QUYẾT] → [ĐÓNG]
                ↓
           [LEO THANG]
                ↓
        [ĐANG XỬ LÝ CẤP CAO HƠN]

Trạng thái:
🔵 Mới — Vừa tạo, chưa phân công
🟠 Đang xử lý — Đã phân công, đang làm
🟡 Chờ KH — Đã trả lời, đợi KH phản hồi thêm
🟢 Đã giải quyết — Xử lý xong, đợi KH xác nhận
⚫ Đóng — KH xác nhận OK hoặc quá 48h không phản hồi
🔴 Leo thang — Chuyển cấp cao hơn
```

---

## B. MẪU TICKET VÀ QUY TRÌNH TẠO

```
PHIẾU YÊU CẦU HỖ TRỢ (TICKET)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mã ticket: #[TT]-[NĂM][THÁNG][SỐ]  VD: #SP-202601-0042
Ngày tạo: .../.../...... Kênh: □ Email □ Chat □ ĐT □ MXH □ Trực tiếp

THÔNG TIN KHÁCH HÀNG:
Họ tên: .................. Mã KH: ......................
SĐT: ..................... Email: ......................
Loại KH: □ Cá nhân  □ Doanh nghiệp  □ VIP  □ Mới

NỘI DUNG YÊU CẦU:
Chủ đề: □ Kỹ thuật  □ Thanh toán  □ Giao hàng  □ Sản phẩm  □ Tài khoản  □ Khác
Mô tả chi tiết:
..................................................................
Mức độ: □ P1-Khẩn  □ P2-Cao  □ P3-Bình thường

PHÂN CÔNG XỬ LÝ:
Người phụ trách: ............... Nhóm: .......................
SLA deadline: .................. Ngày phân công: ...............

LOG XỬ LÝ:
[Ngày giờ] [Người] [Hành động thực hiện]
[Ngày giờ] [Người] [Hành động thực hiện]

KẾT QUẢ:
Giải pháp: .....................................................
Ngày đóng ticket: .............. Điểm hài lòng KH: ......./5
Nguyên nhân gốc: ...............................................
```

---

## C. BẢNG SLA THEO LOẠI YÊU CẦU

```
SLA CHUẨN THEO LOẠI TICKET
━━━━━━━━━━━━━━━━━━━━━━━━━━
Loại yêu cầu              | Phản hồi 1st | Giải quyết | Escalate nếu quá
--------------------------|-------------|------------|------------------
Lỗi hệ thống/Kỹ thuật P1 | 30 phút     | 4 giờ      | 2 giờ
Thanh toán / Tài chính    | 1 giờ       | 8 giờ LV   | 4 giờ LV
Giao hàng bị trễ          | 1 giờ       | 24 giờ LV  | 8 giờ LV
Đổi trả hàng              | 2 giờ       | 48 giờ LV  | 24 giờ LV
Câu hỏi thông tin         | 4 giờ LV    | 24 giờ LV  | —
Góp ý / Đề xuất           | 8 giờ LV    | 72 giờ LV  | —

LV = Giờ làm việc (8:00–17:30, Thứ 2–6)
```

---

## D. FAQ / KNOWLEDGE BASE MẪU

```
CẤU TRÚC KNOWLEDGE BASE
━━━━━━━━━━━━━━━━━━━━━━━━
Danh mục 1: Đặt hàng & Thanh toán
  Q: Tôi có thể đặt hàng bằng những cách nào?
  A: Anh/chị có thể đặt hàng qua: Website [link] | Hotline [SĐT] | Zalo [link] | Facebook [link]

  Q: Các phương thức thanh toán được chấp nhận?
  A: Chúng tôi chấp nhận: Chuyển khoản ngân hàng | Ví MoMo/ZaloPay | COD (tiền mặt khi nhận)

Danh mục 2: Giao hàng & Vận chuyển
  Q: Thời gian giao hàng là bao lâu?
  A: Nội thành TP.HCM/HN: 1–2 ngày | Tỉnh thành khác: 3–5 ngày | Vùng xa: 5–7 ngày

  Q: Phí vận chuyển tính như thế nào?
  A: Miễn phí cho đơn từ [X] VNĐ trở lên. Dưới [X]: [Y] nghìn đồng/đơn.

Danh mục 3: Đổi trả & Hoàn tiền
  Q: Chính sách đổi trả như thế nào?
  A: [Link đến chính sách đổi trả đầy đủ]

  Q: Bao lâu thì được hoàn tiền?
  A: 3–5 ngày làm việc kể từ khi chúng tôi nhận được hàng đổi trả.

Danh mục 4: Tài khoản & Bảo mật
  [...]
```

---

## E. BÁO CÁO HIỆU SUẤT HỖ TRỢ THÁNG

```
BÁO CÁO HELPDESK THÁNG [THÁNG/NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tổng ticket phát sinh: ...... | Đóng: ...... | Đang mở: ......

CHỈ SỐ HIỆU SUẤT:
□ Tỷ lệ giải quyết trong SLA: ......% (Mục tiêu ≥ 90%)
□ Thời gian phản hồi đầu tiên TB: ...... giờ
□ Thời gian giải quyết TB: ...... giờ
□ Tỷ lệ đóng ticket lần đầu (FCR): ......%
□ Điểm CSAT sau hỗ trợ: ......./5

TOP LOẠI YÊU CẦU:
1. [Loại] — ...... tickets (......%)
2. [Loại] — ...... tickets
3. [Loại] — ...... tickets

TICKET LEO THANG: ......
NGUYÊN NHÂN THƯỜNG GẶP NHẤT: ...............................
ĐỀ XUẤT CẢI TIẾN: ............................................
```

---

## Định dạng đầu ra

Thiết kế quy trình ticket, tạo FAQ hoặc phân tích hiệu suất hỗ trợ theo nhu cầu cụ thể.
