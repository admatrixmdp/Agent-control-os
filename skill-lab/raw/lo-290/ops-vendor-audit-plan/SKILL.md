---
name: ops-vendor-audit-plan
description: |
  Lập kế hoạch audit nhà cung cấp tại nhà máy (Supplier On-site Audit) — checklist ISO 9001 + chuyên ngành, ranking risk, lịch audit hàng năm. Dùng skill này khi người dùng yêu cầu: "audit nhà cung cấp", "supplier audit plan", "vendor audit", "second-party audit", "kiểm tra nhà cung cấp tại chỗ", "qualification audit", "process audit NCC", "audit NCC tại nhà máy". Output là Excel audit calendar + Word audit report + checklist 100 mục.
---

# Vendor Audit Plan — Audit NCC Tại Nhà Máy

## Mục Tiêu
Đánh giá tận nơi năng lực sản xuất + hệ thống chất lượng NCC trước khi ký hợp đồng dài hạn / theo dõi định kỳ — giảm rủi ro chuỗi cung ứng 60-80%.

## Khi Nào Dùng
- Qualification NCC mới trước khi cho production
- Re-audit NCC chiến lược 1-2 năm/lần
- Sau khi NCC có sự cố nghiêm trọng (CAPA)
- Trước khi nhận đơn hàng lớn từ khách
- Yêu cầu của khách hàng cuối (Tier-1 audit Tier-2)

## Bước 1: Phân Loại NCC Theo Risk → Tần Suất Audit
| Risk | Tiêu chí | Tần suất audit |
|---|---|---|
| **A (High)** | NVL critical, single source, > 50% volume | 1 năm/lần on-site |
| **B (Med)** | NVL có backup, 10-50% volume | 2 năm/lần on-site |
| **C (Low)** | NVL non-critical, dễ thay | Self-assessment 1 năm/lần |
| **New** | NCC mới | Qualification audit trước first PO |

Lập lịch audit năm: phân bổ NCC theo tháng (max 2 NCC/tháng tránh quá tải).

## Bước 2: Checklist Audit 100 Mục (8 Mảng)
**1. Documentation (10 mục)**:
- ISO 9001/14001/45001 certificate còn hiệu lực
- Quality Manual, SOPs, Work Instructions
- Records retention 3+ năm

**2. Process Control (15 mục)**:
- Control plan từng công đoạn
- SPC, capability Cpk > 1.33
- Setup procedure + first article

**3. Quality (15 mục)**:
- IQC/IPQC/OQC system
- Calibration dụng cụ đo
- Non-conformity handling

**4. Production (10 mục)**:
- Layout 5S
- Machine maintenance log
- Production planning

**5. Material (10 mục)**:
- Incoming inspection
- FIFO/FEFO storage
- Traceability

**6. People (10 mục)**:
- Skill matrix
- Training records
- PPE, safety

**7. Environment (10 mục)**:
- Temperature/humidity control
- Pest control
- ESH compliance

**8. Sub-supplier (10 mục)**:
- Sub-supplier list
- Sub audit?
- Quality flow-down

**9. Specific** (10 mục theo ngành: HACCP F&B, IATF automotive, GMP pharma)

## Bước 3: Conduct Audit + Scoring
Audit 1-2 ngày tại nhà máy NCC:
- Opening meeting (introduce, scope)
- Plant tour
- Document review
- Interview operator, manager
- Closing meeting (preliminary findings)

Mỗi mục chấm:
- 4đ: Fully conform
- 3đ: Minor finding
- 2đ: Major finding
- 1đ: Critical finding (stop business)
- 0đ: Not applicable

Tổng điểm + grade:
- A (90-100%): Approved
- B (75-89%): Approved with conditions
- C (60-74%): Conditional, re-audit 3 tháng
- D (<60%): Disapproved

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Calendar MCP: Schedule audit + invite cả 2 bên
- Google Drive MCP: Lưu audit report, evidence photos
- Google Sheets MCP: Audit calendar năm + result tracker
- Notion MCP: NCC database với audit history
- Gmail MCP: Gửi pre-audit questionnaire + post-audit report
- Slack MCP: Notify Sourcing về NCC fail
- WebSearch: Tra cập nhật chuẩn IATF, AS9100, FSSC mới nhất

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tự động sinh pre-audit questionnaire gửi NCC qua Gmail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()
msg["Subject"] = "Pre-Audit Questionnaire — Vui lòng hoàn thành trước 7/6"
msg["To"] = "qa@ncc.com.vn"
msg.attach(MIMEBase("application","octet-stream"))
with open("Pre_Audit_Q.xlsx","rb") as f:
    part = MIMEBase("application","octet-stream")
    part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition","attachment; filename=Pre_Audit_Q.xlsx")
    msg.attach(part)
# Gửi
```

## Bước 5: Output Format
- `Audit_Calendar_2026.xlsx` — lịch audit cả năm
- `Audit_Checklist_100items.xlsx` — 100 mục có cột chấm
- `Audit_Report_<NCC>_<date>.docx` — báo cáo chính thức
- `CAR_<NCC>.xlsx` — Corrective Action Request tracking
- `Audit_Photos/` — evidence theo NCC
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/VendorAudit/`

## Checklist Trước Khi Giao
- [ ] Pre-audit questionnaire gửi NCC 2 tuần trước
- [ ] Có lead auditor được training
- [ ] Audit 1-2 ngày on-site, không qua loa
- [ ] Closing meeting có biên bản
- [ ] CAR có due date + verification
- [ ] Update NCC database (grade, expiry)
