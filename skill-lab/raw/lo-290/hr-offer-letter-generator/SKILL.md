---
name: hr-offer-letter-generator
description: |
  Tạo thư mời nhận việc (Offer Letter) chuẩn pháp lý Việt Nam, có đầy đủ tổng thu nhập (gross/net), BHXH/BHYT/BHTN, thuế TNCN, benefit, ngày bắt đầu, điều khoản bảo mật.
  Kích hoạt khi người dùng nói: "thư mời nhận việc", "offer letter", "soạn offer", "thư offer tiếng Việt", "tạo offer cho ứng viên", "thư mời làm việc", "offer package", "tính lương net gross offer", "salary breakdown".
  Output là file .docx + .pdf có chữ ký, sẵn gửi email kèm HĐLĐ thử việc.
---

# HR - Tạo Thư Mời Nhận Việc

## Mục Tiêu
Soạn Offer Letter chuyên nghiệp, rõ ràng tổng thu nhập (kể cả khoản chìm), đúng pháp luật lao động VN, giúp ứng viên dễ chấp nhận và giảm tranh chấp lương về sau.

## Khi Nào Dùng
- Sau khi panel quyết định Hire, cần gửi offer trong 24-48h
- Renegotiation offer khi ứng viên counter-offer
- Offer chuyển nội bộ (internal transfer, promotion)
- Offer expat / nhân sự cấp cao (có equity, sign-on bonus)

## Bước 1: Thu Thập Dữ Liệu Offer
Cần xác nhận với hiring manager + Finance:
- Lương gross/net + cơ chế tính
- Thưởng tháng 13, KPI quý/năm, sign-on bonus
- Phụ cấp: ăn trưa, đi lại, điện thoại, nhà ở
- Phí gia nhập BHXH (DN đóng 21.5%, NV đóng 10.5%)
- Số ngày phép năm (tối thiểu 12 theo BLLĐ 2019)
- Thời gian thử việc (≤ 60 ngày với chuyên môn, ≤ 180 ngày với manager)
- Ngày bắt đầu, địa điểm, hình thức làm việc

## Bước 2: Tính Toán Tổng Thu Nhập (Gross-to-Net)
Ví dụ lương gross 30 triệu/tháng, độc thân, không người phụ thuộc:
- BHXH 8% + BHYT 1.5% + BHTN 1% = 10.5% × 30 = 3.15 triệu
- Thu nhập chịu thuế = 30 - 3.15 - 11 (giảm trừ bản thân) = 15.85 triệu
- Thuế TNCN bậc 3 (10-18tr): 15% - 0.75 = 1.6275 triệu
- **Net ≈ 25.22 triệu**

Bảng minh họa tổng thu nhập năm:
| Khoản | /tháng | /năm |
|---|---|---|
| Lương gross | 30tr | 360tr |
| Thưởng tháng 13 | - | 30tr |
| KPI thưởng (tối đa) | - | 60tr |
| **Tổng package** | | **450tr** |

## Bước 3: Soạn Offer Letter Theo Cấu Trúc 9 Phần
1. Tiêu đề + ngày phát hành
2. Chúc mừng + tên ứng viên
3. Vị trí, phòng ban, báo cáo cho ai
4. Ngày bắt đầu + thời gian thử việc
5. **Lương + benefit (gross/net rõ ràng)**
6. Giờ làm việc + địa điểm + hình thức
7. Bảo mật, sở hữu trí tuệ, non-compete
8. Hạn xác nhận (thường 5-7 ngày)
9. Chữ ký CEO/HR Director + ô ký xác nhận

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Gmail MCP: gửi offer PDF qua email với link e-sign
- Drive MCP: lưu offer + countersigned trong folder hồ sơ NV
- Calendar MCP: tạo nhắc deadline phản hồi offer
- WebSearch: tra mức thuế TNCN, mức lương tối thiểu vùng 2026

**Fallback bằng API (e-sign + HRIS):**
```python
# Gửi offer qua DocuSign / VNeID Sign
import requests
envelope = {
    "documents": [{"name": "Offer.pdf", "fileBase64": pdf_b64}],
    "recipients": [{"email": uv_email, "name": uv_name, "tabs": signature_tabs}],
    "status": "sent"
}
requests.post("https://demo.docusign.net/restapi/v2.1/accounts/{}/envelopes".format(ACC),
    json=envelope, headers={"Authorization": f"Bearer {TOKEN}"})
```

## Bước 5: Output Format
- File `.docx` template có logo, font chuẩn công ty
- File `.pdf` xuất từ docx, có chữ ký số CEO
- Bảng salary breakdown đính kèm (Excel)
- Email template gửi kèm
- Lưu tại: `/outputs/Offer_<ten-UV>_<vi-tri>.pdf`

## Checklist Trước Khi Giao
- [ ] Tên, vị trí, ngày bắt đầu chính xác
- [ ] Lương gross/net + breakdown rõ
- [ ] BHXH/BHYT/BHTN đúng tỷ lệ
- [ ] Thuế TNCN tính đúng bậc lũy tiến
- [ ] Thời gian thử việc đúng luật
- [ ] Có điều khoản bảo mật + IP
- [ ] Có deadline xác nhận
- [ ] CEO/HR Director đã duyệt số liệu
- [ ] Sẵn HĐLĐ thử việc đi kèm
