---
name: fin-monthly-closing-checklist
description: |
  Lập checklist đóng sổ kế toán tháng theo lộ trình 10 ngày làm việc cho doanh nghiệp SME Việt Nam,
  phân công rõ task - người phụ trách - deadline - chứng từ kèm. Trigger phrases: "đóng sổ tháng",
  "checklist closing", "month-end close", "kế toán cuối tháng", "lịch closing", "quy trình đóng sổ",
  "T+5 closing", "fast close", "khoá sổ kế toán", "checklist cuối tháng". Output là file Excel
  checklist + HTML dashboard tiến độ.
---

# Checklist Đóng Sổ Kế Toán Tháng (10 ngày)

## Mục Tiêu
Giúp Kế toán trưởng đóng sổ tháng nhanh - không sót bút toán - không bị kiểm toán bắt lỗi.
Chuẩn hoá quy trình "fast close" T+10 cho SME Việt Nam (chuyển dần xuống T+5).

## Khi Nào Dùng
- Đầu tháng mới cần lên kế hoạch close tháng trước
- Onboard kế toán viên mới cần training quy trình
- Doanh nghiệp đang chậm close (>15 ngày), muốn rút xuống 10 ngày
- Chuẩn bị kiểm toán giữa kỳ/cuối năm

## Bước 1: Thu Thập Thông Tin Doanh Nghiệp
Hỏi user:
- Quy mô (số giao dịch/tháng): <500, 500-2000, >2000
- Phần mềm kế toán: MISA, FAST, Bravo, SAP, QuickBooks, Xero
- Có chi nhánh không? Có công ty con không?
- Tháng đang close là tháng mấy? Hôm nay ngày bao nhiêu?

## Bước 2: Build Master Checklist 60-80 Task
Chia theo 4 cụm chính:

**Cụm A - Thu/Chi/Ngân hàng (Ngày 1-2):**
- Đối soát sao kê ngân hàng 100% tài khoản
- Hạch toán phí ngân hàng, lãi tiền gửi
- Kiểm kê quỹ tiền mặt thực tế

**Cụm B - Doanh thu & AR (Ngày 3-4):**
- Đối chiếu doanh thu sàn TMĐT (Shopee/Lazada/Tiki)
- Xuất hoá đơn còn thiếu, phát hành e-invoice
- AR aging, dự phòng phải thu khó đòi

**Cụm C - Chi phí & AP (Ngày 5-7):**
- Hạch toán toàn bộ hoá đơn đầu vào trước 5/T+1
- Cut-off chi phí dồn tích (accruals): điện, nước, lương, BHXH
- Khấu hao TSCĐ, phân bổ CCDC, chi phí trả trước
- Đối chiếu công nợ NCC top 20

**Cụm D - Báo cáo & Review (Ngày 8-10):**
- Lập BS, P&L, CF
- Variance analysis vs ngân sách
- Trình KTT review, ký duyệt
- Lock kỳ kế toán, backup database

## Bước 3: Phân Công & Tracking
Mỗi task có 5 trường:
| Task | Owner | Deadline | Chứng từ kèm | Status |

Status: NotStarted / InProgress / Done / Blocked. Mỗi sáng họp standup 15 phút review tiến độ.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Tạo file checklist sống, share team cùng tick
- Gmail MCP: Gửi daily reminder cho owner task chưa Done
- Google Calendar MCP: Tạo block lịch "Closing Day 1-10"
- WebSearch: Tra Thông tư 200/133 khi có nghiệp vụ mới

**Fallback bằng API:**
```python
# Gọi MISA SME API lấy danh sách bút toán chưa duyệt
import requests
headers = {"Authorization": f"Bearer {MISA_TOKEN}"}
r = requests.get(
    "https://api.misa.vn/sme/v1/journal-entries",
    params={"status": "draft", "period": "2026-05"},
    headers=headers
)
pending = r.json()["data"]
print(f"Còn {len(pending)} bút toán chưa duyệt")
```

## Bước 5: Output Format
1. **Excel checklist** (`closing_checklist_T05_2026.xlsx`): 4 sheet (A/B/C/D), conditional formatting đỏ-vàng-xanh theo trạng thái, cột deadline tự highlight nếu trễ.
2. **HTML dashboard** (`closing_progress.html`): Progress bar % hoàn thành theo ngày, biểu đồ donut số task Done/Pending/Blocked, top 5 task đang blocker.
3. **PDF SOP** (`SOP_Closing_v1.pdf`): Bản chính thức trình BGĐ phê duyệt.

Lưu vào: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/closing/`

## Checklist Trước Khi Giao
- [ ] Đã ghi rõ owner cho từng task (không để trống)
- [ ] Đã ghi deadline cụ thể theo ngày (không ghi "tuần 1")
- [ ] Đã liệt kê chứng từ cần kèm cho mỗi task
- [ ] Đã phân bổ workload đều (không 1 người gánh >40%)
- [ ] Dashboard hiển thị realtime, share quyền view cho BGĐ
- [ ] Có cơ chế escalation khi task Blocked >24h
