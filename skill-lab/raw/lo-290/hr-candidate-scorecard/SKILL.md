---
name: hr-candidate-scorecard
description: |
  Tạo scorecard phỏng vấn (rubric 5 điểm) chấm ứng viên theo competency cho doanh nghiệp Việt Nam, giúp hội đồng phỏng vấn quyết định khách quan, tránh bias cảm tính.
  Kích hoạt khi người dùng nói: "scorecard phỏng vấn", "chấm điểm ứng viên", "rubric phỏng vấn", "đánh giá ứng viên", "interview scorecard", "biểu mẫu chấm phỏng vấn", "rubric 5 điểm tuyển dụng", "form chấm phỏng vấn", "tổng hợp kết quả phỏng vấn".
  Output là file .xlsx scorecard + báo cáo tổng hợp panel decision.
---

# HR - Scorecard Phỏng Vấn

## Mục Tiêu
Chuyển phỏng vấn từ "cảm thấy ok" sang "chấm điểm có cơ sở". Scorecard giúp panel align trước khi go/no-go, đặc biệt khi 3-5 interviewer có quan điểm khác nhau.

## Khi Nào Dùng
- Sau mỗi vòng phỏng vấn, panel cần ghi nhận
- So sánh 3-5 ứng viên shortlist cho 1 vị trí
- Phỏng vấn cấp Manager+ cần Calibration meeting
- Audit chất lượng quyết định tuyển sau 6-12 tháng

## Bước 1: Định Nghĩa Rubric 5 Điểm
Quy ước thống nhất:
- **5 - Xuất sắc**: Vượt xa kỳ vọng, có thể coach người khác
- **4 - Tốt**: Đáp ứng vững, có ví dụ cụ thể
- **3 - Đạt**: Đủ năng lực cơ bản
- **2 - Yếu**: Thiếu, cần training nhiều
- **1 - Không đạt**: Lệch hoàn toàn

Quan trọng: mỗi mức phải có **mô tả hành vi** (behavior anchor), tránh chấm cảm tính.
Ví dụ Leadership-5: "Đã dẫn team ≥ 10 người, có 2 case scale lên gấp đôi trong 12 tháng".

## Bước 2: Xây Bảng Trọng Số Theo Vị Trí
Vd Marketing Manager:
| Competency | Weight |
|---|---|
| Strategy Thinking | 25% |
| Data-driven | 20% |
| Team Leadership | 20% |
| Execution | 15% |
| Communication | 10% |
| Culture Fit | 10% |

Tổng 100%. Điểm cuối = Σ (score × weight).
Ngưỡng pass thường ≥ 3.5/5 với manager, ≥ 3.0 với staff.

## Bước 3: Quy Trình Chấm + Calibration
1. Mỗi interviewer chấm **độc lập** ngay sau phỏng vấn (không bàn trước)
2. Submit vào Google Sheets / ATS trong 24h
3. Họp Calibration 30': review case có chênh lệch ≥ 1.5 điểm
4. Đưa ra quyết định: Strong Hire / Hire / No Hire / Strong No Hire
5. Ghi rõ lý do, lưu hồ sơ ứng viên

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Gmail MCP: gửi scorecard link cho panel ngay sau phỏng vấn
- Calendar MCP: đặt lịch Calibration meeting
- Drive MCP: lưu scorecard mỗi ứng viên 1 file riêng
- Sheets MCP: dashboard tổng hợp điểm trung bình các vòng

**Fallback bằng API (nếu dùng ATS):**
```python
# Push scorecard vào BambooHR / Greenhouse
import requests
data = {"candidate_id": cid, "interviewer": "An",
        "scores": {"strategy": 4, "data": 5, "leadership": 3},
        "overall": "Hire", "notes": notes}
requests.post(f"https://api.bamboohr.com/api/gateway.php/{COMPANY}/v1/applicant_tracking/scorecards",
    json=data, auth=(API_KEY, "x"))
```

## Bước 5: Output Format
- File `.xlsx` 3 sheet: Rubric | Scorecard từng ứng viên | Summary Panel
- Sheet Summary có chart so sánh điểm các ứng viên
- Mục Final Recommendation: Strong Hire / Hire / Hold / No Hire
- Lưu tại: `/outputs/Scorecard_<vi-tri>_<ten-UV>.xlsx`

## Checklist Trước Khi Giao
- [ ] Mỗi competency có behavior anchor 5 mức
- [ ] Tổng weight = 100%
- [ ] Có cột Notes/Evidence bắt buộc điền
- [ ] Có quy tắc ngưỡng pass rõ ràng
- [ ] Có ô Final Recommendation
- [ ] Đã align trước với hiring manager
- [ ] Tuân thủ quy định chống phân biệt đối xử
