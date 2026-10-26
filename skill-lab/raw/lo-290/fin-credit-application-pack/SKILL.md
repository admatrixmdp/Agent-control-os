---
name: fin-credit-application-pack
description: |
  Lập hồ sơ vay vốn ngân hàng đầy đủ - BCTC, phương án kinh doanh, dòng tiền dự án, TS đảm bảo,
  trả lời câu hỏi RM. Trigger phrases: "hồ sơ vay ngân hàng", "credit application",
  "vay vốn lưu động", "vay dự án", "loan proposal", "BCTC vay ngân hàng",
  "phương án vay vốn", "thẩm định tín dụng", "tài sản đảm bảo", "vay LC/UPAS".
  Output là PDF pack đầy đủ + Excel cashflow vay.
---

# Hồ Sơ Vay Ngân Hàng (Vốn Lưu Động + Dự Án)

## Mục Tiêu
Tối đa hoá tỷ lệ duyệt vay - lãi suất tốt + hạn mức cao + ít TS đảm bảo - bằng cách
chuẩn bị hồ sơ chuyên nghiệp, lường trước câu hỏi RM, trình bày dòng tiền trả nợ thuyết phục.

## Khi Nào Dùng
- Vay vốn lưu động đầu năm
- Vay dự án CapEx
- Mở thư tín dụng (L/C) cho hàng nhập
- Vay UPAS (vay USD trả VND) cho XNK
- Refinance khoản vay cũ với điều kiện tốt hơn
- Khi mở rộng quan hệ với ngân hàng mới

## Bước 1: Chọn Sản Phẩm Vay & Ngân Hàng
**Loại vay:**
| Loại | Mục đích | Kỳ hạn | TS đảm bảo |
|------|----------|--------|-----------|
| Vốn lưu động | NVL, lương, AR | ≤12 tháng | AR, HTK, TS BĐS |
| Vay dự án | CapEx mới | 3-7 năm | TS hình thành từ vốn vay |
| L/C | NK hàng | 90-180 ngày | Ký quỹ + bảo lãnh |
| UPAS | Trả NCC nước ngoài | 90-360 ngày | L/C base |
| Bảo lãnh | Đấu thầu, thực hiện HĐ | Theo HĐ | Ký quỹ |

**So sánh NH:**
- Lãi suất công bố vs lãi suất ưu đãi
- Phí: thẩm định, giải ngân, trả trước hạn
- Tỷ lệ cho vay/TS đảm bảo (LTV)
- Tốc độ xử lý (3 ngày vs 3 tuần)

## Bước 2: Chuẩn Bị Bộ Hồ Sơ Tài Liệu
**Hồ sơ pháp lý DN:**
- ĐKKD, MST, điều lệ, biên bản HĐQT
- CCCD/hộ chiếu chủ DN, người đại diện
- Văn bản uỷ quyền vay (nếu không phải GĐ)

**Hồ sơ tài chính:**
- BCTC 2-3 năm gần nhất + tờ khai thuế tương ứng
- BCTC quý/6 tháng gần nhất
- Sổ phụ ngân hàng 6-12 tháng tất cả TK
- Bảng cân đối phát sinh tháng gần nhất
- Báo cáo công nợ AR/AP

**Hồ sơ phương án:**
- Phương án vay vốn (template NH cấp)
- Hợp đồng đầu ra (KH), đầu vào (NCC) chứng minh dòng tiền
- Đối với vay dự án: dự án khả thi, NPV/IRR, payback

**Hồ sơ tài sản đảm bảo:**
- Sổ đỏ/sổ hồng, giấy đăng ký xe
- Định giá độc lập (nếu NH yêu cầu)
- Bảo hiểm tài sản (BH cháy nổ TS BĐS)

## Bước 3: Viết Phương Án Vay Vốn Thuyết Phục
**Cấu trúc phương án:**
1. Giới thiệu DN (lịch sử, ngành, vị thế)
2. Mục đích vay cụ thể (mua gì, bao nhiêu, ai)
3. Phương án sản xuất kinh doanh
4. Dòng tiền hoàn trả - **phần quan trọng nhất**:
   - Doanh thu dự kiến theo tháng
   - Chi phí theo tháng
   - Dòng tiền ròng → đủ trả gốc + lãi
   - DSCR (Debt Service Coverage Ratio) ≥ 1.3 mới an toàn

5. Tài sản đảm bảo (mô tả, giá trị)
6. Cam kết DN

**Trả lời câu hỏi thường gặp RM:**
- Tại sao cần vay đúng số tiền này?
- Nếu doanh thu giảm 20% có trả nợ được không?
- Đã vay NH khác chưa? Quan hệ ra sao?
- Có nợ xấu nào không?

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: Lưu hồ sơ + version control + share RM
- Gmail MCP: Liên lạc, gửi tài liệu bổ sung
- WebFetch: Tra lãi suất công bố VCB, BIDV, MB, TPBank... realtime
- WebSearch: Tra CIC điểm tín dụng DN nếu có truy cập

**Fallback bằng API:**
```python
# Tự động sinh báo cáo dòng tiền trả nợ
import pandas as pd
import numpy_financial as npf

# Vay 5 tỷ, 36 tháng, lãi 10%/năm
P, n, r = 5_000_000_000, 36, 0.10/12
emi = -npf.pmt(r, n, P)

# Doanh thu dự kiến theo tháng (growth)
revenue = [pd.Series(range(1,37)).apply(lambda x: 800_000_000 * (1.02**x))]
opex_pct = 0.75
cash_for_debt = [rev * (1-opex_pct) for rev in revenue[0]]
dscr = [c/emi for c in cash_for_debt]

print(f"EMI: {emi:,.0f}đ/tháng")
print(f"DSCR avg: {sum(dscr)/len(dscr):.2f}")
print(f"DSCR min: {min(dscr):.2f}")
# Nếu DSCR min < 1.3 → cần xin grace period 6 tháng
```

## Bước 5: Output Format
1. **PDF pack chính** (`credit_app_<bank>_<purpose>.pdf`): 40-60 trang, có TOC: hồ sơ pháp lý, BCTC, phương án vay, dòng tiền, TS đảm bảo.
2. **Excel dòng tiền vay** (`loan_cashflow.xlsx`): Sheet "RevenueForecast", "OpexForecast", "DebtService", "DSCR_calc", "Sensitivity" (DT ±20%).
3. **PPTX present RM** (`credit_present.pptx`): 12-15 slide cho buổi gặp RM/Hội đồng tín dụng.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/credit/`

## Checklist Trước Khi Giao
- [ ] DSCR (mean & min) ≥ 1.3
- [ ] Tỷ lệ LTV ≤ 70% (vay/TS đảm bảo)
- [ ] BCTC mới nhất ≤ 6 tháng
- [ ] Phương án vay khớp số tiền + mục đích vay
- [ ] Đã check CIC không có nợ xấu nhóm 3-5
- [ ] Hồ sơ scan PDF rõ nét, có mục lục
