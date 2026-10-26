---
name: data-dashboard-builder
description: |
  Thiết kế và build dashboard kinh doanh trên Looker Studio / Metabase / Power BI / Tableau — từ business question đến mockup, data model, chart selection, filter, drill-down.
  Kích hoạt khi người dùng nói: "xây dashboard", "tạo Looker Studio", "Metabase dashboard", "Power BI report", "dashboard kinh doanh", "BI dashboard", "data visualization", "báo cáo trực quan", "executive dashboard", "dashboard CEO sales marketing".
  Output là blueprint Markdown + SQL queries + dashboard prototype.
---

# Business Dashboard Builder

## Mục Tiêu
Hầu hết dashboard chết yểu vì xây từ data ra (data-first) thay vì từ câu hỏi kinh doanh (question-first). Skill này áp dụng quy trình question-first để dashboard thực sự được dùng hàng tuần.

## Khi Nào Dùng
- CEO/Trưởng phòng yêu cầu "1 dashboard duy nhất xem tất cả"
- Đã có data warehouse, cần lớp visualization
- Hệ thống cũ là Excel/Sheet rời rạc, cần consolidate
- Migration từ tool BI cũ (Tableau → Looker)
- Setup tracking cho team Sales/Marketing/Ops mới

## Bước 1: Question-First Workshop
Hỏi stakeholder chính xác:
- **Audience**: ai sẽ xem dashboard? (CEO/Dept Head/Analyst/Frontline)
- **Decision**: xem xong họ làm gì? "Quyết định gì dựa vào số này?"
- **Cadence**: xem hàng ngày/tuần/tháng?
- **5 câu hỏi cốt lõi** dashboard phải trả lời

Ví dụ Sales Dashboard:
1. Doanh thu MTD vs target ra sao? (gauge)
2. Top 5 sale & bottom 5 sale tuần này? (bar)
3. Pipeline đang ở stage nào? (funnel)
4. Khách hàng nào sắp churn? (table có flag)
5. Conversion rate theo nguồn lead? (heatmap)

## Bước 2: Data Model & Source
Map mỗi câu hỏi → metric → table & column nguồn:
| Question | Metric | Calculation | Source table | Update freq |
|----------|--------|-------------|--------------|-------------|
| Doanh thu MTD | revenue_mtd | SUM(amount WHERE date≥start_month) | fact_orders | hourly |
| Top sale | rep_revenue | SUM by rep_id | fact_orders + dim_sales_rep | daily |

Xác định:
- Data freshness (real-time/hourly/daily)
- Granularity (transaction/daily aggregate)
- Joins cần thiết
- Filter mặc định (date range, region, channel)

## Bước 3: Chọn Loại Chart Đúng
Quy tắc chọn theo intent:
- **So sánh** giá trị → Bar chart (horizontal nếu nhiều category)
- **Xu hướng theo thời gian** → Line chart
- **Tỷ trọng** → Donut (max 5 slice) hoặc stacked bar
- **Phân phối** → Histogram, Box plot
- **Tương quan** → Scatter plot
- **Geography** → Map (Việt Nam tỉnh thành)
- **KPI đơn lẻ** → Big number + sparkline + delta vs LP

Tránh: pie >5 slice, 3D chart, dual-axis nếu không cần.

## Bước 4: Layout & Interaction
Quy tắc F-pattern (mắt đọc):
- **Top row**: 4-6 KPI big number (revenue, GP%, orders, AOV...)
- **Row 2**: 2 trend chart lớn (revenue trend, orders trend)
- **Row 3**: 2-3 breakdown (by category, by region, by channel)
- **Row 4**: 1 table chi tiết drill-down

Filter ở top: date range, segment, region. Click chart → cross-filter các chart khác.

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: data source cho dashboard nhỏ, prototype
- Google Drive MCP: lưu mockup Figma, blueprint
- GitHub MCP: version control LookML/dbt models
- Notion MCP: dashboard documentation, metrics dictionary
- Linear MCP: ticket cho mỗi metric/chart cần build
- Slack MCP: schedule send dashboard daily/weekly digest
- WebSearch: best practice dashboard theo ngành
- WebFetch: pull data từ HubSpot, Shopify, Facebook Ads

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tạo dashboard Metabase qua API
import requests
META = "https://metabase.company.vn"
session = requests.post(f"{META}/api/session",
    json={"username": "admin", "password": "..."}).json()
headers = {"X-Metabase-Session": session["id"]}
# Create card (chart)
card = requests.post(f"{META}/api/card", headers=headers, json={
    "name": "Revenue MTD",
    "dataset_query": {"type": "native",
        "native": {"query": "SELECT SUM(amount) FROM orders WHERE date >= date_trunc('month', now())"},
        "database": 1},
    "display": "scalar",
    "visualization_settings": {}})
```

## Bước 6: Output Format
- File chính: `Dashboard_Blueprint_<Tên>.md`
  - Business questions
  - Metric dictionary
  - Data model diagram
  - Wireframe layout
  - SQL queries cho từng chart
- File SQL: `queries/<chart_name>.sql`
- Mockup Figma export PNG
- Test data CSV để demo
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/dashboards/`

## Checklist Trước Khi Giao
- [ ] Có 5 business questions được stakeholder ký xác nhận
- [ ] Metric dictionary rõ definition + formula
- [ ] Data freshness phù hợp use case
- [ ] Chart type chọn đúng intent
- [ ] Filter + drill-down hoạt động
- [ ] Test với 3 user thật, sửa feedback
- [ ] Có user training video 5 phút
- [ ] Schedule monthly review để tối ưu/remove chart không dùng
