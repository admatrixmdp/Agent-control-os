---
name: ceo-risk-register
description: |
  Sổ đăng ký rủi ro doanh nghiệp theo chuẩn ISO 31000 — gồm phân loại risk, likelihood × impact matrix, owner mitigation, residual risk, review định kỳ.
  Kích hoạt khi người dùng nói: "risk register", "sổ đăng ký rủi ro", "rủi ro doanh nghiệp", "phân tích rủi ro", "risk matrix", "quản trị rủi ro", "risk management", "rủi ro công ty".
  Output là Excel risk register + HTML dashboard.
---

# CEO Risk Register — Sổ Đăng Ký Rủi Ro DN

## Mục Tiêu
Đa số CEO biết rủi ro trong đầu nhưng không document. Khi xảy ra mới gọi crisis. Risk register là tài sản phòng thủ giúp board + leadership thấy 30 rủi ro lớn nhất, ai phụ trách, làm gì.

## Khi Nào Dùng
- Quarterly risk review
- Trước round funding (LP yêu cầu)
- Sau crisis (post-mortem)
- Khi mở thị trường mới
- Annual board meeting

## Bước 1: Phân Loại 7 Nhóm Rủi Ro
1. **Strategic** (chiến lược sai, pivot trễ)
2. **Financial** (cash, FX, lãi suất)
3. **Operational** (supply chain, downtime, lỗi sản phẩm)
4. **People** (key man, attrition, văn hoá)
5. **Compliance & Legal** (luật, hợp đồng, IP)
6. **Cyber & Data** (breach, ransomware, GDPR)
7. **Reputational** (scandal, PR, social media)

Mỗi nhóm 3-7 risk cụ thể → tổng 25-50 risk.

## Bước 2: Score Likelihood × Impact (5×5)
- **Likelihood**: 1 (rare) → 5 (almost certain) trong 12 tháng
- **Impact**: 1 (negligible) → 5 (catastrophic, ảnh hưởng tồn tại)
- **Score = L × I** (1-25)
- Heat map: Xanh (1-5), Vàng (6-12), Cam (13-19), Đỏ (20-25)

## Bước 3: Mitigation + Residual Risk
Mỗi risk có:
- **Inherent risk** (chưa làm gì): L × I
- **Mitigation actions** (đang/sẽ làm): danh sách + owner + deadline + cost
- **Residual risk** (sau khi mitigate): L × I mới
- **Acceptance**: chấp nhận hay tiếp tục giảm

Risk top 10 phải có CEO/board approval level.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Notion MCP: database "Risk Register" với property L, I, owner, status
- Google Sheets MCP: backup file Excel
- Calendar MCP: tạo recurring review hàng quý
- Slack MCP: alert khi risk score thay đổi tăng
- Linear MCP: tạo issue cho mỗi mitigation action

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Heat map matrix
import pandas as pd, numpy as np
import seaborn as sns
matrix = np.zeros((5, 5))
for r in risks:
    matrix[r['impact']-1, r['likelihood']-1] += 1
sns.heatmap(matrix, annot=True, cmap='RdYlGn_r')
```

## Bước 5: Output Format
- Excel risk register `risk-register-Q#-YYYY.xlsx`:
  - Sheet 1: Master list (ID, Risk, Category, L, I, Score, Owner, Status)
  - Sheet 2: Mitigations
  - Sheet 3: Top 10 dashboard
- HTML 5×5 heat map cho board
- PDF top 10 risk briefing
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ 7 nhóm, 25-50 risk
- [ ] Mỗi risk có L × I + lý do
- [ ] Top 10 risk có owner cấp CXO
- [ ] Mitigation có ngân sách + deadline
- [ ] So sánh quý trước (risk nào tăng/giảm)
- [ ] Review quarterly đã đặt calendar
