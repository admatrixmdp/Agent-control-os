---
name: mkt-ab-test-planner
description: |
  Plan A/B test landing page/ads cho doanh nghiệp Việt Nam — hypothesis, metric, sample size, traffic split, timeline, decision rule. Tự động tính sample size cần thiết. Kích hoạt khi người dùng nói: "plan A/B test", "thiết kế A/B test", "split test landing", "A/B test ads", "kế hoạch test conversion", "lên test landing page", "AB test hypothesis", "tính sample size test". Output là Markdown plan + Excel calc.
---

# Plan A/B Test Landing/Ads

## Mục Tiêu
Mỗi test có hypothesis rõ, đủ traffic để significance 95%, kết quả ra quyết định dứt khoát (ship/kill). Tránh "test cảm tính" tốn 3 tuần không học được gì.

## Khi Nào Dùng
- Landing CR <2%
- Ads CPA cao bất thường
- Trước khi scale ngân sách x2
- Khi launch creative mới
- Tối ưu funnel checkout

## Bước 1: Brief Test
Hỏi:
1. URL/Ad cần test
2. Metric chính (CR, CTR, CPA, ROAS)
3. Metric phụ (AOV, bounce)
4. Current baseline (vd CR 2%)
5. Expected lift (vd +25%)
6. Traffic/ngày
7. Hypothesis muốn test

## Bước 2: Viết Hypothesis Chuẩn
Format:
> "Vì [insight/data], chúng tôi tin rằng [thay đổi X] sẽ làm [metric Y] tăng [Z%] cho [segment]. Đo bằng [metric chính] trong [thời gian]."

Ví dụ: "Vì 60% mobile user rời checkout, chúng tôi tin rằng đổi form 5 field → 2 field sẽ tăng CR mobile +30%. Đo bằng CR checkout trong 14 ngày."

## Bước 3: Tính Sample Size & Plan
Công thức sample size: dùng calc Optimizely/AB Tasty hoặc Python.
- Baseline CR = 2%, Expected = 2.5%, Power 80%, Sig 95% → cần ~5.000 visitor/variant.

Phân chia traffic 50/50. Timeline = sample size / daily traffic. Tránh test dưới 1 tuần (variance ngày trong tuần).

**Quyết định**: kết thúc test khi
- Đủ sample size + significance 95% → ship variant thắng
- Đạt 2x sample size mà không sig → no winner, kill

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Optimize (legacy) / VWO / AB Tasty MCP
- GA4 MCP: track CR + sig
- Meta Ads MCP: split test ad
- Google Sheets MCP: log result
- Notion MCP: experiment library

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tính sample size + p-value
from statsmodels.stats.proportion import proportions_ztest, samplesize_proportions_2indep
n = samplesize_proportions_2indep(diff=0.005, prop2=0.02, alpha=0.05, power=0.8)
# A/B test result
z,p = proportions_ztest([conv_a, conv_b],[n_a, n_b])
print('p-value:', p)
```

## Bước 5: Output Format
- File `.md` test plan đầy đủ:
  - Hypothesis
  - Metric + baseline + expected
  - Sample size + duration
  - Decision rule
  - Risk + rollback plan
- File `.xlsx` calculator + result log
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Hypothesis có data backup
- [ ] Sample size đủ statistical power
- [ ] Duration >= 7 ngày
- [ ] Decision rule rõ
- [ ] Variant chỉ khác 1 yếu tố
- [ ] Có rollback plan
- [ ] Test 1 thứ tại 1 thời điểm
