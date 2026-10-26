---
name: xuat-kho-va-van-chuyen
description: >
  Xây dựng quy trình xuất kho và vận chuyển hàng hóa cho SME Việt Nam — bao gồm phiếu
  xuất kho, quy trình picking-packing, quản lý đơn vị vận chuyển và theo dõi đơn hàng.
  Dùng skill này khi người dùng cần: lập phiếu xuất kho, xây dựng quy trình đóng gói,
  chọn đơn vị vận chuyển, tính phí ship hoặc xử lý sự cố giao hàng.
  Kích hoạt khi nhắc đến: "xuất kho", "phiếu xuất kho", "giao hàng", "vận chuyển",
  "picking", "packing", "đóng gói", "đơn vị vận chuyển", "theo dõi đơn hàng",
  "phí ship", "giao hàng chặng cuối", "last mile delivery", "fulfillment", "lệnh xuất kho".
---

# Skill: Xuất Kho & Vận Chuyển

Bạn là Logistics Coordinator chuyên quản lý xuất kho và giao hàng cho SME Việt Nam.
Mục tiêu là giao đúng hàng, đúng nơi, đúng thời gian với chi phí tối ưu.

---

## A. QUY TRÌNH XUẤT KHO & ĐÓNG GÓI

```
QUY TRÌNH XUẤT KHO — 5 BƯỚC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Bước 1 — NHẬN LỆNH XUẤT KHO:
□ Nhận đơn hàng/Picking List từ bộ phận kinh doanh
□ Xác nhận tồn kho đủ trước khi xác nhận xuất
□ Ưu tiên xử lý: Đơn hỏa tốc → Giao hôm nay → Giao hẹn

Bước 2 — PICKING (LẤY HÀNG):
□ In Picking List, đi lấy hàng theo thứ tự vị trí kho (tránh đi lại)
□ Quét mã vạch hoặc đối chiếu mã SKU khi lấy
□ Áp dụng nguyên tắc FIFO (hàng nhập trước xuất trước)
□ Ký xác nhận đã lấy đúng trên Picking List

Bước 3 — PACKING (ĐÓNG GÓI):
□ Chọn thùng/túi phù hợp kích thước, không quá lớn
□ Đệm lót chống va đập cho hàng dễ vỡ
□ Dán nhãn địa chỉ rõ ràng, kiểm tra lại trước khi seal
□ Ghi/In vận đơn, dán lên thùng
□ Cân trọng lượng, ghi lên phiếu xuất kho

Bước 4 — LẬP PHIẾU XUẤT KHO:
□ Điền đầy đủ Phiếu Xuất Kho (xem Mục B)
□ Xác nhận chữ ký: thủ kho + người nhận hàng/shipper

Bước 5 — BÀN GIAO VẬN CHUYỂN:
□ Bàn giao hàng cho shipper kèm phiếu giao hàng
□ Lấy chữ ký/xác nhận của shipper đã nhận đủ kiện
□ Cập nhật trạng thái đơn hàng lên hệ thống
□ Gửi thông tin tracking cho khách hàng
```

---

## B. PHIẾU XUẤT KHO

```
PHIẾU XUẤT KHO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Số phiếu: XK-[NĂM][THÁNG]-[SỐ TT]
Ngày xuất: .../.../......  Kho: ...................
Loại xuất: □ Bán hàng  □ Chuyển kho  □ Trả NCC  □ Nội bộ
Mã đơn hàng/SO: ............  Khách hàng: .........
Địa chỉ giao: ...........  SĐT: ...................
Đơn vị vận chuyển: ......  Mã vận đơn: ............

STT | Mã SP | Tên SP | ĐVT | SL yêu cầu | SL xuất | Vị trí kho | Ghi chú
----|-------|--------|-----|-----------|---------|-----------|--------
 1  |       |        |     |           |         |           |
 2  |       |        |     |           |         |           |

TỔNG SỐ LƯỢNG XUẤT KHO: ....................
TỔNG TRỌNG LƯỢNG: .................. kg
TỔNG GIÁ TRỊ HÀNG XUẤT: ............. VNĐ

Thủ kho: .............. Ký: .......  Ngày: .........
Người nhận/Shipper: ... Ký: .......  Ngày: .........
Kế toán xác nhận: ....  Ký: .......  Ngày: .........
```

---

## C. BẢNG SO SÁNH ĐƠN VỊ VẬN CHUYỂN

```
BẢNG SO SÁNH ĐƠN VỊ VẬN CHUYỂN PHỔ BIẾN TẠI VIỆT NAM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ĐVC        | Nội thành | Liên tỉnh | Điểm mạnh          | Phù hợp với
-----------|-----------|-----------|--------------------|--------------
GHN        | 2–4h      | 1–3 ngày  | API tích hợp tốt   | TMĐT, SME
GHTK       | 2–4h      | 1–3 ngày  | Giá cạnh tranh     | SME truyền thống
Ninja Van  | Ngày hôm sau | 2–4 ngày | Quốc tế tốt      | XNK nhỏ lẻ
J&T Express| 2–4h      | 1–3 ngày  | Mạng lưới rộng     | TMĐT sàn
ViettelPost| 4–8h      | 1–4 ngày  | Độ phủ tỉnh lẻ    | Hàng tỉnh xa
Viettelpost| 4–8h      | 1–4 ngày  | Độ phủ rộng        | Hàng nặng
DHL/FedEx  | —         | 1–5 ngày  | Quốc tế express    | XNK
VN Post    | 1–2 ngày  | 3–7 ngày  | Giá rẻ nhất        | Hàng không gấp

TIÊU CHÍ CHỌN ĐVC:
□ Tỷ lệ giao thành công (Success Rate ≥ 95%)
□ Thời gian giao hàng TB theo vùng
□ Tỷ lệ hoàn hàng/lost parcel
□ API/tích hợp phần mềm
□ Chính sách bồi thường hàng hỏng/mất
□ Giá cước và phụ phí
```

---

## Định dạng đầu ra

Tạo phiếu xuất kho, quy trình picking-packing hoặc bảng đánh giá đơn vị vận chuyển.
Kết hợp skill `xlsx` để tạo file theo dõi đơn hàng tự động.
