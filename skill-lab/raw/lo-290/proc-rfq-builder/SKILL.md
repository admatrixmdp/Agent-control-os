---
name: proc-rfq-builder
description: |
  Soạn Hồ sơ Yêu cầu Báo giá RFQ (Request for Quotation) chuẩn — gồm spec kỹ thuật, T&C thương mại, timeline, tiêu chí chấm điểm, mẫu báo giá. Kích hoạt khi người dùng nói: "soạn RFQ", "viết yêu cầu báo giá", "RFQ template", "RFP cho NCC", "yêu cầu báo giá nhà cung cấp", "soạn TOR mua hàng", "yêu cầu chào hàng cạnh tranh", "đấu thầu mini", "tender document SME", "yêu cầu báo giá quốc tế". Output là file .docx RFQ đầy đủ + Excel mẫu báo giá để NCC điền + Email gửi NCC.
---

# RFQ Builder — Hồ Sơ Yêu Cầu Báo Giá Chuẩn

## Mục Tiêu
Giúp phòng Mua hàng SME tạo RFQ chuyên nghiệp trong 30 phút (thay vì 1-2 ngày) — đảm bảo NCC chào giá đúng spec, dễ so sánh, tránh tranh chấp sau khi ký hợp đồng. Áp dụng nguyên tắc Luật Đấu thầu 2023 (số 22/2023/QH15) cho khu vực tư nhân (không bắt buộc nhưng best practice).

## Khi Nào Dùng
- Mua nguyên vật liệu lớn (>100 triệu) cần so sánh ≥3 NCC
- Mua thiết bị / máy móc đầu tư
- Thuê dịch vụ outsource (marketing, IT, vệ sinh, logistics)
- Mua hàng nhập khẩu từ NCC nước ngoài
- Đổi NCC định kỳ (rebid hàng năm)

## Bước 1: Lập Spec Kỹ Thuật (Technical Specifications)
Phần dễ bị NCC "lách" nhất — phải rõ ràng:
- Tên sản phẩm + mã (SKU, HS Code)
- Thông số kỹ thuật (kích thước, vật liệu, chứng nhận CE/UL/FDA/ISO)
- Số lượng + đơn vị tính + dung sai (±2%)
- Bao bì + ghi nhãn
- Tiêu chuẩn chất lượng (QC plan, AQL 2.5)
- Mẫu vật / drawing đính kèm
- Tiêu chí nghiệm thu (Acceptance Criteria)

## Bước 2: Lập T&C Thương Mại
- Thời gian giao hàng yêu cầu (Lead Time)
- Địa điểm giao hàng (Incoterms 2020: EXW / FOB / CIF / DAP / DDP)
- Điều khoản thanh toán (NET 30 / NET 60 / LC / TT 30-70)
- Tiền tệ (VND / USD / EUR / CNY)
- Bảo hành (12-24 tháng)
- Hiệu lực báo giá (≥30-60 ngày)
- Penalty trễ giao (0.1% - 0.5% / ngày, max 8%)
- Yêu cầu chứng từ (CO/CQ, MSDS, COA, hoá đơn VAT)

## Bước 3: Tiêu Chí Chấm Điểm + Mẫu Báo Giá
Trọng số gợi ý:
- Giá: 40-50%
- Chất lượng + chứng nhận: 20-25%
- Thời gian giao hàng: 15-20%
- Điều kiện thanh toán: 10-15%
- Năng lực NCC (capacity, financial, reference): 5-10%

Mẫu báo giá Excel cho NCC điền: STT | Mã | Tên hàng | Quy cách | SL | Đơn giá | Thành tiền | VAT | Thời gian | Ghi chú

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: lưu RFQ + nhận báo giá NCC qua link
- Gmail MCP: gửi RFQ hàng loạt cho NCC + auto-track ai đã mở
- Google Sheets MCP: dashboard nhận báo giá real-time
- Notion MCP: vendor database — chọn NCC theo category & rating
- WebFetch: tra cứu NCC trên Alibaba / Made-in-China / Globalsources
- WebFetch: kiểm tra GPKD NCC trên `dangkykinhdoanh.gov.vn`

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Gửi RFQ hàng loạt + theo dõi response qua Gmail API
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_rfq_batch(vendor_emails, rfq_docx_path, quotation_template_xlsx_path):
    sent = []
    for email in vendor_emails:
        msg = MIMEMultipart()
        msg["To"] = email
        msg["Subject"] = "[RFQ-2026-001] Yêu cầu báo giá - Deadline 15/06"
        msg.attach(MIMEText("Vui lòng điền mẫu báo giá và gửi lại trước 17h00 ngày 15/06/2026.", "plain"))
        for path in [rfq_docx_path, quotation_template_xlsx_path]:
            with open(path, "rb") as f:
                part = MIMEApplication(f.read())
                part.add_header("Content-Disposition", f'attachment; filename="{path.split("/")[-1]}"')
                msg.attach(part)
        # gmail_service.users().messages().send(...)
        sent.append({"vendor": email, "sent_at": "..."})
    return sent
```

## Bước 5: Output Format
- File `RFQ_<MaDuAn>_<yyyymmdd>.docx`: hồ sơ RFQ đầy đủ
- File `Mau_BaoGia_NCC.xlsx`: mẫu Excel cho NCC điền (locked cells để tránh sửa spec)
- File `Email_RFQ_template.txt`: nội dung email gửi NCC
- File `vendor_response_tracker.xlsx`: theo dõi NCC nào đã gửi báo giá
- File `scoring_matrix.xlsx`: ma trận chấm điểm sau khi nhận đủ báo giá
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/rfq/`

## Checklist Trước Khi Giao
- [ ] Spec kỹ thuật đủ chi tiết, không "phù hợp", "tương đương"
- [ ] Có mẫu báo giá Excel để dễ so sánh
- [ ] T&C thương mại rõ Incoterms + payment terms
- [ ] Có tiêu chí chấm điểm trọng số rõ ràng
- [ ] Deadline báo giá ≥7-14 ngày để NCC chuẩn bị
- [ ] Đã gửi ≥3 NCC để có thể so sánh
- [ ] Có NDA nếu RFQ chứa thông tin nhạy cảm
- [ ] Có tracker theo dõi NCC + nhắc 2 ngày trước deadline
