---
name: ops-bom-builder
description: |
  Xây dựng BOM (Bill of Materials) cho sản phẩm sản xuất — đa cấp (multi-level), kèm định mức tiêu hao, % phế phẩm. Dùng skill này khi người dùng yêu cầu: "tạo BOM", "Bill of Materials", "định mức nguyên vật liệu", "công thức sản phẩm", "BOM multi-level", "indented BOM", "BOM recipe", "danh mục nguyên liệu sản phẩm". Output là Excel BOM cây + JSON sẵn import ERP/MES.
---

# BOM Builder — Xây Dựng Bill of Materials

## Mục Tiêu
Tài liệu hoá đầy đủ "Cần gì để làm 1 sản phẩm", chuẩn cho tính giá thành, MRP, quản lý kho, ISO — cốt lõi vận hành sản xuất.

## Khi Nào Dùng
- Sản phẩm mới R&D xong, ra production
- Triển khai ERP/MES (cần master data BOM)
- Tính lại giá thành chuẩn (Standard Costing)
- Audit ISO 9001 yêu cầu định mức
- Đề xuất nội địa hoá (thay NCC, NVL)

## Bước 1: Cấu Trúc BOM Đa Cấp
```
[Level 0] Sản phẩm cuối: Ghế gỗ X
├── [Level 1] Khung gỗ
│   ├── [Level 2] Thanh ngang (gỗ thông) — 4 cái
│   ├── [Level 2] Thanh dọc (gỗ thông) — 4 cái
│   └── [Level 2] Đinh vít M6 — 16 cái
├── [Level 1] Mặt ngồi
│   ├── [Level 2] Tấm gỗ dán 18mm — 1 tấm
│   └── [Level 2] Vải bọc — 0.5m²
└── [Level 1] Phụ kiện
    ├── [Level 2] Tem hãng — 1 cái
    └── [Level 2] Hộp đóng gói — 1 cái
```

Mỗi item có:
- Part Number (mã NVL)
- Description
- UOM (đơn vị tính)
- Qty per parent (số lượng cho 1 parent)
- Scrap % (tỉ lệ phế phẩm dự kiến)
- Make/Buy (tự làm hay mua ngoài)
- NCC chính + NCC backup
- Lead time
- Standard cost

## Bước 2: Tính Định Mức + Phế Phẩm
**Qty thực tế cần** = Qty BOM × (1 + Scrap%)

Ví dụ:
- BOM cần 0.5m² vải, scrap 8% → cần 0.54 m²
- Standard cost = 0.54 × 80,000 = 43,200 VND/sp

Cộng hết để ra Total Material Cost cho 1 sản phẩm.

3 loại BOM thường dùng:
- **Engineering BOM** (E-BOM): từ R&D, đủ chi tiết kỹ thuật
- **Manufacturing BOM** (M-BOM): bản đã điều chỉnh cho sản xuất
- **Costing BOM**: chỉ chi phí, dùng cho tính giá

## Bước 3: BOM Explosion + Where-Used
**Explosion** = từ 1 đơn hàng 100 ghế → tính ra tổng NVL cần:
- 400 thanh ngang + 400 thanh dọc + 1,600 đinh + ...

**Where-Used** = NVL X được dùng ở những sản phẩm nào (ngược lại):
- Đinh vít M6 dùng ở: Ghế X, Bàn Y, Giường Z

Quan trọng khi:
- NCC báo hết hàng → biết sản phẩm nào ảnh hưởng
- NVL bị lỗi → recall đúng product

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: BOM cây với indent
- Google Drive MCP: Lưu drawing kỹ thuật cho mỗi part
- Notion MCP: Database part number search nhanh
- Slack MCP: Notify khi BOM được phê duyệt version mới
- WebSearch: Tra giá NVL realtime (gỗ, sắt, vải)
- WebFetch: Lấy COA/datasheet từ website NCC

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Push BOM lên Odoo ERP qua XML-RPC
import xmlrpc.client
URL = "https://erp.co.vn"
DB, USER, PWD = "main", "admin", "..."
common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common")
uid = common.authenticate(DB, USER, PWD, {})
models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")
# Create BOM
bom_id = models.execute_kw(DB, uid, PWD, "mrp.bom", "create",
    [{"product_tmpl_id": 123, "product_qty": 1,
      "bom_line_ids": [
          (0,0,{"product_id": 456, "product_qty": 4}),
          (0,0,{"product_id": 789, "product_qty": 16})
      ]}])
print("BOM created:", bom_id)
```

## Bước 5: Output Format
- `BOM_<SKU>.xlsx` — Excel có indent đa cấp + sheet costing
- `BOM_<SKU>.json` — JSON import ERP/MES
- `Where_Used_Matrix.xlsx` — ma trận NVL × Sản phẩm
- `BOM_Tree.mmd` — Mermaid diagram cây
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/BOM/`

## Checklist Trước Khi Giao
- [ ] Mọi part có Part Number duy nhất
- [ ] UOM đúng (mua m² nhưng dùng m²/m³)
- [ ] Scrap % có data lịch sử backup
- [ ] BOM version control (v1.0, v1.1)
- [ ] Có approval workflow trước release
- [ ] Sync với ERP/MES không lệch
