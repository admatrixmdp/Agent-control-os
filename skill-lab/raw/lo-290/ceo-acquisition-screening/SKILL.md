---
name: ceo-acquisition-screening
description: |
  Sàng lọc M&A target từ tiêu chí CEO đưa ra — dùng WebSearch để tìm công ty ứng viên, đánh giá fit strategic/financial/cultural, ra danh sách shortlist 5-10 target có scoring.
  Kích hoạt khi người dùng nói: "sàng lọc M&A", "tìm target M&A", "acquisition screening", "mua công ty", "thâu tóm", "M&A pipeline", "shortlist M&A target", "deal sourcing".
  Output là HTML/PDF target list + Excel scoring.
---

# CEO Acquisition Screening — Sàng Lọc M&A Target

## Mục Tiêu
M&A là cách tăng trưởng nhanh nhất nhưng 70-90% deal thất bại. Skill này giúp CEO sàng lọc target có kỷ luật thay vì "thấy ai bán thì mua".

## Khi Nào Dùng
- Có dư cash/vốn vừa raise
- Cần mở rộng nhanh (geo/segment/tech)
- Đối thủ đang củng cố qua M&A
- Có chiến lược "buy not build"
- Thị trường ngách cần consolidation

## Bước 1: Định Nghĩa Acquisition Criteria
- **Strategic fit**: ngành, segment, công nghệ, khách hàng
- **Size**: doanh thu mục tiêu (VD 10-50 tỷ)
- **Geography**: HCM/HN/SEA
- **Stage**: profitable hay still burning
- **Deal type**: full buyout / majority / minority
- **Valuation range**: bội số EBITDA/Revenue chấp nhận

## Bước 2: Source Target
- Dùng WebSearch: "[ngành] công ty Việt Nam doanh thu 10-50 tỷ"
- LinkedIn: tìm công ty có 20-100 nhân viên trong ngành
- Crunchbase: startup gọi vốn nhưng struggling
- Báo chí: tin tức ngành 12 tháng qua
- Internal: portfolio investor + advisor đề xuất

Mục tiêu: 30-50 long list ban đầu.

## Bước 3: Scoring 5 Tiêu Chí
Mỗi target chấm 1-5:
1. **Strategic fit**: cộng hưởng sản phẩm/khách hàng
2. **Financial**: revenue size, growth, margin
3. **Cultural**: founder fit, team retention rủi ro
4. **Valuation**: bội số có hợp lý không
5. **Feasibility**: founder có willing to sell?

Tổng điểm /25 → shortlist top 5-10.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: source target, news, founder background
- WebFetch: pull website target để hiểu sản phẩm
- LinkedIn (qua WebFetch): tìm founder, headcount
- Notion MCP: M&A pipeline database
- Gmail MCP: track outreach gửi founder

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Score matrix
import pandas as pd
targets = pd.DataFrame([
  {"name": "Co A", "strategic": 5, "financial": 3, "cultural": 4, "valuation": 4, "feasibility": 3},
  {"name": "Co B", "strategic": 4, "financial": 5, "cultural": 3, "valuation": 3, "feasibility": 4},
])
targets['total'] = targets[['strategic','financial','cultural','valuation','feasibility']].sum(axis=1)
shortlist = targets.sort_values('total', ascending=False).head(10)
```

## Bước 5: Output Format
- HTML/PDF target list:
  - Executive summary
  - Acquisition criteria
  - Long list 30-50 (bảng)
  - Shortlist 5-10 với scoring + 1-page profile mỗi target
- Excel scoring model tự động re-rank
- Outreach email template cho founder shortlist
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/ma-screening-YYYY-Q#.pdf`

## Checklist Trước Khi Giao
- [ ] Acquisition criteria viết rõ trước khi search
- [ ] Long list ≥ 30 target
- [ ] Shortlist 5-10 với scoring đầy đủ
- [ ] Mỗi shortlist target có 1-page profile
- [ ] Outreach email không "creepy"
- [ ] Có ước lượng valuation cho từng target
