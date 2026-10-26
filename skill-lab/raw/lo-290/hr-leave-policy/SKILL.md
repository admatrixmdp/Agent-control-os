---
name: hr-leave-policy
description: |
  Soạn chính sách nghỉ phép cho doanh nghiệp Việt Nam đúng Bộ luật Lao động 2019, gồm phép năm, lễ, thai sản, ốm, hiếu hỉ, không lương, WFH; kèm quy trình duyệt và biểu mẫu.
  Kích hoạt khi người dùng nói: "chính sách nghỉ phép", "leave policy", "quy định phép năm", "phép thai sản", "nghỉ không lương", "ngày lễ Việt Nam", "WFH policy", "soạn quy định nghỉ phép", "phép năm tính sao", "quy trình xin nghỉ".
  Output là file .docx chính sách + .xlsx bảng tính phép + form xin nghỉ.
---

# HR - Chính Sách Nghỉ Phép Theo Luật VN

## Mục Tiêu
Chuẩn hóa quy định nghỉ phép tuân thủ BLLĐ 2019, giảm tranh chấp NV - DN, dễ tính toán payroll, đồng thời giữ linh hoạt cho văn hóa công ty.

## Khi Nào Dùng
- Lập handbook lần đầu / cập nhật hằng năm
- Sau khi luật/Nghị định BHXH thay đổi
- Khi NV thắc mắc quy định nghỉ phép
- Trước khi setup HRIS module Time-off

## Bước 1: Liệt Kê Đầy Đủ Các Loại Phép Theo Luật VN
| Loại phép | Số ngày | Có lương | Căn cứ |
|---|---|---|---|
| Phép năm | 12 ngày (NV ≥ 12 tháng) | Có | Đ.113 BLLĐ |
| Thâm niên | +1 ngày/5 năm | Có | Đ.114 |
| Lễ Tết | 11 ngày | Có | Đ.112 |
| Việc riêng | Kết hôn 3, con cưới 1, tang 3 | Có | Đ.115 |
| Thai sản | 6 tháng (mẹ), 5-14 ngày (bố) | BHXH chi | Luật BHXH 2014 |
| Ốm đau | Tối đa 30-180 ngày/năm tùy thâm niên | BHXH 75% | Luật BHXH |
| Không lương | Theo thỏa thuận | Không | Đ.115 |

## Bước 2: Quy Định Bổ Sung Của Công Ty (Tùy Văn Hóa)
Bonus benefit khuyến khích:
- **Phép sinh nhật**: +1 ngày
- **Phép thưởng KPI**: +2-5 ngày khi đạt OKR
- **WFH**: 2 ngày/tuần (không tính phép)
- **Sabbatical**: 1 tháng sau 5 năm
- **Phép cha (Paternity)**: +5 ngày extra ngoài BHXH

Cộng dồn phép: cho phép chuyển 5 ngày sang năm sau, dùng hết trước 31/3.

## Bước 3: Quy Trình Xin & Duyệt
1. NV submit qua hệ thống (HRIS / Form / Slack) trước **3 ngày** với phép thường, **30 ngày** với phép > 5 ngày
2. Manager duyệt trong 24h
3. Hệ thống tự trừ quỹ phép, đồng bộ Calendar
4. NV bàn giao công việc cho backup
5. HR đối soát cuối tháng cho payroll

Trường hợp khẩn (ốm, hiếu): báo manager trong 4h, hoàn tất đơn trong 3 ngày.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Calendar MCP: tự động block phép trên lịch team
- Gmail MCP: gửi thông báo duyệt/từ chối phép
- Sheets MCP: bảng tổng hợp phép từng NV cập nhật real-time
- Slack MCP: bot /leave để NV submit nhanh
- WebSearch: tra cập nhật mức nghỉ thai sản, nghỉ lễ năm 2026

**Fallback bằng API (HRIS):**
```python
# Sync leave balance với MISA AMIS HRM
import requests
for emp in employees:
    balance = calculate_balance(emp.start_date, emp.used_days)
    requests.put(f"https://api.amis.misa.vn/v1/hr/leaves/{emp.id}",
        json={"annual_balance": balance, "year": 2026},
        headers={"Authorization": f"Bearer {TOKEN}"})
```

## Bước 5: Output Format
- File `.docx` Chính sách Nghỉ phép 8-12 trang
- File `.xlsx` Calculator phép (input ngày vào, output số phép)
- Form xin nghỉ phép (Google Form + Docx)
- Bảng tổng hợp phép cả công ty (Sheets)
- Lưu tại: `/outputs/LeavePolicy_<congty>_<YYYY>.docx`

## Checklist Trước Khi Giao
- [ ] Đủ 7 loại phép theo luật
- [ ] Số ngày, lương đúng BLLĐ 2019
- [ ] Có quy trình submit + duyệt rõ
- [ ] Có quy định carry-over (chuyển năm)
- [ ] Có quy định phép khẩn
- [ ] Tích hợp HRIS / Calendar
- [ ] Form xin nghỉ đã chuẩn hóa
- [ ] Bộ phận Kế toán đã review để tính lương
