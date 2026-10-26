---
name: ops-energy-cost-audit
description: |
  Audit chi phí điện theo máy/khu vực — phân bổ hoá đơn EVN theo MJC (Machine-Justified Consumption), tìm máy ngốn điện vô lý, đề xuất tiết kiệm. Dùng skill này khi người dùng yêu cầu: "audit chi phí điện", "energy audit", "kiểm toán năng lượng", "giảm tiền điện nhà máy", "phân bổ điện theo máy", "energy intensity", "EVN bill analysis", "ISO 50001". Output là Excel breakdown + HTML chart + đề xuất tiết kiệm có ROI.
---

# Energy Cost Audit — Audit Chi Phí Điện Theo Máy

## Mục Tiêu
Biến hoá đơn điện EVN từ "1 con số tổng" thành bức tranh chi tiết "máy nào ăn bao nhiêu kWh, đáng giá bao nhiêu" → đề xuất biện pháp giảm 10-25% chi phí.

## Khi Nào Dùng
- Hoá đơn điện tăng đột ngột > 15%
- Triển khai ESG/Carbon footprint
- Sản xuất kêu giá thành cao
- Audit ISO 50001 (Energy Management)
- Trước đầu tư inverter/solar

## Bước 1: Thu Thập Dữ Liệu
3 nguồn:
1. **Hoá đơn EVN 12 tháng** (kWh + VND, phân thấp điểm/cao điểm/bình thường)
2. **Bảng máy + công suất danh định** (kW, giờ chạy/ngày)
3. **Đồng hồ phụ** (nếu có submeter theo zone)

Nếu không có submeter → đặt clamp meter tạm 1 tuần để ước lượng

## Bước 2: Tính Tiêu Thụ Lý Thuyết Theo Máy
```
kWh_máy_tháng = Công suất (kW) × Giờ chạy/ngày × Load factor × 30
```

Load factor (hệ số tải):
- Máy nén khí: 0.6-0.7 (chạy on/off)
- CNC: 0.4-0.5 (gia công xen kẽ idle)
- Lò nung: 0.8-0.9 (chạy liên tục)
- Đèn LED: 1.0

So tổng lý thuyết với hoá đơn:
- Sai lệch < 10%: model OK
- Sai lệch > 20%: có máy "ma" hoặc load factor sai

## Bước 3: Phân Tích Cơ Hội Tiết Kiệm
**Top 10 cơ hội phổ biến**:
1. Tắt máy idle (motor chạy không tải) — tiết 10-30%
2. Lắp biến tần (VFD) cho motor lớn — tiết 20-50%
3. Chuyển giờ cao điểm sang thấp điểm — tiết 30% giá
4. LED thay huỳnh quang — tiết 50% điện chiếu sáng
5. Bù công suất phản kháng (tụ bù) — tránh phạt cos φ
6. Cách nhiệt đường ống hơi/lạnh — tiết 5-15%
7. Vệ sinh dàn nóng máy lạnh — tiết 10%
8. Solar rooftop — ROI 4-6 năm
9. Heat recovery khí nén — tiết 5-10%
10. Khoán điện cho ca trưởng — tiết 3-8%

Mỗi cơ hội tính:
- Đầu tư (VND)
- Tiết kiệm (kWh/năm × giá)
- Payback (tháng)
- IRR

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Bảng nhập kWh + giá EVN theo bậc thang
- Google Drive MCP: Lưu hoá đơn EVN scan
- Slack MCP: Notify khi tiêu thụ vượt budget
- Notion MCP: Database các action giảm điện + status
- WebSearch: Tra giá EVN mới nhất tại evn.com.vn, biểu giá kinh doanh
- WebFetch: Lấy data thời tiết (nhiệt độ) tương quan tiêu thụ AC

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Pull data từ submeter IoT (vd: Schneider EcoStruxure)
import requests, pandas as pd
r = requests.get("https://api.ecostruxure.io/v1/devices/meter-01/readings",
    headers={"Authorization": "Bearer ..."},
    params={"from": "2026-04-01", "to": "2026-04-30",
            "interval": "1h"})
df = pd.DataFrame(r.json()["readings"])
df["hour"] = pd.to_datetime(df["ts"]).dt.hour
df["peak"] = df["hour"].between(9,11) | df["hour"].between(17,20)
peak_kwh = df[df["peak"]]["kwh"].sum()
print(f"Cao điểm: {peak_kwh:.0f} kWh = {peak_kwh*3500:.0f} VND")
```

## Bước 5: Output Format
- `Energy_Audit_<month>.xlsx` — sheet hoá đơn, theo máy, opportunity
- `Energy_Dashboard.html` — chart 12 tháng + drill down theo zone
- `Saving_Proposal.md` — đề xuất top 10 + ROI
- `EVN_Bill_Calculator.xlsx` — calculator tính nhanh giá bậc thang
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/Energy/`

## Checklist Trước Khi Giao
- [ ] So sánh tiêu thụ với cùng kỳ năm trước (degree-day adjusted)
- [ ] Có ít nhất 3 quick win (payback < 6 tháng)
- [ ] Tính được Energy Intensity (kWh/sản phẩm)
- [ ] Đối chiếu cos φ tránh phạt EVN
- [ ] Đề xuất chia theo CAPEX/OPEX
- [ ] Có KPI theo dõi sau khi triển khai
