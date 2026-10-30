---
name: so-bai-hoc
description: Ghi và dùng lại bài học của vòng lặp cải tiến qua sổ SQLite. Dùng sau khi bị sửa, khi một lỗi lặp lại, trước việc giống việc cũ, và khi một quy tắc đủ chín để thành một dòng playbook hoặc một skill nháp.
---
# Sổ bài học

Sổ là một DB SQLite trên máy riêng, tìm full-text BM25. Repo public: không commit DB, wiki, proposals, và không ghi dữ liệu khách hay trích dẫn thật.

CLI, từ gốc repo:

```bash
python3 vong-lap/so-bai-hoc/ledger.py --actor <ten-bot> <lenh>
```

Thêm `--json` khi cần máy đọc. Thêm `--db` nếu sổ không nằm cạnh file CLI.

## 1. Tìm trước khi làm

Việc giống việc cũ (cùng skill, cùng nền tảng, cùng kiểu yêu cầu):

```bash
ledger.py search "<3-6 tu khoa>" --skill <ten> --tier durable --evidence
```

- Có dấu hay không dấu đều khớp, kể cả `đ`.
- `durable` là mặc định nên theo. `working` là gợi ý mạnh. `scratch` là nháp chưa kiểm.
- Bài làm đổi việc đang làm: chạy `used <id>`.
- Bài sai: không xoá. `retire <id> --reason "..."` hoặc `demote <id>`, rồi ghi bài mới.
- Tra tiền lệ bị từ chối: `search "..." --skill <ten> --status retired`.

## 2. Ghi sau khi bị sửa hoặc khi lỗi lặp

Ghi khi chủ sửa, khi một bước hỏng và đã có cách vá, khi phát hiện điều không hiển nhiên, hoặc khi một thủ tục nhiều bước sẽ phải làm lại.

```bash
ledger.py add --bot <ten> --title "<mot cau lenh>" --text "<lam gi, khi nao, vi sao>" \
  --skill <ten trong danh-muc/skills.yaml> --repo owner/repo --nen-tang goclaw \
  --nhan-loi harness|skill|agent|tri-thuc|mo-hinh|khong-loi --tenant <ma-noi-bo> \
  --tags a,b --confidence 0.0-1.0 --sensitivity none|user|finance|sensitive \
  -e transcript:<ma-phien> -e file:<duong-dan> -e url:https://... -e "quote:<cau ngan>"
```

- Một bài, một quy tắc. Viết thành câu lệnh bot khác làm được mà không cần bối cảnh.
- `skill` phải khớp `danh-muc/skills.yaml`. Bài không gắn skill (lỗi harness) thì để trống.
- `nhan_loi` chỉ một nhãn, theo `sua-dung-tang`.
- Luôn có bằng chứng: mã phiên, file, URL, hoặc câu trích. Không có bằng chứng thì kẹt ở `scratch`.
- Confidence khoảng 0.9 khi chủ nói hoặc đã kiểm lại; khoảng 0.5 khi mới đúng một lần; ≤ 0.3 khi còn là đoán.
- Tìm trước. Đã có bài giống thì `evidence add` hoặc `update`, không tạo bản trùng.
- Không ghi mật khẩu, token, số thẻ, email, số điện thoại, thân tin khách. Dẫn bằng vị trí. Việc về người, tiền, sức khoẻ, dữ liệu riêng thì đặt đúng `--sensitivity`.

## 3. Nâng tầng

`scratch` (nháp) → `working` (có bằng chứng, đã dùng ít nhất một lần) → `durable` (đúng thêm một ca độc lập hoặc chủ xác nhận, confidence ≥ 0.6, status thành `accepted`).

- `promote` từ chối bài không có bằng chứng.
- Bài `sensitivity` khác `none` chỉ lên `durable` hoặc `accepted` khi **cả Dat và Quân** đã duyệt. Ghi hai lần `--owner-approved`, mỗi người một mệnh đề: ai, khi nào, ở đâu. Không điền hộ.
- Vài ngày một lần: `review --since 3`. Gộp bài trùng, retire bài cũ, thêm bằng chứng hoặc hạ bài confidence thấp.
- `wiki build` sau khi sổ đổi. Một trang mỗi tag, mỗi nhận định có chú thích. Không commit `wiki/`.

## 4. Một dòng playbook

Khi một bài `durable` đã `accepted` đáng đưa vào playbook cạnh skill:

```bash
ledger.py playbook export --skill <ten> [--out <repo-skill>/playbook.md]
```

- Thêm đúng một dòng `- [Pnn] ... (giúp: n, hại: n)`. Không sửa dòng cũ. Không sửa `SKILL.md`.
- Số `giúp` / `hại` trên dòng là số trong sổ tại lúc xuất (`update --giup --hai`). Sổ giữ số sống; dòng đã ghi không viết lại.
- Chưa chỉ `--out` thì ghi vào `staging/`, không commit.

## 5. Đề xuất skill kèm eval

Từ ba bài cùng một thủ tục lặp lại (một hoặc hai bài vẫn sinh được nháp, người duyệt phải bổ sung):

```bash
ledger.py skill propose <slug> --title "..." --problem "..." --lessons 12,15,19
ledger.py skill eval <slug>
python may-cham/cham.py kiem --repo <root>/proposals/<slug>
```

- Nháp nằm trong `proposals/<slug>/`: `PROPOSAL.md`, `SKILL.md`, `evals/*.yaml` đúng khung máy chấm. Có ít nhất một tình huống `loai: bay`.
- `skill eval` phải OK. `kiem` phải hết lỗi trước khi đưa YAML sang repo skill.
- Nháp không phải skill đang chạy. Không cài khi chưa có lời đồng ý. Bài nhạy cần cả Dat và Quân.

## 6. Không làm

- Không commit DB, wiki, staging, proposals, CSV xuất từ sổ thật.
- Không đưa dữ liệu khách vào `--text`, `--tenant`, quote, hay dòng playbook.
- Không tự điền `--owner-approved`.
- Không sửa skill đang chạy từ lệnh này. Playbook chỉ được thêm dòng; đề xuất skill chỉ là file nháp.
