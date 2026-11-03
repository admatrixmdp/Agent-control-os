---
name: safe-prod-deploy
description: Dùng khi deploy hoặc áp một thay đổi lên hệ thống đang chạy thật (prod, bridge, gateway, migration DB) có nhiều bước. Xác định đúng máy đang chạy, sao lưu, test thật bằng dữ liệu giả, trả lại cấu hình đã đổi để test, rồi báo kèm lệnh rollback. Không dùng cho việc chỉ đọc hay sửa trên máy dev/staging riêng.
---

# Deploy lên prod an toàn

## Khi nào dùng

- Owner bảo deploy, áp bản vá, chạy migration hay đổi cấu hình trên hệ thống đang phục vụ người dùng thật.
- Không dùng cho câu hỏi chỉ đọc (đang chạy bản nào, commit nào) hay sửa trên nhánh riêng, máy dev, staging. Với những việc đó, trả lời hoặc mở PR như thường.

## Các bước

1. **Xác nhận được phép.** Việc đụng prod phải có lệnh rõ của owner ("áp", "xử lý đi") cho đúng thay đổi này. Lời duyệt chuyển qua bot khác thì ghi nguyên văn kèm giờ. Phần chuẩn bị không đụng prod (đọc code, build, test trên bản sao) thì làm luôn, không chờ.
2. **Lần ra máy thật.** Từ domain hoặc endpoint công khai, lần ra máy, tunnel, tiến trình (launchd/systemd/docker) và commit đang chạy. Đừng tin mô tả kiểu "deploy lên server". Ghi lại commit/image hiện tại để rollback.
3. **Đo lại trạng thái.** Dung lượng ổ, version schema (`dirty=false`), schema thật của DB: đo ngay lúc này, không dùng số cũ hay mô tả PR. Code hoặc migration phải khớp tên bảng/cột của prod thật.
4. **Sao lưu trước.** Dump DB hoặc copy file SQLite (cả -wal/-shm), snapshot volume, gắn tag image cũ. Kiểm file backup > 0 byte. Viết sẵn lệnh rollback.
5. **Deploy từng nơi.** Đủ mọi nơi thay đổi phải tới (ví dụ cả gateway, bản đầy đủ và bridge); nơi nào cố ý không đụng thì ghi rõ lý do. Đo downtime.
6. **Test thật, bằng dữ liệu giả.** Mở đúng domain, kiểm tên bundle và một dấu hiệu tính năng mới; gọi đúng tính năng owner cần, không chỉ healthcheck. Test trả lời khách chỉ bằng khách/hội thoại giả, không nhắn khách thật. Cài đặt nào đổi để test thì ghi giá trị cũ, đặt lại và kiểm khớp. Dữ liệu test xoá sau khi xong. Bước nào không test được thì ghi SKIPPED kèm lý do.
7. **Báo cáo.** Bằng ngôn ngữ đời thường: đã chạy ở đâu, test gì và kết quả, downtime, lệnh rollback, mục "Còn lại" (lỗi có sẵn phát hiện được, phần bỏ qua). Sửa ngay nếu báo cáo trước đó sai.

## Rào chắn

- Không mở cổng public, không gửi tin cho khách thật, không xoá dữ liệu thật, không tạo/in credential nếu owner chưa đồng ý rõ.
- Mất dữ liệu hoặc không rollback được thì dừng và hỏi owner.
- Bị sửa hoặc thất bại thì ghi bài học kèm bằng chứng vào sổ bài học (tầng scratch).
