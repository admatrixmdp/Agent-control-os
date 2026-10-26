# SPEC TẠO SKILL.md — DÙNG CHO MỌI BATCH

## 1. Cấu trúc thư mục

Mỗi skill là một thư mục riêng, chứa file `SKILL.md`:
```
/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/<skill-name>/SKILL.md
```

## 2. Format SKILL.md (80-150 dòng, tiếng Việt)

```markdown
---
name: <skill-name>
description: |
  <2-4 câu mô tả skill bằng tiếng Việt. PHẢI có:
  - Nêu skill làm gì
  - Liệt kê 6-10 trigger phrases trong dấu ngoặc kép: "trigger 1", "trigger 2", ...
  - Câu chốt "Output là <markdown/HTML/Excel/PDF/.docx/.pptx>"
---

# <Tên Skill Đầy Đủ>

## Mục Tiêu
<1 đoạn ngắn nêu vấn đề skill giải quyết + giá trị mang lại>

## Khi Nào Dùng
<3-5 bullet tình huống điển hình>

## Bước 1: <Tên bước>
<Hướng dẫn cụ thể, có ví dụ ngắn>

## Bước 2: <Tên bước>
<...>

## Bước 3: <Tên bước>
<...>

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- <connector 1 phù hợp>: <dùng để làm gì>
- <connector 2 phù hợp>: <dùng để làm gì>
- WebSearch: <khi nào dùng>
- WebFetch: <khi nào dùng>

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Ví dụ ngắn gọi API thật của dịch vụ (Facebook Ads, Google Sheets, Shopee Open, etc.)
# 5-15 dòng code mẫu
```

## Bước 5: Output Format
<Mô tả định dạng output: HTML/Excel/PDF/Docx/Slide/Markdown>
<Nêu file path lưu vào /Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/... (hoặc outputs)>

## Checklist Trước Khi Giao
- [ ] <điểm 1>
- [ ] <điểm 2>
- [ ] <điểm 3>
- [ ] <điểm 4>
- [ ] <điểm 5>
```

## 3. Nguyên tắc nội dung

- **Tiếng Việt** xuyên suốt (trừ thuật ngữ chuyên ngành)
- Skill nào liên quan **web/MCP** thì PHẢI có Bước 4 "Tích Hợp Web Bên Ngoài"
- Trigger phrases trong description phải đa dạng (formal + colloquial)
- Tránh trùng nội dung với 50 skill đã có (xem thư mục `/sessions/tender-lucid-darwin/mnt/.claude/skills/`)
- Mỗi skill độc lập, dùng được riêng lẻ

## 4. Mục tiêu cuối

Mỗi skill phải giúp doanh nghiệp:
- TỰ ĐỘNG HOÁ một quy trình thường lệ
- TỐI ƯU CHI PHÍ (thời gian/tiền)
- TĂNG TỐC THỰC THI

Tránh skill chỉ là "giải thích lý thuyết". Phải có **output cụ thể** mà NV có thể giao ngay cho sếp/khách.
