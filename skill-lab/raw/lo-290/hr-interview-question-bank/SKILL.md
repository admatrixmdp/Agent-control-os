---
name: hr-interview-question-bank
description: |
  Tạo ngân hàng câu hỏi phỏng vấn theo vị trí và competency (năng lực) cho doanh nghiệp Việt Nam, gồm câu hỏi kỹ thuật, behavioral (STAR), tình huống, và culture fit.
  Kích hoạt khi người dùng nói: "câu hỏi phỏng vấn", "bộ câu hỏi tuyển dụng", "interview question bank", "câu hỏi STAR", "phỏng vấn năng lực", "câu hỏi cho vị trí X", "bank câu hỏi HR", "soạn câu hỏi phỏng vấn", "interview guide".
  Output là file .xlsx + bản .docx Interview Guide cho hội đồng phỏng vấn.
---

# HR - Ngân Hàng Câu Hỏi Phỏng Vấn

## Mục Tiêu
Chuẩn hóa quy trình phỏng vấn để mọi ứng viên cùng vị trí được đánh giá công bằng, tránh phỏng vấn "tâm tình" mất thời gian. Bộ câu hỏi gắn với competency model để dễ scoring sau này.

## Khi Nào Dùng
- Tuyển vị trí mới, chưa có bộ câu hỏi chuẩn
- Phỏng vấn vòng kỹ thuật/manager/culture fit
- Training panel phỏng vấn cho leader mới
- Audit chất lượng phỏng vấn của các phòng ban

## Bước 1: Xác Định Competency Cần Đánh Giá
Liệt kê 5-7 năng lực cốt lõi cho vị trí, vd Sales Manager:
- Leadership (dẫn dắt team)
- Negotiation (đàm phán B2B)
- Data-driven thinking
- Customer empathy
- Vietnamese market knowledge
- Coaching skill
- Resilience under pressure

Mỗi competency cần 3-5 câu hỏi để cross-check.

## Bước 2: Soạn Câu Hỏi Theo 4 Loại
**A. Behavioral (STAR) - 40%**
"Kể về một lần bạn dẫn team vượt KPI khó. Tình huống? Hành động? Kết quả con số?"

**B. Tình huống (Case) - 25%**
"Sếp giao bạn ra mắt sản phẩm mới ở Đà Nẵng trong 60 ngày, ngân sách 200 triệu. Bạn sẽ làm gì 30 ngày đầu?"

**C. Kỹ thuật - 25%**
Vd Dev: "Giải thích trade-off giữa SQL index và write performance"
Vd Sales: "Bạn dùng công thức nào tính LTV/CAC?"

**D. Culture Fit + Motivation - 10%**
"Vì sao bạn rời công ty cũ?", "Môi trường nào khiến bạn làm tốt nhất?"

## Bước 3: Gán Câu Hỏi Theo Vòng Phỏng Vấn
- **Vòng 1 (HR screening, 30')**: motivation, expectation lương, deal-breaker
- **Vòng 2 (Hiring manager, 60')**: behavioral + tình huống
- **Vòng 3 (Technical/Panel, 60-90')**: kỹ thuật, case
- **Vòng 4 (Culture fit + C-level, 30')**: long-term goal, values

Mỗi vòng có 6-10 câu hỏi chính + 2-3 câu probe (đào sâu).

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Gmail MCP: gửi Interview Guide cho panel
- Calendar MCP: tạo invite phỏng vấn kèm link guide
- Drive MCP: lưu bank câu hỏi sharing với hiring manager
- WebSearch: tham khảo câu hỏi mẫu Google, Glassdoor cho vị trí tương tự

**Fallback bằng API (nếu cần sync ATS):**
```python
# Sync vào Greenhouse/Workable ATS
import requests
for q in question_bank:
    requests.post("https://api.greenhouse.io/v1/interview_kits",
        json={"job_id": JOB_ID, "questions": q},
        auth=(API_KEY, ""))
```

## Bước 5: Output Format
- File `.xlsx` 4 sheet: Competency Map | Behavioral | Case | Technical
- File `.docx` Interview Guide in giấy cho panel (1 trang/vòng)
- Có cột Notes để interviewer ghi nhanh
- Lưu tại: `/outputs/InterviewBank_<vi-tri>.xlsx`

## Checklist Trước Khi Giao
- [ ] Mỗi competency có ≥ 3 câu hỏi
- [ ] Tỷ lệ Behavioral/Case/Tech/Culture = 40/25/25/10
- [ ] Không có câu hỏi vi phạm luật (tôn giáo, hôn nhân, mang thai)
- [ ] Có gợi ý "câu trả lời tốt" để interviewer chấm
- [ ] Đã chia câu hỏi theo từng vòng
- [ ] Có version tiếng Anh nếu phỏng vấn senior
