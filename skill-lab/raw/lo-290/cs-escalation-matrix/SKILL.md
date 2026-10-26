---
name: cs-escalation-matrix
description: |
  Thiết kế ma trận escalation (severity × team × thời gian) cho phòng CSKH — quyết định khi nào escalate, lên ai, trong bao lâu, kèm template thông báo. Dùng skill này khi người dùng yêu cầu: "tạo escalation matrix", "ma trận leo thang", "quy trình escalate", "khi nào báo sếp", "SLA escalation CS", "incident escalation", "ticket nóng leo thang", "chính sách escalate khiếu nại". Output là Excel + flowchart + template email/Slack.
---

# CS Escalation Matrix Designer

## Mục Tiêu
Xây dựng ma trận chuẩn để agent biết chính xác khi nào escalate ticket, lên team/cấp nào, trong bao lâu — tránh ticket nóng bị bỏ quên hoặc escalate sai chỗ làm phiền sếp.

## Khi Nào Dùng
- Agent không biết khi nào nên báo sếp, ticket bị stuck
- Khách hàng VIP/báo chí complain → cần escalate ngay nhưng không biết quy trình
- SLA bị miss vì không có cơ chế tự động leo thang
- Setup mới phòng CS / hoặc reorg team
- Sau sự cố lớn cần rà lại quy trình

## Bước 1: Xác Định 4 Mức Severity
| Severity | Định nghĩa | Ví dụ |
|---|---|---|
| **S1 — Critical** | Ảnh hưởng nhiều KH, brand risk | Hệ thống down, KH VIP threaten kiện |
| **S2 — High** | 1 KH bức xúc, có thể viral | Đơn 5tr giao sai, KH đăng FB |
| **S3 — Medium** | Vấn đề cần giải quyết nhưng KH chấp nhận chờ | Refund chậm 3 ngày |
| **S4 — Low** | Câu hỏi thường, không khẩn | Hỏi cách dùng |

## Bước 2: Thiết Kế Matrix
| Severity | Owner Lv1 | Escalate Lv2 sau | Escalate Lv3 sau | Notify CEO |
|---|---|---|---|---|
| S1 | Agent + TL ngay | 15 phút | 30 phút | Có (luôn) |
| S2 | Agent | 1h | 4h | Nếu chưa giải quyết 8h |
| S3 | Agent | 8h | 24h | Không |
| S4 | Agent | 48h | 5 ngày | Không |

**Lv1 = Agent, Lv2 = Team Lead, Lv3 = CS Manager, Lv4 = Head/CEO.**

## Bước 3: Template Thông Báo Khi Escalate
**Slack/Email template:**
```
[ESCALATION S{level}] Ticket #{ma_ticket}
KH: {ten_kh} ({tier: VIP/Normal})
Vấn đề: {tom_tat_1_dong}
Đã thử: {agent_da_lam}
Lý do escalate: {SLA_missed / Above_authority / VIP}
Cần Mr/Ms {ten_nguoi}: {action_can_lam}
Link ticket: {url}
Deadline phản hồi: {time}
```

Có deadline rõ ràng để tránh ngâm.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Slack MCP: gửi alert tự động vào channel #cs-escalation theo severity
- Gmail MCP: gửi mail escalate cho Manager kèm tag urgent
- Google Sheets: log mọi escalation để review monthly
- Google Calendar MCP: tạo event "Escalation review" weekly
- WebSearch: ITIL / Zendesk escalation framework
- WebFetch: SLA của brand tham khảo

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Auto-escalate Zendesk ticket khi quá SLA
import requests
from datetime import datetime, timedelta
auth = ("agent@co.vn/token", "TOKEN")
r = requests.get("https://co.zendesk.com/api/v2/search.json",
    params={"query": "status<solved priority:high updated<2hours"}, auth=auth)
for t in r.json()["results"]:
    # Đánh dấu escalate + assign TL + alert Slack
    requests.put(f"https://co.zendesk.com/api/v2/tickets/{t['id']}.json",
        json={"ticket": {"priority": "urgent",
                         "assignee_id": TL_ID,
                         "tags": t["tags"] + ["escalated_l2"]}}, auth=auth)
    slack_alert(t)
```

## Bước 5: Output Format
- **Excel `Escalation_Matrix.xlsx`**: sheet Matrix, Severity definitions, Contacts, Examples
- **Flowchart PNG**: vẽ flow "ticket vào → tag severity → assign → escalate timer"
- **Markdown playbook** cho team CS
- **Slack template + Email template** copy-paste ready
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-escalation-matrix/output/`

## Checklist Trước Khi Giao
- [ ] 4 mức severity có định nghĩa rõ + ví dụ
- [ ] Matrix có thời gian cụ thể, không mơ hồ
- [ ] Có owner mỗi mức (tên + backup khi vắng)
- [ ] Template Slack/Email sẵn
- [ ] Auto-escalate qua API/trigger khi miss SLA
- [ ] Đã train team CS, có roleplay 2 case mẫu
