---
name: ceo-financial-snapshot
description: |
  Snapshot tài chính 1 trang cho CEO — pull số từ Google Sheets/Excel kế toán, tính nhanh doanh thu, profit, cash, AR/AP, burn rate, runway. Format đọc trong 60 giây.
  Kích hoạt khi người dùng nói: "snapshot tài chính", "financial snapshot", "tình hình tài chính nhanh", "tóm tắt P&L", "số tài chính hôm nay", "tài chính 1 trang", "quick financial review", "tài chính CEO".
  Output là HTML/PDF 1 trang.
---

# CEO Financial Snapshot — Snapshot Tài Chính 1 Trang

## Mục Tiêu
CEO không phải kế toán — không có thời gian đọc 15 trang BCTC. 1 trang snapshot trả lời 5 câu hỏi: tiền còn không, lời lỗ tháng này, runway, ai nợ ai, có alert gì không.

## Khi Nào Dùng
- Hàng tuần (sáng thứ Hai)
- Trước họp với CFO
- Khi nghi ngờ có vấn đề tiền
- Trước quyết định chi lớn
- Trước họp board

## Bước 1: Pull 10 Chỉ Số Cốt Lõi
1. Cash balance (tổng tài khoản)
2. Doanh thu MTD (month-to-date)
3. Doanh thu vs target tháng %
4. Gross profit %
5. OpEx MTD
6. Net burn / profit MTD
7. AR (khách hàng nợ)
8. AP (mình nợ NCC)
9. AR aging > 60 ngày (rủi ro thu hồi)
10. Runway (tháng còn lại nếu burn)

## Bước 2: So Sánh 3 Mốc
Mỗi chỉ số có 3 cột so sánh:
- This month MTD
- Same period last month
- vs Plan (đầu năm/quý)

% chênh lệch + flag màu.

## Bước 3: Alert Tự Động
- Cash < 3 tháng runway → ĐỎ
- AR aging > 60 ngày > 10% AR → CAM
- OpEx vượt plan > 15% → CAM
- Gross margin giảm > 5% MoM → ĐỎ
- Doanh thu < 80% target → CAM

Mỗi alert có recommended action 1 dòng.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: pull file kế toán Excel/Sheets
- Google Sheets MCP: đọc trực tiếp range
- Gmail MCP: gửi snapshot email tự động hàng tuần
- Slack MCP: post lên #leadership-finance
- Notion MCP: lưu history snapshot để track trend

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Pull Sheets + tính
from googleapiclient.discovery import build
sheets = build('sheets', 'v4', credentials=creds).spreadsheets()
data = sheets.values().get(spreadsheetId=SID, range='P&L!A1:N50').execute()['values']
# Parse
revenue_mtd = sum(float(r[3]) for r in data[1:] if r[2] == 'Revenue')
opex_mtd = sum(float(r[3]) for r in data[1:] if r[2].startswith('OpEx'))
burn = opex_mtd - revenue_mtd * margin
runway = cash / burn
```

## Bước 5: Output Format
- HTML 1 trang:
  - Top: 5 số lớn (Cash, Revenue, Profit, Runway, Alert count)
  - Giữa: bảng 10 chỉ số có 3 cột so sánh
  - Dưới: alert box + recommended action
- PDF print-ready
- Slack version 200 từ
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/snapshot-YYYY-MM-DD.pdf`

## Checklist Trước Khi Giao
- [ ] 10 chỉ số đầy đủ
- [ ] 3 cột so sánh rõ
- [ ] Alert đỏ/cam có action
- [ ] Tổng trên 1 trang A4
- [ ] Đã verify số với kế toán
- [ ] Timestamp + nguồn dữ liệu
