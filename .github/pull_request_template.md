<!-- Mọi PR, từ mọi nguồn (grok, claude, codex, làm tay), qua đủ 6 cổng trong QUY-TAC-DONG-GOP.md. Không để link phiên agent hay footer công cụ trong thân PR. -->
## Thay đổi
- Việc gì, vì sao (1–3 dòng). Phương án CTO (cổng 1):

## Phạm vi
- [ ] Một skill hoặc một việc cho mỗi PR; diff ≤ 600 dòng
- [ ] Chỉ sửa các file liệt kê dưới đây:

## Mức nhạy cảm và duyệt
- Mức nhạy cảm: `none` / `user` / ...
- Trạng thái duyệt: (ai đã duyệt, ngày)

## Bằng chứng kiểm (cổng 3, dán kết quả thật)
- [ ] `python3 may-cham/tests/kiem_thu.py`:
- [ ] `python3 danh-muc/kiem_so.py --base origin/<nhánh gốc>`:
- [ ] `gitleaks git --log-opts="origin/<nhánh gốc>..HEAD" --config .gitleaks.toml`:
- [ ] `python3 .github/ve_sinh.py --base origin/<nhánh gốc>`:
- [ ] Skill sửa `SKILL.md` đã cập nhật `sha256`, `phien_ban` trong `danh-muc/skills.yaml`

## Dữ liệu
- [ ] Không dữ liệu khách thật, không file `.db`, không trích transcript; chỉ dùng giữ chỗ example.com, example.vn, org-a, org-b, app-agent, tenant-demo

## Cổng 4–6
- CTO: `CTO-KET-LUAN: DAT @<head_sha>` hoặc nhãn `cto-dat` (push mới thì phải duyệt lại)
- Self Evolution kiểm nội dung:
- Merge: anh Dat hoặc Quân. Agent không merge.
