---
name: ceo-vendor-shortlist
description: |
  Sàng lọc nhà cung cấp chiến lược (vendor/supplier/agency) — soạn RFI, dùng WebFetch quét website, chấm điểm 5 tiêu chí, ra shortlist 3-5 ứng viên kèm so sánh giá.
  Kích hoạt khi người dùng nói: "sàng lọc NCC", "vendor shortlist", "tìm nhà cung cấp", "RFI vendor", "shortlist supplier", "đánh giá NCC", "chọn agency", "lựa chọn đối tác chiến lược".
  Output là Excel comparison + email outreach.
---

# CEO Vendor Shortlist — Sàng Lọc Nhà Cung Cấp Chiến Lược

## Mục Tiêu
NCC chiến lược (agency, hosting, ERP, BPO) chọn sai = mất 6 tháng + chục tỷ. Skill này chuẩn hoá process từ long list → shortlist 3-5 → final pick có data.

## Khi Nào Dùng
- Chọn agency marketing/legal/audit
- Đổi nhà cung cấp ERP/CRM
- Chọn data center / cloud provider
- Outsource BPO call center
- Thuê PR firm cho crisis

## Bước 1: Định Nghĩa Nhu Cầu (RFI Brief)
- Vấn đề cần giải quyết
- Scope: gì cần làm cụ thể
- Timeline: bắt đầu, milestone, kết thúc
- Budget range
- Must-have vs Nice-to-have features
- Success criteria (KPI đánh giá NCC)

## Bước 2: Long List 15-30 Ứng Viên
- WebSearch keyword + "Việt Nam" hoặc "Asia"
- LinkedIn company search
- Referral từ network
- Past vendor list trong industry
- Mục tiêu: 15-30 cái rồi filter

## Bước 3: Scoring 5 Tiêu Chí (Mỗi /20)
1. **Expertise**: case study, năm kinh nghiệm, certification
2. **Fit**: làm cho khách hàng cùng size/ngành chưa
3. **Price**: ngân sách phù hợp
4. **Team**: quy mô, key person
5. **Risk**: stability tài chính, ownership

Tổng /100 → shortlist top 3-5.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tìm long list theo ngành
- WebFetch: lấy website, case study, About page
- Gmail MCP: gửi RFI cho long list
- Notion MCP: vendor pipeline database
- Linear MCP: track RFI status (sent/responded/declined)

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Scrape vendor website
import requests
from bs4 import BeautifulSoup
for v in vendor_list:
    html = requests.get(v['website']).text
    soup = BeautifulSoup(html, 'html.parser')
    v['team_size'] = soup.find(text=lambda t: 'employees' in t.lower())
    v['clients'] = [a.text for a in soup.select('.client-logo')]
```

## Bước 5: Output Format
- Excel comparison matrix vendor × tiêu chí
- HTML 1 trang shortlist top 5 với pros/cons
- RFI template Word .docx gửi NCC
- Outreach email Markdown
- Score reasoning document
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/vendor-[category]-YYYY.xlsx`

## Checklist Trước Khi Giao
- [ ] Long list ≥ 15
- [ ] RFI brief đầy đủ scope/budget/timeline
- [ ] Scoring 5 tiêu chí có reasoning
- [ ] Shortlist 3-5 với pros/cons cụ thể
- [ ] Reference check ≥ 2 client cũ
- [ ] Outreach email đã personalize
