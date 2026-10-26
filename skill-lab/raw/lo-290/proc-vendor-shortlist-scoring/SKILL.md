---
name: proc-vendor-shortlist-scoring
description: |
  Chấm điểm sàng lọc nhà cung cấp (Vendor Shortlist Scoring) sau khi nhận báo giá — đánh giá theo giá, chất lượng, năng lực, tài chính, kinh nghiệm để chọn 2-3 NCC vào vòng đàm phán. Kích hoạt khi người dùng nói: "chấm điểm NCC", "vendor scoring", "sàng lọc nhà cung cấp", "đánh giá báo giá NCC", "vendor evaluation matrix", "chọn nhà cung cấp", "supplier shortlist", "đánh giá năng lực NCC", "vendor rating", "supplier scorecard". Output là Excel scoring matrix + báo cáo PDF ranking NCC + đề xuất top 3.
---

# Chấm Điểm Sàng Lọc Nhà Cung Cấp (Vendor Scoring)

## Mục Tiêu
Giúp phòng Mua hàng so sánh 5-15 NCC theo cùng tiêu chí, ra quyết định khách quan thay vì "cảm giác". Áp dụng phương pháp Weighted Scoring + AHP đơn giản — phù hợp SME Việt Nam không cần dùng SAP Ariba.

## Khi Nào Dùng
- Sau khi nhận báo giá từ vòng RFQ
- Định kỳ rà soát NCC hiện tại (annual vendor review)
- Trước khi M&A một NCC chiến lược
- Khi tách đơn cho NCC dự phòng (backup vendor)
- Khi audit nội bộ phòng Mua hàng

## Bước 1: Định Nghĩa Tiêu Chí + Trọng Số
Tuỳ ngành mà điều chỉnh, gợi ý cho SME sản xuất / TMĐT:
| Tiêu chí | Trọng số | Cách đo |
|---|---|---|
| Giá tổng (TCO) | 25% | Lowest = 10đ, scale tuyến tính |
| Chất lượng / Chứng nhận | 20% | ISO 9001, sample test pass rate |
| Thời gian giao hàng | 15% | On-time delivery % lịch sử |
| Năng lực sản xuất | 10% | Production capacity vs demand |
| Tài chính (Credit rating) | 10% | D&B / VCBS rating |
| Kinh nghiệm + Reference | 10% | Số năm hoạt động + top 3 KH lớn |
| Vị trí địa lý + logistics | 5% | Khoảng cách + cảng |
| ESG / Compliance | 5% | Báo cáo CSR, audit lao động |

## Bước 2: Thu Thập Data Mỗi NCC
- Bảng báo giá đã chuẩn hoá (cùng Incoterm, cùng VAT)
- GPKD + BCTC 2-3 năm gần nhất (tra `gdt.gov.vn` hoặc xin trực tiếp)
- Chứng nhận ISO / sample test result
- Reference list (3-5 khách hàng tương đương quy mô)
- Audit on-site report (nếu giá trị đơn >500 triệu)
- ESG / Sedex / SMETA report (nếu xuất khẩu EU/Mỹ)

## Bước 3: Tính Điểm + Ranking
Phương pháp Weighted Sum:
- Score(NCC) = Σ (Trọng số × Điểm tiêu chí × 100)
- Cộng thêm điều kiện loại: nếu không có ISO 9001 → loại
- Cộng thêm "Knock-out criteria": NCC có nợ thuế > 30 ngày → loại
- Sensitivity Analysis: thay đổi trọng số ±10% xem ranking có đổi không

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: master scoring matrix sống, share team
- Google Drive MCP: lưu evidence (BCTC, ISO certificate, audit report) theo NCC
- Notion MCP: vendor database 360° + history rating
- Gmail MCP: gửi feedback cho NCC win/loss + thông báo vòng đàm phán tiếp
- WebFetch: tra `dangkykinhdoanh.gov.vn` để verify GPKD + đại diện
- WebFetch: tra `tracuunnt.gdt.gov.vn` để check nợ thuế
- WebSearch: tra review NCC trên Google + Alibaba + LinkedIn

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tính weighted score + sensitivity analysis
import pandas as pd
import numpy as np

def score_vendors(df_vendors, weights, knockouts):
    # df_vendors: rows = NCC, cols = tiêu chí
    # weights: dict {criterion: weight}
    # knockouts: list of (criterion, condition)

    # Loại vendor theo knock-out
    for crit, cond in knockouts:
        df_vendors = df_vendors[df_vendors[crit].apply(cond)]

    # Normalize 0-1 mỗi cột (higher is better, đảo chiều với cột giá)
    for col in weights:
        if col == "price":
            df_vendors[col + "_norm"] = df_vendors[col].min() / df_vendors[col]
        else:
            df_vendors[col + "_norm"] = df_vendors[col] / df_vendors[col].max()

    # Weighted sum
    df_vendors["score"] = sum(df_vendors[c + "_norm"] * w for c, w in weights.items()) * 100
    return df_vendors.sort_values("score", ascending=False)

# Sensitivity analysis: shuffle weights ±10%
def sensitivity(df, weights, n_iter=100):
    ranks = []
    for _ in range(n_iter):
        w_shuffled = {k: v * np.random.uniform(0.9, 1.1) for k, v in weights.items()}
        ranks.append(score_vendors(df.copy(), w_shuffled, []).index.tolist())
    return ranks
```

## Bước 5: Output Format
- File `vendor_scoring_matrix.xlsx`: bảng tính đầy đủ + công thức + sensitivity tab
- File `vendor_ranking_report.pdf`: 5-7 trang
  - Trang 1: Top 3 NCC + recommendation
  - Trang 2-3: Bảng so sánh tiêu chí
  - Trang 4: Heatmap strength/weakness
  - Trang 5: Risk warning từng NCC
  - Trang 6: Sensitivity analysis
  - Trang 7: Đề xuất chiến lược (single vs dual sourcing)
- File `email_feedback_winloss.txt`: template thông báo NCC win/loss
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/vendor-scoring/`

## Checklist Trước Khi Giao
- [ ] Có ≥5 tiêu chí + trọng số rõ ràng tổng = 100%
- [ ] Đã verify GPKD + nợ thuế từng NCC
- [ ] Có knock-out criteria (ISO, financial health, compliance)
- [ ] Đã chuẩn hoá báo giá về cùng Incoterm + VAT
- [ ] Có sensitivity analysis (ranking ổn định khi đổi trọng số ±10%)
- [ ] Đề xuất top 3 vào vòng đàm phán
- [ ] Có kế hoạch dual-sourcing (backup) để tránh phụ thuộc 1 NCC
- [ ] Lưu evidence + audit trail cho compliance
