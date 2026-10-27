# Kiến trúc harness: 7 phân hệ

Nguồn khung: Barbaste và cộng sự, *Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents*, arXiv 2609.00006 (7/2026) — phân tích mã nguồn 11 harness viết mã. Tầng tri thức: **thu thập, đã kiểm chứng ở mức đọc bài gốc**. Phần áp dụng cho MQ là đề xuất.

## Bố cục

```
Lớp giao diện      kênh nhắn tin · ứng dụng sản phẩm · MCP ra ngoài
        │
Lõi harness        [1. Vòng lặp] ← 2. LLM · 3. Công cụ · 4. Bộ nhớ
                                  ← 5. An toàn · 6. Điều phối · 7. Mở rộng
        │
Lớp phiên          nhật ký sự kiện · chạy tiếp sau khởi động lại · tua lại
        │
Hạ tầng            máy chạy · cơ sở dữ liệu · kho skill · vault Markdown
```

## 7 phân hệ

| Phân hệ | Bài nghiên cứu thấy | Nguyên tắc MQ | Chỉ nâng cấp khi |
|---|---|---|---|
| 1. Vòng lặp | 9/11 harness dùng vòng lặp hành động–quan sát tự viết; không harness nào dùng LangChain/LangGraph | Vòng lặp đơn + giới hạn lượt, chi phí, token dạng cấu hình (`chinh-sach/gioi-han.yaml`) | Chỉ số vòng lặp bị phát hiện tăng |
| 2. Tích hợp LLM | Tối ưu theo nhà cung cấp phụ thuộc ai chịu viết mã riêng, không phụ thuộc gắn chặt một hãng | Chọn mô hình theo loại việc; giữ tiền tố lời nhắc ổn định để trúng bộ nhớ đệm | Chi phí mỗi tác vụ vượt biên lợi nhuận gói |
| 3. Công cụ | Từ 1 đến 109 công cụ; nạp trễ công cụ lan từ 1 lên 3 harness trong một quý | Lõi ít công cụ; MCP nghiệp vụ nạp khi cần | Số công cụ nạp mỗi lượt tăng |
| 4. Bộ nhớ | 7/11 nén ngữ cảnh khi chạm ngưỡng | Nén theo ngưỡng + vault Markdown + bộ nhớ liên phiên do agent tự ghi | Số lần nén mỗi phiên cao bất thường |
| 5. An toàn | Chỉ 2/11 có hộp cát cấp hệ điều hành; harness chặt nhất xếp 4 lớp: luật → hook → LLM duyệt → hộp cát | 3 lớp: luật cấu hình → hook → người hoặc LLM duyệt; phân quyền dữ liệu theo khách thay hộp cát | Có sự cố ghi sai dữ liệu khách |
| 6. Điều phối | Mẫu điều phối–thực thi ở harness lớn; có harness cố tình không có | Mặc định một agent; tác tử con chỉ khi việc chạy song song rõ ràng | Việc định kỳ chạy quá lâu |
| 7. Mở rộng | Skill dạng SKILL.md (9/11) vượt MCP (8/11); tên hook bị chép nguyên văn giữa các harness | Skill-first; tên hook chuẩn (`hooks/README.md`) | — |

## Harness nghiệp vụ khác harness viết mã ở đâu

Bài chỉ khảo sát agent viết mã. MQ chạy agent bán hàng, marketing, tài chính, nên 4 điểm phải đổi (ý kiến, không phải kết luận của bài):

| Điểm | Harness viết mã | Harness nghiệp vụ MQ | Hệ quả |
|---|---|---|---|
| Hành động cốt lõi | Sửa file | Ghi vào CRM, POS, tài khoản quảng cáo | Công cụ ghi phải có chế độ xem trước và nhật ký hoàn tác |
| Kiểm chứng | Chạy test, lint | Đọc lại bản ghi, đối soát số | Cổng kiểm chứng gọi công cụ đọc lại, không gọi test |
| Rủi ro lớn nhất | Hỏng mã, lộ khoá | Gửi nhầm khách, tiêu sai ngân sách, sai hoá đơn | Duyệt theo số tiền và số người nhận, không chỉ theo loại lệnh |
| Người dùng | Lập trình viên | Chủ shop, nhân viên sale | Thẻ duyệt viết bằng ngôn ngữ nghiệp vụ, kèm số tiền, số khách |

## Mẫu thiết kế lấy về

| Mẫu | Nguồn trong bài | Ở đây |
|---|---|---|
| Kiểm chứng trước khi dừng | Hermes | `hooks/kiem-chung-truoc-khi-dung.md` |
| Lặp thì hỏi người, không tự huỷ | OpenCode | `hooks/lap-vo-han.md` |
| Nhật ký phiên làm hàng đợi việc | OpenCode | Lớp phiên |
| Thứ tự ưu tiên lệnh, dữ liệu ngoài là dữ liệu | Mistral Vibe | `chinh-sach/thu-tu-uu-tien.md` |
| Chính sách chuyển từ lời nhắc sang cấu hình | Xu hướng 4→7/2026 | `chinh-sach/` |
| Đo tiền lãng phí do trượt bộ nhớ đệm | Pi | `chi-so.md` |

## Không lấy về

Hộp cát cấp hệ điều hành đa nền tảng; giả danh harness khác để dùng gói thuê bao; chép nguyên một harness lớn.
