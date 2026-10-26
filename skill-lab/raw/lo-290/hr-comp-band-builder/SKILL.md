---
name: hr-comp-band-builder
description: |
  Xây khung lương theo band/level cho doanh nghiệp Việt Nam, gắn với market data (Mercer, Talentnet, Robert Walters), benchmark theo ngành, vùng, đảm bảo internal equity.
  Kích hoạt khi người dùng nói: "khung lương", "comp band", "salary band", "lương theo cấp bậc", "thang bảng lương", "benchmark lương", "compensation framework", "khung lương 2026", "xây bậc lương", "salary structure".
  Output là file .xlsx khung lương + chính sách .docx + tool tính tăng lương individual.
---

# HR - Khung Lương Theo Band & Level

## Mục Tiêu
Chấm dứt thương lượng lương cảm tính. Khung lương giúp HR + manager trả lời 3 câu hỏi: (1) Đề xuất lương ứng viên mới ở đâu? (2) Tăng lương bao nhiêu là phù hợp? (3) Có công bằng giữa NV cũ - mới không?

## Khi Nào Dùng
- Công ty scale 50-200 NV, hết thời "ad-hoc"
- Trước cycle tăng lương hằng năm
- Sau khảo sát Total Reward thấy lệch market
- M&A cần hợp nhất khung lương 2 công ty

## Bước 1: Phân Cấp Level + Band
Cấu trúc phổ biến:
| Band | Level | Mô tả |
|---|---|---|
| Entry | L1, L2 | Intern, Junior 0-2 năm KN |
| Individual Contributor | L3, L4, L5 | Mid, Senior, Lead |
| People Manager | M1, M2, M3 | Team Lead, Manager, Senior Manager |
| Director | D1, D2 | Director, Senior Director |
| Executive | E1, E2 | VP, C-level |

Mỗi level có Job Family (Engineering, Sales, Product, Ops...). Tổng matrix = Level × Family.

## Bước 2: Thu Thập Market Data
Nguồn cho VN:
- **Mercer TRS** (chuẩn quốc tế, đắt nhưng đầy đủ)
- **Talentnet Salary Survey** (uy tín VN)
- **First Alliances** + **Navigos** (ngành cụ thể)
- **TopCV Salary Report** (miễn phí, mass market)
- **ITviec Report** (tech)

Lấy P25, P50 (median), P75, P90 cho mỗi level - family - vùng (HN/HCM/Khác).

## Bước 3: Vẽ Salary Band
Mỗi level có khung Min - Mid - Max (thường spread 30-50%):
- **Min** = 85% × P50 market
- **Mid** = 100% × P50
- **Max** = 120% × P50

Ví dụ Senior Engineer L5 HCM 2026:
- Min: 35tr - Mid: 41tr - Max: 50tr

Quy tắc Compa-ratio = lương cá nhân / Mid band:
- 0.85-0.95: Developing (mới lên level)
- 0.95-1.05: Solid
- 1.05-1.15: Strong
- > 1.15: Top, cân nhắc promote

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tra Talentnet Salary Survey 2026, Mercer TRS, ITviec Report
- WebFetch: tải PDF salary report các hãng cung cấp
- Sheets MCP: master Comp Band + per-employee Compa-ratio
- Drive MCP: lưu market data nguồn (confidential)
- Gmail MCP: gửi proposal khung lương cho CFO + CEO

**Fallback bằng API (HRIS sync):**
```python
# Tính tự động compa-ratio cho toàn công ty
import pandas as pd
df = pd.read_excel("payroll.xlsx")
band = pd.read_excel("salary_band.xlsx")
df = df.merge(band, on=["level", "family", "city"])
df["compa_ratio"] = df["salary"] / df["mid_band"]
df["status"] = pd.cut(df["compa_ratio"],
    bins=[0,0.85,0.95,1.05,1.15,2],
    labels=["Below","Developing","Solid","Strong","Above Max"])
df.to_excel("comp_analysis_2026.xlsx")
```

## Bước 5: Output Format
- File `.xlsx` Comp Band Matrix (Level × Family × City × Min/Mid/Max)
- File `.docx` Compensation Policy (philosophy, cycle, đặc cách)
- File `.xlsx` Individual Compa-ratio Analysis
- File `.pptx` proposal trình BOD
- Lưu tại: `/outputs/CompBand_<congty>_<YYYY>.xlsx`

## Checklist Trước Khi Giao
- [ ] Có ≥ 2 nguồn market data đối chiếu
- [ ] Mỗi level có Min/Mid/Max
- [ ] Spread 30-50%
- [ ] Tính theo P50 hoặc P60 tùy chiến lược (pay to attract/retain)
- [ ] Phân theo vùng HN/HCM/Khác
- [ ] Có quy tắc Compa-ratio
- [ ] Có chính sách điều chỉnh (annual review, promotion)
- [ ] CEO/CFO đã approve ngân sách payroll
