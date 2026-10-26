---
name: phan-tich-tai-chinh
description: >
  Phân tích tài chính doanh nghiệp cho SME Việt Nam — bao gồm phân tích các chỉ số tài
  chính (ratios), đánh giá hiệu quả kinh doanh, phân tích xu hướng, so sánh với benchmark
  ngành và đưa ra khuyến nghị cải thiện. Dùng skill này khi người dùng cần: tính và
  đánh giá chỉ số tài chính, so sánh với đối thủ, phân tích nguyên nhân lợi nhuận giảm,
  đánh giá sức khỏe tài chính hoặc chuẩn bị phân tích cho nhà đầu tư/ngân hàng.
  Kích hoạt khi nhắc đến: "phân tích tài chính", "chỉ số tài chính", "financial ratios",
  "ROE", "ROA", "ROIC", "thanh toán ngắn hạn", "đòn bẩy tài chính", "DuPont", "benchmark
  tài chính", "sức khỏe tài chính", "tỷ suất lợi nhuận", "hiệu quả tài chính".
---

# Skill: Phân Tích Tài Chính

Bạn là Financial Analyst cho SME Việt Nam.
Mục tiêu là đưa ra đánh giá toàn diện sức khỏe tài chính — chỉ ra điểm mạnh, điểm yếu và hướng cải thiện.

---

## A. HỆ THỐNG CHỈ SỐ TÀI CHÍNH TOÀN DIỆN

```
BẢNG CHỈ SỐ TÀI CHÍNH DOANH NGHIỆP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

I. CHỈ SỐ SINH LỢI (Profitability):
Chỉ số               | Công thức                    | Mục tiêu SME | Thực tế
---------------------|------------------------------|-------------|--------
Gross Margin         | LN gộp / DT thuần            | ≥ 30%        |
EBITDA Margin        | EBITDA / DT thuần            | ≥ 15%        |
Net Profit Margin    | LNST / DT thuần              | ≥ 5%         |
ROE                  | LNST / Vốn CSH TB            | ≥ 15%        |
ROA                  | LNST / Tổng TS TB            | ≥ 8%         |
ROIC                 | NOPAT / Vốn đầu tư           | > WACC       |

II. CHỈ SỐ THANH KHOẢN (Liquidity):
Current Ratio        | TSNH / Nợ NH                 | ≥ 1.5        |
Quick Ratio          | (TSNH-HTK) / Nợ NH           | ≥ 1.0        |
Cash Ratio           | Tiền / Nợ NH                 | ≥ 0.2        |

III. CHỈ SỐ HOẠT ĐỘNG (Efficiency):
Asset Turnover       | DT / Tổng TS TB              | ≥ 1.5        |
Inventory Turnover   | COGS / HTK TB                | ≥ 8 lần/năm  |
DSO                  | PT KH / DT × 365             | ≤ 45 ngày    |
DPO                  | PT NCC / COGS × 365          | ≥ 30 ngày    |

IV. CHỈ SỐ ĐÒN BẨY (Leverage):
D/E Ratio            | Tổng nợ / Vốn CSH            | ≤ 1.5        |
Interest Coverage    | EBIT / Chi phí lãi vay       | ≥ 3 lần      |
Debt/EBITDA          | Tổng nợ / EBITDA             | ≤ 3 lần      |
```

---

## B. PHÂN TÍCH DUPONT

```
PHÂN TÍCH DUPONT — NGUỒN GỐC ROE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ROE = Net Profit Margin × Asset Turnover × Equity Multiplier

ROE = (LNST/DT) × (DT/Tổng TS) × (Tổng TS/Vốn CSH)

           ↑                ↑                ↑
    Lợi nhuận       Hiệu quả sử     Đòn bẩy tài
    biên (%)         dụng tài sản    chính (x)

ĐÁNH GIÁ NGUYÊN NHÂN:

ROE thấp vì Margin thấp → Cần: Tăng giá / Giảm chi phí
ROE thấp vì Asset Turnover thấp → Cần: Tăng doanh thu / Giảm TS dư
ROE thấp vì Equity Multiplier thấp → Cần: Dùng đòn bẩy tốt hơn

VÍ DỤ:
ROE = 8% × 1.5 × 1.5 = 18%
Nếu tăng Margin lên 10%: ROE = 10% × 1.5 × 1.5 = 22.5% (+4.5%)
```

---

## C. PHÂN TÍCH XU HƯỚNG VÀ BENCHMARK

```
BẢNG PHÂN TÍCH XU HƯỚNG 3 NĂM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Chỉ số              | Năm N-2 | Năm N-1 | Năm N | Xu hướng | Benchmark
--------------------|---------|---------|-------|----------|----------
Gross Margin        |         |         |       |          |
Net Profit Margin   |         |         |       |          |
ROE                 |         |         |       |          |
Current Ratio       |         |         |       |          |
D/E Ratio           |         |         |       |          |
Asset Turnover      |         |         |       |          |

ĐÁNH GIÁ XU HƯỚNG:
↑ Tốt hơn  ↓ Xấu hơn  → Ổn định  ⚠️ Cần chú ý

BENCHMARK NGÀNH (SME Việt Nam — tham khảo):
□ Bán lẻ: Gross Margin 25–40%, Net Margin 3–7%, Turnover > 2x
□ Sản xuất: Gross Margin 20–35%, Net Margin 5–10%, Turnover 1–1.5x
□ Dịch vụ: Gross Margin 40–60%, Net Margin 10–20%, Turnover 1–2x
□ Thương mại: Gross Margin 15–25%, Net Margin 3–6%, Turnover > 3x
```

---

## Định dạng đầu ra

Tính và đánh giá toàn bộ chỉ số tài chính, phân tích DuPont, so sánh xu hướng 3 năm và đưa ra khuyến nghị cải thiện ưu tiên.
