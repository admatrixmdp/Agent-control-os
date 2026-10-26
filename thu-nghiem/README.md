# Phòng thí nghiệm skill & agent

Mỗi thư mục con là **một thí nghiệm**: có giả thuyết, tình huống cố định, kết quả chấm và kết luận. Không sửa skill thật cho tới khi số đo chứng minh.

## Cấu trúc một thí nghiệm

```
thu-nghiem/<YYYY-MM>-<mang>-lo<N>/
  gia-thuyet.md      ← điều cần kiểm, cách chạy, giới hạn
  tinh-huong/*.yaml  ← đúng chuẩn may-cham (khung kế toán), dữ liệu giả lập
  ket-qua.md         ← bảng điểm, giám khảo nhận xét, tóm tắt từng output
  ket-luan.md        ← Giữ / Nâng cấp / Gộp / Lưu trữ + việc tiếp theo
```

## Thang kiểm chứng 5 cấp

| Cấp | Kiểm | Cách chạy |
|---|---|---|
| 1. Định dạng | YAML, cấu trúc skill | `may-cham kiem` |
| 2. Skill đơn | Có skill tốt hơn không skill? | `may-cham cham --so-sanh` |
| 3. Chuỗi skill | Đầu ra skill trước dùng được cho skill sau | Chạy nối trên cùng case |
| 4. Agent loop | Agent tự chọn đúng skill, xong việc nhiều bước | Giao việc cho agent, chấm bằng `cham-phien` |
| 5. Skill loop | Sửa skill rồi chấm lại có tốt lên không | Cùng bộ tình huống; không tăng thì hoàn tác |

## Luật

- Giám khảo là mô hình khác mô hình chạy, chấm mù (không biết bản nào là bản nào).
- Bộ tình huống cố định giữa các lần chấm trước/sau.
- Dữ liệu giả lập, không dữ liệu khách thật.
- Kết quả ở tầng **"thu thập, chưa kiểm chứng"** cho tới khi chạy sạch bằng máy chấm với ≥ 3 tình huống/skill.
- Skill ngoài xử lý xong → cập nhật `skill-lab/trang-thai.yaml`; xem `skill-lab/luu-tru/README.md`.

## Danh sách thí nghiệm

| Thí nghiệm | Mảng | Cấp | Kết quả gọn |
|---|---|---|---|
| [2026-10-sale-lo1](2026-10-sale-lo1/) | sale | 2 (chạy tay) | Skill ngoài thua 3/4; skill nội bộ chưa thắng rõ bản không skill nhưng bản đó bị rò tri thức → phải chạy lại sạch |
