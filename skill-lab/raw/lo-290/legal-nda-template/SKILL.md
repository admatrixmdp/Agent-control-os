---
name: legal-nda-template
description: |
  Tạo Thoả thuận Bảo mật (NDA / Non-Disclosure Agreement) song ngữ Việt-Anh chuẩn pháp lý Việt Nam và quốc tế, dùng cho đối tác trong nước hoặc nước ngoài. Kích hoạt khi người dùng nói: "soạn NDA", "tạo thoả thuận bảo mật", "viết NDA song ngữ", "NDA tiếng Anh tiếng Việt", "hợp đồng bảo mật thông tin", "mutual NDA", "one-way NDA", "NDA đối tác nước ngoài", "soạn confidentiality agreement", "thoả thuận không tiết lộ". Output là file .docx song ngữ 2 cột Việt-Anh sẵn ký + PDF preview.
---

# Thoả Thuận Bảo Mật NDA Song Ngữ Việt-Anh

## Mục Tiêu
Cấp tốc tạo NDA chuẩn dùng được cho đối tác Việt Nam và nước ngoài (Mỹ, Singapore, EU, Nhật, Hàn) tránh phải thuê luật sư mỗi lần làm việc với bên mới. Tuân thủ BLDS 2015 (Điều 387 — bảo mật thông tin tiền hợp đồng) + Luật SHTT 2005 (bí mật kinh doanh).

## Khi Nào Dùng
- Trước khi chia sẻ tài chính, công nghệ, dữ liệu khách hàng với đối tác tiềm năng
- Trước khi nhờ freelancer / nhà thầu phụ làm việc với dữ liệu nhạy cảm
- Trước vòng gọi vốn với nhà đầu tư (M&A, Due Diligence)
- Khi tuyển dụng nhân sự cấp cao (C-level, R&D)
- Khi tham gia hội thảo / pitch / demo sản phẩm chưa launch

## Bước 1: Chọn Loại NDA
- **One-way NDA**: chỉ 1 bên tiết lộ (thường dùng khi pitch với NĐT)
- **Mutual NDA**: cả 2 bên cùng tiết lộ (đối tác chiến lược, JV)
- **Multilateral NDA**: 3+ bên (consortium, R&D chung)
Hỏi user: bên nào tiết lộ thông tin? Có cần cấm headhunt không?

## Bước 2: Thu Thập 8 Thông Tin Bắt Buộc
1. Tên đầy đủ + GPKD/Tax ID/Address của Disclosing Party
2. Tên đầy đủ + GPKD/Tax ID/Address của Receiving Party
3. Mục đích trao đổi (Purpose) — phải cụ thể, không "general business"
4. Định nghĩa Confidential Information (loại trừ gì)
5. Thời hạn bảo mật (thường 3-5 năm, bí mật kinh doanh có thể vô thời hạn)
6. Luật áp dụng (VN / Singapore / New York / English law)
7. Cơ quan giải quyết tranh chấp (Toà án / VIAC / SIAC / ICC)
8. Phạt vi phạm + bồi thường (thường USD 50,000 - 500,000 cho NDA quốc tế)

## Bước 3: Sinh NDA Song Ngữ 2 Cột
Layout: cột trái tiếng Việt, cột phải tiếng Anh, đánh số điều khoản trùng khớp.
Các điều bắt buộc:
- Điều 1: Định nghĩa / Definitions
- Điều 2: Nghĩa vụ bảo mật / Confidentiality Obligations
- Điều 3: Loại trừ / Exclusions (thông tin đã công khai, đã biết trước, được toà yêu cầu)
- Điều 4: Thời hạn / Term (Hiệu lực + thời gian bảo mật sau khi chấm dứt)
- Điều 5: Hoàn trả / Trả lại tài liệu / Return of Materials
- Điều 6: Không chuyển giao quyền / No License Granted
- Điều 7: Bồi thường + Phạt / Remedies (bao gồm Injunctive Relief)
- Điều 8: Luật áp dụng + tranh chấp / Governing Law & Disputes
- Điều 9: Điều khoản chung / Miscellaneous (Severability, Counterparts, e-signature)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: lưu NDA + lưu repository theo template
- Gmail MCP: gửi NDA cho đối tác kèm hướng dẫn ký
- DocuSign / HelloSign MCP: gửi e-signature cho 2 bên
- Notion MCP: lưu danh sách NDA đã ký vào database
- WebFetch: tra trang chính chủ đối tác để xác minh thông tin GPKD (dangkykinhdoanh.gov.vn cho VN, OpenCorporates cho global)

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Sinh NDA từ template Jinja2 + xuất .docx song ngữ
from docxtpl import DocxTemplate
from datetime import datetime, timedelta

doc = DocxTemplate("nda_bilingual_template.docx")
context = {
    "disclosing_party_vn": "Công ty CP ABC",
    "disclosing_party_en": "ABC Joint Stock Company",
    "receiving_party_vn": "XYZ Pte Ltd (Singapore)",
    "purpose": "Đánh giá khả năng hợp tác phân phối tại Đông Nam Á",
    "term_years": 5,
    "governing_law": "Vietnam",
    "dispute_forum": "VIAC",
    "effective_date": datetime.now().strftime("%d/%m/%Y"),
    "penalty_usd": 100000
}
doc.render(context)
doc.save(f"NDA_{context['receiving_party_vn']}_{datetime.now().strftime('%Y%m%d')}.docx")
```

## Bước 5: Output Format
- File `NDA_<doi-tac>_<yyyymmdd>.docx`: song ngữ 2 cột, font Times New Roman 12, sẵn chữ ký 2 bên
- File `NDA_<doi-tac>_<yyyymmdd>.pdf`: bản preview chống chỉnh sửa
- Tóm tắt 1 trang: các điểm cần đối tác lưu ý + thời hạn NDA
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/nda/`

## Checklist Trước Khi Giao
- [ ] Tên + GPKD + địa chỉ 2 bên chính xác (đối chiếu giấy phép)
- [ ] Purpose mô tả cụ thể, không chung chung
- [ ] Định nghĩa Confidential Information bao quát đủ (oral, written, electronic, observed)
- [ ] Có 5 trường hợp loại trừ chuẩn (already public, independently developed, etc.)
- [ ] Thời hạn rõ ràng + xử lý sau khi hết hạn
- [ ] Có Injunctive Relief (yêu cầu toà ngăn chặn ngay)
- [ ] Luật áp dụng + cơ quan tài phán khả thi (tránh chọn toà nước không có hiệp định với VN)
- [ ] 2 ngôn ngữ thống nhất về nghĩa (ghi rõ bản nào ưu tiên khi mâu thuẫn)
