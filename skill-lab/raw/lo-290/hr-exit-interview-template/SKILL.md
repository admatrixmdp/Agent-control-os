---
name: hr-exit-interview-template
description: |
  Template phỏng vấn nghỉ việc (Exit Interview) cho doanh nghiệp Việt Nam, thu thập lý do thực, theme phổ biến, đề xuất hành động giảm turnover; kèm form và báo cáo quý.
  Kích hoạt khi người dùng nói: "exit interview", "phỏng vấn nghỉ việc", "phỏng vấn thôi việc", "khảo sát NV nghỉ", "lý do nghỉ việc", "offboarding", "turnover analysis", "phân tích nghỉ việc", "exit survey", "interview NV thôi việc".
  Output là file .docx form phỏng vấn + .xlsx báo cáo quý theme/lý do + slide tổng hợp BOD.
---

# HR - Template Phỏng Vấn Nghỉ Việc

## Mục Tiêu
NV đã nghỉ là nguồn feedback trung thực nhất (vì không sợ trả đũa). Exit Interview tốt giúp HR phát hiện manager toxic, chính sách lỗi, cơ hội cải tiến trước khi mất thêm người.

## Khi Nào Dùng
- Mỗi khi NV nộp đơn nghỉ
- Khi turnover rate phòng ban > 20%/năm
- Lập báo cáo quý phân tích lý do nghỉ
- Trước khi đề xuất chính sách giữ chân

## Bước 1: Chuẩn Bị Trước Phỏng Vấn
- Tổ chức trong 2 tuần cuối trước ngày làm cuối
- Người phỏng vấn: HRBP (KHÔNG phải manager trực tiếp)
- Thông báo trước: "Cuộc trò chuyện ẩn danh, dùng để cải tiến"
- Đọc lại hồ sơ: thâm niên, vị trí, performance, lương, manager
- Thời lượng: 45-60 phút

## Bước 2: Bộ Câu Hỏi Theo 6 Cụm
**A. Lý do nghỉ (5 câu)**
- "Yếu tố quyết định khiến bạn nghỉ là gì?"
- "Lý do thật so với lý do bạn ghi trong đơn?"
- "Công ty mới offer gì? Lương? Cơ hội?"
- "Quyết định này có thể đảo ngược không?"

**B. Trải nghiệm tại công ty (6 câu)**
- "Điều bạn yêu nhất khi làm ở đây?"
- "Điều bạn ghét nhất?"
- "JD ngày đầu vs công việc thực tế có khớp?"
- "Có cảm thấy được lắng nghe?"

**C. Manager trực tiếp (5 câu)**
- "Manager hỗ trợ phát triển bạn thế nào?"
- "Feedback có hữu ích?"
- "1-1 có đều và chất lượng?"
- "Bạn có recommend Manager này cho người khác?"

**D. Lương thưởng + benefit (3 câu)**
- "Lương có cạnh tranh thị trường?"
- "Quy trình tăng lương có công bằng?"
- "Benefit nào bạn dùng nhiều/ít nhất?"

**E. Văn hóa + Phát triển (4 câu)**
- "Cơ hội học hỏi đủ không?"
- "Có thấy lộ trình thăng tiến?"
- "Văn hóa có như cam kết ngày phỏng vấn?"

**F. Đề xuất (2 câu)**
- "3 điều công ty nên thay đổi ngay?"
- "Bạn còn ở lại nếu...?"

## Bước 3: Phân Tích + Theme Mỗi Quý
Gom các lý do nghỉ thành nhóm:
- Lương thấp / counter offer cao hơn
- Không có cơ hội thăng tiến
- Manager problem (top reason ở VN)
- Burnout / quá tải
- Văn hóa không phù hợp
- Lý do cá nhân (chuyển nơi ở, học tiếp)

Đếm tần suất, phân theo phòng ban → identify red flag.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Calendar MCP: book lịch exit interview ngay khi nhận đơn nghỉ
- Gmail MCP: gửi survey ẩn danh trước phỏng vấn 1 tuần
- Sheets MCP: master tổng hợp lý do nghỉ theo quý
- Drive MCP: lưu transcript ẩn danh
- WebSearch: benchmark turnover rate ngành VN

**Fallback bằng API (HRIS):**
```python
# Sync turnover data vào BI dashboard
import requests, pandas as pd
exits = pd.read_csv("exits_Q2.csv")
top_reasons = exits["reason"].value_counts().head(5)
data = {"quarter": "Q2-2026",
        "turnover_rate": len(exits)/total_emp,
        "top_reasons": top_reasons.to_dict()}
requests.post("https://api.metabase/dataset/turnover", json=data,
    headers={"X-API-Key": API_KEY})
```

## Bước 5: Output Format
- File `.docx` Form Exit Interview (3-4 trang)
- File `.xlsx` Quarterly Exit Analysis (theme, by dept, by manager)
- File `.pptx` Slide BOD review turnover + action
- File `.pdf` Anonymized highlight quotes (rút từ phỏng vấn)
- Lưu tại: `/outputs/ExitInterview_<NV>_<YYYY-MM>.docx`

## Checklist Trước Khi Giao
- [ ] HRBP phỏng vấn, không phải manager
- [ ] Có khẳng định ẩn danh + dùng cải tiến
- [ ] Đủ 6 cụm câu hỏi
- [ ] Hỏi cả "Có thể đảo ngược?" để retain
- [ ] Báo cáo quý phân nhóm theo phòng ban
- [ ] Flag red signal (manager turnover > 30%)
- [ ] Có action cụ thể từ leadership
- [ ] Bảo mật danh tính trong báo cáo
