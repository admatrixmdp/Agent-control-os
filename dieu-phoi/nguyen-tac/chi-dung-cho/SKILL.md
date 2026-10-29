---
name: chi-dung-cho
description: Nguyên tắc chọn mức độ kiểm tra theo chi phí của sai sót — việc sai thì tốn kém (tài chính, pháp lý, gửi ra ngoài, ghi hệ thống thật) chạy quy trình đầy đủ; việc nhỏ, dễ hoàn tác chạy nhẹ. Dùng khi lên kế hoạch một việc hoặc chọn mức eval.
---
# Chi đúng chỗ

## Ba mức
| Mức | Khi nào | Làm gì |
|---|---|---|
| Nhẹ | Nháp, ý tưởng, sửa chữ, việc nội bộ dễ hoàn tác | Làm thẳng, tự kiểm nhanh |
| Vừa | Báo cáo dùng để ra quyết định, nội dung sắp đăng, sửa skill | Checklist skill + bằng chứng + eval của skill |
| Nặng | Tài chính, kế toán, pháp lý, hợp đồng, quảng cáo tốn tiền, ghi dữ liệu thật | Kiểm hai lần độc lập (agent thứ hai hoặc giám khảo khác mô hình) + người duyệt |

## Luật
- Không chạy mức Nặng cho việc Nhẹ: tốn token, chậm, Quân mất kiên nhẫn. Thử nghiệm độc lập với pstack cho thấy quy trình nặng làm một việc mất khoảng gấp đôi thời gian.
- Không chạy mức Nhẹ cho việc Nặng, kể cả khi bị giục.
- Không chắc mức nào thì chọn mức cao hơn một bậc.
