---
name: sales-lead-list-builder
description: |
  Tạo list lead chất lượng từ Apollo/LinkedIn Sales Navigator/Lusha + enrich data (email, phone, LinkedIn, intent) sẵn import CRM. Trigger phrases: "tạo list lead", "build lead list", "scrape Apollo", "tìm khách hàng tiềm năng", "lead list B2B", "enrich data lead", "danh sách prospect", "list lead Sales Navigator", "tìm email công ty", "data outbound". Output là Excel list lead enriched + Markdown query setup.
---

# Lead List Builder & Enrichment

## Mục Tiêu
Tạo list lead 200-2000 prospects match ICP, enriched đầy đủ (verified email, mobile, LinkedIn, intent signal) để outbound campaign khởi động trong 24h.

## Khi Nào Dùng
- Khởi động chiến dịch outbound mới
- Penetrate vertical/region mới
- Bổ sung pipeline cho SDR mới onboard
- Chuẩn bị ABM cho top 50 account
- Refresh list cũ >6 tháng

## Bước 1: Lock ICP filter
Từ ICP doc, chuyển thành Apollo/Sales Nav filter:
- Industry codes (SIC/NAICS)
- Company size: 50-500 NV
- Revenue: $10M-$100M
- Geo: VN, SG, TH
- Technology: "uses Salesforce" / "uses Shopify"
- Person title: "VP Sales", "Head of Revenue"
- Seniority: Director+
- Department: Sales, Marketing

Lưu saved search để reuse.

## Bước 2: Export raw list + Dedupe
- Export CSV 500-2000 dòng
- Dedupe bằng: company domain + person name
- Loại current customer + lost deal <90 ngày
- Loại email pattern catch-all (info@, contact@)

## Bước 3: Enrich 3 lớp
- **Lớp 1 — Contact**: verified email (NeverBounce/ZeroBounce), mobile, LinkedIn URL
- **Lớp 2 — Company**: tech stack (BuiltWith/Wappalyzer), funding (Crunchbase), employee growth (LinkedIn)
- **Lớp 3 — Intent signal**: G2/Bombora intent topic, recent hire (sales/eng), website visit (nếu có 6sense/RB2B)

Mỗi lead có score 0-100 (Fit 50 + Intent 50).

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Apollo MCP: search + enrich + push to CRM
- LinkedIn Sales Navigator: filter advanced + save search
- HubSpot/Salesforce MCP: push lead vào CRM với owner assignment
- WebFetch: verify company còn hoạt động, đọc career page

**Fallback API:**
```python
# Apollo + verify email
import requests
people = requests.post("https://api.apollo.io/v1/mixed_people/search",
    headers={"X-Api-Key": KEY},
    json={"person_titles": ["VP Sales"], "person_seniorities": ["director"],
          "page": 1, "per_page": 100}).json()["people"]
# Verify với NeverBounce
for p in people:
    v = requests.get(f"https://api.neverbounce.com/v4/single/check",
        params={"key": NB_KEY, "email": p["email"]}).json()
    p["email_valid"] = v["result"] == "valid"
```

## Bước 5: Output Format
- **File 1**: `leadlist_<vertical>_<date>.xlsx` — 25 cột: Name, Title, Company, Domain, Email, Email_verified, Mobile, LinkedIn, Industry, Size, Revenue, Tech_stack, Funding_stage, Intent_topic, Fit_score, Intent_score, Total_score, Owner, Status, Notes
- **File 2**: `query_setup.md` — screenshot filter + JSON config để reuse
- **File 3**: `dedupe_log.xlsx` — record bị loại + lý do
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] >95% email verified (loại catch-all & risky)
- [ ] Có cột LinkedIn URL cho 100% lead
- [ ] Score 0-100 mỗi lead, sort giảm dần
- [ ] Đã loại current customer + lost deal recent
- [ ] Max 5 contact / company (tránh spam)
- [ ] Có owner assignment trước khi import CRM
