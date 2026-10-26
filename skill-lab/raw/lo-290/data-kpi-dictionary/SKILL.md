---
name: data-kpi-dictionary
description: |
  Xây dựng từ điển KPI công ty: mỗi metric có definition, công thức SQL chính thức, owner, granularity, source — chấm dứt cãi nhau "doanh thu của em khác doanh thu báo cáo".
  Kích hoạt khi người dùng nói: "từ điển KPI", "metric dictionary", "metric definition", "data catalog", "single source of truth", "định nghĩa KPI", "metric layer", "metrics store", "thống nhất KPI", "data governance metrics".
  Output là Markdown/Notion + YAML metrics + SQL macros dbt.
---

# KPI Metrics Dictionary Builder

## Mục Tiêu
Cảnh "phòng Sales bảo doanh thu 5 tỷ, Finance bảo 4.8 tỷ, BoD nhận 2 con số khác nhau" là vấn đề muôn thuở. Skill này tạo metric dictionary làm single source of truth, được trích trực tiếp từ warehouse — chấm dứt tranh cãi.

## Khi Nào Dùng
- Công ty >50 NV, bắt đầu có nhiều dashboard
- Sếp nhận báo cáo từ 2 nguồn lệch nhau, yêu cầu thống nhất
- Setup data team mới, cần governance ngay từ đầu
- Migrate sang semantic layer (Looker LookML, Cube, dbt Semantic Layer)
- Audit kết thúc năm, kế toán cần định nghĩa rõ revenue

## Bước 1: Phỏng Vấn Stakeholder Tìm Metric Chính
Workshop với mỗi phòng:
- **CEO/BoD**: 5-7 metric tối thượng (revenue, GP%, NPS, headcount, runway)
- **Sales**: pipeline value, win rate, ARR, ACV, CAC
- **Marketing**: MQL/SQL, CPL, ROAS, attribution revenue
- **Product**: MAU/WAU/DAU, retention, NPS, feature adoption
- **Finance**: revenue (recognized vs collected), AR/AP days, burn rate
- **Operations**: fulfillment time, defect rate, OTIF

Mỗi metric hỏi:
- "Định nghĩa chính xác trong câu nói?"
- "Công thức tính?"
- "Edge case: tax có tính không? Refund trừ chưa? Foreign currency?"
- "Ai là owner cuối cùng?"

## Bước 2: Format Mỗi Metric Theo Template
```yaml
- name: gross_revenue
  display_name: "Doanh thu Gộp"
  category: Sales
  owner: CFO (Nguyen Van A)
  description: |
    Tổng giá trị order tính theo ngày ghi nhận (recognition date),
    BAO GỒM VAT, KHÔNG trừ refund/cancellation.
  formula: SUM(orders.gross_amount) WHERE status IN ('confirmed','fulfilled','delivered')
  sql_source: |
    SELECT SUM(gross_amount)
    FROM mart.fct_orders
    WHERE order_status IN ('confirmed', 'fulfilled', 'delivered')
      AND recognition_date BETWEEN {{start_date}} AND {{end_date}}
  granularity:
    time: [day, week, month, quarter, year]
    dimensions: [region, channel, product_category, sales_rep]
  unit: VND
  data_freshness: hourly
  source_tables: [fct_orders, dim_dates]
  related_metrics: [net_revenue, gross_margin]
  exclusions:
    - Refund không trừ ở đây (xem net_revenue)
    - Internal test orders bị filter ở staging layer
  approved_at: 2026-05-15
  reviewed_at: 2026-05-15
  next_review: 2026-11-15
```

## Bước 3: Phân Loại Theo Tầng
- **North Star Metric** (1-3 metric tối quan trọng)
- **L1 Strategic KPIs** (15-25 metric BoD theo dõi)
- **L2 Operational KPIs** (50-100 metric Manager dùng)
- **L3 Diagnostic Metrics** (free-form, analyst tạo)

Quản lý chặt L1, lỏng L3.

## Bước 4: Implement Trong Semantic Layer
Đưa metric vào code:
- **dbt metrics** (`models/marts/metrics.yml`)
- **LookML measures** nếu dùng Looker
- **Cube semantic layer** nếu dùng Cube.dev
- **Mode/Hex** metric library

Mọi dashboard/BI tool query qua semantic layer — không ai viết SQL tự tính revenue nữa.

## Bước 5: Governance Process
- **Tạo metric mới**: cần PR review, approval từ owner + data lead
- **Sửa metric**: phải versioning, thông báo all consumers, có migration plan
- **Deprecate metric**: cảnh báo 30 ngày trước khi xoá
- **Review định kỳ**: 6 tháng/lần check còn relevant không

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- GitHub MCP: lưu metrics.yml trong repo data, PR review
- Notion MCP: portal đọc cho non-tech (tag, search, link to dashboard)
- Slack MCP: bot `/metric revenue` trả về definition tức thì
- Linear MCP: ticket request metric mới có template
- Google Drive MCP: lưu workshop notes, audit history
- WebSearch: best practice metrics layer (dbt, Cube, Looker)
- WebFetch: pull schema dbt Semantic Layer docs

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Bot Slack trả lời /metric <name>
from slack_sdk import WebClient
import yaml
client = WebClient(token="xoxb-...")
metrics = yaml.safe_load(open("metrics.yml"))

def respond(metric_name):
    m = next((x for x in metrics if x["name"] == metric_name), None)
    if not m: return f"Không tìm thấy metric `{metric_name}`"
    return f"""*{m['display_name']}*
Owner: {m['owner']}
Định nghĩa: {m['description']}
Formula: `{m['formula']}`
Đơn vị: {m['unit']} | Refresh: {m['data_freshness']}"""
```

## Bước 7: Output Format
- `Metrics_Dictionary.md` — index có search
- `metrics.yml` — YAML structured, dùng trong code
- `metric_<name>.md` cho từng metric chi tiết
- `Metric_Governance_Policy.md` — quy trình tạo/sửa/xoá metric
- `Workshop_Notes_<YYYYMM>.md` — log buổi phỏng vấn stakeholder
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/metric-dict/`

## Checklist Trước Khi Giao
- [ ] Đã phỏng vấn ≥5 phòng ban
- [ ] North Star + L1 KPI có owner ký xác nhận
- [ ] Mỗi metric có SQL chính thức + edge case nêu rõ
- [ ] Granularity (time + dimension) định nghĩa rõ
- [ ] Đã implement trong semantic layer thực tế
- [ ] Governance process được CTO/CFO duyệt
- [ ] Có Slack bot trả lời tự động definition
- [ ] Lịch review 6 tháng/lần đã set
