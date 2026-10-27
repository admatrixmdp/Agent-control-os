---
name: hoi-bang-ban-nhap
description: Nguyên tắc bắt buộc khi một hành động thuộc mức Hỏi trước (gửi tin, đăng bài, ghi đơn, sửa cấu hình, bật quảng cáo, merge) — làm tới sát bước cuối, nộp bản nháp hoàn chỉnh để Quân chỉ cần duyệt hoặc sửa. Dùng mọi khi agent sắp hỏi "anh có muốn tôi làm không".
---
# Hỏi bằng bản nháp

## Luật
Hỏi trước không có nghĩa là hỏi suông. Làm hết mọi việc có thể làm mà chưa chạm hệ thống thật, rồi dừng ở bước cuối với một bản nháp duyệt được ngay.

Bản nháp phải có:

| Trường | Ví dụ |
|---|---|
| Hành động sẽ làm | Tạo 20 đơn trên POS |
| Nội dung đầy đủ | Danh sách 20 đơn: khách, sản phẩm, số tiền |
| Quy mô | 20 đơn, tổng 15.000.000đ, 20 khách |
| Hoàn tác được không | Được: huỷ đơn trong 24 giờ |
| Điểm cần Quân để ý | 2 khách thiếu địa chỉ |

## Phân biệt với hỏi làm rõ
- Hỏi làm rõ (thiếu thông tin để bắt đầu): hỏi một câu, theo `khong-bia`.
- Hỏi duyệt (đủ thông tin, chờ quyền): nộp bản nháp theo skill này.

## Ví dụ
Sai: "Anh có muốn tôi gửi email báo giá cho khách A không?"
Đúng: "Bản nháp email báo giá cho khách A ở dưới (tiêu đề, nội dung, file báo giá đính kèm). Giá lấy từ bảng giá tháng 10. Anh duyệt thì tôi gửi."

## Nguồn
Ý từ pstack (Lauren Tan, MIT): PR xanh là "sẵn sàng để quyết", không phải "được duyệt". Tầng tri thức: thu thập, chưa kiểm chứng trong hệ MQ.
