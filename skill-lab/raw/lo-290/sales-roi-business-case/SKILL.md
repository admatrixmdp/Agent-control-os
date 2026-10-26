---
name: sales-roi-business-case
description: |
  Viết business case ROI cho KH B2B — quantify pain, calculate savings, payback period, NPV cho EB duyệt. Trigger phrases: "viết business case", "ROI business case", "tính ROI cho khách", "business case template", "soạn justification mua", "ROI calculator deal", "payback period", "NPV calculation sales", "build business case khách hàng", "tính lợi ích mua hàng". Output là Docx business case + Excel ROI model.
---

# ROI Business Case Builder

## Mục Tiêu
Trang bị AE template viết business case 3-5 trang cho Economic Buyer / CFO duyệt mua, có số liệu định lượng pain → savings → payback → NPV — không dựa "feel good" mà dựa data.

## Khi Nào Dùng
- Deal enterprise >$50K
- EB đòi business case formal
- Đối thủ price thấp hơn — chứng minh ROI thắng giá
- Renewal cần justify giữ ngân sách
- Multi-stakeholder cần document share

## Bước 1: Quantify Pain (Cost of Current State)
Pull data từ KH discovery:
- **Time cost**: số NV × giờ/tháng × hourly rate
- **Money cost**: tool hiện tại + lost revenue + waste
- **Opportunity cost**: deal/customer lost do problem
- **Risk cost**: compliance fine, churn risk

Vd: AE tốn 2h/ngày admin = 2 × 22 × 50 AE × $50/h = $110K/tháng = $1.32M/năm

## Bước 2: Quantify Solution Benefit
3 nhóm savings:
- **Hard savings**: cắt tool, cắt headcount, cắt waste (số chắc)
- **Soft savings**: time saved, productivity (số ước lượng)
- **Revenue uplift**: deal close nhanh hơn, retention tốt hơn

Conservative scenario + base case + best case (cho EB chọn).

## Bước 3: Investment Total
- License/Subscription năm 1, 2, 3
- Implementation cost (one-time)
- Training cost
- Internal IT/Ops time
- Tổng TCO 3 năm

## Bước 4: ROI Calculation
- **Payback period**: month investment recovers
- **3-year ROI**: (3-year benefit - 3-year cost) / 3-year cost × 100%
- **NPV** (nếu CFO sophisticated): discount rate 10%

Format:
- Investment: $300K (Year 1)
- Annual benefit: $750K
- Payback: 5 tháng
- 3-year ROI: 650%
- NPV (10% discount): $1.5M

## Bước 5: Risk & Assumption
Liệt kê assumption + risk:
- Adoption rate: assume 80%, risk nếu <60%
- Implementation timeline: 12 tuần, risk +4 tuần
- Benefit realization: 3 tháng ramp
- Vendor risk + mitigation

Showing assumption = trust signal cho CFO.

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce/HubSpot MCP: pull deal data + KH context
- WebFetch: benchmark industry ROI report (Forrester TEI, Gartner)
- Excel MCP: build interactive ROI model
- DocuSign/PandaDoc MCP: gửi business case có e-sign acknowledge

**Fallback API:**
```python
# ROI model
def calc_roi(time_saved_hrs_month, fte_count, hourly, license_annual, impl_one_time):
    annual_benefit = time_saved_hrs_month * 12 * fte_count * hourly
    year_1_cost = license_annual + impl_one_time
    year_2_3_cost = license_annual * 2
    total_3y_benefit = annual_benefit * 3
    total_3y_cost = year_1_cost + year_2_3_cost
    payback = (year_1_cost / (annual_benefit / 12))
    roi_3y = (total_3y_benefit - total_3y_cost) / total_3y_cost * 100
    return {"payback_months": payback, "roi_3y_pct": roi_3y,
            "net_benefit_3y": total_3y_benefit - total_3y_cost}
```

## Bước 7: Output Format
- **File 1**: `business_case_<customer>.docx` — 5 trang đầy đủ
- **File 2**: `roi_model_<customer>.xlsx` — interactive, EB tự sandbox
- **File 3**: `executive_summary.pdf` — 1 trang số liệu cho CEO/CFO
- **File 4**: `cover_email.md` — gửi kèm có CTA
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Số liệu pain dựa data KH thật (không giả định)
- [ ] 3 scenario (conservative/base/best)
- [ ] Payback <12 tháng
- [ ] 3-year ROI >200%
- [ ] Assumption liệt kê transparent
- [ ] Champion review trước gửi EB
- [ ] Có 1 trang executive summary
