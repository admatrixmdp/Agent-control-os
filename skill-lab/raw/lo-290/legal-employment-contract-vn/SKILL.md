---
name: legal-employment-contract-vn
description: |
  Soạn Hợp đồng Lao động (HĐLĐ) chuẩn Bộ luật Lao động 2019 — xác định thời hạn / không xác định thời hạn / thử việc / khoán việc, cho cả lao động phổ thông, văn phòng và quản lý cấp cao. Kích hoạt khi người dùng nói: "soạn HĐLĐ", "hợp đồng lao động", "HĐLĐ xác định thời hạn", "HĐLĐ không xác định thời hạn", "hợp đồng thử việc", "soạn employment contract VN", "HĐLĐ giám đốc", "HĐLĐ part-time", "hợp đồng người lao động nước ngoài", "labour contract Vietnam". Output là file .docx HĐLĐ ký được ngay + bảng tóm tắt quyền lợi.
---

# Hợp Đồng Lao Động Việt Nam — Chuẩn BLLĐ 2019

## Mục Tiêu
Giúp phòng Nhân sự / Pháp chế tạo HĐLĐ chuẩn Bộ luật Lao động 2019 (số 45/2019/QH14, hiệu lực 01/01/2021) + Nghị định 145/2020 + Thông tư 10/2020 — tránh án tuyên vô hiệu hoặc phạt hành chính 5-75 triệu/HĐLĐ sai (NĐ 12/2022).

## Khi Nào Dùng
- Tuyển nhân viên mới (full-time, part-time, thực tập, thời vụ)
- Gia hạn / chuyển loại HĐLĐ (thử việc → chính thức, xác định → không xác định)
- Soạn HĐLĐ cho lao động nước ngoài (cần Work Permit + thẻ tạm trú)
- Soạn HĐLĐ cho CEO / Giám đốc thuê (Director Agreement)
- Cập nhật mẫu HĐLĐ khi BLLĐ / Nghị định thay đổi

## Bước 1: Xác Định Loại HĐLĐ (BLLĐ Đ.20)
- **HĐ không xác định thời hạn**: 2 bên không xác định thời điểm chấm dứt
- **HĐ xác định thời hạn**: tối đa 36 tháng, gia hạn 1 lần (lần 3 PHẢI chuyển thành không xác định)
- **HĐ thử việc** (Đ.24-25): tối đa 180 ngày với CEO, 60 ngày với chuyên môn cao, 30 ngày với chức danh khác, 6 ngày với lao động phổ thông
- **HĐ khoán việc**: theo công việc cụ thể
Lưu ý: KHÔNG còn HĐLĐ "mùa vụ" theo BLLĐ 2019.

## Bước 2: 10 Nội Dung Bắt Buộc (BLLĐ Đ.21)
1. Tên + địa chỉ NSDLĐ + người đại diện
2. Họ tên, ngày sinh, CCCD, địa chỉ NLĐ
3. Công việc + địa điểm làm việc
4. Thời hạn HĐ
5. Mức lương, hình thức trả, kỳ trả, phụ cấp, các khoản bổ sung
6. Chế độ nâng bậc, nâng lương
7. Thời giờ làm việc, nghỉ ngơi (tối đa 48h/tuần, 8h/ngày + làm thêm ≤200h/năm)
8. Trang bị BHLĐ
9. BHXH, BHYT, BHTN (mức 32% tổng — 21.5% NSDLĐ, 10.5% NLĐ)
10. Đào tạo, bồi dưỡng nâng cao trình độ

## Bước 3: Điều Khoản Đặc Biệt Tuỳ Vị Trí
- **C-level / Giám đốc**: cam kết không cạnh tranh (non-compete tối đa 12 tháng có trả lương — chưa được luật hoá rõ, dùng thoả thuận dân sự)
- **Sale / BD**: KPI + commission rule + cam kết bàn giao khách hàng
- **R&D / Tech**: SHTT thuộc công ty (BLLĐ Đ.40 — IP do NLĐ tạo ra trong quá trình lao động)
- **Lao động nước ngoài**: ghi rõ số Work Permit + thẻ tạm trú + visa loại LĐ
- **Bí mật kinh doanh**: thoả thuận bảo mật riêng + bồi thường vi phạm

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: lưu HĐLĐ + sao lưu hồ sơ nhân sự
- Gmail MCP: gửi HĐLĐ cho ứng viên + remind ký
- DocuSign MCP: ký số HĐLĐ (Nghị định 130/2018 công nhận giá trị pháp lý)
- Google Sheets MCP: cập nhật bảng master HR (loại HĐ, ngày hết hạn, lương, BHXH)
- WebFetch: tra cứu mức lương tối thiểu vùng mới nhất tại `molisa.gov.vn` / `thuvienphapluat.vn`
- WebFetch: kiểm tra Work Permit hợp lệ trên cổng dolab.gov.vn (LĐ nước ngoài)

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tính BHXH + thu nhập thực nhận theo mức lương đóng BH
def tinh_thu_nhap(luong_co_ban, phu_cap_bh, phu_cap_khong_bh):
    luong_dong_bh = luong_co_ban + phu_cap_bh
    bhxh_nld = luong_dong_bh * 0.08   # 8% BHXH NLĐ
    bhyt_nld = luong_dong_bh * 0.015  # 1.5% BHYT
    bhtn_nld = luong_dong_bh * 0.01   # 1% BHTN
    tong_dong_bh = bhxh_nld + bhyt_nld + bhtn_nld
    thu_nhap_chiu_thue = luong_co_ban + phu_cap_bh + phu_cap_khong_bh - tong_dong_bh - 11_000_000  # giảm trừ gia cảnh
    # Áp biểu thuế lũy tiến (Luật Thuế TNCN 2007)
    return {"luong_dong_bh": luong_dong_bh, "bh_nld": tong_dong_bh, "tncn_chiu_thue": max(0, thu_nhap_chiu_thue)}

print(tinh_thu_nhap(20_000_000, 2_000_000, 3_000_000))
```

## Bước 5: Output Format
- File `HDLD_<HoTenNLD>_<NgayKy>.docx`: HĐLĐ theo mẫu, chừa chỗ ký + đóng dấu
- File `HDLD_<HoTenNLD>_<NgayKy>.pdf`: bản preview
- File `tom_tat_quyen_loi.pdf`: 1 trang tóm tắt lương + BH + phép năm + KPI cho NLĐ
- Cập nhật `hr_master_list.xlsx` thêm dòng mới với cảnh báo ngày hết hạn HĐ
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/employment-contracts/`

## Checklist Trước Khi Giao
- [ ] Loại HĐLĐ chọn đúng (không quá 2 lần HĐ xác định thời hạn cho 1 NLĐ)
- [ ] Đủ 10 nội dung bắt buộc theo BLLĐ Đ.21
- [ ] Mức lương ≥ lương tối thiểu vùng + phụ cấp đúng quy định
- [ ] Thời giờ làm việc/nghỉ ngơi tuân thủ Đ.105-115
- [ ] BHXH/BHYT/BHTN đăng ký đúng mức đóng
- [ ] Thử việc không quá thời hạn luật cho phép
- [ ] LĐ nước ngoài có Work Permit hợp lệ (hoặc thuộc diện miễn)
- [ ] Đã lưu master HR + cảnh báo ngày hết hạn để gia hạn kịp thời
