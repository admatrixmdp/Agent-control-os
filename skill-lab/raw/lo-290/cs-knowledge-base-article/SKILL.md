---
name: cs-knowledge-base-article
description: |
  Viết article Knowledge Base hỗ trợ chuẩn cấu trúc Problem → Steps → Verify → Related cho self-service và Help Center — SEO, dễ scan, có screenshot, có metric đo lường. Dùng skill này khi người dùng yêu cầu: "viết KB article", "viết bài help center", "tutorial bài hỗ trợ", "how-to article CS", "self-service article", "bài viết FAQ chi tiết", "step-by-step guide", "SEO help article". Output là Markdown + HTML + JSON metadata.
---

# CS Knowledge Base Article Writer

## Mục Tiêu
Viết article hỗ trợ chuẩn cho Help Center / Zendesk / Notion — cấu trúc "Problem → Solution Steps → Verify → Related" — giúp KH self-serve, giảm 30-50% ticket cùng vấn đề, đồng thời SEO Google để bắt search intent.

## Khi Nào Dùng
- Cùng 1 câu hỏi lặp lại > 10 ticket/tuần → cần article
- Launch tính năng mới cần hướng dẫn
- KH search Google "{brand} làm sao..." → muốn rank top
- Migrate FAQ scattered sang KB chuẩn
- Onboard team CS có tài liệu reference

## Bước 1: Chọn Đề Tài Từ Data Ticket
- Pull top 20 intent volume cao nhất trong 30 ngày
- Filter những intent KH có thể tự giải quyết (không cần CSKH tay)
- Ưu tiên đề tài search Google volume cao (dùng Google Keyword Planner)

Ví dụ đề tài: "Làm sao đổi mật khẩu trên app", "Cách yêu cầu hoàn tiền đơn COD"

## Bước 2: Cấu Trúc Article 5 Phần
1. **Title** (60-70 ký tự, dạng câu hỏi)
   - "Làm sao đổi mật khẩu trên app {ten_app}?"
2. **TL;DR** (2-3 dòng): cho người scan
3. **Khi nào dùng article này**: 2-3 bullet KH self-identify
4. **Hướng dẫn từng bước** (3-7 bước, có screenshot)
   - Bước 1: ... (kèm ảnh)
   - Bước 2: ...
5. **Kiểm tra kết quả**: "Bạn đã làm đúng nếu thấy {dấu_hiệu}"
6. **Vẫn lỗi?**: link đến article liên quan + nút "Liên hệ CSKH"
7. **Bài liên quan**: 2-3 link

## Bước 3: Viết Theo Nguyên Tắc SEO + UX
**SEO:**
- Title chứa keyword chính
- H2 chứa biến thể keyword
- 300-800 từ là vừa
- Có alt text cho screenshot
- Internal link 2-3 article cùng category

**UX:**
- Ngôi "bạn"
- Câu ngắn < 20 từ
- Bullet thay paragraph dài
- Số bước có thứ tự (Bước 1, 2, 3)
- Code/đường dẫn dùng `font monospace`

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Zendesk Help Center / Notion: import article
- Google Sheets: track view count + thumbs-up/down
- Gmail MCP: notify team CS khi article mới publish
- Slack MCP: post link article cho team biết để paste vào ticket
- WebSearch: research keyword volume + top result cạnh tranh
- WebFetch: tham khảo article cùng đề tài

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Auto-publish article vào Zendesk Help Center
import requests
auth = ("agent@co.vn/token", "TOKEN")
def publish(article):
    payload = {"article": {
        "title": article["title"],
        "body": article["body_html"],
        "locale": "vi",
        "user_segment_id": None,
        "permission_group_id": ARTICLE_PERM_GROUP_ID,
        "label_names": article["tags"]
    }}
    r = requests.post(f"https://co.zendesk.com/api/v2/help_center/vi/sections/{article['section_id']}/articles.json",
                      json=payload, auth=auth)
    return r.json()["article"]["id"]
```

## Bước 5: Output Format
- **Markdown file** `.md` mỗi article
- **HTML responsive** preview
- **JSON metadata**: title, tags, section, owner, last_review_date
- **Excel `KB_Articles_Index.xlsx`**: list tất cả article + view + thumbs
- **Screenshot folder** `assets/article-id/`
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-knowledge-base-article/output/`

## Checklist Trước Khi Giao
- [ ] Title dạng câu hỏi, có keyword
- [ ] Có TL;DR ≤ 3 dòng
- [ ] Bước < 7, có screenshot mỗi bước
- [ ] Có "Kiểm tra kết quả" rõ ràng
- [ ] Có link "Vẫn lỗi" → CSKH
- [ ] Internal link 2-3 article liên quan
- [ ] Có thumbs feedback để đo "helpful?"
