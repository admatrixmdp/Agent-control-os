---
name: mkt-event-launch-plan
description: |
  Plan ra mắt sản phẩm/dịch vụ cho doanh nghiệp Việt Nam theo timeline T-30 → T0 → T+30 với checklist từng tuần (PR, ads, email, KOL, event, sales enablement). Kích hoạt khi người dùng nói: "plan ra mắt sản phẩm", "product launch plan", "launch roadmap", "kế hoạch launch", "ra mắt sản phẩm mới", "lịch launch 30 ngày", "plan tung sản phẩm", "go to market plan". Output là Excel timeline + dashboard tiến độ.
---

# Plan Ra Mắt Sản Phẩm — T-30 → T0 → T+30

## Mục Tiêu
Đảm bảo mọi đầu việc launch được thực hiện đúng thời điểm, không bỏ sót, có đủ buzz và conversion. Tăng tỷ lệ launch thành công lên 2-3x so với launch không plan.

## Khi Nào Dùng
- Ra mắt sản phẩm mới
- Ra mắt phiên bản 2/3
- Mở rộng thị trường mới
- Tái định vị thương hiệu
- Khai trương cửa hàng/chi nhánh

## Bước 1: Brief Launch
Hỏi:
1. Sản phẩm + USP + giá
2. Ngày launch (T0)
3. Mục tiêu (1.000 đơn? 100 demo?)
4. Ngân sách launch (ads, KOL, event)
5. Đối tượng chính
6. Stack kênh (FB/IG/TikTok/Email/PR)
7. Team size

## Bước 2: Phân Giai Đoạn Timeline
**T-30 → T-15 (Pre-launch buzz):**
- Teaser content "có điều sắp tới"
- KOL gửi gift bí mật
- Email "waiting list" + landing page chờ
- PR pitch báo độc quyền (embargo)

**T-14 → T-1 (Build momentum):**
- Đếm ngược trên social
- Webinar/livestream preview
- Influencer review pre-release
- Email reminder cho waiting list

**T0 (Launch day):**
- Bài launch FB/IG/TikTok đồng loạt 8h sáng
- Press release gửi 6h sáng
- Email blast cho list 9h
- Founder livestream 19h
- Ads kích hoạt
- Affiliate/KOL post

**T+1 → T+14 (Sustain):**
- UGC reshare
- Case study đầu
- Email follow-up KH chưa mua
- Promo cho người mua sớm
- Tối ưu ads

**T+15 → T+30 (Optimize & scale):**
- Báo cáo kết quả
- Scale ads winning
- Cross-sell / upsell
- Plan version 2

## Bước 3: Sinh Checklist Đầu Việc
Excel ~80-120 đầu việc, mỗi việc có: tên, owner, deadline, dependency, trạng thái, ngân sách.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Notion MCP: tạo project board kanban
- Google Calendar MCP: tạo event timeline
- Google Sheets MCP: budget tracker
- Slack MCP: channel #launch-xxx
- Gmail MCP: gửi notify hàng tuần

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tạo task hàng loạt lên Notion database
from notion_client import Client
notion = Client(auth=TOKEN)
for task in tasks:
    notion.pages.create(parent={'database_id':DB_ID}, properties={
      'Name':{'title':[{'text':{'content':task['name']}}]},
      'Deadline':{'date':{'start':task['deadline']}},
      'Owner':{'people':[{'id':task['owner_id']}]},
      'Status':{'status':{'name':'Not started'}}})
```

## Bước 5: Output Format
- File `.xlsx` master timeline 60 ngày
- HTML dashboard tiến độ realtime
- Communication plan (kênh + tần suất)
- Budget breakdown by stage
- Risk log + contingency
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Timeline 60 ngày đầy đủ
- [ ] Mỗi task có owner + deadline
- [ ] Có dependency rõ
- [ ] Budget breakdown
- [ ] Communication plan
- [ ] Risk log + plan B
- [ ] Đã sync Notion/Sheet team
