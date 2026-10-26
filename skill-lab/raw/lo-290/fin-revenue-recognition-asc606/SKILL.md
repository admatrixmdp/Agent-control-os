---
name: fin-revenue-recognition-asc606
description: |
  Ghi nhận doanh thu theo chuẩn ASC 606 / IFRS 15 - phương pháp 5 bước xác định khi nào và
  bao nhiêu doanh thu được ghi nhận. Trigger phrases: "ghi nhận doanh thu",
  "revenue recognition", "ASC 606", "IFRS 15", "5-step model", "performance obligation",
  "transaction price", "POC method", "deferred revenue", "SaaS revenue". Output là
  Excel checklist + memo policy.
---

# Ghi Nhận Doanh Thu Chuẩn ASC 606 / IFRS 15

## Mục Tiêu
Áp dụng chuẩn mực kế toán quốc tế (ASC 606 / IFRS 15) cho ghi nhận doanh thu - quan trọng
với DN SaaS, dịch vụ dài hạn, construction, multi-element. Tránh ghi nhận sai (sớm/muộn)
ảnh hưởng đến BCTC + valuation.

## Khi Nào Dùng
- DN SaaS/subscription cần xác định khi nào ghi nhận
- DN có HĐ multi-year, milestone-based
- DN construction (POC - Percentage of Completion)
- DN có bundle products (HĐ kèm services, warranty)
- Chuẩn bị IPO yêu cầu IFRS / US GAAP

## Bước 1: Mô Hình 5 Bước
**Step 1: Identify Contract with Customer**
- Có cam kết 2 bên rõ ràng (HĐ, PO, email)
- Quyền và nghĩa vụ identified
- Payment terms agreed
- Có commercial substance
- Likelihood of collection

**Step 2: Identify Performance Obligations (POs)**
- Mỗi PO là 1 lời hứa giao 1 sản phẩm/dịch vụ "distinct"
- Distinct = (a) KH có lợi từ riêng nó, (b) tách biệt được trong HĐ
- Ví dụ: Bán phần mềm + implementation + 3 năm support = 3 POs riêng

**Step 3: Determine Transaction Price**
- Giá cố định + variable consideration (discount, rebate, penalty)
- Loại trừ amount thu hộ (sales tax, shipping pass-through)
- Significant financing component nếu thanh toán >12 tháng
- Non-cash consideration ước tính fair value

**Step 4: Allocate Price to POs**
- Theo Standalone Selling Price (SSP) của từng PO
- Phương pháp: observable price, adjusted market, expected cost+margin, residual

**Step 5: Recognize Revenue When/As PO is Satisfied**
- **Point in time** (1 lần): khi control chuyển sang KH
- **Over time** (theo thời gian): khi 1 trong 3 điều kiện met:
  - KH nhận benefit đồng thời
  - Performance tạo TS cho KH control
  - Không có alternative use + có enforceable right to payment

## Bước 2: Áp Dụng Cụ Thể Theo Ngành
**SaaS subscription:**
- Subscription fee: over time (straight-line over service period)
- Setup fee: nếu distinct service → revenue khi delivered; nếu không → defer over expected customer life
- Implementation: thường over time POC

**Construction:**
- POC method: % completion = cost incurred / total estimated cost
- Recognize revenue + cost theo %
- Loss-making contract → recognize loss ngay

**Software license:**
- Functional IP (distinct from updates): point in time tại delivery
- Symbolic IP (giá trị từ ongoing): over time

**Multi-element bundles:**
- Identify từng PO
- Allocate giá theo SSP
- Recognize từng PO riêng

## Bước 3: Disclosure & Documentation
**Required disclosures:**
- Disaggregation of revenue (segment, channel, region, timing)
- Contract balances: AR, contract assets, contract liabilities
- Performance obligations: timing, remaining backlog
- Significant judgments
- Cost to obtain/fulfill contract

**Working paper documentation:**
- HĐ list + key terms summary
- PO identification per contract
- SSP calculation
- Recognition schedule per contract
- Variable consideration estimates with rationale

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Build revenue schedule sống cho từng HĐ
- Google Drive MCP: Lưu HĐ + memo phân tích POs
- WebSearch: Tra ASC 606 EY/PwC/Deloitte guidance, FASB updates
- Gmail MCP: Gửi CFO + audit memo về significant judgment

**Fallback bằng API:**
```python
# Tính revenue waterfall cho SaaS contracts
import pandas as pd
from datetime import date, timedelta

contracts = pd.DataFrame([
    {"id": "C001", "start": "2026-01-01", "term_months": 12,
     "ARR": 120_000_000, "setup": 30_000_000},
    {"id": "C002", "start": "2026-03-15", "term_months": 24,
     "ARR": 240_000_000, "setup": 60_000_000}
])

# Recognize subscription straight-line, setup over contract life
revenue_schedule = []
for _, c in contracts.iterrows():
    monthly_sub = c["ARR"] / 12
    monthly_setup = c["setup"] / c["term_months"]
    start = pd.to_datetime(c["start"])
    for m in range(c["term_months"]):
        rec_month = start + pd.DateOffset(months=m)
        revenue_schedule.append({
            "contract": c["id"], "month": rec_month.strftime("%Y-%m"),
            "subscription_rev": monthly_sub,
            "setup_rev": monthly_setup
        })

df = pd.DataFrame(revenue_schedule)
monthly_total = df.groupby("month")[["subscription_rev", "setup_rev"]].sum()
print(monthly_total)
```

## Bước 5: Output Format
1. **Excel revenue schedule** (`rev_recognition_2026.xlsx`): Sheet "Contracts" master, "5StepAnalysis" per contract, "Recognition_Schedule" theo tháng, "Deferred_Rev_Rollforward".
2. **PDF policy memo** (`revrec_policy_memo.pdf`): 10-15 trang policy DN áp dụng + key judgments.
3. **HTML dashboard** (`revrec_dashboard.html`): Backlog (RPO - Remaining Performance Obligation), recognized vs deferred, waterfall theo tháng.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/revrec/`

## Checklist Trước Khi Giao
- [ ] Mỗi HĐ đã apply 5-step model document
- [ ] POs identified rõ ràng, có rationale
- [ ] SSP có nguồn (price list, observable)
- [ ] Revenue recognition timing thống nhất per loại HĐ
- [ ] Deferred revenue trên BS khớp schedule
- [ ] Có disclosure đầy đủ theo IFRS 15 par 110-129
