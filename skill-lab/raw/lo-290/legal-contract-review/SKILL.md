---
name: legal-contract-review
description: |
  Review hợp đồng kinh tế/dịch vụ chuẩn pháp lý Việt Nam, đánh dấu red flags, chèn comment sửa từng điều khoản theo Luật Thương mại 2005, Luật Dân sự 2015 và Luật Doanh nghiệp 2020. Kích hoạt khi người dùng nói: "review hợp đồng", "đọc hộ hợp đồng", "soát hợp đồng", "kiểm tra điều khoản", "tìm rủi ro hợp đồng", "redline contract", "góp ý hợp đồng", "thẩm định hợp đồng", "hợp đồng này có vấn đề gì", "phân tích hợp đồng". Output là file .docx có Track Changes + bảng red flag và bản tóm tắt rủi ro PDF.
---

# Review Hợp Đồng Chuẩn Pháp Lý Việt Nam

## Mục Tiêu
Giúp doanh nghiệp Việt Nam đọc hợp đồng từ đối tác/khách hàng trong 15-30 phút thay vì thuê luật sư mất 3-7 ngày và 5-20 triệu đồng. Output là bản hợp đồng đã có Track Changes + bảng red flags + đề xuất chỉnh sửa cụ thể từng điều khoản.

## Khi Nào Dùng
- Nhận hợp đồng từ NCC/khách hàng cần ký gấp
- Soát hợp đồng mẫu của công ty trước khi triển khai diện rộng
- Đánh giá rủi ro pháp lý trước khi M&A hoặc hợp tác lớn
- Đào tạo nhân viên mới phòng Pháp chế / Mua hàng
- Tự rà soát hợp đồng cũ để renegotiate

## Bước 1: Phân Loại Hợp Đồng
Xác định loại hợp đồng để áp dụng đúng luật:
- HĐ mua bán hàng hoá → Luật Thương mại 2005 (Điều 24-73)
- HĐ dịch vụ → Bộ luật Dân sự 2015 (Điều 513-526)
- HĐ đại lý/phân phối → Luật Thương mại 2005 (Điều 166-177)
- HĐ thuê tài sản → BLDS 2015 (Điều 472-493)
- HĐ hợp tác kinh doanh BCC → Luật Đầu tư 2020

## Bước 2: Quét 10 Red Flag Bắt Buộc
Đối chiếu hợp đồng với checklist 10 điểm:
1. Thẩm quyền ký (người ký có đúng đại diện pháp luật / được uỷ quyền hợp lệ không?)
2. Đối tượng hợp đồng có rõ ràng, đo lường được không?
3. Giá + phương thức thanh toán + tiền tệ + thuế VAT
4. Thời hạn giao hàng / nghiệm thu + tiêu chí chấp nhận
5. Điều khoản phạt vi phạm (max 8% giá trị HĐ theo Luật TM 2005 Điều 301)
6. Bồi thường thiệt hại (có giới hạn trần không?)
7. Bất khả kháng (Force Majeure) + thông báo
8. Bảo mật + sở hữu trí tuệ
9. Chấm dứt hợp đồng (đơn phương / theo thoả thuận)
10. Luật áp dụng + cơ quan giải quyết tranh chấp (Toà án VN / VIAC / SIAC)

## Bước 3: Chèn Comment + Đề Xuất Sửa
Với mỗi vấn đề tìm được, tạo comment dạng:
```
[RỦI RO CAO] Điều 8.2 quy định phạt 30% giá trị HĐ — VƯỢT trần 8% theo Luật TM 2005 Điều 301.
ĐỀ XUẤT: "Mức phạt vi phạm tối đa 8% giá trị nghĩa vụ bị vi phạm".
```
Phân loại: RỦI RO CAO (đỏ) / TRUNG BÌNH (vàng) / THẤP (xanh).

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: tải hợp đồng gốc + lưu bản đã review
- Gmail MCP: gửi bản review về cho stakeholders kèm summary
- Notion MCP: lưu hợp đồng đã review vào kho contract repository
- DocuSign / Canva MCP: sau khi sửa xong, tạo bản ký số
- WebFetch: tra cứu án lệ liên quan tại thuvienphapluat.vn / congbobanan.toaan.gov.vn
- WebSearch: tìm điều luật mới nhất hoặc dự thảo sửa đổi

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Trích văn bản từ .docx + đối chiếu với điều luật
from docx import Document
import re

doc = Document("HD_NCC.docx")
red_flags = []
penalty_pattern = re.compile(r"phạt.*?(\d+)\s*%", re.IGNORECASE)
for para in doc.paragraphs:
    m = penalty_pattern.search(para.text)
    if m and int(m.group(1)) > 8:
        red_flags.append({
            "clause": para.text[:100],
            "issue": f"Phạt {m.group(1)}% vượt trần 8% (Luật TM 2005 Đ.301)",
            "level": "CAO"
        })
```

## Bước 5: Output Format
- File `.docx` có Track Changes + Comment (mở bằng Word/Google Docs nhìn rõ sửa gì)
- Bảng Excel `red_flags.xlsx` cột: Điều khoản | Nội dung | Mức rủi ro | Cơ sở pháp lý | Đề xuất sửa
- File `.pdf` 1-2 trang tóm tắt cho CEO: Top 5 rủi ro + khuyến nghị ký / chỉnh sửa / từ chối
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/contract-review-<ten-doi-tac>-<yyyymmdd>/`

## Checklist Trước Khi Giao
- [ ] Đã kiểm tra thẩm quyền ký của cả 2 bên (GPKD + uỷ quyền)
- [ ] Đã đối chiếu mức phạt với Luật TM Đ.301 (≤8%)
- [ ] Đã rà clause bất khả kháng + thông báo trong N ngày
- [ ] Đã xác minh cơ quan giải quyết tranh chấp khả thi
- [ ] Đã đánh dấu mọi điều khoản mơ hồ ("hợp lý", "phù hợp" mà không định lượng)
- [ ] Bản tóm tắt PDF không quá 2 trang
- [ ] Có khuyến nghị rõ: KÝ / SỬA / TỪ CHỐI
