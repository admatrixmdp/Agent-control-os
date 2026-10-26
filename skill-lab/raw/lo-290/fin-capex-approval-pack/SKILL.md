---
name: fin-capex-approval-pack
description: |
  Lập hồ sơ phê duyệt CapEx (chi đầu tư) đầy đủ NPV, IRR, payback period, sensitivity và
  rủi ro - chuẩn cho HĐQT duyệt. Trigger phrases: "CapEx approval", "đầu tư tài sản",
  "NPV IRR project", "đề xuất đầu tư", "investment proposal", "payback period",
  "phân tích đầu tư", "ROI dự án", "feasibility study", "business case CapEx".
  Output là Excel financial model + PDF presentation pack.
---

# Pack Phê Duyệt CapEx (NPV / IRR / Payback)

## Mục Tiêu
Chuẩn hoá quy trình xin phê duyệt CapEx - tránh tình trạng đề xuất "cảm tính" lên HĐQT.
Mỗi pack bắt buộc có 3 chỉ số NPV/IRR/Payback + sensitivity + rủi ro, giúp HĐQT quyết
nhanh, đúng.

## Khi Nào Dùng
- Mua máy móc, thiết bị, nhà xưởng mới
- Mở chi nhánh, store mới
- Đầu tư phần mềm, hệ thống ERP/CRM
- Mua lại doanh nghiệp khác (M&A)
- Phát triển sản phẩm mới có CapEx lớn

## Bước 1: Mô Tả Dự Án & Business Case
- **Tên dự án, mục tiêu kinh doanh** (1 trang)
- **Investment** (chi ban đầu): mua tài sản, lắp đặt, training, vốn lưu động ban đầu
- **Vòng đời dự kiến** (5, 7, 10 năm)
- **Phương án thay thế** (no-go, outsource, làm nhỏ hơn) để so sánh

## Bước 2: Xây Dòng Tiền Dự Án
Theo từng năm trong vòng đời:

**Inflows:**
- Doanh thu tăng thêm từ dự án
- Chi phí tiết kiệm được
- Giá trị thanh lý cuối kỳ
- Hoàn vốn lưu động cuối kỳ

**Outflows:**
- Chi đầu tư ban đầu (Year 0)
- Chi vận hành hàng năm (lương, NVL, bảo trì)
- CapEx duy trì hàng năm
- Tăng vốn lưu động hàng năm
- Thuế TNDN trên LN tăng thêm

```
FCF mỗi năm = EBIT × (1-t) + Depreciation - ΔWC - CapEx
```

## Bước 3: Tính NPV, IRR, Payback
**NPV** (Net Present Value):
```
NPV = Σ FCF_t / (1+WACC)^t - Initial Investment
```
- WACC: thường 12-15% cho SME VN, 10-12% cho DN lớn
- NPV > 0: đáng đầu tư

**IRR** (Internal Rate of Return):
- Là discount rate mà NPV = 0
- IRR > WACC + hurdle rate (3-5%) → OK

**Payback period:** Năm hoàn vốn (cộng dồn FCF chạm về 0)
- Discounted Payback: dùng FCF chiết khấu

**Profitability Index** = PV(FCF) / Investment → so sánh các dự án cạnh tranh nguồn vốn.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Build model tham số hoá, share team Finance review
- Google Drive MCP: Lưu pack chính thức + biên bản họp HĐQT
- WebSearch: Tra WACC ngành (Damodaran), lãi suất chiết khấu chuẩn
- WebFetch: Tham khảo case study tương tự đã công bố

**Fallback bằng API:**
```python
# Tính IRR bằng numpy financial
import numpy_financial as npf
cashflows = [-10_000_000_000,  # Year 0
              2_000_000_000, 2_500_000_000, 3_000_000_000,
              3_500_000_000, 4_000_000_000]  # Year 1-5
wacc = 0.13
npv = npf.npv(wacc, cashflows)
irr = npf.irr(cashflows)
print(f"NPV @ WACC {wacc:.0%}: {npv:,.0f}đ")
print(f"IRR: {irr:.2%}")

# Monte Carlo sensitivity 1000 runs
import numpy as np
rng = np.random.default_rng(42)
npvs = []
for _ in range(1000):
    shocked = [cf * rng.uniform(0.8, 1.2) for cf in cashflows]
    npvs.append(npf.npv(wacc, shocked))
print(f"P10 NPV: {np.percentile(npvs, 10):,.0f}")
print(f"P90 NPV: {np.percentile(npvs, 90):,.0f}")
```

## Bước 5: Output Format
1. **Excel financial model** (`CapEx_<projectname>_2026.xlsx`): Sheet "Assumptions", "CashFlow", "NPV_IRR", "Sensitivity" (1D + 2D), "ScenarioBest_Base_Worst", "Risk_Mitigation".
2. **PDF approval pack** (`CapEx_approval_<project>.pdf`): 8-12 trang - Executive Summary, Business Case, Financial Analysis, Risks, Recommendation, Sign-off block.
3. **PPTX slide deck** (`CapEx_<project>.pptx`): 10 slide trình HĐQT.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/capex/`

## Checklist Trước Khi Giao
- [ ] FCF không double-count (khấu hao đã trừ rồi không trừ lại)
- [ ] WACC dùng đúng (cost of debt × (1-t), cost of equity CAPM)
- [ ] Có ít nhất 3 kịch bản Best/Base/Worst
- [ ] Sensitivity các biến quan trọng: revenue, COGS, WACC
- [ ] Có rủi ro & mitigation cụ thể
- [ ] Approval matrix theo mức đầu tư (≤1B: TGĐ, 1-5B: HĐQT, >5B: ĐHCĐ)
