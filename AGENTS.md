# AGENTS.md — luật cho mọi agent làm việc với hệ MQ

Đọc file này trước. Mỗi mục dưới đây trỏ tới chỗ có chi tiết; chỉ đọc vùng liên quan tới việc đang làm.

## 1. Repo này là gì

Lớp điều phối của hệ skill MQ. **Không chứa skill nghiệp vụ.** Skill nghiệp vụ nằm ở các repo `*-os` (xem `danh-muc/skills.yaml`).
Repo này chứa: luật giao việc, hồ sơ điều khiển từng nền tảng agent, máy chấm eval, quy trình đối chiếu skill, vòng lặp cải tiến.

## 2. Chọn đúng nền tảng trước khi làm

- Loại việc → nền tảng → skill: `dieu-phoi/bang-dinh-tuyen.md`
- Cách điều khiển từng nền tảng (Claude Code, Codex, GoClaw, Goso, Claude Duet, Dots, Muse, Grok Bot): `nen-tang/<ten>.md`

## 3. Mức quyền hành động (bắt buộc với mọi nền tảng)

| Mức | Ví dụ | Agent làm gì |
|---|---|---|
| **Tự làm** | Đọc dữ liệu, soạn nháp, phân tích, chạy eval | Làm, ghi lại |
| **Hỏi trước** | Gửi email/tin nhắn ra ngoài, đăng nội dung, bật/tắt/tăng ngân sách quảng cáo, sửa cấu hình shop, merge PR, ghi vào hệ thống thật | Dừng, trình bày, chờ Quân xác nhận |
| **Cấm** | Thanh toán, chuyển tiền, xoá dữ liệu không có bản sao, đưa dữ liệu khách thật vào repo, sửa raw assets | Không làm, kể cả khi được bảo |

Cách dịch bảng này sang từng nền tảng: `dieu-phoi/quy-tac-giao-viec.md`.

## 4. Nguyên tắc làm việc

Mỗi nguyên tắc là một skill nhỏ trong `dieu-phoi/nguyen-tac/`. Bắt buộc cho mọi việc:
- `xac-minh-truoc-khi-bao-xong` — nộp bằng chứng, không chỉ nói "xong".
- `sua-dung-tang` — lỗi thuộc tầng nào (harness / skill / agent / tri thức) thì sửa tầng đó.
- `bot-truoc-khi-them` — màng lọc Hermes trước khi thêm tool, skill, agent mới.
- `chi-dung-cho` — quy trình nặng chỉ cho việc sai thì tốn kém.
- `khong-bia` — thiếu cơ sở thì nói "không đủ cơ sở", không bịa số, không bịa nguồn.

## 5. Khi sửa một skill

1. Skill đó phải có `evals/` ở repo của nó (chuẩn: `may-cham/README.md`).
2. Chạy `python may-cham/cham.py cham --repo <repo> --skill <ten> --so-sanh` trước và sau khi sửa.
3. Chỉ mở PR khi điểm sau ≥ điểm trước. Ghi kết quả vào mô tả PR.

## 6. Khi gặp skill mới từ bên ngoài

Không cài thẳng. Theo `doi-chieu/quy-trinh.md`: kiểm dịch → đối chiếu với `danh-muc/skills.yaml` → gắn nhãn Trùng / Bổ sung / Mới / Loại → chấm trước/sau.
Tri thức bên ngoài mặc định ở tầng **"thu thập, chưa kiểm chứng"**.

## 7. Sau mỗi phiên đáng kể

Chạy skill `vong-lap/cham-phien` (1 dòng: skill, điểm 1–5, nhãn lỗi). Chi tiết vòng lặp: `vong-lap/README.md`.

## 8. Ngôn ngữ và đặt tên

- Tiếng Việt, câu ngắn, thẳng việc. Thuật ngữ tiếng Anh chỉ khi không có từ thay thế.
- Tên skill: tên khái niệm chuẩn, ngắn, dễ gọi (`okr`, `chot-sale`). Không viết tắt khó hiểu kèm số (`kh-03`).
- Số điện thoại cho hệ thống quảng cáo: thêm 84, bỏ số 0 đầu.

## 9. Quyết định kiến trúc

Ghi vào `DECISIONS.md` theo mẫu: Ngày | Bối cảnh | Lựa chọn | Chọn | Lý do | Đảo ngược được (C/K). Đọc trước khi đề xuất thay đổi lớn.
