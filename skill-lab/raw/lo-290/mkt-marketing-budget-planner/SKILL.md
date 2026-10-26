---
name: mkt-marketing-budget-planner
description: |
  Plan ngân sách marketing năm cho doanh nghiệp Việt Nam — phân bổ theo kênh, quý, sản phẩm; gắn KPI và ROI mục tiêu. Kích hoạt khi người dùng nói: "plan ngân sách marketing", "marketing budget", "phân bổ chi phí MKT", "budget plan năm", "ngân sách quảng cáo", "chia budget kênh", "MKT budget allocation", "kế hoạch chi phí marketing". Output là Excel budget + dashboard.
---

# Plan Ngân Sách MKT Năm Theo Kênh

## Mục Tiêu
CEO + CMO có 1 file ngân sách duy nhất, phân bổ theo logic (revenue mục tiêu → CAC → CPL → cost per channel), tracking thực chi vs kế hoạch hàng tháng.

## Khi Nào Dùng
- Lập ngân sách năm tới (Q4 năm trước)
- Re-allocation giữa quý
- Sau khi gọi vốn / scale
- Audit chi phí MKT lãng phí
- Trước khi pitch ngân sách lên CEO/board

## Bước 1: Thu Thập Mục Tiêu
Hỏi:
1. Revenue target năm
2. Target customer mới + ARPU
3. CAC target / ngành benchmark
4. Sản phẩm chính
5. Kênh đang/sẽ chạy
6. Ngân sách top-down (CEO cấp) vs bottom-up (team đề xuất)
7. Tỷ lệ % budget MKT trên revenue (5-15% là phổ biến)

## Bước 2: Backward Calculation
Từ revenue → người mua → lead → traffic.
Ví dụ:
- Target 50.000 KH mới
- ARPU 1.5tr → revenue 75 tỷ
- CR lead → customer 20% → cần 250.000 lead
- CR traffic → lead 5% → cần 5tr visit
- CAC target 300k → ngân sách MKT = 15 tỷ (~20% revenue)

## Bước 3: Phân Bổ Theo Kênh
Mỗi kênh có expected CPL + CR:
| Kênh | Spend | CPL | Lead | CR | Customer |
|---|---|---|---|---|---|
| FB Ads | 3 tỷ | 50k | 60.000 | 20% | 12.000 |
| GG Ads | 2 tỷ | 80k | 25.000 | 25% | 6.250 |
| SEO | 1.5 tỷ | 30k | 50.000 | 18% | 9.000 |
| KOL | 1 tỷ | 70k | 14.000 | 25% | 3.500 |
| Email | 200tr | 10k | 20.000 | 30% | 6.000 |

Phân theo quý có hệ số mùa vụ (Q4 đẩy mạnh do BFCM/Tết).

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: budget tracker
- GA4 + Ads MCP: actual data cập nhật hàng tuần
- Notion MCP: dashboard cho leadership
- Slack MCP: alert overspend
- Looker Studio: visualize

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tự động pull actual spend từ Google + Meta Ads
def get_actual_spend(start, end):
    fb = get_fb_spend(start, end)
    gg = get_gg_spend(start, end)
    return {'facebook':fb,'google':gg,'date':end}

# So sánh vs plan
plan = {'facebook':250000000,'google':166000000}  # tháng
actual = get_actual_spend('2026-06-01','2026-06-30')
variance = {k: actual[k]-plan[k] for k in plan}
```

## Bước 5: Output Format
- File `.xlsx` master budget:
  - Sheet 1: Annual plan by channel x quarter
  - Sheet 2: Monthly breakdown
  - Sheet 3: Actual vs Plan tracker
  - Sheet 4: ROI by channel
- Dashboard HTML / Looker Studio
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Backward từ revenue → spend rõ
- [ ] Mỗi kênh có CPL + CR giả định
- [ ] Có yếu tố mùa vụ
- [ ] Có 10-15% buffer test/contingency
- [ ] Tracker actual vs plan hàng tuần
- [ ] Quyền approve overspend rõ
