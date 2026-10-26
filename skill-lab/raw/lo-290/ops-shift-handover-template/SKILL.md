---
name: ops-shift-handover-template
description: |
  Template bàn giao ca sản xuất/nhà hàng/kho — ghi lại tình trạng máy, đơn hàng, sự cố, công việc kế tiếp giữa các ca. Dùng skill này khi người dùng yêu cầu: "bàn giao ca", "shift handover", "shift report", "giao ca sản xuất", "biên bản giao ca", "shift change template", "ca trưởng bàn giao", "log giao ca". Output là Excel template + form Google + tích hợp Slack.
---

# Shift Handover Template — Bàn Giao Ca Sản Xuất

## Mục Tiêu
Truyền tải đủ thông tin giữa ca, không "mất ngữ cảnh" gây sự cố lặp lại — cực kỳ quan trọng với sản xuất 3 ca, F&B 2 ca, kho 2 ca.

## Khi Nào Dùng
- Cuối mỗi ca sản xuất
- Bàn giao ca trưởng kho
- Restaurant manager ca sáng → ca tối
- Bệnh viện/khách sạn 24/7
- Helpdesk IT trực ca

## Bước 1: Nội Dung Bàn Giao Tiêu Chuẩn (SBAR + 5M)
**SBAR** từ y khoa:
- **Situation**: hiện trạng cuối ca
- **Background**: bối cảnh (sự cố, thay đổi)
- **Assessment**: đánh giá rủi ro tiềm ẩn
- **Recommendation**: ca sau nên ưu tiên gì

**5M cho sản xuất**:
- **Man**: nhân sự đi/về, người tăng cường, tinh thần
- **Machine**: máy hoạt động/lỗi/đang sửa
- **Material**: tồn NVL, đặt thêm gì
- **Method**: SOP có thay đổi không
- **Measure**: KPI ca (sản lượng, NG, OEE)

## Bước 2: Mẫu Form Bàn Giao
```
=== BIÊN BẢN BÀN GIAO CA ===
Ngày: ___ Ca giao: ___ Ca nhận: ___
Người giao: ___ Người nhận: ___

[1] SẢN LƯỢNG CA
- Plan: ___ pcs | Thực: ___ pcs | Đạt: __%
- NG: ___ pcs | Lý do chính: ___

[2] MÁY MÓC
- M01: OK / Lỗi (mô tả): ___
- M02: ...
- Đang sửa: máy nào, ETA fix

[3] NHÂN SỰ
- Có mặt: __/__
- Vắng: tên + lý do
- Tăng cường: ___

[4] NGUYÊN LIỆU
- NVL còn đủ tới: ___
- Cần đặt thêm: ___
- Phụ tùng critical: ___

[5] SỰ CỐ TRONG CA
- Sự cố 1: ___ → Đã xử lý / Đang theo dõi
- Khách phàn nàn: ___

[6] CÔNG VIỆC CHO CA SAU
- [ ] Việc 1
- [ ] Việc 2
- [ ] Việc khẩn

[7] LƯU Ý ĐẶC BIỆT
___

Chữ ký giao: ___ Chữ ký nhận: ___
```

## Bước 3: Quy Trình Bàn Giao 15 Phút
- 5 phút: Người giao tự fill form
- 5 phút: Walk-through tại line/khu (visual check)
- 3 phút: Người nhận hỏi clarify
- 2 phút: 2 bên ký + post lên Slack/Group

Quy tắc:
- Không ai về trước khi handover ký xong
- Ca sau xác nhận đã đọc bằng ✅ trên Slack
- Lưu form 6 tháng phục vụ điều tra sự cố

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Forms MCP: Form bàn giao chuẩn trên mobile
- Google Sheets MCP: Lịch sử bàn giao filter theo ngày/ca
- Slack MCP: Post tự động vào channel #shift-handover
- Notion MCP: Database handover với search full-text
- WebSearch: Benchmark mẫu handover từ Toyota, Honda
- WebFetch: Lấy mẫu shift report từ leanproduction.com

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Đẩy form Google Form -> Slack tự động
# (qua Apps Script trigger onFormSubmit)
def onFormSubmit(e):
    response = e.namedValues
    text = f"""*Bàn giao ca {response['Ca giao'][0]} -> {response['Ca nhận'][0]}*
Người giao: {response['Người giao'][0]}
Sản lượng: {response['Plan'][0]} / {response['Thực'][0]}
Sự cố: {response['Sự cố'][0]}
"""
    requests.post("https://hooks.slack.com/services/...",
        json={"text": text, "channel": "#shift-handover"})
```

## Bước 5: Output Format
- `Shift_Handover_Form.xlsx` — template Excel
- `Shift_Handover_GoogleForm_Link.md` — link Google Form scan QR
- `Handover_Log_<month>.xlsx` — log tổng hợp tháng
- `Critical_Issues_Tracker.xlsx` — issue chưa close qua nhiều ca
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/Handover/`

## Checklist Trước Khi Giao
- [ ] Đủ 7 mục trong form (sản lượng → công việc ca sau)
- [ ] Có chỗ ký 2 bên
- [ ] QR scan từ điện thoại điền nhanh
- [ ] Cảnh báo issue lặp qua > 3 ca
- [ ] Lưu trữ tối thiểu 6 tháng
- [ ] Audit hàng tháng chất lượng handover (random check)
