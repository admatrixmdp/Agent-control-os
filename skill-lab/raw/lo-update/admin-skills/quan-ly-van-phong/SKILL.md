---
name: quan-ly-van-phong
description: >
  Quản lý văn phòng phẩm, thiết bị, cơ sở vật chất và chi phí hành chính cho SME Việt Nam —
  bao gồm lập phiếu đề nghị mua văn phòng phẩm, theo dõi tồn kho, quản lý cấp phát và kiểm soát
  chi phí vận hành văn phòng. Dùng skill này khi người dùng cần: lập danh sách mua văn phòng phẩm,
  theo dõi tồn kho VPP, soạn phiếu cấp phát, lập ngân sách văn phòng, quản lý cơ sở vật chất
  hoặc kiểm soát chi phí hành chính định kỳ.
  Kích hoạt khi nhắc đến: "văn phòng phẩm", "VPP", "mua VPP", "tồn kho văn phòng",
  "cấp phát văn phòng phẩm", "quản lý văn phòng", "chi phí hành chính", "ngân sách văn phòng",
  "cơ sở vật chất", "facility management", "phiếu cấp phát".
---

# Skill: Quản Lý Văn Phòng & Cơ Sở Vật Chất

Bạn là Admin chuyên quản lý văn phòng cho SME Việt Nam.
Mục tiêu là đảm bảo văn phòng vận hành trơn tru, kiểm soát chi phí hành chính hiệu quả.

---

## A. DANH MỤC VĂN PHÒNG PHẨM CHUẨN

```
DANH MỤC VĂN PHÒNG PHẨM ĐỊNH KỲ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Đơn vị: .............. | Kỳ: Tháng ..../......
Người lập: .............. | Ngày: ..............

NHÓM 1 — VĂN PHÒNG PHẨM TIÊU HAO
┌────────────────────────┬──────┬──────┬────────┬──────────┬───────────┐
│ Tên hàng               │ ĐVT  │ Tồn  │ Cần    │ Đơn giá  │ Thành tiền│
├────────────────────────┼──────┼──────┼────────┼──────────┼───────────┤
│ Giấy in A4 (80gsm)     │ Ream │      │        │          │           │
│ Mực in (đen/màu)       │ Hộp  │      │        │          │           │
│ Bút bi (xanh/đen/đỏ)  │ Hộp  │      │        │          │           │
│ Bút highlight          │ Cái  │      │        │          │           │
│ Sổ tay A5/A4           │ Quyển│      │        │          │           │
│ Ghim/Kẹp tài liệu      │ Hộp  │      │        │          │           │
│ Băng keo trong/đôi mặt │ Cuộn │      │        │          │           │
│ Phong bì (nhỏ/lớn)     │ Xấp  │      │        │          │           │
│ Túi đựng hồ sơ         │ Cái  │      │        │          │           │
│ [Khác]                 │      │      │        │          │           │
├────────────────────────┴──────┴──────┴────────┴──────────┴───────────┤
│ TỔNG NHÓM 1:                                               ........... │
└───────────────────────────────────────────────────────────────────────┘

NHÓM 2 — THIẾT BỊ VÀ PHỤ KIỆN VĂN PHÒNG
┌────────────────────────┬──────┬──────┬────────┬──────────┬───────────┐
│ Tên hàng               │ ĐVT  │ Số lượng│ Đơn giá│ Thành tiền│ Ghi chú │
├────────────────────────┼──────┼──────┬─┼──────────┼───────────┤─────────┤
│ [Thiết bị cần mua]     │      │      │ │          │           │         │
└────────────────────────┴──────┴──────┴─┴──────────┴───────────┴─────────┘

TỔNG CỘNG: .............. VNĐ
Người lập đề nghị ký: .............. Quản lý duyệt ký: ..............
```

---

## B. PHIẾU CẤP PHÁT VĂN PHÒNG PHẨM

```
PHIẾU CẤP PHÁT VĂN PHÒNG PHẨM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Số phiếu: ............ Ngày: ..............
Phòng ban nhận: ..................... Người nhận: .....................
Lý do sử dụng: .................................................

STT | Tên hàng | ĐVT | Số lượng yêu cầu | Số lượng cấp | Ghi chú
----|----------|-----|-----------------|--------------|--------
 1  |          |     |                 |              |
 2  |          |     |                 |              |
 3  |          |     |                 |              |

Người nhận                  Thủ kho/Admin
(Ký, ghi rõ họ tên)        (Ký, ghi rõ họ tên)
```

---

## C. THEO DÕI TỒN KHO VĂN PHÒNG PHẨM

```
SỔ THEO DÕI TỒN KHO VĂN PHÒNG PHẨM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mã hàng | Tên hàng | ĐVT | Tồn đầu | Nhập | Xuất | Tồn cuối | Mức tối thiểu | Cần mua
--------|----------|-----|---------|------|------|----------|---------------|--------
        |          |     |         |      |      |          |               |

Lưu ý: Khi Tồn cuối < Mức tối thiểu → tự động đề xuất mua thêm
```

---

## D. NGÂN SÁCH VĂN PHÒNG THÁNG

```
KẾ HOẠCH CHI PHÍ HÀNH CHÍNH THÁNG [THÁNG/NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌──────────────────────────────┬─────────────┬────────────┬──────────┐
│ Khoản mục                    │ Ngân sách   │ Thực chi   │ Chênh lệch│
├──────────────────────────────┼─────────────┼────────────┼──────────┤
│ Văn phòng phẩm               │             │            │          │
│ Điện / Nước                  │             │            │          │
│ Internet / Điện thoại        │             │            │          │
│ Vệ sinh văn phòng            │             │            │          │
│ Sửa chữa / Bảo trì           │             │            │          │
│ Thuê mặt bằng                │             │            │          │
│ Chi phí khác                 │             │            │          │
├──────────────────────────────┼─────────────┼────────────┼──────────┤
│ TỔNG CHI PHÍ HC              │             │            │          │
└──────────────────────────────┴─────────────┴────────────┴──────────┘
```

---

## E. CHECKLIST QUẢN LÝ VĂN PHÒNG ĐỊNH KỲ

```
CHECKLIST HÀNH CHÍNH HÀNG THÁNG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ Kiểm kê tồn kho văn phòng phẩm
□ Lập đề nghị mua VPP tháng tiếp theo
□ Kiểm tra và thanh toán hóa đơn điện/nước/internet
□ Kiểm tra tình trạng thiết bị (máy in, điều hòa, máy tính)
□ Gia hạn bảo hiểm văn phòng (nếu sắp hết hạn)
□ Lập báo cáo chi phí HC tháng gửi BGĐ
□ Kiểm tra vệ sinh, an toàn PCCC
□ Cập nhật danh sách nhà cung cấp và hợp đồng dịch vụ
```

---

## Định dạng đầu ra

Tạo biểu mẫu, danh sách hoặc kế hoạch chi phí theo yêu cầu cụ thể.
Nếu cần file Excel theo dõi tồn kho, kết hợp skill `xlsx`.
