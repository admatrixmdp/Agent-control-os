---
name: mkt-press-kit-builder
description: |
  Tạo press kit chuyên nghiệp cho doanh nghiệp Việt Nam — boilerplate, fact sheet, exec bio, logo, ảnh HD, brand guideline tóm tắt. Tự động sinh nội dung và folder cấu trúc. Kích hoạt khi người dùng nói: "tạo press kit", "build press kit", "media kit", "press kit doanh nghiệp", "fact sheet công ty", "boilerplate", "exec bio", "press kit gửi báo". Output là folder ZIP gồm PDF + ảnh + Markdown.
---

# Press Kit Builder — Boilerplate + Asset

## Mục Tiêu
Mỗi khi gửi pitch PR có ngay 1 press kit đầy đủ, chuẩn brand, tiết kiệm 1-2 ngày chuẩn bị thủ công. Phóng viên có đủ thông tin viết bài ngay.

## Khi Nào Dùng
- Lần đầu xây bộ press kit
- Cập nhật khi gọi vốn / đổi logo / ra leader mới
- Trước event lớn (launch, ngày kỷ niệm)
- Khi báo/podcast/sự kiện request
- Gửi cùng pitch PR

## Bước 1: Thu Thập Thông Tin
Hỏi:
1. Tên công ty + năm thành lập
2. Vision, Mission, USP
3. Sản phẩm/dịch vụ chính
4. Founder & leadership (3-5 người: tên, chức vụ, bio 100 từ)
5. Số liệu: nhân sự, khách hàng, doanh thu, vốn
6. Milestone lớn (giải thưởng, gọi vốn, mở rộng)
7. Logo + ảnh HD (input/path)

## Bước 2: Viết Boilerplate + Fact Sheet
**Boilerplate** (3 phiên bản 50/100/200 từ): đoạn giới thiệu chuẩn paste vào mọi PR.

**Fact sheet** 1 trang:
- Tên + logo + tagline
- Thành lập / trụ sở / website
- Sản phẩm flagship
- Số liệu key
- Milestone timeline
- Đầu tư / cổ đông
- Awards
- Contact PR

## Bước 3: Soạn Exec Bio + Asset List
Mỗi leader 3 phiên bản bio: 1 dòng / 50 từ / 150 từ. Kèm ảnh chân dung HD và link LinkedIn.

Asset list:
- Logo (PNG transparent, SVG, đen/trắng/màu)
- Ảnh sản phẩm HD
- Ảnh team/văn phòng
- Brand color + font
- Video sizzle reel (nếu có)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: tạo folder Press Kit chia subfolder
- Notion MCP: trang public press kit
- Canva/Figma MCP: export logo các định dạng
- WebSearch: tham khảo press kit best-in-class
- WebFetch: lấy thông tin cập nhật từ website chính

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tự động đóng gói press kit thành ZIP
import zipfile, os
with zipfile.ZipFile('press_kit_2026.zip','w') as zf:
    for root,_,files in os.walk('press_kit/'):
        for f in files:
            zf.write(os.path.join(root,f),
              arcname=os.path.relpath(os.path.join(root,f),'press_kit/'))
```

## Bước 5: Output Format
- Folder ZIP cấu trúc:
  - `/01_FactSheet.pdf`
  - `/02_Boilerplate.md`
  - `/03_ExecBio/`
  - `/04_Logo/` (PNG, SVG, các màu)
  - `/05_Photos/` (HD product, team, office)
  - `/06_BrandGuide_lite.pdf`
  - `/07_Contact.md`
- Trang web press kit (URL công khai)
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Boilerplate 3 độ dài
- [ ] Fact sheet 1 trang
- [ ] Exec bio đủ leader chính
- [ ] Logo đủ định dạng + màu
- [ ] Ảnh HD >= 1920px
- [ ] Contact PR rõ
- [ ] Link công khai accessible
