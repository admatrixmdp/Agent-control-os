---
name: fin-tax-cit-estimator
description: |
  Ước tính thuế Thu Nhập Doanh Nghiệp (TNDN) tạm tính quý và quyết toán năm,
  tính các khoản chi phí được/không được trừ và ưu đãi thuế. Trigger phrases:
  "thuế TNDN", "thuế thu nhập doanh nghiệp", "CIT estimate", "tạm tính TNDN quý",
  "quyết toán TNDN", "tính thuế lợi nhuận", "chi phí được trừ", "ưu đãi thuế",
  "tax planning TNDN", "03/TNDN". Output là Excel tính TNDN + PDF tờ khai mẫu 03/TNDN.
---

# Ước Tính Thuế TNDN Tạm Tính Quý

## Mục Tiêu
Giúp Kế toán thuế / CFO ước tính chính xác số TNDN tạm nộp mỗi quý (deadline 30/T+1 sau quý)
để tránh: nộp thiếu bị phạt 0.03%/ngày, hoặc nộp dư mất chi phí cơ hội. Đồng thời quyết toán
năm tối ưu - tận dụng ưu đãi thuế.

## Khi Nào Dùng
- Cuối mỗi quý (Q1, Q2, Q3, Q4)
- Đầu Q1 năm sau quyết toán cả năm
- Khi có dự án mới được ưu đãi cần tính trước impact
- Khi xin chuyển lỗ năm trước

## Bước 1: Xác Định Lợi Nhuận Kế Toán Trước Thuế
Lấy từ P&L kỳ:
```
LN trước thuế kế toán = Doanh thu thuần - Giá vốn - CP bán hàng - CP QLDN
                       + DT tài chính - CP tài chính + LN khác
```

## Bước 2: Điều Chỉnh Theo Luật Thuế
**Cộng vào (chi phí không được trừ):**
- Phạt vi phạm hành chính
- Khoản tài trợ không đúng quy định
- Chi vượt định mức (tiếp khách, quảng cáo trước 2015...)
- Chi không có HĐ hợp lệ
- Khấu hao TSCĐ vượt mức quy định
- Lãi vay vượt EBITDA × 30% (TT 132)

**Trừ ra:**
- DT từ cổ tức đã chịu thuế
- Lỗ năm trước được chuyển (≤ 5 năm)
- DT từ hoạt động được miễn thuế

```
Thu nhập tính thuế = LN kế toán + (cộng vào) - (trừ ra)
```

## Bước 3: Tính Thuế Phải Nộp
**Thuế suất:**
- 20% chuẩn
- 17% DN nhỏ và vừa (DT ≤ 3 tỷ)
- 15% DN siêu nhỏ (DT ≤ 200tr)
- 10% DN công nghệ cao, KCN, R&D (ưu đãi)
- 0% trong 4 năm đầu nếu đủ điều kiện

```
Thuế TNDN phải nộp = Thu nhập tính thuế × thuế suất × (1 - mức ưu đãi)
Tạm nộp quý = (Tổng dự kiến năm) / 4 hoặc actual quý
```

**Lưu ý:** Tổng tạm nộp Q1-Q3 ≥ 75% số quyết toán năm, nếu không bị tính lãi chậm nộp phần thiếu.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Pull P&L từ sheet kế toán
- Google Drive MCP: Lưu file điều chỉnh + bằng chứng cho khoản không được trừ
- Gmail MCP: Gửi báo cáo CFO duyệt trước nộp
- WebSearch: Tra Nghị định 218, Thông tư 78, công văn cập nhật mới

**Fallback bằng API:**
```python
# Gọi MISA AMIS Tax API kiểm tra danh mục chi phí được/không trừ
import requests
expenses = get_expenses_from_gl(period="Q2_2026")
for exp in expenses:
    r = requests.post(
        "https://api.misa.vn/tax/v1/classify",
        json={"description": exp["desc"], "amount": exp["amount"],
              "has_invoice": exp["has_inv"]},
        headers={"Authorization": f"Bearer {TOKEN}"}
    )
    exp["deductible"] = r.json()["deductible"]
    exp["reason"] = r.json()["reason"]
```

## Bước 5: Output Format
1. **Excel tính TNDN** (`CIT_Q2_2026.xlsx`): Sheet "PL_to_taxable" mapping LN kế toán → LN tính thuế, "Adjustments" liệt kê +/- với bằng chứng, "Summary" số phải nộp + due date.
2. **PDF tờ khai** (`03_TNDN_Q2_2026.pdf`): Mẫu tạm tính (nếu áp dụng) hoặc 03/TNDN quyết toán.
3. **HTML dashboard** (`cit_dashboard.html`): Bar chart TNDN 4 quý, donut chi phí được trừ/không trừ, alert deadline còn N ngày.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/tax/cit/`

## Checklist Trước Khi Giao
- [ ] Đã đối chiếu LN kế toán khớp BCTC kỳ
- [ ] Tất cả khoản +/- đều có chứng từ chứng minh
- [ ] Đã check điều kiện ưu đãi thuế còn hiệu lực
- [ ] Tổng tạm nộp Q1-Q3 ≥ 75% ước quyết toán năm
- [ ] Đã nộp eTax trước 30/T+1 sau quý
- [ ] Đã lưu hồ sơ tối thiểu 10 năm
