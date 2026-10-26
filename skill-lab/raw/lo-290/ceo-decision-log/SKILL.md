---
name: ceo-decision-log
description: |
  Ghi log mọi quyết định CEO theo cấu trúc context-options-decision-rationale-owner-revisit — tạo memory tổ chức, audit trail, học từ quyết định sai. Lưu trong Notion database.
  Kích hoạt khi người dùng nói: "decision log", "log quyết định", "ghi quyết định CEO", "decision journal", "nhật ký quyết định", "lưu quyết định", "decision tracking", "audit quyết định".
  Output là Markdown log + Notion database row.
---

# CEO Decision Log — Nhật Ký Quyết Định CEO

## Mục Tiêu
CEO ra 50-100 quyết định mỗi tháng. Không log thì 6 tháng sau không nhớ "tại sao quyết định X" và không học được từ sai lầm. Decision log là tài sản tổ chức — vừa audit, vừa coaching, vừa onboarding leader mới.

## Khi Nào Dùng
- Quyết định chiến lược (giá, thị trường, hire C-level)
- Quyết định tài chính > 100 triệu
- Quyết định người (sa thải, promote, giáng)
- Quyết định reversible vs irreversible (Bezos one-way door)
- Quyết định gây tranh cãi trong leadership

## Bước 1: Khung 7 Trường Bắt Buộc
1. **Title**: 1 câu tóm tắt quyết định
2. **Date**: ngày ra quyết định
3. **Context**: vấn đề/cơ hội + bối cảnh (200 từ)
4. **Options Considered**: ≥ 2 lựa chọn + pros/cons
5. **Decision**: chốt phương án nào
6. **Rationale**: tại sao chọn (200 từ)
7. **Owner + Revisit Date**: ai thực thi + khi nào review

Optional: stakeholders consulted, expected outcome, success metric.

## Bước 2: Phân Loại 4 Type
- **Type 1 (irreversible, high-stakes)**: cần slow, nhiều input
- **Type 2 (reversible)**: fast, không cần consensus
- **Type 3 (delegate)**: chuyển owner khác
- **Type 4 (don't decide)**: chờ thêm info

Mỗi log đánh dấu type → tự nhận ra mình có over-think type 2 không.

## Bước 3: Review Định Kỳ
- Hàng tháng: review 5 quyết định cũ nhất → outcome đúng/sai
- Hàng quý: pattern phân tích (CEO hay sai loại nào?)
- Hàng năm: top 10 quyết định ảnh hưởng nhất

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Notion MCP: database "CEO Decisions" với property type, status, owner, revisit
- Calendar MCP: tạo event review tại ngày revisit
- Slack MCP: alert khi đến ngày revisit
- Gmail MCP: archive email liên quan vào folder Decision
- Linear MCP: link decision với epic/project nếu cần thực thi

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Notion database create page
import requests, datetime
data = {
  "parent": {"database_id": db_id},
  "properties": {
    "Title": {"title": [{"text": {"content": title}}]},
    "Type": {"select": {"name": "Type 1"}},
    "Decision Date": {"date": {"start": str(datetime.date.today())}},
    "Revisit Date": {"date": {"start": "2026-09-01"}},
    "Owner": {"people": [{"id": owner_uuid}]}
  }
}
requests.post("https://api.notion.com/v1/pages", json=data, headers=headers)
```

## Bước 5: Output Format
- Markdown log mỗi quyết định riêng file
- Notion database row tự động đồng bộ
- Excel export quý để review pattern
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/decisions/YYYY-MM-DD-[title].md`

## Checklist Trước Khi Giao
- [ ] Đủ 7 trường bắt buộc
- [ ] Có ≥ 2 options đã consider
- [ ] Rationale ≥ 100 từ (không "vì tôi nghĩ vậy")
- [ ] Phân loại type rõ ràng
- [ ] Revisit date đặt sẵn trên calendar
- [ ] Owner biết họ đang được giao
