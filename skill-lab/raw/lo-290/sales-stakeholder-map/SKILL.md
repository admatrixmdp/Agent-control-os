---
name: sales-stakeholder-map
description: |
  Map stakeholder enterprise deal — phân loại Champion/Supporter/Blocker, mức ảnh hưởng và plan engage từng người. Trigger phrases: "stakeholder map", "map người ra quyết định", "buying committee map", "ai là champion", "ai chặn deal", "stakeholder analysis", "phân tích người ảnh hưởng deal", "power map enterprise", "decision maker map", "vẽ sơ đồ stakeholder". Output là PPT power map + Excel stakeholder tracker.
---

# Stakeholder & Power Map (Enterprise Deal)

## Mục Tiêu
Tăng win rate enterprise deal bằng cách map toàn bộ buying committee 8-15 người, xác định Champion thật và Blocker tiềm ẩn để có chiến lược engage khác biệt từng nhóm.

## Khi Nào Dùng
- Deal enterprise có nhiều BU
- Deal >$100K mất >3 tháng cycle
- Stuck do "chưa qua được pháp lý/tài chính"
- Champion leave công ty
- Trước negotiation final

## Bước 1: Identify Buying Committee
8 role chuẩn enterprise:
- **Economic Buyer (EB)**: ký, kiểm soát budget
- **Champion**: ủng hộ nội bộ, bán hộ
- **Decision Maker (DM)**: chính thức ra quyết định
- **Technical Buyer**: review tech/security
- **User Buyer**: dùng hằng ngày
- **Coach**: feed info nội bộ cho mình
- **Influencer**: lobby cho mình ngoài committee
- **Blocker**: kháng cự active

Mục tiêu: pin tên người vào mỗi role.

## Bước 2: Phân tích 4 Yếu tố mỗi Stakeholder

**A. Power (1-5)**: ảnh hưởng đến quyết định
**B. Interest (1-5)**: mức quan tâm cá nhân với giải pháp
**C. Sentiment**: Champion (+2) / Supporter (+1) / Neutral (0) / Skeptic (-1) / Blocker (-2)
**D. Relationship**: Strong / Moderate / Weak / None — quan hệ AE-stakeholder

Vẽ 2x2 matrix Power × Interest, dán tên vào.

## Bước 3: Engagement Plan Theo Nhóm

**High Power + High Interest + Champion**: lock in, gặp 2 tuần/lần, share roadmap private
**High Power + Low Interest**: tạo interest qua peer reference, executive briefing
**High Power + Negative**: tách Blocker khỏi quyết định, win neutral first
**Low Power + High Interest**: convert thành Coach feed info
**Low Power + Low Interest**: monitor, không invest

Mỗi stakeholder: who-when-what-channel.

## Bước 4: Coaching Champion
Champion thật phải có 3 thứ:
- **Power**: ảnh hưởng nội bộ thật (không chỉ tên to)
- **Pain**: bị tổn thương nếu không có solution
- **Plan**: có kế hoạch giúp deal close (sẵn sàng map nội bộ)

Nếu thiếu 1 → chỉ là Coach, không phải Champion. Phải tìm Champion thật.

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- LinkedIn MCP: org chart, mutual connection, recent move
- Salesforce/HubSpot MCP: contact role, activity history
- Gong MCP: ai phát biểu nhiều trong call
- WebFetch: cá nhân stakeholder qua blog/twitter

**Fallback API:**
```python
# LinkedIn pull team
import requests
people = requests.get("https://api.linkedin.com/v2/peopleSearch",
    params={"companyId": comp_id}, 
    headers={"Authorization": f"Bearer {token}"}).json()
for p in people:
    p["mutual"] = check_mutual_connections(p["id"])
```

## Bước 6: Output Format
- **File 1**: `stakeholder_map_<deal>.pptx` — 1 slide power map 2x2 + 1 slide engagement plan
- **File 2**: `stakeholder_tracker.xlsx` — Name / Title / Role / Power / Interest / Sentiment / Last touch / Next action / Owner
- **File 3**: `champion_coaching.md` — playbook coach Champion bán hộ nội bộ
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ 8 role được pin tên thật
- [ ] Champion verify đủ Power + Pain + Plan
- [ ] Blocker có chiến lược tách hoặc convert
- [ ] Engagement plan có owner + timeline
- [ ] Review weekly trong deal stuck
- [ ] Cập nhật khi có stakeholder mới
