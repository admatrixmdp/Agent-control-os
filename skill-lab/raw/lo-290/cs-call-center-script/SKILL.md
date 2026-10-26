---
name: cs-call-center-script
description: |
  Soạn script tổng đài inbound (KH gọi vào) và outbound (gọi ra) cho team CSKH — opening, discovery, handling objection, closing, đo KPI AHT/FCR. Dùng skill này khi người dùng yêu cầu: "script tổng đài", "script call center", "kịch bản gọi điện CSKH", "script telesale", "training tổng đài viên", "script outbound CSKH", "kịch bản inbound", "telephony script". Output là Markdown script + Excel KPI + dialog roleplay.
---

# CS Call Center Script Designer

## Mục Tiêu
Tạo script chuẩn cho tổng đài inbound + outbound — giúp NV mới có thoại 80% chuẩn ngay tuần đầu, AHT (Average Handle Time) ≤ 5 phút, FCR (First Call Resolution) > 70%.

## Khi Nào Dùng
- Mới setup tổng đài, NV chưa có script
- AHT quá dài, NV "lan man" mất thời gian
- FCR thấp, KH phải gọi lại nhiều lần
- Cần đào tạo NV mới nhanh (onboarding)
- Launch campaign outbound (chăm sóc / upsell)

## Bước 1: Phân Loại Cuộc Gọi
**Inbound:**
- Hỏi thông tin (sản phẩm, giá)
- Khiếu nại / phản ánh
- Yêu cầu hỗ trợ kỹ thuật
- Theo dõi đơn / refund

**Outbound:**
- Welcome call (KH mới mua)
- Chăm sóc sau bán (sau 7/30 ngày)
- Đòi nợ nhẹ (đơn quá hạn thanh toán)
- Upsell / renewal

## Bước 2: Cấu Trúc Script Chuẩn (Inbound)
1. **Greeting** (5s): "Tổng đài {ten_cty} xin nghe, em là {ten}, em hỗ trợ gì ạ?"
2. **Identify** (15s): xin tên + SĐT + mã KH/đơn
3. **Active Listening** (30-60s): nghe vấn đề, không ngắt lời, tóm tắt lại
4. **Problem Solving** (2-3 phút): giải pháp + thực hiện
5. **Confirmation** (15s): "Em đã xử lý [X], anh chị còn cần gì nữa?"
6. **Closing** (10s): cảm ơn + chúc + chào

Mỗi bước có thoại mẫu + câu chuyển nối.

## Bước 3: Handling Objection & Câu Khó
**Bảng đáp ứng câu khó:**
| KH nói | Đáp |
|---|---|
| "Sao trễ thế?" | "Em hiểu sự bất tiện, em check ngay và update trong 5 phút" |
| "Cho gặp sếp!" | "Để em chuyển bộ phận chuyên trách, anh chị giữ máy 2 phút" |
| "Tôi đăng FB cho coi" | "Em xin lỗi và rất muốn giải quyết ngay cho anh chị, em ghi nhận và đề xuất [Y]" |
| "Refund hay không?" | "Theo chính sách [Điều X], anh chị được hoàn [%] trong [N] ngày" |

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets: log call + outcome + agent performance
- Slack MCP: alert khi có call >10 phút (overrun AHT)
- Gmail MCP: gửi summary call cho KH qua email sau cuộc gọi
- WebSearch: best practice script Zappos/Vinhomes hotline
- WebFetch: nghiên cứu IVR menu của brand cùng ngành

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Pull call log từ tổng đài cloud (3CX/Stringee) + dashboard
import requests
H = {"Authorization": "Bearer API_KEY"}
r = requests.get("https://api.stringee.com/v1/call/logs", headers=H,
                 params={"from": "2026-05-27", "to": "2026-05-28"})
for call in r.json()["calls"]:
    duration = call["duration"]
    if duration > 600:
        log_to_sheet(call, flag="overrun")
    if call["status"] == "missed":
        log_to_sheet(call, flag="missed")
```

## Bước 5: Output Format
- **Markdown script** đầy đủ Inbound + Outbound (mỗi loại 1 file)
- **Excel `Call_KPI.xlsx`**: AHT, FCR, miss rate, agent leaderboard
- **Cheat sheet A4**: in dán bàn tổng đài
- **Roleplay scenario**: 5 case Inbound + 3 case Outbound
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-call-center-script/output/`

## Checklist Trước Khi Giao
- [ ] Script có 6 bước rõ ràng
- [ ] Có bảng handling 10+ objection
- [ ] Phân biệt Inbound vs Outbound
- [ ] AHT target ≤ 5 phút, có timer guide trong script
- [ ] Có roleplay tối thiểu 5 scenario
- [ ] KPI sheet update tự động từ tổng đài
