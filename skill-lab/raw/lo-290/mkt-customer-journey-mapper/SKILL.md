---
name: mkt-customer-journey-mapper
description: |
  Vẽ bản đồ hành trình khách hàng (Awareness → Consideration → Purchase → Retention → Loyalty) cho doanh nghiệp Việt Nam với touchpoint, emotion, gap và action. Kích hoạt khi người dùng nói: "map customer journey", "vẽ hành trình khách hàng", "customer journey map", "touchpoint khách hàng", "trải nghiệm khách hàng", "hành trình mua sắm", "CX mapping", "customer experience map". Output là HTML/PDF visual map + Excel touchpoint table.
---

# Map Hành Trình Khách Hàng

## Mục Tiêu
Hiểu khách hàng đi qua đâu, cảm xúc thế nào, ở đâu drop-off, từ đó tối ưu từng touchpoint để tăng CR và NPS.

## Khi Nào Dùng
- Đang có CR thấp không hiểu lý do
- Mở rộng kênh mới (offline ↔ online)
- Sau khi có persona
- Audit CX định kỳ năm
- Trước khi triển khai CRM/automation

## Bước 1: Chọn Persona & Scenario
Hỏi:
1. Persona target (chọn từ persona đã có)
2. Scenario (mua lần đầu / repeat / churn / upgrade)
3. Sản phẩm/dịch vụ
4. Kênh đang có

## Bước 2: Vẽ 5 Stage
| Stage | Awareness | Consideration | Purchase | Retention | Loyalty |
|---|---|---|---|---|---|
| Goal | KH nhận biết | KH so sánh | KH quyết định | KH dùng lại | KH giới thiệu |
| Touchpoint | FB ads, SEO | Website, review | Checkout, sales | Onboarding, support | Loyalty, referral |
| Action KH | Click ads | So sánh giá | Đặt hàng | Mở box, dùng | Share, ref |
| Emotion | Tò mò | Hoài nghi | Lo lắng | Hứng thú | Tự hào |
| Pain | Không tin brand | Giá đắt | Form khó | Không biết dùng | Quên brand |
| Opportunity | Social proof | Testimonial | Live chat | Tutorial video | Loyalty perks |

## Bước 3: Xác Định Gap + Action
Tìm 5-10 gap lớn nhất (vd: "checkout drop 60%", "không có email welcome"). Mỗi gap đề xuất 1-3 action cụ thể, ưu tiên theo impact x effort.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- GA4 MCP: data drop-off funnel
- Hotjar/FullStory MCP: heatmap behavior
- CRM MCP: data deal stage
- Notion MCP: lưu journey map
- Figma/Miro MCP: visualize

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Pull funnel data từ GA4
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest
client = BetaAnalyticsDataClient()
req = RunReportRequest(property='properties/123456',
  dimensions=[{'name':'eventName'}],
  metrics=[{'name':'eventCount'}],
  date_ranges=[{'start_date':'30daysAgo','end_date':'today'}])
res = client.run_report(req)
```

## Bước 5: Output Format
- File HTML/PDF visual map 5 stage có icon, color
- File `.xlsx` touchpoint table chi tiết
- Action priority matrix (impact x effort)
- Owner + deadline từng action
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 5 stage đầy đủ
- [ ] Emotion curve rõ
- [ ] Gap có data backup
- [ ] Action có owner + ETA
- [ ] Đã review với product/sales/CS
- [ ] Visual đẹp dễ hiểu
