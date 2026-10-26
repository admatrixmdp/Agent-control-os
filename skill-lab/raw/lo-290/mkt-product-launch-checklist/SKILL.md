---
name: mkt-product-launch-checklist
description: |
  Checklist 100+ đầu việc tung sản phẩm mới T-30 → T0 cho doanh nghiệp Việt Nam — chia stream Product/Marketing/Sales/CS/Ops. Kích hoạt khi người dùng nói: "checklist tung sản phẩm", "launch checklist", "ra mắt sản phẩm checklist", "to-do launch", "product launch list", "checklist launch SP mới", "launch playbook", "GTM checklist". Output là Excel checklist + Notion board.
---

# Checklist Tung Sản Phẩm Mới T-30 → T0

## Mục Tiêu
Không bỏ sót việc gì trong launch, mọi stream Product/Marketing/Sales/CS/Ops biết rõ ai làm gì, deadline khi nào.

## Khi Nào Dùng
- Lần đầu launch sản phẩm
- Launch phiên bản 2/3
- Launch sub-brand
- Launch nội bộ (feature SaaS)
- Re-launch sản phẩm cũ

## Bước 1: Brief Launch
Hỏi:
1. Sản phẩm + giá + USP
2. Ngày launch (T0)
3. Quy mô (soft launch / public)
4. Team size + stream
5. Ngân sách
6. Mục tiêu KPI

## Bước 2: Chia Stream Đầu Việc
**Product (15 việc):**
- QA sản phẩm cuối
- Pricing + SKU
- Inventory đủ
- Documentation/manual
- Packaging
- Quality test
- Compliance/cert

**Marketing (35 việc):**
- Landing page
- Email chuỗi launch
- Social content 30 ngày
- PR pitch + press kit
- KOL/affiliate
- Ads campaign
- SEO content
- Brand asset (logo, video, photo)
- Tagline + messaging house

**Sales (15 việc):**
- Sales deck
- Battle card
- Pricing calculator
- Demo script
- Objection FAQ
- Training sales team
- CRM setup

**Customer Service (10 việc):**
- FAQ help center
- Training CS team
- Chatbot script
- Return/refund policy
- Internal SOP
- Escalation matrix

**Operations (15 việc):**
- Supply chain ready
- Logistics partner
- Payment gateway
- Tax invoice
- Legal review
- Privacy policy
- T&C
- Insurance
- Refund process

**Analytics (10 việc):**
- Tracking pixel
- GA4 event
- Conversion API
- Dashboard launch metric
- Funnel map
- Cohort analysis

## Bước 3: Gantt + Owner
Mỗi việc:
- Owner duy nhất
- Deadline cụ thể
- Dependency
- Status (Todo/Doing/Done)
- Priority (Critical/High/Medium)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Notion MCP: project board kanban
- Asana/Linear MCP: task management
- Google Calendar MCP: deadline event
- Slack MCP: channel #launch
- Sheets MCP: master tracker

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tạo task hàng loạt qua Notion
from notion_client import Client
notion = Client(auth=TOKEN)
for task in checklist_items:
    notion.pages.create(parent={'database_id':DB},
      properties={
        'Name':{'title':[{'text':{'content':task['name']}}]},
        'Stream':{'select':{'name':task['stream']}},
        'Owner':{'people':[{'id':task['owner_id']}]},
        'Deadline':{'date':{'start':task['deadline']}},
        'Status':{'status':{'name':'Not started'}}})
```

## Bước 5: Output Format
- File `.xlsx` checklist 100+ việc
- Notion board public với team
- Gantt chart timeline
- Daily standup template T-7 → T0
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 100+ việc chia 6 stream
- [ ] Mỗi việc có owner + deadline
- [ ] Dependency rõ
- [ ] Có critical path
- [ ] Risk + plan B
- [ ] Daily standup T-7
- [ ] Đã sync team
