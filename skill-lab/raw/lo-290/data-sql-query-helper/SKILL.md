---
name: data-sql-query-helper
description: |
  Hỗ trợ viết, debug, tối ưu SQL phức tạp: JOIN nhiều bảng, window function, CTE, subquery, performance tuning, anti-pattern detection cho PostgreSQL/MySQL/BigQuery/Snowflake.
  Kích hoạt khi người dùng nói: "viết SQL", "giúp query SQL", "JOIN bảng", "window function", "CTE", "SQL tối ưu", "debug query", "SQL chậm", "viết query phân tích", "SQL BigQuery Snowflake", "PostgreSQL query".
  Output là file .sql có comment + giải thích execution plan.
---

# SQL Query Helper & Optimizer

## Mục Tiêu
Giúp analyst & developer viết SQL chính xác, performant, dễ maintain — đặc biệt cho các use case phân tích kinh doanh phức tạp với window function, CTE, JOIN nhiều cấp.

## Khi Nào Dùng
- Cần phân tích đặc thù: cohort, funnel, attribution, RFM
- Query đang chạy chậm, cần optimize
- Migrate query từ dialect cũ (MySQL → BigQuery)
- Junior analyst cần học pattern SQL nâng cao
- Refactor SQL spaghetti thành CTE rõ ràng

## Bước 1: Hiểu Yêu Cầu Trước Khi Viết
Hỏi rõ:
- **Mục tiêu**: câu trả lời business question gì?
- **Database**: PostgreSQL/MySQL/BigQuery/Snowflake/Redshift (mỗi cái có syntax riêng)
- **Bảng nguồn**: tên, schema, số dòng ước lượng, có index gì
- **Performance**: query này chạy realtime cho dashboard hay batch ETL?
- **Output expected**: row format, mẫu vài dòng đầu

## Bước 2: Áp Dụng Pattern SQL Chuẩn
**CTE thay vì subquery lồng nhau**:
```sql
WITH monthly_revenue AS (
  SELECT date_trunc('month', order_date) AS month,
         SUM(amount) AS revenue
  FROM orders
  WHERE order_date >= '2025-01-01'
  GROUP BY 1
),
mom_growth AS (
  SELECT month, revenue,
         LAG(revenue) OVER (ORDER BY month) AS prev_month,
         (revenue - LAG(revenue) OVER (ORDER BY month))
           / NULLIF(LAG(revenue) OVER (ORDER BY month), 0) AS mom_pct
  FROM monthly_revenue
)
SELECT * FROM mom_growth;
```

**Window function thay vì self-join**:
- `ROW_NUMBER()` — first/last per group
- `LAG/LEAD` — so sánh row liền kề
- `SUM() OVER (PARTITION BY ... ORDER BY ... ROWS BETWEEN ...)` — running total
- `NTILE(4)` — phân quartile

**JOIN đúng cách**:
- INNER khi muốn rows có ở cả 2
- LEFT khi muốn giữ all bên trái
- FULL OUTER chỉ khi cần (tốn)
- Anti-join: `WHERE ... NOT IN (SELECT...)` → đổi thành `LEFT JOIN ... WHERE ... IS NULL`

## Bước 3: Tối Ưu Performance
Checklist tuning:
1. **Filter sớm** — WHERE trước JOIN khi có thể
2. **SELECT cột cụ thể** — không `SELECT *`
3. **Index** — JOIN/WHERE column có index không
4. **Partition pruning** — BigQuery/Snowflake: filter theo partition column
5. **Tránh function trên column trong WHERE** — `WHERE date_trunc('day', ts) = ...` → `WHERE ts >= ... AND ts < ...`
6. **EXISTS thay IN** với subquery lớn
7. **Materialized view** cho query lặp lại

Chạy `EXPLAIN ANALYZE` đọc:
- Seq Scan vs Index Scan
- Hash Join vs Nested Loop
- Rows estimated vs actual (sai → cần VACUUM ANALYZE)

## Bước 4: Anti-Pattern Cần Tránh
- `SELECT DISTINCT` để fix duplicate → fix JOIN thay vì che
- `OR` trong JOIN condition → split thành UNION
- Function trên indexed column trong WHERE
- Nested subquery 3+ tầng → dùng CTE
- `COUNT(*)` thay vì `COUNT(column)` khi muốn count non-null
- Không có timezone awareness khi compare timestamp

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- GitHub MCP: lưu query trong repo `analytics/queries/`, code review
- Google Drive MCP: lưu output CSV cho stakeholder không có DB access
- Notion MCP: query library + giải thích cho team
- Slack MCP: gửi kết quả query định kỳ vào channel
- Linear MCP: ticket cho mỗi query mới cần build
- WebSearch: tra documentation dialect cụ thể (BigQuery DATE_TRUNC khác Postgres)
- WebFetch: pull docs từ docs.snowflake.com, cloud.google.com/bigquery

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Chạy query BigQuery + lấy execution stats
from google.cloud import bigquery
client = bigquery.Client()
job = client.query("""
    WITH daily AS (
      SELECT DATE(order_ts) AS d, SUM(amount) AS rev
      FROM `project.dataset.orders`
      WHERE order_ts >= '2026-01-01'
      GROUP BY 1
    )
    SELECT d, rev, AVG(rev) OVER (ORDER BY d ROWS 6 PRECEDING) AS rev_7d_ma
    FROM daily ORDER BY d
""")
df = job.to_dataframe()
print(f"Bytes processed: {job.total_bytes_processed/1e9:.2f} GB")
print(f"Slot ms: {job.slot_millis}")
```

## Bước 6: Output Format
- File `.sql` có cấu trúc:
  - Header comment: mục tiêu, input, output, author, date
  - CTE từng tầng có comment giải thích
  - Inline comment cho join condition phức tạp
- File `<query_name>_explained.md` giải thích pattern dùng + lý do
- `<query_name>_sample_output.csv` 20 rows mẫu để verify
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/sql-queries/`

## Checklist Trước Khi Giao
- [ ] Query trả về đúng business question ban đầu
- [ ] Comment header rõ mục tiêu & input
- [ ] CTE đặt tên có nghĩa, không `t1`, `t2`
- [ ] Không có anti-pattern (SELECT *, function-on-column)
- [ ] EXPLAIN cho thấy dùng index/partition
- [ ] Test với edge case: NULL, 0 row, duplicate
- [ ] Sample output match expectation
- [ ] Đã review syntax phù hợp dialect đích
