---
name: sales-sales-deck-builder
description: |
  Tạo sales deck 12 slide chuẩn flow Pain → Reframe → Solution → Proof → Pricing → Close. Trigger phrases: "tạo sales deck", "build pitch deck", "sales deck 12 slide", "deck bán hàng B2B", "soạn slide pitch sales", "deck giới thiệu sản phẩm", "viết sales deck", "powerpoint bán hàng", "tạo deck cho AE", "sales presentation deck". Output là PPT 12 slide + script speaker note.
---

# Sales Deck Builder (12 Slide)

## Mục Tiêu
Tạo sales deck 12 slide cho AE pitch demo / executive meeting đạt feedback "rõ ràng + thuyết phục" theo flow Pain → Reframe → Solution → Proof → Pricing → Close.

## Khi Nào Dùng
- Launch sản phẩm mới cần deck
- Refresh deck cũ outdated
- Customize deck cho vertical/persona mới
- Trước customer kickoff meeting
- Roadshow / event pitch

## Bước 1: 12 Slide Structure

1. **Title** — KH name + date, 1 dòng value prop
2. **The Shift** — xu hướng ngành (1 chart/data)
3. **Old Way Pain** — niềm tin cũ tốn cost gì
4. **Reframe** — new way of thinking
5. **Solution Overview** — sản phẩm 1 hình + 3 dòng
6. **Use Case 1** — pain X → solution → outcome
7. **Use Case 2** — pain Y → solution → outcome
8. **Use Case 3** — pain Z → solution → outcome
9. **Proof** — 3 logo + 1 case study số liệu
10. **Differentiator** — tại sao mình vs đối thủ
11. **Pricing** — 3 tier (Good/Better/Best)
12. **Next Step** — 3 option CTA

## Bước 2: Design Principle
- Max 30 từ/slide (không wall of text)
- 1 visual mỗi slide (chart/screenshot/icon)
- Color: 2 màu brand + 1 accent
- Font: 1 family (vd Inter), 3 size
- Slide background không quá rối

## Bước 3: Speaker Notes (2-3 dòng/slide)
Mỗi slide có note:
- Talking point chính (10s)
- 1 câu hỏi trial close
- Transition câu sang slide tiếp

Tổng deck 15-20 phút speak.

## Bước 4: Variant theo Persona
Build 3 version:
- **CFO version**: heavy ROI, TCO, payback
- **COO version**: efficiency, process, automation
- **CMO version**: growth, brand, customer experience

Slide chung 60%, customize 40%.

## Bước 5: A/B Test Hook
Slide 1-4 (hook) test:
- Pain-first vs Vision-first
- Data shock vs Story
- Question vs Statement

Test với 5-10 prospect, đo engagement.

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- PPT/Google Slides MCP: tạo deck
- Drive MCP: lưu template + version
- Salesforce MCP: track deck nào win rate cao
- Gong MCP: phân tích slide nào KH dừng lâu

**Fallback API:**
```python
# PPT auto-generate from template
from pptx import Presentation
ppt = Presentation("master_deck.pptx")
ppt.slides[0].placeholders[1].text = f"{customer} | {date}"
ppt.slides[6].placeholders[1].text = f"Pain: {pain_1}"
# Customize per persona
if persona == "CFO":
    ppt.slides[10].chart.add_series("ROI", roi_data)
ppt.save(f"deck_{customer}_{persona}.pptx")
```

## Bước 7: Output Format
- **File 1**: `sales_deck_master.pptx` — template 12 slide
- **File 2**: `sales_deck_<persona>.pptx` — 3 variant CFO/COO/CMO
- **File 3**: `speaker_notes.md` — script chi tiết
- **File 4**: `deck_AB_test_results.xlsx` — track engagement
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ 12 slide flow chuẩn
- [ ] <30 từ/slide
- [ ] Speaker note 2-3 dòng
- [ ] 3 persona variant
- [ ] Pricing có 3 tier
- [ ] Next step CTA rõ
- [ ] Test với 3 AE trước rollout
