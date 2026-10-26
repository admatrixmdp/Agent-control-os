---
name: ops-kanban-board-setup
description: |
  Setup bảng Kanban quản lý công việc vận hành trên Trello/Notion/Asana/ClickUp — cấu hình column, WIP limit, label, automation, dashboard. Dùng skill này khi người dùng yêu cầu: "tạo bảng Kanban", "setup Trello board", "Notion Kanban", "Asana board", "quản lý công việc bằng Kanban", "WIP limit", "lean workflow", "task board". Output là JSON/CSV import + hướng dẫn cài đặt step-by-step.
---

# Setup Kanban Board Quản Lý Công Việc Vận Hành

## Mục Tiêu
Visual hoá luồng công việc, giới hạn WIP để tránh đa nhiệm, dùng cho ops/maintenance/QC/incident — tăng throughput 30-50% theo các case Lean.

## Khi Nào Dùng
- Team chuyển từ quản lý bằng Excel/Zalo sang công cụ chuyên dụng
- Muốn giảm task "ngâm" quá lâu trong WIP
- Cần dashboard cho sếp xem nhanh tình trạng
- Setup cho team mới (5-20 người)
- Triển khai Lean/Agile cho phòng Ops

## Bước 1: Chọn Tool Phù Hợp
| Tool | Phù hợp khi | Free tier | Mức độ phức tạp |
|---|---|---|---|
| Trello | Team nhỏ, cần đơn giản | Unlimited boards | Dễ |
| Notion | Đã dùng Notion, cần link nhiều DB | Free cá nhân | Vừa |
| Asana | Team trung, cần báo cáo | 15 người free | Vừa |
| ClickUp | Cần nhiều view (Gantt, List, Kanban) | Free đến 5 task | Khó |
| Jira | Có IT/dev, cần workflow phức tạp | 10 user free | Khó |

## Bước 2: Thiết Kế Column & WIP Limit
Workflow chuẩn cho Ops:
```
Backlog → To Do → In Progress (WIP 3) → Review/QC (WIP 2) → Done → Archived
```

Quy tắc WIP:
- WIP limit = số người trong team × 1.5
- Nếu In Progress đầy → không kéo task mới vào, focus dọn cái đang làm
- Có column "Blocked" để tách task kẹt

## Bước 3: Label, Priority, Custom Field
**Label màu** theo loại task:
- Đỏ: Sự cố/Khẩn cấp
- Cam: Bảo trì preventive
- Vàng: Cải tiến (Kaizen)
- Xanh: Routine/Daily
- Tím: Project lớn

**Custom field**:
- Owner (assignee)
- Priority (P0-P3)
- Estimate (giờ)
- Due date
- SLA breach? (formula)

**Automation rules**:
- Khi card chuyển "Done" → archive sau 7 ngày
- Khi due date < 1 ngày → đỏ + notify Slack
- Khi label "Khẩn cấp" → tự assign cho ca trưởng

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Notion MCP: Tạo database Kanban native trong Notion
- Slack MCP: Nối Kanban -> Slack channel #ops cho mỗi card mới
- Google Sheets MCP: Export Kanban -> Sheet để báo cáo BI
- Atlassian MCP: Tạo Jira board nếu dùng Jira
- WebSearch: Tra giá plan Trello/Notion mới nhất
- WebFetch: Lấy template Kanban từ trello.com/templates

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tạo board Trello + cards qua API
import requests
KEY, TOKEN = "...", "..."
# Create board
r = requests.post("https://api.trello.com/1/boards/",
    params={"key": KEY, "token": TOKEN,
            "name": "Ops Daily", "defaultLists": "false"})
board_id = r.json()["id"]
# Create lists
for name in ["Backlog","To Do","In Progress","QC","Done"]:
    requests.post("https://api.trello.com/1/lists",
        params={"key": KEY, "token": TOKEN,
                "name": name, "idBoard": board_id})
```

## Bước 5: Output Format
- `kanban_setup_guide.md` — hướng dẫn click-by-click với screenshot
- `kanban_template_import.json` — file import cho Trello/Notion/ClickUp
- `kanban_csv_seed.csv` — danh sách task mẫu nạp lần đầu
- `kanban_automation_rules.md` — danh sách automation cần bật
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/Kanban/`

## Checklist Trước Khi Giao
- [ ] Column đủ 5-6 stage, không quá 8
- [ ] WIP limit tính theo size team thực tế
- [ ] Có ít nhất 3 automation rule chạy được
- [ ] Label phân loại task rõ ràng theo màu
- [ ] Có training 30 phút cho team
- [ ] Có dashboard tổng + báo cáo tuần
