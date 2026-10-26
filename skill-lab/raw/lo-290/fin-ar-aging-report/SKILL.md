---
name: fin-ar-aging-report
description: |
  Lập báo cáo AR Aging (tuổi nợ phải thu) theo nhóm 0-30, 31-60, 61-90, >90 ngày,
  tự động cảnh báo công nợ quá hạn và đề xuất hành động thu hồi. Trigger phrases:
  "AR aging", "tuổi nợ", "công nợ quá hạn", "báo cáo công nợ phải thu",
  "phải thu khách hàng", "DSO", "thu hồi công nợ", "khách hàng nợ", "aging khách hàng",
  "dự phòng phải thu khó đòi". Output là Excel aging + HTML dashboard với heat map.
---

# Báo Cáo AR Aging + Cảnh Báo Công Nợ Quá Hạn

## Mục Tiêu
Giúp Sales Admin và Kế toán công nợ thu hồi tiền nhanh hơn - thấy ngay khách nào sắp xấu,
priority theo số tiền x mức độ trễ. Giảm DSO 5-10 ngày = giải phóng cả tỷ tiền lưu động.

## Khi Nào Dùng
- Cuối mỗi tuần / cuối tháng
- Trước khi xét nâng/giảm hạn mức tín dụng khách
- Khi cần lập dự phòng phải thu khó đòi cuối kỳ
- Trước họp với Sales review pipeline công nợ

## Bước 1: Thu Thập Dữ Liệu
Lấy từ phần mềm kế toán/ERP:
- Mã KH, tên KH, người phụ trách (Sales owner)
- Số hoá đơn, ngày phát hành, ngày due, số tiền gốc
- Số đã thu, số còn lại
- Term thanh toán đã thoả thuận (Net 30, Net 60...)

## Bước 2: Phân Loại Tuổi Nợ
Tính `aging_days = today - due_date`:

| Nhóm | Khoảng ngày | Mức rủi ro | Tỷ lệ dự phòng gợi ý |
|------|-------------|------------|----------------------|
| Current | <=0 | Bình thường | 0% |
| 1-30 | 1-30 | Thấp | 1% |
| 31-60 | 31-60 | Trung bình | 5% |
| 61-90 | 61-90 | Cao | 20% |
| 91-180 | 91-180 | Rất cao | 50% |
| >180 | >180 | Khó đòi | 100% |

## Bước 3: Phân Tích & Action Plan
**KPI tổng thể:**
- Tổng AR, % quá hạn, DSO (Days Sales Outstanding)
- Top 10 KH nợ lớn nhất + top 10 nợ lâu nhất
- Concentration risk: KH chiếm >20% AR

**Action plan tự động:**
- Nhóm 1-30: gửi email nhắc nhở mềm
- Nhóm 31-60: gọi điện, escalate cho Sales owner
- Nhóm 61-90: gửi công văn nhắc nợ chính thức, ngưng cấp hàng mới
- Nhóm >90: chuyển pháp lý, ngừng giao dịch

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Đẩy aging table sống cho team Sales tự xem
- Gmail MCP: Auto-gửi mail nhắc nợ KH nhóm 1-30 hàng tuần (có template)
- Google Drive MCP: Lưu công văn nhắc nợ ký số nhóm 61-90
- WebSearch: Tra thông tin doanh nghiệp con nợ trên cổng đăng ký kinh doanh

**Fallback bằng API:**
```python
# Gửi tin nhắn nhắc nợ qua Zalo OA API
import requests
for customer in overdue_31_60:
    requests.post(
        "https://openapi.zalo.me/v3.0/oa/message",
        headers={"access_token": ZALO_TOKEN},
        json={
            "recipient": {"user_id": customer["zalo_id"]},
            "message": {"text": f"Kính gửi {customer['name']}, "
                       f"HĐ {customer['inv']} {customer['amount']:,}đ đã quá hạn "
                       f"{customer['days']} ngày. Vui lòng thanh toán..."}
        }
    )
```

## Bước 5: Output Format
1. **Excel aging** (`AR_aging_W22_2026.xlsx`): Pivot theo KH x bucket, conditional color đỏ-cam-vàng-xanh, sheet "Top10" và sheet "Action".
2. **HTML dashboard** (`ar_dashboard.html`): Heat map KH x aging bucket, donut chart % theo nhóm, table action với button "Mark as called/emailed".
3. **PDF nhắc nợ** mẫu (`reminder_letter_template.pdf`): Sẵn sàng merge mail và in.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/ar/`

## Checklist Trước Khi Giao
- [ ] Tổng AR khớp số dư TK 131 trên sổ cái
- [ ] Đã loại các khoản đã ký gối đầu/đã có cam kết hoãn
- [ ] Mỗi KH quá hạn đều có Sales owner ghi rõ
- [ ] Action plan đã có deadline cụ thể (ngày X gọi, ngày Y công văn)
- [ ] Dashboard share quyền view cho Sales Director
- [ ] Có cơ chế escalate >90 ngày lên CFO/CEO
