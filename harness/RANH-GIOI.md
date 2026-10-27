# Ranh giới: giữ harness/ cắt ra được nguyên khối

Mục tiêu: ngày tách sang repo riêng, chỉ cần chép nguyên thư mục `harness/`, sửa đúng các điểm nối ghi dưới đây, không phải lục cả repo.

## 6 luật

1. **Mọi file của harness nằm trong `harness/`.** Không đặt file harness ở thư mục khác, kể cả `vong-lap/`, `dieu-phoi/`.
2. **Liên kết nội bộ dùng đường dẫn tương đối trong `harness/`.**
3. **Ra ngoài chỉ qua điểm nối khai báo ở bảng dưới.** Cần điểm nối mới → thêm dòng vào bảng trong cùng PR.
4. **Bên ngoài trỏ vào `harness/` chỉ ở 2 chỗ:** một dòng trong `README.md` gốc và một dòng trong `DECISIONS.md` gốc.
5. **Quyết định của harness ghi vào `harness/DECISIONS.md`**, không ghi vào `DECISIONS.md` gốc.
6. **Không chép luật từ ngoài vào.** Luật gốc ở đâu thì ở đó; harness chỉ trỏ tới và ánh xạ.

## Điểm nối ra ngoài

| Điểm nối | Harness dùng để làm gì | File trong harness dùng nó | Khi tách repo |
|---|---|---|---|
| `AGENTS.md` mục 3 (mức quyền) | Nguồn gốc 3 mức Tự làm / Hỏi trước / Cấm | `chinh-sach/quyen.yaml`, `chinh-sach/cam.yaml` | Trỏ sang `admatrixmdp/Agent-control-os/AGENTS.md` |
| `may-cham/` | Chạy đề kiểm thử | `danh-gia/README.md` | Gọi máy chấm như công cụ ngoài, hoặc chép adapter harness |
| `danh-muc/skills.yaml` | Tra skill khi đề kiểm thử cần | `danh-gia/README.md` | Trỏ sang repo gốc |

## Khi nào tách (đề xuất, chờ Quân chốt)

Tách khi có **một** trong các dấu hiệu:

- Harness có **mã chạy**, không chỉ tài liệu và cấu hình.
- Có từ **2 sản phẩm** trở lên dùng chung bộ chính sách này.
- Cần **CI hoặc quyền truy cập riêng** khác Agent-control-os.
- Có người hoặc đội **phụ trách riêng** harness.

## Các bước tách

1. Tạo repo mới, chép lịch sử riêng của `harness/` (vd `git filter-repo --path harness/ --path-rename harness/:`).
2. Đổi từng dòng ở bảng điểm nối sang tham chiếu repo gốc.
3. Ở Agent-control-os: thay thư mục bằng một dòng trỏ sang repo mới; sửa 2 dòng ở `README.md` và `DECISIONS.md` gốc.
4. Ghi quyết định tách vào `DECISIONS.md` của cả hai repo.
