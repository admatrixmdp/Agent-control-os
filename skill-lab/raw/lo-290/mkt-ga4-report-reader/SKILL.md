---
name: mkt-ga4-report-reader
description: |
  Đọc và tóm tắt báo cáo Google Analytics 4 cho doanh nghiệp Việt Nam — kéo metric, phát hiện bất thường, sinh insight và action tuần. Kích hoạt khi người dùng nói: "đọc GA4", "phân tích GA4", "báo cáo GA4 tuần", "Google Analytics insight", "GA4 dashboard", "traffic report", "phân tích traffic website", "audit GA4". Output là HTML weekly report + Excel raw.
---

# Đọc & Tóm Tắt Báo Cáo GA4

## Mục Tiêu
Mỗi tuần có 1 báo cáo GA4 ngắn 1 trang đủ insight + action thay vì rời tab GA4 ngó 30 phút mà chẳng rút ra gì.

## Khi Nào Dùng
- Báo cáo tuần/tháng cho sếp
- Phát hiện traffic giảm đột ngột
- Trước launch campaign mới (baseline)
- Sau campaign (đo lift)
- Onboard team mới đọc data

## Bước 1: Kết Nối Property
Hỏi:
1. GA4 Property ID
2. Khoảng thời gian (7d / 28d / 90d)
3. So với period nào (previous / year-over-year)
4. Mục tiêu phân tích (traffic / conversion / audience)
5. KPI quan trọng nhất

## Bước 2: Kéo & Phân Tích 6 Section
1. **Tổng quan**: Users, Sessions, Engagement rate, Avg session duration, Bounce rate
2. **Acquisition**: Top kênh (Organic/Direct/Paid/Social/Email/Referral) + delta
3. **Behavior**: Top pages, Events, Engagement time
4. **Conversion**: Goal conversions, Revenue, CR, AOV
5. **Audience**: Demographic, Device, Location
6. **Bất thường**: spike/drop bất thường, theo nguyên nhân

## Bước 3: Sinh Insight + Action
Mỗi section có:
- 2-3 insight quan trọng (số liệu cụ thể)
- 1-2 action đề xuất

Ví dụ: "Organic traffic giảm 23% WoW, chủ yếu do bài XYZ rớt từ rank 3 → 8. Action: refresh bài + xây 3 backlink trong tuần."

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- GA4 MCP / Analytics Data API
- Search Console MCP: cross-check organic
- Google Ads MCP: cross-check paid
- Google Sheets MCP: log weekly
- Slack MCP: gửi report

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Pull metrics cơ bản
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, Dimension, Metric, DateRange
client = BetaAnalyticsDataClient()
req = RunReportRequest(
  property='properties/123456',
  dimensions=[Dimension(name='sessionDefaultChannelGroup')],
  metrics=[Metric(name='sessions'),Metric(name='conversions'),Metric(name='totalRevenue')],
  date_ranges=[DateRange(start_date='7daysAgo', end_date='today')])
res = client.run_report(req)
```

## Bước 5: Output Format
- File HTML report 1-2 trang weekly + chart
- File `.xlsx` raw data
- Slack message tóm tắt 5 bullet
- Email cho leadership (nếu cần)
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 6 section đầy đủ
- [ ] Delta % so cùng kỳ
- [ ] >= 5 insight có data
- [ ] >= 3 action đề xuất
- [ ] Phát hiện bất thường giải thích nguyên nhân
- [ ] Visual chart dễ đọc
