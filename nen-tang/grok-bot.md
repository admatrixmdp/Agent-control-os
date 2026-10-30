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

## Agent Evolution trên Grok Bot

Grok Bot là nền tảng chạy chính của Agent Evolution (`plugins/agent-evolution/agents/agent-evolution.md`). Cài theo các bước dưới. Mọi chặn quan trọng dùng **cơ chế chặn thật** của GitHub và Grok Bot, không dựa vào lời dặn.

| Bước | Làm gì | Ai làm |
|---|---|---|
| 1 | Tạo một Bot riêng tên "Agent Evolution". Hướng dẫn của Bot chỉ gồm một câu: *"Mỗi lần chạy, clone mới `admatrixmdp/Agent-control-os`, đọc và làm đúng `plugins/agent-evolution/agents/agent-evolution.md`."* Không dạy luật qua trò chuyện, vì bộ nhớ Grok Bot không xem hay sửa được | Quân / Dat |
| 2 | Lịch (routine): 9:00 thứ Hai và thứ Năm, giờ Việt Nam. Lần đầu thứ Hai 2/11/2026 | Quân / Dat |
| 3 | Khoá GitHub **fine-grained**, chỉ mở cho `Agent-control-os`, repo dữ liệu bài học và các repo skill đang tiến hoá (bắt đầu: `sale-suite-os`). Quyền: Contents đọc–ghi, Pull requests đọc–ghi. Không Administration, không Workflows | Quân |
| 4 | **Branch protection** trên nhánh chính các repo đó: bắt buộc PR, bắt buộc ít nhất 1 người duyệt, không cho đẩy thẳng. Đây là chốt chặn thật cho luật "không merge" | Quân |
| 5 | Luật Auto Review của Grok Bot: **Always allow** `git push` lên nhánh `agent-evolution/*` và tạo PR. **Deny** merge, đẩy vào nhánh chính, xoá nhánh hay repo | Quân / Dat |
| 6 | Repo dữ liệu private có `hop-thu/` và `bao-cao/`. Đặt `SELF_EVO_INBOX` trỏ vào `hop-thu/`. Sổ SQLite (`SELF_EVO_DB`) để trên máy Bot, không commit | Quân |

**Lưu ý:** các Bot trong cùng tài khoản Grok **dùng chung máy và phiên đăng nhập**, nên khoá ở bước 3 thì Bot nào cũng dùng được. Đây là lý do khoá phải hẹp và bước 4 bắt buộc.

**Chấm điểm:** Grok Bot chỉ dùng mô hình xAI. Không có `ANTHROPIC_API_KEY` thì Grok vừa chạy vừa chấm, và PR phải ghi "tự chấm, chưa khách quan" (xem mục 5 của bản mô tả agent).
