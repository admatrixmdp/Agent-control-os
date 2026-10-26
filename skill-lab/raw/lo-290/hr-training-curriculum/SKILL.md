---
name: hr-training-curriculum
description: |
  Soạn curriculum (chương trình đào tạo) chi tiết cho khóa nội bộ doanh nghiệp Việt Nam, gồm learning objective, module, slide outline, hoạt động, đánh giá theo Kirkpatrick.
  Kích hoạt khi người dùng nói: "soạn curriculum", "thiết kế khóa đào tạo", "outline khóa học", "training program design", "soạn chương trình đào tạo", "lesson plan", "course design", "thiết kế nội dung training", "khung khóa học", "tạo giáo án".
  Output là file .docx Curriculum + .pptx slide outline + bài tập + checklist trainer.
---

# HR - Soạn Curriculum Khóa Đào Tạo

## Mục Tiêu
Chuyển từ "trainer kể chuyện" sang "khóa học có outcome đo được". Curriculum tốt giúp ai dạy cũng đảm bảo chất lượng, dễ scale, dễ revamp.

## Khi Nào Dùng
- Phát triển khóa nội bộ mới (Leadership, Sales, Onboarding)
- Tái cấu trúc khóa cũ hiệu quả thấp
- Train-the-Trainer cho lực lượng L&D nội bộ
- Tạo curriculum cho mentor/coach chương trình

## Bước 1: Định Nghĩa Learning Objective (LO)
Dùng Bloom's Taxonomy:
- **Remember**: nhớ định nghĩa, công thức
- **Understand**: giải thích bằng lời mình
- **Apply**: dùng trong tình huống mới
- **Analyze**: phân tách thành phần
- **Evaluate**: đánh giá quyết định
- **Create**: tạo sản phẩm mới

LO viết theo công thức "Sau khóa, học viên có thể [động từ Bloom] + [nội dung] + [tiêu chí đánh giá]".
Ví dụ: "Sau khóa, NV Sales có thể THỰC HIỆN cuộc gọi cold call đạt tỷ lệ qualify ≥ 30%".

3-5 LO cho khóa 1-2 ngày. Mỗi LO gắn ≥ 1 module + 1 cách đánh giá.

## Bước 2: Cấu Trúc Curriculum (Module)
Format cho khóa 8 giờ:
| Module | Thời lượng | LO | Hoạt động | Tài liệu |
|---|---|---|---|---|
| M1: Mindset bán hàng | 60' | LO1 | Mini case + thảo luận nhóm | Slide 1-15 |
| M2: SPIN Selling framework | 90' | LO2 | Demo + role-play | Slide 16-30, Handbook ch.1 |
| M3: Đối phó từ chối | 90' | LO3 | Thực hành cặp đôi | Card từ chối thực tế |
| M4: Closing techniques | 60' | LO4 | Video phân tích | Video clip |
| M5: Action Plan cá nhân | 60' | LO5 | Cá nhân viết + share | Worksheet |

Tỷ lệ activity: 30% giảng - 50% thực hành - 20% thảo luận.

## Bước 3: Đánh Giá Theo Kirkpatrick 4 Levels
- **L1 - Reaction**: survey cuối khóa (5 câu, NPS ≥ 8)
- **L2 - Learning**: pre/post test, role-play assessment (đạt ≥ 80%)
- **L3 - Behavior**: 30/60/90 ngày sau, observe có áp dụng?
- **L4 - Results**: KPI business thay đổi sau 3-6 tháng (vd conversion rate +15%)

Pre/post test 10-15 câu. Role-play có rubric chấm. L3-L4 cần manager theo dõi.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Drive MCP: lưu curriculum master + version control
- Gmail MCP: gửi pre-test + chuẩn bị trước khóa
- Calendar MCP: lịch khóa + follow-up sessions
- WebSearch: tra best practice course từ Coursera, Harvard, FUNiX, BAC
- WebFetch: tải curriculum sample các trường

**Fallback bằng API (LMS):**
```python
# Push lên LMS nội bộ (Moodle / Docebo)
import requests
course = {
    "title": "Sales Excellence 8H",
    "modules": modules_json,
    "duration_hours": 8,
    "pre_test_id": 101, "post_test_id": 102,
    "target_audience": ["sales_l3", "sales_l4"]
}
requests.post("https://lms.company.vn/api/courses", json=course,
    headers={"Authorization": f"Bearer {TOKEN}"})
```

## Bước 5: Output Format
- File `.docx` Curriculum 12-20 trang (LO, module, activity, đánh giá)
- File `.pptx` Slide outline 30-50 slide
- File `.docx` Trainer Guide (script + tips)
- File `.docx` Participant Workbook
- Bộ pre/post test (Google Form)
- Bài đánh giá L1 Survey
- Lưu tại: `/outputs/Curriculum_<ten-khoa>_<YYYY>.docx`

## Checklist Trước Khi Giao
- [ ] Có 3-5 LO chuẩn Bloom
- [ ] Mỗi LO gắn module + cách đánh giá
- [ ] Tỷ lệ activity 30/50/20 (giảng/thực hành/thảo luận)
- [ ] Có pre/post test
- [ ] Plan L3/L4 follow-up 30/60/90 ngày
- [ ] Trainer Guide đủ script để người mới dạy được
- [ ] Có Participant Workbook
- [ ] Đã pilot với 5-10 NV trước khi launch
