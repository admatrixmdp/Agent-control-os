---
name: cs-refund-policy-writer
description: |
  Viết chính sách hoàn tiền chuẩn pháp lý Việt Nam (Luật Bảo vệ NTD 2023, Luật TM, Nghị định 52) — đủ điều kiện, thời gian, phương thức, ngoại lệ — phù hợp ngành TMĐT/SaaS/F&B. Dùng skill này khi người dùng yêu cầu: "viết chính sách hoàn tiền", "refund policy", "chính sách đổi trả", "điều khoản hoàn tiền", "viết policy refund Shopee", "chính sách hoàn tiền SaaS", "review refund policy". Output là Markdown + HTML + PDF policy hoàn chỉnh.
---

# CS Refund Policy Writer

## Mục Tiêu
Soạn chính sách hoàn tiền minh bạch, bảo vệ doanh nghiệp khỏi rủi ro pháp lý/lạm dụng, đồng thời đảm bảo quyền lợi NTD theo Luật BVQLNTD 2023 — sẵn sàng đăng website, Shopee, app.

## Khi Nào Dùng
- Doanh nghiệp mới chưa có policy hoặc policy cũ lỗi thời
- Bị khách kiện/khiếu nại do policy không rõ ràng
- Mở rộng kênh bán (thêm Shopee/Lazada) cần policy chuẩn sàn
- Launch SaaS có subscription cần refund prorate
- Audit pháp lý phát hiện policy thiếu điều khoản

## Bước 1: Thu Thập Thông Tin Doanh Nghiệp
Hỏi user:
- **Ngành**: TMĐT vật lý / SaaS / khóa học / F&B / dịch vụ
- **Sản phẩm chính**: gì, giá trị bao nhiêu
- **Kênh bán**: website, Shopee, Tiki, hotline, app
- **Phương thức thanh toán**: COD, banking, momo, thẻ
- **Quyền refund hiện tại**: từ chối? 100%? prorate?

## Bước 2: Xây 7 Mục Bắt Buộc Của Policy
1. **Phạm vi áp dụng**: sản phẩm/dịch vụ nào được refund
2. **Điều kiện hoàn tiền**: hàng còn nguyên tem, trong 7-30 ngày, có lý do
3. **Trường hợp KHÔNG refund**: hàng đã dùng, hàng giảm giá, dịch vụ đã consume
4. **Quy trình yêu cầu**: form, ảnh, ticket
5. **Thời gian xử lý**: review 1-3 ngày, hoàn tiền 3-7 ngày
6. **Phương thức hoàn**: về tài khoản gốc, voucher, ví
7. **Liên hệ khiếu nại**: hotline, email, địa chỉ

## Bước 3: Đối Chiếu Pháp Lý Việt Nam
- **Luật BVQLNTD 2023** (hiệu lực 1/7/2024): Điều 38 — quyền đơn phương chấm dứt hợp đồng từ xa trong 7 ngày
- **Nghị định 52/2013/NĐ-CP**: TMĐT
- **Luật Thương mại 2005**: bảo hành sản phẩm
- **Nghị định 98/2020/NĐ-CP**: xử phạt vi phạm quyền lợi NTD

Cảnh báo user: KHÔNG được đặt điều khoản trái luật (ví dụ: "miễn hoàn tiền mọi trường hợp" — vô hiệu).

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tra cứu cập nhật mới Luật BVQLNTD 2023, hướng dẫn Bộ Công Thương
- WebFetch: lấy policy mẫu Shopee/Tiki/Lazada để align
- Google Sheets: bảng so sánh policy đối thủ
- Gmail MCP: gửi draft cho legal review trước khi publish
- Notion/Drive MCP: lưu version control policy

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Crawl policy refund 5 đối thủ + so sánh
import requests
from bs4 import BeautifulSoup
URLS = ["https://shopee.vn/policies/refund", "https://tiki.vn/refund-policy"]
for url in URLS:
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    sections = [h.get_text() for h in soup.find_all(["h2", "h3"])]
    print(url, sections)
```

## Bước 5: Output Format
- **Markdown `RefundPolicy_v1.md`**: dễ paste lên CMS
- **HTML responsive** đăng website
- **PDF** in dùng nội bộ + đính kèm hợp đồng
- **Bản tóm tắt 1 trang** cho agent CS đọc nhanh
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-refund-policy-writer/output/`

## Checklist Trước Khi Giao
- [ ] Đủ 7 mục bắt buộc
- [ ] Tuân thủ Luật BVQLNTD 2023, không có điều khoản vô hiệu
- [ ] Ngôn ngữ rõ ràng, không lạm dụng "trường hợp đặc biệt"
- [ ] Có ví dụ cụ thể "Trường hợp A: ... Trường hợp B: ..."
- [ ] Legal/luật sư đã review (nếu có)
- [ ] Đăng đúng nơi: footer web + trang policy + Help Center
