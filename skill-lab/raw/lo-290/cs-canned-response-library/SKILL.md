---
name: cs-canned-response-library
description: |
  Xây dựng thư viện canned response (macro/reply mẫu) 30+ tình huống cho agent CSKH — chuẩn tone, đúng pháp lý, có biến số {ten_kh}, {ma_don} để paste nhanh. Dùng skill này khi người dùng yêu cầu: "tạo canned response", "macro Zendesk", "reply mẫu", "template trả lời khách", "thư viện câu trả lời", "quick reply chăm sóc", "macro tổng đài", "kịch bản trả lời email". Output là Excel + file .csv import Zendesk/Freshdesk/Intercom.
---

# CS Canned Response Library

## Mục Tiêu
Tạo 30-60 mẫu trả lời chuẩn cho các tình huống CSKH phổ biến (chào hỏi, xin lỗi, giải thích chính sách, đóng ticket) — giảm thời gian xử lý 50%, đảm bảo tone đồng nhất.

## Khi Nào Dùng
- Onboard agent CS mới, chưa rành chính sách
- Volume ticket tăng, agent phải gõ tay → chậm
- Tone trả lời không đồng nhất giữa các agent
- Setup mới Zendesk/Freshdesk/Intercom cần import macro
- Cần chuẩn hoá phản hồi để giám sát chất lượng

## Bước 1: Liệt Kê 30+ Tình Huống Phổ Biến
Phân nhóm:
- **Chào hỏi & đóng ticket** (5): chào đầu, hỏi thêm, cảm ơn, hẹn callback, đóng case
- **Order & vận chuyển** (8): xác nhận đơn, đang giao, trễ hàng, sai địa chỉ, đổi địa chỉ...
- **Thanh toán & hoàn tiền** (6): hướng dẫn thanh toán, lỗi giao dịch, hoàn tiền 3-5 ngày, giảm giá...
- **Đổi trả & bảo hành** (6): điều kiện đổi trả, mở yêu cầu, gửi sản phẩm về, hết bảo hành...
- **Khiếu nại** (5): xin lỗi, đang điều tra, đã giải quyết, escalate manager...

## Bước 2: Viết Mỗi Template
Format mỗi template:
```
[ID]: CR-012
[Title]: Xin lỗi giao trễ + cập nhật tình trạng
[Use khi]: KH phản ánh đơn trễ > 2 ngày
[Tone]: Xin lỗi chân thành, không đổ lỗi vận chuyển

Chào anh/chị {ten_kh},

Em xin lỗi vì đơn hàng {ma_don} đến tay anh/chị chậm hơn dự kiến.
Em đã kiểm tra và xác nhận đơn đang ở {vi_tri_hien_tai}, dự kiến giao
trong vòng {so_ngay} ngày tới.

Để xin lỗi, em đã gửi tặng anh/chị mã giảm giá {ma_voucher} cho đơn
tiếp theo. Mong anh/chị thông cảm.

Trân trọng,
{ten_agent} — CSKH {ten_cty}
```

Có placeholder rõ ràng để dễ điền tự động.

## Bước 3: Quy Tắc Tone & Pháp Lý
- Ngôi xưng: "em / anh chị" (B2C), "chúng tôi / quý khách" (B2B)
- KHÔNG hứa thời gian cụ thể nếu chưa chắc
- KHÔNG nói "bên vận chuyển làm sai" → nói "đang phối hợp xử lý"
- Refund: nêu rõ "3-5 ngày làm việc theo Điều X chính sách"
- Bồi thường: chỉ đưa voucher trong quyền hạn agent (≤ 50K)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets: master file template để team review & version
- Gmail MCP: tạo draft template từ canned response để gửi nhanh
- Slack MCP: pin top 10 macro vào channel #cs-team
- WebSearch: tham khảo template Zendesk best practice
- WebFetch: fetch trang Help Center của brand để align tone

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Import macro lên Zendesk
import requests, json
auth = ("agent@co.vn/token", "TOKEN")
for m in macros:
    payload = {"macro": {
        "title": m["title"],
        "actions": [{"field": "comment_value", "value": m["body"]}],
        "restriction": None
    }}
    r = requests.post("https://co.zendesk.com/api/v2/macros.json",
                      json=payload, auth=auth)
    print(r.status_code, r.json().get("macro", {}).get("id"))
```

## Bước 5: Output Format
- **File Excel `CannedResponse_v1.xlsx`**: cột ID, Title, Use Case, Body, Tone, Owner
- **File `.csv`** chuẩn import Zendesk/Freshdesk
- **File Markdown** cho team đọc dạng playbook
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-canned-response-library/output/`

## Checklist Trước Khi Giao
- [ ] Tối thiểu 30 template phủ 80% tình huống thường gặp
- [ ] Mỗi template có placeholder rõ ràng
- [ ] Tone đồng nhất, đã review pháp lý
- [ ] Có "Use khi" để agent chọn đúng
- [ ] Đã test paste vào Zendesk, hiển thị OK
- [ ] Có file .csv import được
