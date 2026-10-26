---
name: ceo-customer-letter
description: |
  Viết thư CEO gửi khách hàng cho 3 tình huống: xin lỗi (apology), thông báo thay đổi (announcement), cảm ơn (thank you). Format chân thành, không corporate-speak.
  Kích hoạt khi người dùng nói: "thư CEO gửi khách", "customer letter", "letter từ CEO", "thư xin lỗi khách hàng", "thông báo khách hàng CEO", "apology letter", "thank you letter CEO", "thư khách hàng".
  Output là Markdown letter + email HTML.
---

# CEO Customer Letter — Thư Gửi Khách Hàng

## Mục Tiêu
3 thời điểm CEO PHẢI viết thư khách hàng: outage/sự cố, thay đổi lớn (giá, dịch vụ), thank you milestone. Skill này tạo thư đúng tone — chân thành chứ không corporate-speak.

## Khi Nào Dùng
- Sự cố downtime, data breach, lỗi sản phẩm
- Tăng giá, thay đổi terms
- Discontinue feature
- Milestone (1 năm cùng nhau, IPO)
- Thank you holiday season

## Bước 1: Xác Định Loại Thư
**Loại 1 - Apology**: có lỗi, phải xin lỗi
**Loại 2 - Announcement**: thông báo thay đổi (trung tính hoặc bad news)
**Loại 3 - Thank You**: cảm ơn, không sell

Mỗi loại có công thức khác nhau.

## Bước 2: Công Thức Cho Từng Loại

**Apology Letter Format:**
1. Acknowledge cụ thể chuyện gì xảy ra (1 đoạn)
2. Impact tới khách (1 đoạn)
3. What we did / will do (3-5 bullet cụ thể)
4. Compensation / remedy nếu có
5. Personal commitment từ CEO
6. Contact direct

KHÔNG dùng: "we apologize for any inconvenience", "issues" (dùng "outage", "bug"), passive voice.

**Announcement Format:**
1. Lý do (context)
2. Thay đổi gì cụ thể, từ khi nào
3. Tác động tới khách
4. Lựa chọn cho khách (grandfather, cancel free, migration help)
5. Liên hệ hỗ trợ

**Thank You Format:**
1. Specific milestone (1 năm cùng nhau, version X release)
2. Story 1 customer success cụ thể
3. What's next mà KH được hưởng lợi
4. Heartfelt thanks (không CTA bán)

## Bước 3: Tone Quy Tắc
- First person "I" (cá nhân CEO), không "we" hết
- Câu ngắn ≤ 18 từ
- Không jargon ("synergy", "leverage")
- Show empathy với customer pain
- Concrete > vague
- Sign personal name + chức vụ

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Gmail MCP: gửi mass email với merge tag {{first_name}}
- HubSpot MCP: pull customer list theo segment
- Intercom MCP: gửi qua in-app message
- Notion MCP: archive letter cho future ref
- WebSearch: ví dụ apology letter của Stripe/AirBnB

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Mass email với personalization
from googleapiclient.discovery import build
service = build('gmail', 'v1', credentials=creds)
for customer in customers:
    body = letter_template.format(name=customer['first_name'])
    # ... encode and send
```

## Bước 5: Output Format
- Markdown letter
- HTML email với inline CSS đẹp
- Plain text version (deliverability)
- Subject line A/B (3 variants)
- Send time recommendation
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/customer-letter-[type]-YYYY-MM-DD.md`

## Checklist Trước Khi Giao
- [ ] Đúng 1 trong 3 loại letter
- [ ] First person "I" (CEO)
- [ ] Không jargon corporate
- [ ] Apology có compensation cụ thể
- [ ] Có contact direct email CEO
- [ ] Test send tới 5 customer trước blast
