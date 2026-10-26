---
name: cham-phien
description: Chốt phiên làm việc bằng một dòng chấm điểm — tóm skill đã dùng, hỏi Quân một câu "điểm 1–5, sai ở đâu", gắn nhãn tầng lỗi, rồi ghi vào sổ. Dùng ở cuối mỗi phiên đáng kể trên mọi nền tảng (Claude, ChatGPT, Duet, Dots, GoClaw), hoặc khi Quân gõ "chấm phiên".
---
# Chấm phiên

Thay cho trace tự động ở những nơi không có trace (chat, agent đám mây). 20 dòng chấm có nhãn lỗi do chủ doanh nghiệp gõ có giá trị hơn 2.000 dòng log máy.

## Bước 1. Tự tóm phiên (không hỏi)
- Skill / agent đã dùng (tên đúng như trong `danh-muc/skills.yaml`; không dùng skill nào thì ghi "không skill").
- Nền tảng.
- Việc: một câu.
- Kết quả: một câu.

## Bước 2. Hỏi Quân đúng một câu
> "Điểm 1–5? Sai ở đâu (nếu có)?"

Không hỏi thêm. Quân không trả lời thì ghi điểm trống, không tự chấm thay.

## Bước 3. Gắn nhãn tầng lỗi
Theo skill `sua-dung-tang`: `harness` / `skill` / `agent` / `tri-thuc` / `mo-hinh` / `khong-loi`. Chỉ một nhãn chính.

## Bước 4. Ghi
Ưu tiên theo thứ tự có sẵn:
1. LarkBase bảng `Session_Scorecard` (`vong-lap/larkbase.md`).
2. Nếu không có kết nối LarkBase: in dòng dưới để Quân dán.

```
Ngày | Nền tảng | Skill | Việc | Điểm | Nhãn lỗi | Sai ở đâu | Link phiên
2026-10-26 | claude | hoach-dinh-chien-luoc | PESTEL ngành nội thất | 3 | tri-thuc | Bịa chính sách ô Pháp lý | <link>
```

## Không làm
- Không tự cho điểm.
- Không ghi dữ liệu khách thật vào cột "Việc" — dùng mô tả chung ("shop mỹ phẩm", "khách B2B ngành xây dựng").
