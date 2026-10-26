---
name: cs-livechat-playbook
description: |
  Xây playbook livechat cho agent CSKH — chuẩn 5 giây response, đa cuộc song song, escalation, etiquette, KPI. Dùng skill này khi người dùng yêu cầu: "playbook livechat", "quy trình live chat", "SOP chat support", "training livechat agent", "kịch bản chat website", "chuẩn response time chat", "quản lý chat đồng thời", "chat etiquette CS". Output là Markdown SOP + Excel KPI + cheat sheet.
---

# CS Live Chat Playbook

## Mục Tiêu
Cung cấp playbook chuẩn để agent live chat phản hồi trong 5 giây, xử lý đồng thời 3-5 cuộc, giữ tone chuyên nghiệp, biết khi nào escalate — đảm bảo CSAT > 90%.

## Khi Nào Dùng
- Mới triển khai livechat Tawk/Crisp/Zendesk Chat/Intercom
- Agent chậm phản hồi, KH rời chat
- Agent xử lý 1 cuộc 1 lúc → bottleneck
- Tone chat không đồng nhất, có khi cộc lốc
- Cần KPI rõ ràng cho team chat

## Bước 1: Quy Tắc 5 Giây + Pre-typed Greeting
- **First Response Time (FRT) ≤ 5 giây**: dùng auto-greeting khi KH mở chat
  ```
  Xin chào! Em là {ten_agent} từ {ten_cty}. Em hỗ trợ gì cho anh/chị?
  ```
- Trong 30 giây phải có message từ người thật (không chỉ bot)
- Nếu busy: "Em đang hỗ trợ KH khác, anh/chị chờ em 1 phút nhé"

## Bước 2: Quản Lý Đa Cuộc (Multitasking)
- Mỗi agent max 3-5 cuộc cùng lúc tùy độ phức tạp
- Quy tắc: trả lời theo thứ tự cuộc nào gửi sớm nhất
- Dùng canned response 80% lần gõ
- Note nhanh trong CRM trước khi switch cuộc khác

**Status indicator:** Available (≤2 chat) → Busy (3-4) → Away (5+)

## Bước 3: Etiquette & Tone
- **Bắt đầu**: chào + tên + role
- **Giữa cuộc**:
  - Phản hồi ≤ 30 giây giữa message
  - Nếu cần check, báo: "Em check 1 phút, anh chị đợi nhé"
  - Không bao giờ để "..." quá 2 phút
- **Kết thúc**:
  - Tóm tắt: "Em đã hỗ trợ xong [X, Y]"
  - Hỏi thêm: "Anh chị còn cần gì nữa không?"
  - Cảm ơn + xin đánh giá: "Cảm ơn anh/chị, đánh giá em 1 sao nếu được!"

**Cấm:**
- Dùng emoji quá đà (max 1-2 mỗi message)
- Nói "không biết" → thay bằng "em check ngay"
- Để KH chờ quá 5 phút không update

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Slack MCP: alert TL khi agent overload (>5 chat) hoặc FRT > 30s
- Gmail MCP: gửi transcript chat cho KH sau khi đóng
- Google Sheets: log mọi chat + KPI agent theo ca
- WebSearch: best practice Intercom/Drift livechat
- WebFetch: tham khảo SOP livechat ngành

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Pull metrics chat hàng ngày từ Intercom + dashboard
import requests
H = {"Authorization": "Bearer INTERCOM_TOKEN", "Accept": "application/json"}
r = requests.get("https://api.intercom.io/conversations?per_page=50", headers=H)
for c in r.json()["conversations"]:
    frt = c.get("statistics", {}).get("first_admin_reply_time", 0)
    if frt > 60:
        slack_alert(f"FRT {frt}s on convo {c['id']}")
```

## Bước 5: Output Format
- **Markdown playbook `LiveChat_SOP.md`**: SOP đầy đủ + scenario
- **Excel `Chat_KPI.xlsx`**: FRT, AHT, CSAT, # chat/agent/ca
- **Cheat sheet A4**: in dán bàn agent (canned response + escalation flow)
- **Script kết thúc** xin CSAT
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-livechat-playbook/output/`

## Checklist Trước Khi Giao
- [ ] FRT target ≤ 5s, có auto-greeting
- [ ] Quy tắc multitasking rõ ràng
- [ ] Etiquette: opening + closing chuẩn
- [ ] Escalation flow gắn vào playbook
- [ ] KPI sheet có công thức tự tính
- [ ] Đã roleplay 3 scenario với agent
