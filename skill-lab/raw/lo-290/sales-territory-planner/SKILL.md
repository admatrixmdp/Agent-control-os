---
name: sales-territory-planner
description: |
  Plan khu vực bán hàng theo geo + vertical + revenue potential, balance workload AE. Trigger phrases: "territory planning", "plan khu vực bán hàng", "chia territory AE", "phân vùng sales", "territory design", "geo + vertical sales plan", "lập kế hoạch territory", "balance sales territory", "patch sales", "sales coverage plan". Output là Excel territory map + slide rationale + map visual.
---

# Sales Territory Planner

## Mục Tiêu
Phân chia 50-300 AE vào territory cân bằng theo TAM, workload, travel cost — đảm bảo mỗi AE có equal opportunity và mỗi KH có 1 owner rõ ràng, tránh chồng chéo.

## Khi Nào Dùng
- Annual planning đầu năm
- Sau thêm/giảm headcount đáng kể
- Sau M&A merge sales team
- Restructure GTM (add channel)
- Khi AE complain "patch không công bằng"

## Bước 1: Define Dimension Chia

**Geo-based**: chia theo region/state/city
**Vertical-based**: theo industry (FMCG/Retail/Finance)
**Hybrid**: geo + vertical (vd "SE Asia FMCG")
**Named account**: top 20 enterprise = 1 AE/account
**Round-robin**: SMB nhỏ chia round

Chọn dimension theo product complexity + GTM motion.

## Bước 2: TAM Mapping mỗi Patch
Mỗi territory patch tính:
- TAM (total accounts match ICP)
- SAM (% penetrable)
- Existing customer base
- Open opportunity pipeline
- Historical revenue
- Growth potential 12 tháng

Goal: TAM × win rate ≈ AE quota.

## Bước 3: Workload Balance
Đo:
- # account / AE
- Travel distance (geo)
- Deal complexity (size + cycle)
- Existing relationship density

Threshold:
- Max 150 accounts / AE (SMB)
- Max 30 accounts / AE (enterprise)
- Travel <3h / meeting

## Bước 4: Rules & Exceptions

**Conflict resolution**:
- Account moves territory → split commission 50/50 transition quý
- House account (key strategic) → exception, không chia
- Channel-influenced → channel + direct split

**Named account list**: top 20-50 KH chiến lược → assign theo profile AE, không random.

## Bước 5: Roll-out Plan
- Communicate 30 ngày trước effective
- Transition handover 14 ngày
- Comp plan grace period 1 quý
- Weekly check-in 4 tuần đầu
- Tune sau Q1 nếu cần

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce MCP: account assignment rules
- Mapping MCP (Mapbox/Google Maps): geo visualization
- ZoomInfo/Apollo MCP: TAM data
- BI MCP: workload dashboard
- Excel MCP: territory model

**Fallback API:**
```python
# Optimize territory với scipy
from scipy.optimize import linear_sum_assignment
import numpy as np
# Build cost matrix: AE × Patch (cost = -opportunity)
patches = get_patches()
aes = get_AEs()
cost = np.array([[calc_fit(ae, p) for p in patches] for ae in aes])
row_ind, col_ind = linear_sum_assignment(cost)
assignment = {aes[i]: patches[j] for i, j in zip(row_ind, col_ind)}
```

## Bước 7: Output Format
- **File 1**: `territory_plan.xlsx` — AE × Patch × TAM × Quota × Workload
- **File 2**: `territory_map.html` — interactive map (Folium/Mapbox)
- **File 3**: `named_account_list.xlsx` — top accounts + assignment + rationale
- **File 4**: `territory_rationale.pptx` — slide cho leadership
- **File 5**: `rollout_plan.md` — communication + transition
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Workload balance ±20%
- [ ] Named account assigned by fit
- [ ] Conflict resolution rule rõ
- [ ] Travel reasonable
- [ ] Communication 30 ngày advance
- [ ] Comp transition grace period
