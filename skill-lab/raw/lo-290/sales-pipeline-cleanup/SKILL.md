---
name: sales-pipeline-cleanup
description: |
  Dọn pipeline CRM — close lost stale deal, fix data, update stage chính xác để forecast tin cậy. Trigger phrases: "dọn pipeline", "pipeline cleanup", "close lost deal cũ", "stale opportunity", "fix CRM data", "lau dọn CRM", "pipeline hygiene", "pipeline garbage", "clean pipeline weekly", "rà soát deal cũ". Output là Excel hành động cleanup + Markdown SOP.
---

# Pipeline Hygiene & Cleanup

## Mục Tiêu
Loại bỏ deal "ma" trong pipeline để forecast chính xác, giúp leadership thấy reality và AE tập trung deal thực — thường gỡ được 20-40% pipeline rác sau lần dọn đầu.

## Khi Nào Dùng
- Quarterly cleanup (cuối Q1/Q2/Q3/Q4)
- Trước board meeting cần forecast tin cậy
- Pipeline coverage >5x quota (quá nhiều)
- Win rate giảm bất thường
- Manager mới onboard takeover pipeline

## Bước 1: Pull Pipeline + Phân loại "Bệnh"
Pull tất cả Open deal, flag theo rule:

**A. Stale**: no activity 30+ ngày
**B. Past close date**: close date < hôm nay, vẫn Open
**C. Wrong stage**: ở Late Stage nhưng thiếu signal (no proposal sent, no champion)
**D. Phantom**: created >180 ngày, không có next step
**E. Duplicate**: cùng KH + cùng product
**F. Missing data**: thiếu close date / amount / next step / contact

## Bước 2: Action Mapping
Mỗi flag → action:
- Stale: AE liên hệ trong 7 ngày → nếu không response → demote stage
- Past close date: AE update close date có lý do hoặc close-lost
- Wrong stage: demote về stage đúng + missing data fill
- Phantom: close-lost với reason "No engagement"
- Duplicate: merge giữ deal mới nhất
- Missing data: AE fill trong 3 ngày hoặc bị block thao tác

## Bước 3: SLA + Enforcement
- Mỗi AE phải xử trong 7 ngày work-list
- Manager review trong 1-1 tuần tới
- Reporting: % deal cleaned vs flagged
- Block tạo deal mới nếu >5 deal stale chưa xử

## Bước 4: Post-cleanup Forecast Refresh
Sau cleanup:
- Tổng pipeline mới
- Weighted pipeline (theo stage probability)
- Pipeline coverage = pipeline / quota
- So sánh trước/sau cleanup
- Adjust forecast nếu cần

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce/HubSpot MCP: query + bulk update
- Gong MCP: phát hiện deal có activity vs không (call ngoài CRM)
- Slack MCP: alert AE work-list
- Email MCP: gửi work-list weekly

**Fallback API:**
```python
# Tìm stale + bulk close-lost
from datetime import datetime, timedelta
stale = sf.query(f"""SELECT Id, Name, OwnerId FROM Opportunity 
    WHERE IsClosed = false 
    AND LastActivityDate < {datetime.now()-timedelta(30):%Y-%m-%d}""")
# Bulk update
records = [{"Id": d["Id"], "StageName": "Closed Lost",
            "LossReason__c": "Stale - no engagement"} 
           for d in stale["records"]]
sf.bulk.Opportunity.update(records)
```

## Bước 6: Output Format
- **File 1**: `pipeline_cleanup_worklist.xlsx` — AE / Deal / Flag / Action / Due date / Status
- **File 2**: `pipeline_cleanup_SOP.md` — quy trình + SLA + escalation
- **File 3**: `pipeline_before_after.xlsx` — so sánh số liệu trước/sau
- **File 4**: `forecast_refresh.xlsx` — forecast mới + variance vs cũ
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 6 flag rule chạy tự động (không thủ công)
- [ ] Work-list assign từng AE, không "all team"
- [ ] SLA 7 ngày + enforcement
- [ ] Forecast refresh sau cleanup
- [ ] Communicate transparent với leadership về reduction
- [ ] Lịch quarterly cleanup tự động
