---
name: ceo-cash-position-dashboard
description: |
  Dashboard vị thế tiền mặt cho CEO — pull bank statement đa tài khoản, tính tổng cash, projected cash 13 tuần, AR/AP, FX exposure. Cảnh báo khi runway xuống dưới ngưỡng.
  Kích hoạt khi người dùng nói: "cash position", "vị thế tiền", "dashboard tiền mặt", "cash flow 13 tuần", "13-week cash", "runway dashboard", "tiền mặt công ty", "bank balance tổng".
  Output là HTML dashboard + Excel projection.
---

# CEO Cash Position Dashboard — Vị Thế Tiền Mặt

## Mục Tiêu
"Cash is king". CEO không biết tiền chính xác hôm nay = lái xe nhắm mắt. Dashboard này pull bank balance đa tài khoản, project 13 tuần, alert nguy hiểm.

## Khi Nào Dùng
- Hàng ngày sáng 8h
- Trước quyết định chi lớn (>100M)
- Trước họp board / investor
- Trong giai đoạn raise vốn
- Khi runway < 6 tháng

## Bước 1: Pull Bank Balance Đa Tài Khoản
- VCB, MB, TCB, VPB... (Việt Nam)
- USD account (FX)
- Stripe/PayPal payout pending
- Tiền mặt két (nếu có)

Tổng cash = sum tất cả.

## Bước 2: 13-Week Cash Projection
Cash flow forecast theo tuần:
- **Inflow**: customer payments (theo invoice date), funding tranche
- **Outflow**: payroll (cố định tuần 1 mỗi tháng), rent, supplier, tax, marketing
- **Net cash flow tuần**
- **Cumulative cash**

Identify tuần nào cash xuống thấp nhất (trough).

## Bước 3: 5 Metric Theo Dõi
1. **Total cash** (VND + USD quy đổi)
2. **Runway** (cash / monthly net burn)
3. **Burn multiple** (net burn / net new ARR)
4. **AR aging** (>30, >60, >90 days)
5. **AP outstanding** (mình nợ NCC)

Alert tự động:
- Runway < 6 tháng → ĐỎ + email board
- AR > 60 days > 15% AR → CAM
- AP overdue → ĐỎ

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: pull bank statement đã export
- Plaid/Yodlee (qua API): real-time bank balance
- Stripe MCP: pull payout pending
- Gmail MCP: alert khi runway giảm
- Slack MCP: post snapshot lên #ceo-finance

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# 13-week projection
import pandas as pd
weeks = pd.date_range('2026-05-28', periods=13, freq='W')
inflow = [estimated_collections(w) for w in weeks]
outflow = [estimated_payments(w) for w in weeks]
df = pd.DataFrame({'inflow': inflow, 'outflow': outflow}, index=weeks)
df['net'] = df['inflow'] - df['outflow']
df['cum_cash'] = starting_cash + df['net'].cumsum()
trough_week = df['cum_cash'].idxmin()
```

## Bước 5: Output Format
- HTML dashboard:
  - Hero: total cash big number + runway
  - Line chart 13-week projection
  - Bảng inflow/outflow theo tuần
  - AR/AP aging chart
- Excel `cash-position-YYYY-MM-DD.xlsx`
- Slack alert nếu có ĐỎ
- Daily email 8h sáng
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ tài khoản bank (không sót)
- [ ] FX quy đổi theo tỷ giá hôm nay
- [ ] 13-week projection có giả định rõ
- [ ] Trough tuần được flag
- [ ] Alert tự động set đúng ngưỡng
- [ ] Verify với CFO trước khi gửi CEO
