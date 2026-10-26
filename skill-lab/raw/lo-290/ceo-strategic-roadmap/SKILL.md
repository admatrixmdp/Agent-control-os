---
name: ceo-strategic-roadmap
description: |
  Lập roadmap chiến lược 1-3 năm cho doanh nghiệp dạng Gantt + narrative — bao gồm milestone, owner, dependency, ngân sách và rủi ro. Output dạng dashboard HTML + Excel timeline.
  Kích hoạt khi người dùng nói: "lập roadmap chiến lược", "strategic roadmap", "kế hoạch 3 năm", "roadmap CEO", "lộ trình công ty", "3-year plan", "long-term roadmap", "kế hoạch dài hạn".
  Output là HTML Gantt + Excel.
---

# CEO Strategic Roadmap — Roadmap Chiến Lược 1-3 Năm

## Mục Tiêu
Doanh nghiệp tăng trưởng nhanh thường bị "đầu lo đuôi". Roadmap 1-3 năm giúp CEO align toàn bộ tổ chức về đích đến, phân bổ nguồn lực, tránh dự án trùng lặp/triệt tiêu nhau.

## Khi Nào Dùng
- Đầu năm tài chính
- Sau khi raise round mới
- Sau pivot chiến lược
- Khi board yêu cầu vision 3 năm
- Trước annual off-site

## Bước 1: Thu Thập Đầu Vào
- Vision 3 năm (1 câu)
- 3-5 strategic bets công ty đặt cược
- Doanh thu mục tiêu năm 1, 2, 3
- Headcount mục tiêu
- Budget tổng (CapEx + OpEx)
- Ràng buộc: thị trường, vốn, đối thủ

Hỏi CEO: tham vọng (10x) hay an toàn (2-3x)?

## Bước 2: Chia Roadmap 3 Tầng
**Tầng 1 - Strategic bets** (5-7 cái, kéo 1-3 năm): VD "Thâm nhập miền Bắc", "Ra mắt SaaS B2B"

**Tầng 2 - Milestones quý** (mỗi bet có 4-8 milestone): VD "Q3/2026: Đạt 100 khách trả phí"

**Tầng 3 - Initiatives** (mỗi milestone có 2-4 initiative concret): VD "Tuyển GĐ Bắc Q2"

Mỗi tầng phải có owner + deadline + ngân sách + KPI thành công.

## Bước 3: Vẽ Gantt + Dependency
- Trục thời gian theo quý (12 quý cho 3 năm)
- Mỗi bet 1 dòng, milestones là các block
- Dependency vẽ mũi tên nối milestone phụ thuộc
- Highlight critical path (đỏ)
- Note ngân sách & headcount theo từng giai đoạn

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Notion MCP: tạo database "Strategic Bets" với property quarter, owner, status
- Linear MCP: tạo cycle/project tương ứng từng bet
- Google Drive MCP: lưu Sheet roadmap để các team edit
- WebSearch: tìm benchmark roadmap công ty cùng ngành (VD: SaaS B2B 3-year plan)
- Slack MCP: post highlight lên #strategy

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tạo Gantt bằng plotly
import plotly.figure_factory as ff
tasks = [
  dict(Task="Bet 1: SaaS B2B", Start='2026-01-01', Finish='2027-06-30', Owner='CPO'),
  dict(Task="Bet 2: Thâm nhập Bắc", Start='2026-04-01', Finish='2027-12-31', Owner='CCO'),
]
fig = ff.create_gantt(tasks, group_tasks=True, show_colorbar=True)
fig.write_html('/tmp/roadmap.html')
```

## Bước 5: Output Format
- HTML Gantt interactive (hover hiện chi tiết)
- Excel `strategic-roadmap-YYYY-YYYY.xlsx` 3 sheet: Bets / Milestones / Initiatives
- Narrative .docx 8-12 trang giải thích "tại sao" mỗi bet
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Có 5-7 strategic bets (không quá ít, không quá nhiều)
- [ ] Mỗi bet có owner cấp C-level
- [ ] Critical path được highlight
- [ ] Có ngân sách + headcount cho từng năm
- [ ] Mỗi milestone có KPI đo thành công
- [ ] Narrative giải thích logic chiến lược
