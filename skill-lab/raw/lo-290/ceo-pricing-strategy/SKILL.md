---
name: ceo-pricing-strategy
description: |
  Tư vấn chiến lược giá cho sản phẩm/dịch vụ — phân tích 3 mô hình (value-based, cost-plus, competitive), tính giá tối ưu theo elasticity, gợi ý gói (good/better/best) và psychological pricing.
  Kích hoạt khi người dùng nói: "chiến lược giá", "pricing strategy", "đặt giá sản phẩm", "tính giá bán", "tối ưu giá", "value-based pricing", "đóng gói giá", "psychological pricing", "định giá".
  Output là HTML phân tích + Excel model.
---

# CEO Pricing Strategy — Tư Vấn Chiến Lược Giá

## Mục Tiêu
Giá là đòn bẩy lợi nhuận mạnh nhất nhưng ít CEO dành thời gian. 1% tăng giá → 10% tăng lợi nhuận (nghiên cứu McKinsey). Skill này giúp CEO ra quyết định pricing có data thay vì cảm tính.

## Khi Nào Dùng
- Trước launch sản phẩm mới
- Khi gross margin thấp dưới benchmark
- Khi đối thủ thay đổi giá
- Annual pricing review
- Sau khi raise vốn (cần optimize unit economics)

## Bước 1: Thu Thập Dữ Liệu
- Cost: COGS, fixed cost phân bổ
- Customer: WTP (willingness to pay) qua survey/test
- Đối thủ: giá 5-10 đối thủ chính
- Lịch sử: doanh số theo giá đã thử
- Elasticity nếu có (hoặc estimate)

## Bước 2: So Sánh 3 Mô Hình
**Cost-plus**: Cost × (1 + markup %) — đơn giản, dễ giải thích nhưng bỏ qua giá trị
**Competitive**: ±5-15% so với median đối thủ — an toàn nhưng dễ race-to-bottom
**Value-based**: Dựa trên ROI khách hàng — margin cao nhất, đòi hỏi quantify giá trị

Khuyến nghị chính: value-based cho sản phẩm có ROI rõ; cost-plus cho commodity; competitive cho thị trường đỏ.

## Bước 3: Đóng Gói Good/Better/Best
- 3 tier với feature ladder rõ ràng
- Giá tier giữa = "anchor" (60-70% khách chọn)
- Tier cao tạo decoy (làm tier giữa hợp lý)
- Áp dụng charm pricing (199 thay 200)
- Annual discount 15-20% để tăng LTV

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: lấy giá đối thủ public
- WebFetch: scrape pricing page đối thủ chính
- Google Drive MCP: pull lịch sử doanh số theo giá từ Sheets
- Notion MCP: lưu pricing decision log
- HubSpot MCP: pull data conversion rate theo gói

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tính giá tối ưu theo elasticity
import numpy as np
prices = np.linspace(100, 500, 41)
# Demand model: Q = a - b*P
a, b = 1000, 1.5
revenue = prices * (a - b * prices)
optimal_price = prices[np.argmax(revenue)]
print(f"Optimal: {optimal_price}, Revenue: {max(revenue):.0f}")
```

## Bước 5: Output Format
- HTML report 4-6 trang:
  - Trang 1: Recommended pricing + lý do
  - Trang 2: So sánh 3 mô hình
  - Trang 3: Đóng gói G/B/B
  - Trang 4-5: Sensitivity analysis
  - Trang 6: Roll-out plan
- Excel model tính tự động khi đổi cost/giá
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/pricing-[product]-YYYY.xlsx`

## Checklist Trước Khi Giao
- [ ] Có 3 mô hình so sánh kèm pros/cons
- [ ] Đóng gói G/B/B với feature ladder
- [ ] Có sensitivity table (cost/elasticity)
- [ ] So sánh với 5+ đối thủ
- [ ] Khuyến nghị có lý do số rõ ràng
- [ ] Roll-out plan (grandfather giá cũ?)
