---
name: bo-buoc-ghi-ly-do
description: Nguyên tắc bắt buộc khi làm theo quy trình, playbook hoặc checklist của một skill — bước nào bỏ qua phải ghi rõ là đã bỏ và vì sao, không bỏ ngầm. Dùng mọi khi agent rút gọn, gộp hoặc bỏ bước so với quy trình đã định.
---
# Bỏ bước phải ghi lý do

## Luật
Một bước trong quy trình chỉ có ba trạng thái: **đã làm**, **đã bỏ kèm lý do**, hoặc **chưa làm được kèm lý do**. Không có trạng thái thứ tư là "im lặng bỏ qua".

## Cách ghi
Trong báo cáo cuối việc, thêm một dòng cho mỗi bước bỏ:

| Bước | Trạng thái | Lý do |
|---|---|---|
| Đối soát với sàn Shopee | Bỏ | Chưa có quyền truy cập sàn |
| Chạy `may-cham` | Chưa làm được | Thiếu API key trong phiên |

## Vì sao
- Người duyệt biết kết quả còn thiếu gì, không tin nhầm là đã đủ.
- Bước bị bỏ nhiều lần cùng lý do là tín hiệu sửa quy trình hoặc skill (`sua-dung-tang`).

## Nguồn
Ý từ pstack (Lauren Tan, MIT): playbook chép nguyên vào danh sách việc, bước bỏ qua phải hiện rõ kèm lý do. Tầng tri thức: thu thập, chưa kiểm chứng trong hệ MQ.
