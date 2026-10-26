---
name: sales-negotiation-playbook
description: |
  Playbook đàm phán B2B với BATNA, anchor, trade-off, concession strategy chuẩn Harvard PON. Trigger phrases: "playbook đàm phán", "negotiation playbook", "BATNA sales", "đàm phán giá", "negotiation B2B", "concession strategy", "anchor đàm phán", "negotiate hợp đồng", "đàm phán enterprise deal", "Harvard negotiation framework". Output là Markdown playbook + Excel concession ladder + script roleplay.
---

# Sales Negotiation Playbook (BATNA + Anchor)

## Mục Tiêu
Trang bị AE framework đàm phán cấu trúc Harvard PON — BATNA, ZOPA, anchor, trade-off — để giữ giá (giảm <10% list), tăng deal size 15%, ký multi-year.

## Khi Nào Dùng
- Deal late-stage Negotiation
- KH yêu cầu chiết khấu lớn
- Đối thủ tung giá thấp counter
- Multi-year deal complex
- Procurement involved hard-negotiate

## Bước 1: Preparation (BATNA + ZOPA)

**BATNA mình**: option tốt nhất nếu deal không close
- Walk-away threshold
- Alternative customer thay thế
- Cost of losing deal

**BATNA KH**: option của họ
- Đối thủ mình biết
- Build in-house?
- Status quo (do nothing)

**ZOPA (Zone of Possible Agreement)**:
- Floor (mình): minimum acceptable
- Ceiling (mình): list price
- KH floor + ceiling
- Overlap = ZOPA

## Bước 2: Anchor Strategy
- Mở giá CAO (list + 10-20%)
- Justify bằng value: "Standard package $300K cho package này"
- Đợi KH counter
- Trade concession, không "vứt" giảm giá

## Bước 3: Trade-off Concession Ladder
Mỗi giảm giá PHẢI trade:
- Giảm 5% giá → KH ký 2 năm
- Giảm 10% → multi-year + case study + reference
- Giảm 15% → multi-year + upfront annual payment + co-marketing
- Giảm 20% → exec sponsorship + log Logo + 3 year + reference call

NEVER "free" concession.

## Bước 4: 6 Negotiation Tactic

**A. Silence after offer**: đặt số rồi im
**B. Higher authority**: "Em phải hỏi sếp"
**C. Flinch**: react sốc với demand KH
**D. Vise**: "Anh cần làm tốt hơn"
**E. Good guy/bad guy**: AE + Manager
**F. Deadline**: "Giá này valid hết tháng"

Học counter mỗi tactic KH dùng với mình.

## Bước 5: Concession Behavior

**Giảm sau mỗi vòng**: $20K → $10K → $5K → $2K (tín hiệu close)
**KHÔNG split-the-difference đầu tiên** (mà mình meeting KH ở $X, không phải mid)
**Bundle concession**: "Em sẽ giảm 5% + add training nếu anh ký Q2"

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce CPQ MCP: approval workflow theo discount
- Gong MCP: phân tích AE đàm phán win pattern
- Slack MCP: Manager standby support
- DocuSign MCP: contract execute nhanh

**Fallback API:**
```python
# Discount approval routing
def route_approval(discount_pct, deal_size):
    if discount_pct < 10: return "AE auto-approve"
    elif discount_pct < 20: return "Manager"
    elif discount_pct < 30: return "Director"
    else: return "VP/CRO"

# Trade-off validator
def validate_concession(concession):
    if concession["price_reduction"] > 0 and not concession["trade_received"]:
        raise Exception("Cannot give free concession - require trade")
```

## Bước 7: Output Format
- **File 1**: `negotiation_playbook.md` — full framework
- **File 2**: `BATNA_ZOPA_worksheet.xlsx` — fill per deal
- **File 3**: `concession_ladder.xlsx` — 4 level trade-off
- **File 4**: `negotiation_roleplay.md` — 5 scenario practice
- **File 5**: `objection_to_negotiation.md` — 10 KH objection + counter
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] BATNA + ZOPA xác định trước call
- [ ] Anchor high giá list+
- [ ] Concession có trade-off
- [ ] Approval routing rõ ràng
- [ ] Roleplay weekly với team
- [ ] Final discount log + RCA
