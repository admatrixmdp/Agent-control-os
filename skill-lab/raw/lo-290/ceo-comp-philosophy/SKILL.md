---
name: ceo-comp-philosophy
description: |
  Triết lý lương thưởng (compensation philosophy) cho công ty — định nghĩa percentile thị trường, salary band, equity allocation, bonus structure, performance link.
  Kích hoạt khi người dùng nói: "comp philosophy", "triết lý lương", "salary band", "lương thưởng công ty", "equity allocation", "compensation framework", "policy lương", "bonus structure".
  Output là PDF policy document + Excel band.
---

# CEO Compensation Philosophy — Triết Lý Lương Thưởng

## Mục Tiêu
Không có comp philosophy thì mỗi hire negotiate riêng → bất công, lương leak gây drama. Skill này tạo framework rõ ràng + transparent + bảo vệ company khi raise round.

## Khi Nào Dùng
- Trước khi hire C-level đầu tiên
- Sau khi raise Series A (cần formalize)
- Annual comp review
- Khi attrition do lương
- Trước IPO

## Bước 1: Định Nghĩa 5 Nguyên Tắc Triết Lý
1. **Market positioning**: P50 / P75 / P90 percentile so với benchmark
2. **Pay for performance vs longevity**: trọng số bonus vs base
3. **Transparency level**: open band hay confidential
4. **Equity philosophy**: ai có equity, vesting cliff
5. **Equity vs cash mix**: tỉ lệ theo level

VD nguyên tắc: "Pay base P50, bonus P75 nếu top performer, equity broad-based vesting 4 năm 1 cliff."

## Bước 2: Salary Band Theo Level
Mỗi level có 3 range: Min - Mid (target) - Max
- L1 Junior: 8-12-18M
- L2 Mid: 15-22-32M
- L3 Senior: 25-35-50M
- L4 Lead: 40-55-75M
- L5 Director: 60-85-120M
- L6 VP: 100-140-200M
- L7 CXO: 150-220-350M

(Số ví dụ Việt Nam 2026, điều chỉnh theo ngành)

Band rộng giữa min-max ≈ 1.6-2x.

## Bước 3: Equity Allocation Standard
- Founder: 20-40% (split)
- Co-founder early: 5-15%
- VP/Director: 0.5-2%
- Senior IC: 0.1-0.5%
- Mid IC: 0.05-0.2%
- Junior: 0.01-0.05%
- Pool tổng: 10-20% của cap table

Vesting: 4 năm, cliff 1 năm. Accelerate khi M&A / fired without cause.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: benchmark Việt Nam (TopCV, ITviec, VietnamWorks salary survey)
- WebFetch: lấy report Mercer, Towers Watson
- Notion MCP: salary band document có version
- Google Sheets MCP: cap table tracking
- Gmail MCP: gửi offer letter chuẩn

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tính range với percentile market
import statistics
market_data = [20, 25, 23, 28, 30, 26, 22, 27]  # senior eng VN
p25 = statistics.quantiles(market_data, n=4)[0]
p50 = statistics.median(market_data)
p75 = statistics.quantiles(market_data, n=4)[2]
band = {'min': p25, 'mid': p50, 'max': p75}
```

## Bước 5: Output Format
- PDF policy 8-12 trang với:
  - 5 nguyên tắc triết lý
  - Salary band table
  - Equity allocation grid
  - Promotion criteria
  - Bonus calculation
- Excel cap table simulation
- Offer letter template
- FAQ document cho HR/recruiter
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/comp-philosophy-vN.pdf`

## Checklist Trước Khi Giao
- [ ] 5 nguyên tắc rõ ràng
- [ ] Salary band có benchmark source
- [ ] Equity vesting policy đầy đủ
- [ ] Có lawyer review trước public
- [ ] FAQ trả lời 10 câu hỏi thường gặp
- [ ] Quy ước review band hàng năm
