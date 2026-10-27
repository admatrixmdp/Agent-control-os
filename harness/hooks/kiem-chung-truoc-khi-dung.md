# Hook: kiểm chứng trước khi dừng

Mẫu "verify-on-stop" của Hermes (arXiv 2609.00006, mục 6.2), đổi từ "chạy test" sang "đọc lại bản ghi".

| Mục | Nội dung |
|---|---|
| Sự kiện | `stop` |
| Điều kiện chặn | Trong lượt có công cụ ghi thành công, nhưng sau đó không có công cụ đọc lại cùng đối tượng |
| Kết quả | Chặn việc dừng, yêu cầu agent đọc lại và đối chiếu |

## Ví dụ

Agent tạo 20 đơn rồi trả lời "Đã tạo xong 20 đơn". Hook thấy chưa có lệnh đọc lại → chặn. Agent đọc lại danh sách đơn, thấy 19 mã, báo đúng "tạo được 19/20, đơn thứ 7 lỗi địa chỉ".

## Chống lặp

Chặn tối đa **2 lần** mỗi lượt. Lần thứ 3 cho dừng, kèm cảnh báo "chưa kiểm chứng được" trong câu trả lời.

## Đề kiểm thử

`../danh-gia/de/HN-003-bao-xong-chua-kiem.yaml`
