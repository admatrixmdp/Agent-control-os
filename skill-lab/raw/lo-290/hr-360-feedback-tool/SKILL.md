---
name: hr-360-feedback-tool
description: |
  Triển khai công cụ feedback 360 độ cho doanh nghiệp Việt Nam, thu thập từ peer/manager/direct report/khách hàng, ẩn danh, kết quả ra theme và action plan.
  Kích hoạt khi người dùng nói: "feedback 360", "360 review", "đánh giá 360 độ", "phản hồi đa chiều", "survey 360", "đánh giá peer", "feedback đa chiều", "khảo sát 360", "360 degree feedback", "evaluation 360".
  Output là file .xlsx survey template + báo cáo cá nhân .pdf + .pptx Development Plan.
---

# HR - Công Cụ Feedback 360 Độ

## Mục Tiêu
Cho NV (đặc biệt Manager+) nhìn được "blind spot" qua góc nhìn của peer, sếp, cấp dưới. Khác với perf review (kết quả), 360 tập trung vào **hành vi và phong cách làm việc**.

## Khi Nào Dùng
- Chu kỳ Development Cycle nửa năm
- Bổ nhiệm Manager / Director mới sau 6-12 tháng
- Coaching cấp cao (1-on-1 executive coaching)
- Audit văn hóa lãnh đạo

## Bước 1: Chọn Đối Tượng + Người Đánh Giá
- **Đối tượng**: Manager+ hoặc top performer staff
- **Người đánh giá** (8-12 người):
  - 1 Manager trực tiếp
  - 3-5 Peer (cùng cấp)
  - 3-5 Direct report (nếu là Manager)
  - 1-2 Stakeholder cross-team
  - 1 Self-assessment

Quy tắc ẩn danh: kết quả gộp theo nhóm (vd "Peer trung bình 3.8"), không lộ ai chấm gì, trừ Manager.

## Bước 2: Thiết Kế Bộ Câu Hỏi (25-35 mục)
Theo 5 cụm năng lực Lãnh đạo:
1. **Self-Awareness** (5 câu): biết điểm mạnh/yếu, quản lý cảm xúc
2. **Relationship** (6 câu): lắng nghe, tin cậy, conflict resolution
3. **Execution** (6 câu): set priority, follow through, accountability
4. **Strategic Thinking** (5 câu): big picture, decision making
5. **Coaching & Development** (6 câu): phát triển team, feedback
6. **Open-ended** (3 câu): "Nên TIẾP TỤC làm gì?", "BẮT ĐẦU làm gì?", "DỪNG làm gì?"

Thang đo 1-5 (Strongly Disagree - Strongly Agree). Tránh câu hỏi mơ hồ.

## Bước 3: Quy Trình Triển Khai 4 Tuần
- Tuần 1: NV chọn nominators, HR review
- Tuần 2: Gửi survey ẩn danh, deadline 7 ngày
- Tuần 3: HR/Coach phân tích, tạo report cá nhân
- Tuần 4: Debrief 1-1 với coach (90'), lập Individual Development Plan (IDP)

Báo cáo có: heat map 5 cụm, gap Self vs Others, top 3 strength, top 3 development area, raw comments.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Gmail MCP: gửi survey link ẩn danh cho 10 người
- Sheets MCP: master tổng hợp điểm theo nhóm rater
- Drive MCP: lưu report cá nhân với quyền chỉ NV + coach xem
- Calendar MCP: book debrief 90' với coach
- WebSearch: benchmark 360 báo cáo từ Center for Creative Leadership

**Fallback bằng API (survey tools):**
```python
# Tích hợp Typeform / SurveyMonkey
import requests
form = {"title": f"360 Feedback for {employee_name}",
        "questions": questions_list,
        "anonymous": True}
r = requests.post("https://api.typeform.com/forms", json=form,
    headers={"Authorization": f"Bearer {TOKEN}"})
# Sau thu kết quả -> aggregate by rater_group
```

## Bước 5: Output Format
- File `.xlsx` Survey template + Aggregation logic
- File `.pdf` Báo cáo cá nhân 8-12 trang (chỉ NV + coach + sếp xem)
- File `.pptx` Individual Development Plan 6 tháng tiếp
- Email Confidentiality Notice gửi rater
- Lưu tại: `/outputs/360_<NV>_<H-YYYY>.pdf`

## Checklist Trước Khi Giao
- [ ] ≥ 8 rater, đủ 4 nhóm
- [ ] Bộ câu hỏi ≤ 35 mục, 5 cụm năng lực
- [ ] Có 3 câu open-ended Continue/Start/Stop
- [ ] Quy trình ẩn danh được giải thích rõ
- [ ] Báo cáo chỉ NV + coach + sếp trực tiếp xem
- [ ] Có IDP cụ thể với 3 action 6 tháng
- [ ] Có lịch follow-up sau 3 và 6 tháng
- [ ] Tuân thủ quyền riêng tư dữ liệu cá nhân (Nghị định 13/2023)
