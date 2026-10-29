# danh-muc/ — Sổ đăng ký skill của hệ MQ

`skills.yaml` là **một nguồn sự thật** cho câu hỏi "hệ MQ đang có những skill nào, nằm ở đâu, đã có bộ kiểm thử chưa". Mỗi thư mục chứa `SKILL.md` trong các repo skill là một mục.

Cập nhật lần cuối: **2026-10-26** · Tổng **138 skill** trên **12 repo** · **137** có eval · **1** chưa eval.

## Các trường

| Trường | Ý nghĩa | Cách điền |
|---|---|---|
| `ten` | Tên skill | Lấy đúng `name:` trong frontmatter `SKILL.md` (có thể khác tên thư mục, ví dụ `tiktok-ads`) |
| `repo` | Repo chứa skill | `owner/repo` |
| `duong_dan` | Thư mục chứa `SKILL.md` | Đường dẫn trên nhánh mặc định. Repo có bước dựng (`src/` → `plugins/`) thì ghi đường dẫn nguồn |
| `mang` | Mảng nghiệp vụ | Một trong: `sale`, `marketing`, `quang-cao`, `tai-chinh`, `ke-toan`, `dau-tu`, `quan-tri`, `phap-ly`, `san-pham`, `web`, `thuong-mai-dien-tu`, `khac` |
| `mo_ta_ngan` | Tóm tắt `description` | Tiếng Việt, ≤ 120 ký tự, không chứa dữ liệu khách thật |
| `ngon_ngu` | Ngôn ngữ làm việc của skill | `vi` hoặc `en` |
| `nen_tang` | Nơi skill chạy được | Suy từ manifest trong repo: `.claude-plugin` → `claude-code`; `.codex-plugin` hoặc `.agents/` → `codex`; `gpt/` → `chatgpt`; có thư mục hoặc mô tả GoClaw → `goclaw`. Không chắc thì chỉ ghi `claude-code` |
| `co_eval` | Đã có tình huống kiểm thử chưa | `true` khi `evals/` trên nhánh mặc định hoặc nhánh `evals-v1` có tình huống `skill: <ten>` |
| `so_tinh_huong` | Số tình huống kiểm thử | Đếm file YAML / mục có `skill: <ten>`; repo có bảng độ phủ trong `evals/README.md` thì lấy theo bảng đó. `0` nếu chưa có |
| `trang_thai` | Trạng thái sử dụng | `dang-dung` · `dong-bang` · `loai` · `thu-nghiem`. **Quân quyết** — mặc định `dang-dung` khi mới nhập sổ |
| `trung_voi` | Skill khác trong sổ cùng khái niệm | Chỉ ghi khi rõ ràng; ghi ở cả hai phía |
| `ghi_chu` | Ghi chú tự do | Nguồn sửa thật, nhánh đặc biệt, trạng thái repo ghi |

## Quy tắc cập nhật

1. **Thêm, xoá, đổi tên skill ở repo nào thì sửa sổ trong cùng đợt** — thêm/xoá mục, cập nhật `tong_skill`, `theo_repo`, `co_eval`, `chua_eval` ở đầu file và bảng tổng bên dưới.
2. **Thêm tình huống eval** thì cập nhật `co_eval`, `so_tinh_huong` của skill đó. Khi nhánh `evals-v1` được gộp vào nhánh mặc định, sửa cột "Nguồn eval".
3. **`trang_thai` do Quân quyết.** Agent không tự chuyển skill sang `dong-bang` hay `loai`; chỉ đề xuất trong ghi chú hoặc PR.
4. **Phát hiện trùng** thì ghi `trung_voi` ở cả hai mục và thêm dòng vào mục "Nghi trùng" bên dưới.
5. Không đưa tên khách, tên shop, số liệu khách thật vào `mo_ta_ngan` hay `ghi_chu`.
6. Repo có bản dựng tự sinh (`plugins/` sinh từ `src/`, `claude/` sinh từ `core/`) thì chỉ đăng ký một lần, ghi đường dẫn nguồn hoặc ghi nguồn sửa vào `ghi_chu`.

## Bảng tổng theo repo

| Repo | Số skill | Có eval | Chưa eval | Số tình huống | Nguồn eval |
|---|---:|---:|---:|---:|---|
| `admatrixmdp/marketing-business-skill` | 69 | 69 | 0 | 211 | nhánh `evals-v1` |
| `admatrixmdp/sale-suite-os` | 22 | 22 | 0 | 66 | nhánh `evals-v1` |
| `admatrixmdp/meta-suite-os` | 1 | 0 | 1 | 0 | chưa có |
| `admatrixmdp/google-marketing-os` | 6 | 6 | 0 | 35 | nhánh `evals-v1` |
| `admatrixmdp/tiktok-suite-os` | 1 | 1 | 0 | 27 | nhánh `evals-v1` |
| `admatrixmdp/Company-finance-accountant-os` | 3 | 3 | 0 | 12 | nhánh mặc định |
| `admatrixmdp/investment-MA-os` | 2 | 2 | 0 | 6 | nhánh mặc định |
| `admatrixorg/Company-suite-os` | 16 | 16 | 0 | 78 | nhánh mặc định |
| `admatrixmdp/compliance-vn` | 1 | 1 | 0 | 11 | nhánh `evals-v1` |
| `admatrixmdp/product-dev-os` | 9 | 9 | 0 | 33 | nhánh `evals-v1` |
| `admatrixmdp/webmaster-suite-os` | 6 | 6 | 0 | 25 | nhánh `evals-v1` |
| `admatrixmdp/shopee-suite-os` | 2 | 2 | 0 | 9 | nhánh `evals-v1` |
| **Tổng** | **138** | **137** | **1** | **513** | |

### Theo mảng

| Mảng | Số skill |
|---|---:|
| `marketing` | 58 |
| `sale` | 22 |
| `quang-cao` | 17 |
| `quan-tri` | 16 |
| `san-pham` | 9 |
| `web` | 6 |
| `khac` | 2 |
| `thuong-mai-dien-tu` | 2 |
| `tai-chinh` | 2 |
| `dau-tu` | 2 |
| `ke-toan` | 1 |
| `phap-ly` | 1 |

## Repo đã bỏ qua

| Repo | Lý do |
|---|---|
| `personal-finance-os` | Repo rỗng / không phải repo skill |
| `Hr-suite-os` | Repo rỗng / không phải repo skill |
| `core-process` | Repo rỗng / không phải repo skill |
| `admatrixorg/growth-os` | Mã nguồn ứng dụng Go (`cmd/`, `internal/`, `web/`), không tìm thấy `SKILL.md` |
| `webmaster-suite-os` — plugin `b2b` | Plugin khung, `plugins/b2b/skills/` mới có `.gitkeep` |

## Nghi trùng

Cặp cùng khái niệm (đã ghi `trung_voi`):

| Skill A | Skill B | Ghi chú |
|---|---|---|
| `dinh-gia-san-pham` (marketing vn) | `17-pricing-strategy-global` (marketing global) | Cùng tri thức `pricing-core`, khác tên và khác cấu trúc |
| `viet-tu-nhien` (marketing vn) | `humanizer` (marketing global) | Cùng việc khử giọng AI; bản vi 46 mẫu, bản en 35 mẫu |

Cần Quân xem thêm (chưa ghi `trung_voi` vì chưa rõ là trùng):

| Vấn đề | Chi tiết |
|---|---|
| **Trùng tên** `analyzer` | `meta-suite-os` và `google-marketing-os` cùng có skill tên `analyzer`. Cài chung hai plugin vẫn chạy (khác namespace plugin) nhưng gọi trần tên `analyzer` sẽ mơ hồ — cân nhắc đổi thành `meta-ads-analyzer` / `google-ads-analyzer` |
| Bản song song vn ↔ global | 31 skill marketing vn có bản global cùng số thứ tự (ghi trong `ghi_chu`). Đây là biến thể vùng có chủ đích, không tính là trùng |
| `b2b-foundation` ↔ `sale-suite-os` | Skill tài khoản cũ `b2b-foundation` (ngoài các repo đã quét) chồng vai trò với `00-context-ban-hang` và bộ 22 skill sale — đối chiếu rồi gỡ |
| Bản sao skill tài khoản | `product-dev-os` (9 skill) đang có bản sao cùng tên trong skill tài khoản Claude (`linear-mentor`, `linear-task`, `orca-mentor`, `ui-*`, `product-*`); tương tự `meta-ads-analyzer`, `tiktok-ads-analyzer`, `pancake-pos` — xác định bản nào là gốc |
| `19-ke-hoach-ban-hang` ↔ `10-tinh-kpi-nguoc` / `10-reverse-kpi-global` | Cùng phép quy đổi ngược từ doanh thu; một bên ra định mức hoạt động sale, một bên ra ngân sách marketing — có thể dùng chung công thức |
| `21-audit-ads-performance` / `21-ads-audit-global` ↔ `analyzer` (Meta, Google), `tiktok-ads` | Audit tài khoản quảng cáo đa nền tảng chồng với audit chuyên sâu từng nền tảng — cần quy tắc định tuyến |
| `ke-hoach-okr`, `ke-hoach-bsc`, `chien-luoc-swot-tows`, `chien-luoc-pestel` ↔ plugin `strategy-frameworks` | Plugin khung chiến lược trong tài khoản có `okr`, `bsc`, `swot-pestel` — bản Company-suite-os gắn quy trình Business Goal, bản kia là khung chung |
