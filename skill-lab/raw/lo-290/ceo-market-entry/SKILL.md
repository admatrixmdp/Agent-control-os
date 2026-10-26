---
name: ceo-market-entry
description: |
  Đánh giá thị trường mới (tỉnh/quốc gia/segment) — phân tích TAM/SAM/SOM, lựa chọn entry mode (organic/JV/M&A), dự báo P&L 3 năm và lập go/no-go decision.
  Kích hoạt khi người dùng nói: "vào thị trường mới", "market entry", "TAM SAM SOM", "thâm nhập thị trường", "đánh giá thị trường", "go-to-market strategy", "expand thị trường", "entry strategy".
  Output là PDF report 10-15 trang + Excel financial model.
---

# CEO Market Entry — Đánh Giá Vào Thị Trường Mới

## Mục Tiêu
Quyết định vào thị trường mới (Hà Nội, Đà Nẵng, Campuchia, segment B2B Enterprise) là quyết định bet hàng chục tỉ. Skill này giúp CEO có khung phân tích tránh quyết định cảm tính.

## Khi Nào Dùng
- Cân nhắc mở chi nhánh tỉnh khác
- Expand sang nước Đông Nam Á
- Thêm segment mới (SMB → Enterprise)
- Ra mắt sản phẩm mới
- Trước khi raise vốn vùng địa lý

## Bước 1: Khung Phân Tích 4P + 5C
- **TAM**: tổng thị trường có thể bán (top-down từ báo cáo + bottom-up từ # KH × ARPU)
- **SAM**: thị trường mình có thể serve (cùng segment, cùng giá)
- **SOM**: thực tế đạt được 3 năm (3-15% SAM)
- 5 Cs: Company, Customer, Competitor, Collaborator, Context

## Bước 2: Đánh Giá 4 Entry Mode
1. **Organic**: tự build, chậm, vốn vừa, control cao
2. **Joint Venture**: nhanh local knowledge, chia margin
3. **M&A**: nhanh nhất, đắt, rủi ro integration
4. **Franchise/Licensing**: nhẹ vốn, mất control quality

Bảng so sánh: thời gian, vốn, control, rủi ro, upside.

## Bước 3: Tài Chính 3 Năm
- Doanh thu năm 1/2/3 theo S-curve
- CAC + payback theo segment
- Headcount + cost mở văn phòng
- CapEx (kho, cửa hàng nếu có)
- Break-even tháng
- IRR / payback ROI

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: TAM theo Statista/Euromonitor/GSO, competitor landscape
- WebFetch: báo cáo PDF công khai về thị trường
- Notion MCP: lưu market entry playbook re-use
- Google Drive MCP: pull số tài chính làm baseline
- Slack MCP: collect intel từ #market-intel

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Bottom-up TAM
import pandas as pd
districts = pd.read_csv('gso_population.csv')
target = districts[districts['province'] == 'Hà Nội']
TAM = target['households'].sum() * arpu_year * penetration_realistic
SAM = TAM * 0.4  # serviceable
SOM_3y = SAM * 0.05  # realistic share
```

## Bước 5: Output Format
- PDF report 10-15 trang:
  - Executive summary 1 trang
  - TAM/SAM/SOM
  - 5C analysis
  - 4 entry modes so sánh
  - Financial 3 năm
  - Risks + mitigation
  - Go/No-Go recommendation
- Excel financial model với scenario (base/upside/downside)
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/market-entry-[place].pdf`

## Checklist Trước Khi Giao
- [ ] TAM/SAM/SOM có nguồn rõ ràng
- [ ] So sánh 4 entry modes đầy đủ
- [ ] Financial 3 năm có 3 scenarios
- [ ] Risks ≥ 5 cái có mitigation
- [ ] Recommendation rõ Go/No-Go + lý do
- [ ] Break-even ≤ 24 tháng (nếu không phải giải thích)
