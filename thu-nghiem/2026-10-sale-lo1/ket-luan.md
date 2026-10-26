# Kết luận lô 1

Tầng tri thức: **thu thập, chưa kiểm chứng** — đủ để định hướng sửa, chưa đủ để lưu trữ skill nội bộ nào.

## 1. Giả thuyết

| Giả thuyết | Kết quả |
|---|---|
| Nhãn bước 4 đúng khi chạy thử | **Đúng một phần.** "Trùng" của discovery-call đúng. Hai nhãn "bổ sung" bị chấm dư: late-stage-rescue "cao" → vừa; lead-scoring-engine "vừa" → thấp |
| Skill nội bộ tốt hơn không skill | **Chưa kết luận được** (86 vs 88). Bản không skill bị rò tri thức sale-suite |

## 2. Quyết định cho skill ngoài

Đã ghi vào `skill-lab/trang-thai.yaml`.

| Skill ngoài | Trạng thái | Chỉ lấy |
|---|---|---|
| sales-discovery-call-template | **luu-tru** (trùng) | — |
| sales-lead-scoring-engine | cho-gop → `03` | Danh sách loại cứng trước khi chấm |
| sales-late-stage-rescue | cho-gop → `09` | 8 câu chẩn đoán; pilot dưới ngưỡng tự duyệt |
| sales-objection-handling | cho-gop → `10` | Thư viện 20 phản đối, câu mẫu tiếng Việt |
| sales-icp-builder | cho-gop → `01` | Trục công nghệ, sự kiện kích hoạt, cờ đỏ |

## 3. Lỗi skill nội bộ cần sửa (PR riêng vào sale-suite-os)

| Skill | Lỗi | Sửa |
|---|---|---|
| `03-cham-diem-lead` | Đối thủ vẫn được chấm điểm | Luật **loại cứng trước khi chấm**: đối thủ, sai quy mô, sinh viên/thực tập |
| `09-chot-sale` | Bị gọi cho deal kẹt nhưng vẫn ra kịch bản chốt | Nhánh **deal kẹt**: chẩn đoán 8 câu + tin nhắn lối thoát A/B/C + cam kết tối thiểu; chưa gặp người ký thì không viết kịch bản chốt |
| `10-xu-ly-tu-choi` | Output thừa; gợi ý mang case study không cảnh báo | Chuyển nhật ký chịu trách nhiệm sang `14`; luật **chưa có case thật thì để trống** |
| `08` (qua `09`, `16`) | Gán tính cách cho người chưa gặp | Chỉ gán khi có quan sát; chưa gặp → "chưa đủ dữ liệu" |
| Cả bộ sale-suite | Số quy đổi giả định đưa ra như thật | Luật chung: **mọi số giả định kèm câu xin khách số thật** |

Điểm mạnh từ bản không skill đáng đưa vào chuẩn: tin nhắn champion A/B/C (`09`), bảng 3 mức kết quả khi xử lý từ chối (`10`), cảnh báo "chưa thống nhất định nghĩa số đúng" (`16`).

## 4. Sửa bộ test trước lô 2

| Lỗi | Vá |
|---|---|
| Bản không skill bị rò tri thức | Chạy bằng `may-cham cham --so-sanh` qua API thô |
| Đề ghi sẵn nhãn tính cách | Chỉ mô tả hành vi |
| 1 tình huống/cặp, 1 giám khảo | ≥ 3 tình huống/skill (≥ 1 bẫy), 2 giám khảo khác mô hình |

## 5. Việc tiếp theo

1. Chép 4 tình huống vào `sale-suite-os/evals/` + viết thêm 2 tình huống/skill để đủ chuẩn độ phủ.
2. Chạy sạch `cham --so-sanh --gioi-han 5` cho `03`, `09`, `10`, `16` → lấy mốc trước khi sửa.
3. PR sửa 5 điểm mục 3 vào sale-suite-os, gộp delta từ 4 skill `cho-gop` → chấm lại cùng bộ tình huống.
4. PR merge → chuyển 4 skill `cho-gop` sang `luu-tru` (`da-gop`) kèm phiếu.
