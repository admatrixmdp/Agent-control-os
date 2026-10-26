---
name: ops-sop-writer
description: |
  Viết SOP (Standard Operating Procedure) chuẩn cho mọi quy trình vận hành doanh nghiệp Việt Nam — đầy đủ Input, Step, Output, RACI, KPI. Dùng skill này khi người dùng yêu cầu: "viết SOP", "tạo quy trình chuẩn", "chuẩn hóa quy trình", "tài liệu hóa quy trình", "SOP cho nhân viên mới", "quy trình tác nghiệp chuẩn", "làm tài liệu vận hành", "viết hướng dẫn công việc". Output là file Markdown + bảng RACI dạng Excel sẵn sàng in.
---

# Viết SOP Chuẩn Cho Doanh Nghiệp

## Mục Tiêu
Giúp doanh nghiệp chuẩn hóa quy trình vận hành thành tài liệu SOP dễ đọc, dễ training, có RACI rõ ràng — giảm phụ thuộc người, tăng tốc onboarding nhân viên mới từ 4 tuần xuống 1 tuần.

## Khi Nào Dùng
- Doanh nghiệp đang scale, quy trình chỉ nằm trong đầu sếp/trưởng phòng
- Onboard nhân viên mới mất quá nhiều thời gian
- Sai sót lặp lại do không có quy trình thống nhất
- Chuẩn bị audit ISO 9001 / chuyển giao công việc
- Setup chi nhánh mới cần copy quy trình

## Bước 1: Khảo Sát & Thu Thập Thông Tin
Hỏi người dùng 6 câu:
1. Tên quy trình + mục tiêu (VD: "Quy trình xuất kho hàng hóa")
2. Ai là chủ quy trình (Process Owner)
3. Trigger bắt đầu quy trình
4. Các bước hiện đang làm (liệt kê thô)
5. Các bộ phận liên quan
6. KPI đo lường thành công

## Bước 2: Cấu Trúc SOP Theo Template Chuẩn
Mỗi SOP gồm 10 phần:
1. **Mã SOP** (VD: SOP-WH-001), Phiên bản, Ngày ban hành
2. **Mục đích** (Purpose)
3. **Phạm vi áp dụng** (Scope)
4. **Định nghĩa & Thuật ngữ**
5. **Tài liệu tham chiếu**
6. **Quy trình chi tiết** (Step-by-step)
7. **Bảng RACI** (Responsible, Accountable, Consulted, Informed)
8. **KPI & Đo lường**
9. **Rủi ro & Biện pháp kiểm soát**
10. **Lịch sử thay đổi** (Revision history)

## Bước 3: Viết Step-by-Step Với Format Chuẩn
Mỗi bước có 5 thành phần:
- **STT**: 1, 2, 3...
- **Hành động**: Động từ + đối tượng (VD: "Kiểm tra phiếu xuất kho")
- **Người thực hiện**: Chức danh (VD: Thủ kho)
- **Input**: Cái gì cần có trước khi làm (VD: Phiếu xuất đã duyệt)
- **Output**: Kết quả sau khi làm (VD: Hàng đã xuất, biên bản giao nhận ký 2 bên)
- **Thời gian chuẩn**: Tính bằng phút/giờ
- **Lưu ý/Risk**: Cảnh báo gì

Ví dụ:
| STT | Hành động | Người thực hiện | Input | Output | Thời gian | Lưu ý |
|---|---|---|---|---|---|---|
| 1 | Nhận phiếu xuất từ Sales | Thủ kho | Phiếu xuất duyệt | Phiếu đã ký nhận | 5p | Check chữ ký Sales Manager |

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: Lưu SOP vào folder "Quy trình chuẩn" cho cả công ty truy cập
- Notion MCP: Tạo database SOP có filter theo phòng ban, version control
- Slack MCP: Thông báo SOP mới ban hành/cập nhật vào channel #ops
- WebSearch: Tìm SOP mẫu của ngành (F&B, logistics, retail) để tham khảo
- WebFetch: Tải template SOP ISO 9001 từ trang chính thức

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Đẩy SOP lên Notion database
import requests
NOTION_TOKEN = "secret_xxx"
DB_ID = "abc123"
requests.post("https://api.notion.com/v1/pages",
    headers={"Authorization": f"Bearer {NOTION_TOKEN}",
             "Notion-Version": "2022-06-28"},
    json={"parent": {"database_id": DB_ID},
          "properties": {"Mã SOP": {"title": [{"text": {"content": "SOP-WH-001"}}]},
                         "Phòng ban": {"select": {"name": "Kho"}},
                         "Version": {"number": 1.0}}})
```

## Bước 5: Output Format
- File chính: `SOP_<mã>_<tên>.md` (Markdown để dễ version control trên Git/Notion)
- File phụ: `RACI_<mã>.xlsx` (bảng RACI riêng cho dễ in dán bảng tin)
- Optional: Bản PDF có watermark logo công ty + chữ ký duyệt
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/SOP/`

## Checklist Trước Khi Giao
- [ ] Mã SOP duy nhất, có phiên bản và ngày ban hành
- [ ] Mỗi bước có Input/Output rõ ràng, đo được
- [ ] Bảng RACI không có quá 1 Accountable cho mỗi bước
- [ ] Có KPI đo lường được (số/phút/%/tỷ lệ)
- [ ] Đã review với Process Owner trước khi ban hành
- [ ] Có lịch review định kỳ (6 tháng/lần)
