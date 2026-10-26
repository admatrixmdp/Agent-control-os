---
name: mkt-tagline-generator
description: |
  Sinh 10 phương án tagline thương hiệu/sản phẩm Việt Nam kèm lý do chọn từng câu, ngắn 3-7 từ, dễ nhớ. Theo 5 framework (Benefit/Promise/Action/Emotion/Mystery). Kích hoạt khi người dùng nói: "viết tagline", "slogan thương hiệu", "câu định vị ngắn", "viết slogan", "đặt slogan", "tagline brand", "tagline campaign", "câu khẩu hiệu". Output là Markdown 10 option.
---

# Tagline Generator — 10 Option + Lý Do

## Mục Tiêu
Cung cấp 10 phương án tagline để founder/CMO chọn nhanh, mỗi câu đều có lý lẽ tại sao đáng chọn, tránh tình trạng tagline nghe hay nhưng vô nghĩa.

## Khi Nào Dùng
- Đi cùng positioning statement mới
- Launch campaign lớn cần claim mới
- Refresh brand
- Pitch khách hàng B2B
- Đăng ký bản quyền tên

## Bước 1: Brief
Hỏi:
1. Tên brand + lĩnh vực
2. Positioning statement (nếu có)
3. Audience chính
4. USP/Promise lớn nhất
5. Đối thủ tagline ra sao
6. Ngôn ngữ (VI/EN/song ngữ)
7. Độ dài ưa thích (3-5 từ / 6-7 từ / 1 câu hoàn chỉnh)

## Bước 2: Sinh Tagline Theo 5 Framework
1. **Benefit-led**: lợi ích trực tiếp ("Vay nhanh trong 5 phút")
2. **Promise**: cam kết ("Just do it" - Nike)
3. **Action verb**: kích thích hành động ("Think different" - Apple)
4. **Emotion**: cảm xúc ("Mua nhanh, sống chậm")
5. **Mystery/Curiosity**: gợi tò mò ("Đừng ngại khác biệt")

Mỗi framework sinh 2 tagline → 10 phương án.

## Bước 3: Chấm Điểm & Lý Do
Mỗi tagline chấm 4 tiêu chí (1-10):
- Memorable (dễ nhớ)
- Distinctive (khác biệt với đối thủ)
- Relevant (đúng audience)
- Action (gợi hành động/cảm xúc)

Viết 2-3 dòng lý do cho mỗi câu. Sort theo tổng điểm.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tra tagline đối thủ + cùng ngành
- WebFetch: check trùng tagline đã có
- Google Drive MCP: lưu deck
- Slack MCP: tổ chức poll team chọn
- Notion MCP: lưu brand bible

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tự sinh tagline qua API LLM
from anthropic import Anthropic
client = Anthropic()
msg = client.messages.create(model='claude-opus-4-5',
  max_tokens=1000,
  messages=[{'role':'user','content':
    f'Viết 10 tagline 5 framework cho brand: {brief_text}'}])
```

## Bước 5: Output Format
- File `.md` 10 tagline xếp hạng + lý do
- Slide 1 trang trình bày top 3
- Audio test (đọc to để check phát âm)
- Phương án Tiếng Anh tương ứng (nếu cần)
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 10 tagline đa dạng 5 framework
- [ ] Mỗi câu có lý do chọn
- [ ] Đã chấm điểm 4 tiêu chí
- [ ] Đã check trùng đối thủ
- [ ] Đọc to mượt
- [ ] Có bản EN nếu brand quốc tế
