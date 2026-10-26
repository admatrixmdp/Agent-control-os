# Thiết kế 2 bảng LarkBase cho vòng lặp

Tên trường và loại trường theo giao diện LarkBase.

## Bảng 1: `Session_Scorecard` (sổ chấm phiên)

| Trường | Loại | Ghi chú |
|---|---|---|
| Mã phiên | Số tự động | Khoá |
| Ngày | Ngày | |
| Nền tảng | Một lựa chọn | claude, claude-code, chatgpt, codex, goclaw, goso, claude-duet, dots, muse, grok-bot |
| Skill | Văn bản | Tên đúng như `danh-muc/skills.yaml` |
| Repo | Một lựa chọn | Các repo `*-os` |
| Việc | Văn bản | Một câu, không dữ liệu khách thật |
| Điểm | Đánh giá (1–5) | Quân chấm |
| Nhãn lỗi | Một lựa chọn | harness, skill, agent, tri-thuc, mo-hinh, khong-loi |
| Sai ở đâu | Văn bản | |
| Link phiên | URL | |
| Nguồn ghi | Một lựa chọn | cham-phien, trace-goclaw, nhap-tay |
| Đã xử lý | Hộp kiểm | Vòng B đánh dấu khi đã đề xuất sửa |
| Thay đổi liên quan | Liên kết một chiều → `Skill_Change_Log` | |

**Chế độ xem gợi ý:** "Điểm ≤ 3 chưa xử lý" (lọc Điểm ≤ 3, Đã xử lý = không) — đầu vào vòng B. "Theo nhãn lỗi" (nhóm theo Nhãn lỗi) — xem nên đầu tư tầng nào.

## Bảng 2: `Skill_Change_Log` (kho tiền lệ)

| Trường | Loại | Ghi chú |
|---|---|---|
| Mã thay đổi | Số tự động | |
| Ngày | Ngày | |
| Skill | Văn bản | |
| Repo | Một lựa chọn | |
| Loại thay đổi | Một lựa chọn | playbook-delta, sua-skill, them-eval, gop-tu-ngoai, loai-skill |
| Nội dung đề xuất | Văn bản | Một dòng |
| Điểm trước | Số | Tỷ lệ đạt `may-cham` |
| Điểm sau | Số | |
| Chênh lệch | Công thức | `[Điểm sau] - [Điểm trước]` |
| Kết luận | Một lựa chọn | chap-nhan, tu-choi, cho-duyet |
| Lý do | Văn bản | |
| Link PR | URL | |
| Phiên gốc | Tra cứu ← `Session_Scorecard` | |

**Dùng cho bước B3:** trước khi đề xuất, tra bảng này theo Skill + Nội dung tương tự; đã từng bị từ chối thì không đề xuất lại trừ khi có lý do mới.
