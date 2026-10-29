# Claude Code — giới hạn liên kết plugin giữa các repo

> Hệ MQ tách tri thức thành nhiều repo `*-os` (marketing, webmaster, meta, google, tiktok, shopee, sale…). File này ghi rõ khi tách repo thì plugin **liên kết được tới đâu** và **gãy ở đâu**, để không thiết kế một tính năng dựa trên cơ chế không tồn tại.
> Rút từ đề xuất kiến trúc 09/2026 trong nhánh nghiên cứu cũ của `marketing-business-skill` (mục 6B). Phần còn lại của đề xuất đó — "một repo, nhiều plugin" — không giữ vì hệ đã chọn tách repo.
> **Xác nhận:** mức 1 và mức 2 đối chiếu tài liệu Claude Code ngày 2026-10-29. Mức 3 **chưa xác minh lại** — kiểm trước khi dựa vào.

Câu trả lời có ba mức: hai mức đầu dùng được, mức thứ ba gãy.

## Mức 1 — Một marketplace trỏ tới plugin nằm ở repo khác: dùng được

`source` của từng plugin trong `marketplace.json` không bắt buộc nằm cùng repo:

```json
{
  "name": "your-marketplace",
  "owner": { "name": "Your Org" },
  "plugins": [
    { "name": "core",        "source": "./core" },
    { "name": "meta-suite",  "source": { "source": "github", "repo": "your-org/meta-suite-os" } },
    { "name": "shopee-pack", "source": { "source": "git-subdir", "url": "your-org/monorepo", "path": "packs/shopee" } }
  ]
}
```

Các kiểu `source`: đường dẫn tương đối (`./…`, không được dùng `..`), `github`, `git-subdir`, `url` (git ở host bất kỳ), `archive` (zip qua HTTPS), `npm`, `command`. Nguồn git ghim được bằng `ref` hoặc `sha`.

**Hệ quả:** giữ được **một marketplace "mặt tiền"** — người dùng chỉ `marketplace add` một lần — trong khi nội dung nằm ở nhiều repo. Đây là mô hình tốt nhất khi đã tách repo.

## Mức 2 — Plugin phụ thuộc plugin ở marketplace khác: dùng được, có điều kiện

Mặc định Claude Code **không cài** phụ thuộc từ marketplace khác, trừ khi người dùng đã tự cài và bật nó ở cùng phạm vi. Muốn cho phép, khai tên marketplace đích trong `allowCrossMarketplaceDependenciesOn` của **marketplace gốc** (marketplace chứa plugin người dùng đang cài):

```json
{
  "name": "your-marketplace",
  "owner": { "name": "Your Org" },
  "allowCrossMarketplaceDependenciesOn": ["your-shared-marketplace"],
  "plugins": [
    { "name": "meta-suite", "source": "./meta",
      "dependencies": [ { "name": "core", "marketplace": "your-shared-marketplace" } ] }
  ]
}
```

Ba lưu ý:
- **Chỉ danh sách cho phép của marketplace gốc có hiệu lực** — không kế thừa qua trung gian.
- **Ràng buộc phiên bản** (`"version": "^2.0"`) giải theo tag git dạng `<tên-plugin>--v<phiên-bản>`. Plugin có repo riêng mà không có tag khớp → cài thất bại. Lệnh `claude plugin tag --push` tạo tag đúng chuẩn.
- Thiếu khai báo cho phép: khai phụ thuộc trong marketplace entry thì cài bị từ chối; khai trong `plugin.json` thì cài xong nhưng plugin không nạp được.

## Mức 3 — Dùng chung FILE giữa các repo: không được (chưa xác minh lại)

Plugin chỉ đọc file trong thư mục của chính nó. Liên kết tượng trưng (symlink) chỉ có tác dụng **trong cùng một marketplace**. Hậu quả:

| Muốn làm | Cùng marketplace | Khác marketplace |
|---|---|---|
| Plugin A đọc `benchmarks.md` của plugin B | Symlink — được | Không có cách |
| Gói tổng dùng lại skill của nhiều plugin | Symlink — được | Chỉ khai phụ thuộc (mức 2), không lấy được file |
| Plugin kế thừa `glossary.md` chuẩn | Symlink — được | Phải **chép** vào từng repo |
| Sửa một công thức chung, mọi nơi cập nhật | Tự động | Sửa tay N repo |

## Quy tắc cho hệ MQ

| Tình huống | Làm |
|---|---|
| Hai repo cần cùng một tri thức (ví dụ đo sau click: GA4 ở `webmaster-suite-os`, quảng cáo ở `marketing-business-skill`) | **Một nơi giữ bản đầy đủ**, nơi kia giữ tóm tắt + đường dẫn. Không chép nguyên văn sang hai nơi |
| Muốn người dùng cài nhiều repo một lần | Một marketplace mặt tiền, `source` trỏ `github` tới từng repo |
| Plugin cần MCP hoặc skill của plugin repo khác | Khai `dependencies` + `allowCrossMarketplaceDependenciesOn`, gắn tag phiên bản |
| Muốn tham chiếu file của repo khác | Không làm. Chép phần nhỏ cần dùng, ghi nguồn và ngày chép |
