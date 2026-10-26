---
name: sales-win-loss-analyzer
description: |
  Phân tích win/loss deal qua data CRM + interview KH để tìm pattern thắng/thua actionable. Trigger phrases: "phân tích win loss", "win loss analysis", "tại sao thua deal", "win loss interview", "lý do mất khách", "review deal thua", "win loss report", "phân tích deal closed lost", "tại sao thắng deal", "loss reason analysis". Output là Markdown report + Excel pattern matrix + Slide exec summary.
---

# Win/Loss Analysis

## Mục Tiêu
Trích pattern thắng/thua từ 20-50 deal gần nhất qua CRM data + 10-15 interview KH (won + lost), tìm 3-5 insight actionable để leadership ra quyết định product/pricing/process.

## Khi Nào Dùng
- Win rate giảm 2 quý liên tiếp
- Đối thủ tung sản phẩm mới
- Trước annual planning
- Mid-year sản phẩm pivot
- Mỗi 6 tháng cycle định kỳ

## Bước 1: Phân Loại Data Win/Loss
Pull 12 tháng deal:
- Won: 20+ deal
- Lost (đến đối thủ): 20+ deal
- Lost (no decision): 15+ deal
- Disqualify: skip

Tag mỗi deal: industry, size, persona, deal size, sales cycle, AE, lead source.

## Bước 2: Pattern Analysis 6 Chiều
- **Reason coded**: lý do CRM (top 3 won/lost)
- **Stage stuck**: deal lost stuck stage nào nhiều nhất
- **Source quality**: source nào win rate cao
- **AE skill gap**: AE nào win/lost pattern khác
- **Industry**: vertical nào win cao
- **Competition**: thua ai nhiều nhất

## Bước 3: Interview KH (Bias-free)
Outsource bên 3 hoặc PM, không AE phỏng vấn:
- Won: 5-7 KH "Tại sao chọn mình?" + "Lý do gần như không chọn?"
- Lost: 5-7 KH "Tại sao chọn đối thủ?" + "Mình có thể làm gì khác?"
- No decision: 3-5 KH "Tại sao không quyết?"

Mỗi interview 30 phút, ghi âm có consent.

## Bước 4: Tổng hợp Insight
- Top 3 lý do win (theo data + interview)
- Top 3 lý do lost
- Pattern stage: 60% lost ở Negotiation → pricing issue
- Competition: đối thủ X win 40% deal vs mình
- Sản phẩm gap: feature Y bị hỏi 70% lost deal

## Bước 5: Recommendation
3-5 hành động cụ thể, có owner:
- Product: ưu tiên build feature Y
- Pricing: adjust SMB tier
- Process: deal stage gating
- Enablement: train AE Negotiation
- Marketing: counter messaging đối thủ X

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce/HubSpot MCP: pull won/lost data, loss reason
- Gong MCP: phân tích language late-stage call
- Survey MCP (Typeform/SurveyMonkey): interview KH
- Slack MCP: share insight với product team

**Fallback API:**
```python
# Aggregate loss reason
deals = sf.query("""SELECT LossReason__c, Competitor__c, Industry
    FROM Opportunity WHERE IsClosed=true AND IsWon=false
    AND CloseDate >= LAST_12_MONTHS""")
from collections import Counter
reasons = Counter([d["LossReason__c"] for d in deals["records"]])
top_3 = reasons.most_common(3)
```

## Bước 7: Output Format
- **File 1**: `winloss_report.md` — 10 trang full analysis
- **File 2**: `winloss_pattern_matrix.xlsx` — pattern cross-tab
- **File 3**: `winloss_interviews.md` — quotes + insight 15 interview
- **File 4**: `winloss_exec_summary.pptx` — 5 slide cho leadership
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] >40 deal data + 15 interview
- [ ] Interview bởi bên trung lập (không AE)
- [ ] Pattern dựa data + interview triangulate
- [ ] 3-5 recommendation có owner
- [ ] Action plan có deadline 90 ngày
- [ ] Re-analyze sau 6 tháng để measure impact
