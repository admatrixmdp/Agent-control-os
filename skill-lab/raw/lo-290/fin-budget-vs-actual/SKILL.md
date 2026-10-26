---
name: fin-budget-vs-actual
description: |
  Lập báo cáo Budget vs Actual có variance analysis chi tiết theo phòng ban/SP/kênh,
  tự động giải thích nguyên nhân lệch >10%. Trigger phrases: "budget vs actual",
  "BvA report", "phân tích variance", "chênh lệch ngân sách", "báo cáo ngân sách",
  "actual vs forecast", "lệch ngân sách", "kế hoạch thực hiện", "variance analysis",
  "phân tích chênh lệch". Output là Excel BvA + HTML dashboard có drill-down.
---

# Báo Cáo Budget vs Actual + Variance Analysis

## Mục Tiêu
Biến báo cáo BvA từ "bảng số khô" thành "câu chuyện" - tự động flag chênh lệch lớn,
gợi ý nguyên nhân, và đưa hành động khắc phục cho từng owner. Giúp CEO đọc 5 phút hiểu hết.

## Khi Nào Dùng
- Đầu mỗi tháng review tháng trước
- Quý đóng đến đâu, review BvA YTD đến đó
- Trước họp HĐQT/đại hội cổ đông
- Khi 1 phòng ban liên tục lệch budget, cần root-cause

## Bước 1: Thu Thập Budget & Actual
**Budget:**
- File ngân sách đầu năm (annual budget) phân bổ theo tháng
- Phân theo dimension: Phòng ban / Sản phẩm / Kênh bán / Khu vực

**Actual:**
- Trial balance kỳ báo cáo từ phần mềm kế toán
- Mapping COA → khoản mục budget tương ứng

Đảm bảo cùng "ngôn ngữ" - nếu budget gộp "Marketing", actual cũng phải gộp tương ứng (không để actual chi tiết hơn rồi lệch).

## Bước 2: Tính Variance & Phân Loại
Mỗi dòng tính:
- **Variance abs** = Actual - Budget
- **Variance %** = (Actual - Budget) / Budget
- **Phân loại:** Favorable (F) nếu actual có lợi (DT cao hơn / CP thấp hơn), Unfavorable (U) nếu ngược lại

Threshold flag:
- |Variance %| < 5%: Bình thường (xanh)
- 5-10%: Theo dõi (vàng)
- 10-20%: Cảnh báo (cam)
- >20%: Khẩn cấp (đỏ) → bắt buộc commentary

## Bước 3: Variance Commentary Tự Động
Với mỗi dòng đỏ/cam, tự động sinh giải thích dựa trên rule:

```
IF khoản mục = "Doanh thu kênh Shopee" AND variance < -15%
THEN gợi ý: "Doanh thu Shopee thấp hơn budget X tỷ (-Y%). Cần check:
  1) Có chiến dịch lớn nào của đối thủ không?
  2) Có sản phẩm chủ lực hết hàng không?
  3) Có thay đổi thuật toán/phí sàn không?"
```

Yêu cầu owner phòng ban điền commentary thật trong 48h.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Pull actual từ sheet kế toán, push variance về sheet BvA
- Gmail MCP: Auto-gửi owner phòng ban yêu cầu commentary nếu lệch >10%
- Google Calendar MCP: Đặt meeting "BvA Review" với CFO sau khi report ready
- WebSearch: Benchmark variance ngành (ví dụ: Marketing chi 8-12% doanh thu)

**Fallback bằng API:**
```python
# Gọi MISA/FAST API lấy trial balance kỳ
import requests
r = requests.post(
    "https://api.misa.vn/sme/v1/reports/trial-balance",
    json={"from": "2026-05-01", "to": "2026-05-31"},
    headers={"Authorization": f"Bearer {TOKEN}"}
)
tb = r.json()["data"]
# Map COA → budget category dùng dict mapping
```

## Bước 5: Output Format
1. **Excel BvA** (`BvA_T05_2026.xlsx`): 4 sheet - Summary, Revenue detail, OpEx detail, Commentary. Conditional formatting theo threshold.
2. **HTML dashboard** (`bva_dashboard.html`): Bullet chart Budget vs Actual cho top 10 khoản mục, waterfall lý do lệch lợi nhuận, table commentary với filter theo phòng ban.
3. **PDF executive memo** (`bva_memo_T05.pdf`): 2 trang, top 5 win + top 5 issue + đề xuất.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/bva/`

## Checklist Trước Khi Giao
- [ ] Budget và actual cùng kỳ, cùng đơn vị (VND/USD)
- [ ] Mapping COA → budget category đã verify
- [ ] Tất cả dòng đỏ đều có commentary
- [ ] Owner mỗi dòng đã rõ ràng
- [ ] Có YTD ngoài Period đơn lẻ
- [ ] Đã so cùng kỳ năm trước (YoY)
