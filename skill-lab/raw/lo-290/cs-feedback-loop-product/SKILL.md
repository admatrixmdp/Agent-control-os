---
name: cs-feedback-loop-product
description: |
  Xây dựng feedback loop từ phòng CSKH về Product team — gom insight ticket, tag bug/feature request, prioritize, tracking đến khi ship. Dùng skill này khi người dùng yêu cầu: "feedback loop CS to Product", "kết nối CS với Product team", "customer voice product", "product feedback process", "ticket → product backlog", "VoC program", "insight từ CS", "đóng góp ý tưởng từ CSKH". Output là Excel pipeline + Slack workflow + Markdown SOP.
---

# CS → Product Feedback Loop

## Mục Tiêu
Thiết lập kênh chính thức để insight từ ticket CSKH (bug, feature request, UX pain) chảy về Product team — được prioritize, ship, và feedback lại CS + KH. Đảm bảo "customer voice" không bị mất.

## Khi Nào Dùng
- CS biết bug nhưng Product không nghe
- KH request feature lặp đi lặp lại mà không ai theo dõi
- Product ship feature nhưng không biết CS có cần không
- Sau khi sản phẩm/app launch cần đo VoC (Voice of Customer)
- Setup mới quy trình product/CS

## Bước 1: Phân Loại Insight Từ Ticket
Mỗi ticket có thể chứa:
- **Bug**: lỗi rõ ràng (button không click, data sai)
- **Feature Request**: KH muốn có chức năng mới
- **UX Pain**: KH confuse, không hiểu cách dùng
- **Praise**: khen — feed PR + retention team
- **Competitor Mention**: nhắc tới đối thủ — feed product strategy

Agent tag thêm khi đóng ticket. Tạo dropdown trong Zendesk/Freshdesk.

## Bước 2: Aggregation & Prioritization
Pipeline hàng tuần:
1. Pull tất cả ticket có tag `product_feedback` 7 ngày qua
2. Cluster theo similarity (vd: 30 ticket về "không track được đơn" → 1 cluster)
3. Tính **Pain Score** = (số ticket × giá trị KH × severity) / effort
4. Top 10 cluster đưa vào Product Backlog meeting

Template:
```
[Cluster #023]: "Không tìm thấy đơn cũ trong app"
- Số ticket: 47 trong 30 ngày
- Tier KH: 12 Gold, 35 Standard
- Severity: Medium (KH bực nhưng không churn)
- Suggested fix: search bar trong order history
- Pain Score: 8.2/10
- Owner: PM @nam
```

## Bước 3: Close The Loop Với KH
Khi Product ship feature → quay lại báo KH:
- CS gom danh sách KH từng request → email cá nhân hoá
  ```
  Chào anh/chị {ten}, cảm ơn anh/chị tháng trước đã góp ý
  chúng tôi cần [X]. Hôm nay chúng tôi đã release [X].
  Anh/chị thử và cho em biết nha.
  ```
- Update KB article + canned response
- Thông báo team CS để cập nhật script

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Linear/Jira/Notion MCP: tự tạo ticket Product từ cluster CS
- Slack MCP: channel #cs-to-product, alert khi có cluster mới
- Google Sheets: master backlog feedback dashboard
- Gmail MCP: gửi mail "feature shipped" cho KH từng request
- WebSearch: VoC framework Productboard / Canny

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Đẩy cluster CS thành issue Linear
import requests
H = {"Authorization": "LINEAR_API_KEY", "Content-Type": "application/json"}
q = """mutation { issueCreate(input: {
    title: "[CS] %s",
    description: "%s",
    teamId: "TEAM_ID",
    labelIds: ["customer-feedback"]
}) { issue { id } } }"""
def push_cluster(title, body):
    r = requests.post("https://api.linear.app/graphql",
                      json={"query": q % (title, body)}, headers=H)
    return r.json()
```

## Bước 5: Output Format
- **Excel `Product_Feedback_Pipeline.xlsx`**:
  - Sheet Raw Insight (ticket level)
  - Sheet Cluster (aggregated)
  - Sheet Backlog (đã chuyển PM)
  - Sheet Shipped (đã release)
- **Markdown SOP**: quy trình weekly meeting CS-Product
- **Email template** "feature shipped" cho KH
- **Dashboard** Pain Score top 10 real-time
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-feedback-loop-product/output/`

## Checklist Trước Khi Giao
- [ ] Agent có dropdown tag insight khi đóng ticket
- [ ] Pipeline cluster + score tự động
- [ ] Weekly meeting CS ↔ Product có lịch cố định
- [ ] Sync tự động sang Linear/Jira
- [ ] Có close-the-loop với KH khi ship
- [ ] Dashboard cho leadership xem trend
