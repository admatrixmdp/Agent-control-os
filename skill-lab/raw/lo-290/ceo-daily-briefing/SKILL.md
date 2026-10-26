---
name: ceo-daily-briefing
description: |
  Tạo bản briefing sáng cho CEO tổng hợp toàn bộ email quan trọng, tin nhắn Slack, lịch họp và quyết định cần xử lý từ tối qua đến sáng nay — gói gọn trong 1 trang đọc trong 5 phút.
  Kích hoạt khi người dùng nói: "briefing sáng CEO", "tổng hợp email tối qua", "bản tin sáng CEO", "daily brief", "morning brief CEO", "tóm tắt việc cần xử lý hôm nay", "review sáng cho sếp", "bản tin sếp tổng".
  Output là Markdown/HTML 1 trang gửi qua email lúc 6h sáng.
---

# CEO Daily Briefing — Bản Tin Sáng Cho Sếp Tổng

## Mục Tiêu
Giúp CEO bắt đầu ngày làm việc với 1 bản tóm tắt 5 phút thay vì tốn 45 phút lướt email, Slack, lịch. Tăng tốc ra quyết định buổi sáng, không bỏ sót việc khẩn.

## Khi Nào Dùng
- CEO yêu cầu briefing sáng hằng ngày qua email lúc 6h
- Sau kỳ nghỉ lễ/công tác cần tổng hợp 1-3 ngày
- Trợ lý CEO chuẩn bị tài liệu trước cuộc họp lãnh đạo 8h
- CEO đi công tác cần update từ HQ
- Trước buổi standup tuần

## Bước 1: Thu Thập Nguồn Dữ Liệu
Liệt kê các nguồn cần quét:
- Email Gmail (Inbox + Starred) trong 24h qua
- Slack DM + 3-5 kênh quan trọng (#leadership, #urgent, #board)
- Google Calendar hôm nay + ngày mai
- Notion/Drive: tài liệu mới được share cho CEO
- Hệ thống nội bộ (CRM, HRIS) — chỉ lấy alert đỏ

Hỏi CEO 1 lần để chốt: nguồn nào BẮT BUỘC, nguồn nào tuỳ chọn.

## Bước 2: Phân Loại 5 Nhóm Thông Tin
1. **CẦN QUYẾT ĐỊNH NGAY** (red) — chờ approval, vấn đề khủng hoảng
2. **CẦN BIẾT** (yellow) — tin tức quan trọng, deal update
3. **LỊCH HÔM NAY** — 5-8 cuộc họp + mục tiêu mỗi cuộc
4. **THEO DÕI** — task được giao cho người khác cần follow
5. **GHI CHÚ CÁ NHÂN** — sinh nhật, kỷ niệm, ngày quan trọng

## Bước 3: Viết Briefing Đúng Định Dạng
- Tiêu đề: "Briefing sáng [ngày] — [3 keyword chính]"
- Tổng 400-600 từ
- Mỗi mục có: **việc gì** → **ai liên quan** → **CEO cần làm gì** → **deadline**
- Ngôn ngữ ngắn gọn, không lan man, dùng bullet
- Highlight số tiền, số % bằng **bold**

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Gmail MCP: `search_threads` với query `newer_than:1d is:important` để lấy email nóng
- Calendar MCP: `list_events` lấy lịch hôm nay + ngày mai
- Slack MCP: lấy DM chưa đọc + mention trong 24h
- Google Drive MCP: `list_recent_files` để biết tài liệu mới
- Notion MCP: lấy page có comment mới gửi cho CEO

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Gmail API: lấy email quan trọng 24h
from googleapiclient.discovery import build
service = build('gmail', 'v1', credentials=creds)
results = service.users().messages().list(
    userId='me',
    q='newer_than:1d (is:important OR is:starred)',
    maxResults=30
).execute()
messages = results.get('messages', [])
# Lấy subject + snippet để tóm tắt
```

## Bước 5: Output Format
- File Markdown `briefing-YYYY-MM-DD.md` lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`
- Đồng thời render HTML đẹp (Tailwind inline) để gửi email
- Tiêu đề email: `Briefing [ngày] | [3 highlight đỏ]`
- Gửi qua Gmail MCP `create_draft` lúc 6h sáng (hoặc gửi luôn nếu CEO confirm)

## Checklist Trước Khi Giao
- [ ] Đã liệt kê đủ 5 nhóm thông tin
- [ ] Không có nhóm nào quá 7 bullet (giới hạn để đọc nhanh)
- [ ] Mỗi mục đỏ có deadline rõ ràng
- [ ] Lịch họp có mục tiêu mỗi cuộc
- [ ] Tổng độ dài 400-600 từ
- [ ] Đã đính kèm link đến nguồn gốc (email/Slack thread)
