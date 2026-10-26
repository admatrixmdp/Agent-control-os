---
name: ops-iso9001-readiness
description: |
  Đánh giá sẵn sàng chứng nhận ISO 9001:2015 (Quality Management System) — Gap Assessment theo 10 điều khoản chuẩn. Dùng skill này khi người dùng yêu cầu: "audit ISO 9001", "gap assessment ISO", "chuẩn bị chứng nhận ISO", "ISO 9001 readiness", "QMS audit", "kiểm tra hệ thống chất lượng", "ISO compliance check", "internal audit ISO". Output là Excel gap analysis + Markdown roadmap + Word audit report.
---

# ISO 9001 Readiness — Đánh Giá Sẵn Sàng Chứng Nhận

## Mục Tiêu
Đo lường khoảng cách giữa thực trạng và yêu cầu ISO 9001:2015, lập kế hoạch đóng gap để chứng nhận trong 3-6 tháng — tránh fail audit lần đầu mất 50-100M VND.

## Khi Nào Dùng
- Khách hàng (đặc biệt nước ngoài) yêu cầu ISO 9001
- Đấu thầu B2B/Chính phủ cần ISO
- Nâng cấp QMS hiện tại
- Tái chứng nhận sau 3 năm
- Audit nội bộ (internal audit) định kỳ

## Bước 1: Hiểu 10 Điều Khoản ISO 9001:2015
1. **Scope** (Phạm vi áp dụng)
2. **Normative References** (Tài liệu viện dẫn)
3. **Terms** (Thuật ngữ)
4. **Context of Organization** (Bối cảnh tổ chức) — SWOT, stakeholder
5. **Leadership** (Lãnh đạo) — chính sách, vai trò
6. **Planning** (Hoạch định) — rủi ro/cơ hội, mục tiêu, thay đổi
7. **Support** (Hỗ trợ) — nguồn lực, năng lực, thông tin
8. **Operation** (Vận hành) — kế hoạch, yêu cầu khách, thiết kế, mua, sản xuất
9. **Performance Evaluation** (Đánh giá) — monitoring, internal audit, MR
10. **Improvement** (Cải tiến) — non-conformity, corrective action

## Bước 2: Gap Assessment Checklist
Cho mỗi sub-clause, chấm 4 mức:
- ✅ **Conforming** (4đ): có và đầy đủ
- 🟡 **Minor gap** (3đ): có nhưng cần hoàn thiện
- 🟠 **Major gap** (2đ): có một phần
- ❌ **Not conforming** (1đ): chưa có

Ví dụ:
| Clause | Yêu cầu | Hiện trạng | Score | Gap |
|---|---|---|---|---|
| 4.1 | Hiểu bối cảnh tổ chức | Có SWOT cũ 2024 | 3 | Cập nhật 2026 |
| 5.2 | Chính sách chất lượng | Treo tường, không truyền thông | 2 | Training all staff |
| 6.1 | Risk-based thinking | Không có risk register | 1 | Tạo register |
| 7.5 | Documented info | File rải rác | 2 | Document control |
| 8.5 | Production control | SOP có nhưng cũ | 3 | Update SOP |
| 9.2 | Internal audit | Chưa từng làm | 1 | Train auditor |

Tổng: < 60% = chưa sẵn sàng | 60-80% = 3 tháng | > 80% = sẵn sàng audit

## Bước 3: Roadmap Đóng Gap
Mỗi gap có:
- Hành động cụ thể
- Owner
- Deadline
- Tài liệu cần tạo
- Training cần thực hiện
- Cost ước tính

Sắp xếp theo dependency:
- Bước 1: Document control + Quality Manual (tháng 1)
- Bước 2: SOPs cốt lõi (tháng 2)
- Bước 3: Risk register, internal audit team training (tháng 3)
- Bước 4: First internal audit + corrective actions (tháng 4)
- Bước 5: Management review (tháng 5)
- Bước 6: Stage 1 audit với CB (tháng 6)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: Lưu Quality Manual + SOPs có version control
- Notion MCP: Database tài liệu + status approve
- Google Sheets MCP: Gap tracker + dashboard %
- Slack MCP: Channel #iso9001 cho team chứng nhận
- WebSearch: So phí chứng nhận BSI/SGS/TUV/Bureau Veritas VN
- WebFetch: Tải ISO 9001:2015 standard từ iso.org

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Sync document register lên Notion
import requests
NOTION = "secret_..."
DB = "abc"
docs = [{"code":"QM-01","name":"Quality Manual","ver":"1.0","status":"Draft"},
        {"code":"SOP-WH-001","name":"Xuất kho","ver":"2.1","status":"Approved"}]
for d in docs:
    requests.post("https://api.notion.com/v1/pages",
        headers={"Authorization":f"Bearer {NOTION}",
                 "Notion-Version":"2022-06-28"},
        json={"parent":{"database_id":DB},
              "properties":{"Code":{"title":[{"text":{"content":d["code"]}}]},
                            "Status":{"select":{"name":d["status"]}}}})
```

## Bước 5: Output Format
- `ISO9001_Gap_Assessment.xlsx` — bảng chấm 10 điều khoản
- `ISO9001_Roadmap.md` — lộ trình 6 tháng có Gantt
- `ISO9001_Document_List.xlsx` — danh mục tài liệu cần tạo
- `Internal_Audit_Report.docx` — báo cáo audit nội bộ chuẩn
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/ISO9001/`

## Checklist Trước Khi Giao
- [ ] Đã chấm gap cho cả 10 điều khoản, không bỏ
- [ ] Mỗi gap có owner + due date cụ thể
- [ ] Document tier 1 (Manual), tier 2 (SOP), tier 3 (Form) đầy đủ
- [ ] Có lịch internal audit trước stage 1
- [ ] Có Management Review chuẩn agenda
- [ ] Báo giá chứng nhận từ 2-3 CB
