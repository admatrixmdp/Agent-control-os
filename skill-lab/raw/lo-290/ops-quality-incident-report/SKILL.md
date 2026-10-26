---
name: ops-quality-incident-report
description: |
  Báo cáo sự cố chất lượng + phương pháp 8D (Eight Disciplines) — chuẩn cho Ford/GM/Tier-1, khách hàng nước ngoài yêu cầu hồi đáp khiếu nại. Dùng skill này khi người dùng yêu cầu: "báo cáo sự cố chất lượng", "8D report", "Eight Disciplines", "Quality Incident Report", "QIR", "CAPA", "Corrective and Preventive Action", "trả lời customer complaint". Output là Word 8D report + Excel CAPA tracker.
---

# Quality Incident Report + 8D

## Mục Tiêu
Phản hồi chuyên nghiệp với khiếu nại khách hàng/audit theo chuẩn 8D, đảm bảo không tái diễn — bắt buộc với automotive, electronics, B2B nước ngoài.

## Khi Nào Dùng
- Khách trả hàng/khiếu nại lô lớn
- Recall sản phẩm
- Audit khách hàng phát hiện NCR (Non-conformity Report)
- Yêu cầu CAPA từ FDA, MHRA, NAFIQAD
- Nội bộ: sự cố chất lượng nghiêm trọng

## Bước 1: 8 Bước Của 8D
**D0: Plan** — Lên kế hoạch xử lý ngay (đội phản ứng nhanh)

**D1: Team** — Thành lập đội (5-7 người multidisciplinary):
- Champion (QA Manager)
- Subject matter experts
- Operator

**D2: Problem Description** — Mô tả vấn đề theo 5W2H:
- What (hiện tượng cụ thể)
- Where (sản phẩm, lô, line, khách)
- When (thời điểm phát hiện)
- Who (ai phát hiện)
- Why (vì sao trở thành vấn đề)
- How many (số lượng ảnh hưởng)
- How (cách phát hiện)

**D3: Containment Action** — Hành động ngăn chặn lan rộng:
- Tách hàng lỗi, hold inventory
- Sort 100% lô nghi ngờ
- Thông báo khách hàng + cung cấp hàng thay
- Khắc phục tạm để vận hành tiếp

**D4: Root Cause** — Tìm nguyên nhân gốc (5 Why + Fishbone):
- Root cause of **OCCURRENCE** (vì sao lỗi xảy ra)
- Root cause of **NON-DETECTION** (vì sao QC không phát hiện)
- Root cause of **SYSTEM** (vì sao hệ thống cho phép)

**D5: Permanent Corrective Action** — Hành động khắc phục lâu dài:
- Đối với occurrence
- Đối với non-detection
- Verify hiệu quả qua trial

**D6: Implement** — Triển khai + verify:
- Update SOP, control plan, FMEA
- Train operator
- Đo lường hiệu quả sau 30/60/90 ngày

**D7: Prevent Recurrence** — Phòng ngừa tái diễn rộng hơn:
- Áp dụng lesson learned cho sản phẩm tương tự
- Update FMEA toàn dòng
- Chia sẻ knowledge management

**D8: Recognize Team** — Ghi nhận đội (cảm ơn, học hỏi)

## Bước 2: Format Báo Cáo Chuẩn
File Word có cấu trúc:
- Cover: customer, supplier, complaint #, date
- Each D có 1 mục với hình ảnh, data, evidence
- Action plan có owner + due + status
- Verification result
- Customer sign-off section

## Bước 3: CAPA Tracker
Excel sheet quản lý nhiều 8D song song:
| 8D # | Customer | Issue | D-stage | Owner | Due | Status |
|---|---|---|---|---|---|---|
| 8D-001 | Honda | Lệch màu | D5 | QA-Nam | 30/6 | On track |
| 8D-002 | Cargill | NG kim loại | D7 | QA-Lan | 15/7 | Closed |

Báo cáo cho khách hàng theo timeline:
- D3 trong 24h (containment)
- D4 trong 1 tuần (root cause)
- D5-D8 trong 30 ngày (full report)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: Lưu evidence (ảnh, video, COA)
- Google Sheets MCP: CAPA tracker chia sẻ team QA
- Gmail MCP: Gửi 8D report cho khách hàng
- Slack MCP: Channel #quality-incident
- Atlassian MCP: Tạo Jira ticket cho mỗi action
- WebSearch: Template 8D mới nhất AIAG
- WebFetch: Tải FMEA template từ aiag.org

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Generate 8D Word report tự động
from docx import Document
doc = Document()
doc.add_heading("8D Report — Customer Complaint #2026-001",0)
sections = ["D0 Plan","D1 Team","D2 Problem","D3 Containment",
            "D4 Root Cause","D5 Corrective","D6 Implement",
            "D7 Prevent","D8 Recognize"]
for s in sections:
    doc.add_heading(s, level=1)
    doc.add_paragraph("___ (Fill in) ___")
    if "Action" in s or "Implement" in s:
        t = doc.add_table(rows=1, cols=4)
        for i,h in enumerate(["Action","Owner","Due","Status"]):
            t.rows[0].cells[i].text = h
doc.save("8D_2026_001.docx")
```

## Bước 5: Output Format
- `8D_<customer>_<id>.docx` — Word report chuẩn
- `CAPA_Tracker.xlsx` — danh sách 8D đang mở
- `Quality_Incident_Log.xlsx` — log mọi sự cố (kể cả không 8D)
- `Evidence_<id>/` — folder ảnh, COA, lab test
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/8D/`

## Checklist Trước Khi Giao
- [ ] Đủ 8 D, không skip D7 (prevention)
- [ ] Containment trong 24h
- [ ] Root cause đào 2 chiều: occurrence + non-detection
- [ ] Action có verification kết quả
- [ ] Update FMEA + Control Plan + SOP
- [ ] Khách hàng sign-off chính thức
