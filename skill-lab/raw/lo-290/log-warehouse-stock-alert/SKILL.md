---
name: log-warehouse-stock-alert
description: |
  Cảnh báo tồn kho thấp / cao tự động — tính Reorder Point (ROP), Safety Stock, Economic Order Quantity (EOQ) và phát hiện hàng tồn ứ đọng cho doanh nghiệp Việt Nam dùng KiotViet / Sapo / Misa / Excel. Kích hoạt khi người dùng nói: "cảnh báo tồn kho", "stock alert", "reorder point", "tính safety stock", "tồn kho thấp", "tồn kho ứ đọng", "dead stock", "EOQ", "inventory alert", "low stock notification", "tối ưu tồn kho". Output là Excel inventory dashboard + PDF báo cáo tồn + auto-script gửi alert qua email/Telegram.
---

# Cảnh Báo Tồn Kho Thấp/Cao + Tối Ưu Reorder

## Mục Tiêu
Giúp DN sản xuất / TMĐT Việt Nam tránh 2 thái cực: (1) hết hàng mất bán (stockout 5-15% doanh thu), (2) ứ đọng vốn (dead stock chiếm 20-30% vốn lưu động). Tự động hoá cảnh báo qua KiotViet / Sapo / Misa API.

## Khi Nào Dùng
- Đầu tháng / đầu tuần: kiểm tra ROP toàn SKU
- Mùa cao điểm (Tết, 11/11, 12/12): tăng safety stock
- Khi launch SKU mới: thiết lập baseline 60 ngày
- Khi sale-off / clearance: detect dead stock
- Audit kho định kỳ: phát hiện sai lệch sổ vs thực tế

## Bước 1: Tính 4 Chỉ Số Cốt Lõi
- **Safety Stock (SS)** = Z × σ_LT × √(Lead Time) — Z = 1.65 cho service level 95%, 2.33 cho 99%
- **Reorder Point (ROP)** = (Avg Daily Demand × Lead Time) + Safety Stock
- **EOQ** = √(2 × D × S / H) — D = nhu cầu năm, S = chi phí mỗi lần đặt, H = chi phí lưu kho/đv/năm
- **Inventory Turnover** = COGS / Avg Inventory (lý tưởng: TMĐT >12, sản xuất >6)

Phân loại ABC:
- A: 20% SKU = 80% doanh thu → quản lý chặt, daily check
- B: 30% SKU = 15% doanh thu → weekly
- C: 50% SKU = 5% doanh thu → monthly

## Bước 2: Định Nghĩa Quy Tắc Cảnh Báo
- **LOW STOCK**: stock ≤ ROP → tạo PR/PO ngay
- **CRITICAL**: stock ≤ Safety Stock → escalate Manager
- **OVERSTOCK**: stock > 3 × Avg Monthly Sales → cảnh báo BI/Marketing
- **DEAD STOCK**: không xuất ≥90 ngày + tồn >0 → khuyến mãi clearance
- **NEGATIVE STOCK**: stock < 0 → lỗi sổ sách, audit ngay
- **EXPIRY ALERT**: với FMCG/dược/thực phẩm — cảnh báo trước hạn 30/60/90 ngày

## Bước 3: Pipeline Cảnh Báo Tự Động
1. Cron job 06:00 hàng ngày
2. Pull data từ KiotViet/Sapo/Misa API (hoặc Excel đẩy lên Drive)
3. Tính ROP/SS theo SKU
4. Match với rule engine
5. Gửi alert qua:
   - Email cho QL Kho + Mua hàng (LOW/CRITICAL)
   - Telegram bot cho Mgr (CRITICAL ngay)
   - Slack cho team Marketing (OVERSTOCK > 30 ngày)
6. Log vào Sheets để theo dõi response

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: master inventory dashboard
- Google Drive MCP: lưu báo cáo tồn + lịch sử
- Gmail MCP: gửi alert email theo cấp độ
- Notion MCP: lưu SOP xử lý từng cảnh báo
- WebFetch: tra giá nhập NCC cập nhật khi tính EOQ
- KiotViet / Sapo / Misa MCP (hoặc API): pull tồn real-time

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tính ROP + EOQ + gửi alert qua KiotViet API
import requests
import numpy as np
from datetime import datetime, timedelta

def get_kiotviet_inventory(retailer, token):
    url = "https://public.kiotapi.com/products"
    headers = {"Retailer": retailer, "Authorization": f"Bearer {token}"}
    r = requests.get(url, headers=headers, params={"includeInventory": True, "pageSize": 100})
    return r.json()["data"]

def calc_rop(sku, daily_demand_history, lead_time_days, service_level=0.95):
    avg = np.mean(daily_demand_history)
    std = np.std(daily_demand_history)
    z = 1.65 if service_level == 0.95 else 2.33
    safety_stock = z * std * np.sqrt(lead_time_days)
    rop = avg * lead_time_days + safety_stock
    return {"sku": sku, "avg_demand": avg, "safety_stock": safety_stock, "rop": rop}

def calc_eoq(annual_demand, order_cost, holding_cost_per_unit):
    return np.sqrt(2 * annual_demand * order_cost / holding_cost_per_unit)

def send_alert(sku, current_stock, rop, level):
    # Telegram bot
    msg = f"[{level}] SKU {sku['name']} tồn {current_stock} ≤ ROP {rop:.0f}. Đặt {sku['eoq']:.0f} đơn vị."
    requests.post(
        f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
        json={"chat_id": TG_CHAT_ID, "text": msg, "parse_mode": "Markdown"}
    )

# Daily job
for product in get_kiotviet_inventory(RETAILER, TOKEN):
    rop_info = calc_rop(product["code"], get_sales_30d(product["id"]), product["lead_time"])
    if product["onHand"] <= rop_info["rop"]:
        send_alert(product, product["onHand"], rop_info["rop"], "LOW_STOCK")
```

## Bước 5: Output Format
- File `inventory_dashboard.xlsx`: 5 sheet (Master / ABC / Alerts / EOQ / Dead Stock)
- File `inventory_report_<yyyymm>.pdf`: 6-8 trang cho CEO/COO
  - Trang 1: KPI tổng (Stockout %, Turnover, Dead stock value)
  - Trang 2: Top 20 SKU sắp hết
  - Trang 3: Top 20 SKU ứ đọng (vốn chôn)
  - Trang 4: Phân loại ABC + đề xuất chính sách
  - Trang 5: Lịch sử ROP/EOQ
  - Trang 6: Đề xuất clearance / khuyến mãi
- File `alerts_log.csv`: lưu mọi alert đã gửi để audit
- Script `inventory_cron.py`: cron job hàng ngày
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/inventory/`

## Checklist Trước Khi Giao
- [ ] Đã tính ROP/SS/EOQ cho toàn bộ SKU active
- [ ] Đã phân loại ABC + tần suất kiểm tra phù hợp
- [ ] Có ≥5 quy tắc cảnh báo (LOW, CRITICAL, OVERSTOCK, DEAD, NEGATIVE)
- [ ] Pipeline cron chạy hàng ngày tự động
- [ ] Alert gửi đúng người đúng kênh (email/Telegram/Slack)
- [ ] Có dashboard cho CEO + log audit cho compliance
- [ ] Đã tích hợp KiotViet/Sapo/Misa nếu DN dùng
- [ ] Có chính sách xử lý Dead Stock (clearance, bundle, write-off)
