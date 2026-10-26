---
name: hr-perf-review-template
description: |
  Tạo template đánh giá hiệu suất NV cho doanh nghiệp Việt Nam, kết hợp KPI kết quả + Competency hành vi, theo chu kỳ quý/nửa năm/năm, gắn với tăng lương và thưởng.
  Kích hoạt khi người dùng nói: "đánh giá hiệu suất", "performance review", "perf review", "biểu mẫu đánh giá NV", "template đánh giá", "review cuối năm", "đánh giá nhân sự", "phiếu đánh giá", "PA review", "annual review template".
  Output là file .xlsx form đánh giá + .docx hướng dẫn manager + slide tổng hợp Calibration.
---

# HR - Template Đánh Giá Hiệu Suất

## Mục Tiêu
Cung cấp framework đánh giá hiệu suất nhất quán toàn công ty, vừa định lượng (KPI) vừa định tính (competency), làm cơ sở cho tăng lương, thưởng, bổ nhiệm, PIP.

## Khi Nào Dùng
- Đánh giá cuối quý/nửa năm/năm
- Lập cycle Performance Management lần đầu
- Sau khi triển khai OKR cần đo ngược lại con người
- Trước mùa tăng lương (Tháng 1, Tháng 7)

## Bước 1: Chọn Mô Hình Đánh Giá
Phổ biến ở VN:
- **9-box Grid** (Performance × Potential): cho Manager+
- **KPI 70% + Competency 30%**: cho staff
- **OKR Self-review + Manager-review**: cho team agile
- **Continuous Feedback** (check-in hàng tháng): cho công ty tech

Chọn 1 mô hình, áp dụng nhất quán.

## Bước 2: Cấu Trúc Form Đánh Giá
**Phần A - Thông tin** (Họ tên, vị trí, manager, kỳ đánh giá)

**Phần B - KPI/OKR (70%)**
| KPI | Target | Actual | % Đạt | Score (1-5) |
|---|---|---|---|---|
| Doanh số quý | 2 tỷ | 2.4 tỷ | 120% | 5 |
| Tỷ lệ giữ chân KH | 85% | 88% | 103% | 4 |

**Phần C - Competency (30%)**
6-8 năng lực: Ownership, Customer Focus, Collaboration, Innovation, Communication, Execution, Leadership, Learning Agility. Mỗi mục chấm 1-5 kèm ví dụ.

**Phần D - Self-Reflection**
- 3 thành tựu nổi bật
- 3 điểm cần cải thiện
- Hỗ trợ cần từ manager
- Mục tiêu kỳ tới

**Phần E - Manager Comments + Final Rating**
- Tổng score = 70% KPI + 30% Competency
- Rating: Outstanding (≥4.5) / Exceeds (4-4.5) / Meets (3-4) / Below (2-3) / Unsatisfactory (<2)

## Bước 3: Quy Trình Calibration
1. NV self-review (5 ngày)
2. Manager review + 1-1 (3 ngày)
3. Skip-level review (manager của manager) - 2 ngày
4. **Calibration meeting** giữa các Director: tránh inflation
5. Phân phối rating cuối: ~10% Outstanding, 25% Exceeds, 55% Meets, 8% Below, 2% Unsat (forced curve nhẹ)
6. Manager deliver feedback + ghi nhận sign-off

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Gmail MCP: gửi form đánh giá + nhắc deadline
- Calendar MCP: book 1-1 review meeting toàn công ty
- Sheets MCP: master dashboard rating phân phối theo phòng ban
- Drive MCP: lưu hồ sơ đánh giá từng NV
- WebSearch: tra benchmark rating distribution (Mercer, Talentnet VN)

**Fallback bằng API (HRIS):**
```python
# Push rating vào BambooHR / MISA HRM
import requests
for emp in employees:
    requests.post(f"https://api.bamboohr.com/api/gateway.php/{CO}/v1/employees/{emp.id}/tables/performance",
        json={"date": "2026-12-31", "rating": emp.final_rating,
              "kpi_score": emp.kpi, "competency_score": emp.comp},
        auth=(API_KEY, "x"))
```

## Bước 5: Output Format
- File `.xlsx` Performance Review Form (4 sheet: Form, KPI, Competency, Summary)
- File `.docx` Manager Guide cách chấm + sample feedback
- File `.pptx` Calibration deck (rating distribution, outliers)
- Email template gửi NV thông báo kết quả
- Lưu tại: `/outputs/PerfReview_<NV>_<Q-YYYY>.xlsx`

## Checklist Trước Khi Giao
- [ ] KPI có target con số rõ
- [ ] Competency có behavior anchor 5 mức
- [ ] Tỷ trọng KPI/Competency cộng = 100%
- [ ] Có self-review trước
- [ ] Có Calibration meeting
- [ ] Rating phân phối hợp lý (không inflation)
- [ ] Manager đã training cách feedback
- [ ] Gắn rating với tăng lương/thưởng theo công thức
