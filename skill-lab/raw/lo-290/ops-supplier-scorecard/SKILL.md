---
name: ops-supplier-scorecard
description: |
  Chấm điểm nhà cung cấp (NCC) theo 4 trục PQDS: Price, Quality, Delivery, Service — đầu vào để quyết định gia hạn/loại NCC hàng quý. Dùng skill này khi người dùng yêu cầu: "chấm điểm NCC", "supplier scorecard", "đánh giá nhà cung cấp", "vendor evaluation", "rating nhà cung cấp", "audit NCC", "phân loại NCC ABC", "supplier performance". Output là Excel scoring + Markdown report + PDF gửi NCC.
---

# Supplier Scorecard — Chấm Điểm Nhà Cung Cấp

## Mục Tiêu
Có cơ sở dữ liệu rõ ràng để chọn/loại NCC, đàm phán giá, không phụ thuộc cảm tính — giảm tổng chi phí NVL 5-12%.

## Khi Nào Dùng
- Cuối quý/cuối năm review NCC chiến lược
- Trước khi gia hạn hợp đồng dài hạn
- Đánh giá NCC mới sau 3 tháng dùng thử
- Audit ISO 9001 yêu cầu hồ sơ đánh giá NCC
- Có khiếu nại chất lượng từ sản xuất

## Bước 1: Thu Thập Dữ Liệu PQDS
Cho mỗi NCC, thu data 3-6 tháng gần nhất:

**Price (Giá)** — 25%:
- Giá so với benchmark thị trường
- Tỉ lệ tăng giá vs cam kết
- Điều khoản thanh toán (Net 30/60/90)

**Quality (Chất lượng)** — 30%:
- Tỉ lệ NG khi nhập (IQC fail rate)
- Số lần khiếu nại
- Tỉ lệ trả hàng

**Delivery (Giao hàng)** — 25%:
- On-time delivery rate (OTD)
- Fill rate (giao đủ số lượng)
- Lead time biến động

**Service (Dịch vụ)** — 20%:
- Thời gian phản hồi RFQ
- Hỗ trợ kỹ thuật
- Hợp tác xử lý khiếu nại

## Bước 2: Quy Đổi Sang Điểm 100
Mỗi tiêu chí có công thức chuyển sang điểm:
| Tiêu chí | Công thức | 100đ | 0đ |
|---|---|---|---|
| OTD | OTD% × 100 | 100% đúng hạn | <50% đúng hạn |
| NG rate | (1 - NG%) × 100 | 0% NG | >5% NG |
| Giá vs benchmark | (1 - delta) × 100 | Thấp hơn 10% | Cao hơn 20% |
| Response time RFQ | 100 - giờ trả lời | < 4h | > 48h |

Tổng điểm = Σ (điểm tiêu chí × weight)

Phân hạng:
- **A**: >= 85đ — Ưu tiên, tăng share of wallet
- **B**: 70-84đ — Giữ, kèm cải tiến
- **C**: 55-69đ — Cảnh báo, tìm backup
- **D**: < 55đ — Loại trong 3 tháng

## Bước 3: Soạn Report Cho NCC
Báo cáo gửi NCC gồm:
- Tổng điểm + xếp hạng
- Chi tiết 4 trục với biểu đồ radar
- Top 3 điểm yếu nhất + đề xuất cải thiện
- Cam kết của 2 bên cho quý sau
- Lịch họp review

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Đọc log nhập hàng + QC từ data warehouse
- Gmail MCP: Gửi scorecard PDF cho NCC sau review
- Notion MCP: Database NCC có hồ sơ + scorecard từng quý
- Slack MCP: Notify Sourcing channel về NCC tụt hạng
- WebSearch: So benchmark giá NVL trên alibaba.com, tradekey
- WebFetch: Lấy báo giá đối thủ NCC từ website

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Pull dữ liệu nhập hàng từ MISA AMIS Kế toán
import requests
TOKEN = "..."
r = requests.get("https://amisapp.misa.vn/api/v1/purchase-orders",
    headers={"Authorization": f"Bearer {TOKEN}"},
    params={"from": "2026-01-01", "to": "2026-03-31",
            "supplier_code": "NCC-001"})
orders = r.json()["data"]
otd = sum(1 for o in orders if o["actual_date"] <= o["due_date"]) / len(orders)
print(f"OTD: {otd:.1%}")
```

## Bước 5: Output Format
- `Supplier_Scorecard_Q<n>.xlsx` — full database, 1 row/NCC
- `Supplier_Report_<NCC>.pdf` — báo cáo 2 trang gửi từng NCC
- `Supplier_Radar.html` — chart radar so sánh top 10 NCC
- `Supplier_Action.md` — list NCC cần action + người chịu trách nhiệm
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/Supplier/`

## Checklist Trước Khi Giao
- [ ] Mỗi NCC có data tối thiểu 3 tháng
- [ ] Weight 4 trục cộng đúng 100%
- [ ] Có ít nhất 2 NCC backup cho mỗi mặt hàng critical
- [ ] Report gửi NCC có chữ ký Sourcing Manager
- [ ] Có kế hoạch transition cho NCC hạng D
- [ ] Lưu hồ sơ tối thiểu 3 năm theo ISO
