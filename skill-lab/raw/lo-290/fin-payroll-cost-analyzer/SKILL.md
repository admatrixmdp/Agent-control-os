---
name: fin-payroll-cost-analyzer
description: |
  Phân tích chi tiết chi phí lương + phúc lợi theo phòng ban, chức danh, level - so với budget
  và benchmark thị trường. Trigger phrases: "phân tích lương", "payroll analysis",
  "chi phí lương phòng ban", "labor cost", "tỷ lệ lương trên doanh thu", "compensation analysis",
  "phân tích quỹ lương", "headcount cost", "payroll dashboard", "labor productivity".
  Output là Excel phân tích + HTML dashboard interactive.
---

# Phân Tích Chi Phí Lương Theo Phòng Ban

## Mục Tiêu
Giúp CFO/HR Director nhìn xuyên suốt cấu trúc chi phí nhân sự - phòng nào ROI cao, phòng nào
phình to, có gap với thị trường ở vị trí nào. Phát hiện sớm pay gap dẫn tới turnover.

## Khi Nào Dùng
- Mỗi tháng/quý review chi phí lương
- Trước khi lập budget headcount năm mới
- Khi xét tăng lương/thưởng cuối năm
- Khi turnover cao ở 1 phòng - check xem có pay gap không
- Trước M&A để đánh giá synergy chi phí

## Bước 1: Thu Thập Dữ Liệu Lương
Từ HRIS/Payroll system:
- Mã NV, họ tên, phòng ban, chức danh, level (L1-L10), ngày vào
- Lương cơ bản, phụ cấp (ăn, xăng, điện thoại), thưởng tháng/quý/năm
- BHXH-BHYT-BHTN-KPCĐ (cả phần DN + phần NV)
- Phúc lợi: bảo hiểm sức khoẻ, du lịch, training budget
- OT, hoa hồng (sales)

Tổng = **Total Cost of Employment (TCOE)** chứ không chỉ Net pay.

## Bước 2: Phân Tích Đa Chiều
**Theo phòng ban:**
- Tổng TCOE, headcount, TCOE bình quân
- % trên tổng OpEx, % trên doanh thu
- Doanh thu/đầu người (productivity)

**Theo level:**
- Cấu trúc kim tự tháp - có quá nhiều middle management không?
- Compa-ratio = Salary / Mid-point benchmark

**Theo loại CP:**
- Lương cơ bản %
- Variable (thưởng + hoa hồng) %
- Statutory (BHXH...) %
- Benefits %
→ Healthy mix: 60% base, 20% variable, 15% statutory, 5% benefits

## Bước 3: Benchmark & Cảnh Báo
**So với chính mình:**
- Cùng kỳ năm trước (YoY)
- Tốc độ tăng lương vs tốc độ tăng doanh thu
- Phòng nào có TCOE tăng nhưng productivity giảm → warning

**So thị trường:**
- Dùng survey Mercer, Talentnet, VietnamSalary
- Position nào pay <P25 → rủi ro mất người
- Position nào pay >P75 → review có justify không

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Pull payroll register hàng tháng
- Google Drive MCP: Lưu báo cáo confidential, set quyền giới hạn
- Gmail MCP: Gửi báo cáo cá nhân hoá cho từng Department Head
- WebSearch: Tra lương thị trường trên TopCV, VietnamWorks, Robert Walters report

**Fallback bằng API:**
```python
# Gọi MISA AMIS HRM API lấy payroll register
import requests
r = requests.get(
    "https://api.misa.vn/amis/hrm/v1/payroll",
    params={"period": "2026-05"},
    headers={"Authorization": f"Bearer {TOKEN}"}
)
payroll = r.json()["data"]
# Aggregate by department
import pandas as pd
df = pd.DataFrame(payroll)
summary = df.groupby("department").agg(
    headcount=("employee_id", "count"),
    tcoe=("total_cost", "sum"),
    avg_tcoe=("total_cost", "mean")
)
```

## Bước 5: Output Format
1. **Excel phân tích** (`payroll_analysis_T05_2026.xlsx`): Sheet "ByDept", "ByLevel", "ByPosition", "Benchmark", "Outliers" (NV có cost gấp >2 lần peer).
2. **HTML dashboard** (`payroll_dashboard.html`): Treemap phòng ban × TCOE, sankey flow lương theo cấu phần, scatter productivity vs cost.
3. **PDF executive memo** (`payroll_memo.pdf`): 3 trang - top findings + đề xuất tối ưu cho CEO.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/payroll/`

## Checklist Trước Khi Giao
- [ ] Tổng payroll khớp sổ cái (TK 334, 338)
- [ ] Đã ẩn/mã hoá tên cá nhân trong dashboard public
- [ ] So sánh đủ 3 dimension (Dept, Level, Position)
- [ ] Có benchmark thị trường ≤ 12 tháng tuổi
- [ ] Insight phải có "so what" - đề xuất hành động
- [ ] Quyền truy cập chỉ CFO, CEO, HRD
