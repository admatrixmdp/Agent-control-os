---
name: sales-retail-shelf-audit
description: |
  Audit kệ hàng retail — share of shelf, planogram compliance, OOS, giá vs đối thủ. Trigger phrases: "audit kệ hàng", "shelf audit retail", "share of shelf", "kiểm tra trưng bày", "planogram compliance", "OOS retail audit", "audit cửa hàng", "merchandising audit", "kiểm POSM cửa hàng", "shelf check FMCG". Output là Excel audit form + dashboard + photo report.
---

# Retail Shelf Audit

## Mục Tiêu
Audit 50-500 cửa hàng retail theo tuần/tháng đo share of shelf, OOS, giá, POSM compliance — giúp brand catch issue trong 7 ngày thay vì 1 tháng.

## Khi Nào Dùng
- Brand FMCG có >100 retail point
- Post-promo measurement
- Counter đối thủ tung sản phẩm mới
- New SKU launch tracking
- Quarterly merchandising review

## Bước 1: Audit Field (10-15 Item)

**Availability**:
- SKU listed in store (Y/N)
- OOS (Out of Stock) count
- Days OOS estimate

**Visibility**:
- Share of shelf % (mình / tổng category)
- Shelf position (eye-level, gondola end, secondary)
- Facings count per SKU
- POSM present (poster, wobbler, shelf-talker)

**Pricing**:
- Shelf price vs RRP
- Promo price match T&C
- Competitor pricing

**Planogram**:
- Compliance % vs target
- Photo capture trước/sau merchandiser fix

## Bước 2: Field Survey App
Audit qua app (Repsly/Trax/Nielsen):
- Geo check-in
- Photo capture compulsory
- AI auto-detect facings (advanced)
- Submit offline + sync online
- Time-stamp + audit trail

## Bước 3: Scoring & Compliance Index
Mỗi store score 0-100:
- Availability 30 điểm
- Visibility 30 điểm
- Pricing compliance 20 điểm
- POSM 20 điểm

Aggregate:
- Per region / channel / chain
- Identify top/bottom store
- Trend WoW

## Bước 4: Action & Recovery
Issue detected → action:
- OOS → alert NPP / DSR replenish trong 24h
- Wrong price → POSM correction trong 48h
- Low share of shelf → call store owner / merchandiser
- POSM missing → re-deploy

Track close-loop time.

## Bước 5: Reporting Dashboard
Dashboard cho:
- ASM (Area Sales Manager): store-level
- Trade Marketing: chain/region
- CMO: brand-level
- CEO: KPI summary

Refresh weekly.

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Trax/Pensa MCP: AI image recognition shelf
- Salesforce Field Service MCP: route + audit
- Power BI/Tableau MCP: dashboard
- WhatsApp MCP: alert NPP

**Fallback API:**
```python
# Image-based shelf analysis
import requests
def analyze_shelf(image_path):
    with open(image_path, "rb") as f:
        r = requests.post("https://api.trax.com/v3/analyze",
            headers={"X-Api-Key": KEY}, files={"image": f}).json()
    return {"facings": r["facings_by_brand"],
            "share_of_shelf": r["share_of_shelf"],
            "oos_detected": r["oos_skus"]}
```

## Bước 7: Output Format
- **File 1**: `shelf_audit_form.md` — 15 field standard
- **File 2**: `shelf_audit_results.xlsx` — store × KPI × trend
- **File 3**: `shelf_compliance_dashboard.pptx` — exec view
- **File 4**: `action_recovery_log.xlsx` — issue × action × close-time
- **File 5**: `photo_report.html` — gallery photo before/after
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 10-15 field standard
- [ ] Geo + photo + timestamp compulsory
- [ ] Score 0-100 mỗi store
- [ ] Action close-loop SLA <48h
- [ ] Dashboard refresh weekly
- [ ] Field merchandiser training trước rollout
