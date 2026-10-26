---
name: legal-board-resolution
description: |
  Soạn Nghị quyết / Quyết định của Hội đồng Quản trị (CTCP) hoặc Hội đồng Thành viên (TNHH 2TV+) chuẩn Luật Doanh nghiệp 2020. Kích hoạt khi người dùng nói: "soạn nghị quyết HĐQT", "viết nghị quyết HĐTV", "biên bản họp HĐQT", "Board Resolution VN", "nghị quyết tăng vốn", "nghị quyết bổ nhiệm CEO", "quyết định cổ đông", "nghị quyết M&A", "nghị quyết phân chia lợi nhuận", "soạn biên bản HĐTV". Output là file .docx có biên bản họp + nghị quyết sẵn ký, kèm tài liệu nội bộ cho team Pháp chế.
---

# Nghị Quyết HĐQT / HĐTV Chuẩn Luật DN 2020

## Mục Tiêu
Soạn nghị quyết / biên bản họp HĐQT (CTCP) hoặc HĐTV (TNHH 2 TV trở lên) tuân thủ Luật Doanh nghiệp 2020 (số 59/2020/QH14) — tránh nghị quyết bị tuyên vô hiệu (Đ.151 + Đ.181) khi sai thủ tục triệu tập, thẩm quyền, biểu quyết.

## Khi Nào Dùng
- Bổ nhiệm / miễn nhiệm CEO, Giám đốc tài chính, thành viên HĐQT
- Phê duyệt báo cáo tài chính + phân chia lợi nhuận
- Phê duyệt giao dịch lớn (>35% tài sản — Đ.167)
- Phê duyệt M&A, mua bán cổ phần, phát hành cổ phần mới
- Phê duyệt vay vốn, bảo lãnh, đầu tư dự án
- Thay đổi điều lệ, tăng/giảm vốn, mở chi nhánh

## Bước 1: Xác Định Loại Doanh Nghiệp + Cơ Quan Ra Nghị Quyết
- **CTCP**: ĐHĐCĐ (Đ.138) / HĐQT (Đ.153-157)
- **TNHH 2TV+**: HĐTV (Đ.55-60)
- **TNHH MTV (cá nhân)**: Chủ sở hữu quyết định
- **TNHH MTV (tổ chức)**: Chủ tịch công ty / HĐTV (Đ.79-84)
Phân định thẩm quyền: vấn đề nào HĐQT/HĐTV quyết, vấn đề nào phải ĐHĐCĐ/chủ sở hữu quyết.

## Bước 2: Kiểm Tra Thủ Tục Triệu Tập + Biểu Quyết
- **HĐQT**: thông báo trước ≥3 ngày làm việc (Đ.157), họp khi ≥3/4 thành viên dự, thông qua khi quá nửa đồng ý (chủ tịch có quyền quyết khi 50-50)
- **HĐTV**: triệu tập ≥7 ngày (Đ.57), họp khi đại diện ≥65% vốn dự, thông qua khi ≥65% (hoặc 75% với vấn đề lớn — Đ.59.3)
- **ĐHĐCĐ**: triệu tập ≥21 ngày, thông qua thường khi ≥50%, đặc biệt khi ≥65% (Đ.148)
Phải có sổ đăng ký + biên bản đầy đủ.

## Bước 3: Cấu Trúc Nghị Quyết (8 Phần)
1. **Tiêu đề**: "NGHỊ QUYẾT HỘI ĐỒNG QUẢN TRỊ" + Số / năm
2. **Thông tin công ty**: tên, MST, GPKD, địa chỉ, vốn điều lệ
3. **Căn cứ pháp lý**: Luật DN 2020 + Điều lệ công ty + Biên bản họp số...
4. **Xét thấy**: lý do ban hành (thường 1-3 đoạn)
5. **Quyết nghị**:
   - Điều 1: Nội dung chính (cụ thể, đo lường được)
   - Điều 2: Trách nhiệm thực hiện
   - Điều 3: Hiệu lực
6. **Biểu quyết**: số phiếu thuận / chống / trắng / tỷ lệ %
7. **Người ký**: Chủ tịch HĐQT/HĐTV + thư ký + thành viên (nếu cần)
8. **Nơi nhận**: lưu VT, gửi cổ đông, cơ quan ĐKKD nếu thay đổi điều lệ

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: lưu master nghị quyết + lịch sử
- Gmail MCP: gửi thông báo triệu tập + biên bản cho thành viên
- Google Calendar MCP: lên lịch họp HĐQT/HĐTV định kỳ
- DocuSign MCP: ký số nghị quyết (Nghị định 130/2018)
- Notion MCP: lưu corporate registry — danh sách nghị quyết theo năm
- WebFetch: cập nhật Cổng đăng ký kinh doanh `dangkykinhdoanh.gov.vn` khi nghị quyết thay đổi nội dung GPKD

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Sinh nghị quyết từ template + log corporate registry
from docxtpl import DocxTemplate
from datetime import datetime

def tao_nghi_quyet(loai_dn, so_nq, noi_dung, bieu_quyet):
    template = "BoardResolution_CTCP.docx" if loai_dn == "CTCP" else "Resolution_HDTV.docx"
    doc = DocxTemplate(template)
    context = {
        "so_nq": so_nq,
        "ngay": datetime.now().strftime("%d/%m/%Y"),
        "noi_dung": noi_dung,
        "phieu_thuan": bieu_quyet["thuan"],
        "phieu_chong": bieu_quyet["chong"],
        "phieu_trang": bieu_quyet["trang"],
        "ty_le_thong_qua": f"{bieu_quyet['thuan']/sum(bieu_quyet.values())*100:.2f}%"
    }
    doc.render(context)
    doc.save(f"NQ_{so_nq}_{datetime.now().strftime('%Y%m%d')}.docx")
    # Update corporate registry
    return context
```

## Bước 5: Output Format
- File `NQ_<SoNQ>_<yyyymmdd>.docx`: nghị quyết chính sẵn ký
- File `BienBan_HopHDQT_<SoNQ>.docx`: biên bản họp đi kèm (chứng cứ thủ tục)
- File `Thong_Bao_Trieu_Tap.docx`: thông báo trước khi họp (lưu chứng cứ ≥3 ngày)
- File `corporate_registry.xlsx`: cập nhật vào sổ đăng ký nghị quyết
- Bộ tài liệu nộp Sở KHĐT nếu thay đổi GPKD: Mẫu II-1 + nghị quyết + biên bản
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/board-resolutions/`

## Checklist Trước Khi Giao
- [ ] Đúng thẩm quyền cơ quan ra nghị quyết (HĐQT / HĐTV / ĐHĐCĐ)
- [ ] Đủ thời gian thông báo triệu tập (3 / 7 / 21 ngày)
- [ ] Đủ điều kiện họp (số TV / tỷ lệ vốn dự)
- [ ] Đủ tỷ lệ thông qua theo Luật DN + Điều lệ
- [ ] Có biên bản họp đi kèm (chứng cứ trước toà)
- [ ] Có chữ ký Chủ tịch + Thư ký (Đ.158 với CTCP)
- [ ] Nếu thay đổi GPKD: đã chuẩn bị bộ hồ sơ nộp Sở KHĐT trong 10 ngày
- [ ] Đã lưu vào sổ đăng ký nghị quyết (corporate registry)
