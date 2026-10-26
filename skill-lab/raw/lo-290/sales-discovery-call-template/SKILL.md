---
name: sales-discovery-call-template
description: |
  Template discovery call 30-45 phút theo BANT/MEDDIC, có agenda, 25 câu hỏi phân lớp và scorecard qualify cuối call. Trigger phrases: "template discovery call", "discovery call B2B", "câu hỏi discovery sales", "BANT discovery", "MEDDIC qualify", "chuẩn bị discovery call", "kịch bản discovery", "qualify khách hàng", "discovery framework", "call khám phá nhu cầu". Output là Markdown agenda + Excel scorecard + PDF notes template.
---

# Discovery Call Template (BANT + MEDDIC)

## Mục Tiêu
Cung cấp template discovery call chuẩn giúp AE qualify deal trong 30-45 phút, thu thập đủ data BANT + MEDDIC để đưa ra forecast chính xác và phân bổ ưu tiên hợp lý.

## Khi Nào Dùng
- AE mới onboard cần training framework
- Deal phức tạp enterprise cần qualify sâu
- Sau SDR handover → AE chạy discovery
- Inbound demo request từ KH lạ
- Review deal stuck do qualify yếu

## Bước 1: Pre-call Research (15 phút)
- Đọc website + 3 post LinkedIn của KH
- Check tech stack qua BuiltWith
- Tin tức funding/news 6 tháng gần
- LinkedIn buying committee (3-5 người)
- Lưu pre-call brief 1 trang

## Bước 2: Agenda Discovery (35 phút)

**A. Mở (3 phút)**: chào, xác nhận thời gian, set expectation: "Em đề xuất 30 phút em hỏi để hiểu, 5 phút em chia sẻ nếu phù hợp."

**B. Current State (8 phút) — SPIN Situation**:
- "Quy trình <X> hiện tại chạy ra sao?"
- "Đang dùng tool gì? Tốt/dở điểm nào?"
- "Team bao nhiêu người chạy?"

**C. Pain & Cost (10 phút) — SPIN Problem + Implication**:
- "Pain lớn nhất là gì?" → đào sâu 3 lớp WHY
- "Nó tốn anh bao nhiêu thời gian/tiền/cơ hội mỗi tháng?"
- "Nếu không giải quyết, 6 tháng nữa sẽ ra sao?"

**D. Decision (8 phút) — MEDDIC**:
- Metric: "Anh đo thành công bằng gì?"
- Economic Buyer: "Ai ký?"
- Decision Criteria: "3 tiêu chí chọn?"
- Decision Process: "Quy trình duyệt mất bao lâu?"
- Identify Pain: confirm pain ranked
- Champion: "Ai trong nội bộ ủng hộ?"

**E. Close (6 phút)**: Recap + propose next step (demo / POC / proposal)

## Bước 3: Chấm Scorecard sau call (0-3 mỗi item)
- BANT: Budget, Authority, Need, Timeline
- MEDDIC: 6 dimension
- Tổng /30 → quyết định: Forecast / Pipeline / Disqualify

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Calendar MCP: gửi invite + agenda trước call
- Gong/Chorus MCP: ghi âm + transcript
- Salesforce/HubSpot MCP: log call note + update opportunity stage
- WebFetch: pull thông tin pre-call brief

**Fallback API:**
```python
# HubSpot log call + update deal
import requests
headers = {"Authorization": f"Bearer {token}"}
# Log call
requests.post("https://api.hubapi.com/crm/v3/objects/calls",
    headers=headers, json={"properties": {"hs_call_body": notes,
    "hs_call_duration": 2100}})
# Update deal stage
requests.patch(f"https://api.hubapi.com/crm/v3/objects/deals/{deal_id}",
    headers=headers, json={"properties": {"dealstage": "qualified"}})
```

## Bước 5: Output Format
- **File 1**: `discovery_agenda_<account>.md` — agenda 5 phần + 25 câu hỏi
- **File 2**: `discovery_scorecard.xlsx` — BANT+MEDDIC, tự tính tổng + recommendation
- **File 3**: `discovery_notes_template.docx` — form notes call để AE fill
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Pre-call brief 1 trang đã chuẩn bị
- [ ] Agenda gửi KH trước 24h
- [ ] 25 câu hỏi phân theo SPIN Situation→Need-payoff
- [ ] Scorecard chấm 0-3 mỗi dimension
- [ ] Sau call có next step rõ ràng + deadline
- [ ] Update CRM trong 4 giờ sau call
