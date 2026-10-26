# Luật giao việc và cách dịch sang từng nền tảng

Luật gốc có 3 mức (`AGENTS.md` mục 3): **Tự làm / Hỏi trước / Cấm**. Mỗi nền tảng có cơ chế phân quyền riêng. File này là bảng dịch, viết một lần ở đây; hồ sơ trong `nen-tang/` chỉ trỏ về.

## 1. Bảng dịch

| Nền tảng | Cơ chế có sẵn | Tự làm | Hỏi trước | Cấm |
|---|---|---|---|---|
| Claude Code | Chế độ quyền + hook + luật trong `CLAUDE.md` / `AGENTS.md` | Cho phép công cụ đọc | Để công cụ ghi ở chế độ hỏi; ghi luật vào CLAUDE.md | Hook chặn (PreToolUse) + luật |
| Codex | Sandbox + mức phê duyệt + `AGENTS.md` | Sandbox đọc / ghi workspace | Phê duyệt theo yêu cầu | Sandbox chặn mạng / ghi ngoài workspace + luật |
| GoClaw / Goso | Cấu hình agent, quyền tool, file agent | Cấp tool đọc | Tool ghi qua bước xác nhận / tin nhắn duyệt | Không cấp tool |
| Claude Duet | Hỏi trước khi gửi tin, thanh toán, ký, xoá; kế thừa bộ nhớ app Claude | Mặc định | Mặc định với các hành động trên; ghi thêm luật vào bộ nhớ Claude | Ghi vào bộ nhớ: "không bao giờ …"; Duet vốn không chuyển tiền, không giao dịch chứng khoán |
| OpenAI Dots | **Custom Rules 4 mức**: làm không hỏi / làm nếu đã duyệt trước / hỏi trước / trả lại người + Auto-review | "Làm không hỏi" | "Hỏi trước" | "Trả lại cho người" |
| Meta Muse | Xác nhận cho hành động khó hoàn tác (gửi email, gửi form rủi ro, thanh toán) | Mặc định | Mặc định với các hành động trên | Không có cơ chế cấm rõ → **không giao việc thuộc mức Cấm** |
| Grok Bot | Allow once / Deny / Always allow + luật Auto Review + bàn giao an toàn | "Always allow" | "Allow once" (hỏi mỗi lần) | "Deny" + luật Auto Review |

## 2. Văn bản luật chuẩn để dán vào agent đám mây

Dán nguyên văn vào bộ nhớ / hướng dẫn của Duet, Dots, Muse, Grok Bot:

```
Luật làm việc cho Quân (MQ):
1. Tự làm: đọc, tìm kiếm, tóm tắt, soạn nháp, phân tích.
2. Luôn hỏi trước: gửi email/tin nhắn cho người khác, đăng nội dung, đặt chỗ, gửi form, thay đổi bất kỳ hệ thống nào.
3. Không bao giờ: thanh toán hoặc chuyển tiền; xoá dữ liệu; chia sẻ dữ liệu khách hàng ra ngoài; đăng nhập tài khoản người khác.
4. Thiếu thông tin thì nói "không đủ cơ sở" và hỏi một câu, không đoán.
5. Báo kết quả kèm bằng chứng (link, ảnh chụp, số liệu nguồn).
```

## 3. Các hành động luôn ở mức "Hỏi trước" bất kể nền tảng

- Bật / tắt / tăng ngân sách chiến dịch quảng cáo.
- Ghi đơn, sửa giá, sửa tồn kho trên POS.
- Merge PR, publish trang, đăng bài.
- Gửi bất cứ thứ gì cho khách hàng, đối tác, cơ quan nhà nước.
- Sửa card / dashboard đang có người dùng.

## 4. Chuyển mức quyền

Một hành động chỉ chuyển từ "Hỏi trước" xuống "Tự làm" khi:
1. Đã chạy đúng ít nhất 5 lần liên tiếp ở mức "Hỏi trước" (theo `vong-lap/cham-phien`).
2. Quân đồng ý rõ ràng.
3. Ghi vào `DECISIONS.md`, ghi rõ phạm vi (vd chỉ nhóm Lark X, chỉ shop Y).
