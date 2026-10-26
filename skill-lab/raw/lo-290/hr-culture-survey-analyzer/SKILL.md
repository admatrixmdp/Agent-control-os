---
name: hr-culture-survey-analyzer
description: |
  Phân tích survey văn hoá doanh nghiệp tại Việt Nam, gom theme từ câu mở, đo gap giữa Stated Values vs Lived Values, đề xuất action cho leadership.
  Kích hoạt khi người dùng nói: "phân tích culture survey", "khảo sát văn hoá", "culture assessment", "đo lường văn hoá", "culture diagnostic", "phân tích văn hoá công ty", "values alignment", "khảo sát giá trị", "culture audit", "đánh giá văn hoá DN".
  Output là báo cáo .pdf insights + .pptx action plan cho leadership + heat map theo phòng ban.
---

# HR - Phân Tích Survey Văn Hoá

## Mục Tiêu
Phát hiện gap giữa văn hóa công ty rao giảng (Stated Values) và văn hóa NV trải nghiệm (Lived Values), từ đó đề xuất hành động cụ thể cho leadership thay vì hô hào chung.

## Khi Nào Dùng
- Annual culture audit
- Sau M&A cần hợp nhất văn hóa
- Trước/sau khi launch values mới
- Khi turnover bất thường hoặc engagement giảm

## Bước 1: Thiết Kế Bộ Câu Hỏi
Cấu trúc 3 phần:
**A. Stated Values Awareness (5 câu)**
- "Bạn nhớ 5 giá trị cốt lõi công ty?"
- "Giá trị nào bạn thấy được sống nhất / ít nhất?"

**B. Lived Experience (20 câu)**
Mỗi giá trị có 3-4 câu hỏi behavior cụ thể, vd Customer First:
- "Quyết định mới đây của leadership đặt KH lên trước?"
- "Khi conflict KH vs internal, công ty chọn KH?"
- "Bạn có dữ liệu/quyền để giúp KH ngay?"

**C. Open-ended (5 câu)**
- "Mô tả văn hóa công ty bằng 3 từ"
- "Khoảnh khắc nào bạn thấy tự hào / xấu hổ?"
- "Một điều bạn ước thay đổi văn hóa?"
- "Behavior nào bị thưởng dù trái values?"
- "Leader nào sống đúng giá trị nhất?"

## Bước 2: Phân Tích Quantitative
- Score trung bình từng giá trị (1-5)
- Gap = Awareness score - Lived score
- Segment theo phòng ban, level, thâm niên, vùng (HN/HCM)
- Outliers: phòng ban score thấp/cao bất thường
- Trend so với năm trước (nếu có)

Heat map matrix: Giá trị (cột) × Phòng ban (dòng), màu đỏ = gap lớn.

## Bước 3: Phân Tích Qualitative (Câu Mở)
Quy trình:
1. Tổng hợp raw text (anonymize)
2. Topic modeling / coding theo theme (5-8 theme chính)
3. Đếm tần suất theme
4. Cherry-pick quote tiêu biểu (giữ ẩn danh)
5. Cross-check với quant data

Theme phổ biến trong DN VN:
- Gap giữa "Innovation" rao giảng vs "Sếp luôn đúng"
- Gap "Customer First" vs KPI doanh số ép
- Gap "Work-life balance" vs văn hóa OT
- Gap "Meritocracy" vs quan hệ thân tín
- "Văn hóa gia đình" trở thành mặt nạ né khó khăn

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Gmail MCP: phát survey ẩn danh
- Sheets MCP: aggregate raw data
- Drive MCP: lưu báo cáo confidential
- WebSearch: tra culture framework (Denison, Schein, Hofstede VN)
- WebFetch: benchmark Anphabe Best Workplace VN

**Fallback bằng API (NLP analysis):**
```python
# Topic modeling câu mở
import openai
themes = []
for quote in open_ended_quotes:
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user",
                   "content": f"Trích theme văn hóa từ ý kiến NV sau (3-5 từ khóa): {quote}"}]
    )
    themes.append(resp.choices[0].message.content)
# Count frequency + cluster
```

## Bước 5: Output Format
- File `.pdf` Culture Report 25-30 trang (insight, gap, theme)
- File `.html` Heat Map interactive theo phòng ban
- File `.pptx` Action Plan 6-12 tháng cho leadership
- File `.xlsx` Raw data anonymized cho deep dive
- Bản 1-page Executive Summary
- Lưu tại: `/outputs/CultureSurvey_<congty>_<YYYY>.pdf`

## Checklist Trước Khi Giao
- [ ] Survey ẩn danh thực sự
- [ ] Đủ 3 phần: Awareness - Lived - Open
- [ ] Response rate ≥ 70%
- [ ] Có gap analysis Stated vs Lived
- [ ] Theme từ câu mở có quote evidence
- [ ] Heat map by phòng ban
- [ ] Action plan có owner + deadline cụ thể
- [ ] CEO commit follow-through (không để báo cáo nằm tủ)
- [ ] Resurvey 6-12 tháng đo cải thiện
