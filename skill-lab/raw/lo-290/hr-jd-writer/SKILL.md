---
name: hr-jd-writer
description: |
  Viết Job Description (mô tả công việc) chuẩn cho doanh nghiệp Việt Nam, đầy đủ Role - Responsibilities - Qualifications - Success Metrics, tối ưu cho job board (TopCV, VietnamWorks, LinkedIn).
  Kích hoạt khi người dùng nói: "viết JD", "mô tả công việc", "tuyển vị trí", "đăng tin tuyển dụng", "tạo bản mô tả công việc", "JD cho vị trí X", "soạn mô tả vị trí", "viết tin tuyển dụng", "job description tiếng Việt", "JD chuẩn".
  Output là file .docx + bản markdown sẵn copy lên TopCV/LinkedIn.
---

# HR - Viết Job Description Chuẩn

## Mục Tiêu
Giúp HR/Trưởng phòng viết JD chuyên nghiệp, thu hút ứng viên đúng năng lực, đồng thời làm rõ kỳ vọng để giảm rủi ro tuyển sai. JD vừa là công cụ marketing tuyển dụng vừa là cơ sở pháp lý đính kèm HĐLĐ.

## Khi Nào Dùng
- Mở vị trí tuyển dụng mới (chưa có JD)
- Cập nhật JD cũ đã lỗi thời sau tái cấu trúc
- Chuẩn hóa JD trước khi đăng job board / agency
- Làm phụ lục HĐLĐ cho NV mới
- Viết JD cho headhunter/recruiter săn ứng viên cấp cao

## Bước 1: Thu Thập Thông Tin Vị Trí
Hỏi hiring manager 6 câu cốt lõi:
1. Tên vị trí + cấp bậc (Junior/Senior/Lead/Manager)
2. Báo cáo cho ai, quản lý ai
3. 3 mục tiêu lớn nhất trong 6-12 tháng đầu
4. Ngân sách lương (range gross) + benefit
5. Phải có (must-have) vs Tốt nếu có (nice-to-have)
6. Văn hóa team + lý do nên gia nhập

Ví dụ: "Marketing Manager báo cáo CMO, quản lý 5 NV, mục tiêu tăng leads 40% trong 6 tháng, lương 25-35 triệu gross + thưởng KPI quý."

## Bước 2: Soạn JD Theo Cấu Trúc 7 Phần
1. **Giới thiệu công ty** (3-4 dòng): quy mô, ngành, tăng trưởng
2. **Tóm tắt vai trò** (Role Summary, 2-3 câu)
3. **Trách nhiệm chính** (5-8 bullet, dùng động từ mạnh: lập, dẫn dắt, tối ưu)
4. **Yêu cầu năng lực** (must-have: 4-6 mục; nice-to-have: 2-3 mục)
5. **Thước đo thành công** (Success Metrics) - 3-5 KPI rõ con số
6. **Quyền lợi** (lương, thưởng, BHXH, 13/14 tháng, phụ cấp, WFH)
7. **Cách ứng tuyển** + deadline

Ngôn ngữ: chủ động, ngắn, tránh sáo rỗng kiểu "năng động sáng tạo".

## Bước 3: Tối Ưu SEO Tuyển Dụng
- Đặt keyword vị trí ở dòng đầu (vd: "Marketing Manager - Hà Nội")
- Nêu rõ địa điểm, hình thức làm việc (Onsite/Hybrid/Remote)
- Nêu khoảng lương (tăng 30% lượt apply theo data TopCV)
- Tag công nghiệp/skill (vd: #Performance #B2B #SaaS)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Gmail MCP: gửi JD cho hiring manager duyệt, gửi cho agency
- Drive MCP: lưu JD vào folder "Tuyển dụng 2026"
- WebSearch: tra benchmark lương vị trí trên TopCV Salary, ITviec Report
- WebFetch: tải JD mẫu của công ty cùng ngành để tham khảo cấu trúc

**Fallback bằng API (nếu cần đăng tự động):**
```python
# Đăng JD lên TopCV qua API (hoặc LinkedIn Jobs API)
import requests
payload = {
    "title": "Marketing Manager",
    "location": "Ha Noi",
    "salary_min": 25000000, "salary_max": 35000000,
    "description_html": jd_html,
    "expiry_days": 30
}
r = requests.post("https://api.topcv.vn/v1/jobs",
    json=payload, headers={"Authorization": f"Bearer {TOKEN}"})
```

## Bước 5: Output Format
- File `.docx` theo template công ty (logo, font Times/Arial 11)
- Bản markdown để copy lên TopCV/VietnamWorks/LinkedIn
- Bản tiếng Anh nếu vị trí cần (Tech/Senior)
- Lưu tại: `/outputs/JD_<vi-tri>_<YYYY-MM>.docx`

## Checklist Trước Khi Giao
- [ ] Tên vị trí + cấp bậc rõ ràng
- [ ] Có khoảng lương (gross hoặc net ghi rõ)
- [ ] Trách nhiệm dùng động từ mạnh, không trùng lặp
- [ ] Must-have ≤ 6 mục (tránh đuổi ứng viên)
- [ ] Success Metrics có con số cụ thể
- [ ] Benefit nêu rõ BHXH/BHYT/BHTN theo luật + extra
- [ ] Có deadline + email/link ứng tuyển
- [ ] Hiring manager đã duyệt trước khi đăng
