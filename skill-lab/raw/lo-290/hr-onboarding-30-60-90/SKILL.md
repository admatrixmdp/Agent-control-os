---
name: hr-onboarding-30-60-90
description: |
  Lập kế hoạch onboarding 30/60/90 ngày cho nhân viên mới tại doanh nghiệp Việt Nam, gồm milestones học - làm - đóng góp theo từng mốc, gắn với manager check-in.
  Kích hoạt khi người dùng nói: "onboarding 30 60 90", "kế hoạch hội nhập NV mới", "plan onboarding", "first 90 days", "lộ trình NV mới", "kế hoạch 30 ngày đầu", "onboarding plan", "kế hoạch NV mới", "hội nhập nhân viên", "ramp-up plan".
  Output là file .xlsx kế hoạch + .docx Welcome Kit + email lịch check-in.
---

# HR - Onboarding 30/60/90 Ngày

## Mục Tiêu
Rút ngắn thời gian NV mới đạt productive từ 6 tháng xuống còn 90 ngày. Giảm tỷ lệ early turnover (NV nghỉ trong 6 tháng đầu) thường lên tới 20-30% ở DN VN.

## Khi Nào Dùng
- NV mới sắp onboard (gửi trước ngày làm 3-5 ngày)
- NV chuyển nội bộ sang phòng ban mới
- Manager mới tiếp quản team
- Audit chất lượng onboarding các phòng ban

## Bước 1: Thu Thập Bối Cảnh Vị Trí
Hỏi hiring manager:
- 3 kết quả mong đợi sau 90 ngày
- Các stakeholder chính NV cần làm việc
- Top 5 tài liệu cần đọc
- Hệ thống công cụ cần access (email, Slack, CRM, HRIS)
- Buddy/Mentor là ai
- Training nội bộ bắt buộc (compliance, security)

## Bước 2: Cấu Trúc 30/60/90 Theo Công Thức LEARN - DO - OWN
**30 ngày đầu - LEARN (Học):**
- Hiểu công ty: lịch sử, OKR, văn hóa, sản phẩm
- Gặp 1-1 với 10 stakeholder chính
- Hoàn thành training compliance + security
- Setup hệ thống công cụ
- Shadow 3 case thực tế
- **Output**: Báo cáo "Quan sát 30 ngày" trình manager

**60 ngày - DO (Làm):**
- Sở hữu 1-2 dự án nhỏ độc lập
- Đóng góp meeting team
- Hoàn thành 1 sáng kiến cải tiến quy trình
- Manager đánh giá giữa kỳ
- **Output**: 1 deliverable cụ thể (campaign, code, deal)

**90 ngày - OWN (Sở hữu):**
- Take ownership KPI tháng
- Pass đánh giá thử việc
- Đề xuất kế hoạch quý tiếp theo
- **Output**: Kế hoạch Q1 cá nhân + cam kết KPI

## Bước 3: Lịch Check-in Bắt Buộc
- Ngày 1: HR welcome + buddy intro (60')
- Ngày 7: Manager 1-1 đầu tiên (30')
- Tuần 2-12: 1-1 với manager hàng tuần (30')
- Ngày 30: Review milestone L (45')
- Ngày 60: Review milestone D (60')
- Ngày 89: Đánh giá thử việc chính thức (90')
- Survey NPS ngày 30, 60, 90 (3 câu ngắn)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Calendar MCP: tự động tạo lịch 6 check-in trong 90 ngày
- Gmail MCP: gửi Welcome Email + lịch tuần 1 trước ngày làm
- Drive MCP: chia sẻ folder "Onboarding Kit" có quyền view
- Slack/Slack MCP: add NV vào channel team + #welcome
- WebSearch: tham khảo template Notion / Google của các unicorn VN

**Fallback bằng API (HRIS):**
```python
# Tạo onboarding tasks trong BambooHR / Sapo HR
import requests
tasks = [
    {"name": "Đọc Employee Handbook", "due_days": 3},
    {"name": "Hoàn thành Security Training", "due_days": 7},
    {"name": "Gặp 10 stakeholders", "due_days": 30},
]
for t in tasks:
    requests.post(f"https://api.bamboohr.com/api/gateway.php/{CO}/v1/employees/{EID}/tasks",
        json=t, auth=(API_KEY, "x"))
```

## Bước 5: Output Format
- File `.xlsx` Onboarding Roadmap (sheet 30/60/90 + checklist)
- File `.docx` Welcome Kit (16-20 trang)
- Email Welcome template (gửi T-3 ngày)
- Lịch ICS check-in (import Calendar)
- Lưu tại: `/outputs/Onboarding_<ten-NV>_<vi-tri>.xlsx`

## Checklist Trước Khi Giao
- [ ] Có 3 kết quả mong đợi cụ thể cho 90 ngày
- [ ] Gán Buddy + Mentor rõ
- [ ] Lịch 6 check-in đã tạo trong Calendar
- [ ] Welcome Kit ≤ 20 trang, có hình ảnh
- [ ] Compliance/Security training đã book
- [ ] Setup IT (email, laptop, access) sẵn ngày 1
- [ ] Survey NPS 30/60/90 đã chuẩn bị
- [ ] Manager đã duyệt plan
