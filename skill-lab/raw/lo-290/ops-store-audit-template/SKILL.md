---
name: ops-store-audit-template
description: |
  Template audit cửa hàng/quán hàng tháng — chấm điểm 100 mục theo 6P (People, Product, Process, Place, Promotion, Profit). Dùng skill này khi người dùng yêu cầu: "audit cửa hàng", "store audit", "kiểm tra cửa hàng định kỳ", "mystery shopper checklist", "monthly store inspection", "chấm điểm cửa hàng", "store visit report". Output là Excel form + PDF chấm điểm + dashboard so sánh chi nhánh.
---

# Store Audit Template — Audit Cửa Hàng Định Kỳ

## Mục Tiêu
Chuẩn hoá visit kiểm tra chi nhánh hàng tháng, có cơ sở so sánh tốt-xấu giữa store, drive cải tiến — quan trọng cho chuỗi > 5 cửa hàng.

## Khi Nào Dùng
- Area manager đi tour 5-10 store/tháng
- Mystery shopper (khách bí ẩn)
- Mid-quarter business review
- Trước khi mở chi nhánh thứ 10 cần chuẩn hoá
- Audit nhượng quyền (franchise)

## Bước 1: Cấu Trúc 6P Audit
**People** (20đ): nhân viên, dịch vụ
- Đồng phục đầy đủ, sạch
- Chào khách trong 10 giây
- Biết menu/sản phẩm
- Vệ sinh cá nhân (tóc, móng, nhẫn)

**Product** (20đ): chất lượng sản phẩm
- Đầy đủ menu/SKU
- Sản phẩm đúng chuẩn (visual, taste, size)
- Hạn sử dụng còn dài
- Bảo quản đúng nhiệt

**Process** (15đ): vận hành
- Thời gian phục vụ < cam kết
- Quy trình thanh toán mượt
- Order qua app/POS không lỗi
- Đóng gói chuẩn

**Place** (15đ): mặt bằng, vệ sinh
- Sàn nhà, bàn ghế sạch
- Toilet sạch (audit riêng)
- Biển hiệu sáng, không hỏng
- Nhiệt độ, ánh sáng, nhạc

**Promotion** (15đ): marketing
- POSM treo đúng campaign
- Khuyến mãi cập nhật
- Tờ rơi/voucher có sẵn
- Loyalty program promote

**Profit** (15đ): tài chính
- Doanh thu vs target tháng
- COGS theo định mức
- Waste/spoilage trong ngưỡng
- Inventory đúng

Tổng 100đ.

## Bước 2: Chấm Điểm + Phân Hạng
- 90-100: ⭐⭐⭐⭐⭐ Excellent
- 80-89: ⭐⭐⭐⭐ Good
- 70-79: ⭐⭐⭐ Average
- 60-69: ⭐⭐ Need improvement (tái audit 2 tuần)
- < 60: ⭐ Critical (cảnh báo manager, plan 30 ngày)

Mỗi mục chấm Pass/Fail/Partial + ảnh chứng minh + ghi chú.

## Bước 3: Action Plan Theo Audit
Sau audit, tạo action plan:
- Issue
- Severity (high/med/low)
- Owner (store manager / area / HQ)
- Due date
- Verification method
- Follow-up audit

Trong vòng 48h sau audit → audit recap meeting với store team.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Bảng tổng hợp audit toàn chuỗi
- Google Drive MCP: Lưu ảnh + video audit theo cửa hàng
- Slack MCP: Bot gửi báo cáo audit vào channel manager
- Notion MCP: Database action plan với status tracking
- Google Forms MCP: App audit trên điện thoại với form chuẩn
- WebSearch: Benchmark audit score chuỗi đối thủ
- WebFetch: Lấy tool mystery shopper từ servy.io

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# App audit mobile gửi data về dashboard
import requests
audit_data = {
    "store_id": "QN-Q1-01",
    "auditor": "Nguyen Anh",
    "date": "2026-05-28",
    "people": 18, "product": 17, "process": 14,
    "place": 12, "promotion": 13, "profit": 14,
    "total": 88, "rating": 4,
    "photos": ["url1","url2"],
    "issues": [
        {"area":"place","desc":"Toilet bẩn","severity":"high"}
    ]
}
requests.post("https://hooks.zapier.com/...", json=audit_data)
# Zapier append vào Google Sheets + Slack notify
```

## Bước 5: Output Format
- `Store_Audit_Form.xlsx` — form 100 mục có công thức tự tính
- `Store_Audit_<store>_<date>.pdf` — báo cáo từng cửa hàng
- `Chain_Comparison.html` — dashboard so sánh chi nhánh
- `Action_Plan_<store>.xlsx` — kế hoạch khắc phục
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/StoreAudit/`

## Checklist Trước Khi Giao
- [ ] Tổng cộng 100 điểm chính xác qua 6P
- [ ] Mỗi mục fail có ảnh chứng minh
- [ ] Action plan có owner + due
- [ ] So sánh với audit kỳ trước (cải tiến hay tụt)
- [ ] Top 3 store + Bottom 3 store hàng tháng
- [ ] Lương quản lý link một phần với audit score
