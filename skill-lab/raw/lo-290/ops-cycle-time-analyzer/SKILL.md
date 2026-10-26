---
name: ops-cycle-time-analyzer
description: |
  Phân tích cycle time của từng công đoạn sản xuất/dịch vụ — phát hiện bottleneck, so với takt time, đề xuất line balancing. Dùng skill này khi người dùng yêu cầu: "phân tích cycle time", "đo thời gian công đoạn", "tìm bottleneck", "line balancing", "takt time analysis", "cycle time study", "tối ưu dòng chảy sản xuất". Output là Excel time study + HTML chart Pareto + đề xuất cải tiến.
---

# Cycle Time Analyzer — Phân Tích Thời Gian Công Đoạn

## Mục Tiêu
Đo thực tế thời gian từng bước trong quy trình, so với takt time (nhịp khách yêu cầu), tìm công đoạn nghẽn để cân bằng line, tăng throughput 15-30%.

## Khi Nào Dùng
- Line sản xuất không đạt sản lượng plan
- Khách order tăng, cần biết line đáp ứng được không
- Setup line mới, cần phân chia nhân công
- Triển khai Lean/Continuous Improvement
- So sánh ca ngày vs ca đêm hiệu suất

## Bước 1: Thu Thập Data Time Study
Bấm giờ thực tế từng công đoạn, ít nhất 30 mẫu/công đoạn:
- Tên công đoạn
- Người thực hiện
- Thời gian quan sát (mỗi mẫu)
- Trung bình, max, min, độ lệch chuẩn
- % value-add vs non-value-add (NVA)

Phân loại từng giây:
- **VA** (Value Add): khách sẵn sàng trả tiền (lắp ráp, gia công)
- **NVA cần thiết** (Necessary): kiểm tra, di chuyển có lý do
- **Waste** (Pure waste): chờ đợi, làm lại, di chuyển thừa

## Bước 2: Tính Takt Time
```
Takt Time = (Thời gian làm việc khả dụng / Nhu cầu khách)
```

Ví dụ:
- Ca 8h - nghỉ 1h = 7h khả dụng = 25,200s
- Demand: 600 sp/ngày
- Takt = 25,200 / 600 = 42s/sản phẩm

→ Mọi công đoạn phải <= 42s. Công đoạn nào > 42s = bottleneck.

## Bước 3: Yamazumi Chart (Stacked Bar Theo Công Đoạn)
Vẽ stacked bar cho mỗi công đoạn:
- Trục X: tên công đoạn
- Trục Y: thời gian
- Color stack: VA / NVA / Waste
- Đường đỏ ngang: Takt time

Đề xuất Line Balancing:
- Công đoạn > Takt → tách 2 người, hoặc chuyển bớt task sang công đoạn nhanh
- Công đoạn << Takt → gộp 2 công đoạn
- Mục tiêu: mỗi công đoạn ~85-95% takt (chừa buffer)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Bảng time study + công thức tự tính Takt
- Google Drive MCP: Lưu video time study làm chứng cứ
- Slack MCP: Báo bottleneck mới phát hiện vào channel #production
- Notion MCP: Lưu kết quả time study của từng line
- WebSearch: Tham khảo time study benchmark theo ngành (MTM, MOST)
- WebFetch: Tải template time study từ leanproduction.com

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Đọc data sản lượng từ MES qua REST API
import requests, pandas as pd, numpy as np
r = requests.get("https://mes.factory.local/api/production/cycle-times",
    headers={"X-API-Key": "xxx"},
    params={"line": "L1", "date": "2026-05-27"})
df = pd.DataFrame(r.json())
summary = df.groupby("station").agg(
    mean=("cycle_sec","mean"),
    std=("cycle_sec","std"),
    p95=("cycle_sec", lambda x: np.percentile(x,95)))
takt = 7*3600 / 600
summary["bottleneck"] = summary["mean"] > takt
summary.to_excel("yamazumi.xlsx")
```

## Bước 5: Output Format
- `cycle_time_study.xlsx` — bảng đo, có sheet phân tích
- `yamazumi_chart.html` — chart stacked bar có Takt line
- `bottleneck_pareto.html` — Pareto 80/20 công đoạn chậm nhất
- `line_balancing_proposal.md` — đề xuất tái phân bổ
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/CycleTime/`

## Checklist Trước Khi Giao
- [ ] Mỗi công đoạn có >= 30 mẫu để statistical valid
- [ ] Phân tách rõ VA/NVA/Waste
- [ ] Takt time tính từ demand thực tế
- [ ] Bottleneck có root cause (không chỉ "chậm")
- [ ] Đề xuất có ROI (tăng bao nhiêu sp/h)
- [ ] Có kế hoạch re-measure sau cải tiến
