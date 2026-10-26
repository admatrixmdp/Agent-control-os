---
name: mkt-trade-show-plan
description: |
  Plan tham dự hội chợ B2B (Vietnam Expo, ITE, VIIE, VietBuild...) cho doanh nghiệp Việt Nam — booth, demo, lead capture, follow-up. Kích hoạt khi người dùng nói: "plan hội chợ B2B", "tham dự trade show", "kế hoạch triển lãm", "booth thiết kế", "lead capture event", "event B2B Việt Nam", "Vietnam Expo plan", "tham dự triển lãm". Output là Markdown plan + Excel checklist.
---

# Plan Tham Dự Hội Chợ B2B

## Mục Tiêu
Tận dụng tối đa khoản đầu tư 100tr-500tr cho booth, đem về 200-500 lead chất lượng và 5-15 deal trong 90 ngày sau hội chợ.

## Khi Nào Dùng
- B2B doanh nghiệp tham dự lần đầu
- Mở rộng thị trường mới
- Launch sản phẩm B2B
- Networking với partner/distributor
- Tăng brand authority

## Bước 1: Brief Event
Hỏi:
1. Tên + ngày + địa điểm event
2. Loại booth (kích thước, vị trí)
3. Ngân sách total
4. Số nhân sự dự
5. Mục tiêu (lead/deal/PR/brand)
6. Đối tượng visitor target
7. Sản phẩm/dịch vụ trưng bày

## Bước 2: Chia 3 Giai Đoạn
**Pre-event (T-30 → T-1):**
- Đăng ký booth, thanh toán
- Thiết kế + thi công booth
- Sản xuất marketing material (brochure, namecard, gift, video demo)
- Đào tạo team booth (script, role-play)
- Pre-meeting với lead mục tiêu (book lịch trước)
- Promote sự tham dự (email, social, PR)
- Setup lead capture tool (form/QR/app)

**During event (T0):**
- Daily briefing trước giờ mở
- Booth setup 1h trước mỗi ngày
- Demo lịch theo slot (mỗi 30 phút)
- Lead capture mọi visitor (QR scan namecard)
- Real-time qualification (BANT)
- Social media live update
- Networking ngoài giờ với partner
- End-of-day debrief

**Post-event (T+1 → T+30):**
- Phân loại lead theo độ nóng (hot/warm/cold)
- Email follow-up trong 48h
- Sales call cho hot lead trong 7 ngày
- Báo cáo ROI sự kiện
- Lưu lessons learned

## Bước 3: Sinh Checklist 80-100 Việc
Phân theo giai đoạn + stream (booth, marketing, sales, ops). Mỗi việc có owner + deadline.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Notion MCP: project board event
- Sheets MCP: lead capture sheet
- CRM MCP: import lead sau event
- Gmail MCP: chuỗi follow-up
- Slack MCP: live updates team
- WebSearch: nghiên cứu visitor list nếu có public

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Import lead từ event app vào CRM
import csv, requests
with open('event_leads.csv') as f:
    for row in csv.DictReader(f):
        requests.post('https://api.hubapi.com/crm/v3/objects/contacts',
          headers={'Authorization':f'Bearer {TOKEN}'},
          json={'properties':{
            'firstname':row['name'].split()[0],
            'email':row['email'],
            'company':row['company'],
            'source':'Vietnam Expo 2026',
            'lead_score':row.get('bant_score',0)}})
```

## Bước 5: Output Format
- File `.md` master plan 3 giai đoạn
- File `.xlsx` checklist 80-100 việc
- Brochure + script booth template
- Lead capture form QR code
- Follow-up email template
- ROI calculator post-event
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Plan 3 giai đoạn rõ
- [ ] 80+ task có owner
- [ ] Lead capture đã test
- [ ] Sales script + role-play
- [ ] PR + social plan
- [ ] Follow-up sequence 30 ngày
- [ ] ROI tracker
