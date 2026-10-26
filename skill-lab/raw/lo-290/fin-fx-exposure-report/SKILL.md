---
name: fin-fx-exposure-report
description: |
  Báo cáo rủi ro tỷ giá (FX exposure) cho DN xuất nhập khẩu - đo lường net exposure
  USD/JPY/CNY/EUR và gợi ý phòng vệ (hedge). Trigger phrases: "rủi ro tỷ giá",
  "FX exposure", "hedge tỷ giá", "phòng vệ ngoại tệ", "FX risk", "đánh giá lại tỷ giá",
  "forward contract", "VAS 10 chênh lệch tỷ giá", "natural hedge", "báo cáo ngoại tệ".
  Output là Excel exposure report + PDF hedge proposal.
---

# Báo Cáo Rủi Ro Tỷ Giá USD/JPY/CNY/EUR

## Mục Tiêu
Giúp CFO DN xuất nhập khẩu đo lường chính xác mức độ "phơi nhiễm" tỷ giá - tránh tình trạng
1 cú sốc tỷ giá 5-10% xoá sạch lợi nhuận năm. Đề xuất phương án hedge phù hợp (forward,
swap, natural hedge).

## Khi Nào Dùng
- Cuối mỗi tháng đánh giá lại số dư ngoại tệ
- Trước khi ký hợp đồng xuất nhập khẩu lớn
- Khi NHNN có động thái điều hành tỷ giá
- Khi USD/VND biến động >2% trong 1 tháng
- Lập ngân sách năm với giả định tỷ giá

## Bước 1: Liệt Kê Toàn Bộ Khoản Mục Ngoại Tệ
**Bảng cân đối exposure:**
| Loại | USD | JPY | CNY | EUR |
|------|-----|-----|-----|-----|
| Tiền mặt + TGNH | | | | |
| AR (phải thu KH XK) | | | | |
| AP (phải trả NCC NK) | | | | |
| Vay ngoại tệ | | | | |
| Hợp đồng đã ký (chưa hạch toán) | | | | |
| **Net exposure** | | | | |

Net dương → lãi nếu VND mất giá
Net âm → lỗ nếu VND mất giá

## Bước 2: Tính Risk & Sensitivity
**Translation risk (VAS 10):**
- Đánh giá lại số dư cuối kỳ theo tỷ giá liên ngân hàng
- Chênh lệch tỷ giá hạch toán TK 413 → 635/515

**Transaction risk:**
- Hợp đồng tương lai chưa thanh toán
- Tính theo forward rate kỳ vọng

**Economic risk:**
- Ảnh hưởng dài hạn lên competitiveness
- Khó định lượng - dùng scenario

**Sensitivity:**
- Tỷ giá USD +5%, +10%, -5%, -10% → tác động P&L
- Ngưỡng tolerable: lỗ tỷ giá ≤ 2% lợi nhuận

## Bước 3: Đề Xuất Phương Án Hedge
**Natural hedge (rẻ nhất):**
- Match nhập USD với xuất USD
- Vay USD bằng dòng tiền USD trả

**Forward contract:**
- Khoá tỷ giá tương lai với NH
- Phí 0.5-1.5%/năm tuỳ kỳ hạn
- Áp dụng cho hợp đồng cụ thể, exposure rõ

**Swap:**
- Đổi nghĩa vụ ngoại tệ giữa USD-VND
- Phù hợp vay dài hạn

**Option:**
- Quyền chứ không nghĩa vụ
- Phí cao nhưng linh hoạt
- Hiếm áp dụng ở SME VN

**Quyết định:**
- Hedge 50-80% exposure mở
- Không hedge 100% (mất cơ hội tỷ giá thuận lợi)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebFetch: Pull tỷ giá Vietcombank, NHNN hàng ngày
- WebSearch: Tin tức Fed rate, JP BoJ, PBOC ảnh hưởng tỷ giá
- Google Sheets MCP: Update tỷ giá realtime vào model
- Gmail MCP: Cảnh báo CFO khi USD/VND biến động >1% trong 1 ngày

**Fallback bằng API:**
```python
# Pull tỷ giá Vietcombank tự động
import requests
import xml.etree.ElementTree as ET

r = requests.get("https://www.vietcombank.com.vn/api/exchangerates?date=2026-05-28")
data = r.json()
rates = {item["currencyCode"]: float(item["sell"]) for item in data["Data"]}

# Tính lỗ/lãi đánh giá lại
positions = {"USD": 500_000, "JPY": -10_000_000, "CNY": 200_000}
prev_rates = {"USD": 24_500, "JPY": 165, "CNY": 3_400}
pnl = sum(positions[cur] * (rates[cur] - prev_rates[cur])
          for cur in positions)
print(f"FX P&L tháng: {pnl:,.0f} VND")
```

## Bước 5: Output Format
1. **Excel exposure report** (`fx_exposure_T05_2026.xlsx`): Sheet "Exposure" theo loại tiền, "Revaluation" tính chênh lệch TG, "Sensitivity" 2D, "HedgeProposal".
2. **PDF hedge proposal** (`fx_hedge_proposal.pdf`): 4-6 trang trình CFO/HĐQT.
3. **HTML dashboard** (`fx_dashboard.html`): Line chart tỷ giá 12 tháng, gauge net exposure từng loại, alert khi exposure vượt ngưỡng.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/fx/`

## Checklist Trước Khi Giao
- [ ] Tỷ giá đánh giá lại đúng tỷ giá mua/bán NHTM theo VAS
- [ ] Đã liệt kê đủ tất cả khoản mục ngoại tệ (cả off-balance)
- [ ] Sensitivity ±10% có tính tác động đến covenant
- [ ] Đề xuất hedge có chi phí cụ thể, ROI rõ
- [ ] Có policy hedge ratio min/max (50-80% chẳng hạn)
- [ ] Báo cáo HĐQT định kỳ tháng/quý
