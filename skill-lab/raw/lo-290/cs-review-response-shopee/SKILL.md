---
name: cs-review-response-shopee
description: |
  Trả lời review Shopee / Lazada / Tiki / Google My Business chuẩn — template theo 1-5 sao, tone phù hợp sàn, SEO local, tránh vi phạm. Dùng skill này khi người dùng yêu cầu: "trả lời review Shopee", "reply review Lazada", "phản hồi Google review", "template review sàn TMĐT", "trả lời 1 sao 2 sao", "engagement review online", "auto reply review", "SEO Google review". Output là template Markdown + Excel + auto-reply API.
---

# CS Review Response — Marketplace & Google

## Mục Tiêu
Tạo bộ template + quy trình trả lời 100% review trên Shopee / Lazada / Tiki / Google trong 24h — biến review 1-2 sao thành cơ hội cứu KH, biến 5 sao thành social proof, tăng SEO local + thứ hạng shop.

## Khi Nào Dùng
- Shop có nhiều review không trả lời
- Tỷ lệ 1-2 sao tăng, không có quy trình xử lý
- Cần SEO Google My Business
- Sàn cho điểm shop dựa "% review được trả lời"
- Brand mới mở rộng đa sàn cần đồng nhất tone

## Bước 1: Phân Loại Review Theo Sao
| Sao | Tỷ lệ thông thường | Goal phản hồi |
|---|---|---|
| **5 sao** | 60-70% | Cảm ơn ngắn + xin chia sẻ thêm |
| **4 sao** | 15-20% | Cảm ơn + hỏi cần cải thiện gì |
| **3 sao** | 5-10% | Xin lỗi + đề xuất bù đắp |
| **2 sao** | 3-5% | Xin lỗi sâu + kéo offline xử lý |
| **1 sao** | 2-3% | Xin lỗi + tag manager + đề xuất refund/đổi |

## Bước 2: Template Mỗi Mức Sao
**5 sao:**
```
Cảm ơn anh/chị {ten} đã chia sẻ trải nghiệm tích cực với {ten_sp}!
Đội ngũ {ten_shop} rất vui khi sản phẩm phù hợp với anh/chị.
Hẹn anh/chị lần sau với nhiều ưu đãi mới ạ.
```

**1 sao:**
```
Em rất tiếc khi đọc đánh giá của anh/chị về {ten_sp}.
Em là {ten_agent} - quản lý CSKH của {ten_shop}.
Để xử lý nhanh nhất, em xin phép gọi anh/chị qua số đã đăng ký
trong vòng 24h. Em sẽ chịu trách nhiệm cá nhân để đảm bảo
anh/chị hài lòng. Mong anh/chị thông cảm.
Em xin lỗi một lần nữa.
```

Quy tắc: KHÔNG defensive, KHÔNG đổ lỗi, ĐƯA hành động cụ thể.

## Bước 3: SEO Tip Cho Google Review
- Trong reply có nhắc keyword: "{tên brand} + {dịch vụ chính} + {thành phố}"
  - Ví dụ: "Quán Cà Phê An — quận 7" thay vì chỉ "shop"
- Mention tên đường / khu vực nếu có
- Trả lời > 50 từ để Google index
- Trả lời trong 7 ngày → tăng trust signal

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets: log review + reply + status
- Gmail MCP: thông báo khi review 1-2 sao mới
- Slack MCP: alert kênh #shop-reviews mọi 1-3 sao
- WebSearch: nghiên cứu review chuẩn của shop top
- WebFetch: pull review page Shopee/Lazada (nếu chưa có API)
- Browser MCP: screenshot review viral nếu cần

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Auto-pull review từ Shopee Open Platform + match template
import requests
PARTNER_ID = "..."; SHOP_ID = "..."; ACCESS_TOKEN = "..."
def fetch_reviews():
    r = requests.get("https://partner.shopeemobile.com/api/v2/shop_reviews/get_review",
        params={"partner_id": PARTNER_ID, "shop_id": SHOP_ID,
                "access_token": ACCESS_TOKEN, "page_no": 1, "page_size": 50})
    for rv in r.json()["response"]["item_list"]:
        if not rv["reply"]:
            template = pick_template(rv["rating_star"], rv["comment"])
            reply_review(rv["order_sn"], template)
```

## Bước 5: Output Format
- **Markdown library** `Review_Templates.md`: 5 mức sao × 5-10 biến thể
- **Excel `Review_Log.xlsx`**: review + reply + agent + sentiment
- **Google My Business** template SEO-optimized
- **Auto-reply script** Python
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-review-response-shopee/output/`

## Checklist Trước Khi Giao
- [ ] Template cho cả 5 mức sao
- [ ] Tone phù hợp từng sàn (Shopee thoải mái, Google formal hơn)
- [ ] Có biến thể tránh máy móc lặp lại
- [ ] Có SEO keyword cho Google review
- [ ] Quy trình kéo 1-2 sao offline xử lý
- [ ] Đo lường % review được trả lời trong 24h
