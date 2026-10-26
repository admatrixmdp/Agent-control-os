---
name: proc-po-template
description: |
  Tạo template Đơn Đặt Hàng (Purchase Order — PO) chuẩn cho phòng mua hàng — chi tiết spec, giá, thanh toán, giao hàng, T&C đi kèm. Kích hoạt khi người dùng nói: "tạo PO", "đơn đặt hàng", "purchase order VN", "PO template", "soạn đơn hàng cho NCC", "đặt hàng NCC", "PO xuất khẩu", "PO nhập khẩu", "PO Incoterms", "auto PO". Output là file .docx PO + Excel batch PO generator + PDF gửi NCC.
---

# Template Đơn Đặt Hàng PO Chuẩn

## Mục Tiêu
Cung cấp template PO chuẩn để phòng Mua hàng phát hành đơn nhanh, ràng buộc pháp lý rõ ràng theo hợp đồng khung. Tránh tranh chấp do PO thiếu T&C — vì theo Luật TM 2005 Đ.24, PO + xác nhận = HĐ mua bán hợp lệ.

## Khi Nào Dùng
- Đặt hàng theo HĐ khung (Master Agreement) đã ký với NCC
- Đặt hàng spot (không có HĐ khung — PO trở thành HĐ độc lập)
- Đặt hàng nhập khẩu kèm mở LC / TT
- Đặt hàng gấp / khẩn (emergency PO)
- Đặt hàng định kỳ tự động (blanket PO / standing order)

## Bước 1: Chọn Loại PO
- **Standard PO**: 1 lần giao, 1 lần thanh toán
- **Blanket PO**: 1 PO khung + nhiều lần giao theo schedule (12 tháng)
- **Contract PO**: PO + HĐ khung đính kèm
- **Planned PO**: PO sơ bộ chờ release order chính thức
- **Drop-ship PO**: NCC giao thẳng cho khách hàng cuối (e-commerce)

## Bước 2: 12 Trường Bắt Buộc Trên PO
1. Số PO + ngày phát hành
2. Thông tin Buyer (Tên DN, MST, địa chỉ, người liên hệ)
3. Thông tin Vendor (Tên DN, MST, địa chỉ, người liên hệ)
4. Tham chiếu HĐ khung (nếu có)
5. Bảng hàng hoá: STT | Mã | Tên | Quy cách | SL | Đơn giá | VAT | Thành tiền
6. Tổng giá trị + tiền tệ
7. Điều khoản thanh toán (NET 30 / advance / LC at sight...)
8. Địa điểm + ngày giao hàng + Incoterm
9. Yêu cầu chứng từ (CO/CQ, MSDS, invoice, packing list)
10. Bảo hành / cam kết chất lượng
11. T&C đi kèm (link tới file riêng "PO Standard Terms")
12. Chữ ký + đóng dấu Buyer (thẩm quyền theo policy)

## Bước 3: Quy Trình Phát Hành PO
1. Yêu cầu mua hàng (PR) từ phòng ban → duyệt theo hạn mức
2. Mua hàng tạo PO từ template
3. Duyệt cấp (Manager <100M, Director <500M, CEO >500M)
4. Gửi PO cho NCC qua email + cổng vendor portal
5. NCC ký xác nhận (Acknowledgment) → PO active
6. Track giao hàng (3-way match: PO – GR – Invoice)
7. Đóng PO sau khi nghiệm thu + thanh toán

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: lưu PO + bằng chứng giao hàng + invoice
- Gmail MCP: gửi PO + nhận PO acknowledgment + auto OCR
- Google Sheets MCP: PO register sống + dashboard chi tiêu
- Notion MCP: vendor portal + PO status tracking
- DocuSign MCP: ký số PO (Buyer + Vendor) — tăng tốc 3-5 ngày
- WebFetch: KiotViet / Sapo / Misa Amis Sales — đồng bộ PO với ERP nếu DN dùng
- WebSearch: tra giá thị trường (TMĐT, Alibaba) để verify giá NCC

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Generate batch PO từ DS PR + sync với KiotViet / Misa
from docxtpl import DocxTemplate
import requests
from datetime import datetime

def generate_po(pr_data, vendor_info, contract_ref=None):
    doc = DocxTemplate("po_template.docx")
    po_number = f"PO-{datetime.now().strftime('%Y%m%d')}-{pr_data['pr_id']}"
    context = {
        "po_number": po_number,
        "po_date": datetime.now().strftime("%d/%m/%Y"),
        "vendor": vendor_info,
        "items": pr_data["items"],
        "subtotal": sum(i["qty"] * i["price"] for i in pr_data["items"]),
        "vat_rate": 0.10,
        "incoterm": pr_data.get("incoterm", "DAP Buyer's warehouse"),
        "payment_term": pr_data.get("payment_term", "NET 30"),
        "contract_ref": contract_ref
    }
    context["vat"] = context["subtotal"] * context["vat_rate"]
    context["total"] = context["subtotal"] + context["vat"]
    doc.render(context)
    doc.save(f"{po_number}.docx")

    # Sync KiotViet (nếu dùng)
    # requests.post("https://public.kiotapi.com/purchaseorders", json={...}, headers={"Retailer": "...", "Authorization": "Bearer ..."})
    return po_number
```

## Bước 5: Output Format
- File `PO-<yyyymmdd>-<seq>.docx`: PO chính, font Times New Roman 12
- File `PO-<yyyymmdd>-<seq>.pdf`: bản PDF chống chỉnh sửa, có QR code verify
- File `po_register.xlsx`: master log toàn bộ PO với status, value, vendor, ngày giao
- File `po_standard_terms.pdf`: T&C đi kèm mọi PO (đính trong email)
- Email template gửi NCC + form acknowledgment
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/purchase-orders/`

## Checklist Trước Khi Giao
- [ ] Có đủ 12 trường bắt buộc trên PO
- [ ] Số PO unique + có format dễ tra (PO-yyyymmdd-seq)
- [ ] Đã verify thông tin vendor (MST, tên, địa chỉ)
- [ ] Đã duyệt đúng cấp thẩm quyền theo hạn mức
- [ ] T&C đi kèm rõ ràng (link / attachment)
- [ ] Có cơ chế 3-way match khi nghiệm thu
- [ ] Đã đồng bộ với hệ thống ERP (KiotViet/Misa/SAP)
- [ ] Có dashboard tracking + remind giao trễ
