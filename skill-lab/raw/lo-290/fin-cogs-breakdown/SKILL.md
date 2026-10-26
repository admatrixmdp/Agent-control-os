---
name: fin-cogs-breakdown
description: |
  Tách giá vốn hàng bán (COGS) chi tiết theo từng SKU, dự án, kênh bán, KH - giúp tìm
  SKU/khách hàng âm biên cần xử lý. Trigger phrases: "tách COGS theo SKU", "COGS breakdown",
  "giá vốn theo sản phẩm", "profitability by SKU", "biên LN từng dự án",
  "customer profitability", "channel profitability", "phân tích biên lợi nhuận chi tiết",
  "ABC costing", "true margin". Output là Excel COGS detail + HTML dashboard
  profitability.
---

# Tách COGS Chi Tiết Theo SKU / Dự Án / Kênh

## Mục Tiêu
Hiểu chính xác "ai làm ra tiền cho mình, ai làm mất tiền" ở cấp độ chi tiết. Nhiều DN
nhìn P&L tổng thấy lãi nhưng thực tế 30% SKU lỗ kéo lại 70% còn lại. Skill này phơi bày
sự thật để CEO ra quyết định cut/grow đúng.

## Khi Nào Dùng
- Cuối quý/năm review portfolio sản phẩm
- Trước khi quyết định rationalize SKU (cắt SKU yếu)
- Đàm phán lại với KH B2B chiếm tỷ trọng lớn nhưng biên mỏng
- Đánh giá hiệu quả kênh bán (so Shopee vs Lazada vs Website own)
- Khi giá NVL biến động mạnh ảnh hưởng cấu trúc biên

## Bước 1: Define COGS Components Theo Cấu Trúc
**Direct COGS** (gắn được trực tiếp SKU):
- Nguyên vật liệu (theo BOM)
- Nhân công trực tiếp (theo định mức + actual)
- Bao bì
- Chi phí mua vào (đối với hàng thương mại)
- Vận chuyển NCC về kho

**Indirect COGS - cần phân bổ:**
- Khấu hao máy móc sản xuất
- Lương quản đốc, công nhân gián tiếp
- Điện, nước, gas sản xuất
- Bảo trì máy
- Khấu hao nhà xưởng

**Allocated to Channel/Customer:**
- Phí sàn (Shopee, Lazada theo % revenue kênh)
- Phí thanh toán
- Phí vận chuyển hỗ trợ
- Hoa hồng sales theo % revenue khách
- Marketing CPA phân bổ
- Chi phí phục vụ KH (customer service time)

## Bước 2: Allocation Methodology - ABC Costing
**Activity Based Costing:**
1. Identify activities (Cắt, May, KCS, Đóng gói, Bán hàng)
2. Identify cost driver cho mỗi activity (giờ máy, giờ công, # đơn hàng)
3. Calculate rate (cost / driver)
4. Apply to SKU/customer dựa trên consumption thực tế

**Ví dụ:**
- Total MOH SX = 2 tỷ
- Total giờ máy = 100,000 → rate = 20,000đ/giờ
- SKU A cần 0.5 giờ máy → MOH/SKU A = 10,000đ

**ABC tốt hơn allocation theo % revenue** vì:
- 1 KH order 100 đơn nhỏ tiêu thụ resource khác 1 KH order 1 đơn lớn
- 1 SKU phức tạp cần nhiều công đoạn khác SKU đơn giản

## Bước 3: Phân Tích Profitability Multi-Dimensional
**By SKU:**
| SKU | Revenue | COGS | GM | GM% | Volume | Status |
|-----|---------|------|----|----|--------|--------|
| A001 | 1.2B | 480M | 720M | 60% | 5,000 | ⭐ Star |
| A002 | 800M | 720M | 80M | 10% | 3,000 | ⚠ Marginal |
| A003 | 200M | 250M | -50M | -25% | 800 | ✗ Cut |

**By Customer:**
- 80-20 rule check: 20% KH chiếm bao nhiêu % LN?
- KH lớn nhưng biên thấp: đàm phán hay drop?
- KH nhỏ biên cao: invest grow

**By Channel:**
- Website own: high margin, scale chậm
- Shopee: medium margin, scale nhanh
- Distributor: low margin, volume cao

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Pull sales by SKU/customer, COGS standard, allocate
- Google Drive MCP: Lưu báo cáo phân tích cho từng kỳ
- Gmail MCP: Gửi sales manager list KH "cần đàm phán lại"
- WebSearch: Benchmark margin ngành để biết SKU "10%" có thấp không

**Fallback bằng API:**
```python
# Pull data đa nguồn và tính profitability per SKU
import pandas as pd
import requests

# Sales từ Shopee + Lazada
shopee = requests.get("https://partner.shopee.com/api/v2/order/list",
                     params={"time_from": "2026-05-01", "time_to": "2026-05-31"},
                     headers={"Authorization": SHP_TOKEN}).json()
lazada = requests.get("https://api.lazada.vn/orders",
                     params={...}, headers=LAZ_HDR).json()

# Standard cost từ MISA
costs = requests.get("https://api.misa.vn/sme/v1/products/standard-cost",
                    headers={"Authorization": MISA_TOKEN}).json()

# Build profitability table
df = pd.DataFrame(shopee["orders"] + lazada["orders"])
df["std_cost"] = df["sku"].map({c["sku"]: c["cost"] for c in costs})
df["platform_fee"] = df["revenue"] * df["channel"].map({"Shopee": 0.10, "Lazada": 0.12})
df["gross_profit"] = df["revenue"] - df["std_cost"] - df["platform_fee"]
df["gm_pct"] = df["gross_profit"] / df["revenue"]

# Top losers
losers = df.groupby("sku").agg(rev=("revenue","sum"), gp=("gross_profit","sum"))
print(losers[losers["gp"]<0].sort_values("gp"))
```

## Bước 5: Output Format
1. **Excel COGS breakdown** (`cogs_detail_T05_2026.xlsx`): Sheet "By_SKU", "By_Customer", "By_Channel", "ABC_allocation", "RecommendActions".
2. **HTML dashboard** (`profitability_dashboard.html`): Tree map SKU × revenue × GM%, scatter volume×margin, table top/bottom 20.
3. **PDF action memo** (`profitability_action.pdf`): 3 trang - SKU cần cut, KH cần đàm phán, channel cần focus.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/profitability/`

## Checklist Trước Khi Giao
- [ ] Sum COGS detail khớp tổng COGS trên P&L
- [ ] Allocation methodology consistent (không cherry-pick)
- [ ] Đã tính cả phí sàn, hoa hồng, marketing phân bổ
- [ ] Phân tích cả 3 chiều SKU/Customer/Channel
- [ ] Action có deadline + owner cụ thể
- [ ] Sensitivity: nếu allocation đổi, kết luận có đổi không?
