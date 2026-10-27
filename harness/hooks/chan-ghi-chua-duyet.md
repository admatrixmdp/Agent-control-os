# Hook: chặn ghi chưa duyệt

| Mục | Nội dung |
|---|---|
| Sự kiện | `pre_tool_use` |
| Khớp | Công cụ thuộc nhóm `hoi_truoc` trong `../chinh-sach/quyen.yaml`, hoặc chạm `nang_muc_khi` |
| Kết quả | Chặn, trừ khi đầu vào có mã duyệt hợp lệ |

## Luồng

1. Agent gọi công cụ ghi (vd tạo 20 đơn).
2. Hook không thấy mã duyệt → **chặn**, tạo phiếu duyệt với các trường trong `the_duyet`, gửi qua kênh duyệt.
3. Hook trả lời agent: "Đang chờ duyệt, mã phiếu …". Agent báo người dùng và **dừng lượt**, không thử lại.
4. Người duyệt bấm Duyệt → hệ thống chạy lại lệnh, kèm mã duyệt.
5. Hook thấy mã hợp lệ → cho qua.

## Vì sao duyệt bất đồng bộ

Hook thường bị giới hạn thời gian chạy rất ngắn, không đủ chờ người trả lời. Nên hook chỉ chặn và tạo phiếu; việc chờ nằm ngoài hook.

## Mã duyệt

- Dùng **một lần**.
- Gắn với **dấu băm của đầu vào công cụ**: duyệt "20 đơn" không dùng được cho "200 đơn".
- Hết hạn theo `het_han_phut`; hết hạn = từ chối.

## Đề kiểm thử

`../danh-gia/de/HN-002-tao-don-hang-loat.yaml`
