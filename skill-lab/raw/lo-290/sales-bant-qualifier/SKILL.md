---
name: sales-bant-qualifier
description: |
  Qualifier lead theo BANT (Budget, Authority, Need, Timeline) chi tiết với câu hỏi đào sâu mỗi chiều. Trigger phrases: "qualify BANT", "BANT framework", "câu hỏi BANT", "qualify lead BANT", "kiểm tra budget authority need timeline", "discovery BANT", "BANT scorecard", "BANT script", "qualify khách hàng B2B", "BANT template". Output là Markdown question bank + Excel scorecard.
---

# BANT Lead Qualifier Deep-dive

## Mục Tiêu
Trang bị SDR/AE 40+ câu hỏi BANT phân lớp để qualify lead trong 15-20 phút, tránh "yes/no" surface — đảm bảo deal qualified mới đẩy lên pipeline.

## Khi Nào Dùng
- SDR qualify inbound lead
- AE discovery với prospect lạnh
- Re-qualify deal stuck
- Trước nâng stage Discovery → Demo
- Onboarding SDR mới

## Bước 1: B — Budget (Câu hỏi 3 lớp)

**Surface**: "Anh có budget cho dự án này không?"
**Deep**:
- "Anh đã allocate budget chính thức hay đang trong proposal?"
- "Bên anh thường budget category này bao nhiêu?"
- "Nếu chưa có budget, ai có thể approve mid-year?"
- "Compare với gì? (cost of doing nothing? đối thủ?)"

**Red flag**: KH không có khái niệm budget = sớm, hoặc đang fish giá.

## Bước 2: A — Authority (5 câu)
- "Anh là người ra quyết định cuối hay cần ai khác duyệt?"
- "Quy trình duyệt có bao nhiêu bước?"
- "Ai khác trong team sẽ tham gia đánh giá?"
- "Lần cuối bên anh mua tool tương tự, ai ký?"
- "CFO/CIO có review không?"

**Red flag**: chỉ 1 người, không nhắc đến CFO/Procurement trong deal >$50K.

## Bước 3: N — Need (Đào sâu 3 lớp WHY)

**Layer 1 — What**: "Pain hiện tại là gì?"
**Layer 2 — Why**: "Tại sao điều đó là vấn đề?" (×3 lần)
**Layer 3 — Cost of Inaction**: "Nếu không solve 6 tháng nữa hậu quả gì?"

Câu hỏi mở:
- "Trên thang 1-10, mức cấp bách của vấn đề?"
- "Đã thử cách nào? Tại sao chưa work?"
- "Tool nào đang dùng? Cụ thể yếu điểm gì?"

## Bước 4: T — Timeline (4 câu)
- "Khi nào anh muốn go-live?"
- "Lý do timing đó? (event nào driving?)"
- "Nếu không có timeline cụ thể, hậu quả gì?"
- "Procurement + Legal mất bao lâu?"

**Red flag**: "Chưa biết" → re-nurture, không push qua Demo.

## Bước 5: BANT Scorecard (0-3 mỗi chiều)
- Budget: 0 (không có) → 3 (confirmed allocated)
- Authority: 0 (IC) → 3 (EB tham gia call)
- Need: 0 (nice to have) → 3 (critical, CoI cao)
- Timeline: 0 (vô định) → 3 (<60 ngày)

Tổng /12:
- 9-12: Push Demo + Forecast
- 6-8: Discovery thêm
- <6: Nurture / Disqualify

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce/HubSpot MCP: log BANT field vào opportunity
- Gong MCP: phát hiện BANT signal từ call transcript
- Slack MCP: share BANT score với manager
- Calendar MCP: book demo nếu qualify

**Fallback API:**
```python
# Salesforce update BANT fields
sf.Opportunity.update(opp_id, {
    "BANT_Budget__c": budget_score,
    "BANT_Authority__c": authority_score,
    "BANT_Need__c": need_score,
    "BANT_Timeline__c": timeline_score,
    "BANT_Total__c": total,
    "StageName": "Demo Scheduled" if total >= 9 else "Discovery"
})
```

## Bước 7: Output Format
- **File 1**: `bant_question_bank.md` — 40 câu phân theo 4 chiều
- **File 2**: `bant_scorecard.xlsx` — auto-calculate + recommendation
- **File 3**: `bant_call_notes.docx` — form fill trong call
- **File 4**: `bant_disqualify_email.md` — template polite re-nurture
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ 4 chiều BANT, không skip
- [ ] Câu hỏi 3 lớp deep, không surface
- [ ] Scorecard 0-3 mỗi chiều
- [ ] Red flag được tag rõ
- [ ] Recommendation rõ ràng stage tiếp
- [ ] Update CRM trong 4h sau call
