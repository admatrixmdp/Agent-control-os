---
name: cs-faq-knowledge-base
description: |
  Xây dựng Knowledge Base FAQ chuẩn cho phòng CSKH doanh nghiệp Việt Nam — có category, search, tag, version để agent tra cứu nhanh và khách tự phục vụ. Dùng skill này khi người dùng yêu cầu: "xây FAQ", "tạo knowledge base", "KB chăm sóc khách hàng", "thư viện câu hỏi thường gặp", "self-service help center", "tổng hợp FAQ sản phẩm", "FAQ shopee/website", "viết FAQ chuẩn". Output là Excel + Markdown KB sẵn sàng import lên Zendesk/Freshdesk/Intercom.
---

# CS FAQ Knowledge Base Builder

## Mục Tiêu
Tạo hệ thống FAQ có cấu trúc (category → sub-category → article) giúp giảm 40-60% ticket lặp lại, agent tra cứu trong 10 giây, và khách hàng tự phục vụ qua help center.

## Khi Nào Dùng
- Doanh nghiệp mới setup phòng CS chưa có KB
- KB cũ rối, không search được, agent vẫn hỏi nhau
- Cần migrate FAQ từ Word/Excel sang Zendesk/Freshdesk
- Launch sản phẩm mới cần FAQ tức thì
- Tỷ lệ self-service < 20%, muốn nâng lên 50%+

## Bước 1: Thu Thập Câu Hỏi Nguồn
Hỏi user 3 input:
- **Ngành/sản phẩm**: TMĐT, SaaS, F&B, dịch vụ...
- **Nguồn câu hỏi**: log chat, email tickets, comment FB, Shopee Q&A
- **Top 20-50 câu** khách hỏi nhiều nhất

Phân nhóm sơ bộ: Đặt hàng | Thanh toán | Vận chuyển | Đổi trả | Bảo hành | Tài khoản | Sản phẩm | Khác.

## Bước 2: Thiết Kế Cấu Trúc KB
Mỗi article có schema:
| Field | Mô tả |
|---|---|
| ID | KB-001, KB-002... |
| Category | Lv1 (Đặt hàng) |
| Sub-category | Lv2 (Hủy đơn) |
| Question | Câu hỏi khách (ngôn ngữ tự nhiên) |
| Short Answer | Trả lời 2-3 câu cho chatbot |
| Full Answer | Trả lời đầy đủ có step + ảnh |
| Tags | hủy-đơn, refund, COD |
| Owner | Team Order |
| Last Updated | 2026-05-28 |
| Status | Published / Draft |

## Bước 3: Viết Article Chuẩn
Mỗi article theo format:
- **Tiêu đề**: dạng câu hỏi khách hay gõ ("Làm sao hủy đơn đã thanh toán?")
- **TL;DR**: 1 câu trả lời
- **Chi tiết**: 3-5 bước, có screenshot
- **Liên quan**: link 2-3 article liên quan
- **Nếu vẫn lỗi**: nút "Liên hệ CSKH"

Viết tone thân thiện ngôi "bạn/anh chị", tránh từ chuyên môn.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets (mcp__6a1149b8): tạo bảng FAQ master, share team chỉnh sửa
- Gmail MCP: search email subject "câu hỏi", "tư vấn" để thu thập câu hỏi thật
- WebSearch: tìm FAQ chuẩn của đối thủ cùng ngành
- WebFetch: crawl page FAQ đối thủ tham khảo cấu trúc

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Bulk import FAQ lên Zendesk Help Center
import requests
ZD_DOMAIN = "company.zendesk.com"
auth = ("agent@co.vn/token", "API_TOKEN")
for article in faq_list:
    payload = {"article": {
        "title": article["question"],
        "body": article["full_answer"],
        "locale": "vi",
        "section_id": article["section_id"]
    }}
    r = requests.post(f"https://{ZD_DOMAIN}/api/v2/help_center/vi/sections/{article['section_id']}/articles.json",
                      json=payload, auth=auth)
    print(r.status_code, r.json().get("article", {}).get("id"))
```

## Bước 5: Output Format
- **File Excel `FAQ_Master_v1.xlsx`**: sheet "Articles" (full schema), sheet "Categories", sheet "Tags"
- **Folder Markdown `kb/`**: mỗi article 1 file `.md` để import Zendesk/Notion
- **Link Google Sheets** live editing
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-faq-knowledge-base/output/`

## Checklist Trước Khi Giao
- [ ] Tối thiểu 30 article cho doanh nghiệp nhỏ, 100+ cho lớn
- [ ] Mỗi article có TL;DR + bước chi tiết
- [ ] Có tag để search nhanh
- [ ] Tone ngôn ngữ thân thiện, ngôi "bạn/anh chị"
- [ ] Có owner + ngày review để duy trì
- [ ] Đã thử search 10 câu hỏi mẫu — ra đúng article
