---
name: hr-training-needs-analysis
description: |
  Phân tích nhu cầu đào tạo (Training Needs Analysis - TNA) theo phòng ban cho doanh nghiệp Việt Nam, gắn skill gap với business goal, ưu tiên ROI và đề xuất chương trình.
  Kích hoạt khi người dùng nói: "phân tích nhu cầu đào tạo", "TNA", "training needs analysis", "khảo sát đào tạo", "skill gap analysis", "kế hoạch đào tạo năm", "training plan", "nhu cầu L&D", "competency gap", "training assessment".
  Output là file .xlsx skill gap matrix + .docx báo cáo TNA + .pptx đề xuất training calendar năm.
---

# HR - Phân Tích Nhu Cầu Đào Tạo (TNA)

## Mục Tiêu
Trả lời câu hỏi: "Năm tới nên đào tạo cái gì, cho ai, ngân sách bao nhiêu để hỗ trợ tốt nhất mục tiêu kinh doanh?". Tránh tình trạng "training cho có" hoặc trùng lặp.

## Khi Nào Dùng
- Q4 lập kế hoạch L&D + budget năm sau
- Sau khi cập nhật chiến lược công ty / OKR
- Khi launch competency framework mới
- Audit hiệu quả chương trình training hiện tại

## Bước 1: Thu Thập Input 4 Nguồn
1. **Top-down (Business strategy)**: OKR công ty/phòng ban năm tới → skill nào cần
2. **Bottom-up (NV)**: Survey 10-15 câu về self-assessed skill gap + nguyện vọng
3. **Manager view**: Đánh giá skill gap của team theo competency framework
4. **Performance data**: KPI miss ở đâu, root cause có phải thiếu skill?

Kết hợp 4 nguồn → priority list, tránh chỉ dựa vào "NV muốn học gì".

## Bước 2: Skill Gap Matrix
Tạo bảng:
| Skill | Current (1-5) | Required (1-5) | Gap | # NV cần | Priority |
|---|---|---|---|---|---|
| Excel nâng cao | 2.5 | 4 | 1.5 | 30 | High |
| Tiếng Anh giao tiếp | 3.0 | 4 | 1.0 | 50 | Medium |
| Negotiation B2B | 2.0 | 4 | 2.0 | 15 | High |
| Data Analytics | 1.5 | 3 | 1.5 | 25 | High |

Cụm theo Job Family + Level. Highlight Top 10 skill gap urgent.

## Bước 3: Đề Xuất Format Training Cho Mỗi Gap
Theo mô hình 70-20-10:
- **70% On-the-job**: rotation, stretch assignment, project shadowing
- **20% Social**: mentoring, coaching, communities of practice
- **10% Formal**: classroom, e-learning, certification

Cho mỗi gap top priority, chọn format phù hợp:
- Skill kỹ thuật (Excel, SQL) → e-learning + bài tập
- Soft skill (Leadership) → workshop + coaching + role-play
- Sản phẩm/Quy trình → On-the-job + SOP
- Tiếng Anh → External course + buddy practice

Tính budget = (số NV) × (chi phí/đầu người) + chi phí phát triển nội dung.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Gmail MCP: gửi TNA survey link cho toàn NV
- Sheets MCP: tổng hợp self + manager rating skill
- Drive MCP: lưu skill matrix + report
- WebSearch: tra giá khóa học VN (TopCV Academy, Coursera, FUNiX, BAC)
- WebFetch: scrape catalog các provider lớn

**Fallback bằng API (LMS):**
```python
# Pull data completion từ Coursera for Business / FUNiX LMS
import requests
r = requests.get(f"https://api.coursera.org/api/businesses.v1/{ORG}/completions",
    headers={"Authorization": f"Bearer {TOKEN}"})
# Cross-check completion vs skill gap
```

## Bước 5: Output Format
- File `.xlsx` Skill Gap Matrix (Job Family × Skill × Gap × Priority)
- File `.docx` TNA Report 15-20 trang
- File `.pptx` Training Plan + Calendar năm
- File `.xlsx` Budget breakdown
- File `.pdf` Catalog đề xuất khóa học/provider
- Lưu tại: `/outputs/TNA_<congty>_<YYYY>.xlsx`

## Checklist Trước Khi Giao
- [ ] Có input từ 4 nguồn (strategy, NV, manager, performance)
- [ ] Skill gap đo bằng scale 1-5
- [ ] Top 10 priority skill rõ
- [ ] Áp dụng 70-20-10
- [ ] Có budget chi tiết
- [ ] Có Training Calendar năm (12 tháng)
- [ ] Có cách đo ROI (Kirkpatrick 4 levels)
- [ ] Manager + Heads of Dept đã đồng thuận
