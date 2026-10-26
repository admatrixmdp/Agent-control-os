---
name: cs-chatbot-script-designer
description: |
  Thiết kế kịch bản chatbot CSKH (intent + entity + flow + fallback) cho Facebook Messenger / Zalo OA / website chat — tự động trả lời 60-80% câu hỏi thường gặp. Dùng skill này khi người dùng yêu cầu: "thiết kế chatbot", "viết script chatbot", "kịch bản Messenger bot", "Zalo OA chatbot", "intent flow chatbot", "AI chatbot CS", "tạo flow bot", "chatbot tự động trả lời". Output là JSON intent + flowchart + Markdown script chi tiết.
---

# CS Chatbot Script Designer

## Mục Tiêu
Thiết kế chatbot xử lý 60-80% câu hỏi thường gặp trên Messenger/Zalo/website — giảm tải agent, trả lời 24/7, handover thông minh khi cần người thật.

## Khi Nào Dùng
- Tỷ lệ inbox lặp lại (track đơn, hỏi giá, FAQ) > 50%
- Agent online giờ hành chính, ngoài giờ KH chờ → mất khách
- Đang dùng bot rule cứng, KH bực vì "không hiểu"
- Launch sản phẩm mới cần Q&A 24/7
- Muốn integrate bot với CRM/order system

## Bước 1: Liệt Kê Intent Cần Cover
Phân nhóm:
- **Greeting / Smalltalk** (5): chào, cảm ơn, tạm biệt
- **Pre-sales** (8): hỏi giá, hỏi tồn kho, so sánh SP, ưu đãi
- **Order tracking** (5): track đơn, sửa địa chỉ, hủy đơn
- **Post-sales** (8): hỏi hướng dẫn dùng, đổi trả, bảo hành
- **Khác** (4): liên hệ người thật, giờ làm việc, địa chỉ

Mỗi intent có 5-10 câu mẫu (training utterances).

## Bước 2: Thiết Kế Flow Cho Top 10 Intent
Cho mỗi intent vẽ flow:
```
User: "track đơn"
  → Bot: "Anh chị nhập mã đơn (VD: AB123)"
    → User nhập "AB123"
      → Bot gọi API order → trả status
        → Nếu "đang giao" → "Đơn đang ở {tinh}, dự kiến {ngay}"
        → Nếu "chưa thanh toán" → "Đơn chưa thanh toán, link: {url}"
        → Nếu lỗi → "Em không tìm thấy, kết nối agent"
```

Mỗi nhánh có button quick reply để KH không phải gõ nhiều.

## Bước 3: Xử Lý Fallback & Handover
- **Fallback Lv1** (bot không hiểu lần 1): "Em chưa rõ ý, anh chị có thể chọn mục dưới đây?" + 4 button gợi ý
- **Fallback Lv2** (không hiểu lần 2): "Em sẽ chuyển bạn cho agent, đợi 1 phút"
- **Handover trigger**:
  - User gõ "gặp người thật", "agent", "tổng đài"
  - 3 lần fallback liên tiếp
  - Detect cảm xúc tiêu cực (từ chửi, viết hoa)
  - Giá trị đơn > 5tr

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets: log conversation + intent miss để retrain
- Slack MCP: alert khi bot handover liên tục → quá tải
- WebSearch: tham khảo flow chatbot top brand
- WebFetch: kéo nội dung FAQ từ website làm training data
- Gmail MCP: gửi báo cáo weekly hiệu quả bot

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Webhook nhận message Messenger + trả lời theo intent
from flask import Flask, request
app = Flask(__name__)

INTENTS = {
    "track_order": ["track đơn", "đơn đến đâu", "mã đơn", "tracking"],
    "price": ["giá bao nhiêu", "bao nhiêu tiền"],
}
def classify(text):
    for intent, keywords in INTENTS.items():
        if any(k in text.lower() for k in keywords):
            return intent
    return "fallback"

@app.post("/webhook")
def webhook():
    msg = request.json["entry"][0]["messaging"][0]["message"]["text"]
    intent = classify(msg)
    reply = handle(intent, msg)
    send_message(reply)
    return "OK"
```

## Bước 5: Output Format
- **JSON `intents.json`**: list intent + utterances + responses, import được vào Dialogflow/Rasa/ManyChat
- **Flowchart** (Mermaid/PNG) cho top 10 intent
- **Markdown script** chi tiết từng intent + ví dụ hội thoại
- **Excel** training utterances để team mở rộng
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-chatbot-script-designer/output/`

## Checklist Trước Khi Giao
- [ ] Tối thiểu 20 intent + 5 utterances mỗi intent
- [ ] Top 10 intent có flowchart đầy đủ
- [ ] Quick reply button thay vì bắt gõ chữ
- [ ] Fallback 2 cấp + handover thông minh
- [ ] Có API hook cho order/CRM
- [ ] Đã test với 50 câu hỏi thật, đạt > 70% match đúng
