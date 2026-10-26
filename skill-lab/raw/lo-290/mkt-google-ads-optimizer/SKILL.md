---
name: mkt-google-ads-optimizer
description: |
  Tối ưu Google Ads cho doanh nghiệp Việt Nam — quản lý keyword, negative keyword, bid, Quality Score và đề xuất action tuần. Tự động phát hiện search term wasted spend và đề xuất pause/add negative. Kích hoạt khi người dùng nói: "tối ưu Google Ads", "quản lý GG Ads", "audit Google Ads", "negative keyword Google", "tối ưu bid GG Ads", "quality score Google", "search term report", "tối ưu CPA Google Ads". Output là Excel báo cáo + HTML dashboard.
---

# Tối Ưu Google Ads — Keyword, Negative, Bid

## Mục Tiêu
Giảm 15-30% chi phí lãng phí (search term không liên quan, keyword Quality Score thấp) đồng thời tăng CR/ROAS thông qua tối ưu liên tục theo dữ liệu hàng tuần.

## Khi Nào Dùng
- Tài khoản đã chạy >2 tuần, có data
- CPA tăng đột ngột không rõ lý do
- Trước khi scale ngân sách
- Audit account nhận về từ agency
- Tối ưu định kỳ tuần/tháng

## Bước 1: Kết Nối Account
Hỏi: Customer ID, loại campaign (Search/Shopping/PMax/Display), KPI mục tiêu (CPA/ROAS/Search Lost IS), khoảng thời gian phân tích.

## Bước 2: Phân Tích 5 Khu Vực
1. **Search Term Report**: tìm term có CR=0, spend > 200k → add negative
2. **Keyword Performance**: keyword QS<5 → review ad copy/LP; keyword CTR>5% + CR cao → tăng bid
3. **Ad Copy**: pause ad CTR <50% trung bình adgroup
4. **Audience**: phân tích remarketing list, in-market segment
5. **Bid Strategy**: tCPA/tROAS có đạt target?

## Bước 3: Sinh Action List
Mỗi action ghi rõ: WHAT (làm gì), WHERE (cấp nào - campaign/adgroup/keyword), WHY (lý do data), EXPECTED IMPACT.

Ví dụ:
- Pause keyword "khóa học miễn phí" - CR=0 sau 50 click, save 1.2tr/tháng
- Thêm negative -"free", -"miễn phí" cấp account
- Tăng bid keyword "đào tạo AI doanh nghiệp" +20% - CR 8% > target

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Ads MCP / API connector: kéo report, add negative, đổi bid
- Google Sheets MCP: log thay đổi để rollback nếu cần
- GA4 MCP: cross-check landing page CR
- WebSearch: tra benchmark CPC ngành VN
- Slack MCP: thông báo daily

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Kéo search term report Google Ads API
from google.ads.googleads.client import GoogleAdsClient
client = GoogleAdsClient.load_from_storage('google-ads.yaml')
ga = client.get_service('GoogleAdsService')
query = """SELECT search_term_view.search_term, metrics.cost_micros,
  metrics.conversions FROM search_term_view
  WHERE segments.date DURING LAST_30_DAYS"""
for row in ga.search(customer_id='1234567890', query=query):
    print(row.search_term_view.search_term, row.metrics.cost_micros/1e6)
```

## Bước 5: Output Format
- File `.xlsx`:
  - Sheet 1: Search term cần add negative
  - Sheet 2: Keyword pause/tăng bid
  - Sheet 3: Ad copy cần đổi
  - Sheet 4: Tổng action + expected save
- HTML dashboard tóm tắt cho sếp
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ 3 cấp campaign/adgroup/keyword
- [ ] Số tiền tiết kiệm ước tính rõ
- [ ] Mỗi action có data minh chứng
- [ ] Có negative list cấp account
- [ ] Đã đối chiếu GA4 conversion
- [ ] Có lịch review tuần tiếp theo
