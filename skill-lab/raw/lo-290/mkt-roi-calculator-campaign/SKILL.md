---
name: mkt-roi-calculator-campaign
description: |
  Tính ROI/LTV-CAC cho từng campaign marketing của doanh nghiệp Việt Nam. Phân tích lãi/lỗ, payback period, kênh nào nên tăng/giảm. Kích hoạt khi người dùng nói: "tính ROI campaign", "ROI marketing", "LTV CAC", "payback campaign", "đo lường hiệu quả campaign", "marketing ROI", "calculate ROAS", "lãi lỗ campaign". Output là Excel calc + báo cáo HTML.
---

# ROI Calculator Campaign — LTV/CAC

## Mục Tiêu
Sau mỗi campaign biết rõ thực sự lời/lỗ bao nhiêu sau khi trừ COGS + chi phí ads + nhân sự + payback bao lâu, tránh "ROAS đẹp nhưng vẫn lỗ".

## Khi Nào Dùng
- Đánh giá campaign vừa kết thúc
- Báo cáo cho CEO/CFO
- Quyết định scale/kill campaign
- So sánh ROI giữa kênh
- Tính LTV theo cohort

## Bước 1: Thu Thập Số Liệu
Hỏi:
1. Campaign + thời gian
2. Total spend (ads + KOL + creative + nhân sự)
3. Số đơn / khách hàng mới
4. Doanh thu trực tiếp từ campaign
5. AOV / ARPU
6. Margin % (sau COGS, shipping, hoàn trả)
7. Tần suất mua lại (lần/năm)
8. Average customer lifespan (tháng)

## Bước 2: Tính 6 Chỉ Số Cốt Lõi
- **CAC** = Total spend / Số KH mới
- **ROAS** = Doanh thu / Ads spend
- **Net Margin** = (Doanh thu × margin%) - Total spend
- **CPA blended** = Total spend / Tổng người mua
- **LTV** = AOV × frequency × lifespan × margin%
- **LTV/CAC** ratio (mục tiêu >3)
- **Payback period** = CAC / (Monthly revenue × margin%)

## Bước 3: Phân Tích & Đề Xuất
Mỗi campaign chấm:
- LTV/CAC >3 + payback <12 tháng → SCALE
- LTV/CAC 1-3 + payback 12-24 tháng → TỐI ƯU
- LTV/CAC <1 → KILL

So sánh giữa kênh, sản phẩm, segment. Đề xuất reallocation.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Meta Ads MCP / Google Ads MCP: pull spend
- Shopify/CRM MCP: pull revenue + customer
- Google Sheets MCP: master ROI tracker
- Slack MCP: alert campaign lỗ
- Notion MCP: report archive

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tính LTV theo cohort
import pandas as pd
df = pd.read_csv('orders.csv', parse_dates=['order_date'])
df['cohort'] = df.groupby('customer_id')['order_date'].transform('min').dt.to_period('M')
df['month_since'] = ((df['order_date'].dt.to_period('M') - df['cohort']).apply(lambda x: x.n))
ltv = df.groupby('cohort')['revenue'].sum() / df.groupby('cohort')['customer_id'].nunique()
print(ltv)
```

## Bước 5: Output Format
- File `.xlsx` calculator có input động
- Báo cáo HTML 1 trang per campaign
- Dashboard tổng cộng campaign
- Action list (scale/optimize/kill)
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ spend trực tiếp + gián tiếp
- [ ] Margin % đã trừ COGS + return
- [ ] LTV tính theo cohort thật
- [ ] Payback period rõ
- [ ] So sánh giữa kênh
- [ ] Action SCALE/OPTIMIZE/KILL
