---
name: sales-quote-generator
description: |
  Sinh báo giá tự động từ template chuẩn có điều khoản, tiers, discount logic và auto-fill thông tin KH từ CRM. Trigger phrases: "tạo báo giá", "generate quote", "sinh quote tự động", "báo giá template", "soạn báo giá nhanh", "quote sales", "tạo bảng giá khách hàng", "config price quote", "báo giá CRM", "auto báo giá". Output là PDF quote + Excel + Markdown email kèm.
---

# Quote Generator (Template + Discount Logic)

## Mục Tiêu
Sinh báo giá chuẩn 2-3 trang trong <5 phút, áp dụng đúng pricing rules (volume discount, multi-year, payment term), tránh sai sót giá làm sales nhanh hơn 10x.

## Khi Nào Dùng
- KH yêu cầu báo giá nhanh
- Renewal khi giá có thay đổi
- Khi cần chốt thử nhiều scenarios cho KH
- Sales mới chưa thuộc rules pricing
- Cần báo giá hàng loạt (>10 KH)

## Bước 1: Pull data KH từ CRM
Auto-fill:
- Company name, legal name, address, tax ID
- Contact: Economic Buyer + AP contact
- Quote owner (AE) + email
- Product/SKU đã chọn trong opportunity
- Term năm hợp đồng

## Bước 2: Apply Pricing Logic
Áp dụng auto:
- **Volume discount**: >100 user = 10%, >500 = 15%, >1000 = 20%
- **Multi-year**: 2-year = 5% off, 3-year = 10% off
- **Payment**: annual upfront = 5%, monthly = +0
- **New customer**: + first-year discount theo policy
- **Approval rule**: discount >20% phải Manager duyệt; >30% phải Director

Hiển thị rõ "List price → Discount → Net price" để KH thấy giá trị.

## Bước 3: Tạo Quote Template
**Trang 1**: Logo, Quote # (auto), Date, Valid until (30 ngày), Bill to / Ship to
**Trang 2**: Line items table — SKU, Description, Qty, Unit price, Discount, Net
**Trang 3**: Terms (payment, SLA, cancellation, IP, jurisdiction) + chữ ký 2 bên

Footer: T&C link, support contact, bank info.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce CPQ / HubSpot Quote MCP: tạo quote native từ opp
- DocuSign/PandaDoc MCP: thêm e-sign workflow
- Gmail MCP: gửi quote kèm email cover
- Drive MCP: lưu quote PDF vào folder customer

**Fallback API:**
```python
# Salesforce CPQ tạo Quote
sf.Quote.create({"OpportunityId": opp_id, "Name": f"Quote-{cust}",
    "ExpirationDate": "2026-06-30", "Pricebook2Id": pb_id})
# Add line items
for item in line_items:
    sf.QuoteLineItem.create({"QuoteId": quote_id, "Product2Id": item["sku"],
        "Quantity": item["qty"], "UnitPrice": item["price"],
        "Discount": item["discount"]})
```

## Bước 5: Output Format
- **File 1**: `quote_<QUOTE-ID>.pdf` — 2-3 trang signed-ready
- **File 2**: `quote_<QUOTE-ID>.xlsx` — chi tiết line item + tổng tax
- **File 3**: `quote_cover_email.md` — email gửi kèm
- **File 4**: `approval_log.xlsx` — track ai duyệt discount
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Quote # unique, auto-increment
- [ ] Valid-until rõ ràng (30/60 ngày)
- [ ] Discount logic apply đúng tier
- [ ] Approval workflow trigger khi cần
- [ ] Tax (VAT 10%) tính đúng
- [ ] Có chữ ký 2 bên trên trang cuối
- [ ] Backup vào CRM + Drive
