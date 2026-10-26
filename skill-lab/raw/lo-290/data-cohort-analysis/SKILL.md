---
name: data-cohort-analysis
description: |
  Phân tích cohort retention & revenue: nhóm khách hàng theo tháng acquisition, đo % quay lại / chi tiêu các tháng sau — phát hiện chất lượng user theo từng nguồn/chiến dịch.
  Kích hoạt khi người dùng nói: "phân tích cohort", "cohort analysis", "retention cohort", "revenue cohort", "phân tích giữ chân", "user retention", "LTV cohort", "tỷ lệ quay lại theo nhóm", "cohort heatmap", "weekly cohort".
  Output là Excel/Sheets heatmap + SQL + insight Markdown.
---

# Cohort Retention & Revenue Analysis

## Mục Tiêu
Cohort analysis là cách tốt nhất để biết "chiến dịch tháng 3 hút khách có chất lượng không" — không bị bias bởi growth. Skill này build cohort heatmap chuẩn, tự cập nhật, kèm insight kinh doanh.

## Khi Nào Dùng
- Sản phẩm SaaS/subscription cần biết retention thực tế
- E-commerce cần biết LTV theo nguồn lead
- Đánh giá chất lượng user theo từng chiến dịch marketing
- Trước khi báo cáo investor (Series A/B cần retention curve)
- Phát hiện sản phẩm "leaky bucket" — vào nhiều nhưng rớt sớm

## Bước 1: Định Nghĩa Cohort
Quyết định 4 thông số:
- **Cohort định nghĩa bởi**: First purchase / Signup / First payment / First subscription
- **Cohort size unit**: Day / Week / Month / Quarter
- **Event đo retention**: Login / Purchase / Active session
- **Time horizon**: 6 tháng / 12 tháng / 24 tháng

Ví dụ: "Cohort theo tháng signup, đo retention bằng có purchase trong tháng đó, theo dõi 12 tháng".

## Bước 2: Query Cohort Table
SQL chuẩn (BigQuery/PostgreSQL):
```sql
WITH cohorts AS (
  SELECT customer_id,
         DATE_TRUNC(MIN(order_date), MONTH) AS cohort_month
  FROM orders
  GROUP BY customer_id
),
activity AS (
  SELECT o.customer_id,
         c.cohort_month,
         DATE_TRUNC(o.order_date, MONTH) AS active_month,
         DATE_DIFF(DATE_TRUNC(o.order_date, MONTH),
                   c.cohort_month, MONTH) AS month_number,
         SUM(o.amount) AS revenue
  FROM orders o
  JOIN cohorts c USING(customer_id)
  GROUP BY 1, 2, 3, 4
),
cohort_sizes AS (
  SELECT cohort_month, COUNT(DISTINCT customer_id) AS cohort_size
  FROM cohorts GROUP BY 1
)
SELECT a.cohort_month, a.month_number,
       COUNT(DISTINCT a.customer_id) AS active_users,
       SUM(a.revenue) AS revenue,
       COUNT(DISTINCT a.customer_id) * 1.0 / cs.cohort_size AS retention_rate
FROM activity a
JOIN cohort_sizes cs USING(cohort_month)
GROUP BY 1, 2, cs.cohort_size
ORDER BY 1, 2;
```

## Bước 3: Build Heatmap
Pivot table:
- **Hàng**: cohort_month
- **Cột**: month_number (0, 1, 2, ... 12)
- **Giá trị**: retention_rate (hoặc revenue per user)

Heatmap màu: 100% xanh đậm → 0% trắng.

Đọc heatmap:
- **Đọc ngang** một hàng — cohort này hành xử ra sao theo thời gian
- **Đọc dọc** một cột — cùng age, các cohort khác nhau ra sao
- **Đọc chéo** — tháng cụ thể nào tất cả cohort spike (event/holiday)

## Bước 4: Tách Cohort Theo Segment
Phân tích sâu hơn — tách cohort theo:
- **Acquisition channel** (FB Ads / Google / Organic / Referral)
- **First product category** (mua áo first vs giày first)
- **First order value** (LowAOV / MidAOV / HighAOV)
- **Region** (HCM / HN / Tỉnh khác)

So sánh retention curve giữa các segment để biết nguồn nào đáng đầu tư hơn.

Ví dụ phát hiện: Facebook Ads có CAC thấp nhưng retention 3 tháng = 15%, Google Ads CAC cao gấp đôi nhưng retention 35% → Google Ads thực ra rẻ hơn LTV.

## Bước 5: Tính LTV Từ Cohort
LTV cumulative = SUM(revenue per user) qua các month_number.

LTV curve giúp:
- Biết khi nào user "trả lại CAC" → CAC payback period
- Set max bid cho ads (CAC < 50% LTV 12 tháng)
- Project revenue tương lai

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: pivot heatmap, conditional formatting
- GitHub MCP: lưu SQL trong analytics repo
- Slack MCP: gửi cohort report monthly vào #growth
- Notion MCP: page "Cohort tháng X" có insight
- Linear MCP: ticket experiment cải thiện retention
- WebSearch: benchmark retention rate theo ngành (Shopify, Stripe Atlas)
- WebFetch: pull data Mixpanel/Amplitude qua API

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tạo heatmap PNG để gửi báo cáo
import pandas as pd, seaborn as sns, matplotlib.pyplot as plt
df = pd.read_csv("cohort.csv")
pivot = df.pivot(index="cohort_month",
                 columns="month_number",
                 values="retention_rate")
plt.figure(figsize=(14, 8))
sns.heatmap(pivot, annot=True, fmt=".1%", cmap="YlGnBu",
            cbar_kws={"label": "Retention %"})
plt.title("Monthly Cohort Retention")
plt.savefig("cohort_heatmap.png", dpi=200, bbox_inches="tight")
```

## Bước 7: Output Format
- `Cohort_Analysis_<YYYYMM>.xlsx`
  - Sheet 1: Raw cohort data
  - Sheet 2: Retention heatmap
  - Sheet 3: Revenue cohort heatmap
  - Sheet 4: LTV curve
  - Sheet 5: Segment comparison
- `cohort_query.sql`
- `Cohort_Insights.md` — top 5 insight + recommendation
- `cohort_heatmap.png` cho slide
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/cohort/`

## Checklist Trước Khi Giao
- [ ] Định nghĩa cohort + retention event rõ ràng
- [ ] Có ≥6 cohort liên tiếp để thấy pattern
- [ ] Heatmap chuẩn (cohort dọc, age ngang)
- [ ] Tách ít nhất 1 segment (channel/category)
- [ ] LTV cumulative + CAC payback có tính
- [ ] Top 3 insight rút ra có actionable
- [ ] So sánh với benchmark ngành
- [ ] Schedule refresh tự động hàng tháng
