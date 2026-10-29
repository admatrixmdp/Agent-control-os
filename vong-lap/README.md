# Vòng lặp cải tiến skill

Hai vòng tách rời: **vòng A** chạy trong mỗi phiên làm việc, **vòng B** chạy ban đêm để cải tiến skill. Ghép từ 4 vòng đã được kiểm chứng: skill-creator (Anthropic), autoresearch (Karpathy), harness engineering (OpenAI), ACE playbook (Stanford/SambaNova).

## Vòng A — thực thi (mỗi phiên)

| Bước | Việc | Trạng thái |
|---|---|---|
| A1 | Gọi skill | Có |
| A2 | Đọc luật: `AGENTS.md`, `SKILL.md` | Có |
| A3 | Đọc bài học cũ: `playbook.md` cạnh skill | **Chưa có** — tạo khi skill có bài học đầu tiên |
| A4 | Làm việc, lấy số từ nguồn (MCP) | Có |
| A5 | Sensor kiểm đầu ra | Chưa — để sau, lỗi lặp lại sẽ chỉ ra sensor nào đáng viết |
| A6 | Ghi dấu: trace (GoClaw có sẵn) + **`cham-phien`** (mọi nền tảng) | `cham-phien` có ở `vong-lap/cham-phien/` |

## Vòng B — tiến hoá (cron đêm)

| Bước | Việc | Ở đâu | Trạng thái |
|---|---|---|---|
| B1 | Gom dòng chấm phiên + trace mới, gắn nhãn tầng lỗi | GoClaw cron / Claude scheduled task | Thiết kế |
| B2 | Đề xuất **một** dòng bài học vào `playbook.md` (chỉ thêm, không viết lại) | PR vào repo skill | Thiết kế |
| B3 | Tra tiền lệ: đề xuất tương tự từng bị từ chối chưa | LarkBase `Skill_Change_Log` | Thiết kế |
| B4 | Chạy `may-cham` có sửa vs không sửa | `may-cham/cham.py` | **Có** |
| B5 | Tốt hơn → để PR chờ duyệt; kém hơn → đóng PR | GitHub | Thiết kế |
| B6 | Ghi tiền lệ chấp nhận / từ chối | LarkBase | Thiết kế |

## Định dạng `playbook.md` (đặt cạnh SKILL.md trong repo skill)

```markdown
# Playbook — <tên skill>
<!-- Chỉ thêm dòng mới. Không viết lại dòng cũ. Bộ đếm cập nhật sau mỗi lần chấm. -->
- [P01] Ô không có văn bản pháp lý → ghi "—", không suy đoán. (giúp: 3, hại: 0)
- [P02] Lấy đơn 7 ngày trong 1 lần gọi, xử lý cục bộ. (giúp: 5, hại: 0)
```

Vì sao chỉ thêm: viết lại toàn bộ làm bối cảnh thoái hoá dần thành đoạn mơ hồ (lỗi "sập bối cảnh" mà ACE mô tả).

## Mức tự động theo loại tài sản

| Tài sản | Mức tự động |
|---|---|
| Playbook / tri thức | Cao — delta tự động, Quân xem tuần |
| Skill có kết quả kiểm được (số, định dạng, file) | Vừa–cao — eval tự động, Quân duyệt diff |
| Skill nội dung (copy, brief, chiến lược) | Thấp — giám khảo + Quân chấm mẫu |
| Agent, định tuyến | Thấp — chỉ khi dữ liệu nhãn lỗi chỉ rõ |
| Harness, luật quyền | Rất thấp — Quân quyết, ghi `DECISIONS.md` |

## Ba rủi ro đã biết

1. **Skill tự sinh có thể vô dụng** — nghiên cứu 2026: skill do người tuyển chọn giúp rõ, skill tự sinh có thể không tăng trung bình. → Không để agent tự đẻ skill hàng loạt.
2. **"Vách tự tin"** — vòng lặp càng thành công càng cố chấp. → Bước B3 tra tiền lệ, không chỉ đếm thành công.
3. **Lách metric** — agent tối ưu chuỗi kiểm thay vì ý. → Giám khảo chấm theo `hanh_vi`, tập giữ lại (v2), Quân xem mẫu.
