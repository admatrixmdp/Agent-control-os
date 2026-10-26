---
name: ceo-1on1-template
description: |
  Template 1-1 meeting giữa CEO và cấp dưới trực tiếp (CXO, GĐ phòng) — agenda chuẩn, 15 câu hỏi mạnh, ghi chú action, follow-up tự động. Giúp CEO 1-1 đều đặn không bỏ sót.
  Kích hoạt khi người dùng nói: "1-1 template", "one-on-one CEO", "agenda 1-1", "câu hỏi 1-1", "template gặp cấp dưới", "1on1 meeting", "biểu mẫu 1-1", "check-in meeting".
  Output là Markdown notes + Notion page.
---

# CEO 1-on-1 Template — Mẫu Họp 1-1 Cho CEO

## Mục Tiêu
1-1 là công cụ leverage cao nhất của CEO nhưng đa số làm qua loa thành "status update". Template này biến 1-1 thành kênh phát hiện sớm vấn đề, coach cấp dưới, build trust.

## Khi Nào Dùng
- Hằng tuần với từng CXO/GĐ trực tiếp (5-7 người)
- Trước khi promote/giáng cấp
- Khi cấp dưới sắp burn-out
- Sau cuộc khủng hoảng
- Khi engagement thấp

## Bước 1: Hỏi Bối Cảnh
- Ai? Vị trí gì? Báo cáo trực tiếp CEO bao lâu?
- Tần suất 1-1 hiện tại?
- Mục tiêu cuộc này: routine/coach/feedback/khó khăn?
- Bao lâu: 30 hay 60 phút?

## Bước 2: Agenda 5 Khối
**Khối 1 (5 phút) — Cá nhân**: "Tuần này thế nào? Có gì đáng kể ngoài công việc?"
**Khối 2 (10-15 phút) — Họ dẫn**: "Cái gì quan trọng nhất với bạn tuần này?" (để họ chọn topic)
**Khối 3 (10-15 phút) — Sếp dẫn**: 1-2 chủ đề CEO muốn raise (priority/risk/feedback)
**Khối 4 (5-10 phút) — Career/growth**: skill đang phát triển, support cần
**Khối 5 (5 phút) — Action**: 3 action items + owner + deadline + next 1-1

## Bước 3: 15 Câu Hỏi Mạnh Để Có Sẵn
1. "Năng lượng tuần này 1-10 là mấy?"
2. "Việc gì khiến bạn không ngủ được?"
3. "Bạn cần gì tôi giúp mà ngại hỏi?"
4. "Team của bạn ai đang gặp vấn đề?"
5. "Nếu là tôi, bạn sẽ đổi gì ở công ty?"
6. "3 ưu tiên của bạn 30 ngày tới là gì?"
7. "Bạn muốn role gì sau 12 tháng?"
8. "Đối thủ làm gì khiến bạn lo?"
9. "Feedback mới nhất khách hàng cho?"
10. "Skill nào bạn muốn phát triển?"
11. "Quyết định nào bạn đang chờ tôi?"
12. "Ai trong team xứng đáng được recognize?"
13. "Cái gì lãng phí thời gian của bạn nhất?"
14. "Bạn có nghĩ chiến lược công ty đúng không?"
15. "Tôi đang làm gì khiến công việc của bạn khó hơn?"

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Notion MCP: tạo template page "1-1 [Name] [Date]" với 5 khối + lịch sử
- Calendar MCP: tạo recurring event 1-1 weekly
- Slack MCP: gửi reminder agenda 1h trước
- Gmail MCP: gửi follow-up email với action items sau cuộc
- Linear MCP: convert action items thành issues

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tạo Notion page cho mỗi 1-1
import requests
data = {
  "parent": {"database_id": db_id},
  "properties": {
    "Name": {"title": [{"text": {"content": f"1-1 with {name} - {date}"}}]},
    "Status": {"select": {"name": "Scheduled"}}
  },
  "children": template_blocks
}
requests.post("https://api.notion.com/v1/pages", json=data, headers=headers)
```

## Bước 5: Output Format
- Markdown notes 1-1 với 5 khối + action checklist
- Notion page lưu trữ kèm history
- Email follow-up sau cuộc (action + ETA)
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/1on1-[name]-YYYY-MM-DD.md`

## Checklist Trước Khi Giao
- [ ] Có đủ 5 khối agenda
- [ ] 3 action items max (không quá tham)
- [ ] Mỗi action có owner + deadline
- [ ] Lịch 1-1 tiếp theo đã đặt
- [ ] Câu hỏi tránh "có/không" — toàn open-ended
- [ ] Note ngắn gọn không leak confidential
