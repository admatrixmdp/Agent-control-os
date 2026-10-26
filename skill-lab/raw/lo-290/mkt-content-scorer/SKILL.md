---
name: mkt-content-scorer
description: |
  Chấm điểm content marketing trước khi đăng cho doanh nghiệp Việt Nam — đo hook, clarity, CTA, brand voice, SEO. Cho điểm 0-100 + góp ý sửa. Kích hoạt khi người dùng nói: "chấm điểm content", "content scorer", "đánh giá bài đăng trước khi post", "review content trước khi đăng", "kiểm duyệt content", "QA content", "score post", "đánh giá content marketing". Output là báo cáo HTML scoring + suggestions.
---

# Chấm Điểm Content Trước Khi Đăng

## Mục Tiêu
Mọi bài viết/video script đều qua "vòng kiểm tra cuối" có chấm điểm khách quan, tránh đăng nội dung yếu làm giảm tăng trưởng kênh.

## Khi Nào Dùng
- Team có 5+ writer cần chuẩn hóa chất lượng
- Outsource agency/freelancer
- Onboard intern viết content
- QA hàng ngày trước publish
- Audit content cũ chưa hiệu quả

## Bước 1: Nhập Content + Context
Hỏi:
1. Loại content (FB post / blog / TikTok script / email)
2. Audience target
3. Mục tiêu (engage / click / sale)
4. Kênh đăng
5. Brand voice guide (link)
6. Nội dung cần chấm

## Bước 2: Chấm 6 Trục
Mỗi trục 0-100, tổng quy ra 0-100:
1. **Hook 3s** (20đ): câu mở có giữ chân không?
2. **Clarity** (15đ): rõ ràng, không lan man?
3. **Brand Voice** (15đ): khớp guide không?
4. **Value/Insight** (20đ): có giá trị thực hay nói chung chung?
5. **CTA** (15đ): có CTA rõ và phù hợp?
6. **SEO/Hashtag** (15đ): keyword/hashtag tối ưu?

Chấm chi tiết, mỗi trục có 2-3 dòng giải thích.

## Bước 3: Đề Xuất Cải Tiến
Mỗi điểm trừ → 1 gợi ý sửa cụ thể.
Ví dụ:
- Hook 12/20: "Câu mở quá chung 'AI đang phát triển nhanh'. Sửa: 'Tôi vừa cho AI làm 3 tiếng việc / tốn 50k. Đây là cách...'"
- CTA 8/15: "Không có CTA. Thêm: 'Comment 'AI' để nhận template'"

Phân loại điểm tổng:
- >85: Publish ngay
- 70-85: Sửa minor rồi đăng
- 50-70: Sửa major
- <50: Viết lại

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: kiểm tra topic đã viết chưa (tránh trùng)
- Notion MCP: lưu scoring history + theo dõi writer
- Sheets MCP: stats writer (điểm TB/tháng)
- Slack MCP: gửi feedback cho writer

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Chấm điểm dùng LLM với rubric
from anthropic import Anthropic
client = Anthropic()
def score(content, context):
    prompt = f'''Chấm điểm content sau theo 6 trục Hook (20), Clarity (15),
    Brand Voice (15), Value (20), CTA (15), SEO (15). Trả JSON.
    Context: {context}
    Content: {content}'''
    res = client.messages.create(model='claude-opus-4-5',
      max_tokens=2000, messages=[{'role':'user','content':prompt}])
    return res.content[0].text
```

## Bước 5: Output Format
- File HTML scoring report 1 trang
- File `.md` feedback chi tiết cho writer
- Tracker điểm theo writer/tháng
- Library best content (>90đ) làm reference
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Chấm đủ 6 trục
- [ ] Mỗi trục có giải thích
- [ ] Có gợi ý sửa cụ thể
- [ ] Phân mức Publish/Edit/Rewrite
- [ ] Tracker writer
- [ ] Đã đối chiếu brand voice guide
