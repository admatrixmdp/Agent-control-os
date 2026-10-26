---
name: sales-contract-redline
description: |
  Đọc & redline hợp đồng KH/đối tác, đánh dấu red flag (liability, IP, termination, jurisdiction) và đề xuất phản hồi cho legal. Trigger phrases: "redline hợp đồng", "review hợp đồng", "check red flag contract", "đọc hợp đồng B2B", "đánh giá hợp đồng KH", "tìm rủi ro hợp đồng", "negotiate contract", "phân tích MSA", "review SOW", "kiểm tra điều khoản hợp đồng". Output là Docx có comment + Markdown redline summary.
---

# Contract Redline & Red Flag Detector

## Mục Tiêu
Hỗ trợ Sales/Legal đọc hợp đồng KH gửi (MSA/SOW/Order Form) trong 30 phút, đánh dấu 10-15 điều khoản rủi ro phổ biến và đề xuất counter-language sẵn.

## Khi Nào Dùng
- KH gửi paper-pa-paper template của họ
- Enterprise redline standard MSA của mình
- Renewal có điều khoản mới
- Partnership contract với đối tác kênh
- Trước khi escalate cho external counsel

## Bước 1: Đọc tổng quan + Xác định loại contract
- MSA (Master Services Agreement) — khung dài hạn
- SOW (Statement of Work) — scope dự án
- Order Form — đơn hàng đính kèm MSA
- DPA (Data Processing Agreement) — GDPR
- NDA — secrecy

Mỗi loại có 10-15 điều khoản chuẩn cần check.

## Bước 2: Quét 12 Red Flag Phổ Biến

**A. Liability**:
1. Unlimited liability — REJECT, counter "cap at 12 months fees"
2. Consequential damages bao gồm — counter "exclude"

**B. IP & Confidentiality**:
3. IP của mình bị chuyển sang KH — REJECT
4. NDA term >5 năm — counter "3 years"
5. KH được dùng tên + logo không cần consent — counter "with prior written"

**C. Termination**:
6. KH terminate convenience 0 notice — counter "30 days notice"
7. Auto-renewal không có opt-out — counter "30 days before expiry"

**D. Payment**:
8. Net 90+ — counter "Net 30"
9. Withhold payment nếu disputed → giữ toàn bộ — counter "only disputed portion"

**E. Compliance**:
10. SLA 99.99% với penalty 10x fees — counter "credit only, 1x"
11. Indemnification 1 chiều — counter "mutual"
12. Jurisdiction nước KH (high-risk) — counter "Singapore arbitration"

## Bước 3: Đề xuất Counter-language
Mỗi red flag → propose:
- Lý do reject/modify (1 câu business risk)
- Counter language exact text
- Fallback nếu KH không chịu (mức compromise)
- Escalation trigger (gửi GC/CFO)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Drive/SharePoint MCP: pull template MSA của công ty để so sánh
- DocuSign MCP: track version history
- Slack MCP: ping legal/CFO khi red flag major
- WebFetch: tìm benchmark điều khoản chuẩn ngành

**Fallback API:**
```python
# Google Docs API thêm comment vào contract
from googleapiclient.discovery import build
docs = build('docs', 'v1', credentials=creds)
for rf in red_flags:
    docs.documents().batchUpdate(documentId=doc_id, body={
        "requests": [{"createComment": {"location": {"index": rf["pos"]},
                      "comment": rf["counter_language"]}}]}).execute()
```

## Bước 5: Output Format
- **File 1**: `contract_<KH>_redlined.docx` — bản KH gửi + track changes + comment
- **File 2**: `redline_summary_<KH>.md` — bảng 12 red flag: Issue / Risk / Counter / Fallback / Escalation
- **File 3**: `counter_proposal_email.md` — email gửi legal KH kèm version mới
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đã check đủ 12 red flag phổ biến
- [ ] Counter-language exact, không "TBD"
- [ ] Có fallback compromise cho mỗi điểm
- [ ] Escalation rule rõ (GC/CFO/CEO khi nào)
- [ ] Track changes bật, không edit thẳng
- [ ] Legal review trước khi gửi KH
