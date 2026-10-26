---
name: fin-tax-vat-summary
description: |
  Tóm tắt thuế GTGT (VAT) đầu vào - đầu ra theo tháng/quý, chuẩn bị tờ khai 01/GTGT
  và hồ sơ hoàn thuế. Trigger phrases: "thuế VAT", "tờ khai GTGT", "thuế đầu vào đầu ra",
  "01/GTGT", "hoàn thuế VAT", "tóm tắt thuế tháng", "tax summary", "kê khai thuế GTGT",
  "VAT input output", "kê khai thuế tháng". Output là Excel kê khai + PDF tờ khai mẫu
  01/GTGT.
---

# Tóm Tắt Thuế GTGT Tháng/Quý + Hỗ Trợ Tờ Khai

## Mục Tiêu
Tự động hoá việc đối chiếu thuế GTGT đầu vào - đầu ra trước hạn 20/T+1 hoặc hạn quý,
phát hiện sớm hoá đơn rủi ro (NCC bỏ trốn, hoá đơn không hợp lệ), tối ưu khấu trừ.

## Khi Nào Dùng
- Đầu mỗi tháng/quý làm tờ khai
- Trước khi nộp hồ sơ hoàn thuế GTGT
- Kiểm tra trước thanh tra thuế
- Cuối năm tổng kết VAT để chốt sổ

## Bước 1: Thu Thập Hoá Đơn
**Đầu ra (output VAT):**
- Toàn bộ hoá đơn điện tử bán ra trong kỳ
- Phân loại theo thuế suất: 0%, 5%, 8%, 10%
- Doanh thu không thuế (xuất khẩu, không chịu thuế)

**Đầu vào (input VAT):**
- Tất cả hoá đơn mua vào hợp lệ
- Phân: dùng cho hoạt động chịu thuế (khấu trừ 100%), hoạt động không chịu thuế (không khấu trừ), cả hai (phân bổ theo tỷ lệ doanh thu)

## Bước 2: Đối Chiếu & Tính Số Phải Nộp
```
VAT phải nộp = VAT đầu ra - VAT đầu vào được khấu trừ
```

Nếu âm → chuyển kỳ sau hoặc xin hoàn (nếu đủ điều kiện ≥ 300tr hoàn xuất khẩu, ≥ 12 tháng âm liên tục với DN nội địa).

**Đối chiếu chéo:**
- Đầu vào: tra MST NCC trên cổng tracuunnt.gdt.gov.vn xem có đang hoạt động không
- So tổng doanh thu trên 01/GTGT với sổ doanh thu (TK 511, 711)
- So đầu vào với sổ 133

## Bước 3: Phát Hiện Rủi Ro
**Red flags:**
- HĐ đầu vào từ NCC đã ngừng hoạt động → loại khỏi khấu trừ
- HĐ mua >20tr nhưng thanh toán tiền mặt → không được khấu trừ
- HĐ thiếu MST/tên/địa chỉ chuẩn → cần điều chỉnh
- Chênh lệch doanh thu kê khai vs sổ kế toán → soát lại

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: Lưu hoá đơn PDF/XML đã đối chiếu
- Gmail MCP: Pull hoá đơn điện tử nhận qua email từ NCC
- WebFetch: Tra cứu MST trên `tracuunnt.gdt.gov.vn`
- WebSearch: Tra thông tư mới về VAT (TT 80, NĐ 123)

**Fallback bằng API:**
```python
# Gọi API VietInvoice/Viettel/MISA Meinvoice lấy danh sách HĐ điện tử
import requests
r = requests.post(
    "https://api-vinvoice.viettel.vn/InvoiceAPI/InvoiceWS/getInvoices",
    json={"taxCode": "0312345678",
          "fromDate": "2026-05-01", "toDate": "2026-05-31",
          "type": "input"},
    headers={"Authorization": f"Bearer {VIETTEL_TOKEN}"}
)
invoices = r.json()["data"]
# Check MST từng NCC qua API GDT
for inv in invoices:
    nnt = requests.get(f"https://api.gdt.gov.vn/nnt/{inv['sellerTaxCode']}")
    inv["status"] = nnt.json()["status"]  # "Đang hoạt động" / "Ngừng"
```

## Bước 5: Output Format
1. **Excel kê khai** (`VAT_T05_2026.xlsx`): Sheet "Output" (bán ra), "Input" (mua vào), "Summary" tổng hợp khớp với chỉ tiêu trên 01/GTGT, "RedFlag" liệt kê HĐ rủi ro.
2. **PDF tờ khai** (`01_GTGT_T05_2026.pdf`): Mẫu 01/GTGT điền sẵn, sẵn sàng ký số nộp eTax.
3. **HTML dashboard** (`vat_dashboard.html`): Biểu đồ VAT đầu ra/đầu vào 12 tháng, gauge số phải nộp/được hoàn, alert HĐ rủi ro.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/tax/vat/`

## Checklist Trước Khi Giao
- [ ] Đã tra MST 100% NCC trên cổng GDT
- [ ] Đã loại HĐ thanh toán tiền mặt >20tr
- [ ] Tổng doanh thu trên tờ khai khớp sổ
- [ ] Đã so chéo với 01/GTGT của NCC nếu là KH thường xuyên
- [ ] Đã backup XML hoá đơn theo quy định 10 năm
- [ ] Nộp trước hạn 20/T+1 (tránh phạt chậm nộp)
