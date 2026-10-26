---
name: legal-compliance-checklist
description: |
  Tạo checklist tuân thủ pháp luật định kỳ cho doanh nghiệp Việt Nam — lao động (BLLĐ), thuế (Luật QLT), an toàn thông tin (NĐ 13/2023), môi trường, PCCC, an toàn thực phẩm, BHXH. Kích hoạt khi người dùng nói: "checklist compliance", "tự rà soát pháp lý", "checklist tuân thủ", "audit nội bộ doanh nghiệp", "compliance định kỳ", "checklist BLĐ thuế ATTT", "compliance calendar", "rà soát hồ sơ pháp lý", "checklist legal", "compliance review VN". Output là Excel checklist + dashboard PDF + Calendar nhắc deadline.
---

# Checklist Compliance Định Kỳ Cho DN Việt Nam

## Mục Tiêu
Giúp doanh nghiệp tự rà soát compliance theo lịch tháng/quý/năm — tránh phạt vì sót kê khai thuế (NĐ 125/2020 phạt 8-25M/lần), trễ báo cáo lao động (NĐ 12/2022 phạt 5-75M), sai NĐ 13/2023 dữ liệu cá nhân (2-5% doanh thu).

## Khi Nào Dùng
- Đầu năm: lập compliance calendar 12 tháng
- Cuối quý: rà BCTC + kê khai thuế
- Khi tuyển 50+ nhân viên: hồ sơ BLĐ + BHXH + nội quy
- Trước thanh tra (thuế / BLĐ / công an PCCC)
- Trước M&A / gọi vốn (DD — Due Diligence)

## Bước 1: Phân Loại Theo Lĩnh Vực (8 Nhóm)
1. **Doanh nghiệp / GPKD**: cập nhật thay đổi GPKD, báo cáo tài chính, công bố thông tin (Đ.176 LDN với CTCP đại chúng)
2. **Thuế**: GTGT (tháng/quý), TNDN (quý + năm), TNCN, môn bài, hoá đơn điện tử (TT 78/2021)
3. **Lao động**: HĐLĐ, nội quy lao động, thoả ước, báo cáo sử dụng lao động (mẫu 01 NĐ 145/2020)
4. **BHXH / BHYT / BHTN**: kê khai mỗi tháng, chốt sổ khi nghỉ
5. **An toàn thông tin**: NĐ 13/2023 — Hồ sơ TIA, đăng ký xử lý dữ liệu, báo cáo sự cố
6. **PCCC**: NĐ 136/2020 — kiểm tra định kỳ, huấn luyện, hồ sơ phương án
7. **Môi trường**: ĐTM/Cam kết BVMT, báo cáo công tác BVMT năm, quản lý chất thải nguy hại
8. **Ngành đặc thù**: ATTP (TT 43/2018), Dược (NĐ 54/2017), Fintech (TT 39/2014), TMĐT (NĐ 52/2013)

## Bước 2: Build Compliance Calendar
Tạo lịch năm với deadline cụ thể:
- 20 hàng tháng: kê khai thuế GTGT tháng (DN >50 tỷ doanh thu)
- 30/31 hàng tháng: nộp BHXH
- 30/1: kê khai môn bài năm
- 30/3: BCTC năm + quyết toán TNDN
- 30/3: quyết toán TNCN
- 31/5: báo cáo BVMT năm trước
- 30/6: báo cáo sử dụng lao động 6T đầu năm
- 31/12: báo cáo sử dụng lao động cả năm + báo cáo CTC

## Bước 3: Sinh Checklist 100+ Items
Mỗi item gồm: Lĩnh vực | Yêu cầu | Văn bản pháp lý | Tần suất | Người phụ trách | Status | Deadline | Bằng chứng | Mức phạt nếu sai

Ví dụ:
| Lĩnh vực | Yêu cầu | VB Pháp lý | Tần suất | Status |
|----|----|----|----|----|
| Thuế | Kê khai GTGT tháng | TT 80/2021 | Hàng tháng | ✅ |
| BLĐ | Cập nhật nội quy LĐ với Sở LĐTBXH (≥10 NLĐ) | BLLĐ Đ.118-119 | Khi thay đổi | ⚠️ |
| ATTT | Lưu hồ sơ TIA cho xử lý dữ liệu | NĐ 13/2023 Đ.43 | Liên tục | ❌ |
| PCCC | Diễn tập PCCC | NĐ 136/2020 | 6 tháng/lần | ✅ |

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: master checklist sống, share toàn team
- Google Calendar MCP: tự động tạo event deadline (alarm 7/3/1 ngày trước)
- Gmail MCP: gửi remind hàng tuần cho từng phòng ban phụ trách
- Notion MCP: lưu evidence (PDF kê khai thuế, BCTC, hợp đồng) theo case
- WebFetch: cập nhật văn bản mới từ `thuvienphapluat.vn`, `chinhphu.vn`, `gdt.gov.vn`
- WebSearch: tra văn bản hướng dẫn mới + dự thảo sửa đổi

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Sinh compliance calendar tự động + push lên Google Calendar
from datetime import datetime, timedelta
import json

compliance_items = [
    {"name": "Kê khai thuế GTGT tháng", "freq": "monthly", "day": 20, "responsible": "Kế toán trưởng"},
    {"name": "Nộp BHXH tháng", "freq": "monthly", "day": 30, "responsible": "HR"},
    {"name": "Quyết toán TNDN năm", "freq": "yearly", "month": 3, "day": 30, "responsible": "CFO"},
    {"name": "Báo cáo sử dụng lao động 6T", "freq": "yearly", "month": 6, "day": 30, "responsible": "HR Manager"},
    {"name": "Diễn tập PCCC", "freq": "half_year", "responsible": "Admin"},
    {"name": "Báo cáo BVMT năm", "freq": "yearly", "month": 5, "day": 31, "responsible": "Admin"},
    {"name": "Audit nội bộ NĐ 13 dữ liệu cá nhân", "freq": "yearly", "month": 12, "day": 15, "responsible": "DPO"}
]

events = []
for year in [2026, 2027]:
    for item in compliance_items:
        # tạo các date phù hợp + đẩy lên Calendar API
        events.append({"summary": item["name"], "responsible": item["responsible"], "year": year})
```

## Bước 5: Output Format
- File `compliance_checklist_<TenDN>_<Nam>.xlsx`: 8 sheet theo 8 lĩnh vực
- File `compliance_calendar_<Nam>.ics`: import vào Google Calendar
- File `compliance_dashboard.pdf`: dashboard tóm tắt cho CEO/CFO (% completion, top 5 risk)
- File `compliance_evidence/`: folder lưu chứng từ (BCTC, kê khai thuế, BCSDLD)
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/compliance/`

## Checklist Trước Khi Giao
- [ ] Đã liệt kê đủ 8 lĩnh vực + ngành đặc thù
- [ ] Mỗi item có VB pháp lý + tần suất + người phụ trách rõ ràng
- [ ] Có mức phạt nếu vi phạm (để CEO ưu tiên)
- [ ] Đã tạo Calendar event tự động với alarm trước deadline
- [ ] Có thư mục lưu evidence (BCTC, kê khai, biên bản)
- [ ] Dashboard tóm tắt % completion theo phòng ban
- [ ] Có cơ chế escalation khi sót deadline (thông báo CEO + CFO)
- [ ] Đã review nửa năm 1 lần để cập nhật văn bản pháp luật mới
