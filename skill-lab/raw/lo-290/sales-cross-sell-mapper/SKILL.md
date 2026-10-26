---
name: sales-cross-sell-mapper
description: |
  Map cơ hội cross-sell sản phẩm khác cho KH theo persona, industry, lifecycle stage với kịch bản gợi mở. Trigger phrases: "cross-sell map", "bán chéo sản phẩm", "cross sell B2B", "map cơ hội cross sell", "bán thêm sản phẩm khác", "cross-sell theo persona", "tăng wallet share", "bán chéo khách hàng cũ", "matrix cross sell", "chiến lược cross sell". Output là Markdown playbook + Excel mapping matrix.
---

# Cross-sell Opportunity Mapper

## Mục Tiêu
Tăng wallet share KH hiện hữu bằng matrix mapping sản phẩm × persona × industry × lifecycle stage để CSM/AE biết "bán cái gì cho ai khi nào".

## Khi Nào Dùng
- Doanh nghiệp có >3 SKU/product line
- Sau M&A acquire portfolio mới
- KH mới onboard sản phẩm chính
- Renewal có cơ hội bundle
- Cần roadmap account growth

## Bước 1: Inventory Product/Service
Liệt kê hết SKU bán được:
- Tên + value prop 1 dòng
- Persona target (CFO/Marketing/Sales/Ops)
- Industry fit (FMCG/Retail/Finance/...)
- Lifecycle stage phù hợp (Onboard/Adopt/Renew/Expand)
- Average deal size
- Sales cycle days

## Bước 2: Build Cross-sell Matrix
Tạo bảng 2 chiều:
- Hàng: 8-15 sản phẩm
- Cột: 5 persona × 4 lifecycle = 20 cell
- Cell ghi: Priority (P1/P2/P3) + Trigger event

Ví dụ:
- KH mua Product A (CRM) → Persona Sales VP → Stage Adopt (3 tháng) → Cross-sell P1: Sales Coaching tool (trigger: NPS >40)
- Cross-sell P2: Forecasting tool (trigger: pipeline >$1M)

## Bước 3: Script Gợi Mở theo Matrix
Mỗi cell P1 có script 50 từ:
- Reference outcome KH đã đạt với sản phẩm hiện tại
- Bridge: "Khách cùng size như anh sau khi đạt X thường gặp Y"
- Solution: "Sản phẩm Z giải quyết Y, share case study?"
- Soft CTA: "Em book 20 phút show được không?"

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce/HubSpot MCP: pull KH đã mua gì, chưa mua gì
- Gainsight MCP: lifecycle stage + adoption signal
- WebFetch: industry benchmark cross-sell rate
- Slack MCP: alert AE khi KH match trigger

**Fallback API:**
```python
# Pull KH có sản phẩm A nhưng chưa có B
soql = """SELECT Account.Name, Account.Id 
    FROM Asset WHERE Product2.Name = 'Product A' 
    AND Account.Id NOT IN 
    (SELECT AccountId FROM Asset WHERE Product2.Name = 'Product B')"""
candidates = sf.query(soql)["records"]
# Filter theo lifecycle + persona
```

## Bước 5: Output Format
- **File 1**: `crosssell_matrix.xlsx` — 8 sản phẩm × 20 cell (persona × stage), color-coded P1/P2/P3
- **File 2**: `crosssell_playbook.md` — playbook cho mỗi P1 cell, có script + trigger + ROI
- **File 3**: `crosssell_candidates.xlsx` — list KH match mỗi cell, có owner + next action
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ toàn bộ SKU trong matrix
- [ ] Mỗi cell có priority + trigger
- [ ] P1 có script + ROI sẵn
- [ ] Candidates list có owner assigned
- [ ] Tránh "bán mọi thứ cho mọi người"
- [ ] Cập nhật khi launch SKU mới
