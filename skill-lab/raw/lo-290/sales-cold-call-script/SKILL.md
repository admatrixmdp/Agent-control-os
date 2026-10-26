---
name: sales-cold-call-script
description: |
  Viết script cold call B2B 60 giây có opening hook, permission-based ask, value prop và CTA đặt meeting. Trigger phrases: "viết script cold call", "kịch bản gọi điện lạnh", "cold call script 60s", "soạn lời chào gọi điện sales", "script tele-sales", "opening cold call", "script gọi B2B", "kịch bản gọi khách lạnh", "viết lời thoại telesales", "tạo script điện thoại bán hàng". Output là Markdown script + Excel objection map.
---

# Cold Call Script Builder (60s Opening)

## Mục Tiêu
Tạo script cold call mở đầu 60s đạt connect→meeting rate >5%, giúp SDR vượt qua 15 giây quyết định của KH bằng pattern interrupt + value-first hook.

## Khi Nào Dùng
- Đào tạo SDR mới, cần template chuẩn
- Launch sản phẩm mới cần outbound calling
- Reactivate cold list >500 contacts
- Penetrate vertical mới chưa có script
- Nâng cấp script cũ connect rate thấp

## Bước 1: Hỏi context sản phẩm + persona
- Sản phẩm + 1 outcome cụ thể (số đo được)
- Persona (CEO/CFO/Head of Sales) + pain ưu tiên
- Industry + 2-3 đối thủ KH thường so sánh
- Mục tiêu call: đặt meeting / qualify / re-engage

## Bước 2: Viết 5 Phần Script

**A. Pattern Interrupt (5s)**: "Chào anh Minh, em là An từ Taki. Em biết em đang gọi lúc anh không hẹn — em xin 30 giây có được không?"

**B. Hook (15s)**: 1 câu nêu pain + 1 số chứng minh
"Em đang giúp các CFO bên FMCG cắt 15% chi phí closing tháng. Bên anh có đang xài Excel cho hợp nhất báo cáo không?"

**C. Permission-based Pivot (10s)**: Tuỳ trả lời, pivot sang qualify hoặc hẹn meeting

**D. CTA (15s)**: 2-option close
"Em đề xuất 20 phút thứ 3 10h hoặc thứ 5 3h — anh tiện cái nào?"

**E. Voicemail (15s)**: Ngắn, có hook + lý do call lại

## Bước 3: Xử lý 5 phản đối phổ biến trong cuộc gọi
- "Đang bận" → "Em hiểu, em xin 20s rồi quyết định gọi lại nhé?"
- "Gửi email đi" → "Dạ em sẽ gửi, nhưng em cần 1 câu hỏi để gửi cho đúng…"
- "Không quan tâm" → "Anh cho em 1 câu — anh chưa quan tâm vì <X> hay vì <Y>?"
- "Đang dùng đối thủ" → "Em không kéo anh chuyển, em chỉ muốn chia sẻ <điểm khác biệt>"
- "Bao nhiêu tiền" → "Phụ thuộc nhu cầu, em đề xuất 15 phút để báo số chuẩn"

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- LinkedIn/WebFetch: pull thông tin prospect 2 phút trước call (role, recent post)
- Calendar MCP: check slot trống ngay khi KH đồng ý, gửi invite trong cuộc gọi
- HubSpot/Salesforce MCP: log call disposition + next step ngay sau cuộc gọi

**Fallback API:**
```python
# HubSpot tạo call activity
import requests
headers = {"Authorization": f"Bearer {token}"}
data = {"properties": {"hs_call_status": "COMPLETED",
        "hs_call_disposition": "Connected",
        "hs_call_body": "Hẹn meeting Thứ 3 10h"}}
requests.post("https://api.hubapi.com/crm/v3/objects/calls",
              headers=headers, json=data)
```

## Bước 5: Output Format
- **File 1**: `coldcall_script_<persona>.md` — script full 5 phần + voicemail
- **File 2**: `objection_map_<persona>.xlsx` — cột: Objection / Reframe / Pivot question
- **File 3**: `call_tracker.xlsx` — log call/connect/meeting để tính conversion
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Opening dưới 5s, có pattern interrupt
- [ ] Có permission-based ask (không bắt KH nghe)
- [ ] Hook chứa 1 con số chứng minh
- [ ] CTA là 2-option, không yes/no
- [ ] Voicemail dưới 15s
- [ ] Bao gồm ít nhất 5 objection script
