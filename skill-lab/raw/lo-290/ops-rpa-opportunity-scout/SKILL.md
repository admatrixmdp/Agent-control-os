---
name: ops-rpa-opportunity-scout
description: |
  Phát hiện cơ hội tự động hóa (RPA) trong quy trình vận hành — đánh giá ROI, đề xuất giải pháp Make/Zapier/n8n/Power Automate phù hợp với SME Việt Nam. Dùng skill này khi người dùng yêu cầu: "tìm cơ hội RPA", "automation opportunity", "tự động hóa quy trình", "audit quy trình tự động hóa", "Make.com workflow", "Zapier automation", "n8n self-hosted", "giảm thao tác thủ công". Output là Excel scoring + Markdown report đề xuất top 5 use case.
---

# Phát Hiện Cơ Hội RPA & Đề Xuất Tự Động Hóa

## Mục Tiêu
Quét toàn bộ quy trình vận hành để chỉ ra đâu là việc "lặp đi lặp lại + dễ tự động", tính ROI tiết kiệm giờ/người, đề xuất tool RPA phù hợp ngân sách SME.

## Khi Nào Dùng
- Nhân viên kêu "ngày nào cũng copy-paste cùng thứ"
- Muốn giảm nhân sự admin/data entry
- Sếp hỏi "công ty mình có thể automate cái gì?"
- Vừa mua subscription Make/Zapier nhưng chưa biết dùng vào đâu
- Audit hàng năm trước budget IT

## Bước 1: Map Hoạt Động Thường Lệ
Hỏi danh sách các task lặp lại hàng ngày/tuần/tháng. Với mỗi task ghi:
- Tên task
- Người làm + Phòng ban
- Tần suất (lần/ngày, lần/tuần)
- Thời gian/lần (phút)
- Hệ thống liên quan (Excel, Sheets, KiotViet, Sapo, Email, Slack, Zalo)

## Bước 2: Chấm Điểm RPA Suitability
Mỗi task chấm 5 tiêu chí (1-5 điểm):
| Tiêu chí | 1đ | 5đ |
|---|---|---|
| **Lặp lại** | Mỗi tháng 1 lần | Mỗi giờ |
| **Quy tắc rõ ràng** | Nhiều ngoại lệ | If-then rõ |
| **Số bước** | <3 bước | 5-15 bước qua nhiều app |
| **Khối lượng** | <10 record/lần | >100 record/lần |
| **Stable input** | Format thay đổi liên tục | Format cố định |

→ Task >= 18 điểm = ƯU TIÊN AUTOMATE

## Bước 3: Đề Xuất Tool & Kiến Trúc
| Use case | Tool đề xuất | Lý do |
|---|---|---|
| Sync Sheets <-> CRM | Make.com | UI đẹp, scenario phức tạp |
| Slack notification | Zapier | Trigger nhanh, free tier ổn |
| Tự host, data nhạy cảm | n8n self-host | Free, chạy VPS 5$/tháng |
| Office 365 ecosystem | Power Automate | Có sẵn license |
| Web scraping + AI | Make + GPT | Kết hợp AI agent |
| Sàn TMĐT VN | KiotViet API + Make webhook | API chuẩn REST |

Tính ROI: `(Giờ tiết kiệm/tháng × Lương/giờ) - (Tool fee + Build time)`

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Đọc bảng task log để phân tích
- Slack MCP: Survey nhân viên về task lặp lại qua bot
- Notion MCP: Lưu RPA backlog vào database
- WebSearch: Tra giá Make.com/Zapier mới nhất
- WebFetch: Lấy template scenario từ make.com/templates

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tạo scenario Make.com qua API
import requests
MAKE_TOKEN = "xxx"
TEAM_ID = "12345"
r = requests.post(f"https://eu1.make.com/api/v2/scenarios",
    headers={"Authorization": f"Token {MAKE_TOKEN}"},
    json={"teamId": TEAM_ID,
          "name": "Sync KiotViet -> Google Sheets",
          "blueprint": {"flow": [...]}})
print(r.json())
```

## Bước 5: Output Format
- `rpa_scoring.xlsx` — bảng chấm điểm 5 tiêu chí cho mọi task
- `rpa_top5_proposal.md` — Markdown đề xuất chi tiết top 5 với ROI
- `rpa_roadmap_6months.md` — lộ trình 6 tháng triển khai
- Optional: blueprint JSON sẵn import Make.com
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/RPA/`

## Checklist Trước Khi Giao
- [ ] Mỗi use case có ROI tính bằng VND
- [ ] Có thời gian build estimate (giờ dev)
- [ ] Đề xuất tool có giá rõ ràng
- [ ] Có risk: data security, vendor lock-in
- [ ] Phân loại Quick win (<1 tuần) vs Long term
- [ ] Owner triển khai được chỉ định
