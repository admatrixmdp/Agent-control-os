---
name: ceo-hiring-plan
description: |
  Lập kế hoạch tuyển dụng năm theo phòng ban + budget — tính headcount cần, role priority, time-to-hire, cost-per-hire, recruiter capacity, signing bonus pool.
  Kích hoạt khi người dùng nói: "kế hoạch tuyển dụng", "hiring plan", "headcount plan", "kế hoạch hire năm", "workforce planning", "recruitment plan", "hiring budget", "manpower planning".
  Output là Excel hiring plan + HTML timeline.
---

# CEO Hiring Plan — Kế Hoạch Tuyển Dụng Năm

## Mục Tiêu
Hire sai cadence → over-hire (burn cash) hoặc under-hire (kéo tăng trưởng). Skill này tạo plan có data từ revenue target ngược về headcount cần.

## Khi Nào Dùng
- Đầu năm tài chính
- Sau khi raise vốn
- Trước expansion
- Sau lay-off cần re-plan
- Khi recruiter overload

## Bước 1: Reverse Engineer Từ Revenue Goal
- Revenue target năm
- Revenue per employee benchmark (SaaS: $100-200k, services: $80-150k)
- → Total headcount cần cuối năm
- Headcount đầu năm
- → Net new hires cần
- Plus attrition replacement (10-25% turnover)
- → Total gross hires

## Bước 2: Phân Bổ Theo Phòng Ban
Tỷ lệ chuẩn SaaS B2B (tham khảo, điều chỉnh theo công ty):
- Engineering: 30-40%
- Sales: 15-25%
- Customer Success: 10-15%
- Marketing: 8-12%
- G&A (HR, Finance, Legal): 8-12%
- Operations/Other: 5-10%

Mỗi phòng có 5 cột: hiện tại / net new / replacement / total hire / end headcount.

## Bước 3: Role Priority + Timeline
Mỗi role có:
- Title + level (Junior/Mid/Senior/Lead/Director/VP)
- Priority (P0/P1/P2)
- Start month
- Time-to-hire estimate (30-90 ngày)
- Salary band (min/mid/max)
- Signing bonus nếu cần
- Recruiter assigned

Plot lên timeline 12 tháng để thấy peak nào quá tải.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: pull current headcount từ HRIS sheet
- Greenhouse/Lever MCP: pull pipeline hiện tại
- WebSearch: benchmark salary band Việt Nam 2026
- Notion MCP: hiring plan database
- Linear MCP: tạo issue cho mỗi req cần mở

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Headcount projection
target_revenue = 100_000_000_000  # 100 tỷ VND
rev_per_emp = 1_500_000_000  # 1.5 tỷ
end_hc = target_revenue / rev_per_emp
attrition = 0.18
net_new = end_hc - start_hc
gross_hire = net_new + start_hc * attrition
print(f"Cần hire {gross_hire:.0f} người")
```

## Bước 5: Output Format
- Excel `hiring-plan-YYYY.xlsx`:
  - Sheet 1: Summary by department
  - Sheet 2: Role detail (1 row/role)
  - Sheet 3: Timeline Gantt
  - Sheet 4: Budget (salary + bonus + recruiter cost)
- HTML timeline visualize
- 1-page summary cho board
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Revenue per employee có benchmark
- [ ] Mỗi role có owner + priority
- [ ] Timeline có recruiter capacity check
- [ ] Salary band có benchmark Việt Nam
- [ ] Budget tổng tính cả benefits (×1.3)
- [ ] Buffer attrition replacement
