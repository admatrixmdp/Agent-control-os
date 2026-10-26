---
name: ops-maintenance-schedule
description: |
  Lập lịch bảo trì preventive (PM) cho máy móc theo tần suất giờ chạy/lịch — tránh dừng máy đột xuất, kéo dài tuổi thọ thiết bị. Dùng skill này khi người dùng yêu cầu: "lịch bảo trì máy", "preventive maintenance", "PM schedule", "bảo trì định kỳ", "TPM plan", "maintenance calendar", "lịch bảo dưỡng thiết bị", "MTBF MTTR". Output là Excel calendar + Google Calendar sync + checklist từng PM.
---

# Maintenance Schedule — Lịch Bảo Trì Preventive

## Mục Tiêu
Chuyển từ "hỏng đâu sửa đó" (reactive) sang bảo trì có kế hoạch — giảm downtime đột xuất 40-70%, tăng MTBF (Mean Time Between Failures).

## Khi Nào Dùng
- Máy móc mới đầu năm, lập plan cả năm
- Sau khi có sự cố lớn cần lập preventive
- Triển khai TPM/RCM
- Audit ISO 55001 (Asset management)
- Khi MTBF < 100h và bạn không biết tại sao

## Bước 1: Inventory Máy Móc
Lập danh sách asset, mỗi máy có:
- Mã máy (VD: CNC-01, BOIL-02)
- Tên/Model/Hãng
- Ngày mua, tuổi máy
- Khu vực, ca làm việc
- Người vận hành chính
- Tài liệu nhà SX (manual, PM matrix)
- Critical level (A: dừng = stop line, B: backup được, C: ít ảnh hưởng)

## Bước 2: Phân Loại PM Theo Tần Suất
4 loại PM chuẩn:
| Loại | Tần suất | Ai làm | Ví dụ |
|---|---|---|---|
| **Daily** | Đầu/cuối ca | Operator | Vệ sinh, check dầu, kiểm tra rò rỉ |
| **Weekly** | Thứ 7 | Tech + Op | Tra dầu, siết bulong, lau cảm biến |
| **Monthly** | Ngày 1 | Maint Tech | Thay dầu, lọc, kiểm tra rung |
| **Yearly** | Tháng 12 | Maint + NCC | Overhaul, hiệu chuẩn, sơn |

Theo giờ chạy:
- 500h: lọc dầu
- 2000h: thay dầu thủy lực
- 5000h: thay vòng bi
- 10000h: đại tu

## Bước 3: Tạo Lịch + Gắn Người
Excel calendar với:
- Cột: ngày trong tháng
- Hàng: máy
- Cell: mã PM (D/W/M/Y) + tên người thực hiện
- Color code: chưa làm (xám), đang làm (vàng), xong (xanh), trễ (đỏ)

Quy tắc:
- PM không trùng vào ngày peak production
- 2 máy critical cùng loại không bảo trì cùng ngày
- Cuối tuần ưu tiên overhaul lâu

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Calendar MCP: Tạo event PM cho từng máy + invite tech
- Google Sheets MCP: Master schedule + log PM đã làm
- Slack MCP: Bot nhắc PM trước 1 ngày
- Notion MCP: Database asset + lịch sử PM mỗi máy
- WebSearch: Tra catalog phụ tùng để mua trước PM
- WebFetch: Tải PM matrix từ trang nhà SX máy

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Push lịch PM lên Google Calendar
from googleapiclient.discovery import build
from google.oauth2 import service_account
creds = service_account.Credentials.from_service_account_file("creds.json")
svc = build("calendar","v3",credentials=creds)
for pm in pm_list:
    event = {"summary": f"PM {pm['machine']} - {pm['type']}",
             "start": {"dateTime": pm["start"]},
             "end": {"dateTime": pm["end"]},
             "attendees": [{"email": pm["tech_email"]}],
             "description": pm["checklist_url"]}
    svc.events().insert(calendarId="maintenance@co.vn",
        body=event, sendUpdates="all").execute()
```

## Bước 5: Output Format
- `PM_Master_Schedule_2026.xlsx` — calendar cả năm
- `PM_Checklist_<máy>.pdf` — checklist từng loại PM
- `PM_Dashboard.html` — % PM hoàn thành theo tháng, MTBF/MTTR
- `Spare_Parts_Order.xlsx` — danh mục phụ tùng cần đặt trước PM
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/Maintenance/`

## Checklist Trước Khi Giao
- [ ] Mỗi máy critical có PM ít nhất hàng tháng
- [ ] PM checklist có chi tiết bước + thông số đo
- [ ] Có sub phụ tùng dự phòng (min stock)
- [ ] Lịch không xung đột với plan sản xuất
- [ ] Có trường log: ai làm, thời gian thực, kết quả
- [ ] MTBF/MTTR được tính từ log
