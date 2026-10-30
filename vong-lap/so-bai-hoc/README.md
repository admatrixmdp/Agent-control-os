# Sổ bài học

Sổ dùng chung cho vòng lặp cải tiến. Bot ghi bài học kèm bằng chứng, tìm lại bằng BM25, nâng tầng, xuất một dòng playbook, và sinh tình huống để `may-cham` kiểm. Chỉ Python 3 thư viện chuẩn và SQLite FTS5.

Sổ gốc là file SQLite trên máy riêng. Sync sang LarkBase (`vong-lap/larkbase.md`) là tuỳ chọn, chưa nối. Repo này public: không commit `ledger.db`, `wiki/`, `staging/`, `proposals/`, và không ghi bài học hay trích dẫn thật.

```
vong-lap/so-bai-hoc/
  ledger.py          # CLI
  SKILL.md
  tests/test_ledger.py
  ledger.db          # máy riêng, gitignore
  wiki/              # `wiki build` sinh ra, gitignore
  staging/           # playbook xuất tạm, gitignore
  proposals/<slug>/  # nháp skill + evals/*.yaml, gitignore
```

Chạy từ gốc repo:

```bash
alias sbh='python3 vong-lap/so-bai-hoc/ledger.py --actor ten-bot'
```

`--db` hoặc `SELF_EVO_DB` đổi file DB. `--root` hoặc `SELF_EVO_ROOT` đổi chỗ ghi wiki, staging, proposals. Thêm `--json` để lấy JSON.

## Lệnh

| Việc | Lệnh |
|---|---|
| Thêm bài | `sbh add --bot grok-a --title "..." --text "..." --skill <ten> --repo owner/repo --nen-tang goclaw --nhan-loi skill --tenant gia-lap --tags a,b --confidence 0.8 --sensitivity none -e transcript:phien-gia-lap -e file:./duong-dan -e "quote:..."` |
| Tìm | `sbh search "gui tin" [--skill X] [--tier durable] [--status retired] [--nhan-loi tri-thuc] [--all-terms] [--evidence]` |
| Xem | `sbh show 3`, `sbh list --tier working --skill X` |
| Bằng chứng | `sbh evidence add 3 url:https://... --note "..."`, `sbh evidence list 3` |
| Tầng | `sbh promote 3`, `sbh demote 3`, `sbh retire 3 --reason "..."`, `sbh accept 3` |
| Sửa / đã dùng | `sbh update 3 --confidence 0.9 --giup 2 --hai 0`, `sbh used 3` |
| Rà | `sbh review --since 3` |
| Playbook | `sbh playbook export --skill <ten> [--out playbook.md] [--lesson 3]` |
| CSV | `sbh export-csv out.csv`, `sbh import-csv out.csv` (bỏ qua `uid` đã có) |
| Wiki | `sbh wiki build` |
| Skill nháp | `sbh skill propose <slug> --title "..." --problem "..." --lessons 1,2`, rồi `sbh skill eval <slug>` |
| Nhật ký | `sbh audit [--id 3]` |

## Trường gắn với vòng lặp

| Trường | Ý nghĩa |
|---|---|
| `skill` | Tên đúng `ten` trong `danh-muc/skills.yaml`. Để trống nếu bài không gắn skill (ví dụ lỗi harness). Tên lạ bị từ chối. |
| `repo` | Repo chứa skill, dạng `owner/repo`. |
| `nen_tang` | `claude`, `claude-code`, `chatgpt`, `codex`, `goclaw`, `goso`, `claude-duet`, `dots`, `muse`, `grok-bot`. |
| `nhan_loi` | `harness`, `skill`, `agent`, `tri-thuc`, `mo-hinh`, `khong-loi`. Một nhãn chính, theo `sua-dung-tang`. |
| `tenant` | Mã nội bộ. Không ghi tên khách. |
| `giup`, `hai` | Bộ đếm sống trong sổ. Dòng playbook chỉ chụp số tại lúc xuất. |
| `approvers` | `Dat,Quân` khi đủ hai người duyệt. |

## Quy tắc

- **Tầng:** `scratch` → `working` → `durable`. Chưa có bằng chứng thì ở `scratch`. Lên `durable` cần confidence ≥ 0.6; status chuyển thành `accepted`.
- **Nhạy cảm:** `sensitivity` là `user`, `finance` hoặc `sensitive` thì không lên `durable` hay `accepted` nếu thiếu duyệt của **cả Dat và Quân**. Truyền hai lần `--owner-approved`, mỗi người một mệnh đề (ai, khi nào, ở đâu). `Đạt` và `Quan` không dấu vẫn được nhận. Không tự điền cờ này.
- **Playbook:** `playbook export --skill X` lấy một bài `durable` đã `accepted` của skill đó (confidence cao nhất, chưa xuất) và **thêm** một dòng `- [Pnn] ... (giúp: n, hại: n)`. Không sửa dòng cũ. Không ghi `SKILL.md`. File chưa có thì tạo đầu mục một lần. Mặc định ghi vào `staging/`.
- **Tìm:** có dấu hoặc không dấu đều ra, kể cả `đ`/`d`. Mặc định OR, xếp BM25 (tiêu đề nặng hơn nội dung). `--all-terms` bắt mọi từ. `--status retired` để tra tiền lệ đã bỏ.
- **Rà:** bài mới, bài cũ, confidence thấp, bài không bằng chứng, bài nhạy chưa accepted, cặp nghi trùng (Jaccard ≥ 0.5 hoặc BM25 ≥ 60% điểm tự khớp).
- **Wiki:** chỉ bài `working` và `durable` chưa retire. Mỗi nhận định có chú thích bằng chứng. Bài `sensitive` bị ẩn trừ khi `--include-sensitive`. Không commit thư mục wiki.
- **Đề xuất skill:** ghi `proposals/<slug>/` gồm `PROPOSAL.md`, `SKILL.md` nháp, và `evals/*.yaml` đúng khung `may-cham` (`id`, `skill`, `loai`, `dau_vao`, `mong_doi.phai_co` / `khong_duoc_co` / `hanh_vi`, `can_cu`, `nguoi_duyet`). Có ít nhất một bẫy `loai: bay`. Đây là nháp. Không sửa skill đang chạy. Kiểm bằng `python may-cham/cham.py kiem --repo proposals/<slug>`.
- **Chặn bí mật:** tiêu đề, nội dung, bằng chứng, tenant và dòng playbook bị từ chối nếu có dạng email, số điện thoại, hoặc token. Không ghi thân tin nhắn khách. Dẫn bằng mã phiên hoặc đường dẫn.
- **Nhật ký:** mọi thay đổi vào bảng `audit`. Giờ theo `Asia/Ho_Chi_Minh`.

## Kiểm thử

```bash
python3 vong-lap/so-bai-hoc/tests/test_ledger.py
```

Chạy trên DB tạm. Nếu `ledger.db` cạnh CLI đã tồn tại, cuối buổi kiểm tra kích thước không đổi.
