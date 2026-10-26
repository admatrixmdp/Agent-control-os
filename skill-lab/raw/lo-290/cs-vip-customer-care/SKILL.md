---
name: cs-vip-customer-care
description: |
  Thiết kế chương trình chăm sóc khách hàng VIP — phân tier, touchpoint theo dịp (sinh nhật, kỷ niệm, lễ), gift, dedicated agent, SLA ưu tiên. Dùng skill này khi người dùng yêu cầu: "chăm sóc khách VIP", "VIP loyalty program", "dedicated agent VIP", "quà sinh nhật khách", "occasion-based marketing CS", "tier customer care", "white-glove service", "chương trình thân thiết". Output là Excel CRM plan + email template + lịch touch-point.
---

# CS VIP Customer Care Program

## Mục Tiêu
Xây chương trình chăm sóc VIP để giữ chân khách top 5-10% giá trị nhất — tăng retention 20%+, LTV 2-3 lần, biến VIP thành brand advocates.

## Khi Nào Dùng
- Doanh nghiệp có nhóm khách lớn, doanh thu tập trung 80/20
- Khách VIP rời đi, không có cảnh báo
- Cạnh tranh cao, đối thủ kéo khách VIP
- Mở rộng cao cấp/luxury cần white-glove service
- Sau khi có dữ liệu CRM đủ phân tier

## Bước 1: Phân Tier VIP
| Tier | Tiêu chí | Quyền lợi |
|---|---|---|
| **Diamond** | LTV > 100tr/năm | Dedicated agent, SLA 1h, gift cao cấp, event riêng |
| **Gold** | LTV 30-100tr/năm | Priority queue, gift sinh nhật, voucher 10% |
| **Silver** | LTV 10-30tr/năm | Fast support, voucher sinh nhật |
| **Standard** | < 10tr/năm | Như KH thường |

Phân tier 6 tháng/lần dựa CRM data, có grandfathering 3 tháng khi tier giảm.

## Bước 2: Touchpoint Theo Dịp
**Lịch chăm sóc VIP cả năm:**
- **Sinh nhật KH**: voucher + thiệp tay (Diamond), gift sang
- **Ngày kỷ niệm thành VIP**: thank-you note
- **Tết Nguyên Đán**: gift lớn + thiệp CEO ký
- **Lễ ngành**: ưu đãi riêng
- **Sau mua hàng**: welcome call trong 48h
- **Định kỳ Q1/Q3**: business review call (B2B) hoặc satisfaction call (B2C)
- **Khi không mua > 60 ngày**: re-engagement call

## Bước 3: Dedicated Agent & SLA Ưu Tiên
- Mỗi VIP có 1 Account Manager hoặc Senior CS dedicated
- VIP gọi → auto route qua AM (skill-based routing)
- SLA: Diamond 1h / Gold 2h / Silver 4h
- Có "VIP escalation hotline" riêng, bỏ qua queue thường
- Sticky session: cùng agent trong 1 vấn đề

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Calendar MCP: tạo reminder sinh nhật/kỷ niệm tự động
- Gmail MCP: gửi thiệp cá nhân hoá CEO ký
- Google Sheets: CRM-lite tracking VIP + lịch sử touchpoint
- Slack MCP: alert AM khi VIP có ticket / mất 30+ ngày không mua
- WebSearch: best practice VIP program (Apple, Vingroup)
- WebFetch: tham khảo loyalty tier của brand

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Auto-detect VIP churn risk + alert AM
import requests
from datetime import datetime, timedelta
crm = requests.get("https://crm.api/customers?tier=diamond,gold").json()
for c in crm:
    last_order = datetime.fromisoformat(c["last_order_date"])
    if datetime.now() - last_order > timedelta(days=60):
        # Tạo task cho AM
        requests.post("https://crm.api/tasks", json={
            "customer_id": c["id"],
            "owner": c["account_manager"],
            "type": "vip_re_engage",
            "due": (datetime.now() + timedelta(days=3)).isoformat()
        })
```

## Bước 5: Output Format
- **Excel `VIP_Program.xlsx`**:
  - Sheet Tier: tiêu chí + quyền lợi
  - Sheet Calendar: touch-point cả năm
  - Sheet VIP list: tên + AM + lịch sử
  - Sheet KPI: retention rate / NPS VIP
- **Email template** sinh nhật, kỷ niệm, re-engagement
- **Script welcome call** sau khi lên VIP
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-vip-customer-care/output/`

## Checklist Trước Khi Giao
- [ ] Tiêu chí tier khách quan, dựa CRM data
- [ ] Quyền lợi mỗi tier khác biệt rõ
- [ ] Calendar 12 tháng có touchpoint cụ thể
- [ ] Mỗi VIP có AM được assign
- [ ] SLA ưu tiên rõ
- [ ] Có cơ chế alert churn risk
