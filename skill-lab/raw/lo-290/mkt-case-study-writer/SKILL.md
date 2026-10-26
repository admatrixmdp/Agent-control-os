---
name: mkt-case-study-writer
description: |
  Viết case study khách hàng theo cấu trúc Problem → Solution → Result + data cho doanh nghiệp Việt Nam (B2B/B2C). Tự động phỏng vấn KH và soạn 800-1500 từ. Kích hoạt khi người dùng nói: "viết case study", "case study khách hàng", "success story", "customer case", "viết bài chia sẻ KH", "case study B2B", "câu chuyện thành công", "case study marketing". Output là Markdown + PDF design.
---

# Viết Case Study Khách Hàng

## Mục Tiêu
Mỗi tháng có 1-2 case study chất lượng dùng cho sales pitch, website, social, ads — tăng conversion lead 30-50% so với chỉ có testimonial chữ.

## Khi Nào Dùng
- B2B SaaS / dịch vụ cần social proof
- Khóa học/coaching có case học viên thành công
- Ecom có KH chuyển hóa rõ
- PR + pitch báo
- Sales enablement

## Bước 1: Chọn Customer & Phỏng Vấn
Hỏi:
1. Tên KH + ngành + size
2. Sản phẩm họ dùng
3. Người liên hệ phỏng vấn
4. Kết quả đạt được (số liệu)
5. Có cho phép public name không
6. Asset có sẵn (logo, ảnh, quote)

Bộ câu hỏi phỏng vấn 10-15 câu:
- Trước khi dùng [sản phẩm], pain point lớn nhất?
- Đã thử giải pháp nào?
- Tại sao chọn [sản phẩm]?
- Onboarding ra sao?
- Kết quả sau X tháng (số liệu)?
- 3 lợi ích lớn nhất?
- Khuyên ai nên dùng?
- 1 câu quote.

## Bước 2: Cấu Trúc Case Study
Format chuẩn 800-1500 từ:
1. **Headline** + result chính (số liệu nổi bật)
2. **About** customer (1 đoạn: ngành, size, geographic)
3. **Challenge** (vấn đề trước khi dùng, có quote)
4. **Why us** (tại sao chọn)
5. **Solution** (cách triển khai, có ảnh/video)
6. **Result** (3-5 metric tăng, bảng before/after)
7. **Quote** lớn cuối
8. **About** brand + CTA

## Bước 3: Viết & Thiết Kế
Quy tắc:
- 60% câu chuyện, 40% data
- Số liệu cụ thể (không "tăng đáng kể")
- Trích quote nguyên văn
- Tone của founder customer
- Ảnh thật (founder, team, sản phẩm sử dụng)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebFetch: lấy thông tin công khai về KH (website, LinkedIn)
- Notion MCP: case study library
- Google Drive MCP: lưu PDF
- Gmail MCP: gửi consent + draft cho KH duyệt
- Loom MCP: video case study tùy chọn

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tự gom data customer từ CRM để chèn vào case
import requests
def get_customer_metrics(customer_id):
    crm = requests.get(f'https://api.hubapi.com/crm/v3/objects/contacts/{customer_id}',
      headers={'Authorization':f'Bearer {TOKEN}'}).json()
    deals = requests.get(f'https://api.hubapi.com/crm/v3/objects/deals',
      params={'associations':'contact','contactId':customer_id},
      headers={'Authorization':f'Bearer {TOKEN}'}).json()
    return {'contact':crm, 'deals':deals['results']}
```

## Bước 5: Output Format
- File `.md` case study đầy đủ
- File PDF thiết kế đẹp cho sales deck
- Bản tóm tắt 100 từ cho slide
- Tweet thread + LinkedIn post lấy từ case
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Có sự đồng ý của KH
- [ ] Số liệu cụ thể có nguồn
- [ ] 2-3 quote nguyên văn
- [ ] Ảnh/asset thật
- [ ] Cấu trúc Problem→Solution→Result rõ
- [ ] CTA cuối phù hợp
- [ ] Đã review với KH trước publish
