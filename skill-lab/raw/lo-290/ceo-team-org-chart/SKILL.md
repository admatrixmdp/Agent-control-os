---
name: ceo-team-org-chart
description: |
  Sinh sơ đồ tổ chức (org chart) tự động từ HRIS/Google Sheets — hiển thị cấu trúc báo cáo, headcount theo phòng, vacant role, span of control. Output SVG/PDF.
  Kích hoạt khi người dùng nói: "sơ đồ tổ chức", "org chart", "team chart", "cấu trúc công ty", "biểu đồ phòng ban", "organizational chart", "headcount chart", "reporting structure".
  Output là SVG + PDF + PowerPoint slide.
---

# CEO Team Org Chart — Sơ Đồ Tổ Chức Động

## Mục Tiêu
Sơ đồ tổ chức vẽ tay nhanh outdate. Skill này tự sinh org chart từ HRIS/Sheets mỗi tháng — show span of control, vacant role, ratio IC vs Manager để CEO ra quyết định tái cấu trúc.

## Khi Nào Dùng
- Sau wave hire/lay-off
- Trước reorg
- Onboarding nhân viên mới (đưa org chart)
- Annual planning (xem có top-heavy không)
- Trước due diligence (M&A, fundraising)

## Bước 1: Nhập Cấu Trúc
- Bảng employees: name, title, manager, department, status (active/vacant/hiring)
- Lấy từ HRIS hoặc Google Sheet "Employees"
- Hỏi: hiện 2 lớp/3 lớp/4 lớp báo cáo

## Bước 2: Tính Metric Tổ Chức
- Total headcount + active + vacant
- Headcount mỗi phòng ban
- Span of control trung bình (số report/manager)
- IC : Manager ratio (mục tiêu ≥ 6:1)
- % role vacant (target < 10%)
- Layers (số lớp từ CEO xuống IC, target ≤ 5)

## Bước 3: Vẽ Org Chart
- Tree top-down: CEO → CXOs → Directors → Managers → ICs
- Mỗi node có: ảnh + tên + title + ngày join
- Vacant role: hộp đứt nét + "HIRING"
- Color code: phòng ban
- Compact mode cho công ty 100+ người

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: pull bảng employees
- HRIS connector (BambooHR, Misa, FastWork): full integration
- Slack MCP: lookup avatar nhân viên
- Notion MCP: post org chart vào page "Company"
- Google Drive MCP: lưu SVG vào shared folder

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Vẽ org chart bằng graphviz
import graphviz
dot = graphviz.Digraph(format='svg', graph_attr={'rankdir':'TB'})
for emp in employees:
    style = 'filled,dashed' if emp['status']=='vacant' else 'filled'
    dot.node(emp['id'], f"{emp['name']}\n{emp['title']}", style=style, fillcolor='lightblue')
    if emp['manager_id']:
        dot.edge(emp['manager_id'], emp['id'])
dot.render('/tmp/orgchart')
```

## Bước 5: Output Format
- SVG (scalable) cho web
- PDF print-ready khổ A2
- PNG cho Slack/Notion
- 1 slide PPT chèn vào board deck
- Bảng metric kèm theo (Excel)
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/orgchart-YYYY-MM.svg`

## Checklist Trước Khi Giao
- [ ] Tất cả employee active hiển thị
- [ ] Vacant role được flag rõ
- [ ] Span of control mỗi manager hiển thị
- [ ] Color code phòng ban
- [ ] Có metric tổ chức (ratio, layers)
- [ ] Privacy: không show salary
