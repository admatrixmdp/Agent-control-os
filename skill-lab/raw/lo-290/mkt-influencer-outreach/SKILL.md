---
name: mkt-influencer-outreach
description: |
  Outreach KOL/KOC cho doanh nghiệp Việt Nam — soạn email/inbox cá nhân hóa và brief hợp tác chi tiết (gift/PR/paid). Tự động lọc influencer theo ngách, engagement và phù hợp brand. Kích hoạt khi người dùng nói: "outreach KOL", "tìm influencer", "email KOC", "brief hợp tác influencer", "KOL marketing", "tìm KOC TikTok IG", "viết tin nhắn KOL", "đàm phán KOL". Output là Excel danh sách + email/DM template + brief PDF.
---

# Outreach KOL/KOC + Brief Hợp Tác

## Mục Tiêu
Mỗi tháng tiếp cận 50-100 KOL/KOC chuẩn ngách, đạt tỷ lệ phản hồi 20-40% và book được 5-15 deal phù hợp ngân sách (gift/PR/paid).

## Khi Nào Dùng
- Launch sản phẩm mới
- Mở rộng audience qua influencer
- TikTok Shop cần affiliate
- Cần social proof từ KOL/KOC
- Campaign theo mùa (Tết, 8/3, BFCM)

## Bước 1: Xác Định Tiêu Chí Influencer
Hỏi:
1. Ngành/sản phẩm
2. Audience mục tiêu
3. Budget/người (gift/0đ → 50tr+)
4. Loại hợp tác (post/video/livestream/affiliate)
5. Số influencer cần (10/50/100)
6. KPI (reach/sales/UGC)
7. Tier ưu tiên (nano <10k, micro 10-100k, macro 100k-1M, mega 1M+)

## Bước 2: Tìm & Lọc Influencer
Dùng WebSearch + WebFetch tìm theo hashtag, ngách, location. Lọc theo:
- Engagement rate >3% (nano), >2% (macro)
- Audience VN >70%
- Niche phù hợp brand
- Chưa hợp tác đối thủ trong 60 ngày
- Quality content (không spam giveaway)

## Bước 3: Soạn Outreach Cá Nhân Hóa
Template 4 phần:
1. Câu mở khen cụ thể (không chung chung) — đề cập 1 video/post cụ thể
2. Lý do reach (sản phẩm fit với content họ)
3. Offer rõ ràng (gift + commission/paid)
4. CTA (reply/đặt lịch call)

3 variant: cho Nano, Micro, Macro.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tìm influencer theo ngách
- WebFetch: lấy profile + engagement
- Gmail MCP: gửi outreach hàng loạt cá nhân hóa
- Google Sheets MCP: tracker outreach
- Notion MCP: database KOL CRM
- Slack MCP: notify khi có reply

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tự động gửi email cá nhân hóa hàng loạt
import csv, smtplib
from email.mime.text import MIMEText
with open('kol_list.csv') as f:
    for row in csv.DictReader(f):
        body = template.format(name=row['name'],
          video_link=row['recent_video'])
        msg = MIMEText(body)
        msg['To']=row['email']; msg['Subject']=subject
        smtp.send_message(msg)
```

## Bước 5: Output Format
- File `.xlsx` danh sách KOL có cột: tên, platform, follower, ER, contact, tier, status
- 3 email/DM template + 3 follow-up
- Brief hợp tác `.pdf`: scope, deliverable, deadline, payment, T&C
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Danh sách 50+ KOL đã lọc
- [ ] Mỗi KOL có contact (email/phone/inbox)
- [ ] Email cá nhân hóa với chi tiết riêng
- [ ] Brief có scope + KPI + payment rõ
- [ ] Follow-up 2-3 lần
- [ ] Tracker đầy đủ status
