---
name: hr-promotion-package
description: |
  Soạn hồ sơ đề bạt thăng chức cho NV tại doanh nghiệp Việt Nam, gồm achievement, business impact, leadership readiness, future role; chuẩn để trình hội đồng promotion.
  Kích hoạt khi người dùng nói: "đề bạt", "thăng chức", "promotion package", "hồ sơ thăng chức", "promote NV", "đề xuất thăng tiến", "promotion case", "trình hội đồng promotion", "đề bạt cấp manager", "thăng cấp NV".
  Output là file .docx promotion case + .pptx slide trình hội đồng + scorecard panel chấm.
---

# HR - Hồ Sơ Đề Bạt Thăng Chức

## Mục Tiêu
Chuẩn hóa quy trình đề bạt, đảm bảo công bằng + có cơ sở. Tránh tình trạng "sếp nói thì lên" hoặc "ai ngồi lâu thì lên". Hồ sơ tốt giúp panel quyết định nhanh, NV mới hiểu tại sao mình hoặc đồng nghiệp được lên.

## Khi Nào Dùng
- Promotion cycle định kỳ (2 lần/năm: T1, T7)
- Spot promotion cho top performer
- Thăng chức gắn với tái cấu trúc (vd Team Lead → Manager)
- Tạo lộ trình cho high-potential

## Bước 1: Tiêu Chí Eligibility
NV phải đạt:
- Thâm niên tối thiểu ở level hiện tại (vd 18-24 tháng)
- Rating ≥ Exceeds Expectation 2 chu kỳ gần nhất
- Compa-ratio hiện tại < ngưỡng (vẫn còn room band trên)
- Có readiness "ready now" (không phải "ready in 12 months")
- Không trong PIP/kỷ luật

## Bước 2: Cấu Trúc Promotion Case 5 Phần
**1. Tổng quan NV** (1 trang)
- Họ tên, vị trí hiện tại, thâm niên, manager
- Đề xuất level mới + lý do timing

**2. Achievement & Impact** (2 trang)
- 3-5 thành tựu lớn nhất 12-24 tháng qua
- Mỗi thành tựu: Situation - Task - Action - Result (STAR)
- Quantify: revenue, cost saved, efficiency %, NPS
- Ví dụ: "Dẫn dự án X tiết kiệm 1.2 tỷ/năm, được CEO ghi nhận tại all-hands T6/2025"

**3. Leadership Readiness** (1 trang)
- Đã coach/mentor bao nhiêu người, kết quả?
- Đã làm stretch assignment ở scope cao hơn?
- Feedback 360 (nếu có)
- Behavior tiêu biểu thể hiện level mới

**4. Future Role** (1 trang)
- Mô tả role mới, scope, team size, budget
- 3-6-12 tháng đầu sẽ làm gì?
- Risk + mitigation (nếu fail, kế hoạch?)

**5. Compensation Adjustment** (0.5 trang)
- Lương hiện tại vs band mới
- Đề xuất tăng (thường 10-20% promotion + thưởng one-time)
- Total comp năm mới

Tổng hồ sơ 5-7 trang. Kèm bằng chứng đính kèm.

## Bước 3: Quy Trình Trình Hội Đồng
1. Manager submit case → HRBP review form
2. Skip-level manager đọc, sign-off
3. Promotion Panel: HR Head + 2-3 Director cross-function
4. Mỗi case trình 15-20 phút (5 phút manager pitch, 10' Q&A, 5' panel chấm)
5. Quyết định: Approved / Hold / Reject
6. Thông báo NV trong 7 ngày, công bố nội bộ
7. Hiệu lực thường đầu Q kế tiếp

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Drive MCP: lưu hồ sơ promotion (confidential)
- Calendar MCP: book Promotion Panel meeting
- Gmail MCP: gửi case + slide cho panel đọc trước
- Sheets MCP: master promotion candidates tracker
- WebSearch: benchmark promotion rate ngành (Talentnet 10-15%)

**Fallback bằng API (HRIS update):**
```python
# Update HRIS sau khi approve
import requests
update = {
    "employee_id": EID,
    "new_level": "M2",
    "new_title": "Senior Marketing Manager",
    "new_base_salary": 65_000_000,
    "effective_date": "2026-07-01"
}
requests.put(f"https://api.bamboohr.com/api/gateway.php/{CO}/v1/employees/{EID}",
    json=update, auth=(API_KEY, "x"))
```

## Bước 5: Output Format
- File `.docx` Promotion Case 5-7 trang
- File `.pptx` Slide trình panel (10 slide)
- File `.xlsx` Scorecard panel chấm
- File `.docx` Letter thông báo (cho NV)
- File `.xlsx` Comp Adjustment Calculator
- Lưu tại: `/outputs/Promotion_<NV>_<YYYY-Q>.docx`

## Checklist Trước Khi Giao
- [ ] NV đáp ứng eligibility
- [ ] Achievement có ≥ 3 ví dụ STAR + quantify
- [ ] Có evidence Leadership Readiness
- [ ] Future role rõ scope + 3-6-12 plan
- [ ] Comp adjustment trong band mới
- [ ] Skip-level manager đã sign-off
- [ ] Slide trình panel ≤ 10 slide
- [ ] Có plan thông báo + công bố
- [ ] Calibration cross-function tránh bias
