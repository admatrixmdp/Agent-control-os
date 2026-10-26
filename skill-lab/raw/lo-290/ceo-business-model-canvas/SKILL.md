---
name: ceo-business-model-canvas
description: |
  Tạo Business Model Canvas (BMC) 9 ô động cho ý tưởng kinh doanh mới hoặc business unit hiện có — kèm Lean Canvas variant, hypothesis test, và unit economics.
  Kích hoạt khi người dùng nói: "business model canvas", "BMC", "lean canvas", "mô hình kinh doanh", "canvas Osterwalder", "phác thảo mô hình", "thiết kế business model", "9 ô canvas".
  Output là HTML canvas + Excel unit economics.
---

# CEO Business Model Canvas — BMC Động

## Mục Tiêu
Trước khi đầu tư hàng tỷ vào idea mới, dành 4h vẽ BMC để stress-test. Skill này tạo BMC 9 ô + hypothesis cần validate + unit economics — không chỉ là tài liệu trang trí.

## Khi Nào Dùng
- Idea sản phẩm mới
- Tách business unit mới
- Pivot mô hình kinh doanh
- Trước khi gọi vốn
- Khi dạy founder/intrapreneur

## Bước 1: Fill 9 Ô BMC Cốt Lõi
1. **Customer Segments**: ai trả tiền? phân khúc cụ thể (tránh "everyone")
2. **Value Proposition**: vấn đề gì được giải quyết, gain/pain
3. **Channels**: cách reach + bán + service
4. **Customer Relationships**: self-service / dedicated / community
5. **Revenue Streams**: 1 lần / recurring / freemium / transaction
6. **Key Resources**: gì cần (con người, tech, IP, vốn)
7. **Key Activities**: làm gì hằng ngày
8. **Key Partners**: ai supply, ai phân phối
9. **Cost Structure**: fixed vs variable, cost dominant

## Bước 2: Hypothesis Test
Mỗi ô có 2-3 hypothesis cần validate. VD:
- "Segment freelancer Việt Nam có 200k người sẵn trả 200k/tháng"
- "Kênh Facebook Group đủ để reach 30% segment với CAC < 50k"

Chia hypothesis: Validated / Testing / Risky.
Risky hypothesis ưu tiên test trước.

## Bước 3: Unit Economics
- ARPU (revenue per user / month)
- CAC
- CAC Payback
- Gross Margin %
- LTV (ARPU × tháng × margin)
- LTV/CAC ratio (cần ≥ 3)

Nếu LTV/CAC < 1.5 → mô hình rủi ro, cần redesign.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Canva MCP: dùng template BMC đẹp 9 ô
- Notion MCP: BMC sống có comment + version
- WebSearch: lấy benchmark unit economics ngành
- Google Sheets MCP: model financial 3 năm
- Slack MCP: collect feedback từ team

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Unit economics check
arpu = 200_000
cac = 600_000
margin = 0.65
churn_monthly = 0.05  # 5%
ltv = arpu * margin / churn_monthly
ratio = ltv / cac
print(f"LTV: {ltv:,.0f}, LTV/CAC: {ratio:.2f}")
# Nếu < 3 → cần action
```

## Bước 5: Output Format
- HTML 9-ô BMC interactive (click ô để expand hypothesis)
- Excel unit economics có scenario (base/up/down)
- 1-page PDF canvas in được khổ A3
- Hypothesis log với status validate
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/bmc-[idea]-vN.html`

## Checklist Trước Khi Giao
- [ ] Đủ 9 ô, không bỏ trống
- [ ] Mỗi ô có 2-3 hypothesis
- [ ] Risky hypothesis được flag
- [ ] LTV/CAC ratio tính rõ
- [ ] Có comparison với benchmark ngành
- [ ] Có roadmap validate 30/60/90 ngày
