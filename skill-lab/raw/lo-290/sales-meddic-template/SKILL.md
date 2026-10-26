---
name: sales-meddic-template
description: |
  Template MEDDIC fill cho enterprise deal — Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion. Trigger phrases: "MEDDIC template", "MEDDIC framework", "qualify MEDDIC", "enterprise deal qualification", "MEDDPICC", "MEDDIC checklist", "fill MEDDIC", "MEDDIC scorecard", "MEDDIC question", "MEDDIC sales". Output là Markdown template + Excel deal grid.
---

# MEDDIC/MEDDPICC Template Fill

## Mục Tiêu
Trang bị AE enterprise framework MEDDIC chi tiết để qualify deal lớn (>$100K), tăng win rate >35% bằng thông tin sâu mỗi dimension thay vì BANT surface.

## Khi Nào Dùng
- Deal enterprise >$100K
- Sales cycle >3 tháng
- Buying committee >5 người
- Deal stuck cần re-qualify
- Pipeline review forecast commit

## Bước 1: M — Metrics (Outcome KH muốn đo)
Câu hỏi:
- "Anh đo thành công bằng metric gì cụ thể?"
- "Baseline hiện tại là bao nhiêu?"
- "Target trong 6/12 tháng?"
- "Ai chịu trách nhiệm metric đó (board, CEO, CFO)?"

Output: 3-5 metric có số baseline + target + owner.

## Bước 2: E — Economic Buyer (Người ký)
- Tên + title + email + LinkedIn
- Đã gặp chưa? Lần cuối?
- EB hiểu pain ở mức nào (high/medium/low)?
- EB ưu tiên gì (cost / risk / growth)?
- Champion access đến EB qua kênh nào?

**Red flag**: chưa gặp EB sau stage Demo.

## Bước 3: D — Decision Criteria
- Tiêu chí KH dùng chọn vendor (technical + business + commercial)
- Trọng số tiêu chí (KH cho biết)
- Vendor nào đang competing
- "Must have" vs "nice to have"
- Mình match tiêu chí nào, miss cái nào

## Bước 4: D — Decision Process
- Bao nhiêu bước, ai duyệt mỗi bước
- Timeline mỗi bước (security review, legal, finance)
- Procurement involvement?
- Past purchase tương tự mất bao lâu?
- Có RFP/RFI không?

## Bước 5: I — Identify Pain
- Pain ranked top 3
- Cost of Inaction (số đo được)
- Pain ai cảm nhận nhất (EB hay user)
- Vì sao chưa solve (chính trị, ngân sách, không biết)

## Bước 6: C — Champion
Champion thật = Power + Pain + Plan:
- Power: ảnh hưởng nội bộ (vouch được khi crisis)
- Pain: cá nhân bị tổn thương nếu không có solution
- Plan: sẵn sàng map nội bộ giúp mình close

Có Champion thật → +20% win rate. Chỉ Coach → rủi ro.

## Bước 7: P + P + C (MEDDPICC mở rộng)
- **Paper Process**: legal/contract steps
- **Competition**: vendor competing + strength/weakness
- **Coach**: ai feed info nội bộ (khác Champion)

## Bước 8: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce/HubSpot MCP: custom fields MEDDIC trên Opportunity
- LinkedIn MCP: verify EB role + tenure
- Gong MCP: tìm EB mention trong call
- Slack MCP: ping team khi miss dimension

**Fallback API:**
```python
# Validate MEDDIC complete trước stage advance
def meddic_complete(opp):
    fields = ["Metrics__c","EconomicBuyer__c","DecisionCriteria__c",
              "DecisionProcess__c","IdentifiedPain__c","Champion__c"]
    return all(opp[f] for f in fields)

opp = sf.Opportunity.get(opp_id)
if opp["StageName"] == "Negotiation" and not meddic_complete(opp):
    raise Exception("MEDDIC incomplete - cannot advance to Negotiation")
```

## Bước 9: Output Format
- **File 1**: `meddic_template_<deal>.md` — fill đầy đủ 6+ dimension
- **File 2**: `meddic_grid.xlsx` — Deal × Dimension matrix, color-coded
- **File 3**: `meddic_scorecard.xlsx` — chấm 0-3 mỗi dimension
- **File 4**: `meddic_question_bank.md` — 50 câu hỏi đào sâu
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] EB đã gặp ít nhất 1 lần
- [ ] Champion verify Power + Pain + Plan
- [ ] Metrics có số baseline + target
- [ ] Decision process có timeline rõ
- [ ] Competition mapped với strength/weakness
- [ ] Block stage advance nếu MEDDIC incomplete
