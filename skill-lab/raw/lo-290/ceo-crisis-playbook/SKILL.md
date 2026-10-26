---
name: ceo-crisis-playbook
description: |
  Playbook xử lý khủng hoảng cho CEO — 3 cấp độ (vận hành/PR/tài chính), checklist 24h đầu, template thông cáo nội bộ + external, checklist truyền thông.
  Kích hoạt khi người dùng nói: "playbook khủng hoảng", "crisis management", "xử lý scandal", "PR crisis", "khủng hoảng truyền thông", "crisis playbook", "incident response CEO", "khẩn cấp".
  Output là PDF playbook + template communications.
---

# CEO Crisis Playbook — Sổ Tay Xử Lý Khủng Hoảng

## Mục Tiêu
Khủng hoảng = thời gian phản ứng tính bằng giờ. CEO không có thời gian Google "phải làm gì khi sa thải lớn". Playbook chuẩn bị trước theo 3 cấp độ giúp react trong 1h thay vì 24h.

## Khi Nào Dùng
- Scandal truyền thông (sản phẩm lỗi, founder controversy)
- Khủng hoảng vận hành (data breach, outage lớn)
- Khủng hoảng tài chính (không trả lương kịp, runway 2 tháng)
- Lay-off > 10% nhân sự
- Khủng hoảng pháp lý (kiện tụng, audit)

## Bước 1: Phân Loại 3 Cấp Độ Crisis
**Cấp 1 - Localized**: ảnh hưởng 1 phòng/khách hàng nhỏ. CEO biết nhưng owner là CXO. SLA: 24h.
**Cấp 2 - Departmental**: ảnh hưởng toàn department hoặc nhiều khách hàng. CEO chủ trì. SLA: 4h.
**Cấp 3 - Existential**: ảnh hưởng tồn tại công ty/uy tín. CEO + Board active. SLA: 1h response.

Mỗi cấp có chain command + comms cadence khác nhau.

## Bước 2: Checklist 24h Đầu (Cấp 2-3)
**0-1h**: Assess scope, gather facts, đừng commit gì
**1-2h**: Triệu tập crisis team (CEO, CFO, Legal, PR, Head of Affected Dept)
**2-4h**: Brief tất cả người dự internal, viết holding statement
**4-8h**: Comms internal (toàn công ty), comms với khách hàng/đối tác bị ảnh hưởng
**8-24h**: Public statement nếu cần, monitor truyền thông xã hội, daily standup
**24h+**: Daily updates, post-mortem playbook

## Bước 3: Templates Comms
- **Internal (toàn công ty)**: thừa nhận, what we know, what we're doing, next update khi nào
- **Khách hàng (email)**: apology cá nhân + remedy
- **Truyền thông (press release)**: facts only, no speculation, contact PR
- **Board/Investor**: chi tiết + ask gì
- **Social media**: 1 statement chính + pinned

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Slack MCP: tạo channel #crisis-[code], invite crisis team
- Gmail MCP: gửi mass email khách hàng từ template
- WebSearch: monitor báo chí mention công ty 24/7
- Notion MCP: lưu post-mortem & timeline crisis
- Calendar MCP: tạo recurring daily standup mỗi 12h

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Monitor truyền thông bằng Google News API
import requests
r = requests.get(
  "https://newsapi.org/v2/everything",
  params={"q": f'"{company_name}"', "from": "2026-05-28", "sortBy": "publishedAt", "apiKey": KEY}
)
articles = r.json()['articles']
negative = [a for a in articles if sentiment(a['title']) == 'neg']
```

## Bước 5: Output Format
- PDF playbook 15-20 trang chứa:
  - Phân loại 3 cấp độ
  - Checklist 24h đầu
  - Templates comms
  - Contact list (PR firm, legal, board)
  - Past crisis lessons (nếu có)
- Markdown live document trong crisis để team edit
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/crisis-playbook-vN.pdf`

## Checklist Trước Khi Giao
- [ ] 3 cấp độ rõ ràng + SLA
- [ ] Checklist 24h chia phút
- [ ] 5 templates comms sẵn sàng
- [ ] Contact list đã verify số điện thoại
- [ ] Post-mortem template
- [ ] Đã drill playbook ít nhất 1 lần
