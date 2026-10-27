# harness/ — khung vận hành agent của hệ MQ

**Harness = mọi thứ quanh mô hình**: vòng lặp, công cụ, bộ nhớ, an toàn, điều phối, mở rộng. Lõi chạy là nền tảng agent của MQ (xem `DECISIONS.md` trong thư mục này). Thư mục này giữ **phần độc lập nền tảng**: luật, chính sách, đặc tả hook, đề kiểm thử, chỉ số. Nền tảng nào làm lõi cũng đọc cùng một bộ.

Tạm đặt trong Agent-control-os. Tách ra repo riêng khi đủ dày — luật tách ở `RANH-GIOI.md`. **Đọc `RANH-GIOI.md` trước khi thêm file.**

## Bản đồ

| Đường dẫn | Chứa gì | Phân hệ |
|---|---|---|
| `RANH-GIOI.md` | Luật giữ thư mục cắt ra được; điểm nối ra ngoài; điều kiện tách | — |
| `DECISIONS.md` | Quyết định riêng của harness | — |
| `kien-truc.md` | 7 phân hệ, nguyên tắc MQ cho từng phân hệ, khác biệt harness nghiệp vụ | Cả 7 |
| `chinh-sach/quyen.yaml` | Ánh xạ 3 mức quyền sang hành động và ngưỡng duyệt | 5. An toàn |
| `chinh-sach/cam.yaml` | Việc agent không bao giờ tự làm | 5. An toàn |
| `chinh-sach/gioi-han.yaml` | Giới hạn lượt, chi phí, token | 1. Vòng lặp |
| `chinh-sach/thu-tu-uu-tien.md` | 7 cấp ưu tiên lệnh; dữ liệu ngoài luôn là dữ liệu | 5. An toàn |
| `hooks/` | Đặc tả 3 hook: chặn ghi chưa duyệt, kiểm chứng trước khi dừng, chặn lặp | 1, 5, 7 |
| `chi-so.md` | 7 chỉ số sức khoẻ harness | Cả 7 |
| `danh-gia/` | Đề kiểm thử hành vi harness (khác eval skill) | Cả 7 |

## Nguyên tắc

- **Harness mỏng, skill dày.** Mỗi phân hệ chọn mức tối thiểu đủ dùng; chỉ nâng khi có lỗi thật đòi hỏi.
- **Chính sách nằm trong cấu hình**, không nhét vào lời nhắc — để không mất khi nén ngữ cảnh.
- **Mọi con số ngưỡng để trống** đến khi có 2 tuần số đo nền. Không đặt trước.

## Trạng thái (2026-10-27)

| Hạng mục | Trạng thái |
|---|---|
| Kiến trúc 7 phân hệ | v1, tài liệu |
| Chính sách quyền, cấm, giới hạn | Khung; ngưỡng chờ số đo nền; `cam.yaml` chờ Quân bổ sung |
| Hook | Đặc tả; chưa cài trên nền tảng lõi |
| Đề kiểm thử | 3 đề mẫu; máy chấm v1 chưa chạy được đề harness (xem `danh-gia/README.md`) |
| Chỉ số | Định nghĩa; chưa có bảng lưu |
