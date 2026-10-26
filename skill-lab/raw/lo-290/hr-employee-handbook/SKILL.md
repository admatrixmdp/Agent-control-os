---
name: hr-employee-handbook
description: |
  Soạn Sổ tay nhân viên (Employee Handbook) chuẩn cho doanh nghiệp Việt Nam, 8-10 phần gồm văn hóa, nội quy, lương thưởng, BHXH, kỷ luật, theo Bộ luật Lao động 2019.
  Kích hoạt khi người dùng nói: "sổ tay nhân viên", "employee handbook", "nội quy lao động", "soạn handbook", "tài liệu nhân viên mới", "company handbook", "employee guide", "sổ tay công ty", "nội quy công ty", "policy handbook".
  Output là file .docx 40-60 trang + .pdf flipbook + .pptx tóm tắt onboarding.
---

# HR - Sổ Tay Nhân Viên

## Mục Tiêu
Tạo 1 nguồn duy nhất (single source of truth) trả lời 80% câu hỏi NV về chính sách, giảm tải HR. Đồng thời là cơ sở pháp lý khi xử lý vi phạm, đảm bảo tuân thủ BLLĐ 2019.

## Khi Nào Dùng
- Công ty mới thành lập / startup vừa scale qua 50 NV
- Cập nhật handbook hằng năm (luật BHXH/lương min thay đổi)
- Sau M&A, hợp nhất nhiều bộ chính sách
- Trước khi đăng ký Nội quy lao động với Sở LĐ-TBXH

## Bước 1: Audit Chính Sách Hiện Có
Liệt kê tài liệu đang có: HĐLĐ mẫu, quy chế lương, quy chế thưởng, quy trình xin nghỉ phép, quy định an toàn... Phân loại nào còn dùng, nào lỗi thời, nào thiếu.

## Bước 2: Cấu Trúc 10 Phần Chuẩn
1. **Chào mừng + sứ mệnh/giá trị cốt lõi** (2-3 trang)
2. **Cơ cấu tổ chức + phòng ban** (2 trang)
3. **Tuyển dụng - Thử việc - Hợp đồng** (theo Đ.24-29 BLLĐ)
4. **Giờ làm việc, nghỉ ngơi, OT** (Đ.105-108 BLLĐ, tối đa 40h OT/tháng, 200h/năm, 300h cho ngành đặc thù)
5. **Tiền lương, thưởng, phụ cấp** (chu kỳ trả, hình thức, công thức)
6. **BHXH - BHYT - BHTN** (tỷ lệ NV 10.5% + DN 21.5%, mức trần)
7. **Nghỉ phép** (12 ngày phép năm + 11 ngày lễ + nghỉ thai sản 6 tháng)
8. **Quy tắc ứng xử + bảo mật + xung đột lợi ích**
9. **Kỷ luật lao động** (khiển trách, kéo dài nâng lương, cách chức, sa thải - đúng Đ.124-128)
10. **Quy trình khiếu nại + nghỉ việc**

Mỗi phần: nguyên tắc → quy trình → biểu mẫu → liên hệ.

## Bước 3: Việt Hóa Văn Phong + Kèm Ví Dụ
- Tránh văn bản pháp lý khô, dùng câu chủ động
- Mỗi quy định kèm "Ví dụ" 2-3 dòng
- Có FAQ cuối mỗi chương (5-7 Q&A phổ biến)
- Hộp lưu ý "Quan trọng" cho rủi ro pháp lý

Ví dụ FAQ Nghỉ phép: "Phép năm chưa dùng có được trả tiền không? - Theo Đ.113.3 BLLĐ, NV chấm dứt HĐLĐ chưa nghỉ hết phép thì DN thanh toán bằng tiền."

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tra cập nhật BLLĐ 2019, Nghị định 145/2020, mức BHXH 2026
- WebFetch: tải handbook tham khảo từ FPT, VinGroup, Techcombank
- Drive MCP: lưu handbook + bản dịch + biểu mẫu phụ lục
- Gmail MCP: gửi handbook cho toàn công ty kèm form xác nhận đã đọc

**Fallback bằng API (publish nội bộ):**
```python
# Đẩy lên intranet Notion/Confluence
import requests
page = {"parent": {"page_id": INTRANET_ID},
        "properties": {"title": [{"text": {"content": "Sổ tay NV 2026"}}]},
        "children": handbook_blocks}
requests.post("https://api.notion.com/v1/pages",
    json=page, headers={"Authorization": f"Bearer {TOKEN}",
    "Notion-Version": "2022-06-28"})
```

## Bước 5: Output Format
- File `.docx` 40-60 trang, có mục lục tự động, header/footer logo
- File `.pdf` xuất từ docx, có bookmark
- File `.pptx` 15 slide tóm tắt cho onboarding
- File `.xlsx` checklist NV xác nhận đã đọc/hiểu
- Lưu tại: `/outputs/EmployeeHandbook_<congty>_<YYYY>.docx`

## Checklist Trước Khi Giao
- [ ] Đủ 10 phần chuẩn
- [ ] Tham chiếu BLLĐ 2019 + Nghị định mới nhất
- [ ] Có biểu mẫu phụ lục (đơn xin phép, đơn nghỉ việc, biên bản vi phạm)
- [ ] Có FAQ mỗi chương
- [ ] Luật sư lao động/HR Manager đã review
- [ ] Đăng ký Nội quy lao động với Sở LĐ (nếu DN ≥ 10 NV)
- [ ] Có cơ chế cập nhật annually
- [ ] Form xác nhận đã đọc kèm
