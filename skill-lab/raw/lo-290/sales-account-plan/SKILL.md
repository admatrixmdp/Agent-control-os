---
name: sales-account-plan
description: |
  Tạo Account Plan chiến lược cho KH lớn (top 10-20) gồm hoàn cảnh, white space, stakeholder map, plan 1-3-5 năm. Trigger phrases: "account plan", "kế hoạch khách hàng lớn", "strategic account plan", "plan top KH", "kế hoạch tài khoản chiến lược", "1-3-5 năm account", "white space account", "account growth plan", "plan key account", "lập plan KH lớn". Output là Docx/PDF account plan 8-12 trang + Excel white space.
---

# Strategic Account Plan (1-3-5 Year)

## Mục Tiêu
Tạo plan chiến lược cho 10-20 KH lớn đóng góp >60% revenue, mapping toàn bộ org chart, white space, đối thủ, milestone 1-3-5 năm để AE/CSM align team execute.

## Khi Nào Dùng
- Top 20 KH chiếm >60% revenue
- KH enterprise có nhiều BU/region
- Sau win deal lớn cần plan growth
- Khi assign Strategic Account Manager mới
- Annual planning kickoff

## Bước 1: Account Overview (1 trang)
- Company info: legal, HQ, BU, geo, revenue, employee
- Current ARR + product mix + tier
- Champion + Economic Buyer + Sponsor
- 3 wins + 3 challenges 12 tháng qua

## Bước 2: White Space Analysis (2 trang)
Mapping:
- BU/region/persona đã mua vs chưa mua
- Sản phẩm đang dùng vs chưa dùng
- Use case đang triển khai vs có thể mở rộng
- Ngân sách KH allocate cho category (ước lượng)
- Đối thủ đang chiếm phần nào (vs mình)

Output: Matrix BU × Product, mark green (own), yellow (compete), red (lose to competitor), white (open).

## Bước 3: Stakeholder Map (1 trang)
Vẽ org chart 20-30 người:
- Title, role
- Quan hệ với mình: Champion / Supporter / Neutral / Skeptic / Blocker
- Mức quan hệ: Strong / Moderate / Weak / None
- Plan tăng quan hệ: who-when-how

## Bước 4: 1-3-5 Year Plan (3 trang)

**Year 1 (specific)**:
- Q1-Q4 milestone
- Expansion target (ARR uplift)
- Risk mitigation
- Owner + budget

**Year 2-3 (directional)**:
- Geo/BU expansion
- New product introduction
- Joint innovation (co-marketing, case study)

**Year 5 (vision)**:
- Strategic partnership level
- Becoming reference customer
- Co-development

## Bước 5: Risk & Mitigation (1 trang)
- Top 5 risk: champion leave, M&A, budget cut, competitor takeover, product issue
- Mitigation cho mỗi risk
- Early warning indicator + alert owner

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce MCP: pull account data, opportunity history
- LinkedIn MCP: stakeholder org chart + recent moves
- WebFetch: news, 10-K, earnings call insight
- Slack MCP: dedicated channel cho account plan execution

**Fallback API:**
```python
# LinkedIn Company API pull org info
import requests
r = requests.get(f"https://api.linkedin.com/v2/organizations/{org_id}",
    headers={"Authorization": f"Bearer {token}"}).json()
# Pull employees by title
emps = requests.get(f"https://api.linkedin.com/v2/people-search",
    params={"keywords": "VP", "company": org_id}).json()
```

## Bước 7: Output Format
- **File 1**: `account_plan_<KH>.docx` — 10 trang đầy đủ 6 phần
- **File 2**: `whitespace_matrix.xlsx` — BU × Product mapping
- **File 3**: `stakeholder_map.pptx` — org chart visual
- **File 4**: `account_plan_dashboard.xlsx` — tracker quarterly milestone
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] White space có data cụ thể (không chung chung)
- [ ] Stakeholder map đủ 20+ người
- [ ] Year 1 plan quarterly milestone
- [ ] Risk top 5 + mitigation owner
- [ ] Review quarterly + update
- [ ] Buy-in từ Champion KH (review chung)
