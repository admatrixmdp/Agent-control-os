---
name: ceo-weekly-review
description: |
  Tổng kết tuần cấp công ty cho CEO — gộp KPI từ Sales/Marketing/Vận hành/Tài chính/Nhân sự từ Google Sheets, CRM, HRIS thành 1 báo cáo điều hành 1 trang + biểu đồ trend.
  Kích hoạt khi người dùng nói: "tổng kết tuần CEO", "weekly review", "báo cáo tuần lãnh đạo", "wrap-up tuần", "review tuần đa phòng ban", "tổng hợp KPI tuần", "báo cáo cho sếp tổng tuần này", "weekly business review".
  Output là HTML dashboard + PDF gửi email tối Chủ Nhật.
---

# CEO Weekly Review — Tổng Kết Tuần Đa Phòng Ban

## Mục Tiêu
Cuối tuần CEO không phải gọi từng GĐ phòng ban để xin số. Tự động lôi dữ liệu từ Sheets/CRM/HRIS, so sánh với tuần trước + plan, đánh dấu phòng nào on/off-track, viết 3 insight chiến lược.

## Khi Nào Dùng
- Tối Chủ Nhật chuẩn bị họp Mon morning
- Sau khi đóng tuần kinh doanh
- CEO đi công tác cần review từ xa
- Trước buổi monthly business review (gộp 4 tuần)

## Bước 1: Định Nghĩa Bộ KPI Chuẩn
Mỗi phòng ban có 3-5 KPI cốt lõi:
- **Sales**: Doanh thu, số deal won, pipeline, CAC
- **Marketing**: MQL, CPL, traffic, conversion
- **Vận hành**: On-time delivery, defect rate, NPS
- **Tài chính**: Cash position, burn rate, AR ngày
- **Nhân sự**: Headcount, turnover, hire vs plan

Hỏi CEO confirm bộ KPI 1 lần, sau đó cố định trong template.

## Bước 2: Pull Số Tự Động
- Lấy số tuần hiện tại (Mon-Sun)
- Lấy số tuần trước để so sánh WoW
- Lấy plan/target tuần để so sánh actual vs plan
- Tính % chênh lệch + flag màu (xanh ≥100%, vàng 80-99%, đỏ <80%)

## Bước 3: Viết 3 Insight Chiến Lược
Không chỉ liệt kê số. Phải có:
- **What happened**: chuyện gì đáng chú ý nhất tuần
- **So what**: ý nghĩa với công ty
- **Now what**: CEO cần làm gì tuần tới
Mỗi insight 2-3 câu, tổng 3 insight = 150 từ.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: `search_files` tìm file weekly report mới nhất
- Google Sheets (qua Drive MCP): đọc tab KPI tổng hợp
- Gmail MCP: lấy email báo cáo tuần từ các GĐ phòng ban (label "weekly-report")
- Slack MCP: lấy update từ kênh #leadership-weekly
- Notion MCP: nếu công ty dùng Notion làm OS thì pull từ database KPI

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Google Sheets API: đọc range KPI
from googleapiclient.discovery import build
sheets = build('sheets', 'v4', credentials=creds).spreadsheets()
result = sheets.values().get(
    spreadsheetId='SHEET_ID',
    range='KPI_Dashboard!A1:H50'
).execute()
rows = result.get('values', [])
# Parse thành dict {department: {kpi: value}}
```

## Bước 5: Output Format
- HTML dashboard 1 trang với:
  - Header tuần + 5 KPI lớn (cards)
  - Bảng phòng ban × KPI có màu
  - 3 box insight
  - Biểu đồ trend 8 tuần (Chart.js)
- Export PDF qua `weasyprint` hoặc Chrome headless
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/weekly-W##-YYYY.pdf`
- Gửi qua Gmail draft cho CEO + cc lãnh đạo phòng ban

## Checklist Trước Khi Giao
- [ ] Đủ 5 phòng ban có số
- [ ] So sánh đủ 3 mốc: actual / WoW / vs plan
- [ ] 3 insight ngắn gọn không trùng nhau
- [ ] Có biểu đồ trend 8 tuần
- [ ] PDF dưới 2 MB
- [ ] Ghi rõ "tuần này = từ DD/MM đến DD/MM"
