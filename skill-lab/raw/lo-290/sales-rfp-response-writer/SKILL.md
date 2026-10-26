---
name: sales-rfp-response-writer
description: |
  Trả lời RFP/RFI có cấu trúc, dùng template thư viện câu trả lời + cá nhân hoá tab differentiator. Trigger phrases: "trả lời RFP", "viết RFP response", "RFI response", "RFP template", "soạn proposal RFP", "RFP answer library", "bid response", "tender response", "viết hồ sơ thầu", "RFP B2B". Output là Docx response + Excel question matrix.
---

# RFP/RFI Response Writer

## Mục Tiêu
Trả lời RFP 100-500 câu hỏi trong 5-7 ngày bằng cách reuse thư viện câu trả lời + cá nhân hoá 20% — đạt shortlist rate >50%.

## Khi Nào Dùng
- KH gửi RFP/RFI/RFQ
- Government tender
- Re-bid renewal có competitive
- Enterprise procurement quy trình
- Partnership tender

## Bước 1: Go/No-go Decision (Day 0)
Trước khi viết, đánh giá:
- Budget rõ ràng?
- Champion nội bộ KH?
- Match ICP?
- Win probability >30%?
- Resource available 5-7 ngày?

Nếu fail 2/5 → No-bid (đỡ tốn time team).

## Bước 2: Cấu trúc Response Document
Phần chuẩn:
- **Cover letter** — 1 trang
- **Executive summary** — 2 trang, hook differentiator
- **Company overview** — 1 trang
- **Solution architecture** — 5-10 trang
- **Implementation plan** — 2-3 trang
- **Pricing** — 1-2 trang
- **References** — 2-3 case study + reference
- **Appendix** — security, compliance, SLA

## Bước 3: RFP Answer Library
Build library 200+ câu trả lời chuẩn:
- Sort theo category (Security/Architecture/Pricing/SLA)
- Mỗi câu có:
  - Question variant (3-5 cách hỏi)
  - Standard answer (250 từ)
  - Differentiator angle
  - Updated date + owner

Khi RFP đến: match 70-80% câu, viết mới 20-30%.

## Bước 4: Personalization Layer
20% PHẢI personalize:
- Reference KH cùng industry
- Specific use case match
- Local presence (geo)
- Differentiator vs competitor named in RFP

## Bước 5: Win Theme + Discriminator
Mỗi response có 3-5 win theme:
- Theme = lý do nên chọn mình
- Lồng vào Executive Summary + recurring trong response
- Vd: "Faster time-to-value", "Lowest TCO", "Vietnam-based support"

Discriminator = đối thủ không có (vd local server, ISO cert).

## Bước 6: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Loopio/Responsive (RFP tool) MCP: AI auto-fill từ library
- Drive/SharePoint MCP: collaborative editing
- Slack MCP: review request từ SME
- WebFetch: pull industry benchmark
- DocuSign MCP: sign response

**Fallback API:**
```python
# Auto-match answer library to RFP question
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

def match_answers(rfp_questions, library):
    matches = []
    for q in rfp_questions:
        q_emb = model.encode(q)
        scores = [(ans, cosine(q_emb, model.encode(ans["question"])))
                  for ans in library]
        matches.append(sorted(scores, key=lambda x: -x[1])[:3])
    return matches
```

## Bước 7: Output Format
- **File 1**: `rfp_response_<customer>.docx` — full doc 30-100 trang
- **File 2**: `rfp_answer_library.xlsx` — 200+ Q&A reusable
- **File 3**: `rfp_question_matrix.xlsx` — Q × Owner × Status
- **File 4**: `rfp_win_themes.md` — 5 theme + script
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Go/No-go quyết định Day 0
- [ ] 70-80% answer từ library
- [ ] 20-30% personalize
- [ ] Win theme nhúng xuyên suốt
- [ ] Pricing cross-check Finance
- [ ] Legal review trước nộp
- [ ] Submit trước deadline 24h (không sát nút)
