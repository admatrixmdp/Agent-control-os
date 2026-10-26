---
name: mkt-conversion-funnel-audit
description: |
  Audit funnel conversion (TOFU/MOFU/BOFU) cho doanh nghiệp Việt Nam — phân tích từng tầng, chỉ ra drop-off, đề xuất action ưu tiên. Kích hoạt khi người dùng nói: "audit funnel", "phân tích conversion funnel", "TOFU MOFU BOFU", "audit drop off", "tối ưu funnel", "phễu bán hàng", "marketing funnel audit", "phân tích phễu". Output là HTML dashboard + Excel breakdown.
---

# Audit Funnel Conversion TOFU/MOFU/BOFU

## Mục Tiêu
Xác định chính xác tầng nào của funnel đang "rò rỉ" nặng nhất, cho phép team tập trung 80% nguồn lực vào fix 20% vấn đề có impact cao nhất.

## Khi Nào Dùng
- Doanh thu chững nhưng traffic tăng
- CAC tăng đột ngột
- Trước khi scale ngân sách
- Audit định kỳ quý
- Sau khi launch sản phẩm mới

## Bước 1: Map Funnel Đầy Đủ
Hỏi:
1. Loại business (ecom/SaaS/khóa học/services)
2. Kênh traffic chính
3. Stack tracking (GA4, FB Pixel, CRM)

Vẽ funnel chuẩn:
- TOFU: Ad impression → Click → Visit
- MOFU: Visit → Lead (form/cart)
- BOFU: Lead → Customer
- Post: Customer → Repeat → Advocate

Mỗi tầng có CR mục tiêu benchmark (vd: visit→lead 5%, lead→customer 20%).

## Bước 2: Kéo Số & Tính CR Từng Tầng
Dùng GA4 + Ads platform + CRM lấy số 30 ngày qua. Tính:
- CR mỗi tầng
- So với benchmark ngành
- So với 30 ngày trước
- Theo segment (device, channel, campaign)

## Bước 3: Chấm Drop-off + Đề Xuất Action
Tầng nào CR <50% benchmark = critical. Đề xuất action theo nguyên nhân:
- TOFU yếu: creative/audience/targeting
- MOFU yếu: landing page/social proof/offer
- BOFU yếu: trust/checkout/payment options
- Post yếu: onboarding/support/loyalty

Mỗi action có expected lift + effort + owner.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- GA4 MCP: funnel exploration report
- Meta Ads MCP: impression → click → conversion
- CRM MCP: lead → customer rate
- Hotjar MCP: heatmap drop-off
- Notion MCP: action board

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Pull funnel report từ GA4 Data API
from google.analytics.data_v1beta import BetaAnalyticsDataClient
client = BetaAnalyticsDataClient()
res = client.run_report({
  'property':'properties/12345',
  'dimensions':[{'name':'eventName'}],
  'metrics':[{'name':'eventCount'}],
  'date_ranges':[{'start_date':'30daysAgo','end_date':'today'}],
  'dimension_filter':{'filter':{'field_name':'eventName',
    'in_list_filter':{'values':['page_view','add_to_cart','begin_checkout','purchase']}}}})
```

## Bước 5: Output Format
- File HTML dashboard funnel visual (chart hình phễu)
- File `.xlsx` chi tiết số liệu từng tầng + segment
- Top 10 action priority
- Roadmap fix 30/60/90 ngày
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Funnel đầy đủ 4 tầng
- [ ] So sánh benchmark + period
- [ ] Identify top 3 leak
- [ ] Action có expected impact
- [ ] Có owner + deadline
- [ ] Dashboard visual đẹp
