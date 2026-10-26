---
name: ops-warehouse-layout
description: |
  Thiết kế layout kho hàng theo FIFO/FEFO + ABC analysis — tối ưu picking path, slot tốc độ cao gần cửa, giảm walking distance 30-50%. Dùng skill này khi người dùng yêu cầu: "thiết kế layout kho", "ABC analysis kho", "tối ưu kho hàng", "FIFO warehouse", "FEFO", "picking path", "slotting kho", "warehouse layout design". Output là sơ đồ kho SVG + Excel ABC + hướng dẫn slotting.
---

# Thiết Kế Layout Kho Theo FIFO + ABC

## Mục Tiêu
Giảm thời gian picking trung bình mỗi đơn 30-50%, đảm bảo FIFO/FEFO không xuất nhầm lô cũ, tận dụng không gian dọc — cốt lõi cho 3PL và kho TMĐT.

## Khi Nào Dùng
- Setup kho mới
- Kho hiện tại bị quá tải, picking chậm
- Sản phẩm có hạn sử dụng (FMCG, dược, F&B)
- Mua thêm kệ/MHE, cần plan slotting lại
- Audit 5S kho hàng tháng

## Bước 1: ABC Analysis SKU
Lấy data sales 3-6 tháng gần nhất:
- Class A: 20% SKU đầu, đóng góp 80% revenue → SLOT VÀNG (gần cửa, tầng dễ với)
- Class B: 30% SKU tiếp theo, 15% revenue → SLOT BẠC
- Class C: 50% SKU đuôi, 5% revenue → SLOT SAU (xa, tầng cao)

Công thức Pareto:
```
Sort SKU theo revenue desc → cumulative % → cắt ngưỡng 80/95/100
```

Bổ sung XYZ analysis (theo biến động):
- X: bán đều → có thể auto-replenish
- Y: theo mùa
- Z: bán bất thường → để ít tồn

## Bước 2: Vẽ Sơ Đồ Khu Vực Kho
Chia kho thành các zone:
- **Inbound** (nhận hàng): gần cửa nhập, có bãi tạm
- **Storage** (lưu trữ): chia A/B/C zone
- **Picking** (soạn hàng): kệ thấp, mật độ cao
- **Packing** (đóng gói): bàn + máy in tem
- **Outbound** (xuất): gần cửa xuất, lane theo đơn vị vận chuyển
- **Return/QC** (riêng biệt, không trộn với hàng good)

Quy tắc khoảng cách:
- Lối đi chính: 3m (xe nâng quay đầu)
- Lối phụ: 1.5m (xe đẩy)
- Chiều cao kệ: 5-tầng cho A, 7-tầng cho C

## Bước 3: Slotting Rules
- **FIFO**: lô nhập trước xuất trước → kệ flow-through (lùa từ sau, lấy phía trước)
- **FEFO**: lô hết hạn trước xuất trước → label màu theo tháng
- **Heavy at bottom**: hàng nặng tầng 1, nhẹ tầng cao
- **Fast at front**: A-item ngay đầu lối đi, < 2 bước chân
- **Pair items**: hàng bán kèm để gần nhau (giảm walking)
- **Hazardous separate**: hóa chất, dễ cháy zone riêng có MSDS

Path algorithm: S-shape hoặc Return path → check thời gian thực tế.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Đọc data SKU + sales lịch sử
- Google Drive MCP: Lưu sơ đồ kho SVG/PDF, share cho thủ kho
- Notion MCP: Database SKU có cột location code
- WebSearch: Tra kích thước kệ chuẩn ngành (Selectiv, Drive-in, Push-back)
- WebFetch: Báo giá MHE từ websosanh.vn, lazada B2B

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# ABC analysis từ KiotViet
import requests, pandas as pd
TOKEN = "..."
RETAILER = "yourshop"
r = requests.get(f"https://public.kiotapi.com/products",
    headers={"Authorization": f"Bearer {TOKEN}",
             "Retailer": RETAILER})
df = pd.DataFrame(r.json()["data"])
df = df.sort_values("revenue", ascending=False)
df["cum_pct"] = df["revenue"].cumsum() / df["revenue"].sum()
df["class"] = df["cum_pct"].apply(
    lambda x: "A" if x<=0.8 else "B" if x<=0.95 else "C")
df.to_excel("abc_analysis.xlsx", index=False)
```

## Bước 5: Output Format
- `warehouse_layout.svg` — sơ đồ tổng kho với zone màu
- `ABC_analysis.xlsx` — danh sách SKU phân loại + location đề xuất
- `slotting_map.xlsx` — map location code -> SKU
- `picking_path_demo.html` — animation S-shape path
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/Warehouse/`

## Checklist Trước Khi Giao
- [ ] ABC tính dựa trên data thật, không ước lượng
- [ ] FIFO/FEFO áp dụng đúng cho SKU có hạn dùng
- [ ] Lối đi đủ rộng cho MHE
- [ ] Khu hazardous tách riêng có quy định PCCC
- [ ] Location code có format chuẩn (Zone-Aisle-Bay-Level-Position)
- [ ] Có training thủ kho 1 buổi
