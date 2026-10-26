---
name: legal-vendor-contract
description: |
  Soạn Hợp đồng Cung cấp Hàng hoá / Dịch vụ với Nhà Cung Cấp (NCC) chuẩn Việt Nam — gồm spec hàng hoá, SLA, thanh toán, bảo hành, phạt vi phạm, bảo mật, kiểm toán NCC. Kích hoạt khi người dùng nói: "soạn hợp đồng NCC", "hợp đồng nhà cung cấp", "vendor contract VN", "hợp đồng mua hàng", "hợp đồng cung ứng", "soạn HĐ supplier", "template HĐ NCC", "hợp đồng outsourcing", "hợp đồng gia công", "service agreement VN". Output là file .docx hợp đồng đầy đủ phụ lục + Excel bảng kiểm soát NCC.
---

# Hợp Đồng Cung Cấp Hàng Hoá / Dịch Vụ Với NCC Chuẩn VN

## Mục Tiêu
Cung cấp template hợp đồng NCC chuẩn pháp lý Việt Nam (Luật TM 2005, BLDS 2015, Luật Đấu thầu nếu liên quan) giúp phòng mua hàng / pháp chế triển khai nhanh, tránh điều khoản bất lợi và đảm bảo SLA đo lường được.

## Khi Nào Dùng
- Mua nguyên vật liệu thường xuyên (HĐ khung 1 năm + đơn đặt hàng PO)
- Thuê dịch vụ outsource (marketing, IT, vệ sinh, logistics)
- Gia công sản phẩm (OEM/ODM)
- Mua thiết bị / máy móc có bảo hành
- Hợp tác với nhà thầu xây lắp

## Bước 1: Chọn Mô Hình Hợp Đồng
- **HĐ khung + PO**: thanh toán theo từng đơn (master agreement + purchase order)
- **HĐ trọn gói**: 1 giá, 1 lần giao
- **HĐ định kỳ**: subscription / monthly recurring
- **HĐ gia công**: NCC dùng nguyên liệu của bên A
Hỏi user: NCC trong nước hay nước ngoài? Có VAT 8% / 10% / 0% không?

## Bước 2: Spec Hàng Hoá / Dịch Vụ + SLA
Bắt buộc có phụ lục:
- Phụ lục 1: Mô tả kỹ thuật (BOM, drawing, sample) — nguồn tranh chấp lớn nhất
- Phụ lục 2: Tiêu chí nghiệm thu (Acceptance Criteria) — đo lường được
- Phụ lục 3: SLA (uptime ≥99.5%, response time ≤4h, đền bù 5% phí tháng nếu miss)
- Phụ lục 4: Giá + lịch thanh toán (30% tạm ứng / 60% sau giao / 10% sau bảo hành)
- Phụ lục 5: Danh sách hàng hoá / báo giá (price list)

## Bước 3: 12 Điều Khoản Chính
1. Đối tượng + phạm vi cung cấp
2. Giá + thuế VAT + điều kiện điều chỉnh giá (CPI, FX, raw material)
3. Phương thức + thời hạn thanh toán (NET 30 / NET 60 / LC)
4. Giao hàng (Incoterms 2020: FOB/CIF/DAP/EXW), địa điểm, chứng từ
5. Kiểm tra + nghiệm thu (trong N ngày, từ chối nếu không đạt)
6. Bảo hành (12-24 tháng, đổi trả/sửa chữa, ai chịu chi phí logistic)
7. Phạt vi phạm + bồi thường (max 8% theo Luật TM Đ.301)
8. Quyền kiểm toán NCC (audit right) — gồm an toàn lao động, môi trường, lao động trẻ em
9. Bảo mật + SHTT (sample, drawing thuộc bên A)
10. Bất khả kháng + Material Adverse Change
11. Chấm dứt HĐ (đơn phương khi NCC chậm 30 ngày, phá sản, đổi chủ sở hữu)
12. Luật áp dụng + giải quyết tranh chấp (Toà án VN / VIAC ad hoc)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: lưu HĐ + repo NCC theo từng category
- Gmail MCP: gửi HĐ cho NCC ký + remind
- Google Sheets MCP: cập nhật bảng master vendor list (tên, MST, hạng, SLA score)
- DocuSign MCP: e-sign giữa 2 bên có pháp lý theo Nghị định 130/2018
- WebFetch: kiểm tra GPKD NCC trên `dangkykinhdoanh.gov.vn` (Cổng TT QG)
- WebFetch: tra cứu nợ thuế NCC trên `tracuunnt.gdt.gov.vn`

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Verify MST nhà cung cấp + sinh hợp đồng từ template
import requests
from docxtpl import DocxTemplate

mst = "0312345678"
r = requests.get(f"https://api.vietqr.io/v2/business/{mst}").json()
ncc_info = {
    "ten_ncc": r["data"]["name"],
    "dia_chi": r["data"]["address"],
    "mst": mst,
    "dai_dien": r["data"].get("representative", ""),
    "trang_thai": r["data"]["status"]  # phải = "Đang hoạt động"
}
doc = DocxTemplate("vendor_contract_template.docx")
doc.render({**ncc_info, "gia_tri_hd": 500_000_000, "ngay_ky": "01/06/2026"})
doc.save(f"HD_{ncc_info['ten_ncc'][:30]}_{mst}.docx")
```

## Bước 5: Output Format
- File `HD_NCC_<ten>_<mst>.docx`: hợp đồng chính + 5 phụ lục
- File `HD_NCC_<ten>_<mst>.pdf`: bản PDF chống chỉnh sửa
- File `vendor_master_list.xlsx`: cập nhật vào master list với status "Đang đàm phán / Đã ký / Tạm dừng"
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/vendor-contract/`

## Checklist Trước Khi Giao
- [ ] Đã verify MST NCC còn hoạt động (gdt.gov.vn)
- [ ] Đã đối chiếu GPKD: NCC có giấy phép kinh doanh đúng ngành nghề bán cho mình
- [ ] Phụ lục kỹ thuật đầy đủ + được 2 bên ký nháy từng trang
- [ ] SLA định lượng được (con số, %, ngày, không "hợp lý")
- [ ] Điều khoản giá có cơ chế điều chỉnh khi CPI/FX biến động >10%
- [ ] Có quyền audit + checklist ESG (nếu NCC xuất khẩu sang EU/Mỹ)
- [ ] Mức phạt ≤8% giá trị HĐ (Luật TM Đ.301)
- [ ] Đã đăng ký vào master vendor list + cảnh báo lịch hết hạn
