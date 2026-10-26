---
name: xu-ly-hang-huy-hang-loi
description: >
  Xây dựng quy trình xử lý hàng hủy, hàng lỗi và hàng hoàn trả về kho cho SME Việt Nam —
  bao gồm phân loại hàng hoàn, kiểm tra tái nhập kho, hủy hàng hết hạn/không đạt chất lượng
  và ghi nhận kế toán. Dùng skill này khi người dùng cần: xử lý hàng khách trả về, phân loại
  hàng lỗi, lập biên bản hủy hàng hoặc xây dựng quy trình reverse logistics.
  Kích hoạt khi nhắc đến: "hàng hoàn", "hàng trả về", "reverse logistics", "hủy hàng",
  "hàng lỗi", "hàng hết hạn", "xử lý hoàn hàng", "biên bản hủy hàng", "hàng không đạt",
  "phân loại hàng hư", "thanh lý hàng", "scrap hàng hóa", "hàng đổi trả từ KH".
---

# Skill: Xử Lý Hàng Hủy & Hàng Lỗi

Bạn là Warehouse/QC Manager chuyên xử lý hàng không đạt cho SME Việt Nam.
Mục tiêu là phân loại đúng, xử lý nhanh, ghi nhận chính xác để kiểm soát tổn thất.

---

## A. QUY TRÌNH XỬ LÝ HÀNG HOÀN TRẢ TỪ KHÁCH HÀNG

```
QUY TRÌNH TIẾP NHẬN HÀNG HOÀN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Bước 1 — TIẾP NHẬN:
□ Nhận hàng hoàn từ ĐVC kèm phiếu giao hàng/vận đơn hoàn
□ Đếm số kiện, ký xác nhận với ĐVC
□ Lập Phiếu Tiếp Nhận Hàng Hoàn (xem Mục B)

Bước 2 — KIỂM TRA & PHÂN LOẠI:
□ Mở kiện hàng, kiểm tra tình trạng
□ Đối chiếu với thông tin đơn hàng gốc
□ Phân loại vào 4 nhóm:
   A — Nguyên vẹn, tái bán được ngay
   B — Cần vệ sinh/tân trang nhẹ
   C — Hỏng do vận chuyển (claim ĐVC)
   D — Hỏng do KH sử dụng/lỗi NCC → Ghi nhận, xử lý riêng

Bước 3 — XỬ LÝ THEO PHÂN LOẠI:
□ Nhóm A: Nhập lại kho thương phẩm
□ Nhóm B: Chuyển sang khu vực xử lý, tân trang rồi nhập lại
□ Nhóm C: Lập hồ sơ khiếu nại với ĐVC
□ Nhóm D: Lập biên bản, báo NCC hoặc trình BGĐ duyệt hủy

Bước 4 — CẬP NHẬT HỆ THỐNG:
□ Cập nhật tồn kho theo kết quả phân loại
□ Kết nối với bộ phận kế toán để xử lý bút toán
□ Gửi báo cáo hàng hoàn hàng tuần cho quản lý
```

---

## B. PHIẾU TIẾP NHẬN HÀNG HOÀN

```
PHIẾU TIẾP NHẬN HÀNG HOÀN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Số phiếu: HH-[NĂM][THÁNG]-[SỐ TT]
Ngày tiếp nhận: .../.../......
Mã đơn hàng gốc: ............  Mã khiếu nại/đổi trả: ............
Lý do hoàn: □ KH đổi ý  □ Hàng lỗi NCC  □ Giao sai  □ Hỏng vận chuyển

STT | Mã SP | Tên SP | SL hoàn | Tình trạng | Phân loại | Xử lý đề xuất
----|-------|--------|---------|-----------|-----------|---------------
 1  |       |        |         |           | □A □B □C □D |
 2  |       |        |         |           | □A □B □C □D |

KẾT QUẢ KIỂM TRA TỔNG HỢP:
□ Nhóm A (tái bán): ...... sản phẩm
□ Nhóm B (tân trang): ...... sản phẩm
□ Nhóm C (claim ĐVC): ...... sản phẩm | Giá trị: ......... đ
□ Nhóm D (hỏng/hủy): ...... sản phẩm | Giá trị: ......... đ

Người tiếp nhận: .............. Thủ kho xác nhận: .................
```

---

## C. BIÊN BẢN HỦY HÀNG

```
BIÊN BẢN HỦY HÀNG HÓA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Số biên bản: BH-[NĂM][THÁNG]-[SỐ TT]
Ngày lập: .../.../......  Địa điểm: .................

HỘI ĐỒNG HỦY HÀNG:
□ Đại diện BGĐ: ........................
□ Trưởng kho: ............................
□ Kế toán: ...............................
□ QC/Kiểm định: ..........................

DANH SÁCH HÀNG HỦY:
STT | Mã SP | Tên SP | Số lô | HSD | ĐVT | SL | Đơn giá | Thành tiền | Lý do hủy
----|-------|--------|-------|-----|-----|----|---------|-----------|-----------
 1  |       |        |       |     |     |    |         |           |
 2  |       |        |       |     |     |    |         |           |

TỔNG GIÁ TRỊ HÀNG HỦY: ......................... đ

PHƯƠNG THỨC HỦY:
□ Tiêu hủy tại chỗ (đốt/nghiền/chôn lấp)
□ Bán phế liệu, thanh lý dưới giá
□ Trả lại nhà cung cấp theo bảo hành

Hội đồng xác nhận đã chứng kiến hủy hàng: ký tên đầy đủ

HẠCH TOÁN KẾ TOÁN:
Nợ TK 632 (Giá vốn)/TK 1388 (Phải thu NCC bảo hành): ........ đ
Có TK 156 (Hàng hóa): ........ đ
```

---

## Định dạng đầu ra

Tạo phiếu tiếp nhận hàng hoàn, biên bản hủy hàng hoặc quy trình reverse logistics theo đặc thù ngành.
Kết hợp skill `xlsx` để theo dõi hàng hoàn/hàng lỗi và tính giá trị tổn thất.
