# Chỉ số sức khoẻ harness

Mục tiêu đặt sau 2 tuần đo mức nền. Chưa có bảng lưu; khi dựng, đặt tên bảng và ghi vào đây.

| Chỉ số | Cách tính | Phân hệ | Đọc thế nào |
|---|---|---|---|
| Tỷ lệ hoàn thành có kiểm chứng | Tác vụ xong và qua hook kiểm chứng / tổng tác vụ | 1 | Chỉ số chính |
| Chi phí mỗi tác vụ | Tiền token / tác vụ hoàn thành, tách theo sản phẩm | 2 | So với giá gói để biết biên lợi nhuận |
| Tiền lãng phí do trượt bộ nhớ đệm | Tiền token tiết kiệm được nếu tiền tố lời nhắc ổn định | 2 | Khoản tiết kiệm rẻ nhất |
| Số công cụ nạp mỗi lượt | Trung bình định nghĩa công cụ trong lời nhắc | 3 | Tăng dần = nạp trễ hỏng |
| Số lần nén mỗi phiên | Đếm sự kiện nén | 4 | Cao = skill hoặc công cụ trả về quá dài |
| Tỷ lệ hỏi duyệt / tỷ lệ bị từ chối | Hỏi duyệt / tác vụ; từ chối / hỏi | 5 | Từ chối nhiều = agent hiểu sai ý; hỏi quá nhiều = luật quá chặt |
| Số vòng lặp bị phát hiện | Số lần hook chặn lặp kích hoạt | 1 | Báo hiệu lỗi thiết kế skill hoặc công cụ |
