# Quy tắc đóng góp — 6 cổng

Mọi thay đổi vào repo này **qua đủ 6 cổng, theo đúng thứ tự**. Luật áp cho mọi nguồn: agent grok, claude, codex, hay người sửa tay. **Admin cũng không được bỏ qua cổng nào**, kể cả khi GitHub cho phép (quyền admin, bypass branch protection, merge thẳng, push thẳng lên nhánh gốc). Bỏ một cổng thì PR không được merge; đã lỡ merge thì revert và làm lại từ cổng bị bỏ.

| Cổng | Ai | Đạt khi |
|---|---|---|
| 1. Phương án | CTO | CTO ra phương án hoặc duyệt gói nguồn trước khi làm: phạm vi, file được sửa, tiêu chí nghiệm thu |
| 2. Thực thi | Agent thực thi (Delivery) hoặc người làm tay | Làm trên nhánh riêng, mở PR theo mẫu `.github/pull_request_template.md`. Mỗi PR một skill hoặc một việc, diff ≤ 600 dòng |
| 3. Máy kiểm | GitHub Actions `Cổng PR` | 3 check `cong-kiem-thu`, `cong-gitleaks`, `cong-ve-sinh` xanh trên head hiện tại |
| 4. CTO duyệt | CTO | Check `cong-cto` xanh: có `CTO-KET-LUAN: DAT @<head_sha>` (comment hoặc review) hoặc nhãn `cto-dat`, do login trong danh sách cho phép, đúng head hiện tại. Push mới thì kết luận cũ hết hiệu lực, nhãn bị gỡ, CTO duyệt lại |
| 5. Kiểm nội dung | Self Evolution | Đọc nội dung skill hoặc tài liệu, xác nhận không lộ dữ liệu, không lệch luật `AGENTS.md` |
| 6. Merge | Anh Dat hoặc Quân (CODEOWNERS) | Người merge kiểm cổng 1–5 đều có bằng chứng rồi mới merge. **Agent không bao giờ merge** |

## 4 check của cổng 3–4 (`.github/workflows/cong-pr.yml`)

- `cong-kiem-thu`: `python3 may-cham/tests/kiem_thu.py` và `python3 danh-muc/kiem_so.py --base <nhánh gốc>`. Sửa một `SKILL.md` trong repo mà không cập nhật `sha256` trong `danh-muc/skills.yaml` thì trượt.
- `cong-gitleaks`: quét các commit của PR theo `.gitleaks.toml` (bộ luật mặc định cộng số điện thoại, email thật, link phiên agent, domain/org nội bộ).
- `cong-ve-sinh`: `python3 .github/ve_sinh.py --base <nhánh gốc>`. Chặn file `.db`, `.sqlite`, `.env`; số điện thoại, email, IP, đường dẫn cá nhân, domain/org nội bộ trong dòng thêm mới; link phiên agent trong commit message và thân PR; footer công cụ trong thân PR.
- `cong-cto`: như cổng 4 ở bảng trên.

Chạy cả 4 tại chỗ trước khi mở PR, dán kết quả vào thân PR (lệnh có trong mẫu PR).

## Dữ liệu và tên thật

- **Cấm** domain, org, tên miền con, IP và tài khoản thật của hệ thống nội bộ; cấm số điện thoại, email, tên khách, đường dẫn máy cá nhân, file `.db` và trích dẫn transcript.
- **Được dùng** giữ chỗ giả công khai, rõ ràng là giả: `example.com`, `example.vn` (và tên miền con của chúng), `org-a`, `org-b`, `app-agent`, `tenant-demo`. Ví dụ `github.com/org-a/app-agent` hay `ops@example.vn` qua được cả `cong-gitleaks` lẫn `cong-ve-sinh`; domain thật thì trượt.
- Trường `repo` trong `danh-muc/skills.yaml` ghi `owner/repo` thật là dữ liệu sổ, không phải link, nên được phép.
- Không để link phiên claude.ai, cursor.com (agents) hay chatgpt trong commit message và thân PR. Xóa footer công cụ khỏi thân PR.

## Sửa chính các cổng

File định nghĩa cổng (`.github/`, `.gitleaks.toml`, `danh-muc/kiem_so.py`, file này) do CODEOWNERS bảo vệ và cũng qua đủ 6 cổng. Nới một luật quét phải ghi lý do trong thân PR.
