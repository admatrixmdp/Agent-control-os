---
name: cs-ticket-tagging-automation
description: |
  Thiết kế hệ thống auto-tag ticket CSKH theo intent (đổi trả, hỏi giá, complaint, kỹ thuật...) bằng rule + keyword + AI để phân tuyến đúng team, đo lường chính xác. Dùng skill này khi người dùng yêu cầu: "auto tag ticket", "phân loại ticket tự động", "intent classification CS", "tagging Zendesk", "rule routing ticket", "category ticket tự động", "phân tuyến ticket", "AI phân loại email khách". Output là bộ rule + Python script + Excel taxonomy.
---

# CS Ticket Tagging Automation

## Mục Tiêu
Tự động phân loại ticket khi vừa vào hệ thống — dựa trên keyword, sender, channel, content — để route đúng team, đo lường intent thật, và trigger workflow phù hợp. Mục tiêu: 80% ticket auto-tag đúng, giảm 70% thời gian phân loại thủ công.

## Khi Nào Dùng
- Volume ticket > 200/ngày, không thể tag tay
- Báo cáo intent không chính xác do tag thủ công sai/thiếu
- Cần SLA khác nhau theo intent (complaint < 2h, hỏi giá < 24h)
- Setup mới Zendesk/Freshdesk muốn auto-route
- Train chatbot/AI cần dataset có tag chuẩn

## Bước 1: Xây Taxonomy Tag
Phân 3 cấp:
- **Lv1 — Intent**: question / complaint / refund / technical / sales_lead / cancel
- **Lv2 — Topic**: shipping / payment / product / account / promo
- **Lv3 — Severity**: low / medium / high / critical

Ví dụ ticket: `intent:complaint` + `topic:shipping` + `severity:high` → route Team Logistics, SLA 2h.

Lưu taxonomy thành bảng để team thống nhất.

## Bước 2: Thiết Kế Rule Auto-Tag
**Rule kết hợp 4 nguồn:**
1. **Keyword body**: "hoàn tiền|refund|trả lại" → `refund`
2. **Subject email**: bắt đầu "[KHIẾU NẠI]" → `complaint:high`
3. **Channel**: từ Facebook Page → `social`; từ hotline → `phone`
4. **Sender domain**: @vip-partner.com → `vip:true`

Ưu tiên rule mạnh hơn (sender > subject > body).

## Bước 3: Tích Hợp AI Cho Trường Hợp Khó
Khi rule không match → gọi LLM phân loại:
- Prompt: "Phân loại ticket sau vào intent {list_intents}. Chỉ trả về 1 từ."
- Threshold confidence > 0.7 mới auto-tag, dưới ngưỡng để "Cần review"
- Log dataset để retrain mỗi tháng

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Gmail MCP: search/label email theo rule để test trước khi áp dụng
- Google Sheets: log ticket + tag để audit weekly
- Slack MCP: gửi alert khi ticket `severity:critical` tag được
- WebSearch: best practice taxonomy Zendesk/Intercom
- WebFetch: tham khảo intent list của help center mẫu

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Auto-tag ticket Zendesk khi mới tạo
import requests, re
auth = ("agent@co.vn/token", "TOKEN")
RULES = [
    (r"hoàn tiền|refund|trả lại", ["refund"]),
    (r"giao trễ|chưa nhận", ["shipping", "complaint"]),
    (r"không vào được|lỗi đăng nhập", ["technical", "account"]),
]
def tag_ticket(ticket_id, subject, body):
    text = (subject + " " + body).lower()
    tags = []
    for pattern, tg in RULES:
        if re.search(pattern, text):
            tags.extend(tg)
    if tags:
        r = requests.put(f"https://co.zendesk.com/api/v2/tickets/{ticket_id}.json",
                         json={"ticket": {"tags": tags}}, auth=auth)
        return r.json()
```

## Bước 5: Output Format
- **Excel `Taxonomy_v1.xlsx`**: sheet Tag tree, Rule mapping, Routing matrix
- **Python script `auto_tag.py`** chạy cron mỗi 5 phút
- **Markdown playbook** cho team CS hiểu hệ thống tag
- **Báo cáo weekly** % auto-tag đúng, intent top 10
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-ticket-tagging-automation/output/`

## Checklist Trước Khi Giao
- [ ] Taxonomy 3 cấp, không trùng lặp
- [ ] Rule cover 80%+ ticket sample
- [ ] AI fallback cho case không match rule
- [ ] Routing matrix gắn team owner + SLA
- [ ] Đã test với 100 ticket lịch sử
- [ ] Dashboard accuracy hàng tuần
