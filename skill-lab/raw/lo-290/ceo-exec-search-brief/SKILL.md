---
name: ceo-exec-search-brief
description: |
  Brief tìm CXO gửi headhunter / executive search firm — mô tả role, success criteria, target company, comp package, timeline. Format giúp headhunter source chất lượng cao.
  Kích hoạt khi người dùng nói: "exec search brief", "tuyển CXO", "brief headhunter", "tuyển CEO/CTO/CFO", "executive search", "C-level brief", "tuyển lãnh đạo cấp cao", "search firm brief".
  Output là PDF brief + Markdown.
---

# CEO Exec Search Brief — Brief Tìm CXO Gửi Headhunter

## Mục Tiêu
Tuyển CXO mất 4-9 tháng, mỗi mis-hire = $500k-2M loss. Brief tốt giúp headhunter source 5x faster + 3x quality. Skill này tạo brief chuẩn McKinsey/Korn Ferry trong 2h.

## Khi Nào Dùng
- Tìm thay thế CXO rời công ty
- Mở vị trí CXO mới (CTO, CFO, CMO, CPO, COO)
- Hire VP cấp cao báo cáo CEO
- Sau Series B+ cần executive bench
- Replace founder role với external CEO

## Bước 1: Định Nghĩa Role Cốt Lõi
- Title chính thức + report to
- Top 3 outcomes 12 tháng đầu phải đạt
- Top 5 responsibilities daily
- Scope: P&L size, team size, geo
- Why role tồn tại bây giờ (story)

## Bước 2: Ứng Viên Lý Tưởng
**Must-have (5-7)**: kinh nghiệm chính, certification, scale từng quản lý
**Nice-to-have (3-5)**: industry, network, language
**Red flag (3-5)**: lý do reject ngay (job hopping, brand mismatch)

Target companies (10-15 công ty headhunter nên approach):
- 3-5 đối thủ trực tiếp
- 3-5 công ty tương tự ngành khác
- 2-3 fast-growth startup
- 2-3 corporate enterprise

## Bước 3: Comp Package + Timeline
- Base salary range
- Annual bonus % target
- Equity % range
- Signing bonus (relocation, sign-on)
- Benefits đặc biệt
- Timeline:
  - Search kick-off
  - Long list (week 4)
  - Shortlist 5-6 (week 8)
  - Final 2-3 cho CEO (week 12)
  - Offer (week 14-16)
- Search fee structure (% first year comp, thường 30-33%)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: target company list, comp benchmark
- LinkedIn (qua WebFetch): scan profile target
- Gmail MCP: gửi brief cho 3-5 search firm
- Notion MCP: candidate pipeline tracker
- Calendar MCP: schedule intro call với search firm

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Comp benchmark từ levels.fyi tương đương VN
benchmarks = {
  'CFO_VN_50M_USD_revenue': {'base': 200_000_000, 'bonus_pct': 50, 'equity_pct': 1.5},
  'CTO_seriesA': {'base': 180_000_000, 'bonus_pct': 30, 'equity_pct': 2.0}
}
# Adjust theo stage + size
```

## Bước 5: Output Format
- PDF brief 6-10 trang gửi search firm:
  - Company overview + stage
  - Role mandate
  - Ideal candidate profile
  - Target company list
  - Comp package
  - Process & timeline
- Markdown version để revise quick
- Cover letter cá nhân CEO gửi 3 search firm chọn pitch
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/exec-brief-[role]-YYYY.pdf`

## Checklist Trước Khi Giao
- [ ] Top 3 outcomes 12 tháng rất cụ thể
- [ ] Must-have ≤ 7 (không quá tham)
- [ ] Target company list ≥ 10
- [ ] Comp package có range realistic
- [ ] Timeline 14-16 tuần
- [ ] Board signed off comp authority
