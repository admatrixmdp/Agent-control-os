---
name: sales-challenger-script
description: |
  Script Challenger Sales — Teach (insight mới), Tailor (cá nhân), Take Control (định khung deal) cho enterprise B2B. Trigger phrases: "Challenger Sale", "Challenger framework", "teach tailor take control", "Challenger script", "insight selling", "Challenger sales coaching", "commercial insight", "Challenger pitch", "script Challenger B2B", "approach Challenger". Output là Markdown script + Slide deck commercial insight.
---

# Challenger Sales Script (Teach-Tailor-Take Control)

## Mục Tiêu
Trang bị AE approach Challenger để dạy KH insight họ chưa biết (commercial teaching) → reframe pain → định khung deal — đặc biệt hiệu quả khi KH skeptical hoặc đang dùng đối thủ.

## Khi Nào Dùng
- KH "tự tin biết hết", không thấy pain mới
- Đối thủ đã thống trị mind-share KH
- Sản phẩm có insight độc đáo về thị trường
- C-level deal cần thought leadership
- KH đòi compare feature checklist (cạm bẫy)

## Bước 1: T — Teach (Commercial Insight)
Cấu trúc 5 phần Pitch Teach 7 phút:

**A. Warmer (1 phút)**: chia sẻ insight chung "3 xu hướng đang thay đổi ngành anh"

**B. Reframe (1.5 phút)**: lật ngược niềm tin phổ biến
"Hầu hết tin rằng X. Thật ra X đang tốn các anh $Y mà không biết."

**C. Rational Drowning (1.5 phút)**: số liệu tàn nhẫn
"Nghiên cứu 200 công ty cùng size cho thấy 70% mất 15% revenue do <vấn đề mới>."

**D. Emotional Impact (1 phút)**: cá nhân hoá pain
"Em đoán team anh đang gặp <triệu chứng>, đúng không?"

**E. New Way (2 phút)**: cách tiếp cận mới (không phải sản phẩm)
"Cách giải quyết đúng là <approach>, không phải <approach cũ>."

## Bước 2: Ta — Tailor
Personalize Teach theo:
- Industry (FMCG vs SaaS vs Manufacturing)
- Role (CFO care cost, CMO care growth, COO care efficiency)
- Stage growth (startup vs scale vs enterprise)
- Recent event (M&A, funding, restructure)

KHÔNG dùng generic deck — phải có ít nhất 3 customization.

## Bước 3: Tc — Take Control
- Đặt câu hỏi "khó chịu": "Anh có sẵn sàng đầu tư để fix nó năm nay không?"
- Push back giá: "Nếu giá là rào cản duy nhất, em không gọi lại. Có rào cản nào nữa không?"
- Định khung competitive: "Đối thủ A giải pháp tốt cho <use case khác>. Nhưng nếu anh care về <X>, anh phải compare trên tiêu chí đúng."
- Lead với deadline: "Em đề xuất quyết trong 2 tuần để go-live Q3."

Không phải bullying — là confident và biết KH cần gì hơn họ.

## Bước 4: 5 Profile Sales — Tại sao Challenger thắng
Theo Adamson:
- Hard Worker (20%) — đạt 9% high performance
- Lone Wolf (15%) — 25%
- Relationship Builder (18%) — 7%
- Reactive Problem Solver (20%) — 14%
- **Challenger (27%) — 39%** (complex deal đạt 54%)

Challenger thắng vì dám teach + push back.

## Bước 5: Commercial Insight Pitch Deck (10 slide)
1. Title — pain provocation
2. Industry shift (data)
3. Common belief (đa số tin gì)
4. Why it's wrong (số chứng minh)
5. Cost of doing nothing
6. New way of thinking
7. Mental model cụ thể
8. Implementation principle
9. Where our solution fits (chỉ slide 9!)
10. Next step

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- WebFetch/WebSearch: pull industry data làm insight
- Salesforce MCP: log insight nào KH react với
- Gong MCP: phân tích AE đang teach hay pitch feature
- Slide MCP: tạo deck Commercial Insight

**Fallback API:**
```python
# Tự động tạo insight từ industry data
import requests
report = requests.get(f"https://api.statista.com/statistics/{topic}",
    headers={"X-Api-Key": KEY}).json()
insight = generate_insight(report)  # LLM
# Output: "70% CFOs thừa nhận chi phí Q4 vượt 15% budget vì X"
```

## Bước 7: Output Format
- **File 1**: `challenger_pitch.md` — script Teach 7 phút
- **File 2**: `commercial_insight_deck.pptx` — 10 slide
- **File 3**: `challenger_objection.md` — push-back script khi KH skeptical
- **File 4**: `challenger_industry_data.xlsx` — data point làm insight
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Insight có data thật (không bịa)
- [ ] Reframe lật ngược belief phổ biến
- [ ] Tailor ít nhất 3 customization
- [ ] Solution chỉ xuất hiện slide 9/10
- [ ] AE dám push back giá / timeline
- [ ] Test với top 3 AE trước rollout
