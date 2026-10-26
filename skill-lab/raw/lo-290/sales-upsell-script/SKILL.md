---
name: sales-upsell-script
description: |
  Soạn script upsell KH hiện hữu theo trigger usage/milestone/feature gap với value-first approach, tăng expansion ARR. Trigger phrases: "script upsell", "upsell khách hàng cũ", "tăng tier khách hiện hữu", "expansion sales", "upsell SaaS", "viết script tăng gói", "convert KH lên premium", "upgrade khách hàng", "upsell B2B", "kịch bản tăng gói". Output là Markdown script + Excel upsell triggers list.
---

# Upsell Script Builder

## Mục Tiêu
Tăng NRR và expansion ARR bằng script upsell timing-based đánh vào trigger thực (usage cap, new feature, team growth) thay vì spam offer ngẫu nhiên.

## Khi Nào Dùng
- KH hit 80% usage limit
- KH thêm 30% headcount tháng qua
- Launch feature/tier mới
- Sau QBR thành công
- Renewal kèm upgrade

## Bước 1: Xác định Upsell Trigger
3 nhóm trigger:

**Trigger Usage** (KH cần thêm capacity):
- Hit >80% seat/quota/storage
- Heavy user feature X >50 lần/tháng
- API call gần limit

**Trigger Milestone**:
- Headcount tăng 20%+ trong 6 tháng
- KH announce expansion (geo, vertical)
- KH funding round mới

**Trigger Feature Gap**:
- Active user request feature có ở tier cao
- Support ticket pattern → feature có ở tier cao giải quyết
- Competitor feature KH hỏi đã có ở premium

## Bước 2: Script Theo Trigger

**Template A — Usage cap**:
"Chào anh Minh, em thấy team anh đã dùng 85% seat tháng này (50/60). Theo trend 3 tháng, anh sẽ hit ceiling trong 6 tuần. Em đề xuất 2 option:
1. Add 20 seat ngay → giá lock năm hiện tại
2. Upgrade Pro tier → unlimited + 3 feature mới
Anh muốn em chạy số ROI option nào?"

**Template B — Milestone**:
"Chào anh, em thấy bên anh tuyển thêm 15 sales 2 tháng qua. Nhân dịp này em xem lại workflow team mới — họ có thể cần feature X em đang ở Premium. Em đề xuất 30 phút review không?"

**Template C — Feature gap**:
"Tuần này em thấy team anh submit ticket #X 3 lần. Cái này Pro tier resolve được trong 1 click. Em chia sẻ demo 10 phút được không?"

## Bước 3: Trial close + Negotiate
- Hỏi outcome: "Nếu unlock X, team anh tiết kiệm bao nhiêu giờ/tuần?"
- Đưa ROI nhanh: "X giờ × hourly cost = $Y/tháng → payback 2 tháng"
- Mở option: monthly add-on / annual upgrade / pilot 30 ngày

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce/HubSpot MCP: pull usage data + opportunity expansion
- Gainsight MCP: trigger alert khi hit threshold
- Gmail MCP: send upsell email với data viz
- Slack MCP: notify CSM khi trigger fired

**Fallback API:**
```python
# Pull usage + trigger upsell
import requests
usage = requests.get(f"https://app.com/api/usage/{acct_id}").json()
if usage["seats_used"] / usage["seats_total"] > 0.8:
    # Trigger upsell workflow trong HubSpot
    requests.post("https://api.hubapi.com/automation/v3/workflows/123/enrollments/contacts/{email}",
        headers=headers)
```

## Bước 5: Output Format
- **File 1**: `upsell_scripts.md` — 6 template theo 3 trigger × 2 channel (email/call)
- **File 2**: `upsell_triggers.xlsx` — Trigger / Threshold / Account / Owner / Script template / Status
- **File 3**: `upsell_roi_calc.xlsx` — input usage + output ROI tự tính
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Trigger có ngưỡng data cụ thể
- [ ] Script value-first (không feature-dump)
- [ ] Có ROI calculator gửi kèm
- [ ] Trial close giữa script
- [ ] Multiple option (add-on / upgrade / pilot)
- [ ] Tag account đã upsell trong CRM (tránh spam)
