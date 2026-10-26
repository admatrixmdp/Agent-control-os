---
name: it-offboarding-it-checklist
description: |
  Tạo checklist IT offboarding chuẩn khi NV nghỉ việc: revoke account, thu hồi thiết bị, audit data, archive email, transfer ownership Google Drive — tránh rò rỉ và mất tài sản.
  Kích hoạt khi người dùng nói: "checklist nghỉ việc IT", "offboarding IT", "thu hồi tài khoản nhân viên", "revoke account", "NV nghỉ thu lại laptop", "offboard nhân sự IT", "exit IT process", "tắt account người nghỉ", "audit data NV nghỉ", "transfer ownership khi nghỉ".
  Output là checklist Markdown + ticket Linear + báo cáo audit.
---

# IT Offboarding Checklist Generator

## Mục Tiêu
Đảm bảo khi NV nghỉ việc: (1) không còn quyền truy cập hệ thống, (2) thu hồi đủ tài sản IT, (3) dữ liệu quan trọng được chuyển giao, (4) audit log lưu lại — phòng tránh rò rỉ data & tranh chấp pháp lý sau này.

## Khi Nào Dùng
- NV chính thức nghỉ việc (resignation/termination)
- NV chuyển phòng ban (cần thu quyền cũ, cấp quyền mới)
- Contractor/freelancer hết hợp đồng
- Sa thải khẩn cấp vì vi phạm (cần revoke ngay lập tức)
- M&A, layoff hàng loạt

## Bước 1: Phân Loại Kịch Bản Offboard
Hỏi HR/Manager:
- **Friendly exit** (NV xin nghỉ, bàn giao bình thường) — quy trình chuẩn
- **Hostile exit** (sa thải, vi phạm) — revoke ngay TRƯỚC khi báo NV
- **Death/medical leave dài** — pause account, không xoá data
- **Internal transfer** — chỉ điều chỉnh quyền, không thu thiết bị

Hỏi thông tin cần:
- Mã NV, phòng ban, line manager, người nhận bàn giao
- Last working day, last login allowed day
- Có laptop/màn hình/headset/SIM/thẻ ra vào nào
- Có quyền admin hệ thống nào không (đặc biệt: AWS root, GitHub org owner)

## Bước 2: Checklist 5 Nhóm
**A. Pre-LWD (trước last working day 3 ngày)**
- [ ] Thông báo IT từ HR (Slack #it-requests + ticket)
- [ ] Xác định người nhận bàn giao
- [ ] Chuẩn bị folder archive

**B. Revoke Account (đúng giờ LWD + 1h)**
- [ ] Disable account AD/Okta (KHÔNG xoá ngay, suspend 90 ngày)
- [ ] Revoke Google Workspace / Microsoft 365 session
- [ ] Tắt VPN, MFA, SSH key, API token
- [ ] Remove khỏi Slack workspace, GitHub org, Linear, Notion
- [ ] Đổi password share account chung mà NV biết
- [ ] Revoke quyền AWS/GCP/Azure (special: root/owner)

**C. Data & Email (LWD → LWD+7)**
- [ ] Set email auto-reply "Tôi đã không còn làm việc, liên hệ X@..."
- [ ] Forward email đến manager 30 ngày
- [ ] Transfer ownership Google Drive sang manager
- [ ] Backup mailbox PST/MBOX lưu archive
- [ ] Transfer Notion pages, Figma files, GitHub repos cá nhân

**D. Thu hồi tài sản vật lý (LWD)**
- [ ] Thu laptop + sạc + chuột/bàn phím + headset
- [ ] Thu màn hình/dock (nếu mượn)
- [ ] Thu SIM công ty, thẻ ra vào, key fob
- [ ] Wipe & re-image laptop về template
- [ ] Cập nhật asset inventory: status = "Kho"

**E. Audit & Đóng hồ sơ (LWD+7)**
- [ ] Báo cáo audit: ngày disable, người thực hiện, signed off
- [ ] Lưu log access 90 ngày cuối của NV
- [ ] Gửi HR xác nhận hoàn tất để chốt lương cuối

## Bước 3: Phối Hợp Với HR & Finance
- HR cung cấp danh sách tài sản đã ký nhận lúc onboard
- Finance đối chiếu giá trị tài sản chưa trả → trừ lương cuối
- Legal review nếu là hostile exit (NDA, non-compete)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Linear MCP: tạo project "Offboarding {Tên NV}" với 25 sub-tasks
- Google Drive MCP: list & transfer ownership file của NV
- Gmail MCP: setup auto-reply, forward, archive mailbox
- Slack MCP: deactivate user, archive DM
- GitHub MCP: remove khỏi org, transfer repo ownership
- Notion MCP: reassign pages của NV cho manager
- WebSearch: tra quy định pháp lý về retention email

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Suspend Google Workspace user + transfer Drive
from googleapiclient.discovery import build
admin = build('admin', 'directory_v1', credentials=creds)
admin.users().update(userKey='nam@company.vn',
                     body={'suspended': True}).execute()
# Transfer Drive ownership
transfer = build('datatransfer', 'datav1', credentials=creds)
transfer.transfers().insert(body={
    "oldOwnerUserId": "OLD_ID", "newOwnerUserId": "MANAGER_ID",
    "applicationDataTransfers": [{"applicationId": "55656082996"}]
}).execute()
```

## Bước 5: Output Format
- File chính: `Offboarding_Checklist_<TênNV>_<LWD>.md`
- Báo cáo audit: `Offboarding_Audit_Report_<TênNV>.pdf` ký xác nhận
- Template master: `IT_Offboarding_Master_Template.md`
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/offboarding-it/`

## Checklist Trước Khi Giao
- [ ] Xác định đúng kịch bản (friendly/hostile)
- [ ] Revoke account đúng giờ LWD không sớm không muộn
- [ ] Transfer Drive/Notion ownership trước khi disable
- [ ] Thu đủ tài sản vật lý, có ký nhận
- [ ] Backup mailbox & lưu log 90 ngày
- [ ] HR + Finance + Legal đều ký xác nhận
- [ ] Update asset inventory chuyển trạng thái về Kho
