---
name: fin-inventory-valuation
description: |
  Định giá hàng tồn kho theo phương pháp FIFO / Bình quân gia quyền (Weighted Average) /
  Đích danh, tính dự phòng giảm giá hàng tồn kho. Trigger phrases: "định giá tồn kho",
  "FIFO inventory", "bình quân gia quyền", "weighted average inventory",
  "dự phòng giảm giá HTK", "inventory valuation", "giá xuất kho", "kiểm kê kho",
  "obsolete inventory", "NRV hàng tồn". Output là Excel tính giá xuất + báo cáo HTK
  cuối kỳ.
---

# Định Giá Hàng Tồn Kho FIFO / Bình Quân Gia Quyền

## Mục Tiêu
Tính chính xác giá xuất kho mỗi lần xuất → giá vốn hàng bán chính xác → P&L chính xác.
Đồng thời định giá HTK cuối kỳ theo Lower of Cost or NRV để tránh khai khống tài sản,
tuân thủ VAS 02.

## Khi Nào Dùng
- Hàng ngày khi có lệnh xuất kho (nếu chọn FIFO real-time)
- Cuối tháng tính giá xuất bình quân (nếu chọn WA cuối kỳ)
- Cuối năm kiểm kê thực tế, đánh giá NRV
- Trước kiểm toán xác nhận giá trị HTK

## Bước 1: Thu Thập Dữ Liệu Nhập Xuất
Mỗi SKU cần lịch sử:
- Tồn đầu kỳ: số lượng, đơn giá
- Phiếu nhập kho: ngày, SL, đơn giá, NCC (kèm chi phí mua: vận chuyển, thuế NK)
- Phiếu xuất kho: ngày, SL, mục đích (bán, sản xuất, mẫu)

**Lưu ý:** Giá nhập = giá hoá đơn + chi phí mua trực tiếp - chiết khấu

## Bước 2: Chọn Phương Pháp & Tính Toán

**FIFO (First In First Out):**
- Xuất theo lô nhập trước
- Tồn cuối = lô nhập sau cùng
- Phù hợp: thực phẩm, mỹ phẩm có HSD

**Bình quân gia quyền (cả kỳ):**
```
Đơn giá BQ = (Tồn ĐK × Giá ĐK + Tổng nhập × Giá nhập) / (SL tồn ĐK + Tổng SL nhập)
Giá xuất = SL xuất × Đơn giá BQ
```

**Bình quân di động (sau mỗi lần nhập):**
- Tính lại đơn giá BQ ngay sau mỗi phiếu nhập
- Phù hợp ERP real-time

**Đích danh:**
- Áp dụng cho hàng giá trị cao, theo lô riêng (xe, máy móc)

## Bước 3: Dự Phòng Giảm Giá HTK (NRV)
Cuối kỳ rà soát:
- **NRV** (Net Realizable Value) = Giá bán dự kiến - CP để bán
- Nếu NRV < Giá gốc → lập dự phòng = (Giá gốc - NRV) × SL

**Hàng cần check:**
- Hàng tồn kho lâu (>180 ngày không bán)
- Hàng lỗi, hỏng, hết HSD
- Hàng đã giảm giá thị trường (so spot price)
- Hàng theo mùa đã qua mùa

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Pull phiếu nhập xuất từ sheet kho
- Google Drive MCP: Lưu biên bản kiểm kê có chữ ký + ảnh
- WebSearch: Tra giá thị trường spot cho NRV check (đặc biệt nguyên vật liệu)
- WebFetch: Tra giá đối thủ trên Shopee/Lazada để dự phòng

**Fallback bằng API:**
```python
# Pull nhập-xuất từ MISA Mshopkeeper / KiotViet API
import requests
r = requests.get(
    "https://public.kiotapi.com/inventories",
    headers={"Retailer": SHOP, "Authorization": f"Bearer {TOKEN}"},
    params={"from": "2026-05-01", "to": "2026-05-31"}
)
inventory_moves = r.json()["data"]
# Tính FIFO bằng deque
from collections import deque
lots = deque()  # mỗi lot: (qty, unit_cost)
for move in sorted(inventory_moves, key=lambda x: x["date"]):
    if move["type"] == "IN":
        lots.append((move["qty"], move["unit_cost"]))
    else:  # OUT
        remaining = move["qty"]
        cost = 0
        while remaining > 0 and lots:
            lot_qty, lot_price = lots[0]
            take = min(lot_qty, remaining)
            cost += take * lot_price
            remaining -= take
            if take == lot_qty: lots.popleft()
            else: lots[0] = (lot_qty - take, lot_price)
        move["cogs"] = cost
```

## Bước 5: Output Format
1. **Excel định giá** (`inventory_valuation_T05_2026.xlsx`): Sheet "Movement" lịch sử N-X, "Cost_calc" tính giá theo phương pháp chọn, "Ending" tồn cuối kỳ, "Provision" dự phòng NRV.
2. **PDF báo cáo HTK** (`inventory_report_T05.pdf`): Mẫu chính thức trình KTT.
3. **HTML dashboard** (`inventory_dashboard.html`): Bar chart top 20 SKU theo giá trị, scatter aging vs value, donut tồn theo nhóm SKU.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/inventory/`

## Checklist Trước Khi Giao
- [ ] Phương pháp áp dụng nhất quán với năm trước (nếu đổi phải có thuyết minh)
- [ ] Tổng giá trị HTK khớp TK 152, 153, 155, 156
- [ ] Đã kiểm tra NRV cho hàng tồn >180 ngày
- [ ] Có biên bản kiểm kê thực tế cuối kỳ
- [ ] Dự phòng giảm giá đã hạch toán TK 229
- [ ] Backup file tính theo từng kỳ
