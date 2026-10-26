---
name: sales-rfp-scoring
description: |
  Chấm điểm RFP/tender quyết định Go/No-go bid trước khi đầu tư resource viết response. Trigger phrases: "chấm điểm RFP", "Go No-go bid", "RFP qualification", "đánh giá RFP có bid", "bid decision RFP", "RFP scoring criteria", "có nên trả lời RFP", "bid quali", "tender scoring", "RFP qualification matrix". Output là Excel scoring + Markdown decision memo.
---

# RFP Go/No-go Scoring

## Mục Tiêu
Đảm bảo team chỉ bid những RFP có win probability >30%, tránh "RFP wallpaper" tốn 5-10 ngày-người mỗi response cho deal sẽ thua.

## Khi Nào Dùng
- RFP/RFI nhận về
- Government tender mới
- Re-bid renewal competitive
- Partnership tender
- Khi sales pipeline bị quá tải RFP

## Bước 1: 10 Tiêu chí Scoring (0-3 mỗi cái)

**Fit (40 điểm)**:
1. ICP match (industry, size, geo)
2. Use case match sản phẩm
3. Budget rõ trong RFP
4. Technical requirements khả thi
5. Decision timeline reasonable

**Win Probability (60 điểm)**:
6. Có champion / contact nội bộ KH
7. Đã pre-engage trước RFP (vs cold)
8. Đối thủ chính - we beat them historically?
9. Pricing competitive
10. Discriminator rõ (chỉ mình có)

Tổng /30 → ×3.33 → /100.

## Bước 2: Decision Threshold
- >70: GO — full team commit
- 50-70: GO with conditions (cần Champion access)
- 30-50: GO partial (light response, skip optional sections)
- <30: NO-GO

## Bước 3: Decision Memo (1 trang)
Document:
- Score breakdown
- Champion status
- Top 3 risk
- Resource needed (people × days)
- Expected ROI nếu win
- Decision + sign-off (Sales Director)

## Bước 4: No-bid Communication
Polite no-bid response (giữ relationship):
- "Cảm ơn opportunity"
- "Sau cân nhắc, RFP này không match focus hiện tại"
- "Mong làm việc với anh chị future"
- Đề xuất referral nếu phù hợp

KHÔNG ghost. Reputational risk.

## Bước 5: Win Rate Tracking
Aggregate:
- RFP received per quarter
- Bid vs no-bid ratio
- Bid win rate
- No-bid follow-up rate (KH quay lại sau no-bid)
→ Tune threshold quarterly.

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce MCP: pull historical win/lost RFP
- Slack MCP: bid committee approval workflow
- Email MCP: send no-bid letter
- Drive MCP: archive RFP + decision

**Fallback API:**
```python
# Auto-score RFP from intake form
def score_rfp(rfp):
    score = 0
    score += 3 if rfp["industry"] in ICP_INDUSTRIES else 0
    score += 3 if rfp["budget_disclosed"] else 0
    score += 3 if rfp["champion_id"] else 0
    score += 3 if rfp["pre_engaged"] else 0
    # ...
    pct = score / 30 * 100
    return {"score": pct, "decision": "GO" if pct > 70 else "REVIEW" if pct > 50 else "NO-GO"}
```

## Bước 7: Output Format
- **File 1**: `rfp_scoring_<rfp-id>.xlsx` — 10 tiêu chí scored
- **File 2**: `rfp_decision_memo.md` — 1 trang sign-off
- **File 3**: `nobid_letter_template.md` — polite refuse
- **File 4**: `rfp_pipeline_tracker.xlsx` — all RFP + decision + outcome
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 10 tiêu chí scored 0-3
- [ ] Decision memo có sign-off
- [ ] No-bid có polite response (không ghost)
- [ ] Resource budget cho GO
- [ ] Quarterly review win rate
- [ ] Update threshold theo data
