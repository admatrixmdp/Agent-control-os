---
name: sales-proposal-writer
description: |
  Viết proposal/báo giá B2B 8-12 trang có executive summary, ROI, scope, pricing, timeline, terms — chuẩn enterprise. Trigger phrases: "viết proposal", "báo giá B2B", "soạn proposal khách hàng", "đề xuất giải pháp", "tạo proposal sales", "viết business proposal", "báo giá doanh nghiệp", "proposal template", "soạn báo giá chuyên nghiệp", "viết document chào hàng". Output là PDF/Docx proposal + Excel pricing.
---

# B2B Proposal Writer

## Mục Tiêu
Tạo proposal B2B 8-12 trang chuyên nghiệp giúp deal late-stage closing nhanh, có executive summary 1 trang đủ để CEO duyệt, ROI rõ ràng và terms gọn để legal review nhanh.

## Khi Nào Dùng
- Deal post-demo cần proposal trong 3-5 ngày
- Enterprise đòi formal document để duyệt
- Renewal/upsell deal cần proposal chính thức
- Trả lời RFP có yêu cầu format proposal
- Pitch dự án implement tích hợp lớn

## Bước 1: Pull discovery data
Tổng hợp từ discovery + demo:
- 3 pain ưu tiên KH đã confirm
- Outcome KH muốn đạt (có số)
- Buying committee (Economic Buyer + Champion)
- Decision criteria + timeline
- Budget range
- Competitive context (đối thủ KH đang xét)

## Bước 2: Cấu trúc Proposal 9 phần

**1. Cover (1 trang)**: logo 2 bên, tên KH, ngày, person of contact
**2. Executive Summary (1 trang)**: 3 pain → 3 solution → 3 outcome + 1 con số ROI
**3. Understanding Your Business (1 trang)**: chứng minh hiểu KH (paraphrase pain)
**4. Proposed Solution (2 trang)**: 3 use case mapping pain, có screenshot
**5. Expected Outcome (1 trang)**: 5 metric + baseline + target + ROI calculator
**6. Implementation Plan (1 trang)**: timeline 6-12 tuần, milestone, owner
**7. Investment (1 trang)**: pricing table 3 tier (Good/Better/Best), gọi "Đề xuất"
**8. Why Us (1 trang)**: 3 case study cùng ngành + 3 differentiator
**9. Next Steps & Terms (1 trang)**: 3 next step + key terms (payment, SLA, cancellation)

## Bước 3: Pricing Strategy 3-tier
- **Good**: chỉ core feature, giá thấp hơn 30% — anchor thấp
- **Better (recommended)**: full feature, giá target — bold, highlight
- **Best**: + premium support, integration custom — anchor cao

Mỗi tier ghi rõ: gồm gì, không gồm gì, hợp đồng bao lâu, payment terms.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce/HubSpot MCP: pull deal info, contact, products
- DocuSign/PandaDoc MCP: gửi proposal có e-sign workflow
- Drive/SharePoint MCP: lưu template proposal
- WebFetch: pull case study mới nhất

**Fallback API:**
```python
# PandaDoc tạo proposal từ template + send
import requests
r = requests.post("https://api.pandadoc.com/public/v1/documents",
    headers={"Authorization": f"API-Key {key}"},
    json={"name": f"Proposal-{customer}", "template_uuid": tpl_id,
          "tokens": [{"name": "Customer.Name", "value": customer},
                     {"name": "Pricing.Total", "value": price}],
          "recipients": [{"email": eb_email, "role": "buyer"}]})
doc_id = r.json()["id"]
requests.post(f"https://api.pandadoc.com/public/v1/documents/{doc_id}/send")
```

## Bước 5: Output Format
- **File 1**: `proposal_<customer>_<date>.docx` — 9 phần, ~10 trang, có brand cover
- **File 2**: `proposal_<customer>_<date>.pdf` — bản gửi KH (signed)
- **File 3**: `pricing_<customer>.xlsx` — 3-tier breakdown + ROI calculator
- **File 4**: `proposal_cover_email.md` — email gửi proposal + next step
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Executive summary 1 trang đủ cho CEO duyệt
- [ ] Mỗi pain mapping 1 solution + 1 outcome đo được
- [ ] Pricing 3-tier với recommended highlighted
- [ ] ROI calculator có công thức rõ
- [ ] Terms gọn, không gài chữ nhỏ
- [ ] Logo + thông tin KH chính xác (kiểm 2 lần)
- [ ] Send via e-sign tool, không scan tay
