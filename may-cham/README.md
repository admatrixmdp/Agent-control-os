# Máy chấm eval dùng chung

Một máy chấm cho mọi repo skill của hệ MQ. Đề thi (file YAML) nằm trong `evals/` của từng repo skill; máy chấm chỉ có một, ở đây.

## 1. Chuẩn định dạng tình huống (chuẩn chung toàn hệ)

Lấy từ `Company-finance-accountant-os/evals/README.md`. Một file YAML = một tình huống.

```yaml
id: SL-029                       # duy nhất trong repo
skill: 09-chot-sale              # tên thư mục skill hoặc name trong frontmatter
loai: chuan | bay                # bay = bẫy: agent phải nhận ra và xử lý đúng
mo_ta: ""
dau_vao: |
  (lời người dùng / dữ liệu giả lập)
mong_doi:
  phai_co: ["..."]               # gợi ý chuỗi phải xuất hiện
  khong_duoc_co: ["..."]         # gợi ý chuỗi cấm
  hanh_vi: ""                    # MÔ TẢ HÀNH VI — căn cứ phán xử cuối cùng
can_cu: []
nguoi_duyet: ""                  # để trống = chưa chính thức
```

Quy tắc độ phủ: mỗi skill ≥ 3 tình huống, ≥ 1 bẫy. Dữ liệu giả lập, không dữ liệu khách thật.

## 2. Hai lệnh

| Lệnh | Cần API key? | Làm gì | Mã thoát |
|---|---|---|---|
| `kiem` | Không | Kiểm YAML hỏng, thiếu trường, sai `loai`, trùng id, skill không tồn tại; cảnh báo độ phủ | 1 nếu có lỗi (hoặc có cảnh báo khi `--nghiem`) |
| `cham` | Có (`ANTHROPIC_API_KEY`) | Chạy từng tình huống, chấm, xuất bảng điểm `.md` + chi tiết `.jsonl` | 1 nếu tỷ lệ đạt < `--nguong` (mặc định 0.8) |

```bash
python may-cham/cham.py kiem --repo ../sale-suite-os
python may-cham/cham.py cham --repo ../sale-suite-os --skill 09-chot-sale --so-sanh
python may-cham/cham.py cham --repo ../sale-suite-os --gioi-han 5          # chạy thử 5 câu
python may-cham/cham.py cham --repo ../sale-suite-os --khong-giam-khao     # chỉ chấm chuỗi, rẻ
```

## 3. Cách chấm một tình huống

1. Nạp `SKILL.md` + `references/` của skill (cắt ở 60.000 ký tự) làm hướng dẫn hệ thống.
2. Gửi `dau_vao` cho mô hình chạy (`--model`, mặc định `claude-opus-5-5`, đổi bằng biến `CHAM_MODEL`).
3. **Kiểm chuỗi:** so `phai_co` / `khong_duoc_co` sau khi chuẩn hoá Unicode, hoa/thường, khoảng trắng.
4. **Giám khảo:** mô hình thứ hai (`--giam-khao`, mặc định `claude-sonnet-5-5`) đọc `hanh_vi` + kết quả kiểm chuỗi + câu trả lời, trả `{dat, ly_do}`. Giám khảo chấm theo ý: câu từ chối có trích lại cụm cấm vẫn đạt.
5. Kết luận cuối = giám khảo (hoặc kiểm chuỗi nếu `--khong-giam-khao`).
6. `--so-sanh`: chạy thêm bản **không có skill** để đo skill có làm tốt hơn mô hình trần không. Cột "Skill có ích?" = **không** là tín hiệu skill thừa hoặc hỏng.

Giám khảo dùng mô hình khác mô hình chạy để giảm tự chấm cho mình (ý từ `/interrogate` của pstack).

## 4. Giới hạn v1 — cần biết

| Giới hạn | Hệ quả | Hướng xử lý |
|---|---|---|
| Không có tool / MCP trong phiên chấm | Skill cần gọi Pancake, Bluecore, Meta… chỉ được chấm phần lập luận và xử lý bẫy | Tình huống nên đưa dữ liệu giả lập ngay trong `dau_vao` |
| Một lượt hỏi đáp | Hành vi "hỏi lại" được chấm ở câu trả lời đầu — đủ cho bẫy thiếu dữ liệu | Hội thoại nhiều lượt: v2 |
| Chỉ Claude API | Chưa đo skill trên GPT / Grok | Adapter `codex exec` / xAI: v2 |
| Giám khảo có thể sai | Kết quả là tín hiệu, không phải phán quyết | Tình huống quan trọng: người duyệt xem `.jsonl` |
| Chưa chạy thật với API | Mới kiểm bằng giả lập | Lần chạy đầu: `--gioi-han 5` trên một repo |

## 5. Gắn vào CI của repo skill

Thêm vào repo skill file `.github/workflows/eval.yml`:

```yaml
name: Kiểm eval
on:
  pull_request:
    paths: ["evals/**", "plugins/**", "skills/**"]
jobs:
  kiem:
    uses: admatrixmdp/Agent-control-os/.github/workflows/kiem-eval.yml@main
    with:
      nghiem: false
```

Lưu ý: gọi workflow từ repo private khác cần bật **Settings → Actions → Access → "Accessible from repositories owned by the user"** ở repo Agent-control-os. Lệnh `cham` trên CI cần secret `ANTHROPIC_API_KEY` ở repo skill và tốn tiền — để chạy tay hoặc chạy theo lịch, không chạy mỗi PR.

## 6. Kiểm thử chính máy chấm

```bash
python may-cham/tests/kiem_thu.py   # 7 kiểm thử, không cần API key
```

Thư mục `tests/mau/` chứa skill mẫu `chot-sale-mau` chỉ để kiểm thử, không phải skill thật.

## 7. Mở rộng (v2)

- Adapter nền tảng: `--nen-tang codex` (gọi `codex exec`), `--nen-tang xai`.
- Hội thoại nhiều lượt: trường `luot_tiep` trong YAML.
- Ghi kết quả về LarkBase bảng `Skill_Change_Log` (`vong-lap/larkbase.md`).
- Tập giữ lại (held-out): trường `giu_lai: true` — không dùng khi sửa skill, chỉ dùng để kiểm cuối.
