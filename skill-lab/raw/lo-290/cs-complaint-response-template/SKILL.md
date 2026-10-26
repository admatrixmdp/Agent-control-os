---
name: cs-complaint-response-template
description: |
  Tạo template trả lời than phiền/khiếu nại của khách hàng theo công thức HEARD (Hear-Empathize-Apologize-Resolve-Diagnose) — chuyên nghiệp, hạ nhiệt, không nhận lỗi quá đà. Dùng skill này khi người dùng yêu cầu: "viết thư trả lời khiếu nại", "template trả lời than phiền", "phản hồi khách bức xúc", "xử lý complaint", "trả lời 1 sao", "viết reply phàn nàn", "hạ nhiệt khách nóng giận", "công thức HEARD CS". Output là email/Zalo/comment template + script điện thoại.
---

# CS Complaint Response Template Generator

## Mục Tiêu
Tạo template trả lời 5-10 tình huống khiếu nại phổ biến — giúp agent CS xử lý nhanh, đúng tone, không làm khách nóng thêm, không nhận trách nhiệm pháp lý quá đà.

## Khi Nào Dùng
- KH đăng FB chỉ trích, comment 1 sao Shopee
- Email/inbox phàn nàn dài, cảm xúc tiêu cực
- Agent mới chưa biết cách hạ nhiệt
- Cần phản hồi nhanh trước khi viral
- Standardize tone để mọi agent xử lý đồng nhất

## Bước 1: Phân Loại Than Phiền
| Loại | Ví dụ | Tone phù hợp |
|---|---|---|
| **Chất lượng SP** | "Hàng dởm, không như quảng cáo" | Xin lỗi + đề xuất đổi/hoàn |
| **Vận chuyển** | "Giao trễ 5 ngày" | Xin lỗi + giải thích + bồi thường nhẹ |
| **Thái độ NV** | "Em CS láo, trả lời cộc lốc" | Xin lỗi sâu + cam kết training |
| **Lừa đảo cảm nhận** | "Tôi sẽ kiện, đăng báo" | Thận trọng, không thừa nhận lỗi pháp lý |
| **Hiểu lầm chính sách** | "Sao bắt tôi trả phí ship trả?" | Giải thích nhẹ nhàng, dẫn link policy |

## Bước 2: Áp Dụng Công Thức HEARD
**H**ear — Lắng nghe: "Cảm ơn anh chị đã phản ánh"
**E**mpathize — Thấu cảm: "Em hiểu sự bất tiện anh chị gặp phải"
**A**pologize — Xin lỗi (có điều kiện): "Em xin lỗi vì trải nghiệm chưa tốt"
**R**esolve — Giải quyết: "Em đề xuất [hành động cụ thể] trong [thời gian]"
**D**iagnose — Tìm hiểu sâu (nếu cần): "Cho em hỏi thêm [chi tiết X]"

## Bước 3: Viết 5-10 Template Theo Tình Huống
Mỗi template có:
- **Tình huống**: mô tả khi nào dùng
- **Tone**: mức độ xin lỗi (nhẹ/trung/sâu)
- **Body**: full text có placeholder
- **Lưu ý pháp lý**: KHÔNG nói gì để tránh bẫy

Ví dụ:
```
[Tình huống]: KH đăng FB tố sản phẩm hỏng + đe doạ kiện
[Tone]: Sâu, kéo offline

"Chào anh/chị {ten_kh},
Em là {ten_agent} của {ten_cty}. Em đã đọc bài đăng của anh/chị và rất tiếc
về trải nghiệm anh/chị gặp phải với sản phẩm {ten_sp}.
Để xử lý nhanh và đúng nhất, em xin phép liên hệ riêng anh/chị qua
số {sdt_kh}. Em cam kết phản hồi trong 24h với phương án cụ thể.
Mong anh/chị cho phép em xử lý riêng để bảo mật thông tin và đảm bảo
quyền lợi tốt nhất. Trân trọng."

[Lưu ý]: KHÔNG nhận "sản phẩm có lỗi" trên public — chỉ "trải nghiệm chưa tốt"
```

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Gmail MCP: tạo draft trả lời email khiếu nại
- Slack MCP: chuyển vụ phức tạp vào channel #complaint-war-room
- Google Sheets: log mọi complaint + cách xử lý → analytics
- WebSearch: tra cứu best practice xử lý FB rant, Shopee 1-star
- WebFetch: lấy ngữ cảnh public post để biết khách viết gì

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Auto-reply comment 1-2 sao Shopee
import requests
def reply_shopee_review(review_id, rating, comment):
    if rating <= 2:
        # Match template theo keyword
        if "trễ" in comment.lower():
            template = TEMPLATE_LATE_DELIVERY
        elif "hỏng" in comment.lower():
            template = TEMPLATE_DEFECT
        else:
            template = TEMPLATE_GENERIC
        # Gọi Shopee Partner API reply
        requests.post("https://partner.shopeemobile.com/api/v2/shop/reply_review",
                      json={"review_id": review_id, "reply": template})
```

## Bước 5: Output Format
- **Markdown library** `Complaint_Templates.md` có 10+ template
- **Excel** `ComplaintLog.xlsx` để track case + outcome
- **Script điện thoại** kèm dialog mẫu cho hotline
- **Cheat sheet 1 trang** A4 in dán bàn agent
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-complaint-response-template/output/`

## Checklist Trước Khi Giao
- [ ] Tối thiểu 10 template phủ tình huống chính
- [ ] Mỗi template áp dụng HEARD đầy đủ
- [ ] Lưu ý pháp lý: không nhận lỗi quá đà public
- [ ] Có hướng dẫn "Kéo offline" cho case nóng
- [ ] Template có placeholder rõ
- [ ] Đã roleplay 3 case mẫu với agent
