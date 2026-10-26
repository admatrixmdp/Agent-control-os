---
name: cs-csat-survey
description: |
  Thiết kế và triển khai survey CSAT/CES/NPS sau khi đóng ticket CSKH — câu hỏi chuẩn, kênh gửi (email/SMS/Zalo), phân tích kết quả, action plan. Dùng skill này khi người dùng yêu cầu: "tạo CSAT survey", "đo hài lòng khách hàng", "khảo sát sau ticket", "CES survey", "NPS khách hàng", "survey post-call", "đo lường chất lượng CS", "feedback form khách". Output là form HTML + email template + Excel báo cáo.
---

# CS CSAT / CES Survey Designer

## Mục Tiêu
Thiết kế survey ngắn (1-3 câu) gửi sau mỗi ticket để đo CSAT (mức hài lòng), CES (mức dễ dàng), NPS (mức giới thiệu) — phục vụ KPI agent + cải tiến quy trình.

## Khi Nào Dùng
- Chưa có hệ thống đo CSAT, sếp hỏi không trả lời được
- Có CSAT nhưng tỷ lệ response < 10%, không representative
- Cần KPI agent dựa trên feedback khách
- Sau khi launch sản phẩm/quy trình mới, muốn đo phản ứng
- Setup quarterly business review cần số liệu khách

## Bước 1: Chọn Loại Survey Phù Hợp
- **CSAT** (Customer Satisfaction): "Bạn hài lòng với hỗ trợ vừa rồi?" — thang 1-5 sao
- **CES** (Customer Effort Score): "Mức độ dễ dàng để được hỗ trợ?" — thang 1-7
- **NPS** (Net Promoter Score): "Khả năng bạn giới thiệu cho bạn bè?" — thang 0-10

→ Khuyến nghị: CSAT sau mọi ticket, NPS 1 lần/quý, CES sau onboarding/migration.

## Bước 2: Thiết Kế Câu Hỏi
Quy tắc:
- 1 câu chính + 1 câu mở (tùy chọn) → response rate cao
- Câu mở: "Có điều gì chúng tôi nên cải thiện?" (chỉ khi điểm ≤ 3)
- Khen ngợi agent: "Agent {ten_agent} hỗ trợ bạn thế nào?"

Mẫu CSAT VN:
```
Bạn hài lòng với hỗ trợ từ {ten_agent}?
[1] Rất không hài lòng  [2] Không hài lòng  [3] Bình thường
[4] Hài lòng  [5] Rất hài lòng

Bạn muốn góp ý gì? (Không bắt buộc)
[________________________]
```

## Bước 3: Chọn Kênh & Thời Điểm Gửi
- **Email**: gửi 1h sau khi đóng ticket, subject "Đánh giá hỗ trợ — 30 giây"
- **Zalo OA**: gửi 30 phút sau, dạng button 1-5
- **SMS**: chỉ với ticket VIP/high-value
- **Pop-up trong app**: ngay khi đóng chat

Quy tắc: 1 KH chỉ nhận 1 survey / 7 ngày để tránh spam.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Gmail MCP: tạo template + draft survey email batch
- Google Sheets: thu kết quả survey, dashboard auto-update
- Slack MCP: alert real-time khi có điểm 1-2 sao (Detractor)
- WebSearch: best practice CSAT/NPS Vietnamese context
- WebFetch: tham khảo form Typeform/Google Form mẫu

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Gửi CSAT qua Zendesk + tự động đẩy về Google Sheet
import requests, gspread
auth = ("agent@co.vn/token", "TOKEN")
# Lấy ticket đã đóng trong 1h qua
r = requests.get("https://co.zendesk.com/api/v2/search.json",
    params={"query": "status:solved updated>1hour"}, auth=auth)
for t in r.json()["results"]:
    survey_link = f"https://forms.gle/abc?ticket={t['id']}"
    # Trigger gửi mail qua trigger Zendesk hoặc SMTP
    send_email(t["requester_email"], survey_link)
```

## Bước 5: Output Format
- **HTML form** survey responsive (mobile-first)
- **Email template** subject + body, có placeholder
- **Excel dashboard** `CSAT_Dashboard.xlsx`: tab CSAT/CES/NPS, agent leaderboard, trend tuần
- **Action plan template** cho điểm thấp
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-csat-survey/output/`

## Checklist Trước Khi Giao
- [ ] Survey ≤ 3 câu, hoàn thành < 30 giây
- [ ] Mobile-friendly, tap 1 lần xong
- [ ] Tích hợp được với ticket system
- [ ] Có alert real-time cho Detractor
- [ ] Dashboard tự update, không phải làm tay
- [ ] Có quy trình follow-up khi điểm thấp
