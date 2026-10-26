---
name: data-customer-segmentation
description: |
  Phân khúc khách hàng bằng RFM (Recency, Frequency, Monetary) để xác định nhóm VIP, có nguy cơ churn, mới, cần kích hoạt — kèm chiến lược marketing tự động hoá cho mỗi segment.
  Kích hoạt khi người dùng nói: "phân khúc khách hàng", "customer segmentation", "RFM analysis", "phân nhóm KH", "khách hàng VIP", "khách hàng churn", "lifecycle marketing", "phân loại khách", "tệp khách hàng vàng", "segment marketing".
  Output là Excel/CSV phân segment + SQL + chiến lược marketing Markdown.
---

# Customer Segmentation (RFM) Analyzer

## Mục Tiêu
80% doanh thu đến từ 20% khách. Skill này dùng RFM phân khúc khách hàng thành 8-11 nhóm có hành động cụ thể — VIP, At Risk, Cannot Lose, Newbie... giúp marketing tập trung đúng người, ngân sách hiệu quả gấp 3-5 lần.

## Khi Nào Dùng
- Có >500 khách hàng + đủ 12 tháng lịch sử transaction
- Marketing đang gửi blast email/SMS giống nhau cho tất cả
- Cần tối ưu chi phí CRM (giảm spam, tăng conversion)
- Lên kế hoạch loyalty program / tier rewards
- Identify churners trước khi họ thực sự churn

## Bước 1: Chuẩn Bị Data Đầu Vào
Cần tối thiểu:
- `customer_id`
- `order_date`
- `order_amount`

Tùy chọn:
- `customer_email`, `customer_phone`
- `product_category`, `acquisition_channel`
- `first_order_date`

Yêu cầu data: ít nhất 12 tháng để Recency có nghĩa.

## Bước 2: Tính 3 Chỉ Số RFM
**Recency (R)**: số ngày từ lần mua cuối đến hôm nay (càng nhỏ càng tốt)
**Frequency (F)**: tổng số order trong 12 tháng
**Monetary (M)**: tổng giá trị 12 tháng

SQL:
```sql
WITH rfm_raw AS (
  SELECT customer_id,
         DATEDIFF(CURRENT_DATE, MAX(order_date)) AS recency,
         COUNT(*) AS frequency,
         SUM(order_amount) AS monetary
  FROM orders
  WHERE order_date >= DATEADD(month, -12, CURRENT_DATE)
  GROUP BY customer_id
)
SELECT *,
  NTILE(5) OVER (ORDER BY recency DESC) AS r_score,  -- 5 = recent
  NTILE(5) OVER (ORDER BY frequency) AS f_score,
  NTILE(5) OVER (ORDER BY monetary) AS m_score
FROM rfm_raw;
```

## Bước 3: Map RFM Score → Segment
Dùng matrix 11 segment chuẩn:

| Segment | R | F | M | Mô tả | Hành động |
|---------|---|---|---|-------|-----------|
| Champions | 4-5 | 4-5 | 4-5 | KH ngon nhất | VIP perks, refer-a-friend |
| Loyal | 3-5 | 3-5 | 3-5 | KH trung thành | Upsell, loyalty tier |
| Potential Loyalist | 4-5 | 1-2 | * | Mới mua, ít lần | Onboarding email series |
| New Customers | 5 | 1 | 1 | Mới hôm qua | Welcome + 2nd purchase incentive |
| Promising | 3-4 | 1 | 1 | Có tiềm năng | Engagement campaign |
| Need Attention | 3 | 2-3 | 2-3 | Trung bình | Survey, personalization |
| About to Sleep | 2-3 | 1-2 | 1-2 | Giảm mua | Reactivation offer |
| At Risk | 1-2 | 2-5 | 2-5 | Từng tốt, đang lơ | Win-back: discount cao |
| Cannot Lose | 1-2 | 4-5 | 4-5 | VIP đang biến mất | Personal call from manager |
| Hibernating | 1-2 | 1-2 | 1-2 | Hết nhiệt | Last-chance offer |
| Lost | 1 | 1 | 1 | Coi như mất | Stop marketing để tiết kiệm |

## Bước 4: Chiến Lược Marketing Cho Mỗi Segment
Mỗi segment cần:
- **Channel** ưu tiên (email/SMS/Zalo/call/quảng cáo retargeting)
- **Message tone** (cảm ơn / FOMO / xin lỗi / quan tâm)
- **Offer** (no offer / 5% / 15% / personal gift)
- **Frequency** (weekly / monthly / quarterly)
- **Success metric** (open rate / conversion / reactivation %)

Ví dụ "At Risk" — channel: email + SMS, tone: "Chúng tôi nhớ bạn", offer: 20% off, frequency: 3 email trong 14 ngày, metric: % return purchase trong 30 ngày.

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: export segment list cho team marketing
- Gmail MCP: gửi campaign test cho mẫu nhỏ trước
- Slack MCP: notify segment shifts hàng tuần
- Notion MCP: playbook chiến lược mỗi segment
- Linear MCP: ticket cho mỗi campaign
- WebSearch: benchmark conversion rate theo industry
- WebFetch: pull data từ Shopify/WooCommerce orders

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Đẩy segment vào Mailchimp/Customer.io làm audience riêng
import pandas as pd, requests
df = pd.read_csv("rfm_segments.csv")
champions = df[df.segment == "Champions"]
# Mailchimp API
for _, row in champions.iterrows():
    requests.post(
        f"https://us1.api.mailchimp.com/3.0/lists/LIST_ID/members",
        auth=("any", "API_KEY"),
        json={"email_address": row["email"],
              "status": "subscribed",
              "tags": ["Champion", "RFM_2026_05"]})
```

## Bước 6: Output Format
- `RFM_Segmentation_<YYYYMM>.xlsx`
  - Sheet 1: Raw RFM scores per customer
  - Sheet 2: Segment summary (count, avg revenue, % of total)
  - Sheet 3: Action playbook
  - Sheet 4: Migration matrix (so với kỳ trước, ai chuyển segment)
- `rfm_query.sql` — query tái tạo được
- `Segment_Strategy.md` — chiến lược chi tiết mỗi segment
- `Campaign_Briefs/<segment>.md` — brief gửi marketing
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/segmentation/`

## Checklist Trước Khi Giao
- [ ] Data ≥12 tháng, ≥500 KH
- [ ] R/F/M tính đúng, có NTILE 5
- [ ] 11 segment có count + % rõ ràng
- [ ] Migration matrix so với kỳ trước
- [ ] Mỗi segment có strategy + offer cụ thể
- [ ] A/B test plan cho 2-3 segment lớn
- [ ] Refresh schedule (monthly hoặc weekly)
- [ ] Marketing team đã ký action plan
