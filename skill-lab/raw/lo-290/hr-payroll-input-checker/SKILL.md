---
name: hr-payroll-input-checker
description: |
  Kiểm tra input lương trước khi chạy payroll tháng tại doanh nghiệp Việt Nam: chấm công, OT, phép, thưởng, kỷ luật, BHXH, thuế TNCN, phát hiện sai sót trước khi chuyển khoản.
  Kích hoạt khi người dùng nói: "kiểm tra input lương", "payroll check", "check chấm công", "audit payroll", "rà soát lương trước khi chạy", "kiểm tra OT", "soát BHXH TNCN", "validate payroll input", "tiền lương tháng", "rà payroll".
  Output là file .xlsx report sai sót + dashboard variance + checklist sign-off trước chuyển khoản.
---

# HR - Check Input Lương Trước Khi Chạy Payroll

## Mục Tiêu
Phát hiện sai sót đầu vào TRƯỚC khi payroll chạy, tránh phải hoàn lương (rất phiền với thuế TNCN + BHXH) và mất uy tín HR. 1 sai sót lương = 5-10 NV mất niềm tin.

## Khi Nào Dùng
- Hằng tháng, từ ngày 25 chạy check trước khi payroll ngày 1-5
- Sau sự kiện đặc biệt (tăng lương đại trà, sa thải, bonus)
- Audit định kỳ quý/năm
- Sau khi migrate hệ thống payroll

## Bước 1: Liệt Kê Input Cần Check
Checklist 10 mục:
1. **Lương cơ bản (base)**: có thay đổi do tăng lương, promote không?
2. **Chấm công (time)**: số ngày công, ngày phép, ngày nghỉ không lương
3. **OT**: số giờ × hệ số (150% ngày thường, 200% ngày nghỉ, 300% lễ Tết)
4. **Phụ cấp**: ăn trưa, đi lại, điện thoại, chuyên cần
5. **Thưởng**: KPI tháng, hoa hồng sales, thưởng đột xuất
6. **Khấu trừ**: tạm ứng, vi phạm (chỉ khấu trừ hợp pháp), kỷ luật
7. **BHXH/BHYT/BHTN**: tỷ lệ 10.5% NV, mức trần (20 lần lương tối thiểu vùng)
8. **Thuế TNCN**: bậc lũy tiến, giảm trừ bản thân 11tr + người phụ thuộc 4.4tr
9. **NV mới**: prorate theo ngày làm
10. **NV nghỉ**: thanh toán phép chưa dùng, trợ cấp thôi việc nếu đủ điều kiện

## Bước 2: Build Variance Check
So sánh tháng này vs tháng trước cho từng NV:
- Variance > 5% → cần lý do (promote, joiners, leavers, OT bất thường, thưởng)
- Variance > 20% → flag đỏ, manager phải confirm

Bảng output:
| NV | Tháng trước | Tháng này | Variance % | Lý do | OK? |
|---|---|---|---|---|---|
| Nguyễn Văn A | 25tr | 30tr | +20% | Bonus KPI Q1 + OT | ✓ |
| Trần Thị B | 18tr | 12tr | -33% | Nghỉ không lương 8 ngày | ✓ |

## Bước 3: Validate Theo Luật
- Lương thực nhận ≥ Lương tối thiểu vùng 2026 (HN/HCM vùng I: 4.96tr; vùng II: 4.41tr; vùng III: 3.86tr; vùng IV: 3.45tr - cập nhật từ Nghị định)
- OT ≤ 40h/tháng, ≤ 200h/năm (300h cho ngành đặc thù)
- BHXH đóng đúng base (không < lương tối thiểu, không > 20 lần)
- Thuế TNCN tính đúng cho người phụ thuộc đã đăng ký
- Lương nữ thai sản: BHXH chi, công ty không khấu trừ phép

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Sheets MCP: pull chấm công từ máy quét vân tay
- Gmail MCP: gửi báo cáo variance cho manager confirm
- Drive MCP: lưu hồ sơ payroll mỗi tháng (lưu 10 năm theo luật)
- Calendar MCP: lịch chạy payroll cố định
- WebSearch: tra mức lương tối thiểu vùng 2026, thuế TNCN cập nhật

**Fallback bằng API (Payroll system):**
```python
# Cross-check MISA Payroll vs chấm công vân tay
import requests, pandas as pd
payroll = requests.get("https://api.misa.amis.vn/v1/payroll/preview",
    params={"month": "2026-05"},
    headers={"Authorization": f"Bearer {TOKEN}"}).json()
timesheet = pd.read_csv("timesheet_2026-05.csv")

# So sánh số ngày công, OT
merged = pd.DataFrame(payroll).merge(timesheet, on="employee_id")
discrepancy = merged[abs(merged["payroll_days"] - merged["actual_days"]) > 0]
discrepancy.to_excel("variance_2026-05.xlsx")
```

## Bước 5: Output Format
- File `.xlsx` Variance Report (NV nào lệch > 5%)
- File `.xlsx` Compliance Check (BHXH, TNCN, lương min)
- File `.xlsx` Sign-off Sheet (HR Manager + Finance + CEO ký)
- Dashboard `.html` summary KPI payroll (tổng cost, headcount, OT rate)
- File `.docx` Báo cáo phát hiện sai sót + đề xuất
- Lưu tại: `/outputs/PayrollCheck_<YYYY-MM>.xlsx`

## Checklist Trước Khi Giao
- [ ] Đối chiếu chấm công vs hệ thống payroll
- [ ] OT đúng hệ số 150/200/300%
- [ ] BHXH/BHYT/BHTN đúng tỷ lệ + base
- [ ] TNCN tính đúng bậc lũy tiến
- [ ] Người phụ thuộc đã đăng ký + còn hiệu lực
- [ ] Lương min vùng đúng 2026
- [ ] Variance > 5% có lý do
- [ ] Variance > 20% manager đã confirm
- [ ] Sign-off đủ chữ ký HR + Finance + CEO
- [ ] Backup hồ sơ 10 năm (Đ.118 BLLĐ + Luật BHXH)
