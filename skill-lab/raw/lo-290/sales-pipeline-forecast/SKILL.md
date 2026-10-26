---
name: sales-pipeline-forecast
description: |
  Dự báo pipeline theo weighted stage + AI signal, tạo 3 case forecast (Commit/Best/Pipe) cho leadership. Trigger phrases: "dự báo pipeline", "pipeline forecast", "weighted forecast", "commit best pipe", "forecast doanh thu sales", "tính forecast quý", "dự báo doanh số", "build forecast model", "forecast accuracy", "pipeline projection". Output là Excel forecast model + PPT exec summary.
---

# Pipeline Forecast Builder (Weighted + AI)

## Mục Tiêu
Tạo forecast chính xác >85% bằng kết hợp weighted stage probability + AI signal (engagement, sentiment) + manager judgment — 3 case Commit/Best Case/Pipeline cho leadership ra quyết định.

## Khi Nào Dùng
- Cuối tuần/cuối tháng/cuối quý forecast cycle
- Board meeting cần forecast tin cậy
- Reforecast sau event lớn (lose deal lớn, đối thủ chiếm KH)
- Annual planning
- Adjust quota mid-year

## Bước 1: Stage Probability Baseline
Pull historical 12 tháng:
- Mỗi stage có conversion-to-close rate thật
- Vd: Discovery 10%, Demo 25%, Proposal 50%, Negotiation 75%, Verbal 90%

Lưu ý: dùng historical thật, không dùng default CRM.

## Bước 2: 3 Case Forecast

**Commit Case (high confidence)**:
- Verbal commit từ KH
- Close date trong period
- Có signed quote hoặc PO sắp ký
- Probability >80%
→ Manager confident commit con số này

**Best Case**:
- Commit + Late stage deal probability 50-80%
- Có champion + EB engaged
- Close date trong period
→ Top-end achievable nếu mọi thứ đúng kế hoạch

**Pipeline (Total weighted)**:
- All open opportunity × stage probability
- Cho biết health pipeline dài hạn

## Bước 3: AI Signal Adjustment
Adjust weighted theo signal:
- Engagement: số email/meeting 30 ngày qua. Low → -10%
- Last activity: >14 ngày → -15%
- Multithreading: chỉ 1 contact → -10%
- Champion verified: +10%
- Proposal sent: +15% nếu đang Negotiation
- Mutual Action Plan signed: +20%

## Bước 4: Manager Override + Sanity Check
Manager review từng deal:
- Approve / Adjust / Reject từng deal trong Commit
- Note lý do nếu override
- So với 4 quý trước: forecast accuracy bao nhiêu?

Sanity check:
- Coverage = Pipeline / Quota nên 3-5x
- Win rate trung bình 25-35% → outlier flag
- Average deal size có khớp historical?

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce/HubSpot MCP: pull opportunity + activity
- Gong/Clari MCP: pull AI signal sẵn có
- Slack MCP: forecast call ping
- Drive MCP: lưu version forecast history

**Fallback API:**
```python
# Weighted forecast calculation
import pandas as pd
opps = sf.query("""SELECT Id, Name, Amount, StageName, CloseDate,
    LastActivityDate, ProbabilityAI__c FROM Opportunity 
    WHERE IsClosed = false AND CloseDate <= THIS_QUARTER""")
df = pd.DataFrame(opps["records"])
stage_prob = {"Discovery": 0.1, "Demo": 0.25, "Proposal": 0.5,
              "Negotiation": 0.75, "Verbal": 0.9}
df["weighted"] = df["Amount"] * df["StageName"].map(stage_prob)
df["adjusted"] = df["weighted"] * (1 + df["ProbabilityAI__c"]/100)
print(f"Pipeline weighted: {df['adjusted'].sum():,.0f}")
```

## Bước 6: Output Format
- **File 1**: `forecast_<quarter>.xlsx` — sheet Commit / Best / Pipe + summary + variance
- **File 2**: `forecast_exec_summary.pptx` — 3 slide: number, top deal, risk
- **File 3**: `forecast_accuracy_history.xlsx` — track forecast vs actual mỗi quý
- **File 4**: `deal_signal_review.xlsx` — deal flag bởi AI để Manager review
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Probability dùng historical thật
- [ ] 3 case rõ ràng (Commit/Best/Pipe)
- [ ] AI signal adjustment có log
- [ ] Manager override có lý do
- [ ] So sánh accuracy 4 quý trước
- [ ] Forecast submit đúng deadline (không trễ)
