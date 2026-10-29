# Quy trình đối chiếu skill bên ngoài với skill nội bộ

Áp cho kho 290 skill cần nghiên cứu, và mọi skill bên ngoài sau này.

## Nguyên tắc chỗ chứa

**290 skill thô không đặt trong repo này.** Repo này được mọi agent đọc lúc khởi động — phải nhỏ, ổn định, tin cậy cao. Kho thô đặt ở repo riêng `skill-lab` (đề xuất), với 3 luật:
1. Không có `marketplace.json` / manifest plugin → không bao giờ được cài.
2. Toàn bộ ở tầng tri thức **"thu thập, chưa kiểm chứng"**.
3. Chỉ agent đối chiếu đọc; không đưa vào ngữ cảnh khởi động của agent khác.

Repo này chỉ giữ: quy trình (file này), mẫu phiếu (`mau-phieu.yaml`), và kết quả đã chốt (cập nhật vào `danh-muc/skills.yaml` + `DECISIONS.md`).

## 7 bước

| Bước | Việc | Ai | Đầu ra |
|---|---|---|---|
| 1. Kiểm dịch | Giấy phép; chỉ dẫn ẩn (prompt injection); lệnh shell nguy hiểm; gọi mạng lạ; trùng tên skill nội bộ | Script + 1 agent đọc | Loại ngay những skill rủi ro |
| 2. Lấy dấu vân tay | Trích name, description, trigger, cấu trúc đầu ra, references, mảng | Script | 1 phiếu / skill (`mau-phieu.yaml`) |
| 3. Ánh xạ | Tìm 0–n skill nội bộ cùng khái niệm trong `danh-muc/skills.yaml` | Agent | Trường `anh_xa` trong phiếu |
| 4. Gắn nhãn | **Trùng** (đã có, không hơn) / **Bổ sung** (có đoạn hay hơn) / **Mới** (khái niệm chưa có, đáng có) / **Loại** | Agent đề xuất, **Quân chốt** | Trường `nhan` |
| 5. Trích delta | Với "Bổ sung": chỉ lấy đoạn hay, viết lại theo giọng và chuẩn MQ, mở PR vào repo skill tương ứng. Với "Mới": qua `bot-truoc-khi-them` trước | Agent | PR |
| 6. Chấm trước/sau | `may-cham cham --so-sanh` trên skill cũ và skill đã gộp | Máy chấm | Bảng điểm trong PR |
| 7. Ghi sổ | Cập nhật `danh-muc/skills.yaml`, LarkBase `Skill_Change_Log` (loại `gop-tu-ngoai`), `DECISIONS.md` nếu thêm skill mới | Agent | Tiền lệ |

Tri thức chỉ lên tầng **"thu thập, đã kiểm chứng"** sau khi qua bước 6. Không bao giờ tự lên tầng "tự trải nghiệm".

## Nhịp làm

Lô 30 skill / tuần, ưu tiên mảng có nhiều skill nội bộ nhất (marketing, sale) vì đối chiếu ở đó có giá trị cao nhất. Ước tính 10 tuần cho 290 skill.

## Ví dụ

Skill ngoài `pricing-psychology-playbook` → ánh xạ `17-pricing-strategy-global` và `dinh-gia-san-pham` → nhãn **Bổ sung** (có bảng ngưỡng giá theo nhóm thu nhập) → trích bảng thành `references/nguong-gia.md` trong `marketing-business-skill` → chấm 6 tình huống của 2 skill trước/sau → tỷ lệ đạt giữ nguyên nhưng giám khảo ghi câu trả lời có căn cứ hơn → giữ, ghi sổ.

## Ứng viên đầu tiên

**pstack** (Lauren Tan, MIT) — có cả bản gốc Cursor và bản port Claude/Codex/ChatGPT để so. Đã xét sơ bộ ở `tham-khao/pstack.md`; chạy đủ 7 bước khi có `skill-lab`.
