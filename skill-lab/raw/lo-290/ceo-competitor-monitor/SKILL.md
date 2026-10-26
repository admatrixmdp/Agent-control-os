---
name: ceo-competitor-monitor
description: |
  Theo dõi đối thủ tự động hàng tuần dùng WebSearch — quét tin tuyển dụng, giá sản phẩm, ra mắt tính năng, funding, lãnh đạo mới, PR. Tổng hợp thành báo cáo 1 trang gửi CEO sáng Thứ Hai.
  Kích hoạt khi người dùng nói: "theo dõi đối thủ", "competitor monitor", "spy đối thủ", "competitive intelligence", "đối thủ làm gì tuần này", "competitor watch", "tracking đối thủ", "battlecard tuần".
  Output là HTML/PDF báo cáo tuần + Slack alert.
---

# CEO Competitor Monitor — Radar Đối Thủ Tự Động

## Mục Tiêu
CEO biết đối thủ làm gì tuần này trong 5 phút thay vì tốn 1 ngày Google. Tự động phát hiện thay đổi giá, ra mắt sản phẩm, hire executive, funding, scandal.

## Khi Nào Dùng
- Hàng tuần (sáng Thứ Hai)
- Trước họp chiến lược
- Khi nghe tin đối thủ raise round
- Khi đối thủ thay CEO
- Trước launch sản phẩm mới của mình

## Bước 1: Thiết Lập Watchlist
- Danh sách 5-15 đối thủ trực tiếp + gián tiếp
- Mỗi đối thủ có: tên, website, LinkedIn, page FB, careers page
- 5 chiều cần theo dõi:
  1. Giá (pricing page)
  2. Tính năng/sản phẩm mới
  3. Tuyển dụng (career page → headcount/role mới)
  4. Funding (Crunchbase, TechCrunch, báo)
  5. PR/scandal/lãnh đạo mới

## Bước 2: Quét Tự Động
- WebSearch query cho mỗi đối thủ × 5 chiều
- WebFetch trang pricing để diff với tuần trước
- Crawl careers page đếm số job mới
- Search "[competitor] funding 2026", "[competitor] CEO"

## Bước 3: So Sánh Với Snapshot Tuần Trước
- Load snapshot tuần trước (JSON)
- Diff:
  - Giá có thay đổi → cảnh báo
  - Job mới mở (đặc biệt role chiến lược) → cảnh báo
  - Tính năng mới → cảnh báo
  - Funding/news → cảnh báo
- Chỉ report DELTA, không lặp lại đã biết

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tìm tin tức 7 ngày qua từng đối thủ
- WebFetch: lấy nội dung pricing page + careers
- Slack MCP: post alert lên #competitive-intel
- Notion MCP: lưu database snapshot tuần
- Gmail MCP: gửi email tổng hợp cho CEO sáng T2

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# So sánh snapshot pricing
import requests, json, difflib
old = json.load(open('snapshot_week_prev.json'))
new = {}
for comp in competitors:
    html = requests.get(comp['pricing_url']).text
    new[comp['name']] = extract_prices(html)
diff = {k: (old.get(k), new[k]) for k in new if old.get(k) != new[k]}
```

## Bước 5: Output Format
- HTML báo cáo 1 trang:
  - Top: Alert đỏ (thay đổi quan trọng)
  - Giữa: bảng 5 đối thủ × 5 chiều, có icon thay đổi
  - Dưới: insight + đề xuất phản ứng
- File `competitor-week-WW-YYYY.pdf`
- Slack message ngắn 200 từ post lên #leadership
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Watchlist đủ 5-15 đối thủ
- [ ] Quét đủ 5 chiều
- [ ] Chỉ report delta, không lặp
- [ ] Mỗi alert có recommended action
- [ ] Có nguồn URL cho mỗi tin
- [ ] Snapshot tuần lưu lại để tuần sau diff
