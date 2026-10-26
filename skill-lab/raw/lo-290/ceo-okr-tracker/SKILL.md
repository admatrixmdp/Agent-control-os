---
name: ceo-okr-tracker
description: |
  Theo dõi OKR cấp công ty và phòng ban theo quý — pull dữ liệu key results từ Sheets/Notion, tính %, đánh dấu OKR off-track (đỏ/vàng/xanh), gợi ý hành động cứu OKR có nguy cơ trượt.
  Kích hoạt khi người dùng nói: "tracker OKR", "theo dõi OKR quý", "OKR đang ở đâu", "review OKR công ty", "cập nhật OKR", "OKR check-in", "báo cáo OKR cho CEO", "OKR dashboard", "OKR off-track".
  Output là HTML dashboard + bảng Excel.
---

# CEO OKR Tracker — Theo Dõi OKR Quý

## Mục Tiêu
CEO không phải gọi từng phòng ban hỏi "OKR tới đâu". Hệ thống tự động pull, tính %, cảnh báo OKR nào sắp trượt và gợi ý hành động cứu trước khi quá muộn.

## Khi Nào Dùng
- Check-in OKR 2 tuần/lần
- Cuối tháng review OKR quý
- Trước họp leadership team
- Khi CEO nghi ngờ 1 phòng đang lệch hướng
- Đầu quý mới để chốt OKR cũ

## Bước 1: Đọc Cấu Trúc OKR
Nguồn chuẩn (chọn 1):
- Google Sheet template OKR (Objective → 3-5 KR → owner → target → current)
- Notion database OKR
- Excel local

Mỗi KR phải có: tên, target số, current số, owner, deadline.

## Bước 2: Tính Toán Trạng Thái
- **% completion** = current/target
- **% time elapsed** = (ngày đã qua / tổng ngày quý) × 100
- **Health**:
  - Xanh: % completion ≥ % time elapsed
  - Vàng: chậm 10-25%
  - Đỏ: chậm > 25% hoặc chưa start

Tính cả OKR level công ty + level từng phòng ban.

## Bước 3: Insight + Hành Động Cứu
Với mỗi OKR đỏ:
- Lý do trượt (1 câu)
- Đề xuất 2-3 hành động cứu (ai làm, làm gì, deadline)
- Hỏi: cần CEO can thiệp không?

Với OKR xanh: ghi nhận, không spam CEO.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: tìm file "OKR Q[N] [năm]"
- Google Sheets (qua Drive): pull range OKR
- Notion MCP: query database OKR theo filter Quarter
- Slack MCP: post tóm tắt lên #okr-checkin
- Linear MCP: cross-check OKR với epic Linear nếu công ty dùng

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Notion API: query database OKR
import requests
r = requests.post(
    f"https://api.notion.com/v1/databases/{db_id}/query",
    headers={"Authorization": f"Bearer {token}", "Notion-Version": "2022-06-28"},
    json={"filter": {"property": "Quarter", "select": {"equals": "Q2 2026"}}}
)
okrs = r.json()['results']
```

## Bước 5: Output Format
- HTML dashboard với:
  - Header: % completion tổng công ty
  - Bảng OKR công ty (3-5 Objectives, mỗi cái có KR con)
  - Phần riêng cho từng phòng ban
  - Trend line 12 tuần
- Excel file `okr-tracker-Q#-YYYY.xlsx` 2 sheet: Summary + Detail
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Tất cả OKR có owner rõ ràng
- [ ] Color code đúng quy ước
- [ ] OKR đỏ đều có hành động cứu
- [ ] Có so sánh % completion vs % time elapsed
- [ ] Tổng số OKR công ty ≤ 5 objective
- [ ] Ghi rõ ngày check-in
