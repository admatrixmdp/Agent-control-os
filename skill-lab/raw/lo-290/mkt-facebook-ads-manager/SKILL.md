---
name: mkt-facebook-ads-manager
description: |
  Quản lý tài khoản Facebook/Meta Ads cho doanh nghiệp Việt Nam và sinh báo cáo CPM/CTR/CPA/ROAS hàng ngày/tuần. Tự động đề xuất tối ưu (tăng/giảm budget, pause adset kém, scale ads tốt). Kích hoạt khi người dùng nói: "quản lý Facebook Ads", "báo cáo FB Ads", "tối ưu Meta Ads", "phân tích CPM CTR", "ROAS Facebook", "scale ads FB", "audit tài khoản Meta", "báo cáo quảng cáo FB". Output là HTML dashboard + action list.
---

# Quản Lý Facebook/Meta Ads + Báo Cáo

## Mục Tiêu
Tiết kiệm 5-10h/tuần cho media buyer bằng cách tự động kéo data, phân tích bất thường, đưa action ngay (pause/scale/duplicate) thay vì phải mở Ads Manager soi từng adset.

## Khi Nào Dùng
- Báo cáo hàng ngày cho sếp/agency
- Tối ưu khi CPA tăng đột ngột
- Trước khi scale budget x2-x5
- Audit tài khoản nhận về từ agency cũ
- Quản lý nhiều account cùng lúc

## Bước 1: Kết Nối Tài Khoản
Hỏi:
1. Ad Account ID
2. Khoảng thời gian phân tích (3/7/14/30 ngày)
3. KPI mục tiêu (CPA, ROAS, CPL)
4. Ngưỡng cảnh báo (vd CPA > 200k là red)
5. Mục tiêu campaign (Sales/Lead/Traffic/Awareness)

## Bước 2: Kéo Dữ Liệu Và Tính Toán
Lấy metric cấp Campaign / Adset / Ad:
- Spend, Impression, Reach, CPM
- Link Click, CTR, CPC
- Conversion, CPA, ROAS
- Frequency, Relevance Score
- Hook rate (3s view / impression)
- Hold rate (15s view / 3s view)

## Bước 3: Phân Tích Và Đề Xuất Action
Quy tắc:
- CTR < 0.8% + Freq > 3 → đổi creative
- CPA > 2x KPI mục tiêu sau 3 ngày → pause adset
- ROAS > 3.0 + spend < 50% budget → scale x1.5
- Hook rate < 20% → đổi hook 3s đầu
- Có 2 adset trùng audience → tắt 1

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Meta Ads MCP / Facebook Marketing API connector: kéo insight, pause/scale ad
- Google Sheets MCP: đẩy báo cáo daily
- Slack MCP: gửi cảnh báo khi CPA vượt ngưỡng
- WebSearch: tra benchmark CPM ngành
- Google Drive MCP: lưu báo cáo PDF/HTML

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Kéo insight Facebook Ads API
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
FacebookAdsApi.init(access_token=TOKEN)
acc = AdAccount('act_123456')
fields = ['campaign_name','spend','impressions','ctr','cpm','actions']
params = {'level':'campaign','date_preset':'last_7d'}
insights = acc.get_insights(fields=fields, params=params)
```

## Bước 5: Output Format
- File HTML dashboard có:
  - KPI tổng quan (spend, ROAS, CPA, CTR)
  - Bảng campaign sorted theo ROAS
  - Top 5 ads tốt nhất + Top 5 kém nhất
  - Action list 10 mục cụ thể (pause/scale/test)
- File `.xlsx` raw data
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ metric campaign/adset/ad
- [ ] So sánh với 7 ngày trước (delta %)
- [ ] Có action list ưu tiên
- [ ] Cảnh báo red/yellow/green rõ
- [ ] Có gợi ý budget reallocation
- [ ] Đã sync Sheet hoặc Slack
