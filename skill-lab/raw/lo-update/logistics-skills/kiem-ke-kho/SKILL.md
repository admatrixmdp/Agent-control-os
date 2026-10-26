---
name: kiem-ke-kho
description: >
  Xây dựng quy trình kiểm kê kho định kỳ và đột xuất cho SME Việt Nam — bao gồm kế hoạch
  kiểm kê, phân công nhóm, biên bản kiểm kê, đối chiếu số liệu và xử lý chênh lệch.
  Dùng skill này khi người dùng cần: lập kế hoạch kiểm kê hàng hóa, tạo biên bản kiểm kê,
  xử lý chênh lệch tồn kho hoặc chuẩn bị kiểm kê cuối năm.
  Kích hoạt khi nhắc đến: "kiểm kê", "kiểm kê kho", "inventory count", "stock count",
  "biên bản kiểm kê", "kiểm kê cuối năm", "chênh lệch tồn kho", "xử lý thiếu hụt kho",
  "đối chiếu kho", "cycle count", "kiểm kê định kỳ", "physical inventory".
---

# Skill: Kiểm Kê Kho

Bạn là Warehouse Auditor chuyên tổ chức kiểm kê cho SME Việt Nam.
Mục tiêu là phát hiện chênh lệch tồn kho sớm, đảm bảo số liệu sổ sách khớp thực tế.

---

## A. KẾ HOẠCH KIỂM KÊ

```
KẾ HOẠCH KIỂM KÊ KHO [ĐỊNH KỲ/ĐỘT XUẤT]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Loại kiểm kê:
□ Kiểm kê toàn kho (cuối năm, cuối quý)
□ Cycle count theo nhóm (A hàng tháng, B hàng quý, C hàng năm)
□ Kiểm kê đột xuất khi nghi ngờ thất thoát
□ Kiểm kê trước/sau khi bàn giao thủ kho

PHÂN CÔNG:
□ Trưởng ban kiểm kê: ................. (Trưởng kho/Kế toán)
□ Nhóm đếm thực tế: .................. (Không phải thủ kho)
□ Nhóm đối chiếu sổ sách: ............. (Kế toán)
□ Giám sát: ........................... (BGĐ/Kiểm toán nội bộ)

THỜI GIAN & PHẠM VI:
Ngày kiểm kê: .../.../......  Thời gian: ...... đến ......
Kho/khu vực kiểm kê: ...........................................
Số lượng SKU dự kiến: ..........
Ngừng nhập xuất trong kiểm kê: □ Có □ Không (kiểm kê luân phiên)

CHUẨN BỊ TRƯỚC KIỂM KÊ:
□ In danh sách SKU và số lượng theo sổ sách (Blind count — không cho người đếm thấy)
□ Dán số thứ tự cho từng vị trí kho
□ Dọn dẹp, sắp xếp gọn gàng trước ngày kiểm kê
□ Hoàn thành nhập xuất trước giờ kiểm kê
□ Chuẩn bị thiết bị: máy quét mã vạch, bảng kẹp, bút
```

---

## B. BIÊN BẢN KIỂM KÊ

```
BIÊN BẢN KIỂM KÊ KHO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Số biên bản: KK-[NĂM][THÁNG]-[SỐ TT]
Ngày kiểm kê: .../.../......  Kho: ...................
Thời điểm chốt số liệu: ......  Người lập: ..............

Mã SP | Tên SP | ĐVT | SL theo sổ | SL thực tế | Chênh lệch | Ghi chú nguyên nhân
------|--------|-----|-----------|-----------|-----------|--------------------
      |        |     |           |           | +/−       |
      |        |     |           |           | +/−       |

TỔNG HỢP:
Tổng SKU kiểm kê: ......
SKU không chênh lệch: ...... (......%)
SKU chênh lệch dương (thừa): ...... SKU — Giá trị: ......đ
SKU chênh lệch âm (thiếu): ...... SKU — Giá trị: ......đ
Tỷ lệ chính xác tồn kho: ......%

XÁC NHẬN: Ban kiểm kê ký tên
Trưởng ban: ............... Thủ kho: ................
Kế toán: .................. Giám sát: ................
```

---

## C. XỬ LÝ CHÊNH LỆCH TỒN KHO

```
QUY TRÌNH XỬ LÝ CHÊNH LỆCH SAU KIỂM KÊ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Bước 1 — XÁC MINH LẠI:
□ Đếm lại lần 2 những SKU chênh lệch
□ Kiểm tra hàng chờ nhập/xuất chưa cập nhật
□ Kiểm tra hàng gửi đi sửa chữa, ký gửi

Bước 2 — XÁC ĐỊNH NGUYÊN NHÂN:
□ Lỗi nhập liệu (nhầm mã SKU, nhầm số lượng)
□ Nhập/xuất không lập phiếu
□ Hàng hỏng chưa ghi giảm
□ Thất thoát/mất cắp (cần điều tra)

Bước 3 — PHÂN QUYỀN XỬ LÝ:
□ Chênh lệch < 0.1% giá trị kho: Thủ kho điều chỉnh, kế toán xác nhận
□ Chênh lệch 0.1–1% giá trị kho: Trưởng bộ phận duyệt
□ Chênh lệch > 1% hoặc nghi ngờ thất thoát: BGĐ duyệt, có thể điều tra

Bước 4 — ĐIỀU CHỈNH SỔ SÁCH:
Hạch toán khi thiếu hàng (do hư hỏng):
Nợ TK 632 Giá vốn: ......đ
Có TK 156 Hàng hóa: ......đ

Bước 5 — PHÒNG NGỪA TÁI DIỄN:
□ Cải thiện quy trình nhập/xuất (không cho thiếu phiếu)
□ Lắp camera kho nếu nghi thất thoát
□ Cycle count thường xuyên hơn với mặt hàng giá trị cao
```

---

## Định dạng đầu ra

Tạo kế hoạch kiểm kê, biên bản kiểm kê hoặc hướng dẫn xử lý chênh lệch theo quy mô kho.
Kết hợp skill `xlsx` để tạo bảng kiểm kê tự động tính chênh lệch.
