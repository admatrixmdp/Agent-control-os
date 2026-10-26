---
name: hr-engagement-survey
description: |
  Thiết kế và phân tích Employee Engagement Survey cho doanh nghiệp Việt Nam, gồm eNPS, 8-12 driver gắn kết, câu hỏi mở; trả về dashboard và action plan theo phòng ban.
  Kích hoạt khi người dùng nói: "engagement survey", "khảo sát gắn kết", "eNPS", "khảo sát nhân viên", "đo lường gắn kết", "employee survey", "khảo sát hài lòng NV", "pulse survey", "annual employee survey", "đo mức độ hài lòng".
  Output là form khảo sát + báo cáo .pdf + dashboard HTML + action template cho từng phòng ban.
---

# HR - Survey Gắn Kết Nhân Viên (eNPS)

## Mục Tiêu
Đo "nhiệt độ" tổ chức một cách định lượng, phát hiện vấn đề trước khi NV nghỉ. eNPS đơn giản dễ benchmark; survey full giúp đi sâu các driver.

## Khi Nào Dùng
- Annual survey cuối năm
- Pulse check quý (10-12 câu ngắn)
- Sau sự kiện lớn (M&A, layoff, lãnh đạo mới)
- Audit văn hóa trước IPO/funding round

## Bước 1: Chọn Format Survey
- **Pulse (5-10 phút)**: 10-15 câu, hằng quý
- **Annual Full (15-20 phút)**: 40-60 câu + open-ended, 1 lần/năm
- **eNPS Only**: 1 câu chính + 2 câu mở

eNPS câu chính: "Bạn có khả năng giới thiệu công ty cho bạn bè làm việc?" thang 0-10. 
- Promoter 9-10, Passive 7-8, Detractor 0-6.
- eNPS = %Promoter - %Detractor. VN benchmark trung bình ~ 10-30.

## Bước 2: Thiết Kế Bộ Câu Hỏi (40-50 câu)
Theo 10 driver chính:
1. Lãnh đạo (Leadership)
2. Manager trực tiếp
3. Đồng nghiệp + Collaboration
4. Cơ hội phát triển + Learning
5. Lương thưởng + Recognition
6. Work-life balance + Wellbeing
7. Văn hóa + Values
8. Truyền thông nội bộ
9. Resources + Tools
10. Career growth + Promotion

Mỗi driver 3-5 câu thang Likert 5 mức. Thêm 3 câu mở:
- "Điều gì khiến bạn yêu công ty nhất?"
- "Một thay đổi bạn muốn thấy năm tới?"
- "Lý do nào sẽ khiến bạn nghỉ?"

## Bước 3: Triển Khai + Phân Tích
1. Đảm bảo ẩn danh (dùng tool bên thứ 3, không lưu email)
2. Truyền thông trước: CEO video kêu gọi tham gia
3. Mở survey 7-10 ngày, gửi nhắc 2 lần
4. Target response rate ≥ 75%
5. Phân tích:
   - Score trung bình từng driver
   - So sánh phòng ban / level / thâm niên
   - eNPS overall + segmented
   - Theme từ câu mở (gom nhóm topic modeling)
   - Identify top 3 drivers và bottom 3

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Gmail MCP: gửi link survey cho toàn NV, nhắc 2 lần
- Sheets MCP: master data từ survey raw
- Slack MCP: bot nhắc tham gia survey
- Drive MCP: lưu report final cho leadership
- WebSearch: benchmark eNPS VN từ Anphabe, FlexJobs

**Fallback bằng API (Survey tools):**
```python
# Pull data từ SurveyMonkey / Qualtrics
import requests
r = requests.get(f"https://api.surveymonkey.com/v3/surveys/{ID}/responses/bulk",
    headers={"Authorization": f"Bearer {TOKEN}"})
df = pd.DataFrame(r.json()["data"])
# Tính eNPS, driver score, phân tích theme câu mở
```

## Bước 5: Output Format
- File `.docx` Survey instrument (40-50 câu)
- File `.pdf` Executive Report 20-25 trang
- Dashboard `.html` interactive (driver score, heatmap phòng ban)
- File `.pptx` action plan theo phòng ban (mỗi phòng 3 action)
- Email kết quả gửi toàn công ty (transparency)
- Lưu tại: `/outputs/EngagementSurvey_<YYYY>.pdf`

## Checklist Trước Khi Giao
- [ ] Đảm bảo ẩn danh thực sự
- [ ] eNPS chính + 10 driver phụ
- [ ] Có ≥ 3 câu mở
- [ ] Response rate target ≥ 75%
- [ ] Phân tích segmented (dept, level, tenure)
- [ ] Báo cáo có Top 3 + Bottom 3 driver
- [ ] Mỗi phòng ban có ≥ 3 action commit
- [ ] Lịch follow-up sau 6 tháng
- [ ] CEO chia sẻ kết quả công khai
