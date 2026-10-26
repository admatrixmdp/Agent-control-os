---
name: fin-cost-of-goods-builder
description: |
  Tính giá thành sản phẩm sản xuất theo định mức BOM + chi phí nhân công + overhead phân bổ,
  cho cả phương pháp Job Costing và Process Costing. Trigger phrases: "tính giá thành",
  "BOM costing", "standard cost", "giá thành sản phẩm", "manufacturing cost",
  "job costing", "process costing", "labor + overhead", "cost rollup", "tính COGS sản xuất".
  Output là Excel cost sheet + PDF báo cáo giá thành.
---

# Tính Giá Thành Sản Phẩm Theo BOM + Labor + Overhead

## Mục Tiêu
Tính chính xác giá thành đến từng SKU/lệnh sản xuất để quyết định giá bán, đánh giá hiệu quả
sản xuất, phát hiện sản phẩm âm biên. Đặc biệt quan trọng với DN sản xuất multi-SKU.

## Khi Nào Dùng
- Cuối tháng tính giá thành thực tế cho hạch toán
- Trước khi đưa ra giá bán SKU mới
- Khi thay đổi nguyên liệu, phương án sản xuất
- Đánh giá hiệu quả từng dây chuyền, từng tổ
- Quyết định make vs buy (tự sản xuất hay outsource)

## Bước 1: Chuẩn Bị BOM (Bill of Materials)
Cho mỗi SKU thành phẩm, lập BOM:
| SKU thành phẩm | Mã NVL | Tên NVL | Định mức | Đơn vị | Đơn giá NVL | Hao hụt % |

Ví dụ áo thun:
- Vải cotton: 0.6m × 80,000đ = 48,000đ
- Chỉ: 50m × 100đ = 5,000đ
- Cúc: 5 cái × 500đ = 2,500đ
- Bao bì: 1 × 3,000đ = 3,000đ
- **Total Material Cost (TMC) = 58,500đ**

Lưu ý hao hụt định mức: vải cắt thừa 5%, chỉ rơi vãi 2%.

## Bước 2: Chi Phí Nhân Công Trực Tiếp (DL)
Cho mỗi công đoạn:
- Thời gian định mức (phút/SP)
- Đơn giá nhân công theo tổ/level
- Tỷ lệ hiệu suất thực tế vs định mức

Ví dụ áo thun:
- Cắt: 3 phút × 600đ/phút = 1,800đ
- May: 15 phút × 700đ/phút = 10,500đ
- KCS: 2 phút × 800đ = 1,600đ
- **Total DL = 13,900đ**

## Bước 3: Phân Bổ Overhead Sản Xuất (MOH)
**Tập hợp MOH:**
- Lương quản đốc, công nhân gián tiếp
- Khấu hao máy móc nhà xưởng
- Điện, nước, gas sản xuất
- Bảo trì máy, công cụ dụng cụ
- Bảo hiểm nhà xưởng

**Phân bổ theo driver:**
- Theo giờ máy chạy
- Theo giờ công lao động
- Theo số lượng sản xuất
- Theo ABC (Activity Based Costing) nếu phức tạp

```
OH rate = Total MOH / Total driver
OH cho SKU = OH rate × driver consumed
```

**Total Cost = TMC + DL + MOH**

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Pull BOM master, push cost sheet về sheet sản xuất
- Google Drive MCP: Lưu cost sheet theo từng lệnh sản xuất
- Gmail MCP: Gửi báo cáo variance giám đốc sản xuất + CFO
- WebSearch: Tra giá NVL thị trường (thép, vải, hạt nhựa) làm benchmark

**Fallback bằng API:**
```python
# Pull dữ liệu sản xuất từ FAST Manufacturing API
import requests
r = requests.post(
    "https://api.fast.com.vn/manuf/v1/production-orders",
    json={"period": "2026-05"},
    headers={"Authorization": f"Bearer {TOKEN}"}
)
po_list = r.json()["data"]
# Tính variance: actual vs standard
for po in po_list:
    sku = po["sku"]
    actual_qty = po["completed_qty"]
    std_cost = standard_cost[sku] * actual_qty
    actual_cost = po["actual_material"] + po["actual_labor"] + po["actual_oh"]
    po["variance"] = actual_cost - std_cost
    po["variance_pct"] = po["variance"] / std_cost * 100
```

## Bước 5: Output Format
1. **Excel cost sheet** (`product_costing_T05_2026.xlsx`): Sheet "BOM_master", "Std_cost" theo SKU, "Actual_cost" theo lệnh SX, "Variance" so sánh, "MOH_allocation" chi tiết.
2. **PDF báo cáo giá thành** (`cogs_report_T05.pdf`): Trình giám đốc sản xuất + CFO.
3. **HTML dashboard** (`costing_dashboard.html`): Waterfall chart cấu phần giá thành, bar chart variance top 10 SKU, scatter giá thành vs giá bán (phát hiện âm biên).

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/costing/`

## Checklist Trước Khi Giao
- [ ] BOM đã verify với phòng kỹ thuật + R&D
- [ ] Định mức nhân công đo bằng stopwatch ≥ 3 lần
- [ ] Driver phân bổ OH có logic, không tuỳ tiện
- [ ] Tổng cost roll-up khớp giá vốn sổ cái
- [ ] Variance >5% có giải thích
- [ ] Cost sheet update khi giá NVL đổi >3%
