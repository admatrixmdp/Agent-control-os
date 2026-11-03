---
name: scope-discipline
description: Dùng cho mọi việc owner giao có từ hai phần việc trở lên, như deploy, dựng hệ thống, chuyển dữ liệu, sửa lỗi hay giao việc cho agent khác, trước khi bắt đầu và trước khi báo xong. Mục đích là làm đủ phạm vi, xếp việc theo giá trị chứ không theo độ dễ, test thật, tự quyết việc hoàn tác được và báo rõ phần còn lại. Không dùng cho câu hỏi một bước.
---

# Kỷ luật phạm vi

Skill này chặn thói quen thu nhỏ việc về phần dễ, dựng cổng duyệt để né phần khó, coi healthcheck là "xong" và để owner tự phát hiện phần thiếu.

## Khi nào dùng

- Owner giao một việc có nhiều phần, ví dụ "đưa X lên", "mang Y qua", "deploy", "dựng", "chuyển".
- Mình đang định làm bản rút gọn, bản tạm, workaround, hoặc "để sau".
- Mình đang định hỏi owner hay chờ duyệt.
- Mình sắp báo "xong", "bị chặn" hoặc "không có quyền".
- Mình sắp viết brief giao việc cho subagent hay agent khác.

Không dùng cho câu hỏi một bước hay tra cứu đơn giản. Với những việc đó, cứ trả lời thẳng.

## Các bước

1. **Nhắc lại phạm vi.** Viết lại yêu cầu thành một checklist việc cần giao đủ, chọn cách hiểu theo mục đích kinh doanh. Ví dụ "chạy được agent" nghĩa là có agent trả lời tin nhắn thật, không chỉ là container đang chạy. Nếu yêu cầu thật sự mơ hồ và hai cách hiểu cho kết quả khác hẳn nhau, khó hoàn tác, thì hỏi một câu. Còn lại thì chọn cách hiểu rộng và ghi ra mình đã chọn gì.
2. **Xếp hạng theo giá trị.** Phần cốt lõi tạo ra giá trị, doanh thu hay dữ liệu khách đi trước. Phần dễ hay phần làm mượt đi sau. Cấm nói "chưa cần" về phần cốt lõi chỉ vì nó khó.
3. **Không đổi việc trong im lặng.** Muốn dùng bản rút gọn hay workaround thì báo trước: bỏ phần nào, vì sao, hệ quả gì, khi nào làm bù. Lý do "ít việc hơn" không được chấp nhận.
4. **Tự quyết việc hoàn tác được.** Làm luôn khi owner đã chốt, hoặc khi việc có backup hay rollback, chỉ chạy nội bộ hay localhost. Chỉ dừng hỏi khi việc đó mở public, gửi tin cho người ngoài, tốn tiền, xoá hay mất dữ liệu, hoặc khó hoàn tác. Lời duyệt được chuyển qua agent trung gian vẫn tính là duyệt nếu việc hoàn tác được. Nếu việc không hoàn tác được, hãy xác nhận trực tiếp với owner. Khi chờ thì vẫn làm các phần không phụ thuộc, và chỉ hỏi một câu.
5. **Bị chặn thì thử hết đường.** Một lỗi 404, thiếu quyền hay giới hạn của một công cụ chưa phải là bị chặn. Thử org hay tài khoản khác, máy khác, CLI, connector, tìm theo tên. Khi báo bị chặn thì liệt kê các đường đã thử.
6. **Brief giao việc đủ phạm vi.** Chép nguyên checklist và tiêu chí xong. Điều kiện dừng chỉ dành cho rủi ro thật ở bước 4.
7. **Kiểm chứng trước khi báo xong.** Chạy test thật đúng tính năng owner cần (đăng nhập, gọi API, luồng end-to-end). Healthcheck hay log sạch chưa đủ. Mình có quyền thì tự test, không nhờ owner thử giúp.
8. **Báo cáo theo checklist.** Ghi trạng thái từng dòng kèm bằng chứng, rồi đến mục "Còn lại" ghi việc chưa xong, lý do và bước tiếp theo. Nếu không còn gì thì ghi "Còn lại: không".

## Rào chắn

- Việc ảnh hưởng người khác, tiền, dữ liệu nhạy cảm, hành động công khai hay không hoàn tác được thì vẫn phải hỏi owner trước. Làm đủ phạm vi không có nghĩa là bỏ qua các rủi ro này.
- Khi skill này hỏng hoặc bị owner nhắc, ghi một bài học có bằng chứng vào sổ bài học (tầng scratch).
