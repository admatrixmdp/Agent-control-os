---
name: it-vendor-saas-audit
description: |
  Audit toàn bộ SaaS doanh nghiệp đang dùng: chi phí, số seat, mức độ sử dụng thực tế, sự trùng lặp tính năng — để cắt giảm lãng phí 20-40% ngân sách SaaS.
  Kích hoạt khi người dùng nói: "audit SaaS", "kiểm tra phần mềm công ty đang dùng", "SaaS spend review", "phần mềm trùng tính năng", "rà soát license", "vendor management", "SaaS portfolio review", "tối ưu danh mục SaaS", "đánh giá nhà cung cấp", "consolidate SaaS".
  Output là báo cáo Excel + kế hoạch hành động Markdown.
---

# SaaS & Vendor Audit Tool

## Mục Tiêu
Trung bình doanh nghiệp dùng 130+ SaaS, 30-40% không dùng tới. Skill này giúp IT/Finance audit toàn bộ danh mục SaaS, tìm điểm cắt giảm — tiết kiệm 20-40% chi phí SaaS hàng năm.

## Khi Nào Dùng
- Cuối năm review ngân sách IT
- CFO yêu cầu cắt giảm chi phí
- Mới về làm Head of IT, cần map toàn bộ portfolio
- M&A xong cần consolidate 2 portfolio SaaS
- Phát hiện chi phí SaaS tăng vọt bất thường

## Bước 1: Thu Thập Danh Sách SaaS
Nguồn data lấy từ:
- **Sao kê thẻ tín dụng công ty** (chính xác nhất)
- **Hoá đơn từ Finance** (subscription monthly/yearly)
- **SSO provider** (Okta, Google, Microsoft) — list app đã connect
- **Hỏi từng phòng ban** "team em đang dùng tool gì có trả tiền"
- **Browser audit** — tool như Productiv, Torii (nâng cao)

## Bước 2: Phân Loại & Đánh Giá Mỗi SaaS
Cột tracking trên bảng audit:
- Tên SaaS / Category (Communication, Design, DevTools, CRM...)
- Vendor / Plan / Billing cycle / Chi phí năm
- Số seat đã mua / Số seat active 30 ngày qua (% utilization)
- Owner phòng ban / Owner cá nhân (account admin)
- Tier dữ liệu (có lưu PII / data khách không)
- Có SOC 2 / ISO 27001 không
- Renewal date
- Tính năng chính

Tính cột phái sinh:
- **Cost per active user/month**
- **Utilization %** = active seats / paid seats
- **Overlap score** — có SaaS khác cùng tính năng không

## Bước 3: Phân Loại Hành Động
Mỗi SaaS rơi vào 1 trong 5 nhóm:
1. **Keep & Optimize** — dùng tốt, renew bình thường
2. **Right-size** — giảm seat (utilization <60%)
3. **Consolidate** — gộp với SaaS khác cùng tính năng
4. **Renegotiate** — đàm phán giá khi renew (đặc biệt vendor >$10K/năm)
5. **Cancel** — utilization <20% hoặc không còn cần

Ví dụ: phát hiện công ty dùng Zoom + Google Meet + Teams → consolidate về Google Meet (đã có Workspace) → tiết kiệm 15K USD/năm.

## Bước 4: Tính Tiềm Năng Tiết Kiệm
Lập bảng savings:
- Cancel category — tiết kiệm 100% chi phí
- Right-size — tiết kiệm 30-50%
- Renegotiate — tiết kiệm 10-25% (volume discount, multi-year)
- Tổng savings dự kiến vs ngân sách hiện tại

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: file audit master, dashboard auto-update
- Google Drive MCP: lưu hợp đồng SaaS quét PDF
- Slack MCP: khảo sát "tool nào team đang dùng" qua poll
- Notion MCP: knowledge base về portfolio SaaS công ty
- Linear MCP: mỗi action item là 1 ticket có deadline
- Gmail MCP: search inbox tìm invoice từ vendor
- WebSearch: tra giá thị trường để benchmark
- WebFetch: pull pricing page vendor để so sánh

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Lấy danh sách app đã SSO qua Okta
import requests
OKTA_DOMAIN = "company.okta.com"
TOKEN = "SSWS ..."
headers = {"Authorization": TOKEN, "Accept": "application/json"}
r = requests.get(f"https://{OKTA_DOMAIN}/api/v1/apps",
                 headers=headers, params={"limit": 200})
apps = [{"name": a["label"], "status": a["status"],
         "users": a.get("_links", {}).get("users", {}).get("count", 0)}
        for a in r.json()]
```

## Bước 6: Output Format
- File chính: `SaaS_Audit_<YYYYQQ>.xlsx`
  - Sheet 1: Inventory tổng
  - Sheet 2: Utilization analysis
  - Sheet 3: Overlap matrix
  - Sheet 4: Savings plan
  - Sheet 5: Renewal calendar
- Báo cáo executive: `SaaS_Audit_Executive_Summary.md` (1 trang cho CEO)
- Action plan: `SaaS_Optimization_Plan.md` (deadline cụ thể)
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/saas-audit/`

## Checklist Trước Khi Giao
- [ ] Đã list ≥90% SaaS thực tế đang dùng
- [ ] Cross-check 3 nguồn (CC statement, SSO, hỏi user)
- [ ] Có utilization % cho mỗi SaaS
- [ ] Đã xác định overlap (≥2 tools cùng tính năng)
- [ ] Savings plan có deadline + owner
- [ ] Renewal calendar 12 tháng tới
- [ ] Báo cáo executive ≤2 trang, có số liệu cụ thể
