---
name: hr-headcount-plan
description: |
  Lập kế hoạch headcount năm theo phòng ban cho doanh nghiệp Việt Nam, gắn với business plan, attrition giả định, replacement vs new hire, budget payroll tổng và phân kỳ quý.
  Kích hoạt khi người dùng nói: "headcount plan", "kế hoạch nhân sự năm", "manpower plan", "workforce planning", "kế hoạch tuyển dụng năm", "budget payroll", "headcount budget", "kế hoạch nhân lực", "FTE plan", "manpower budget".
  Output là file .xlsx HC Plan + budget payroll + recruitment calendar + scenario simulation.
---

# HR - Kế Hoạch Headcount Năm

## Mục Tiêu
Trả lời 3 câu hỏi cho CEO/CFO: (1) Năm tới cần bao nhiêu NV để hỗ trợ business plan? (2) Chi phí lương + thưởng tổng bao nhiêu? (3) Khi nào tuyển, ai tuyển trước?

## Khi Nào Dùng
- Q4 lập budget năm sau
- Sau khi ban hành chiến lược 1-3 năm
- Re-plan giữa năm nếu business thay đổi
- Trước khi xin funding (investor hỏi)

## Bước 1: Thu Thập Driver Business
Hỏi mỗi Head of Dept:
- OKR/Revenue target 2026
- Workload hiện tại có gánh được không?
- 3 dự án lớn năm tới + manpower estimate
- Có replace ai không (NV nghỉ, promote)?
- Có outsource/automation thay người không?

Cross-check với CFO về capacity ngân sách.

## Bước 2: Tính Toán Headcount Cần
Công thức:
```
HC end-of-year = HC current + New Hires - Attrition
HC peak = max(HC quarterly)
FTE-month = Σ (HC monthly)
Payroll = FTE-month × avg cost per FTE
```

Giả định Attrition rate:
- Tech: 18-25%/năm
- Sales: 25-35%
- Ops/Admin: 10-15%
- Manager+: 8-12%

Phân kỳ tuyển theo quý:
| Q1 | Q2 | Q3 | Q4 |
|---|---|---|---|
| 15 hires | 25 hires | 20 hires | 10 hires |

Lưu ý lead time tuyển: junior 4-6 tuần, senior 8-12 tuần, manager 12-20 tuần.

## Bước 3: Tính Cost Per Hire + Total Cost
**Cost per Hire (CPH)**:
- External cost: job board, agency (15-25% lương năm), background check
- Internal cost: recruiter time, hiring manager time
- Onboarding: laptop, training, ramp-up time
- Average ~ 8-15tr (staff), 30-60tr (manager), 100tr+ (executive)

**Total Annual Payroll**:
```
= Σ (lương tháng × 12 × số NV mỗi level)
+ Bonus (10-30%)
+ BHXH/BHYT/BHTN DN đóng (~21.5%)
+ Benefit (lunch, transport, insurance health)
+ CPH × new hires
```

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Sheets MCP: master HC plan + scenario simulation
- Gmail MCP: gửi proposal cho CFO + CEO
- Drive MCP: lưu version control HC plan
- Calendar MCP: lịch hiring kickoff per quý
- WebSearch: benchmark attrition rate VN (Talentnet, Mercer)

**Fallback bằng API (HRIS + Finance):**
```python
# Sync với hệ thống tài chính (Misa/Bravo) để check budget khả thi
import requests, pandas as pd
hc_plan = pd.read_excel("hc_plan_2026.xlsx")
total_payroll = (hc_plan["base_salary"] * 12 * 1.5).sum()  # +50% cho bonus+BHXH

# Push vào ERP để Finance review
requests.post("https://api.misa.amis.vn/v1/finance/budget",
    json={"category": "Payroll 2026", "amount": total_payroll,
          "breakdown": hc_plan.to_dict("records")},
    headers={"Authorization": f"Bearer {TOKEN}"})
```

## Bước 5: Output Format
- File `.xlsx` HC Plan Master (per dept, per quarter, per level)
- File `.xlsx` Budget Payroll (gross + BHXH + bonus + benefit)
- File `.xlsx` Recruitment Calendar (vị trí, deadline, recruiter)
- File `.xlsx` Scenario Simulation (3 cases: conservative/base/aggressive)
- File `.pptx` Slide trình BOD
- Lưu tại: `/outputs/HeadcountPlan_<YYYY>.xlsx`

## Checklist Trước Khi Giao
- [ ] HC plan align business OKR/revenue target
- [ ] Có attrition assumption theo phòng ban
- [ ] Phân kỳ quý (không dồn Q4)
- [ ] Có CPH cụ thể
- [ ] Có Total Payroll cộng BHXH + thưởng + benefit
- [ ] 3 scenarios (con-base-agg)
- [ ] CFO đã review affordability
- [ ] Heads of Dept ký nhận HC
- [ ] Recruitment calendar realistic (lead time đúng)
- [ ] Có cơ chế re-forecast giữa năm
