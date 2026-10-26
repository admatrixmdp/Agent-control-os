---
name: ops-oee-tracker
description: |
  Tracker OEE máy móc (Overall Equipment Effectiveness) = Availability × Performance × Quality — tự động tính, dashboard realtime, cảnh báo khi tụt. Dùng skill này khi người dùng yêu cầu: "tính OEE máy", "OEE tracker", "hiệu suất thiết bị tổng thể", "Availability Performance Quality", "downtime tracking", "TPM dashboard", "Six Big Losses", "machine performance". Output là Excel template + HTML dashboard + Google Sheet auto-import.
---

# OEE Tracker — Theo Dõi Hiệu Suất Máy Tổng Thể

## Mục Tiêu
Đo lường thật khả năng khai thác máy móc theo chuẩn OEE quốc tế, phát hiện 6 Big Losses, đặt target nâng OEE từ trung bình ngành 60% lên World Class 85%.

## Khi Nào Dùng
- Đầu tư mới máy CNC/dây chuyền, cần benchmark
- Sản xuất không đạt KPI nhưng không biết tại sao
- Triển khai TPM (Total Productive Maintenance)
- Lên kế hoạch bảo trì preventive
- Justify mua máy mới (OEE máy cũ < 50%)

## Bước 1: Định Nghĩa Các Thành Phần OEE
```
OEE = Availability × Performance × Quality
```

**Availability** = (Run Time / Planned Production Time)
- Loại Loss: Breakdown (sự cố), Setup/Adjustment (chỉnh máy)

**Performance** = (Ideal Cycle Time × Total Count) / Run Time
- Loại Loss: Minor Stops (kẹt nhỏ), Reduced Speed (chạy chậm)

**Quality** = Good Count / Total Count
- Loại Loss: Defects (lỗi), Startup Rejects (hàng đầu ca lỗi)

Ví dụ:
- Planned: 480 phút (ca 8h - nghỉ)
- Downtime: 60 phút → Run Time = 420 phút
- Availability = 420/480 = 87.5%
- Ideal cycle = 1 sp/phút → Ideal count = 420 sp
- Actual count = 380 sp → Performance = 380/420 = 90.5%
- Reject 10 sp → Good = 370 → Quality = 370/380 = 97.4%
- **OEE = 87.5% × 90.5% × 97.4% = 77.1%**

## Bước 2: Six Big Losses Tracking
| Loss | Loại | Cách giảm |
|---|---|---|
| 1. Breakdown | Availability | Preventive Maint, root cause |
| 2. Setup/Changeover | Availability | SMED (single-minute exchange) |
| 3. Minor Stops | Performance | Andon + 5 Why mỗi stop |
| 4. Reduced Speed | Performance | Hiệu chuẩn, training |
| 5. Defects | Quality | Poka-yoke, SPC |
| 6. Startup Rejects | Quality | Warm-up procedure |

Mỗi lần dừng máy → ghi mã loss + thời gian. Hằng tuần Pareto loss tốn thời gian nhất.

## Bước 3: Dashboard Thiết Kế
- Top-left: OEE hiện tại (gauge chart, target 85%)
- Top-right: 3 chỉ số A/P/Q rời
- Mid: Trend OEE 30 ngày
- Bottom-left: Pareto Six Big Losses
- Bottom-right: Top 5 lý do downtime tuần này

Benchmark theo Toyota Production System:
- < 40%: Kém
- 40-60%: Trung bình ngành VN
- 60-85%: Tốt
- > 85%: World class

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Nhật ký downtime + tự công thức OEE
- Slack MCP: Bot cảnh báo OEE < 60% trong ca
- Notion MCP: Database các loss code + mô tả
- Google Drive MCP: Lưu file dashboard chia sẻ cho ca trưởng
- WebSearch: So benchmark OEE ngành (textile, electronics, food)
- WebFetch: Tải tool OEE Calculator từ oee.com

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Pull data từ MES + tính OEE realtime
import requests, datetime as dt
r = requests.get("https://mes.local/api/v1/machine/CNC-01/status",
    headers={"X-API-Key": "..."},
    params={"date": dt.date.today().isoformat()})
d = r.json()
A = d["run_time_min"] / d["planned_min"]
P = (d["ideal_cycle_sec"] * d["total_count"]) / (d["run_time_min"]*60)
Q = d["good_count"] / d["total_count"]
OEE = A * P * Q
print(f"OEE={OEE:.1%} A={A:.1%} P={P:.1%} Q={Q:.1%}")
if OEE < 0.6:
    # Notify Slack
    requests.post("https://hooks.slack.com/...",
        json={"text": f":warning: OEE CNC-01 = {OEE:.1%}"})
```

## Bước 5: Output Format
- `OEE_Template.xlsx` — bảng nhập downtime + auto tính OEE
- `OEE_Dashboard.html` — dashboard interactive (Chart.js)
- `Loss_Codes.md` — danh mục mã loss + mô tả
- `OEE_Weekly_Report.pdf` — bản in cho trưởng ca
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/OEE/`

## Checklist Trước Khi Giao
- [ ] Ideal cycle time là theo nhà SX máy, không tự đặt
- [ ] Mỗi downtime > 5 phút phải ghi mã loss
- [ ] Quality count gồm cả rework, không chỉ scrap
- [ ] Có baseline 4 tuần trước khi đặt target
- [ ] Dashboard refresh tối thiểu mỗi giờ
- [ ] Có TPM team review weekly
