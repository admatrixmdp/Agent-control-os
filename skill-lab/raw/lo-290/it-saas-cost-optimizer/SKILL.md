---
name: it-saas-cost-optimizer
description: |
  Tối ưu chi phí SaaS bằng right-sizing license: giảm seat dư, đổi plan phù hợp, đàm phán renewal, tận dụng volume discount — tiết kiệm 25-40% ngân sách SaaS.
  Kích hoạt khi người dùng nói: "tối ưu chi phí SaaS", "license rightsize", "giảm chi phí phần mềm", "SaaS cost optimization", "đàm phán renewal", "right-size seat", "giảm seat dư", "SaaS savings", "FinOps SaaS", "tối ưu license Microsoft Adobe".
  Output là Excel kế hoạch tối ưu + script email đàm phán vendor.
---

# SaaS Cost Optimizer

## Mục Tiêu
Phòng IT bị áp lực cắt giảm 20-30% chi phí mỗi năm. Skill này giúp tìm chính xác chỗ cắt mà KHÔNG ảnh hưởng năng suất — bằng data về utilization thực tế của mỗi license.

## Khi Nào Dùng
- Sắp đến mùa renewal lớn (Microsoft, Adobe, Salesforce)
- CFO yêu cầu plan cắt giảm
- Đã làm SaaS audit, giờ đến bước action
- Layoff giảm 20% NV, license thừa nhiều
- Bị vendor tăng giá đột ngột

## Bước 1: Tập Trung 5 SaaS Tốn Nhất
Quy tắc 80/20 — thường 5-10 SaaS lớn chiếm 70% chi phí:
- Microsoft 365 / Google Workspace (E3/E5 plans)
- Salesforce / HubSpot (per-seat)
- Adobe Creative Cloud
- Slack / Zoom / Teams
- GitHub / GitLab / Atlassian suite

Lấy:
- Số seat đã mua
- Số seat active 30/60/90 ngày
- Plan hiện tại
- Renewal date & price
- Multi-year discount có chưa

## Bước 2: 6 Kỹ Thuật Right-Size
**1. Cắt seat inactive 60+ ngày** — quick win, tiết kiệm 10-25%

**2. Downgrade plan**:
- M365 E5 → E3 nếu không dùng Power BI Pro, Defender, Phone System
- Salesforce Enterprise → Professional nếu team <50 và không cần advanced
- Slack Business+ → Pro nếu không cần SAML SSO (mặc dù khuyên giữ)

**3. Annual thay vì monthly** — giảm 17-20%

**4. Multi-year commit** — 3 năm thường giảm 15-25%

**5. Volume tier crossing** — đẩy số seat qua mốc 100/250/500 để được tier discount

**6. Bundle** — gộp với vendor cùng họ (Microsoft E5 vs E3+riêng Power BI)

## Bước 3: Đàm Phán Renewal
Quy trình 90-60-30 ngày:
- **T-90**: phân tích usage, lập target giảm 10-20%
- **T-60**: gửi RFP đối thủ (Google vs Microsoft, HubSpot vs Salesforce)
- **T-30**: meeting với account manager, leverage RFP để giảm giá
- **T-15**: chốt deal, signed

Câu mẫu đàm phán:
- "Chúng tôi đang đánh giá [Đối thủ X] với offer rẻ hơn 25%"
- "Utilization năm qua chỉ 65%, chúng tôi sẽ giảm seat 30%"
- "Nếu commit 3 năm, mức discount tốt nhất là gì?"
- "End of quarter rồi, có deal đặc biệt không?"

## Bước 4: Tạo SaaS FinOps Practice
Setup chu trình:
- **Monthly**: dashboard utilization, alert seat inactive
- **Quarterly**: review portfolio, kill SaaS <20% utilization
- **Annual**: full audit + renewal calendar
- **Approval flow**: SaaS mới >$500/month phải qua IT + Finance

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: dashboard tracking savings vs target
- Gmail MCP: gửi email đàm phán với vendor
- Slack MCP: alert seat inactive cho manager phòng ban
- Notion MCP: vendor management database
- Linear MCP: ticket mỗi action savings
- WebSearch: benchmark giá thị trường (G2, Capterra reviews)
- WebFetch: pull pricing page vendor để có data đàm phán

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Lấy usage Microsoft 365 để right-size
import requests
TOKEN = "..."  # Graph API token
headers = {"Authorization": f"Bearer {TOKEN}"}
# User activity 30 days
r = requests.get(
    "https://graph.microsoft.com/v1.0/reports/getOffice365ActiveUserDetail(period='D30')",
    headers=headers)
# Parse CSV, đếm user có lastActivity = null → inactive
inactive = sum(1 for row in r.text.split("\n")[1:]
               if row and row.split(",")[5] == "")
print(f"Inactive M365 users last 30d: {inactive}")
```

## Bước 6: Output Format
- File chính: `SaaS_Cost_Optimization_Plan_<YYYY>.xlsx`
  - Sheet 1: Current spend baseline
  - Sheet 2: Right-size opportunities
  - Sheet 3: Renewal calendar with target
  - Sheet 4: Savings tracker
- `Negotiation_Playbook.md` — script đàm phán mỗi vendor lớn
- Báo cáo CFO: `SaaS_Savings_Report.md` (chỉ ra số tiết kiệm cam kết vs đạt được)
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/saas-cost/`

## Checklist Trước Khi Giao
- [ ] Đã phân tích 5+ SaaS chiếm 70% chi phí
- [ ] Mỗi SaaS có 6 kỹ thuật right-size đánh giá
- [ ] Target savings: ≥20% tổng SaaS spend
- [ ] Renewal calendar 12 tháng có action 90-60-30
- [ ] Script đàm phán cho 3 vendor lớn nhất
- [ ] FinOps process monthly đã setup
- [ ] Approval flow SaaS mới đã ban hành
- [ ] CFO đồng ý target và timeline
