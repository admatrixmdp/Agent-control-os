---
name: ops-okr-rollup-ops
description: |
  Rollup OKR vận hành theo phòng ban — tổng hợp Objective + Key Results từ các team con (sản xuất, kho, QC, bảo trì, mua hàng) lên cấp COO/CEO. Dùng skill này khi người dùng yêu cầu: "rollup OKR", "OKR vận hành", "tổng hợp OKR phòng ban", "OKR phòng Operations", "báo cáo OKR quý", "objective key result", "dashboard OKR", "OKR review meeting". Output là Excel rollup + HTML dashboard + slide tóm tắt.
---

# Rollup OKR Vận Hành Theo Phòng Ban

## Mục Tiêu
Tổng hợp OKR từ nhiều team con thành 1 bức tranh duy nhất cho COO/CEO, phát hiện KR nào ở mức rủi ro, KR nào lệch hướng so với Objective gốc.

## Khi Nào Dùng
- Quarterly OKR Review (đầu/giữa/cuối quý)
- Setup OKR đầu năm cho phòng Operations
- Đại hội cổ đông/board meeting
- Khi sếp hỏi "tổng quan tháng này Ops thế nào?"
- Audit OKR sau M&A/restructure

## Bước 1: Thu Thập OKR Tầng Dưới
Cho mỗi team con (Sản xuất, Kho, QC, Bảo trì, Mua hàng), thu:
- Objective (1 câu định tính)
- 3-5 Key Results (đo lường được, có baseline + target)
- Owner
- Tỷ lệ hoàn thành hiện tại (0-100%)
- Confidence level (1-10)
- Blockers

Format chuẩn:
```
Team: Sản xuất
O: Trở thành line sản xuất hiệu quả nhất khu vực Đông Nam Bộ
  KR1: OEE từ 65% → 80% (hiện 72%, 60%)
  KR2: Tỉ lệ NG từ 2.5% → 1.0% (hiện 1.8%, 50%)
  KR3: Lead time từ 7 ngày → 4 ngày (hiện 5.5 ngày, 50%)
```

## Bước 2: Mapping OKR Team → OKR Phòng Operations
Mỗi KR của team phải đóng góp vào KR cấp phòng. Vẽ bảng:
| OKR Phòng Ops | KR | Team đóng góp | KR team |
|---|---|---|---|
| Giảm chi phí vận hành 15% | Cost/unit ↓ 15% | Sản xuất | OEE ↑ |
|  |  | Mua hàng | Giá NVL ↓ 5% |
|  |  | Bảo trì | Downtime ↓ 30% |

Phát hiện KR mồ côi (không link lên objective phòng) → cảnh báo

## Bước 3: Tính Score Tổng Hợp
Score mỗi KR:
- 0.0-0.3: Đỏ (rủi ro cao)
- 0.4-0.6: Vàng (cần theo dõi)
- 0.7-1.0: Xanh (đang tốt)

Score Objective = trung bình có trọng số KR (mỗi KR có weight do team đặt)

Cảnh báo:
- Objective < 0.4: triệu họp khẩn
- KR confidence < 5: review weekly
- KR không update > 2 tuần: ping owner

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Đọc sheet OKR từng team
- Notion MCP: Pull OKR database nếu công ty dùng Notion
- Slack MCP: Gửi báo cáo rollup vào channel #leadership
- Google Drive MCP: Lưu file rollup quý có version
- Atlassian MCP: Sync với Jira nếu KR gắn với epics
- WebSearch: Benchmark OKR ngành sản xuất từ rework.withgoogle.com

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Đọc OKR từ nhiều sheet và rollup
import gspread, pandas as pd
gc = gspread.service_account()
teams = ["Sản xuất","Kho","QC","Bảo trì","Mua hàng"]
all_okr = []
for t in teams:
    ws = gc.open("OKR_Q2_2026").worksheet(t)
    df = pd.DataFrame(ws.get_all_records())
    df["Team"] = t
    all_okr.append(df)
master = pd.concat(all_okr)
master["Score"] = master["Current"] / master["Target"]
master.groupby("Objective_Phong")["Score"].mean().to_excel("rollup.xlsx")
```

## Bước 5: Output Format
- `OKR_Rollup_Q<n>.xlsx` — bảng tổng hợp với màu RYG
- `OKR_Dashboard.html` — dashboard có chart Sunburst Objective → KR
- `OKR_Summary.pptx` — slide 5-7 trang cho board meeting
- `OKR_Risks.md` — list KR đỏ + đề xuất unblock
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/OKR/`

## Checklist Trước Khi Giao
- [ ] Mọi KR team đều mapping lên KR phòng
- [ ] Confidence + % completion có cho từng KR
- [ ] Cảnh báo KR đỏ có owner và đề xuất
- [ ] Không quá 3-5 Objective cấp phòng
- [ ] Dashboard refresh tự động qua link Sheet
- [ ] Có lịch review weekly KR đỏ
