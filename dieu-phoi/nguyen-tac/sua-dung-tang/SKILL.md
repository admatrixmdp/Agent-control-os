---
name: sua-dung-tang
description: Nguyên tắc khi một agent hoặc skill cho kết quả sai — gắn nhãn lỗi vào đúng tầng (harness, skill, agent, tri thức, mô hình) rồi sửa tầng thấp nhất giải quyết được. Dùng khi chấm phiên, sửa skill, hoặc agent lặp lỗi.
---
# Sửa đúng tầng

## Năm tầng và dấu hiệu
| Tầng | Dấu hiệu | Sửa ở đâu |
|---|---|---|
| Harness (luật, quyền, điều kiện dừng) | Làm sai phạm vi, chạy quá đà, không dừng, không hỏi khi phải hỏi | `AGENTS.md`, `dieu-phoi/quy-tac-giao-viec.md`, cấu hình nền tảng |
| Skill (thủ tục) | Đúng việc nhưng sai cách, sai định dạng, thiếu bước | `SKILL.md` của skill + thêm eval |
| Agent (vai trò, tool) | Chọn sai skill, sai tool, giao nhầm | `dieu-phoi/bang-dinh-tuyen.md`, cấu hình agent |
| Tri thức | Đúng quy trình nhưng sai dữ kiện, thiếu bối cảnh | `references/` của skill hoặc Knowledge_Base |
| Mô hình | Sai dù mọi tầng trên đúng | Đổi mô hình hoặc chấp nhận, ghi lại |

## Luật
1. Gắn **một** nhãn chính cho mỗi lỗi.
2. Sửa tầng **thấp nhất** giải quyết được. Không sửa lỗi tri thức bằng cách thêm câu lệnh vào skill. Không tạo agent mới để vá lỗi harness.
3. Mỗi lần sửa một thay đổi nhỏ, có thể hoàn tác, kèm eval chứng minh.

## Ví dụ
Agent PESTEL bịa tên nghị định. Nhãn: **tri thức** (không có văn bản trong references) + **skill** (thiếu luật "không có nguồn thì ghi —"). Sửa: thêm luật một dòng vào skill, thêm eval bẫy. Không đổi mô hình.
