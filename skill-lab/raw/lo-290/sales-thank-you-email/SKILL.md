---
name: sales-thank-you-email
description: |
  Email cảm ơn sau meeting với recap, value-add, next step rõ ràng — gửi trong 2h. Trigger phrases: "thank you email", "email sau meeting", "email cảm ơn KH", "recap email", "follow-up sau call", "post-meeting email", "email sau demo", "soạn email cảm ơn sales", "next step email", "summary email khách hàng". Output là Markdown template + bộ 5 biến thể theo stage.
---

# Post-Meeting Thank You Email

## Mục Tiêu
Tăng meeting → next-step conversion >70% bằng email cảm ơn sent trong 2h sau meeting, có recap pain + value confirmed + next step rõ ràng — biến momentum trở thành commitment.

## Khi Nào Dùng
- Sau cold call connect
- Sau discovery call
- Sau demo
- Sau executive meeting
- Sau close-won

## Bước 1: Quy tắc Gửi
- Trong 2h sau meeting (muộn = mất momentum)
- Reply trên thread cũ nếu có (cùng subject)
- CC champion + relevant attendees
- Tránh forward sang internal kèm KH

## Bước 2: Template 5 Phần (max 150 từ)

**A. Cảm ơn (1 câu)**: "Cảm ơn anh Minh dành 30 phút sáng nay."

**B. Recap Pain (2-3 câu)**:
"Anh đã chia sẻ 3 ưu tiên:
1. Forecast accuracy 70% → target 90%
2. AE tốn 2h/ngày admin
3. Onboard sales 6 tháng → muốn 3 tháng"

**C. Recap Value (2-3 câu)**:
"Em đã chia sẻ cách <sản phẩm> giải quyết:
- Forecast bằng AI signal: 88% accuracy KH X
- Auto-log activity: cắt 1.5h/ngày
- Onboard playbook: 90 ngày to quota"

**D. Next Step (1-2 câu, RÕ RÀNG)**:
"Em đề xuất next step: demo sâu cho team anh thứ 5 10h, 45 phút. Anh confirm em book."

**E. Soft close (1 câu)**:
"Em đã attach case study công ty Y cùng size — anh xem trước được không?"

## Bước 3: Personalize 3 Yếu tố
Mỗi email PHẢI có:
- 1 chi tiết cá nhân meeting nhắc (vd "anh nhắc team mới hire 5 sales")
- 1 attachment giá trị (case study, ROI calc, article)
- 1 specific next step với time đề xuất

Tránh template chung chung.

## Bước 4: 5 Biến thể theo Stage

**Post-Discovery**: focus pain confirmation + demo CTA
**Post-Demo**: focus value confirmation + proposal CTA
**Post-Proposal**: focus address objection + closing CTA
**Post-Negotiation**: focus terms confirmation + signature CTA
**Post-Close**: focus celebration + handover CSM

Mỗi biến thể có template riêng.

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Gmail/Outlook MCP: gửi từ thread cũ, CC champion
- Salesforce/HubSpot MCP: log email vào activity
- Gong MCP: pull pain points từ call transcript
- Calendar MCP: book next step trực tiếp trong email

**Fallback API:**
```python
# Gmail thread reply
import base64
from email.mime.text import MIMEText
msg = MIMEText(body)
msg["To"] = prospect_email
msg["Subject"] = original_subject  # reply trên thread cũ
msg["In-Reply-To"] = original_msg_id
msg["References"] = original_msg_id
raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
requests.post("https://gmail.googleapis.com/gmail/v1/users/me/messages/send",
    headers={"Authorization": f"Bearer {token}"},
    json={"raw": raw, "threadId": thread_id})
```

## Bước 6: Output Format
- **File 1**: `thankyou_email_template.md` — 5 phần master
- **File 2**: `thankyou_email_variants.md` — 5 biến thể theo stage
- **File 3**: `thankyou_email_examples.md` — 3 ví dụ filled cho industry khác nhau
- **File 4**: `personalize_checklist.md` — 3-yếu-tố check
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Gửi trong 2h sau meeting
- [ ] <150 từ
- [ ] Có 3 personalize element
- [ ] Next step có time cụ thể
- [ ] Reply trên thread cũ
- [ ] Có attachment giá trị
- [ ] Log CRM trong 1h
