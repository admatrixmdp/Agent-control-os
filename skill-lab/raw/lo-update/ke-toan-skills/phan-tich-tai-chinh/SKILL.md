---
name: phan-tich-tai-chinh
description: >
  Phân tích chuyên sâu các chỉ số tài chính và sức khỏe tài chính của SME Việt Nam — bao gồm
  phân tích khả năng thanh toán, hiệu quả hoạt động, khả năng sinh lời, cơ cấu vốn, và so sánh
  với chuẩn ngành. Dùng khi người dùng cần đánh giá tình hình tài chính, chuẩn bị vay vốn ngân hàng,
  báo cáo nhà đầu tư, hoặc ra quyết định kinh doanh. Kích hoạt khi nhắc đến: "phân tích tài chính",
  "chỉ số tài chính", "sức khỏe tài chính", "ROE", "ROA", "tỷ lệ nợ", "đánh giá tài chính",
  "financial analysis", "chuẩn bị hồ sơ vay vốn", "phân tích cho nhà đầu tư".
---

# Skill: Phân Tích Chỉ Số Tài Chính

Bạn là chuyên gia phân tích tài chính cho SME Việt Nam.
Mục tiêu là biến số liệu trên báo cáo tài chính thành insights có thể hành động — giúp lãnh đạo ra quyết định sáng suốt.

---

## Quy trình làm việc

### 1. Thu thập dữ liệu
Yêu cầu người dùng cung cấp (hoặc nhập số liệu từ BCTC):
- Bảng cân đối kế toán (ít nhất 2 kỳ để so sánh)
- Báo cáo kết quả kinh doanh
- Báo cáo lưu chuyển tiền tệ (nếu có)

---

## HỆ THỐNG CHỈ SỐ TÀI CHÍNH (DuPont Framework)

### NHÓM 1 — KHẢ NĂNG THANH TOÁN (Liquidity Ratios)

| Chỉ số | Công thức | Mức tham khảo tốt | Ý nghĩa |
|--------|-----------|-------------------|---------|
| Current Ratio | TSNH / Nợ NH | 1.5 – 3.0 | Khả năng trả nợ ngắn hạn |
| Quick Ratio | (TSNH - HTK) / Nợ NH | ≥ 1.0 | Không cần bán hàng vẫn trả được nợ |
| Cash Ratio | Tiền / Nợ NH | ≥ 0.2 | Thanh toán ngay tức khắc |
| Working Capital | TSNH - Nợ NH | > 0 | Vốn lưu động ròng |

**Cảnh báo:**
- Current Ratio < 1: Nguy hiểm — không đủ tài sản ngắn hạn để trả nợ
- Current Ratio > 3: Có thể đang để tiền/HTK ứ đọng quá nhiều

---

### NHÓM 2 — HIỆU QUẢ HOẠT ĐỘNG (Efficiency Ratios)

| Chỉ số | Công thức | Đơn vị | Mức tốt |
|--------|-----------|--------|---------|
| Vòng quay tài sản | Doanh thu / Tổng tài sản | Lần | ≥ 1 |
| Vòng quay HTK | GVHB / HTK bình quân | Lần | Tùy ngành |
| Số ngày tồn kho (DIO) | 365 / Vòng quay HTK | Ngày | Càng thấp càng tốt |
| DSO (Phải thu) | (Phải thu / DT) × 365 | Ngày | < 45 ngày |
| DPO (Phải trả) | (Phải trả / GVHB) × 365 | Ngày | 30–60 ngày |
| CCC | DSO + DIO - DPO | Ngày | < 45 ngày |

---

### NHÓM 3 — KHẢ NĂNG SINH LỜI (Profitability Ratios)

| Chỉ số | Công thức | Mức tốt (SME VN) |
|--------|-----------|-----------------|
| Gross Profit Margin | LN gộp / DT × 100% | Tùy ngành (Bán lẻ 20–40%, Dịch vụ 40–70%) |
| EBITDA Margin | EBITDA / DT × 100% | ≥ 10–15% |
| Net Profit Margin | LNST / DT × 100% | ≥ 5–10% |
| ROA | LNST / Tổng TS bình quân × 100% | ≥ 5% |
| ROE | LNST / VCSH bình quân × 100% | ≥ 15% |
| ROCE | EBIT / (Tổng TS - Nợ NH) × 100% | ≥ 12% |

**Phân tích ROE theo DuPont:**
```
ROE = Net Margin × Asset Turnover × Equity Multiplier
    = (LNST/DT) × (DT/Tổng TS) × (Tổng TS/VCSH)
```
→ Giúp xác định ROE đến từ đâu: Biên lợi nhuận / Hiệu quả sử dụng tài sản / Đòn bẩy tài chính

---

### NHÓM 4 — CƠ CẤU VỐN & ĐÒN BẨY (Leverage Ratios)

| Chỉ số | Công thức | Mức an toàn |
|--------|-----------|------------|
| Debt-to-Equity (D/E) | Tổng nợ / VCSH | ≤ 1.0 – 2.0 |
| Debt-to-Assets | Tổng nợ / Tổng TS | ≤ 50–60% |
| Interest Coverage | EBIT / Lãi vay | ≥ 3 |
| Debt Service Coverage | EBITDA / (Nợ gốc + Lãi vay) | ≥ 1.25 |

**Cảnh báo:**
- D/E > 2: Rủi ro tài chính cao, khó vay thêm
- Interest Coverage < 1.5: Nguy hiểm — lợi nhuận không đủ trả lãi

---

### NHÓM 5 — TĂNG TRƯỞNG (Growth Ratios)

| Chỉ số | Công thức | So sánh với |
|--------|-----------|------------|
| Tăng trưởng doanh thu | (DT kỳ này - DT kỳ trước) / DT kỳ trước | Ngành, lạm phát |
| Tăng trưởng lợi nhuận | Tương tự | Phải > Tăng trưởng DT |
| Tăng trưởng tổng tài sản | Tương tự | Phải đi kèm ROA ổn định |

---

## PHÂN TÍCH SO SÁNH (BENCHMARKING)

### Tham khảo chuẩn theo ngành (Việt Nam)

| Ngành | Gross Margin | Net Margin | ROE | D/E |
|-------|-------------|------------|-----|-----|
| Bán lẻ/FMCG | 20–35% | 2–5% | 15–25% | 0.5–1.5 |
| Sản xuất | 15–30% | 5–10% | 12–20% | 0.5–1.5 |
| Dịch vụ | 40–70% | 10–20% | 15–30% | 0.2–0.8 |
| Bất động sản | 20–40% | 5–15% | 10–20% | 1.0–3.0 |
| Xây dựng | 10–20% | 2–6% | 10–18% | 1.0–2.0 |
| F&B | 30–60% | 5–12% | 15–25% | 0.3–1.0 |

---

## SCORECARD SỨC KHỎE TÀI CHÍNH (100 điểm)

| Nhóm chỉ số | Trọng số | Tiêu chí đánh giá |
|-------------|----------|-------------------|
| Khả năng thanh toán | 25đ | Current ratio, Quick ratio, Cash ratio |
| Sinh lời | 30đ | Net margin, ROE, ROA |
| Hiệu quả hoạt động | 20đ | CCC, Vòng quay TS |
| Cơ cấu vốn | 15đ | D/E, Interest coverage |
| Tăng trưởng | 10đ | Tăng trưởng DT và LN |

**Thang điểm:**
- 80–100: Sức khỏe tốt — Ổn định, có thể mở rộng
- 60–79: Sức khỏe trung bình — Cần cải thiện một số điểm
- 40–59: Cần chú ý — Một số rủi ro đáng kể
- < 40: Cần hành động ngay — Nguy cơ tài chính cao

---

## Định dạng đầu ra

```
📊 PHÂN TÍCH TÀI CHÍNH TOÀN DIỆN

Doanh nghiệp: [Tên] | Kỳ phân tích: [Ngày/Năm]

━━━ SCORECARD SỨC KHỎE TÀI CHÍNH ━━━
🎯 TỔNG ĐIỂM: [X]/100 — [Đánh giá tổng thể]

━━━ PHÂN TÍCH TỪNG NHÓM CHỈ SỐ ━━━

1. Khả năng thanh toán: [X]/25
   Current Ratio: [X] → [🟢/🟡/🔴 Đánh giá]
   Quick Ratio: [X] → [Đánh giá]
   Nhận xét: [...]

2. Khả năng sinh lời: [X]/30
   Net Margin: [X%] → [Đánh giá]
   ROE: [X%] → [Đánh giá]
   ROA: [X%] → [Đánh giá]
   DuPont: [Phân tích nguồn gốc ROE]

3. Hiệu quả hoạt động: [X]/20
   CCC: [X] ngày → [Đánh giá]
   DSO: [X] ngày | DIO: [X] ngày | DPO: [X] ngày

4. Cơ cấu vốn: [X]/15
   D/E: [X] → [Đánh giá]
   Interest Coverage: [X] → [Đánh giá]

5. Tăng trưởng: [X]/10
   Doanh thu: [+/-X%] | Lợi nhuận: [+/-X%]

━━━ SO SÁNH VỚI CHUẨN NGÀNH ━━━
[Bảng so sánh]

━━━ ĐIỂM MẠNH TÀI CHÍNH ━━━
• [Top 3 điểm mạnh]

━━━ RỦI RO & CẢNH BÁO ━━━
• [Các vấn đề cần xử lý]

━━━ ĐỀ XUẤT CỤ THỂ ━━━
• [5 hành động ưu tiên]
```
