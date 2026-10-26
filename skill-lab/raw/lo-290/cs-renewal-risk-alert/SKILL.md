---
name: cs-renewal-risk-alert
description: |
  Hệ thống cảnh báo rủi ro không gia hạn (renewal risk) cho B2B/SaaS — gom signal (usage drop, ticket negative, champion leave), score risk, action play. Dùng skill này khi người dùng yêu cầu: "renewal risk", "churn prediction", "early warning churn", "cảnh báo gia hạn", "B2B renewal management", "save-the-deal playbook", "tín hiệu khách rời đi", "retention alert". Output là Excel signal matrix + Python script + email playbook.
---

# CS Renewal Risk Alert System

## Mục Tiêu
Phát hiện sớm 60-90 ngày trước hết hạn KH nào có rủi ro không gia hạn — dựa vào signal usage, support, stakeholder — để CSM can thiệp đúng lúc, tăng renewal rate từ 70% → 90%+.

## Khi Nào Dùng
- B2B/SaaS có hợp đồng năm/quý
- Renewal rate < 85%, không hiểu vì sao
- Phát hiện muộn → đã không kịp save
- Cần KPI CSM team
- Sau khi có 6+ tháng dữ liệu usage

## Bước 1: Liệt Kê 10+ Signal Rủi Ro
| Signal | Trọng số | Ngưỡng |
|---|---|---|
| Login giảm > 50% so 30 ngày trước | 20 | Yes/No |
| Active users giảm > 30% | 15 | Yes/No |
| Feature adoption đứng yên 60 ngày | 10 | Yes/No |
| Ticket negative tăng | 15 | > 3 ticket/tháng |
| CSAT < 3/5 trong khảo sát gần nhất | 10 | < 3 |
| Champion (người đề xuất mua) rời công ty | 20 | LinkedIn change |
| Không tham gia QBR | 5 | Miss 2 QBR liên tiếp |
| Giảm seats / downgrade plan | 10 | Yes/No |
| Yêu cầu xuất data | 15 | Export request |
| Mention competitor trong ticket | 10 | Yes/No |

**Risk Score** = sum trọng số signal hit / 130 × 100

- Score 0-30: Healthy
- 31-60: At Risk
- 61-100: Critical (cần CEO/Sales tham gia save)

## Bước 2: Save-The-Deal Playbook
Theo level risk:
- **At Risk (31-60)**:
  - CSM call 1-1 trong 7 ngày
  - Diagnostic: vì sao? thiếu gì?
  - Đề xuất training, sponsor session
- **Critical (61-100)**:
  - Escalate Head of CS + Sales lead
  - Meeting với sponsor cấp cao của KH
  - Custom proposal: giảm giá / mở rộng dịch vụ / pause plan
  - Nếu không cứu được: graceful offboarding để KH quay lại sau

## Bước 3: Renewal Timeline 90/60/30 Ngày
- **T-90**: chạy risk scan, CSM bắt đầu engage
- **T-60**: renewal call với champion, gửi ROI report
- **T-45**: gửi proposal renewal + upsell
- **T-30**: legal review hợp đồng
- **T-15**: ký gia hạn
- **T-0**: chuyển post-renewal celebration

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets: bảng renewal pipeline + risk score
- Slack MCP: alert real-time #cs-renewals khi score nhảy lên Critical
- Gmail MCP: gửi ROI report tự động T-60
- Google Calendar MCP: book renewal call T-90
- WebSearch: LinkedIn để check champion job change
- Linear/Notion MCP: tạo task save-the-deal

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Daily renewal risk scan + alert
import requests
from datetime import datetime, timedelta
H = {"Authorization": "Bearer TOKEN"}
SIGNALS_WEIGHTS = {"login_drop": 20, "ticket_neg": 15, "champion_left": 20, ...}
def scan():
    customers = requests.get("https://api/customers?renewal_in=90d", headers=H).json()
    for c in customers:
        signals = check_signals(c)
        score = sum(SIGNALS_WEIGHTS[s] for s in signals if signals[s]) / 130 * 100
        if score > 60:
            create_task(c["csm"], "Critical renewal", c["id"])
            slack_alert(c, score, signals)
```

## Bước 5: Output Format
- **Excel `Renewal_Pipeline.xlsx`**:
  - Sheet KH sắp hết hạn 90 ngày tới
  - Sheet Signal matrix
  - Sheet Save plan
- **Markdown playbook** `SaveTheDeal.md`
- **Slack alert template**
- **Email proposal renewal** + ROI report template
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-renewal-risk-alert/output/`

## Checklist Trước Khi Giao
- [ ] Tối thiểu 8 signal có data source
- [ ] Risk score công thức minh bạch
- [ ] Timeline 90/60/30 có action mỗi mốc
- [ ] Save-the-deal playbook theo level
- [ ] Alert tự động vào Slack/email
- [ ] Có KPI renewal rate đo hàng quý
