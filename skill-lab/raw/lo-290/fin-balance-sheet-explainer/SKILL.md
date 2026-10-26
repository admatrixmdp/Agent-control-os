---
name: fin-balance-sheet-explainer
description: |
  Giải thích Báo Cáo Tài Chính (BS, P&L, CF) cho CEO/Founder không có nền tài chính - dịch số
  thành insight kinh doanh dễ hiểu. Trigger phrases: "giải thích BCTC", "đọc bảng cân đối",
  "hiểu báo cáo tài chính", "BS P&L CF cho CEO", "phân tích BCTC", "ratio phân tích",
  "ROA ROE", "current ratio", "giải thích số liệu kế toán", "explainer financial statement".
  Output là HTML interactive explainer + PDF executive memo.
---

# Giải Thích BCTC Cho CEO Không Có Nền Tài Chính

## Mục Tiêu
Biến những "con số khô khan" trên BCTC thành câu chuyện kinh doanh dễ hiểu cho CEO/Founder
(thường có nền kỹ thuật, kinh doanh, không phải kế toán). Mỗi chỉ số được giải thích bằng
ngôn ngữ đời thường + so sánh + đề xuất hành động.

## Khi Nào Dùng
- Sau khi đóng sổ tháng/quý/năm
- CEO/founder mới onboard, cần training BCTC
- Trước họp với nhà đầu tư
- Trước họp HĐQT/ĐHCĐ
- Khi BCTC có biến động lạ cần CFO giải thích

## Bước 1: Tóm Tắt 3 Báo Cáo Bằng 3 Câu
**Bảng Cân Đối Kế Toán (BS):** "Tại ngày X, công ty SỞ HỮU bao nhiêu, NỢ bao nhiêu, VỐN CHỦ bao nhiêu."

**Báo Cáo Kết Quả Kinh Doanh (P&L):** "Trong kỳ Y, công ty BÁN được bao nhiêu, TIÊU bao nhiêu, LÃI/LỖ bao nhiêu."

**Báo Cáo Lưu Chuyển Tiền Tệ (CF):** "Trong kỳ Y, công ty THỰC SỰ thu được bao nhiêu TIỀN, chi bao nhiêu TIỀN, cuối kỳ còn bao nhiêu TIỀN."

→ **Quan trọng nhất**: P&L có thể lãi nhưng CF âm = sắp chết!

## Bước 2: Giải Thích Bằng Ẩn Dụ Đời Thường
**BS = "Cái tủ":**
- Tài sản = Đồ trong tủ (gạo, mì, máy tính)
- Nợ phải trả = Tiền mượn người khác để mua đồ
- Vốn chủ = Tiền túi mình bỏ ra mua đồ
- Phương trình: Tài sản = Nợ + Vốn chủ

**P&L = "Báo cáo bữa ăn":**
- Doanh thu = Tiền cả gia đình kiếm được
- Giá vốn = Tiền mua nguyên liệu
- CP bán hàng = Tiền marketing chợ
- CP QLDN = Tiền lương quản gia
- LN thuần = Tiền còn dư cuối tháng

**CF = "Két sắt":**
- HĐKD = Tiền vào ra từ bán hàng
- HĐĐT = Tiền vào ra từ mua/bán nhà
- HĐTC = Tiền vào ra từ vay/trả nợ

## Bước 3: 10 Chỉ Số Vàng Cho CEO
| Chỉ số | Công thức | Healthy | Ý nghĩa cho CEO |
|--------|-----------|---------|-----------------|
| Current Ratio | TS ngắn hạn / Nợ ngắn hạn | >1.5 | Đủ tiền trả nợ ngắn? |
| Quick Ratio | (TSNH - HTK) / NNH | >1.0 | Trừ hàng tồn còn đủ trả? |
| DSO | AR / DT ngày | <45 ngày | Bao lâu thu được tiền KH? |
| DPO | AP / Giá vốn ngày | 30-60 ngày | Bao lâu trả NCC? |
| Inventory Days | HTK / Giá vốn ngày | <60 | Hàng đọng bao lâu? |
| Gross Margin | LN gộp / DT | Tuỳ ngành | Sản phẩm lãi thực bao nhiêu? |
| Operating Margin | LN HĐKD / DT | >10% | Vận hành có lãi không? |
| Net Margin | LN sau thuế / DT | >5% | Tổng lại lãi bao nhiêu? |
| ROA | LN / Tổng TS | >8% | TS sinh lời thế nào? |
| ROE | LN / Vốn CSH | >15% | Vốn mình bỏ ra sinh lời? |
| Debt/Equity | Tổng nợ / VCSH | <1.5 | Đòn bẩy có quá cao? |

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Pull BCTC kỳ, tính tự động 10 ratio
- Google Drive MCP: Lưu memo phiên bản hàng tháng
- Gmail MCP: Gửi CEO memo 1 trang mỗi đầu tháng
- WebSearch: Benchmark ratio ngành Việt Nam (Vietstock, Cafef)

**Fallback bằng API:**
```python
# Pull data BCTC từ MISA và compare với benchmark ngành
import requests
r = requests.post(
    "https://api.misa.vn/sme/v1/reports/financial-statements",
    json={"period": "2026-05"},
    headers={"Authorization": f"Bearer {TOKEN}"}
)
bs, pl, cf = r.json()["bs"], r.json()["pl"], r.json()["cf"]

# Tính ratios
ratios = {
    "current_ratio": bs["current_assets"] / bs["current_liabilities"],
    "dso": bs["ar"] / (pl["revenue"] / 30),
    "gross_margin": pl["gross_profit"] / pl["revenue"],
    "roe": pl["net_income"] / bs["equity"]
}

# So với industry benchmark từ Cafef
benchmark = requests.get("https://cafef.vn/api/industry-benchmark?sic=5651").json()
for k, v in ratios.items():
    status = "GOOD" if v > benchmark[k] else "BELOW"
    print(f"{k}: {v:.2f} ({status} vs benchmark {benchmark[k]:.2f})")
```

## Bước 5: Output Format
1. **HTML interactive explainer** (`bctc_explainer_T05.html`): Hover từng dòng BCTC hiện popup giải thích, ratio dashboard với gauge xanh-vàng-đỏ.
2. **PDF executive memo** (`ceo_memo_T05.pdf`): 2 trang, top 5 thay đổi quan trọng + 3 câu hỏi CEO cần hỏi CFO.
3. **PPTX 5 slide** (`bctc_5slides.pptx`): Slide cho cuộc họp 15 phút với CEO.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/explainer/`

## Checklist Trước Khi Giao
- [ ] Không dùng jargon kế toán mà không giải thích
- [ ] Mỗi ratio có "so what" - đề xuất hành động
- [ ] Có so sánh: cùng kỳ năm trước + benchmark ngành
- [ ] Highlight 3 thay đổi LỚN NHẤT (biến động >20%)
- [ ] Memo CEO ≤ 2 trang, đọc ≤ 5 phút
- [ ] Có sẵn slide để present nếu CEO yêu cầu deep-dive
