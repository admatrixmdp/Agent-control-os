---
name: mkt-seo-backlink-prospecting
description: |
  Tìm cơ hội backlink chất lượng cao và soạn email outreach cá nhân hóa cho website doanh nghiệp Việt Nam. Tự động lọc theo DR, ngách, ngôn ngữ và sinh 5-10 mẫu email theo từng loại link (guest post, broken link, resource page). Kích hoạt khi người dùng nói: "tìm backlink", "backlink prospecting", "xin guest post", "outreach SEO", "email xin link", "tìm cơ hội link building", "tăng DR website", "kéo backlink chất lượng". Output là Excel danh sách prospect + email templates.
---

# Backlink Prospecting + Email Outreach

## Mục Tiêu
Tăng tốc khâu tìm và tiếp cận đối tác backlink — từ 1 ngày làm thủ công xuống 1 giờ với 50-100 prospect, mỗi prospect có email contact và template outreach đã cá nhân hóa.

## Khi Nào Dùng
- Triển khai SEO off-page lần đầu
- Mở rộng authority ngách mới
- Đang đuổi top 3 và cần đẩy DR
- Có content asset mới (báo cáo, ebook) cần link
- Phục hồi link bị mất sau migration

## Bước 1: Xác Định Loại Backlink
Hỏi user 3 thứ:
1. Trang đích cần link (URL + anchor mong muốn)
2. Ngách + ngôn ngữ
3. Loại tactic: Guest post / Broken link / Resource page / HARO / Skyscraper / Niche edit

## Bước 2: Sinh Footprint Tìm Prospect
Dựa loại tactic, sinh footprint Google. Ví dụ guest post:
- `"viết cho chúng tôi" + [ngách]`
- `"đăng bài khách" + [ngách]`
- `inurl:write-for-us [ngách]`
Resource page:
- `intitle:"resources" [ngách]`
- `intitle:"useful links" [ngách]`
Dùng WebSearch sinh 100-200 URL ứng viên.

## Bước 3: Đánh Giá Và Chấm Điểm Prospect
Mỗi prospect chấm 0-100 dựa:
- Relevance ngách (40%)
- Authority/DR ước tính (30%)
- Traffic ước tính (15%)
- Khả năng phản hồi (15%)
Lọc giữ top 50 (>= 60 điểm).

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tìm footprint, kiểm tra contact page
- WebFetch: lấy email từ trang Contact/About
- Gmail MCP: tạo draft email outreach hàng loạt
- Google Sheets MCP: tracker outreach (gửi/mở/reply/link)
- Notion MCP: lưu database prospect

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Gửi email outreach bằng Gmail API
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64
msg = MIMEText(body_text)
msg['to'] = prospect_email
msg['subject'] = subject_line
raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
service.users().messages().send(userId='me', body={'raw': raw}).execute()
```

## Bước 5: Output Format
- File `.xlsx` `Backlink_Prospects_<domain>.xlsx`:
  - Sheet 1: Prospect list (URL, contact email, DR, score, status)
  - Sheet 2: Email templates (5 mẫu/tactic)
  - Sheet 3: Tracker (sent/opened/replied/linked)
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Tối thiểu 50 prospect đã lọc
- [ ] Mỗi prospect có email contact
- [ ] Đã chấm điểm theo 4 tiêu chí
- [ ] 5+ email template cá nhân hóa
- [ ] Có script follow-up sau 5-7 ngày
- [ ] Đã setup tracker để đo hiệu quả
