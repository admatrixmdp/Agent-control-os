---
name: hr-pip-builder
description: |
  Soạn Performance Improvement Plan (PIP) 30-60-90 ngày cho NV underperform tại doanh nghiệp Việt Nam, đúng pháp lý BLLĐ, có mục tiêu đo lường, support plan và lộ trình thoát.
  Kích hoạt khi người dùng nói: "PIP", "kế hoạch cải thiện hiệu suất", "performance improvement plan", "đưa NV vào PIP", "cảnh báo NV yếu", "plan cải tiến", "kỷ luật hiệu suất", "PIP 30 60 90", "underperform NV", "warning letter performance".
  Output là file .docx PIP document + .xlsx tracker + lịch check-in + thư thông báo.
---

# HR - Plan Cải Thiện Hiệu Suất (PIP 30-60-90)

## Mục Tiêu
PIP là cơ hội cuối cho NV underperform: rõ vấn đề, rõ kỳ vọng, rõ hỗ trợ. Đồng thời là **bằng chứng pháp lý** cần thiết nếu phải chấm dứt HĐLĐ theo Đ.36 BLLĐ 2019.

## Khi Nào Dùng
- NV rating "Below Expectation" 2 chu kỳ liên tiếp
- Sau warning verbal/written không cải thiện
- Manager đề xuất, HRBP thẩm định cần PIP
- Tránh dùng PIP để "ép nghỉ" - sai luật và phản tác dụng

## Bước 1: Thẩm Định Có Đáng PIP?
HRBP họp với manager check:
- Vấn đề là performance (đo được) hay hành vi (cần kỷ luật khác)?
- NV đã có verbal warning + written warning chưa?
- Manager đã 1-1 + feedback rõ chưa?
- JD và KPI có rõ ràng từ đầu?
- Có vấn đề bên ngoài công việc (sức khỏe, gia đình)?

Nếu YES tất cả → đáng PIP. Nếu manager skip feedback → khoan PIP, fix process.

## Bước 2: Soạn PIP Document
Cấu trúc chuẩn:
1. **Thông tin NV + lý do PIP** (cụ thể: KPI nào miss, hành vi nào)
2. **Gaps đã quan sát** (3-5 điểm, kèm ví dụ cụ thể có ngày tháng)
3. **Mục tiêu cải thiện** SMART:
   - 30 ngày: foundation (vd học SOP, hoàn thành training)
   - 60 ngày: progress (vd 50% KPI target)
   - 90 ngày: meet expectation (vd 100% KPI)
4. **Support plan**: mentor, training, resource, 1-1 hàng tuần
5. **Đánh giá**: cách đo, ai đo, tần suất
6. **Hậu quả**: nếu cuối 90 ngày không cải thiện → chuyển vị trí / chấm dứt HĐLĐ theo Đ.36
7. **Chữ ký** NV + Manager + HR

## Bước 3: Triển Khai PIP
- Họp PIP kickoff (60'): Manager + HRBP + NV. Tone hỗ trợ, không đe dọa
- 1-1 hàng tuần manager-NV (30')
- Check-in chính thức ngày 30, 60, 90 (60' mỗi lần) có HRBP
- Document mọi cuộc họp (biên bản signed)
- Cập nhật PIP tracker hàng tuần

Kết thúc PIP:
- **Pass**: NV qua, off PIP, theo dõi thêm 3 tháng
- **Extend**: thêm 30 ngày (chỉ khi có tiến bộ rõ)
- **Fail**: chấm dứt HĐLĐ theo Đ.36.1 BLLĐ - báo trước 45 ngày (HĐLĐ không xác định thời hạn), 30 ngày (12-36 tháng), 3 ngày (< 12 tháng)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Calendar MCP: tự book check-in 30/60/90 + 1-1 weekly
- Gmail MCP: gửi PIP document + biên bản họp cho NV
- Drive MCP: lưu hồ sơ PIP (confidential, chỉ HR + Manager + NV)
- Sheets MCP: tracker theo dõi tiến độ KR
- WebSearch: tra Đ.36 BLLĐ 2019 + án lệ tranh chấp lao động

**Fallback bằng API (Legal review):**
```python
# Log PIP timeline để phòng tranh chấp
import requests, datetime
event = {"employee_id": EID, "event_type": "PIP_milestone",
         "date": datetime.date.today().isoformat(),
         "notes": "30-day review: 60% target met",
         "documents": ["pip_v1.pdf", "1on1_log.pdf"]}
requests.post("https://hr-legal-log.internal/events", json=event,
    headers={"X-API-Key": API_KEY})
```

## Bước 5: Output Format
- File `.docx` PIP Document 4-6 trang (template chuẩn pháp lý)
- File `.xlsx` PIP Tracker (KR weekly progress)
- File `.docx` Meeting Minutes template (30, 60, 90)
- File `.docx` Thư thông báo PIP (formal)
- File `.docx` Mẫu thư chấm dứt HĐLĐ (nếu fail)
- Lưu tại: `/outputs/PIP_<NV>_<YYYY-MM>.docx` (folder mã hóa)

## Checklist Trước Khi Giao
- [ ] Vấn đề là performance đo được, không phải bias
- [ ] NV đã có verbal/written warning trước
- [ ] Mục tiêu SMART 30/60/90 rõ con số
- [ ] Support plan cụ thể (mentor, training)
- [ ] Lịch check-in đã set
- [ ] Biên bản mọi cuộc họp có chữ ký
- [ ] Tham chiếu Đ.36 BLLĐ trong thư
- [ ] Luật sư lao động review trước khi gửi
- [ ] Tone hỗ trợ - không đe dọa
