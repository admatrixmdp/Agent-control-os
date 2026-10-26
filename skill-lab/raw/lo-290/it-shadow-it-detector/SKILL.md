---
name: it-shadow-it-detector
description: |
  Phát hiện Shadow IT — phần mềm/SaaS NV tự ý dùng không qua IT: browser extension, ChatGPT cá nhân, Google Drive personal, tools đăng ký bằng thẻ cá nhân được hoàn tiền.
  Kích hoạt khi người dùng nói: "phát hiện shadow IT", "shadow IT detection", "NV dùng tool ngoài kiểm soát", "browser extension audit", "rà soát công cụ không chính thức", "rogue SaaS", "unauthorized apps", "AI tool NV tự dùng", "audit ChatGPT cá nhân công ty", "data leak qua tool ngoài".
  Output là báo cáo risk Markdown + danh sách action.
---

# Shadow IT Detector

## Mục Tiêu
Shadow IT chiếm 30-50% chi phí IT thực tế và là nguồn rò rỉ data lớn nhất (NV upload file công ty lên ChatGPT cá nhân, dùng Google Drive cá nhân). Skill này giúp IT phát hiện & xử lý có hệ thống.

## Khi Nào Dùng
- Mới về làm Head of IT, muốn biết "iceberg dưới mặt nước"
- Phát hiện file công ty xuất hiện trên Google Drive cá nhân
- Audit ISO/SOC 2 yêu cầu inventory toàn bộ SaaS
- Sau khi triển khai DLP, cần tinh chỉnh dựa vào shadow IT
- Sau khi AI bùng nổ (ChatGPT, Claude), cần policy AI use

## Bước 1: Định Nghĩa Shadow IT Trong Bối Cảnh Công Ty
Phân 4 loại:
1. **SaaS không qua duyệt** — NV tự đăng ký Notion/Trello cá nhân, đẩy data công việc lên
2. **Browser Extension** — extension đọc được mọi trang, có khả năng exfil data
3. **AI Tools** — ChatGPT, Claude, Gemini cá nhân; NV paste data nhạy cảm
4. **Storage cá nhân** — Drive cá nhân, Dropbox cá nhân, USB

## Bước 2: Phương Pháp Phát Hiện
**A. Phân tích DNS/Proxy logs**
- Pull log từ firewall/proxy 30 ngày
- Đếm top domains nhân viên truy cập
- Filter category "Productivity / AI / Storage" không có trong whitelist
- Ví dụ phát hiện: 47 NV vào chatgpt.com trung bình 2h/ngày

**B. Audit Browser Extension**
- Triển khai Chrome Browser Cloud Management (free)
- Pull list extension cài đặt từng máy
- Cross-check blacklist extension đã biết exfil data

**C. Email/CC Statement Mining**
- Search inbox NV: "welcome to", "receipt for", "verify your account"
- Search statement thẻ cá nhân hoàn tiền: subscription <$50/month
- Đối chiếu với inventory SaaS chính thức → cái nào không match = shadow

**D. SSO Logs**
- Pull Okta/Google login logs
- App nào có login nhưng không trong portfolio chính thức → shadow

**E. AI Tool Detection**
- Audit token usage: NV paste >X ký tự vào ChatGPT/Claude
- Network signature: openai.com, claude.ai, gemini.google.com

## Bước 3: Đánh Giá Rủi Ro Mỗi Shadow IT
Chấm 3 trục:
- **Data Sensitivity** (0-5): tool có khả năng đụng PII/financial/IP không
- **Usage Scale** (0-5): bao nhiêu NV dùng, bao lâu/ngày
- **Vendor Trust** (0-5): có SOC 2 không, vendor uy tín không

Risk score = D × U × (5-T). >40 = critical, 20-40 = high, <20 = medium.

## Bước 4: Hành Động Theo Risk Tier
- **Critical** — block ngay, gọi NV làm việc, education
- **High** — sanction: mua phiên bản enterprise, đưa vào portfolio chính thức
- **Medium** — monitor, ra policy cho phép có điều kiện
- **Low** — ignore, focus tài nguyên khác

Ví dụ: ChatGPT cá nhân (risk score 45) → mua ChatGPT Enterprise, ép NV dùng, block chat.openai.com cá nhân.

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: scan có file chia sẻ ra ngoài domain không
- Gmail MCP: search inbox tìm "welcome to <SaaS>" 
- Slack MCP: bot khảo sát "tool gì team đang dùng"
- Notion MCP: track shadow IT register
- Linear MCP: tạo ticket xử lý từng case shadow IT
- WebSearch: tra reputation của tool, vendor lạ
- WebFetch: pull privacy policy của tool, đánh giá risk

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Lấy danh sách extension cài qua Chrome Browser Cloud Management
from googleapiclient.discovery import build
service = build('chromemanagement', 'v1', credentials=creds)
result = service.customers().reports().countInstalledApps(
    customer="customers/my_customer",
    pageSize=100,
    orderBy="install_count desc"
).execute()
for app in result.get("installedApps", []):
    print(app["appId"], app["displayName"], app["installCount"])
```

## Bước 6: Output Format
- File chính: `Shadow_IT_Report_<YYYYMM>.md`
- `Shadow_IT_Register.xlsx` — bảng tất cả phát hiện kèm risk score
- `AI_Tool_Usage_Audit.md` — riêng AI tools (ChatGPT/Claude/Gemini)
- `Action_Plan_<YYYYMM>.md` — action theo risk tier
- Policy đề xuất: `AI_Acceptable_Use_Policy.md`
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/shadow-it/`

## Checklist Trước Khi Giao
- [ ] Đã pull DNS log + SSO log + CC statement
- [ ] Phát hiện ≥20 shadow IT (chuẩn doanh nghiệp 100 NV)
- [ ] Risk score 3 trục cho mỗi shadow
- [ ] Action plan có owner + deadline
- [ ] Có khảo sát NV (anonymous) để hiểu lý do dùng
- [ ] Đề xuất tool thay thế chính thức cho cái phổ biến
- [ ] Trình bày executive: không "đổ lỗi NV" mà focus giải pháp
