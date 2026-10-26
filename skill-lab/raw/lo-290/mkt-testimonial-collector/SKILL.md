---
name: mkt-testimonial-collector
description: |
  Thu thập testimonial khách hàng qua email + form chuẩn — pull quote, ảnh, video ngắn, để dùng cho ads/LP/social. Kích hoạt khi người dùng nói: "thu testimonial", "xin testimonial KH", "testimonial collector", "form testimonial", "video review KH", "thu thập feedback tốt", "lấy testimonial", "testimonial campaign". Output là form + email template + tracker.
---

# Thu Thập Testimonial Khách Hàng

## Mục Tiêu
Mỗi tháng có 20-50 testimonial mới chất lượng (text/ảnh/video) để dùng cross-channel, tăng trust + CR LP/Ads 30-60%.

## Khi Nào Dùng
- Brand mới chưa nhiều social proof
- Trước launch sản phẩm/campaign
- Sau khi giao hàng / hoàn thành dịch vụ
- KH thân thiết lâu năm
- Chuẩn bị event/PR

## Bước 1: Brief Campaign
Hỏi:
1. Sản phẩm + KH target
2. Loại testimonial cần (text/ảnh selfie/video 30-60s)
3. Số lượng/tháng
4. Incentive (voucher / spotlight / quà)
5. Quyền sử dụng (đăng ads / LP / social)
6. Mẫu testimonial muốn (focus result hay cảm xúc)

## Bước 2: Soạn Email + Form
**Email** 200 từ:
- Cảm ơn cá nhân
- Lý do xin testimonial (giúp KH khác quyết định)
- 3 câu hỏi gợi ý (để KH dễ trả lời)
- Link form 2 phút
- Quyền sử dụng minh bạch
- Incentive

**Form** 5-7 câu:
1. Tên + chức vụ + công ty (cho B2B)
2. Lý do mua [sản phẩm]
3. 3 điều thích nhất
4. Kết quả đạt được (có số liệu thì tốt)
5. Khuyên ai nên mua
6. Upload ảnh chân dung / sản phẩm sử dụng
7. Video selfie 30s (optional - thưởng x3)

## Bước 3: Curate & Format
Mỗi testimonial format thành 4 dạng:
- Pull quote ngắn (1-2 dòng) cho LP/ads
- Quote dài (5-7 dòng) + ảnh + tên cho LP
- Carousel IG/FB
- Video clip 15s cho Reel/TikTok

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Typeform/Google Forms MCP: form đẹp + logic skip
- Gmail MCP: gửi cá nhân hóa
- Senja/Testimonial.to MCP (nếu có): video testimonial
- Sheets MCP: tracker
- Notion MCP: testimonial library

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tự động gửi email bulk personalized
import csv, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
with open('happy_customers.csv') as f:
    for row in csv.DictReader(f):
        msg = MIMEMultipart()
        msg['To']=row['email']; msg['Subject']='Xin {} 2 phút'.format(row['name'])
        body = template.format(name=row['name'], product=row['product'])
        msg.attach(MIMEText(body,'html'))
        smtp.send_message(msg)
```

## Bước 5: Output Format
- Form testimonial (Typeform/Google Forms)
- 3 email template (gửi / nhắc / cảm ơn)
- Tracker Sheet
- Library Notion lưu testimonial sẵn dùng
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Form <2 phút điền
- [ ] 3 câu hỏi gợi ý dễ trả lời
- [ ] Có upload ảnh/video
- [ ] Quyền sử dụng rõ
- [ ] Tracker cá nhân hóa
- [ ] Có chuỗi nhắc nếu chưa response
