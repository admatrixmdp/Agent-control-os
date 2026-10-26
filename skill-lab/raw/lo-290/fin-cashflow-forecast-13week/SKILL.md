---
name: fin-cashflow-forecast-13week
description: |
  Dự báo dòng tiền 13 tuần rolling cho doanh nghiệp SME Việt Nam - cảnh báo sớm thiếu tiền,
  tối ưu hạn mức tín dụng. Trigger phrases: "dự báo cashflow", "13 week cashflow",
  "rolling forecast", "dự báo dòng tiền", "cash forecast", "cảnh báo thiếu tiền",
  "kế hoạch dòng tiền", "cashflow tuần", "TWCF", "treasury forecast". Output là file Excel
  model 13 tuần + HTML dashboard cảnh báo.
---

# Dự Báo Cashflow 13 Tuần Rolling

## Mục Tiêu
Cung cấp công cụ "early warning system" cho CFO - thấy trước 3 tháng dòng tiền âm/dương ở tuần nào,
chủ động vay vốn lưu động hoặc đẩy nhanh thu hồi công nợ. Đây là chuẩn của tập đoàn lớn áp xuống SME.

## Khi Nào Dùng
- Đầu mỗi tuần cần update forecast cho tuần kế tiếp
- Đàm phán hạn mức tín dụng với ngân hàng (cần proof dòng tiền)
- Trước khi quyết định CapEx lớn, tuyển ồ ạt, mở chi nhánh
- Doanh nghiệp đang tăng trưởng nóng nhưng cashflow căng

## Bước 1: Thu Thập Dữ Liệu Đầu Vào
- **Cash on hand** đầu kỳ: tổng số dư các tài khoản ngân hàng + tiền mặt
- **AR aging**: chia nhóm theo tuần dự kiến thu (T+0, T+1, T+2... T+12)
- **AP schedule**: tất cả hoá đơn NCC phải trả + due date
- **Lương + BHXH**: định kỳ tuần nào của tháng
- **Thuế VAT, TNCN, TNDN**: due date 20/T+1 và quý
- **Vay/trả nợ gốc-lãi**: theo lịch ngân hàng

## Bước 2: Xây Model 13 Tuần Rolling
Cấu trúc 5 khối:

**Inflows (dòng vào):**
- Thu từ khách hàng (theo AR aging)
- Vay mới giải ngân
- Tiền lãi gửi
- Thu khác (refund, thanh lý)

**Outflows (dòng ra):**
- Trả NCC (theo AP)
- Lương + BHXH + phúc lợi
- Thuế các loại
- Tiền thuê, điện, nước, internet
- Trả gốc + lãi vay
- CapEx đã commit
- Chi phí khác

**Net cashflow tuần = Inflows - Outflows**
**Ending balance = Opening + Net**

## Bước 3: Phân Tích & Cảnh Báo
- Tuần nào ending balance < ngưỡng tối thiểu (VD: 2 tỷ) → flag ĐỎ
- Tuần nào âm → flag ĐEN, gợi ý hành động:
  - Đẩy nhanh thu top 5 AR
  - Hoãn 1 số khoản AP không khẩn cấp
  - Drawdown hạn mức tín dụng
  - Hoãn CapEx
- Tính DCR (Debt Coverage Ratio) từng tuần

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Sync số liệu thực tế tuần qua, recalc forecast
- Google Drive MCP: Lưu version history mỗi tuần để compare
- Gmail MCP: Auto-gửi cảnh báo CFO khi balance dự kiến < ngưỡng
- WebSearch: Tra lãi suất liên ngân hàng để tính chi phí vay ngắn hạn

**Fallback bằng API:**
```python
# Gọi Vietcombank/MB Open Banking API lấy số dư realtime
import requests
r = requests.get(
    "https://openapi.vietcombank.com.vn/v1/accounts/balance",
    headers={"X-API-Key": VCB_KEY, "Authorization": f"Bearer {VCB_TOKEN}"}
)
balances = r.json()["accounts"]
total_cash = sum([a["available_balance"] for a in balances])
# Bơm vào ô A2 của file forecast
```

## Bước 5: Output Format
1. **Excel model** (`cashflow_13w_W22_2026.xlsx`): Sheet "Forecast" 13 cột tuần, sheet "Assumption" để chỉnh tham số, sheet "Sensitivity" 3 kịch bản Best/Base/Worst.
2. **HTML dashboard** (`cashflow_dashboard.html`): Biểu đồ cột ending balance 13 tuần với threshold line, table top inflows/outflows tuần tới, list cảnh báo top 5.
3. **PDF 1 trang** (`cashflow_exec_summary.pdf`): Cho CEO/HĐQT review nhanh.

## Checklist Trước Khi Giao
- [ ] Đã verify opening balance khớp sao kê ngân hàng
- [ ] AR/AP đã import bản mới nhất (không cũ hơn 24h)
- [ ] Đã chạy 3 kịch bản (Best/Base/Worst)
- [ ] Threshold cảnh báo đã align với CFO
- [ ] Có cơ chế update tự động hàng tuần
- [ ] Dashboard hiển thị rõ tuần "âm" bằng màu đỏ
