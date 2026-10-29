# Grok Bot (xAI)

| Mục | Nội dung |
|---|---|
| Lớp | B |
| Định danh | Agent early-beta, chạy trên VM đám mây bền vững gắn tài khoản; tách biệt với Grok chat, xAI API và Grok Build |
| Lối vào tri thức | Trình duyệt, hệ thống tệp, terminal, connector (Gmail, Google Calendar, Drive, OneDrive, Outlook, Teams, SharePoint, Salesforce) và **MCP tuỳ chỉnh** (phải truy cập công khai hoặc qua tunnel) → lối vào rõ nhất cho MQ Knowledge MCP |
| Lối vào quy tắc | Allow once / Deny / Always allow; luật Auto Review; bàn giao an toàn cho bước nhạy cảm |
| Bộ nhớ | **Không xem, sửa, xuất, xoá được** → không đưa thông tin nhạy cảm |
| Lịch | Routines, lịch chạy, kích hoạt theo sự kiện từ Cursor |
| Đầu ra & trace | Không mô tả nhật ký |
| Giới hạn cứng | Không self-host; chỉ mô hình xAI; nhiều Bot cùng tài khoản **dùng chung máy và phiên đăng nhập → không có ranh giới quyền riêng**; ứng dụng desktop macOS/Windows + iPhone |
| Chi phí | Thử 14 ngày, sau đó 200 USD/tháng (hoặc kèm SuperGrok Heavy / Cursor Ultra / Cursor Teams Premium) |
| Nên giao | Việc trình duyệt trên web không có API, việc có MCP nội bộ, mô hình "Chief of Staff" điều phối nhiều Bot theo mảng (cách Lauren Tan dùng) |
| Không giao | Việc cần tách quyền giữa các vai trò; việc mức Cấm |
| Ghi chú | Grok qua API (lớp C) đang dùng trong `admatrixmdp/core-process` (`gcli/grok-4.6:high`) cho việc viết code |

Nguồn: Unite.ai, iPhone in Canada (8/2026), Vellum, aiidelist. Xác nhận: 2026-10-26.
