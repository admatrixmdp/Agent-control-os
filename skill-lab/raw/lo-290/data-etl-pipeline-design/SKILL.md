---
name: data-etl-pipeline-design
description: |
  Thiết kế ETL/ELT pipeline nhẹ cho doanh nghiệp vừa & nhỏ: từ source (DB/API/CSV) qua staging, transform, lên data mart — dùng Airbyte/dbt/Airflow/Python scheduled jobs.
  Kích hoạt khi người dùng nói: "thiết kế ETL", "pipeline dữ liệu", "ELT", "data pipeline", "dbt model", "Airbyte source", "Airflow DAG", "data warehouse", "staging mart", "tích hợp data từ nhiều nguồn".
  Output là kiến trúc Markdown + dbt project skeleton + DAG Python.
---

# ETL / ELT Pipeline Designer

## Mục Tiêu
SME hay vướng "data nằm 10 nơi, không ghép được". Skill này giúp thiết kế pipeline ELT modern (source → warehouse → dbt transform → mart) gọn nhẹ, chi phí <$500/tháng, chạy tin cậy.

## Khi Nào Dùng
- Setup data warehouse lần đầu cho SME
- Có nhiều SaaS (HubSpot, Shopify, Facebook Ads), cần gộp
- Excel/Sheet quá tải, cần move lên warehouse
- Migrate ETL legacy (SSIS, Talend) sang stack hiện đại
- Build mart cho team Marketing/Sales/Finance

## Bước 1: Map Sources & Destinations
Liệt kê tất cả source:
- **Production DB**: MySQL/PostgreSQL của app
- **SaaS**: HubSpot, Shopify, Facebook Ads, Google Ads, Stripe
- **File**: CSV upload manual từ phòng ban
- **API**: bên thứ 3 không có connector sẵn
- **Spreadsheet**: Google Sheets nguồn data tay

Destination:
- **Warehouse**: BigQuery (rẻ nhất cho SME), Snowflake, Redshift
- **Mart**: schema riêng cho mỗi phòng ban (sales_mart, marketing_mart)

## Bước 2: Chọn Architecture ELT vs ETL
**ELT (khuyến nghị cho SME)**:
- Extract → Load raw vào warehouse → Transform bằng SQL/dbt
- Tận dụng compute warehouse, dễ debug, dễ schema evolution

**Stack đề xuất**:
- **Extract & Load**: Airbyte (open-source, 300+ connectors) hoặc Fivetran (trả phí)
- **Warehouse**: BigQuery (~$5/TB scan)
- **Transform**: dbt (SQL-based, version control, test built-in)
- **Orchestration**: Airflow / Dagster / dbt Cloud / Cron
- **Monitoring**: dbt artifacts + Slack alert

## Bước 3: Layered Modeling (dbt convention)
3 lớp:
- **Raw / Staging** (`stg_*`): 1-1 với source, chỉ rename column, cast type, không business logic
- **Intermediate** (`int_*`): JOIN, deduplicate, enrich
- **Marts** (`fct_*`, `dim_*`): facts & dimensions theo phòng ban
  - `fct_orders`, `fct_sessions`, `fct_payments`
  - `dim_customers`, `dim_products`, `dim_dates`

Ví dụ structure:
```
models/
├── staging/
│   ├── hubspot/stg_hubspot__contacts.sql
│   └── shopify/stg_shopify__orders.sql
├── intermediate/int_orders_enriched.sql
└── marts/
    ├── sales/fct_orders.sql
    └── marketing/fct_attribution.sql
```

## Bước 4: Data Quality & Testing
Trong mỗi dbt model `.yml`:
- `not_null` cho ID columns
- `unique` cho primary key
- `relationships` để check foreign key
- `accepted_values` cho status enum
- Custom test: revenue >= 0, date in range

Setup freshness check: source data delay >24h → alert Slack.

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- GitHub MCP: dbt project + CI/CD (run test on PR)
- Google Drive MCP: lưu data dictionary, ERD
- Slack MCP: alert pipeline fail, freshness issue
- Notion MCP: documentation cho mỗi mart, owner, definition
- Linear MCP: ticket request data mới từ phòng ban
- WebSearch: connector có sẵn cho source X chưa
- WebFetch: pull docs Airbyte/dbt khi gặp lỗi

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Custom extractor cho API không có connector
import requests, json
from google.cloud import bigquery
client = bigquery.Client()

# Pull data từ API VN-only như Sapo, Haravan, KiotViet
def extract_kiotviet():
    token = "..."
    headers = {"Retailer": "shop", "Authorization": f"Bearer {token}"}
    r = requests.get("https://public.kiotapi.com/orders",
                     headers=headers, params={"pageSize": 100})
    return r.json()["data"]

# Load raw vào BigQuery
rows = extract_kiotviet()
errors = client.insert_rows_json("project.raw.kiotviet_orders", rows)
```

## Bước 6: Output Format
- `Pipeline_Architecture.md` — high-level diagram, stack chosen, cost estimate
- `dbt_project_skeleton/` — folder dbt init với `dbt_project.yml`, ~3 model mẫu
- `Source_Mapping.xlsx` — bảng source → table → schedule → owner
- `Data_Dictionary.md` — mỗi mart table có cột, type, definition
- `DAG_<pipeline_name>.py` — Airflow DAG mẫu
- `Cost_Estimate.xlsx` — chi phí monthly (Airbyte/Fivetran + BigQuery + dbt Cloud)
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/etl-design/`

## Checklist Trước Khi Giao
- [ ] Đã liệt kê đủ source + destination
- [ ] Architecture có diagram (Mermaid/Lucidchart)
- [ ] Layered modeling staging/int/marts rõ
- [ ] Test data quality cho tất cả mart tables
- [ ] Schedule + retry + alert đã định nghĩa
- [ ] Cost estimate <$500/tháng cho SME
- [ ] CI/CD chạy test trên PR
- [ ] Data dictionary có owner + definition
