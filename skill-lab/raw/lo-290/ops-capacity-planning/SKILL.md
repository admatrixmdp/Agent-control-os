---
name: ops-capacity-planning
description: |
  Lập kế hoạch công suất sản xuất (Capacity Planning) theo demand forecast — tính RCCP, finite capacity, xác định bottleneck & overtime cần thiết. Dùng skill này khi người dùng yêu cầu: "capacity planning", "kế hoạch công suất", "tính công suất sản xuất", "RCCP", "finite capacity", "lập plan dài hạn sản xuất", "load profile", "công suất khả dụng". Output là Excel capacity model + HTML chart load vs capacity + đề xuất.
---

# Capacity Planning — Lập Kế Hoạch Công Suất Sản Xuất

## Mục Tiêu
Trả lời câu hỏi "Nhà máy có đủ công suất nhận đơn này không?" và "Cần OT/ca 3/nhập thêm máy ở thời điểm nào?" — tránh nhận đơn không làm nổi hoặc dư công suất gây phí.

## Khi Nào Dùng
- Sales đưa forecast 3-12 tháng
- Khách hàng lớn đề xuất hợp đồng dài hạn
- Cân nhắc đầu tư máy mới
- Mùa cao điểm (Tết, back-to-school, đám cưới)
- Sau khi mất 1 line/máy do sự cố

## Bước 1: Tính Công Suất Khả Dụng (Available Capacity)
```
AC = Số máy × Giờ/ngày × Ngày/tháng × Uptime × Efficiency
```

Ví dụ:
- 5 máy CNC × 16h (2 ca) × 26 ngày × 0.85 (uptime) × 0.9 (eff) = 1591h/tháng
- Mỗi sản phẩm cần 0.5h → công suất = 3182 sp/tháng

Phân biệt:
- **Design Capacity** (lý thuyết)
- **Effective Capacity** (sau trừ planned downtime)
- **Actual Capacity** (sau trừ unplanned)

## Bước 2: Tính Load Từ Demand
Demand × cycle time = Load (h)
| Tháng | Demand (pcs) | Load (h) | AC (h) | Util% | Gap |
|---|---|---|---|---|---|
| T6 | 2,800 | 1,400 | 1,591 | 88% | OK |
| T7 | 3,500 | 1,750 | 1,591 | 110% | -159h |
| T8 | 4,200 | 2,100 | 1,591 | 132% | -509h |
| T9 | 2,500 | 1,250 | 1,591 | 79% | Dư |

Tháng có gap → tính cách bù.

## Bước 3: Đề Xuất Giải Pháp Theo Gap
| Mức gap | Giải pháp | Cost | Lead time |
|---|---|---|---|
| < 10% | OT cuối tuần | OT × 1.5 | Ngay |
| 10-25% | Thêm ca 3 + thuê tạm | Nhân công × 1.3 | 1-2 tuần |
| 25-50% | Outsource sub-assembly | Phụ thuộc giá outsource | 2-4 tuần |
| > 50% | Đầu tư máy mới | Capex lớn | 3-6 tháng |

Cũng có thể dịch chuyển plan: làm trước tháng nhàn, lùi tháng peak.

RCCP (Rough-Cut Capacity Planning) cho 3-6 tháng tới, MPS cho 1-3 tháng.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Capacity model + demand forecast
- Slack MCP: Cảnh báo khi util > 95% trong tháng
- Notion MCP: Database capacity quyết định
- Google Calendar MCP: Block lịch OT, holiday
- WebSearch: Benchmark utilization rate ngành (chuẩn 75-85%)
- WebFetch: Lấy template capacity từ apics.org

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Pull demand forecast từ ERP + tính capacity
import requests, pandas as pd
fc = requests.get("https://erp.local/api/forecast",
    headers={"X-Token":"..."},
    params={"horizon_months":6}).json()
df = pd.DataFrame(fc["data"])
df["load_h"] = df["units"] * 0.5  # cycle time
machines = 5
ac_per_month = machines * 16 * 26 * 0.85 * 0.9
df["util"] = df["load_h"] / ac_per_month
df["gap_h"] = df["load_h"] - ac_per_month
df["action"] = df["util"].apply(
    lambda u: "OK" if u<0.9 else "OT" if u<1.1
    else "Add shift" if u<1.25 else "Invest")
df.to_excel("capacity_plan.xlsx")
```

## Bước 5: Output Format
- `Capacity_Model.xlsx` — bảng tính AC/Load/Util theo tháng
- `Load_vs_Capacity.html` — chart bar với đường AC ngang
- `Capacity_Action_Plan.md` — quyết định OT/ca/invest theo tháng
- `What_If_Scenarios.xlsx` — sensitivity analysis 3 kịch bản
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/Capacity/`

## Checklist Trước Khi Giao
- [ ] Uptime và Efficiency lấy từ data lịch sử (không tự đặt 100%)
- [ ] Demand có 3 kịch bản: Best/Base/Worst
- [ ] Đã trừ ngày lễ Tết, ngày Chủ nhật
- [ ] Có buffer 10-15% cho biến động
- [ ] Đề xuất hành động cụ thể cho mỗi tháng gap
- [ ] Review hàng tháng so với actual
