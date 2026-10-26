---
name: fin-internal-control-soc1
description: |
  Soạn hệ thống Kiểm Soát Nội Bộ ICFR (Internal Control over Financial Reporting) chuẩn SOX/SOC1
  cho doanh nghiệp - matrix rủi ro, kiểm soát chính, quy trình test. Trigger phrases:
  "kiểm soát nội bộ", "ICFR", "SOX compliance", "SOC1 report", "risk control matrix",
  "internal audit", "kiểm soát tài chính", "control framework", "COSO", "RCM matrix".
  Output là PDF ICFR documentation + Excel RCM.
---

# Soạn ICFR / Internal Control Framework (SOX-style)

## Mục Tiêu
Xây hệ thống kiểm soát nội bộ chuyên nghiệp cho SME chuẩn bị niêm yết, gọi vốn PE/VC,
hoặc đơn giản là tự bảo vệ trước gian lận. Dựa trên COSO framework + SOX 404 áp xuống
quy mô vừa - phù hợp doanh nghiệp 200-2000 NV.

## Khi Nào Dùng
- DN chuẩn bị IPO (cần ICFR audit)
- DN nhận vốn PE/VC yêu cầu compliance
- Sau khi có vụ gian lận / mất tiền lớn
- Khi mở rộng nhiều chi nhánh, khó kiểm soát tập trung
- Định kỳ năm 2 năm review/refresh

## Bước 1: COSO Framework 5 Components
1. **Control Environment**: tone-at-the-top, code of conduct, HR policies
2. **Risk Assessment**: identify, analyse, respond to risks
3. **Control Activities**: policies + procedures (3-way match, segregation of duties, authorization)
4. **Information & Communication**: cách truyền thông, reporting
5. **Monitoring**: internal audit, management review, exceptions handling

## Bước 2: Build Risk-Control Matrix (RCM)
Cho mỗi quy trình tài chính, list:

**Process: Procure-to-Pay (P2P):**
| Risk | Inherent Rating | Key Control | Control Type | Frequency | Owner |
|------|-----------------|-------------|--------------|-----------|-------|
| Mua hàng không cần thiết | High | PR approval matrix | Preventive | Per transaction | Procurement Mgr |
| Trả tiền sai NCC | High | 3-way match PO-GR-Invoice | Preventive | Per invoice | AP Accountant |
| Trả 2 lần cùng hoá đơn | Medium | Auto-block duplicate by ERP | Preventive | Per invoice | System |
| NCC khống (ghost vendor) | High | Vendor approval, MST verify | Preventive | Per new vendor | KTT |

**Process: Order-to-Cash (O2C):**
| Bán hàng KH không tín dụng | High | Credit check before order | Preventive | Per order | Credit ctrl |
| Ghi nhận DT sớm (cooking books) | High | Revenue recognition checklist | Detective | Monthly | KTT |

**Process: Record-to-Report (R2R):**
| Bút toán điều chỉnh không hợp lý | High | JE review + approval | Preventive | Per JE >X amount | CFO |
| BCTC sai do mapping | Medium | Trial balance to BCTC tie-out | Detective | Monthly | CFO |

## Bước 3: Test of Design + Test of Operating Effectiveness
**Test of Design (TOD):**
- Đọc policy
- Walkthrough 1 transaction từ đầu đến cuối
- Conclude: control thiết kế có đủ mitigate risk không?

**Test of Operating Effectiveness (TOE):**
- Sample size theo frequency:
  - Daily control: 25 samples
  - Weekly: 15
  - Monthly: 5
  - Quarterly: 2
- Re-perform / inspect documentation
- Document exception (nếu có) + management response

**Conclusion:**
- Effective: control hoạt động đúng
- Deficient: lỗ hổng, cần remediate
- Material weakness: nghiêm trọng, có thể ảnh hưởng BCTC

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: Lưu RCM, walkthroughs, test working papers
- Google Sheets MCP: Test result tracker, deficiency log
- Gmail MCP: Gửi process owner notification về deficiency + remediation deadline
- WebSearch: Tra COSO 2013 framework, SOX 404 guidance, IIA standards

**Fallback bằng API:**
```python
# Auto-test segregation of duties bằng cách query ERP log
import requests
import pandas as pd

# Pull log từ ERP - ai làm gì trên hệ thống
r = requests.get(
    "https://api.misa.vn/sme/v1/audit-log",
    params={"period": "2026-05"},
    headers={"Authorization": f"Bearer {TOKEN}"}
)
log = pd.DataFrame(r.json()["log"])

# Test: Cùng 1 user vừa tạo PO vừa duyệt PO?
po_creators = log[log["action"]=="CREATE_PO"][["user", "po_id"]]
po_approvers = log[log["action"]=="APPROVE_PO"][["user", "po_id"]]
violations = po_creators.merge(po_approvers, on=["user", "po_id"])
if len(violations) > 0:
    print(f"SoD VIOLATION: {len(violations)} POs created+approved by same user!")
    print(violations)
```

## Bước 5: Output Format
1. **PDF ICFR documentation** (`ICFR_documentation_v1.pdf`): 50-80 trang - COSO overview, process narratives, RCM, test plan.
2. **Excel RCM master** (`RCM_2026.xlsx`): Sheet "P2P", "O2C", "R2R", "Payroll", "Treasury", "ITGC" - 200-500 controls.
3. **HTML control dashboard** (`control_dashboard.html`): Heat map risk×control, % controls tested, list deficiency open.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/icfr/`

## Checklist Trước Khi Giao
- [ ] Mỗi key risk có ≥ 1 mitigating control
- [ ] Segregation of duties đã test: ai tạo ≠ ai duyệt ≠ ai ghi sổ
- [ ] Có ITGC (IT general controls) cho ERP/email/server
- [ ] Test sample size đúng theo frequency
- [ ] Deficiency có remediation plan + owner + deadline
- [ ] Management certification ký bởi CEO + CFO
