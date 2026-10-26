---
name: mkt-blog-article-writer
description: |
  Viết bài blog SEO tiếng Việt 1500-3000 từ chuẩn EEAT (Experience, Expertise, Authoritativeness, Trust) cho doanh nghiệp. Tự động cấu trúc theo intent, tối ưu keyword, chèn FAQ và schema gợi ý. Kích hoạt khi người dùng nói: "viết bài blog SEO", "viết article chuẩn EEAT", "viết bài 2000 từ", "viết blog post", "viết content website", "viết bài chuẩn SEO", "viết bài cho blog công ty", "viết bài thought leadership". Output là file Markdown + Word.
---

# Viết Bài Blog SEO Chuẩn EEAT

## Mục Tiêu
Sản xuất bài blog dài 1500-3000 từ chất lượng cao, đáp ứng tiêu chuẩn EEAT của Google 2024-2026, vừa lên top SERP vừa giữ chân người đọc 4+ phút.

## Khi Nào Dùng
- Cần bài pillar/cluster theo content map
- Viết bài cạnh tranh top 3 SERP
- Bài tận dụng kiến thức chuyên gia nội bộ
- Bài cần đứng được lâu (evergreen)
- Bài có thể tái sử dụng cho video/podcast

## Bước 1: Thu Thập Brief
Hỏi user:
1. Keyword chính + 5-10 keyword phụ
2. Intent (I/C/T)
3. Đối tượng (persona)
4. USP/POV độc đáo
5. Tài liệu nội bộ (case study, số liệu)
6. URL top 3 SERP đang đứng để tham khảo

## Bước 2: Xây Outline Chuẩn EEAT
- H1 chứa keyword + lợi ích
- Intro 100-150 từ: hook + promise + signal authority (kinh nghiệm/dữ liệu)
- 6-10 H2 trả lời lần lượt search intent
- Mỗi H2: 200-350 từ + ví dụ thực tế hoặc số liệu
- Box "Insight từ chuyên gia" 2-3 lần trong bài
- FAQ 5-7 câu cuối bài
- CTA cuối: download/đăng ký/contact

## Bước 3: Viết Nội Dung
Quy tắc:
- Câu ngắn 15-20 từ
- Đoạn 3-4 dòng
- Bullet/numbered list sau mỗi 200 từ
- Inject keyword tự nhiên (mật độ 1-1.5%)
- Trích nguồn uy tín (gov, edu, báo lớn) 3-5 link
- Chèn ảnh gợi ý + alt text
- Có ít nhất 1 bảng so sánh

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tra số liệu, thống kê mới nhất 2026
- WebFetch: đọc top 3 SERP để hiểu gap
- Google Drive MCP: lưu bản Word
- Notion MCP: đẩy bài vào CMS pipeline
- Wordpress connector (nếu có): publish draft

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Đẩy bài vào WordPress qua REST API
import requests
r = requests.post('https://abc.vn/wp-json/wp/v2/posts',
  auth=('user','app_password'),
  json={'title':title,'content':html_body,'status':'draft',
        'categories':[5],'tags':[12,15]})
print(r.json()['link'])
```

## Bước 5: Output Format
- File `.md` + `.docx` tên `Blog_<keyword>_<date>`
- Kèm bản schema FAQ JSON-LD copy paste được
- Kèm meta title + meta description đã tối ưu
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ 1500+ từ
- [ ] Keyword chính xuất hiện trong title, H1, intro, conclusion
- [ ] Có ít nhất 3 link external + 3 internal link gợi ý
- [ ] FAQ 5-7 câu có schema
- [ ] EEAT signal rõ (tác giả, kinh nghiệm, số liệu nguồn)
- [ ] Đã có meta + slug + alt ảnh
