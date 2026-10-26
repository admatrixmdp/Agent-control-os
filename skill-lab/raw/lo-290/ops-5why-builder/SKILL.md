---
name: ops-5why-builder
description: |
  Xây dựng phân tích 5 Why nhanh có template Word/Excel sẵn dùng cho mọi sự cố nhỏ-vừa trong vận hành. Dùng skill này khi người dùng yêu cầu: "phân tích 5 Why", "5 Whys analysis", "tìm nguyên nhân gốc nhanh", "5 tại sao", "Why-Why analysis", "phân tích vấn đề đơn giản", "template 5 Why". Output là file .docx + .xlsx có chỗ điền nhanh, in được mang vào meeting.
---

# 5 Why Builder — Phân Tích 5 Tại Sao Nhanh

## Mục Tiêu
Tách biệt với RCA full (Fishbone + 8D), 5 Why đơn lẻ là công cụ chạy nhanh trong 15-30 phút cho sự cố nhỏ, dùng trong daily stand-up, shift handover, hoặc khi sếp hỏi "tại sao?" 5 lần.

## Khi Nào Dùng
- Sự cố nhỏ phát hiện hàng ngày trong ca sản xuất
- Daily stand-up team Operations
- Sau khi khách phàn nàn 1 đơn hàng
- Trainings staff làm quen tư duy critical
- Quick win trước khi mở RCA chính thức

## Bước 1: Định Nghĩa Vấn Đề Một Câu
Format chuẩn: "Cái gì + Khi nào + Đo lường được"
- ❌ "Khách phàn nàn" (mơ hồ)
- ✅ "Khách hàng X phàn nàn đơn 12345 giao trễ 2 ngày so với cam kết"

## Bước 2: Hỏi Tại Sao 5 Lần Liên Tiếp
Quy tắc:
- Mỗi lần Why phải đáp "vì..."
- Không nhảy logic — câu sau phải là hệ quả trực tiếp của câu trước
- Không dừng ở "lỗi con người" → tiếp tục hỏi tại sao họ làm sai
- Stop khi câu trả lời là "hệ thống/quy trình/chính sách"

Template:
```
Vấn đề: Đơn 12345 giao trễ 2 ngày
Why 1? Vì hàng xuất khỏi kho trễ 1 ngày so với plan
Why 2? Vì hàng QC fail phải rework
Why 3? Vì lô nguyên liệu nhập bị ẩm mốc
Why 4? Vì NCC giao trong cơn mưa, không bọc kỹ
Why 5? Vì hợp đồng NCC chưa quy định điều kiện đóng gói khi mưa
ROOT CAUSE: Thiếu điều khoản hợp đồng về đóng gói/vận chuyển theo thời tiết
```

## Bước 3: Đề Xuất Action
Mỗi Why có thể tạo action ngắn hạn (band-aid) và Why 5 có action dài hạn (preventive).
| Mức | Action | Owner | Due | Mục đích |
|---|---|---|---|---|
| Why 1 | Mở thêm ca tăng tốc xuất kho | Quản lý kho | 1 ngày | Khắc phục ngay |
| Why 3 | Kiểm tra ẩm trước khi nhập | QC | 3 ngày | Containment |
| Why 5 | Update hợp đồng NCC điều khoản đóng gói | Mua hàng | 30 ngày | Root cause fix |

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Docs MCP: Mở template 5 Why có sẵn header công ty
- Notion MCP: Database 5 Why log có filter theo phòng ban/tháng
- Slack MCP: Bot prompt "5 Why hôm nay" sau mỗi incident
- WebSearch: Tham khảo case 5 Why của Toyota, lean.org

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tự sinh template Word 5 Why với python-docx
from docx import Document
doc = Document()
doc.add_heading("5 Why Analysis — <Ngày>", 0)
doc.add_paragraph("Vấn đề: ____________________")
for i in range(1, 6):
    doc.add_paragraph(f"Why {i}? __________________________")
doc.add_paragraph("Root Cause: __________________")
doc.add_heading("Action Plan", 1)
table = doc.add_table(rows=1, cols=4)
table.rows[0].cells[0].text = "Action"
table.rows[0].cells[1].text = "Owner"
table.rows[0].cells[2].text = "Due"
table.rows[0].cells[3].text = "Status"
doc.save("5why_template.docx")
```

## Bước 5: Output Format
- `5why_<ngay>_<incident>.docx` — file Word có chỗ điền tay
- `5why_<ngay>_<incident>.xlsx` — bản Excel có dropdown
- `5why_log_<thang>.xlsx` — sổ tổng hợp toàn bộ 5 Why trong tháng
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/5Why/`

## Checklist Trước Khi Giao
- [ ] Vấn đề mô tả có số liệu cụ thể
- [ ] Đủ 5 lần Why, không tự ý dừng ở 3
- [ ] Câu trả lời cuối là về hệ thống, không phải về cá nhân
- [ ] Có ít nhất 1 action preventive cho root cause
- [ ] Owner + Due date cụ thể, không "ASAP"
- [ ] Đã chia sẻ với người liên quan trước khi đóng
