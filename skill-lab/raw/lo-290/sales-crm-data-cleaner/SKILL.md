---
name: sales-crm-data-cleaner
description: |
  Làm sạch dữ liệu CRM — dedup contact/account, format phone/email, chuẩn hoá field. Trigger phrases: "làm sạch CRM", "CRM data cleaning", "dedup contact CRM", "fix format CRM", "chuẩn hoá data CRM", "data hygiene Salesforce", "clean HubSpot data", "dedup khách hàng", "sửa lỗi data CRM", "CRM data quality". Output là Excel cleanup report + Python script + SOP.
---

# CRM Data Cleaner

## Mục Tiêu
Tăng CRM data quality score lên >90% bằng dedup + format + missing field auto-fill — giảm AE wasted time (15-20% productivity lost do data bẩn).

## Khi Nào Dùng
- Quarterly cleanup
- Sau import list lớn
- Trước implement BI dashboard
- Migration CRM (Hub→SF)
- Data accuracy <70%

## Bước 1: Audit Quality Score
Đo 5 metric:
- **Completeness**: % field bắt buộc filled
- **Validity**: email/phone format đúng
- **Uniqueness**: % không duplicate
- **Consistency**: company name pattern (Inc. vs Inc vs INC)
- **Timeliness**: last update <90 ngày

Tổng score 0-100.

## Bước 2: Dedup Rule

**Contact dedup**:
- Match: email exact
- Match: first+last+company fuzzy >85%
- Match: phone normalized

**Account dedup**:
- Match: website domain
- Match: name fuzzy >85%
- Match: address/postal

Merge rule: giữ record có nhiều activity nhất, append data field còn lại.

## Bước 3: Format Standardization
- Phone: E.164 format (+84-...)
- Email: lowercase
- Company name: strip suffix "Co., Ltd", "Inc.", capital first
- Address: chuẩn hoá tỉnh/thành theo OpenStreetMap
- Industry: chuẩn ISIC code

## Bước 4: Missing Field Auto-fill
- Industry: enrich qua Apollo/Clearbit
- Company size: enrich
- Phone: NeverBounce verify + lookup
- LinkedIn URL: scrape
- Geo: lookup từ address

Báo cáo % auto-fill vs cần thủ công.

## Bước 5: Validation Rules đặt vào CRM
Sau cleanup, set rule prevent:
- Email format invalid → block save
- Phone không E.164 → warn
- Required field missing → block
- Duplicate detection real-time

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce/HubSpot MCP: query + bulk update
- Apollo/Clearbit MCP: enrich missing data
- NeverBounce MCP: email validate
- Slack MCP: report cleanup result

**Fallback API:**
```python
# Salesforce dedup + format
import pandas as pd
contacts = pd.DataFrame(sf.query_all("SELECT Id, Email, Phone, FirstName, LastName, AccountId FROM Contact")["records"])
contacts["Email"] = contacts["Email"].str.lower()
contacts["Phone"] = contacts["Phone"].apply(normalize_e164)

# Find duplicates
dups = contacts[contacts.duplicated(subset=["Email"], keep=False)]
# Merge logic: keep most recent activity
for email, group in dups.groupby("Email"):
    keep_id = group.sort_values("LastActivityDate").iloc[-1]["Id"]
    delete_ids = group[group["Id"] != keep_id]["Id"].tolist()
    for d in delete_ids:
        sf.Contact.delete(d)
```

## Bước 7: Output Format
- **File 1**: `crm_audit_<date>.xlsx` — 5 metric score + breakdown
- **File 2**: `dedup_log.xlsx` — record merged + lost data alert
- **File 3**: `cleanup_script.py` — reusable script
- **File 4**: `crm_validation_rules.md` — rule add vào CRM admin
- **File 5**: `cleanup_SOP.md` — quarterly process
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Backup CRM trước cleanup
- [ ] Dedup rule test trên sandbox
- [ ] Merge logic giữ activity history
- [ ] Validation rule prevent regression
- [ ] Score before/after report
- [ ] Quarterly cleanup cadence
