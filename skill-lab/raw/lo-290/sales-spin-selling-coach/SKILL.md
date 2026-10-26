---
name: sales-spin-selling-coach
description: |
  Hướng dẫn SPIN Selling cho AE — Situation, Problem, Implication, Need-payoff với 20 câu hỏi mẫu mỗi loại. Trigger phrases: "SPIN selling", "SPIN framework", "câu hỏi SPIN", "SPIN coaching", "Situation Problem Implication Need-payoff", "SPIN training", "SPIN script", "SPIN questioning", "soạn câu hỏi SPIN", "SPIN sales coach". Output là Markdown coaching guide + Excel question bank.
---

# SPIN Selling Coach (Neil Rackham)

## Mục Tiêu
Đào tạo AE technique đặt câu hỏi SPIN để KH tự nhận pain + value, thay vì AE "thuyết giáo" — tăng deal closure 30-50% theo nghiên cứu Huthwaite.

## Khi Nào Dùng
- AE mới onboard training discovery
- Roleplay weekly sales meeting
- Sản phẩm complex cần consultative selling
- KH skeptical / không thấy pain
- Trước demo enterprise

## Bước 1: S — Situation Questions (Tìm hiểu hiện trạng)
Mục đích: lấy data, KHÔNG quá nhiều (KH chán).

Ví dụ:
- "Team sales bên anh hiện bao nhiêu người?"
- "Đang dùng CRM nào? Tích hợp với gì?"
- "Quy trình từ MQL đến closed-won mất bao lâu trung bình?"
- "Tỷ lệ AE đạt quota?"

Rule: max 5 câu Situation trước khi chuyển Problem.

## Bước 2: P — Problem Questions (Khai phá vấn đề)
Mục đích: KH tự nói pain.

- "Phần nào của quy trình tốn time nhất?"
- "AE complain về điều gì khi dùng CRM?"
- "Có chỗ nào data nhập trùng / mất?"
- "Forecast accuracy bao nhiêu %? Đủ cho leadership không?"

## Bước 3: I — Implication Questions (Đào sâu hậu quả)
Mục đích: làm pain LỚN, KH thấy urgency.

- "Nếu AE tốn 2h/ngày làm admin, ảnh hưởng quota thế nào?"
- "Forecast off 20% mỗi quý, board phản ứng ra sao?"
- "Bao nhiêu deal lost vì follow-up chậm 24h?"
- "Cost of AE turnover khi tool tệ là bao nhiêu/năm?"

Câu hỏi Implication TĂNG perceived value, KH bắt đầu muốn mua.

## Bước 4: N — Need-payoff Questions (KH tự bán cho chính mình)
Mục đích: KH tự nói value, không phải AE.

- "Nếu giải quyết được X, team anh tiết kiệm bao nhiêu giờ?"
- "Forecast accuracy 90% sẽ giúp board thế nào?"
- "Cải thiện turnover sẽ tiết kiệm $$ nào?"
- "Nếu close deal nhanh 30%, ARR tăng bao nhiêu?"

→ KH tự articulate value = giảm giá phản đối + tăng commitment.

## Bước 5: Pattern SPIN trong Discovery 30 phút
- Phút 1-5: Situation (5 câu)
- Phút 6-15: Problem (5-7 câu)
- Phút 16-22: Implication (3-5 câu, không vội)
- Phút 23-28: Need-payoff (3-4 câu)
- Phút 29-30: Recap + next step

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Gong/Chorus MCP: phân tích AE đang hỏi S/P/I/N tỷ lệ nào
- Salesforce MCP: log SPIN findings vào opportunity
- Slack MCP: share best SPIN questions weekly
- Video MCP: roleplay record + review

**Fallback API:**
```python
# Phân tích tỷ lệ SPIN trong call AE
def analyze_spin(transcript):
    counts = {"S": 0, "P": 0, "I": 0, "N": 0}
    for q in extract_questions(transcript):
        if any(k in q for k in ["bao nhiêu","đang dùng","quy trình"]): counts["S"]+=1
        elif any(k in q for k in ["khó","vấn đề","tốn"]): counts["P"]+=1
        elif any(k in q for k in ["hậu quả","ảnh hưởng","mất"]): counts["I"]+=1
        elif any(k in q for k in ["nếu","tiết kiệm","giá trị"]): counts["N"]+=1
    return counts  # Top AE tỷ lệ I+N ~40%
```

## Bước 7: Output Format
- **File 1**: `spin_coaching_guide.md` — guide 6 trang đầy đủ
- **File 2**: `spin_question_bank.xlsx` — 80 câu chia 4 loại theo persona
- **File 3**: `spin_call_template.md` — flow 30 phút
- **File 4**: `spin_roleplay_scenarios.md` — 10 scenario practice
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ 20 câu mỗi loại S/P/I/N
- [ ] Pattern 30 phút có proportion đúng
- [ ] Implication làm KH "ouch"
- [ ] Need-payoff để KH tự nói value
- [ ] Roleplay weekly schedule
- [ ] Manager coach call review
