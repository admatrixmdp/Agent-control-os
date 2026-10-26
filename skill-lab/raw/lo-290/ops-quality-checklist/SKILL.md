---
name: ops-quality-checklist
description: |
  Tạo checklist kiểm tra chất lượng (QC) theo SKU/sản phẩm cho doanh nghiệp sản xuất, F&B, retail Việt Nam — đầy đủ tiêu chí AQL, sample size, pass/fail criteria. Dùng skill này khi người dùng yêu cầu: "tạo QC checklist", "checklist kiểm tra chất lượng", "AQL sampling", "tiêu chí kiểm hàng", "QC theo SKU", "quality inspection", "tạo phiếu QC", "kiểm tra đầu vào nguyên liệu". Output là Excel multi-sheet + PDF in được mang xuống xưởng.
---

# Tạo Checklist QC Theo SKU

## Mục Tiêu
Chuẩn hóa kiểm tra chất lượng cho từng SKU/lô hàng — giảm tỉ lệ hàng lỗi tới tay khách, có hồ sơ trace lỗi rõ ràng, hỗ trợ chứng nhận ISO/HACCP.

## Khi Nào Dùng
- Setup QC cho line sản xuất mới
- Nhận hàng từ NCC (IQC - Incoming Quality Control)
- Kiểm cuối line (OQC - Outgoing)
- Kiểm hàng nhập kho từ China/factory
- Audit định kỳ mặt hàng đang bán

## Bước 1: Thu Thập Thông Tin SKU
Hỏi:
1. Tên SKU + mã + ảnh
2. Loại kiểm tra: IQC / IPQC / OQC / FQC
3. Sample size (theo lô hay 100%)
4. Tiêu chuẩn áp dụng: ISO 2859, AQL 2.5/4.0, GMP, HACCP

## Bước 2: Phân Loại Lỗi (Defect Classification)
3 mức:
- **Critical (CR)**: lỗi nghiêm trọng, mất an toàn → AQL 0
- **Major (MA)**: ảnh hưởng chức năng, thẩm mỹ rõ → AQL 2.5
- **Minor (MI)**: lỗi nhỏ, không ảnh hưởng dùng → AQL 4.0

Ví dụ với áo thun:
- CR: rách lỗ thủng, mất khuy, kim còn dính
- MA: lệch may > 3mm, lem màu, sai size
- MI: chỉ thừa < 1cm, label hơi cong

## Bước 3: Soạn Checklist Theo Cấu Trúc Chuẩn
Mỗi item gồm 8 cột:
| STT | Hạng mục | Tiêu chí pass | Phương pháp kiểm | Dụng cụ | Loại lỗi | Sample | Kết quả |
|---|---|---|---|---|---|---|---|
| 1 | Kích thước | 30±0.2cm | Đo bằng thước | Thước cuộn | MA | 5/lô | OK/NG |
| 2 | Trọng lượng | 250±5g | Cân điện tử | Cân 1kg | MA | 5/lô | OK/NG |
| 3 | Màu sắc | So với mẫu chuẩn | Mắt thường, ánh sáng D65 | Light box | MI | 100% | OK/NG |

Tra bảng AQL ISO 2859-1 để xác định sample size:
- Lô 91-150: General Level II → n=20, Ac=1, Re=2 (AQL 2.5)
- Lô 1201-3200: n=125, Ac=7, Re=8

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Lưu QC log realtime, dashboard tỉ lệ NG theo SKU
- Google Drive MCP: Lưu ảnh hàng NG có ngày giờ
- Slack MCP: Bot cảnh báo khi tỉ lệ NG > ngưỡng
- Notion MCP: Database tiêu chuẩn QC từng SKU
- WebSearch: Tra bảng AQL ISO 2859 mới nhất
- WebFetch: Tải tiêu chuẩn TCVN từ tcvn.gov.vn

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tự động log kết quả QC vào Google Sheets
import gspread
gc = gspread.service_account(filename="creds.json")
sheet = gc.open("QC_Log_2026").sheet1
sheet.append_row(["2026-05-28", "SKU-001", "Lô-A123",
                  "QC-Nguyen", 125, 3, "Pass",
                  "Lỗi: 2 lệch may, 1 lem màu"])
```

## Bước 5: Output Format
- `QC_Checklist_<SKU>.xlsx` — Excel có sheet Tiêu chí, Sample plan, Log
- `QC_Checklist_<SKU>.pdf` — bản in mang xuống xưởng, có ô tick
- `QC_Defect_Photos/` — folder ảnh mẫu lỗi chuẩn để training
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/QC/`

## Checklist Trước Khi Giao
- [ ] Mỗi tiêu chí có chuẩn đo lường rõ (số + đơn vị)
- [ ] Sample size tra theo ISO 2859, không tự đặt
- [ ] Có ảnh mẫu lỗi Critical/Major
- [ ] Cột "Phương pháp kiểm" có chỉ rõ dụng cụ
- [ ] Có chỗ ký tên QC + thời gian
- [ ] Có flow xử lý khi NG (rework/return/scrap)
