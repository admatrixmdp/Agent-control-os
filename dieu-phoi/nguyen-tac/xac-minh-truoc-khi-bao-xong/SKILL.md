---
name: xac-minh-truoc-khi-bao-xong
description: Nguyên tắc bắt buộc trước khi báo một việc đã xong — nộp bằng chứng kiểm được trên kết quả thật (số từ nguồn, link, ảnh chụp, kết quả chạy). Dùng mọi khi agent sắp nói "đã xong", "đã sửa", "đã gửi", "đã cập nhật".
---
# Xác minh trước khi báo xong

## Luật
"Đã chạy" không phải bằng chứng. "Đã đúng" mới là bằng chứng. Trước khi báo xong, nộp ít nhất một bằng chứng loại phù hợp:

| Loại việc | Bằng chứng tối thiểu |
|---|---|
| Báo cáo số liệu | Số khớp nguồn gốc (ghi bảng/nguồn và kỳ), tổng kiểm chéo |
| Sửa skill | Bảng điểm `may-cham` trước/sau |
| Ghi vào hệ thống (POS, Linear, LarkBase) | Đọc lại bản ghi vừa ghi, đối chiếu từng trường |
| Code | Test chạy xanh + chạy thật đường đi bị ảnh hưởng |
| Nội dung, tài liệu | Mở lại file đã xuất, kiểm checklist của skill |
| Thao tác web | Ảnh chụp trạng thái sau thao tác |

## Cách viết báo cáo
- Kết quả: một câu.
- Bằng chứng: link / số / ảnh.
- Chưa kiểm được gì: nói thẳng, không lấp liếm.

## Ví dụ
Sai: "Đã cập nhật giá 12 sản phẩm."
Đúng: "Đã cập nhật giá 12 sản phẩm. Đọc lại từ POS: 12/12 khớp bảng giá mới. Chưa kiểm giá trên sàn Shopee vì chưa có quyền."

## Nguồn
Ý từ nguyên tắc "xác minh là hạ tầng" của pstack (Lauren Tan, MIT). Tầng tri thức: thu thập, chưa kiểm chứng trong hệ MQ.
