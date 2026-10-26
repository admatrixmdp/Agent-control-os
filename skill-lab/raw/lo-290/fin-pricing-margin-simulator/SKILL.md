---
name: fin-pricing-margin-simulator
description: |
  Mô phỏng giá bán - biên lợi nhuận theo từng SKU với các kịch bản chiết khấu, chương trình
  khuyến mãi, thay đổi giá đầu vào. Trigger phrases: "mô phỏng giá", "pricing simulation",
  "tính biên lợi nhuận", "margin analysis", "what-if pricing", "tăng giá bao nhiêu",
  "break-even price", "chiết khấu bao nhiêu hợp lý", "price waterfall", "net pricing".
  Output là Excel simulator + HTML interactive widget.
---

# Mô Phỏng Giá - Biên Lợi Nhuận Theo SKU

## Mục Tiêu
Trang bị cho Sales Manager / Pricing Analyst công cụ "what-if" trả lời nhanh: nếu giảm giá 10%
thì lợi nhuận biến động ra sao, đối thủ giảm thì mình hoà vốn ở giá nào, deal lớn nên chiết
khấu tối đa bao nhiêu mà không lỗ.

## Khi Nào Dùng
- Trước khi launch flash sale, mega sale
- Khi sales xin duyệt deal chiết khấu lớn
- Khi giá NVL biến động cần điều chỉnh giá bán
- Đàm phán với khách B2B về volume discount
- Lập price list mới theo quý/năm

## Bước 1: Thu Thập Input Cost Cho Mỗi SKU
**Cost components:**
- Giá vốn sản xuất / mua (COGS)
- Phí sàn TMĐT (Shopee 8-12%, Lazada, Tiki...)
- Phí thanh toán (cổng pay 1.5-3%)
- Phí ship freeship (nếu mình bù)
- Chi phí marketing phân bổ (CPA)
- Phí kho vận, đóng gói
- Phí hoàn trả ước tính (return rate × cost)
- Hoa hồng sales (% revenue)

**Phân loại Fixed vs Variable** rõ ràng để tính break-even đúng.

## Bước 2: Build Margin Waterfall
```
Gross Price          100,000
- Promo discount     -10,000  (-10%)
- Voucher sàn        -5,000   (-5%)
= Net Price          85,000

- Phí sàn 10%        -8,500
- Phí pay 2%         -1,700
- Ship hỗ trợ        -10,000
= Net Revenue        64,800

- COGS               -40,000
= Gross Profit       24,800   (Gross Margin 38%)

- CP Mkt phân bổ     -8,000
- Hoa hồng sales 3%  -1,944
= Contribution Margin 14,856  (CM 22.9%)

- OPEX phân bổ       -6,000
= Operating Profit   8,856    (OP 13.6%)
```

## Bước 3: Sensitivity & Scenario
Tạo bảng độ nhạy 2 chiều:
- Trục X: % chiết khấu (0%, 5%, 10%, 15%, 20%, 25%)
- Trục Y: % tăng volume kỳ vọng (0%, +10%, +30%, +50%, +100%)
- Ô giá trị: Tổng Operating Profit

→ Phát hiện "sweet spot" giảm giá X% tăng vol Y% mới có lợi.

**Break-even price** = mức giá tối thiểu để Gross Margin ≥ 0 sau toàn bộ phí biến đổi.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Input file giá + cost realtime, output kết quả simulator
- WebFetch: Crawl giá đối thủ trên Shopee/Lazada để benchmark
- WebSearch: Tra phí sàn cập nhật (Shopee thường đổi quý/lần)
- Gmail MCP: Gửi recommend pricing cho Sales Director duyệt

**Fallback bằng API:**
```python
# Crawl giá đối thủ qua Shopee Open API
import requests
my_skus = ["áo thun nam", "quần jean nữ"]
for kw in my_skus:
    r = requests.get(
        f"https://shopee.vn/api/v4/search/search_items",
        params={"keyword": kw, "limit": 20, "by": "sales"}
    )
    items = r.json()["items"]
    prices = [i["item_basic"]["price"]/100000 for i in items]
    print(f"{kw}: P25={min(prices)}, P50={sorted(prices)[len(prices)//2]}, P75={max(prices)}")
```

## Bước 5: Output Format
1. **Excel simulator** (`pricing_simulator_2026.xlsx`): Sheet "Input" SKU + cost, "Calculator" tính margin theo waterfall, "Sensitivity" bảng 2D, "Competitor" benchmark giá đối thủ.
2. **HTML widget** (`pricing_widget.html`): Interactive slider để Sales kéo % giảm giá → thấy ngay biên LN cập nhật realtime.
3. **PDF deal approval** (`deal_approval_template.pdf`): Mẫu trình duyệt deal lớn, có chỗ ký KTT, Sales Director, CEO.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/pricing/`

## Checklist Trước Khi Giao
- [ ] COGS đã update theo cost sheet mới nhất
- [ ] Phí sàn TMĐT đã đúng % cập nhật quý
- [ ] Đã tính Contribution Margin (không chỉ Gross Margin)
- [ ] Sensitivity table có cảnh báo vùng âm biên (đỏ)
- [ ] Break-even price hiển thị rõ ràng
- [ ] Có approval matrix theo mức chiết khấu
