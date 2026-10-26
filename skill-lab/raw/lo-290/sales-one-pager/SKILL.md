---
name: sales-one-pager
description: |
  Tạo one-pager bán hàng A4 cho leave-behind, intro email, event handout. Trigger phrases: "tạo one pager", "sales one pager A4", "leave behind document", "one page brochure", "soạn one pager sản phẩm", "sales handout", "intro one pager", "PDF 1 trang giới thiệu", "tạo flyer bán hàng", "one pager B2B". Output là PDF A4 + Docx editable.
---

# Sales One-Pager Builder (A4)

## Mục Tiêu
Tạo one-pager A4 design đẹp dùng làm leave-behind sau meeting, attach email cold outreach, handout event — convey value trong <30s đọc.

## Khi Nào Dùng
- Sau cold call cần gửi material
- Event/conference handout
- LinkedIn outreach attachment
- Partner sales kit
- Channel arming distributor

## Bước 1: 7-Section Layout A4

**Header (top 15%)**:
- Logo + tagline
- Headline: 1 câu value prop (8-12 từ)

**Section 1 (left col, top)** — Pain bullet (3 dòng)

**Section 2 (right col, top)** — Solution bullet (3 dòng)

**Section 3 (middle)** — Proof: 3 logo KH + 1 stat
"$2M saved cho Coca-Cola in 6 months"

**Section 4 (left col, bottom)** — 3 differentiator icon + 1 dòng

**Section 5 (right col, bottom)** — 3-step "How it works"

**Footer (bottom 10%)**:
- CTA: scan QR / email / book call link
- Contact + website
- Compliance line nếu cần

## Bước 2: Design Rule
- Brand color 2 màu + 1 accent
- Font: 1 sans-serif family
- Heading 24-32pt, body 10-12pt
- White space generous (40%)
- Icon dùng Heroicons / Lucide free
- Image: 1 hero illustration

## Bước 3: 3 Variant theo Mục Đích
- **Event handout**: heavy visual, scan QR mạnh
- **Email attachment**: text-readable trên mobile preview
- **Channel sales kit**: có co-brand space cho partner logo

## Bước 4: Localization
Vietnamese + English version:
- Cùng layout
- Translate đúng tone
- Local proof (KH VN cho version VN)
- Compliance (Số ĐKKD, địa chỉ HCM/HN)

## Bước 5: Print + Digital
Build 2 version:
- **Print**: 300 DPI, CMYK, 5mm bleed
- **Digital**: 150 DPI, RGB, max 2MB PDF

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Canva/Figma MCP: design + version control
- Drive MCP: lưu template + share link
- Gmail MCP: attach gửi nhanh
- WebSearch: tìm font/icon free

**Fallback API:**
```python
# Generate one-pager PDF với reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
c = canvas.Canvas("onepager.pdf", pagesize=A4)
c.drawImage("logo.png", 30, 800, width=100, height=40)
c.setFont("Helvetica-Bold", 28)
c.drawString(30, 750, "Cut closing time by 30%")
# ... bullets, proof, CTA
c.save()
```

## Bước 7: Output Format
- **File 1**: `one_pager_<product>.pdf` — A4 print + digital
- **File 2**: `one_pager_<product>.docx` — editable Word
- **File 3**: `one_pager_<product>_en.pdf` — English version
- **File 4**: `one_pager_event_handout.pdf` — variant event
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Headline <12 từ
- [ ] 3 logo proof + 1 stat
- [ ] CTA rõ ràng (QR/email/link)
- [ ] White space 40%
- [ ] Print + Digital 2 file
- [ ] VN + EN version
- [ ] Brand guideline tuân thủ
