---
name: fin-petty-cash-control
description: |
  Kiểm soát quỹ tiền mặt (petty cash) - quy trình lập quỹ, chi, kiểm kê hàng ngày, tránh
  thất thoát. Trigger phrases: "quỹ tiền mặt", "petty cash", "kiểm kê quỹ",
  "quản lý tiền mặt", "imprest fund", "biên bản kiểm kê quỹ", "tồn quỹ thực tế",
  "phiếu chi tiền mặt", "thủ quỹ", "cash count". Output là Excel sổ quỹ + biên bản
  kiểm kê PDF.
---

# Kiểm Soát Quỹ Tiền Mặt (Petty Cash)

## Mục Tiêu
Quản lý quỹ tiền mặt theo nguyên tắc imprest fund - định mức cố định, mỗi lần bổ sung
bằng đúng số đã chi. Tránh thất thoát, gian lận, mâu thuẫn giữa thủ quỹ và kế toán.

## Khi Nào Dùng
- Setup quỹ tiền mặt cho công ty mới / chi nhánh mới
- Hàng ngày cuối giờ kiểm kê quỹ
- Định kỳ tuần / tháng kiểm kê đột xuất
- Khi đổi thủ quỹ (bàn giao)
- Trước kiểm toán cuối năm

## Bước 1: Thiết Lập Quỹ (Imprest)
**Định mức quỹ:**
- Tính nhu cầu chi tiền mặt bình quân/tuần × 1.5 = định mức
- Ví dụ: cần 50tr/tuần → quỹ 75tr
- Quá ngưỡng phải gửi NH ngay (tránh rủi ro)

**Phân cấp duyệt chi:**
- Chi < 500k: thủ quỹ tự duyệt (theo PChi sẵn)
- 500k - 5tr: Trưởng phòng + KTT
- 5tr - 20tr: KTT + Giám đốc
- > 20tr: phải chuyển khoản

**Chứng từ:**
- Phiếu chi tiền mặt mẫu 02-TT (có số sê-ri, ngày, người nhận, MTD, nội dung, số tiền)
- HĐ/chứng từ gốc kèm

## Bước 2: Quy Trình Chi Tiền Mặt
1. Người đề nghị viết Đề nghị tạm ứng / thanh toán
2. Trưởng phòng duyệt
3. KTT duyệt
4. Kế toán thanh toán lập phiếu chi
5. Thủ quỹ chi tiền + người nhận ký
6. Cuối ngày thủ quỹ:
   - Cộng tổng chi, tổng thu
   - So tồn cuối = tồn đầu + thu - chi
   - Đếm tiền thực tế khớp tồn sổ
   - Lập biên bản kiểm kê quỹ ngày

## Bước 3: Kiểm Kê Định Kỳ
**Hàng ngày (thủ quỹ tự):**
- Đếm tiền cuối ngày
- Khớp với sổ quỹ
- Lưu biên bản kiểm kê ngày

**Hàng tuần (KTT):**
- Kiểm kê đột xuất, không báo trước
- Đối chiếu toàn bộ phiếu chi trong tuần

**Hàng tháng (Hội đồng kiểm kê):**
- 3 người: KTT, thủ quỹ, đại diện BGĐ
- Lập biên bản kiểm kê chính thức
- Phát hiện chênh: lập biên bản xử lý

**Bút toán xử lý chênh:**
- Thừa quỹ: Nợ 111 / Có 338 (chờ xử lý) hoặc 711 (thu khác)
- Thiếu quỹ: Nợ 138 (truy thu thủ quỹ) hoặc 632/811 (nếu có lý do)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Sổ quỹ sống cho thủ quỹ điền, KTT view realtime
- Google Drive MCP: Lưu ảnh phiếu chi, biên bản kiểm kê có chữ ký
- Gmail MCP: Auto-gửi BGĐ tồn quỹ cuối ngày, alert khi vượt định mức
- Google Calendar MCP: Đặt lịch kiểm kê đột xuất ngẫu nhiên

**Fallback bằng API:**
```python
# Auto-sync sổ quỹ vào MISA/FAST qua API
import requests
daily_entries = [
    {"date": "2026-05-28", "type": "OUT", "amount": 800_000,
     "voucher": "PC2605/01", "desc": "Mua VPP",
     "account_dr": "6427", "account_cr": "111"},
    {"date": "2026-05-28", "type": "OUT", "amount": 2_500_000,
     "voucher": "PC2605/02", "desc": "Tiếp khách",
     "account_dr": "6428", "account_cr": "111"}
]
for entry in daily_entries:
    requests.post(
        "https://api.misa.vn/sme/v1/journal-entries",
        json=entry,
        headers={"Authorization": f"Bearer {TOKEN}"}
    )
```

## Bước 5: Output Format
1. **Excel sổ quỹ** (`cash_book_T05_2026.xlsx`): Sheet "Daily" sổ quỹ hàng ngày, "Vouchers" danh sách phiếu chi/thu, "InventoryCheck" log kiểm kê.
2. **PDF biên bản kiểm kê** (`cash_count_28052026.pdf`): Mẫu 08-TT, có chỗ ký 3 bên.
3. **HTML dashboard** (`cash_dashboard.html`): Line chart tồn quỹ 30 ngày, gauge tồn hiện tại vs định mức, table phiếu chi gần nhất.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/cash/`

## Checklist Trước Khi Giao
- [ ] Tồn quỹ thực tế = tồn quỹ sổ
- [ ] Phiếu chi 100% có chữ ký người nhận + KTT + GĐ (nếu >5tr)
- [ ] Không có phiếu chi >20tr trong tháng (vi phạm policy)
- [ ] Đã tách bạch quỹ chính - quỹ tạm ứng - quỹ ngoại tệ
- [ ] Camera quan sát khu vực để tiền nếu >100tr
- [ ] Backup file sổ quỹ hàng ngày
