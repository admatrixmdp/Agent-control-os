---
name: it-asset-inventory
description: |
  Quản lý sổ tài sản IT của doanh nghiệp Việt Nam: laptop, desktop, màn hình, license phần mềm, thiết bị mạng, máy chủ — kèm cấp phát, thu hồi, bảo hành, khấu hao.
  Kích hoạt khi người dùng nói: "sổ tài sản IT", "quản lý laptop công ty", "asset inventory", "danh sách thiết bị IT", "quản lý license phần mềm", "theo dõi thiết bị nhân viên", "IT asset register", "kiểm kê thiết bị IT", "CMDB nhẹ", "tracking license SaaS".
  Output là Excel/Google Sheet có công thức + dashboard.
---

# IT Asset Inventory Manager

## Mục Tiêu
Tạo một sổ tài sản IT duy nhất (single source of truth) giúp IT Manager biết: ai đang giữ thiết bị gì, license nào còn hạn, máy nào sắp hết bảo hành, khấu hao bao nhiêu — thay vì rải rác trong nhiều file Excel cá nhân.

## Khi Nào Dùng
- Công ty trên 20 NV, IT bắt đầu loạn không biết laptop ở đâu
- Cần báo cáo tài sản IT cho Kế toán/Kiểm toán
- Audit license phần mềm (Microsoft, Adobe, Autodesk) tránh phạt
- Lên kế hoạch refresh laptop 3-4 năm/lần
- Mua bảo hiểm thiết bị, cần list chi tiết

## Bước 1: Định Nghĩa Loại Tài Sản
Phân loại thành 5 nhóm:
1. **Endpoint** — laptop, desktop, tablet, smartphone
2. **Peripheral** — màn hình, bàn phím, chuột, dock, headset
3. **Network** — router, switch, AP, firewall, modem
4. **Server & Storage** — server vật lý, NAS, cloud VM
5. **License & SaaS** — Microsoft 365, Adobe, Figma, Slack, Notion, GitHub

## Bước 2: Thiết Kế Cột Tracking
Cột bắt buộc cho mỗi tài sản:
- Asset ID (LAP-001, MON-045, LIC-SW-012)
- Loại / Brand / Model / Serial Number
- Cấu hình (CPU/RAM/SSD nếu là máy)
- Ngày mua / Giá / Nhà cung cấp / Số hóa đơn
- Bảo hành đến / Hết khấu hao
- Tình trạng (Đang dùng / Kho / Sửa chữa / Thanh lý)
- Người giữ (HR ID, tên, phòng ban)
- Ngày cấp phát / Ngày thu hồi
- Ghi chú (lỗi đã sửa, va đập, MAC address)

## Bước 3: Tự Động Tính Khấu Hao & Cảnh Báo
Công thức Sheet:
- Khấu hao 36 tháng (laptop) / 48 tháng (server): `=Giá*(1-(TODAY()-NgàyMua)/(36*30.5))`
- Sắp hết bảo hành <30 ngày: tô đỏ
- License sắp hết hạn <60 ngày: thông báo
- Máy không cấp cho ai >30 ngày: cảnh báo "tài sản đang nằm im"

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: file master inventory, share read-only cho Kế toán/HR
- Google Drive MCP: lưu hóa đơn PDF gắn link vào từng asset
- Slack MCP: bot cảnh báo "Laptop LAP-023 hết bảo hành 15 ngày nữa"
- Notion MCP: trang asset của mỗi NV để họ tự xem
- Linear MCP: tạo ticket khi cần thu hồi/cấp mới
- WebFetch: tra cứu giá trị thị trường model cũ khi thanh lý

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Sync inventory lên Google Sheets
import gspread
gc = gspread.service_account(filename='key.json')
sh = gc.open("IT_Asset_Inventory")
ws = sh.worksheet("Endpoints")
# Append một asset mới
ws.append_row(["LAP-024", "Dell", "Latitude 5440", "SN12345",
               "i5/16GB/512GB", "2025-01-15", 22000000, "FPT Shop",
               "HD-2025-001", "2028-01-15", "Đang dùng", "EMP-089"])
```

## Bước 5: Output Format
- File chính: `IT_Asset_Inventory_<YYYYMM>.xlsx` (5 sheet: Endpoint/Peripheral/Network/Server/License)
- Dashboard sheet: tổng số máy, % đang dùng, giá trị còn lại, top 5 phòng ban dùng nhiều
- Báo cáo PDF hàng quý gửi CFO
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/it-asset/`

## Checklist Trước Khi Giao
- [ ] Mỗi asset có Asset ID duy nhất
- [ ] Cột bảo hành & khấu hao có công thức tự tính
- [ ] Có cột "Người giữ" link với danh sách NV
- [ ] Cảnh báo hết bảo hành tô màu tự động
- [ ] Dashboard tổng quan trên 1 sheet
- [ ] Có sheet License riêng với số seat, ngày renew
- [ ] Backup file mỗi tháng
