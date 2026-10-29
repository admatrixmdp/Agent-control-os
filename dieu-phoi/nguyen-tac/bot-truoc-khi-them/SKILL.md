---
name: bot-truoc-khi-them
description: Màng lọc Hermes — bắt buộc chạy trước khi thêm tool, framework, repo, skill hay agent mới vào hệ MQ. Chấm 4 tiêu chí rồi chốt REJECT hoặc ADAPT; nếu ADAPT chỉ lấy phần lõi. Dùng khi Quân muốn cài, tích hợp, hoặc khi agent định tạo thứ mới.
---
# Bớt trước khi thêm (màng lọc Hermes)

## Bước 1. Hỏi trước: có thể bớt thay vì thêm không?
- Skill đã có làm được không? Tra `danh-muc/skills.yaml`.
- Gộp vào skill có sẵn được không?
- Bỏ đi thứ gì để không cần thêm?

## Bước 2. Chấm 4 tiêu chí
| Tiêu chí | Câu hỏi | Điểm 1–5 |
|---|---|---|
| Giá trị lõi | Giải quyết đau thật nào, đo bằng gì? | |
| Phình hệ | Thêm bao nhiêu file, skill, chỗ phải bảo trì? | (cao = phình ít) |
| Tích hợp | Chạy với chuẩn SKILL.md, eval YAML, MCP sẵn có không? | |
| An toàn | Giấy phép, dữ liệu ra ngoài, chỉ dẫn ẩn, quyền ghi | |

## Bước 3. Chốt
- **REJECT** nếu giá trị lõi ≤ 2 hoặc an toàn ≤ 2.
- **ADAPT** nếu không: ghi rõ lấy phần nào, bỏ phần nào, đặt ở đâu.
- Ghi vào `DECISIONS.md`.

## Ví dụ
pstack (47 mục): ADAPT. Lấy cách đóng nguyên tắc thành skill, ý tưởng định tuyến, bảng chuyển đổi giữa nền tảng. Bỏ playbook viết code. Xem `tham-khao/pstack.md`.
