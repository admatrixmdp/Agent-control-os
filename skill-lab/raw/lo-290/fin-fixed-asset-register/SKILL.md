---
name: fin-fixed-asset-register
description: |
  Quản lý sổ Tài Sản Cố Định (TSCĐ) - theo dõi nguyên giá, khấu hao tích luỹ, giá trị còn lại,
  lập bảng khấu hao tháng. Trigger phrases: "sổ TSCĐ", "tài sản cố định", "tính khấu hao",
  "depreciation schedule", "fixed asset register", "khấu hao đường thẳng", "thanh lý TSCĐ",
  "kiểm kê TSCĐ", "FA register", "bảng khấu hao". Output là Excel sổ TSCĐ + bảng khấu hao
  hàng tháng.
---

# Sổ Tài Sản Cố Định + Tính Khấu Hao

## Mục Tiêu
Quản lý chặt đời sống tài sản từ ngày mua → sử dụng → thanh lý. Tự động tính khấu hao
hàng tháng đẩy vào sổ cái, tránh sai sót thủ công và đảm bảo tuân thủ TT 45/2013/TT-BTC.

## Khi Nào Dùng
- Mỗi tháng tính khấu hao đưa vào hạch toán
- Khi mua mới TSCĐ cần đăng ký
- Khi thanh lý/nhượng bán cần xoá sổ
- Kiểm kê TSCĐ cuối năm
- Trước kiểm toán xác nhận giá trị còn lại

## Bước 1: Khởi Tạo / Update Sổ TSCĐ
Mỗi tài sản cần các trường:
- Mã TS (FA-2026-001), tên, mô tả
- Phân nhóm: Nhà cửa, MMTB, Phương tiện, Văn phòng, Vô hình (phần mềm, license)
- Ngày bắt đầu sử dụng, nguyên giá
- Thời gian sử dụng (theo khung TT 45)
- Phương pháp khấu hao: Đường thẳng / Số dư giảm dần / Sản lượng
- Phòng ban sử dụng, người quản lý, vị trí
- Tài khoản kế toán (211, 213, 214)

## Bước 2: Tính Khấu Hao Hàng Tháng
**Đường thẳng (phổ biến nhất):**
```
KH tháng = Nguyên giá / (Số năm × 12)
```

Lưu ý:
- TS bắt đầu sử dụng giữa tháng → tính từ tháng kế tiếp
- Khi giá trị còn lại = 0, dừng khấu hao nhưng vẫn theo dõi đến khi thanh lý
- TSCĐ ngừng sử dụng tạm thời (sửa chữa) vẫn khấu hao

**Bảng khấu hao tháng** gồm cột:
| Mã TS | Tên | Nguyên giá | KH tháng | KH luỹ kế | GT còn lại | Phòng ban | TK Nợ | TK Có |

## Bước 3: Theo Dõi Biến Động & Kiểm Kê
**Biến động trong kỳ:**
- Mua mới (Nợ 211 / Có 112, 331)
- Thanh lý/nhượng bán (xoá nguyên giá, KH luỹ kế, ghi nhận lỗ/lãi)
- Điều chuyển nội bộ giữa phòng ban
- Đánh giá lại (theo NĐ)

**Kiểm kê:**
- Lập biên bản kiểm kê thực tế
- Đối chiếu với sổ → phát hiện thừa/thiếu
- Lập biên bản xử lý

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Sổ TSCĐ sống, share view cho từng quản lý phòng ban
- Google Drive MCP: Lưu ảnh tài sản + hợp đồng mua, biên bản kiểm kê
- Gmail MCP: Gửi quản lý phòng ban xác nhận kiểm kê
- WebSearch: Tra TT 45/2013/TT-BTC khung khấu hao cập nhật

**Fallback bằng API:**
```python
# Đẩy bút toán khấu hao tháng vào MISA/FAST qua API
import requests
journal = {
    "voucher_date": "2026-05-31",
    "description": "Trích khấu hao TSCĐ T05/2026",
    "entries": [
        {"account": "6424", "department": dept,
         "debit": amount_kh, "credit": 0}
        for dept, amount_kh in depreciation_by_dept.items()
    ] + [{"account": "214", "debit": 0,
          "credit": sum(depreciation_by_dept.values())}]
}
requests.post(
    "https://api.misa.vn/sme/v1/journal-entries",
    json=journal, headers={"Authorization": f"Bearer {TOKEN}"}
)
```

## Bước 5: Output Format
1. **Excel sổ TSCĐ** (`FA_register_2026.xlsx`): Sheet "Master" full danh sách, "Monthly_Depreciation" theo tháng, "Movements" (mua-bán-điều chuyển), "Inventory_Check" biên bản kiểm kê.
2. **PDF bảng khấu hao** (`depreciation_T05_2026.pdf`): Mẫu chuẩn để in lưu hồ sơ.
3. **HTML dashboard** (`fa_dashboard.html`): Pie chart giá trị còn lại theo nhóm, bar chart nguyên giá theo phòng ban, table TS sắp hết khấu hao.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/fa/`

## Checklist Trước Khi Giao
- [ ] Tổng KH tháng khớp số dư TK 214
- [ ] Tất cả TS có ảnh chụp lưu Drive
- [ ] Khung khấu hao tuân thủ TT 45
- [ ] Đã đối chiếu kiểm kê thực tế ≥ 1 lần/năm
- [ ] Hồ sơ thanh lý có biên bản, hoá đơn đầy đủ
- [ ] Backup sổ TSCĐ định kỳ hàng tháng
