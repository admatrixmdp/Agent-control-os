---
name: hr-disciplinary-letter
description: |
  Soạn thư kỷ luật chuẩn pháp lý Việt Nam (khiển trách, kéo dài nâng lương, cách chức, sa thải) theo Đ.124-128 BLLĐ 2019, kèm biên bản họp xử lý kỷ luật.
  Kích hoạt khi người dùng nói: "thư kỷ luật", "biên bản kỷ luật", "kỷ luật lao động", "khiển trách NV", "thư sa thải", "disciplinary letter", "warning letter", "thư cảnh cáo", "xử lý kỷ luật NV", "thư cách chức".
  Output là file .docx thư kỷ luật + biên bản họp + chứng cứ đính kèm theo đúng quy trình BLLĐ.
---

# HR - Thư Kỷ Luật Pháp Lý

## Mục Tiêu
Đảm bảo mọi quyết định kỷ luật đúng trình tự, đúng hình thức, đúng nội dung theo BLLĐ 2019, tránh thua kiện tại tòa lao động (tỷ lệ DN thua > 60% khi NV khởi kiện do sai quy trình).

## Khi Nào Dùng
- NV vi phạm nội quy lao động đã ban hành
- Sau khi đã xác minh hành vi vi phạm
- Trước khi áp dụng 1 trong 4 hình thức kỷ luật (Đ.124)
- Khi cần văn bản pháp lý phòng tranh chấp

## Bước 1: Xác Định Hình Thức Kỷ Luật (Đ.124)
| Hình thức | Áp dụng cho | Tham chiếu |
|---|---|---|
| Khiển trách | Vi phạm lần đầu, mức độ nhẹ | Đ.124.1 |
| Kéo dài nâng lương ≤ 6 tháng | Vi phạm tái diễn | Đ.124.2 |
| Cách chức | NV giữ chức vụ vi phạm | Đ.124.2 |
| Sa thải | Vi phạm nghiêm trọng (Đ.125) | Đ.124.3 |

Sa thải chỉ áp dụng với:
- Trộm cắp, tham ô, gây thiệt hại nghiêm trọng
- Tiết lộ bí mật kinh doanh/công nghệ
- Sử dụng ma túy tại nơi làm việc
- NV bị kỷ luật kéo dài nâng lương / cách chức mà tái phạm
- Tự ý bỏ việc 5 ngày cộng dồn/30 ngày, hoặc 20 ngày/365 ngày không lý do chính đáng

## Bước 2: Trình Tự Bắt Buộc (Đ.122)
1. **Lập biên bản vi phạm** ngay khi phát hiện (có chữ ký NV vi phạm, nhân chứng)
2. **Mời họp xử lý kỷ luật** trước ≥ 5 ngày (có giấy mời ghi rõ thời gian, địa điểm, hành vi vi phạm)
3. **Tổ chức họp** với đầy đủ:
   - NV vi phạm (bắt buộc có mặt; nếu vắng 3 lần mới được xử vắng mặt)
   - Đại diện công đoàn cơ sở
   - NSDLĐ hoặc người được ủy quyền
   - Người chứng kiến (nếu có)
4. **Biên bản họp** có chữ ký các bên
5. **Quyết định kỷ luật** ra trong thời hiệu (6 tháng từ ngày phát hiện, có thể 12 tháng cho vi phạm tài chính)

## Bước 3: Cấu Trúc Thư Kỷ Luật
```
QUYẾT ĐỊNH XỬ LÝ KỶ LUẬT LAO ĐỘNG
Số: ___/QĐ-[CONGTY]
Hôm nay, ngày __/__/2026

Căn cứ:
- BLLĐ 2019 (Đ.122, 124, 125)
- Nội quy lao động công ty đã đăng ký với Sở LĐ-TBXH ngày...
- Biên bản vi phạm ngày...
- Biên bản họp xử lý kỷ luật ngày...

QUYẾT ĐỊNH:
Điều 1: Áp dụng hình thức kỷ luật [TÊN HÌNH THỨC] đối với ông/bà [TÊN], vị trí [...]
Lý do: [Mô tả hành vi cụ thể, viện dẫn điều khoản nội quy bị vi phạm]
Điều 2: Hiệu lực kể từ ngày...
Điều 3: Các phòng ban liên quan có trách nhiệm thi hành.

NSDLĐ ký                Công đoàn xác nhận
```

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Drive MCP: lưu hồ sơ kỷ luật (rất confidential, kiểm soát quyền)
- Calendar MCP: book họp xử lý kỷ luật + nhắc 5 ngày trước
- Gmail MCP: gửi giấy mời họp (có dấu thời gian gửi)
- WebSearch: tra BLLĐ 2019 + Nghị định 145/2020 + án lệ tranh chấp
- WebFetch: cập nhật Thông tư mới nhất từ Bộ LĐ-TBXH

**Fallback bằng API (Legal log):**
```python
# Log đầy đủ timeline phòng tranh chấp tòa án
import requests, datetime
disciplinary_log = {
    "employee_id": EID,
    "violation_date": "2026-03-15",
    "violation_description": "...",
    "internal_rule_clause": "Đ.4.2.b Nội quy lao động",
    "meeting_invitation_sent": "2026-03-20",
    "meeting_date": "2026-03-26",
    "form": "Khiển trách",
    "decision_date": "2026-03-27",
    "documents": ["bien_ban_vi_pham.pdf", "bb_hop.pdf", "qd_kyluat.pdf"]
}
requests.post("https://legal-log.internal/disciplinary", json=disciplinary_log)
```

## Bước 5: Output Format
- File `.docx` Biên bản vi phạm
- File `.docx` Giấy mời họp xử lý kỷ luật
- File `.docx` Biên bản họp
- File `.docx` Quyết định kỷ luật
- Hồ sơ chứng cứ đính kèm (PDF scan)
- Lưu tại: `/outputs/Disciplinary_<NV>_<YYYY-MM>/` (folder mã hóa)

## Checklist Trước Khi Giao
- [ ] Có Nội quy lao động đã đăng ký Sở LĐ-TBXH
- [ ] Hành vi vi phạm đúng quy định nội quy
- [ ] Hình thức kỷ luật đúng Đ.124
- [ ] Sa thải chỉ áp dụng nếu thuộc Đ.125
- [ ] Mời họp trước ≥ 5 ngày bằng văn bản
- [ ] Có đại diện công đoàn dự
- [ ] NV được trình bày
- [ ] Biên bản họp có đủ chữ ký
- [ ] Trong thời hiệu (6 hoặc 12 tháng)
- [ ] Luật sư lao động đã review
- [ ] KHÔNG áp dụng phạt tiền/cắt lương (cấm tại Đ.127)
