---
name: it-onboarding-it-checklist
description: |
  Tạo checklist IT onboarding cho nhân viên mới: cấp account email, VPN, MFA, Slack, máy laptop, license phần mềm, đào tạo bảo mật — đảm bảo ngày đầu NV vào là sẵn sàng làm việc.
  Kích hoạt khi người dùng nói: "checklist onboarding IT", "cấp tài khoản nhân viên mới", "IT onboarding", "setup máy cho NV mới", "tài khoản email VPN cho người mới", "quy trình IT nhận việc", "new hire IT", "onboard nhân sự mới IT", "day one setup", "chuẩn bị IT cho người mới".
  Output là checklist Markdown + ticket Linear/Jira tự động.
---

# IT Onboarding Checklist Generator

## Mục Tiêu
Đảm bảo nhân viên mới có đủ công cụ làm việc 100% ngay ngày đầu — không còn cảnh "vào tuần thứ 2 mới có Slack". Đồng thời giúp IT giảm 70% thời gian thủ công nhờ checklist + automation.

## Khi Nào Dùng
- Có batch tuyển dụng mới (đặc biệt fresher onboard hàng loạt)
- Setup IT cho Manager/CXO cấp cao (cần ưu tiên & nhiều quyền)
- Onboard remote worker (cần ship máy, VPN, MFA từ xa)
- Onboard contractor/freelancer (cần limit quyền, hết hạn account)
- Chuẩn hoá quy trình IT đang làm "tự phát"

## Bước 1: Thu Thập Thông Tin NV Mới
Hỏi HR đầu vào:
- Họ tên, mã NV, phòng ban, chức danh, line manager
- Ngày bắt đầu, hợp đồng chính thức/thử việc/contractor
- Cấp bậc (Junior/Mid/Senior/Manager/Lead/Director)
- Vị trí làm việc (HCM/HN/remote/hybrid)
- Tool đặc thù theo job (Designer cần Figma, Dev cần GitHub, Sales cần CRM)

## Bước 2: Sinh Checklist Theo 4 Nhóm
**A. Tài khoản & Quyền (T-3 ngày trước onboard)**
- [ ] Tạo email công ty (firstname.lastname@company.vn)
- [ ] Tạo account Microsoft 365 / Google Workspace + cấp license
- [ ] Add vào AD/Okta group theo phòng ban
- [ ] Bật MFA bắt buộc
- [ ] Tạo VPN account
- [ ] Add Slack/Teams + invite các channel mặc định

**B. Thiết bị (T-1 ngày)**
- [ ] Chuẩn bị laptop (cài OS, Office, antivirus, MDM enroll)
- [ ] Mã hoá ổ đĩa (BitLocker/FileVault)
- [ ] Cài VPN client, Slack, Zoom, browser company profile
- [ ] In tờ "tài khoản tạm thời" + bắt buộc đổi pass lần đầu
- [ ] Chuẩn bị màn hình, dock, headset, túi laptop

**C. Quyền theo job (Day 0)**
- [ ] License phần mềm chuyên môn (Figma/Adobe/GitHub Copilot)
- [ ] Truy cập Google Drive folder phòng ban
- [ ] Notion/Confluence workspace
- [ ] CRM/HRM nếu là Sales/HR

**D. Đào tạo bảo mật (Day 1)**
- [ ] Ký Acceptable Use Policy
- [ ] Học khóa security awareness (30')
- [ ] Test phishing simulation

## Bước 3: Tự Động Hoá Tạo Ticket
Mỗi mục trong checklist → tạo 1 sub-task trong Linear/Jira/Asana với:
- Assignee: IT Admin phụ trách
- Due date: T-3, T-1, Day 0
- Label: `onboarding`, `priority-high`
- Parent ticket: "Onboard <Tên NV> <Ngày start>"

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Linear MCP: tự tạo project "Onboarding {Tên NV}" + 20 sub-tasks
- Slack MCP: gửi welcome message vào DM + invite channel
- Google Drive MCP: tạo folder cá nhân NV mới, share quyền
- Notion MCP: clone template onboarding page cho NV
- Gmail MCP: gửi email welcome kèm tài khoản tạm thời
- WebSearch: tra hướng dẫn enroll MDM theo loại máy

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tạo user Google Workspace
from googleapiclient.discovery import build
service = build('admin', 'directory_v1', credentials=creds)
user = {"name": {"givenName": "Nam", "familyName": "Nguyen"},
        "password": "TempP@ssw0rd!", "primaryEmail": "nam.nguyen@company.vn",
        "orgUnitPath": "/Marketing", "changePasswordAtNextLogin": True}
service.users().insert(body=user).execute()
```

## Bước 5: Output Format
- File chính: `Onboarding_Checklist_<TênNV>_<NgàyStart>.md`
- Template tổng: `IT_Onboarding_Master_Template.md`
- File Excel tracking nhiều NV onboarding cùng lúc
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/onboarding-it/`

## Checklist Trước Khi Giao
- [ ] Checklist chia rõ T-3, T-1, Day 0, Day 1
- [ ] Có assignee cụ thể cho từng item
- [ ] Tài khoản email format chuẩn công ty
- [ ] MFA bắt buộc bật trước Day 0
- [ ] License phần mềm match job description
- [ ] Có template welcome email & welcome Slack
- [ ] Test thử với 1 NV thật trước khi rollout
