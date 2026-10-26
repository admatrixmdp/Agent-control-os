---
name: hr-bonus-plan-design
description: |
  Thiết kế chương trình thưởng cuối năm cho doanh nghiệp Việt Nam: lương tháng 13, thưởng KPI cá nhân, thưởng theo profit-share công ty, thưởng team, gắn rating và pool.
  Kích hoạt khi người dùng nói: "thiết kế thưởng cuối năm", "bonus plan", "thưởng tháng 13", "thưởng KPI", "profit share", "thưởng Tết", "đề xuất thưởng", "bonus structure", "kế hoạch thưởng", "thưởng năm".
  Output là file .xlsx Bonus Calculator + .docx Bonus Policy + simulation 3 scenarios.
---

# HR - Thiết Kế Chương Trình Thưởng

## Mục Tiêu
Biến thưởng từ "chuyện sếp quyết" thành công thức minh bạch gắn 3 yếu tố: (1) công ty đạt mục tiêu, (2) phòng ban đạt KPI, (3) cá nhân đạt rating. Vừa motivate vừa kiểm soát ngân sách.

## Khi Nào Dùng
- Q4 lập kế hoạch thưởng năm tới
- Sau khi chốt P&L năm, phân bổ bonus pool thực tế
- Thiết kế thưởng cho team Sales (theo công thức riêng)
- Trình BOD/CEO duyệt cơ chế

## Bước 1: Xác Định Cấu Trúc Thưởng
Mô hình 4 lớp:
1. **Lương tháng 13** (1 tháng cố định, gắn thâm niên) - bắt buộc giữ chân
2. **Bonus Pool công ty** = % × Lợi nhuận sau thuế (vd 5-10%)
3. **Phân bổ Pool theo phòng ban** dựa trên KPI phòng ban đạt
4. **Phân bổ cá nhân** dựa trên Performance Rating

Công thức cá nhân:
```
Bonus = Base × Target% × Company Multiplier × Dept Multiplier × Individual Multiplier
```

Ví dụ: Base 30tr × 200% target × 1.1 (công ty vượt 10%) × 1.0 (phòng đạt) × 1.2 (rating Exceeds) = 79.2tr

## Bước 2: Đặt Target Bonus % Theo Level
| Level | Target Bonus (% lương năm) |
|---|---|
| Junior/Mid (L3-L4) | 10-15% |
| Senior/Lead (L5) | 15-25% |
| Manager (M1-M2) | 25-40% |
| Director (D1+) | 40-60% |
| Sales | 30-100% (variable cao) |
| C-level | 50-100% + LTI/Equity |

## Bước 3: Multiplier Theo Rating
| Rating | Multiplier |
|---|---|
| Outstanding | 1.5x - 2.0x |
| Exceeds | 1.2x - 1.4x |
| Meets | 0.9x - 1.1x |
| Below | 0.3x - 0.6x |
| Unsatisfactory | 0x (không thưởng) |

Tổng phân bổ phải = Bonus Pool đã duyệt (zero-sum game).

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Sheets MCP: Bonus Calculator real-time với input rating + P&L
- Gmail MCP: gửi thư thông báo bonus cá nhân (confidential)
- Drive MCP: lưu Bonus Pool allocation per dept
- Calendar MCP: lịch thông báo + ngày chi (thường trước Tết 7 ngày)
- WebSearch: tra benchmark Bonus % VN (Talentnet, Mercer Total Reward)

**Fallback bằng API (Payroll):**
```python
# Push số bonus vào MISA AMIS Payroll
import requests
for emp in employees:
    bonus = base * target_pct * co_mult * dept_mult * ind_mult
    requests.post("https://api.amis.misa.vn/v1/payroll/bonus",
        json={"employee_id": emp.id, "amount": bonus,
              "type": "annual", "pay_date": "2026-01-25"},
        headers={"Authorization": f"Bearer {TOKEN}"})
```

## Bước 5: Output Format
- File `.xlsx` Bonus Calculator (input rating + P&L → output cá nhân)
- File `.docx` Bonus Policy 6-8 trang
- File `.xlsx` Simulation 3 scenarios (P&L 80%/100%/120%)
- File `.pptx` deck trình CEO + BOD
- Mẫu thư bonus cá nhân (mailmerge)
- Lưu tại: `/outputs/BonusPlan_<congty>_<YYYY>.xlsx`

## Checklist Trước Khi Giao
- [ ] Có lương tháng 13 cố định (text quan trọng giữ NV)
- [ ] Bonus Pool % gắn với P&L
- [ ] Có Target Bonus % theo level
- [ ] Multiplier theo rating công bằng
- [ ] Tổng allocation = Bonus Pool (không overshoot)
- [ ] Có simulation tối thiểu 3 scenarios
- [ ] Tính thuế TNCN cho bonus (cộng tháng chi)
- [ ] CEO + CFO đã sign-off
- [ ] Ngày chi rõ (thường 25-29 Tết âm)
