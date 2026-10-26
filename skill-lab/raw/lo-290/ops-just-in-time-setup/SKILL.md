---
name: ops-just-in-time-setup
description: |
  Setup hệ thống JIT/Lean — Kanban cards, Takt time, supermarket, heijunka, milkrun — cho sản xuất tiệm cận zero inventory. Dùng skill này khi người dùng yêu cầu: "setup JIT", "Just-in-Time", "Lean Manufacturing", "Kanban hệ thống pull", "Takt time setup", "supermarket Lean", "heijunka box", "milkrun setup". Output là Excel Kanban calc + sơ đồ pull system + checklist triển khai.
---

# Just-In-Time / Lean Setup

## Mục Tiêu
Chuyển từ sản xuất push (theo plan dài hạn → tồn kho lớn) sang pull (theo demand thực → tồn kho thấp), giảm tồn kho 50-80%, cycle time 30-60%.

## Khi Nào Dùng
- Tồn kho NVL/WIP quá cao chiếm vốn lưu động
- Cycle time dài, lead time khách dài
- Sản xuất theo lô lớn nhưng demand đa dạng
- Đối tác Tier-1 của Toyota/Honda/VinFast yêu cầu
- Sau khi đã có 5S + standard work

## Bước 1: Hiểu 4 Trụ JIT
1. **Takt Time** — nhịp khách hàng yêu cầu
2. **Continuous Flow** — sản phẩm chảy liên tục, không lô lớn
3. **Pull System** — chỉ làm khi có nhu cầu hạ nguồn
4. **Level Production (Heijunka)** — san bằng sản xuất theo mix + volume

Điều kiện tiên quyết:
- Quy trình ổn định, ít NG (< 1%)
- Setup time ngắn (SMED < 10 phút)
- NCC tin cậy (OTD > 98%)
- Đã có 5S + Visual Management

## Bước 2: Tính Số Kanban Cards
```
N = (D × LT × (1 + α)) / C
```
Trong đó:
- D = demand/đơn vị thời gian
- LT = lead time bổ sung (replenishment)
- α = safety factor (10-30%)
- C = container size (số sản phẩm/thùng)

Ví dụ:
- D = 100 sp/giờ, LT = 2 giờ, α = 0.2, C = 25 sp/thùng
- N = (100 × 2 × 1.2) / 25 = 9.6 → làm 10 cards

3 loại Kanban:
- **Production Kanban** (P-card): tín hiệu sản xuất
- **Withdrawal Kanban** (W-card): tín hiệu lấy hàng
- **Signal Kanban**: tín hiệu setup máy đợt mới

## Bước 3: Thiết Kế Supermarket + Milkrun
**Supermarket** = kho đệm có vị trí cố định cho mỗi part, có max-min level.

Quy tắc:
- 1 location = 1 SKU
- Max level = số kanban × container
- Min level = trigger reorder (1-2 container còn lại)
- FIFO chặt chẽ (lùa từ sau, lấy phía trước)

**Milkrun** = xe đẩy đi vòng theo route cố định, mỗi 30-60 phút:
- Tuyến A: kho NVL → line 1 → line 2 → kho
- Tuyến B: line 3 → packing → outbound
- Có biểu giờ chuẩn

**Heijunka Box** = lưới ô theo giờ × loại sản phẩm:
| 8h | 9h | 10h | 11h |
|---|---|---|---|
| A | B | A | C |
| B | A | C | A |

→ Mỗi giờ làm hỗn hợp sản phẩm, không lô lớn 1 sp.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Kanban calc + dashboard inventory
- Slack MCP: Cảnh báo Kanban thiếu (e-kanban)
- Notion MCP: Database part numbers + container size
- Google Drive MCP: Lưu sơ đồ supermarket layout
- WebSearch: Tham khảo Toyota Production System tài liệu chính thức
- WebFetch: Tải template Heijunka/Kanban từ leanenterprise.org

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# E-Kanban: tự sinh tín hiệu khi tồn xuống min
import requests
from datetime import datetime
parts = [
    {"sku":"A-001","stock":50,"min":40,"max":250,"container":25},
    {"sku":"B-002","stock":120,"min":100,"max":400,"container":50}
]
for p in parts:
    if p["stock"] <= p["min"]:
        cards_needed = (p["max"]-p["stock"]) // p["container"]
        requests.post("https://hooks.slack.com/...",
            json={"text":f":zap: KANBAN: SKU {p['sku']} cần SX {cards_needed} thùng"})
```

## Bước 5: Output Format
- `JIT_Setup_Plan.md` — roadmap 90 ngày triển khai
- `Kanban_Calculator.xlsx` — tính số card cho mọi SKU
- `Supermarket_Layout.svg` — sơ đồ kho đệm
- `Heijunka_Box_Template.xlsx` — lưới mix sản xuất theo giờ
- `Milkrun_Routes.md` — tuyến + giờ chuẩn
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/JIT/`

## Checklist Trước Khi Giao
- [ ] Đã chạy 5S + standard work 3 tháng trước
- [ ] NCC OTD đủ tin cậy (> 95%)
- [ ] SMED < 10 phút cho máy critical
- [ ] Số card có buffer 20% biến động
- [ ] Có training Lean cho toàn team
- [ ] KPI inventory turn đo trước/sau triển khai
