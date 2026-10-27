# Hook: chặn lặp

Mẫu của OpenCode (arXiv 2609.00006, mục 6.2): lặp thì hỏi người, không tự huỷ.

| Mục | Nội dung |
|---|---|
| Sự kiện | `pre_tool_use` |
| Điều kiện | 3 lần gọi liên tiếp cùng công cụ, cùng đầu vào (so dấu băm) |
| Kết quả | Chặn, hỏi người: "Agent đang lặp lại [công cụ] 3 lần. Tiếp tục hay dừng?" |

Mỗi lần kích hoạt cộng 1 vào chỉ số "số vòng lặp bị phát hiện" (`../chi-so.md`). Tăng đều = skill hoặc công cụ có lỗi thiết kế, sửa ở tầng đó (`sua-dung-tang`).
