---
name: cs-ticket-trend-report
description: |
  Tạo báo cáo trend ticket CSKH hàng tuần — volume, intent breakdown, SLA, agent performance, root cause top issue. Dùng skill này khi người dùng yêu cầu: "báo cáo ticket weekly", "trend ticket CS", "weekly CS report", "phân tích volume ticket", "báo cáo SLA tuần", "agent leaderboard CS", "root cause analysis CS", "dashboard chăm sóc khách hàng". Output là Excel + HTML dashboard + PDF executive summary.
---

# CS Ticket Trend Weekly Report

## Mục Tiêu
Báo cáo weekly cho CS Manager + Leadership — chỉ rõ trend volume, intent top, SLA performance, agent leaderboard, top 3 vấn đề cần fix gốc. Tiết kiệm 4-8h làm báo cáo tay mỗi tuần.

## Khi Nào Dùng
- CS Manager báo cáo sếp hàng tuần
- Đang tăng volume bất thường → cần biết vì sao
- Có agent dưới chuẩn cần kèm
- Sau khi launch sản phẩm/feature → đo impact lên CS
- Quarterly business review

## Bước 1: Cấu Trúc Báo Cáo 5 Phần
1. **Executive Summary** (1 trang): top 3 highlight + 3 issue
2. **Volume & Trend**: ticket vào / đóng / backlog so tuần trước
3. **Intent Breakdown**: top 10 intent + % thay đổi
4. **SLA Performance**: FRT, AHT, FCR theo channel
5. **Agent Leaderboard**: top 5 + bottom 3

## Bước 2: Tính Toán Metric Chuẩn
**Công thức:**
- **Volume W/W**: (week_n − week_n-1) / week_n-1 × 100%
- **FRT** (First Response Time): trung vị (median) > trung bình
- **AHT** (Avg Handle Time): tổng thời gian / số ticket đóng
- **FCR** (First Contact Resolution): % ticket đóng không reopen / không escalate
- **CSAT**: avg rating 1-5
- **Backlog**: số ticket open quá > 7 ngày

## Bước 3: Root Cause Analysis Top 3
Mỗi tuần chọn 3 intent có volume tăng > 30% W/W:
- Pull 10 ticket sample của intent đó
- Phân tích: nguyên nhân gốc là gì? (bug? policy? UX? marketing miscommunication?)
- Đề xuất fix + owner

Template:
```
[Issue #1]: Hỏi "không track được đơn" tăng 78% W/W (122 → 217 ticket)
Root cause: API tracking lỗi từ thứ Hai, ETA fix Thứ Năm
Owner: PM Logistics
Impact: 217 ticket × 8 phút = 29h agent / tuần
Recommended: thông báo lên homepage + canned response sẵn
```

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets: pull data từ Zendesk → dashboard live
- Gmail MCP: gửi báo cáo sáng Thứ Hai cho leadership
- Slack MCP: post summary vào #cs-leadership weekly
- Linear/Jira MCP: tạo issue cho root cause top 3
- WebSearch: benchmark FRT/CSAT ngành VN

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Auto-generate weekly CS report
import requests, pandas as pd
from datetime import datetime, timedelta
auth = ("agent@co.vn/token", "TOKEN")
end = datetime.now()
start = end - timedelta(days=7)
r = requests.get("https://co.zendesk.com/api/v2/incremental/tickets.json",
                 params={"start_time": int(start.timestamp())}, auth=auth)
df = pd.DataFrame(r.json()["tickets"])
summary = {
    "total_in": len(df),
    "total_solved": len(df[df.status == "solved"]),
    "avg_frt": df["first_response_time_in_minutes"].median(),
    "top_intents": df.groupby("tags").size().nlargest(10).to_dict()
}
generate_pdf(summary)
send_to_leadership(summary)
```

## Bước 5: Output Format
- **Excel `CS_Weekly_W{nn}.xlsx`**:
  - Sheet Summary
  - Sheet Volume Trend (chart)
  - Sheet Intent breakdown
  - Sheet SLA
  - Sheet Agent leaderboard
  - Sheet Root cause top 3
- **HTML dashboard** view-only cho leadership
- **PDF Executive Summary** 2 trang
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-ticket-trend-report/output/`

## Checklist Trước Khi Giao
- [ ] Báo cáo có 5 phần đầy đủ
- [ ] Metric công thức rõ ràng, đo lặp lại được
- [ ] Top 3 issue có owner + ETA fix
- [ ] So sánh W/W và MoM
- [ ] Chart trực quan, không bảng số khô
- [ ] Tự động gửi sáng Thứ Hai
