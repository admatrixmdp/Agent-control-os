---
name: fin-ap-payment-runner
description: |
  Lập kế hoạch thanh toán nhà cung cấp (NCC) tối ưu theo due date, ưu tiên chiến lược
  và cash available, tránh trả sớm phí cơ hội hoặc trả trễ mất uy tín. Trigger phrases:
  "kế hoạch thanh toán", "AP payment run", "lịch trả NCC", "trả nhà cung cấp",
  "công nợ phải trả", "payment scheduling", "ưu tiên thanh toán", "lịch chi tiền",
  "thanh toán nhà cung cấp", "AP run". Output là Excel payment batch + PDF danh sách
  trình duyệt.
---

# Plan Thanh Toán Nhà Cung Cấp Theo Due Date + Cash Available

## Mục Tiêu
Giúp Kế toán AP và Treasurer "chia bánh tiền" mỗi đợt chi - đảm bảo NCC chiến lược
không bị trễ, NCC chiến thuật vẫn ổn, tận dụng tối đa thời gian giữ tiền mà không
phá uy tín. Tự động sinh batch payment chuyển khoản ngân hàng.

## Khi Nào Dùng
- Mỗi đợt chi tuần (thứ 2 và thứ 5)
- Khi cash căng phải quyết định ai trả trước
- Cuối tháng push thanh toán theo cam kết
- Khi có chiết khấu thanh toán sớm (early payment discount) cần tính ROI

## Bước 1: Thu Thập Danh Sách AP Open
Từ phần mềm kế toán lấy tất cả invoice chưa thanh toán:
- Mã NCC, tên NCC, phân loại (Chiến lược/Chiến thuật/Thường)
- Số HĐ, ngày phát hành, due date, số tiền
- Có chiết khấu thanh toán sớm không (2/10 net 30 chẳng hạn)
- Phương thức thanh toán (CK, TM, LC)

## Bước 2: Lấy Cash Available
- Số dư khả dụng các tài khoản thanh toán
- Trừ buffer tối thiểu (VD: giữ 500tr emergency)
- Cộng dòng tiền vào dự kiến trong 7 ngày (từ skill cashflow-13week)

## Bước 3: Thuật Toán Ưu Tiên
Tính `priority_score` cho từng HĐ:

```
priority = w1 * urgency + w2 * strategic + w3 * discount - w4 * size_penalty
```

- urgency: số ngày quá hạn (càng quá hạn càng cao)
- strategic: 3 nếu NCC chiến lược, 2 chiến thuật, 1 thường
- discount: % chiết khấu thanh toán sớm (nếu trả sớm trong window)
- size_penalty: HĐ quá lớn so với cash → giảm priority để chia nhiều đợt

Sắp xếp giảm dần, lấy từ trên xuống đến khi hết cash available.

**Đặc biệt:** Luôn ưu tiên trả lương, thuế, BHXH, điện-nước, lãi vay (non-negotiable).

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Sync danh sách AP open từ sheet kế toán
- Gmail MCP: Gửi NCC thông báo lịch thanh toán cụ thể (giữ uy tín)
- Google Drive MCP: Lưu file batch payment đã ký số
- WebSearch: Tra lãi suất ngân hàng nếu cần delay payment đổi vay ngắn

**Fallback bằng API:**
```python
# Đẩy batch payment qua VCB Open Banking API
import requests
batch = {
    "batch_id": "PAY_20260528_01",
    "from_account": "0011000123456",
    "items": [
        {"to_account": v["bank_acc"], "amount": v["amount"],
         "ref": v["invoice_no"], "ben_name": v["supplier"]}
        for v in payment_list
    ]
}
r = requests.post(
    "https://openapi.vietcombank.com.vn/v1/payments/batch",
    json=batch,
    headers={"Authorization": f"Bearer {VCB_TOKEN}"}
)
print(r.json()["batch_status"])  # PENDING_APPROVAL
```

## Bước 5: Output Format
1. **Excel batch** (`AP_batch_20260528.xlsx`): Sheet "Approved" gồm NCC, số tiền, tài khoản, MST, nội dung CK; sheet "Deferred" liệt kê khoản hoãn + lý do.
2. **PDF duyệt chi** (`payment_approval_20260528.pdf`): 1-2 trang, có chỗ ký KTT-CFO-CEO theo phân cấp.
3. **HTML dashboard** (`ap_dashboard.html`): Bar chart cash vs payment 4 tuần tới, table top NCC waiting, status (Paid/Pending/Hold).

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/ap/`

## Checklist Trước Khi Giao
- [ ] Tổng payment batch ≤ cash available - buffer
- [ ] Đã trả 100% lương, thuế, BHXH, điện-nước due trong tuần
- [ ] NCC chiến lược quá hạn ≤ 7 ngày
- [ ] Tận dụng được early payment discount nếu IRR >12%/năm
- [ ] Batch có đủ chữ ký phân cấp
- [ ] Thông báo lịch trả cho NCC bị hoãn để giữ quan hệ
