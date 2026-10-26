---
name: ceo-press-release
description: |
  Viết thông cáo báo chí chuẩn báo Việt Nam — headline kéo click, lead 5W1H, body 3 đoạn, quote CEO, boilerplate, contact. Phù hợp gửi VnExpress, Forbes Vietnam, CafeF.
  Kích hoạt khi người dùng nói: "thông cáo báo chí", "press release", "viết PR ra mắt", "thông báo cho báo", "press kit", "news release", "media release", "thông cáo cho báo chí".
  Output là Word .docx + Markdown.
---

# CEO Press Release — Thông Cáo Báo Chí

## Mục Tiêu
Mỗi lần ra mắt sản phẩm/raise vốn/M&A, công ty cần press release chuẩn để báo Việt Nam đăng. Format sai 1 chi tiết = bị từ chối. Skill này tạo bản chuẩn trong 20 phút thay vì 2 ngày.

## Khi Nào Dùng
- Ra mắt sản phẩm mới
- Công bố funding round
- M&A / strategic partnership
- Bổ nhiệm CXO mới
- Đạt milestone lớn (1M user, IPO, expansion)
- Crisis response (cùng template khác)

## Bước 1: Thu Thập Thông Tin
- Tin gì? (1 câu)
- Tại sao quan trọng (3 lý do)
- Số liệu cụ thể (round size, % growth, headcount)
- Quote CEO (1-2 câu)
- Quote đối tác/investor (1 câu, nếu có)
- Boilerplate công ty (50-80 từ)
- Contact PR (email, phone)

## Bước 2: Cấu Trúc Chuẩn
```
THÔNG CÁO BÁO CHÍ
[Để đăng ngay / Embargo đến HH:MM ngày DD/MM]

[HEADLINE: 8-12 từ, chứa keyword chính]
[SUB-HEADLINE: 15-25 từ bổ sung context]

[CITY, NGÀY] — [Lead paragraph: 5W1H trong 30-40 từ]

[Body 1: chi tiết tin chính]

[Quote CEO: "..." - tên CEO, chức vụ]

[Body 2: context ngành / lý do quan trọng]

[Quote đối tác/khách hàng (nếu có)]

[Body 3: what's next]

ABOUT [COMPANY]
[Boilerplate 50-80 từ]

LIÊN HỆ:
[Tên] - [Title]
[Email] - [Phone]

###
```

## Bước 3: Quy Tắc Báo Chí VN
- Headline ≤ 12 từ, có động từ mạnh
- Lead trong 30-40 từ trả lời WHO/WHAT/WHEN/WHERE/WHY
- Body 3 đoạn × 60-80 từ
- Quote đặt trong nháy kép, attribution sau
- Tổng 400-500 từ
- Tránh từ marketing rỗng ("đột phá", "tiên phong" không có data)
- Có ảnh kèm (logo + ảnh CEO + sản phẩm)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tham khảo press release tương tự trên VnExpress/CafeF
- Gmail MCP: gửi blast cho danh sách 30-50 nhà báo
- Notion MCP: lưu archive PR + KPI media coverage
- Google Drive MCP: lưu ảnh + logo dùng kèm
- Canva MCP: tạo press kit image

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Gmail blast với personalization
from email.mime.text import MIMEText
for journo in journalists:
    msg = MIMEText(pr_body.format(name=journo['first']))
    msg['Subject'] = headline
    msg['To'] = journo['email']
    # Send via Gmail API
```

## Bước 5: Output Format
- Word `.docx` chuẩn báo chí
- Markdown để paste vào CMS
- Press kit zip (release.docx + logo.png + CEO_photo.jpg + product.jpg)
- Email pitch ngắn (50 từ) gửi journo
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/pr-[topic]-YYYY-MM-DD/`

## Checklist Trước Khi Giao
- [ ] Headline ≤ 12 từ, có keyword
- [ ] Lead trả lời 5W1H
- [ ] Tổng 400-500 từ
- [ ] Có quote CEO + 1 quote khác
- [ ] Boilerplate cập nhật
- [ ] Có contact + ảnh kèm
- [ ] Đã embargo (nếu cần)
