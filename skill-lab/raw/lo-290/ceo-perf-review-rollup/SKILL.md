---
name: ceo-perf-review-rollup
description: |
  Tổng hợp đánh giá hiệu suất công ty cuối năm — pull score từ HRIS/Sheets, ranking distribution, calibration giữa phòng ban, đề xuất bonus & promotion theo budget.
  Kích hoạt khi người dùng nói: "rollup performance review", "tổng hợp đánh giá năm", "perf review CEO", "calibration performance", "annual review rollup", "phân phối đánh giá", "company-wide review", "end-of-year performance".
  Output là HTML dashboard + Excel calibration.
---

# CEO Performance Review Rollup — Tổng Hợp Đánh Giá Cả Công Ty

## Mục Tiêu
Cuối năm CEO duyệt 200 đánh giá cá nhân = 2 ngày đọc. Skill này rollup thành dashboard 1 trang, flag phòng nào "everyone is great" (inflation), gợi ý calibration.

## Khi Nào Dùng
- Annual performance review cycle (Q4)
- Mid-year check-in (Q2)
- Trước bonus pool allocation
- Trước promotion announcement
- Khi nghi ngờ rating inflation

## Bước 1: Thu Thập Đánh Giá Cá Nhân
- Pull từ HRIS / Lattice / 15Five / Notion
- Mỗi nhân viên có: manager rating (1-5), peer rating, self rating
- Goal achievement %
- Promotion recommendation (Y/N)
- Bonus % proposed

## Bước 2: Distribution Analysis
Phân phối rating công ty:
- % top performers (5/5)
- % strong (4)
- % meeting (3)
- % needs improvement (2)
- % not meeting (1)

Healthy distribution (bell curve):
- 10-15% top
- 25-30% strong
- 40-50% meeting
- 10-15% needs imp
- 2-5% not meeting

Flag phòng ban lệch xa (VD 80% top → inflation).

## Bước 3: Calibration Giữa Phòng Ban
- So sánh distribution của Eng vs Sales vs Ops
- Nếu Eng có 60% top vs Sales 20% top → cần calibration meeting
- Đề xuất re-rate những người borderline
- Kiểm tra bias (gender, tenure, manager favorite)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Lattice/15Five MCP: pull review data
- Google Sheets MCP: backup HRIS export
- Slack MCP: notify managers calibration meeting
- Notion MCP: lưu calibration notes confidential
- Gmail MCP: send promotion letters đã approve

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Distribution check
import pandas as pd
df = pd.read_csv('reviews.csv')
dist = df.groupby(['department', 'rating']).size().unstack(fill_value=0)
dist_pct = dist.div(dist.sum(axis=1), axis=0)
# Flag department có >50% rating 5
inflated = dist_pct[dist_pct[5] > 0.5].index.tolist()
print(f"Inflated departments: {inflated}")
```

## Bước 5: Output Format
- HTML dashboard CEO 1 trang:
  - Distribution chart công ty + per dept
  - Bonus pool allocation
  - Promotion list (Y/N approved)
  - Calibration alerts
- Excel `perf-rollup-YYYY.xlsx` confidential
- 1-on-1 prep cards cho mỗi CXO discuss team
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/` (encrypted)

## Checklist Trước Khi Giao
- [ ] Tất cả nhân viên có rating
- [ ] Distribution flag phòng inflation
- [ ] Calibration đã chạy với managers
- [ ] Bonus pool fit budget
- [ ] Bias check (gender, tenure)
- [ ] File encrypted, access list giới hạn
