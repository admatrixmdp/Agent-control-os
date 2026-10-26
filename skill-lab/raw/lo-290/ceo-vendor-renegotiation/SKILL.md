---
name: ceo-vendor-renegotiation
description: |
  Đàm phán lại với NCC chính (hosting, SaaS, agency) — chuẩn bị kịch bản 5 bước, email gửi NCC, talking points, BATNA, fallback options để giảm 20-40% chi phí.
  Kích hoạt khi người dùng nói: "đàm phán lại NCC", "vendor renegotiation", "renegotiate contract", "giảm giá nhà cung cấp", "cắt chi phí SaaS", "negotiate hosting", "đàm phán giá", "renegotiate vendor".
  Output là Markdown playbook + email template.
---

# CEO Vendor Renegotiation — Đàm Phán Lại Với NCC Chính

## Mục Tiêu
Mọi SaaS/hosting/agency contract có thể giảm 20-40% khi renew nếu negotiate đúng. CEO không có thời gian = bỏ tiền. Skill này tạo playbook để CFO/Procurement execute.

## Khi Nào Dùng
- 60-90 ngày trước renewal
- Sau khi cut spending strategy
- Đối thủ cùng vendor đang được giá tốt hơn
- Volume usage tăng/giảm đáng kể
- Crisis cost optimization

## Bước 1: Audit Hợp Đồng Hiện Tại
- Vendor + sản phẩm
- Annual spend (VND/USD)
- Usage thực tế (% capacity)
- Term length + auto-renewal date
- Last price change ngày nào
- Discount đã có

## Bước 2: BATNA + Alternatives
- Liệt kê 3-5 vendor alternative
- Quote sơ bộ từ alternative (WebSearch hoặc demo)
- Switching cost (data migration, training)
- BATNA: nếu vendor không giảm, sẵn sàng switch không?

Nếu BATNA yếu → focus vào multi-year discount thay vì price cut.

## Bước 3: Negotiation Playbook 5 Bước
**Bước 1 - Soft Notify** (90 ngày trước): "Chúng tôi đang review vendor portfolio, muốn thảo luận về renew"
**Bước 2 - Data Push** (75 ngày): chia sẻ usage data, market benchmark, ask discount
**Bước 3 - Counter Offer** (60 ngày): nếu họ giảm 10%, push 25%; cite alternative
**Bước 4 - Best & Final** (30 ngày): "Đây là số chúng tôi có thể đồng ý"
**Bước 5 - Walk Away nếu cần** (15 ngày): execute switch hoặc accept

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: G2/Capterra price comparison, alternative vendors
- WebFetch: pricing page alternative
- Gmail MCP: gửi email negotiation theo template
- Notion MCP: lưu negotiation log
- Calendar MCP: schedule call với vendor account exec

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tính savings projection
current_annual = 600_000_000  # 600M VND
discount_pct = 0.30
multi_year_lock = 2  # year
savings = current_annual * discount_pct * multi_year_lock
print(f"Saved: {savings:,.0f} VND over {multi_year_lock} years")
```

## Bước 5: Output Format
- Markdown playbook 4-6 trang:
  - Audit hiện tại
  - BATNA + alternatives
  - 5-step negotiation script
  - Email templates (5 emails theo timeline)
  - Talking points cho call
- Excel savings projection
- Negotiation log template
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/vendor-renego-[name]-YYYY.md`

## Checklist Trước Khi Giao
- [ ] Hợp đồng hiện tại đã audit
- [ ] 3+ alternative có quote
- [ ] BATNA quyết định trước negotiate
- [ ] Email template 5 bước sẵn
- [ ] Talking points cover objection
- [ ] Walk-away point xác định trước
