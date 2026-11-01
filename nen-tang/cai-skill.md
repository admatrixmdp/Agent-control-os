# Cài skill vào công cụ — một bản gốc, nhiều công cụ cùng đọc

Ý tưởng lấy từ OpenKnowledge Skills Studio (2026-11-01, tầng "thu thập, chưa kiểm chứng"). Chỉ lấy nguyên tắc, **không cài ứng dụng** (xem `DECISIONS.md`).

## 1. Bốn luật

| # | Luật | Nghĩa là |
|---|---|---|
| 1 | **Một bản gốc** | Skill nghiệp vụ chỉ sửa ở repo `*-os`. Thư mục skill của Claude Code, Codex, Cursor là **liên kết** tới bản gốc, không phải bản chép |
| 2 | **Bản ai đã sửa thì giữ nguyên** | Ở máy có thư mục thật (bản chép hoặc đã sửa) thì script và Agent Evolution không đè. Phần khác với bản gốc **là bài học**: lấy bằng `chenh`, nộp vào hộp thư |
| 3 | **Chung hay riêng** | Skill có trong `danh-muc/skills.yaml` là skill **chung**: nằm trong repo, có eval, cả đội dùng. Skill **riêng** (giọng viết, thói quen cá nhân của Quân) chỉ ở thư mục cá nhân trên máy, không vào repo, không vào sổ |
| 4 | **Đổi chỗ không đổi tên** | Chuyển skill sang repo khác thì chỉ sửa `repo`, `duong_dan` trong sổ. Giữ nguyên `ten` để sổ bài học và lịch sử điểm eval còn nối được |

## 2. Chọn cách cài

| Cách | Hợp với | Cái giá |
|---|---|---|
| **Plugin** (Claude Code marketplace) | Bộ ổn định, cài một lệnh: Agent Evolution, sale-suite, marketing | Chỉ Claude Code. Sửa tại máy bị bản cập nhật đè |
| **Liên kết** (`scripts/lien_ket_skill.py`) | Skill còn đang tiến hoá; dùng chung cho Codex, Cursor | Phải clone repo và `git pull` để nhận bản mới |
| **Tải lên** | GoClaw (qua API `goclaw_skill_*`) | Bản trên GoClaw là bản chép, cần đồng bộ lại khi bản gốc đổi |
| **Qua MCP hoặc luật** | Agent đám mây: Duet, Dots, Muse, Grok Bot | Xem `nen-tang/<ten>.md` và `mcp/` |

Một repo đã cài vào Claude Code bằng plugin thì **không liên kết thêm vào Claude Code**, nếu không sẽ hiện hai bản cùng skill. Sổ ghi ở `cach_cai_theo_repo`; script tự bỏ qua.

## 3. Lệnh

```bash
export MQ_REPOS=~/repos            # thư mục chứa các repo đã clone, đặt theo tên repo
S=scripts/lien_ket_skill.py

python3 $S kiem --cong-cu claude-code,codex,cursor --noi may --mang sale       # xem trạng thái
python3 $S lien-ket --cong-cu codex,cursor --noi may --mang sale               # in kế hoạch
python3 $S lien-ket --cong-cu codex,cursor --noi may --mang sale --ap-dung     # tạo liên kết
python3 $S lien-ket --cong-cu codex --noi du-an --dich ~/du-an-x --skill 09-chot-sale --ap-dung
python3 $S chenh --cong-cu cursor --noi may --skill 09-chot-sale               # bản riêng khác gì
```

Thư mục của từng công cụ ghi ở `nen-tang/thu-muc-skill.yaml`. Công cụ đổi chỗ đọc skill thì sửa file đó, không sửa script.

| Trạng thái | Nghĩa | Làm gì |
|---|---|---|
| `dung` | Liên kết trỏ đúng bản gốc | Không |
| `chua-co` | Chưa có ở đích | `lien-ket --ap-dung` |
| `ban-rieng` | Thư mục thật ở máy | Giữ. Chạy `chenh`, nộp bài học nếu phần khác đáng giữ |
| `lech` | Liên kết trỏ chỗ khác | Người dùng tự xem; script không sửa |
| `thieu-nguon` | Chưa clone repo, hoặc sổ sai đường dẫn | Clone repo, hoặc sửa sổ |
| `plugin` | Repo cài bằng plugin cho công cụ này | Không |

## 4. Từ bản riêng thành bài học

```bash
python3 scripts/lien_ket_skill.py chenh --cong-cu cursor --skill 09-chot-sale > /tmp/chenh.diff
python3 vong-lap/so-bai-hoc/hop_thu.py nop --bot dat-cursor --skill 09-chot-sale --nen-tang cursor \
  --nhan-loi skill --title "Thêm câu hỏi khi khách chê đắt" \
  --text "Đã sửa tại máy: hỏi 'so với cái gì' trước khi giảm giá. Lý do: 3 deal tháng 10" \
  -e file:/tmp/chenh.diff
```

Agent Evolution chấm trước và sau như mọi bài học khác. Điểm tốt hơn thì phần sửa vào bản gốc, cả đội nhận qua liên kết. Bản riêng ở máy vẫn giữ; người sửa muốn quay về bản gốc thì tự đổi tên thư mục của mình, rồi chạy lại `lien-ket`.

## 5. Lưu ý

- **Windows** (vault `F:\`): script thử symlink trước. Không có quyền thì dùng junction, không cần quyền quản trị. **Chưa kiểm** công cụ nào đọc được junction. Thử từng công cụ trước khi dùng thật.
- **Không gom kho.** `.agent/skills`, `.claude/skills`, `skills/` trong vault là 3 kho khác nhau. Script chỉ thêm liên kết cho skill có trong sổ; không chuyển, không xoá, không trộn thư mục có sẵn.
- Hai repo cùng tên skill (vd `analyzer` của meta-ads và google-ads): sổ ghi `ten_lien_ket` khác nhau. Script dừng nếu còn trùng.
