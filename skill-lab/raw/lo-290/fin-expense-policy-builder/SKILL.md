---
name: fin-expense-policy-builder
description: |
  Soạn chính sách công tác phí, chi tiếp khách, đi lại, ăn ở, văn phòng phẩm chuẩn cho
  doanh nghiệp SME Việt Nam - phù hợp luật thuế TNDN. Trigger phrases: "chính sách công tác phí",
  "expense policy", "chi phí đi lại", "per diem policy", "tiếp khách doanh nghiệp",
  "quy định thanh toán chi phí", "company travel policy", "định mức chi phí",
  "T&E policy", "soạn quy chế tài chính". Output là PDF chính sách + Excel mức trần
  chi tiết.
---

# Soạn Chính Sách Công Tác Phí & Chi Phí Doanh Nghiệp

## Mục Tiêu
Xây bộ chính sách T&E (Travel & Entertainment) rõ ràng - hạn chế tranh cãi NV-Kế toán,
đảm bảo chi phí được trừ thuế, tránh lạm dụng. Áp dụng cho mọi level từ nhân viên đến CEO.

## Khi Nào Dùng
- Doanh nghiệp mới chưa có chính sách
- Soát lại policy cũ đã 2-3 năm không update
- Khi mở rộng sang thị trường mới (HCM, HN, nước ngoài)
- Trước kiểm toán cuối năm
- Khi có vụ "tranh cãi" giữa NV và Kế toán về việc hoàn

## Bước 1: Khảo Sát Hiện Trạng & Benchmark
- Hỏi user về quy mô, ngành, văn hoá (tiết kiệm vs hào phóng)
- Khảo sát NV xem họ thường phát sinh CP gì
- Xem chính sách của top 3 đối thủ (tránh "cứng quá mất người")
- Tham khảo TT 78, NĐ 218 phần chi phí được trừ

## Bước 2: Build Định Mức Theo Level
**Theo cấp bậc:**

| Khoản | NV | Trưởng phòng | Giám đốc | TGĐ/HĐQT |
|-------|-----|--------------|----------|----------|
| Khách sạn/đêm (HN-HCM) | 1.0tr | 1.5tr | 2.5tr | 4.0tr |
| Khách sạn (tỉnh) | 700k | 1.0tr | 1.5tr | 2.5tr |
| Per diem ăn uống/ngày | 300k | 400k | 600k | 1.0tr |
| Vé máy bay | Eco | Eco | Business | Business |
| Vé tàu | A1 | A1 | VIP | VIP |
| Taxi/Grab | Phải hợp lý | Phải hợp lý | Free | Free |
| Tiếp khách/người (theo TT) | 500k | 700k | 1.0tr | 1.5tr |

**Loại CP:**
- Đi lại: vé MB, tàu, taxi/grab, thuê xe
- Lưu trú: khách sạn ≤ X sao
- Ăn uống: per diem hoặc thực chi có HĐ
- Tiếp khách
- Đào tạo: học phí, sách
- Văn phòng phẩm cá nhân
- Điện thoại, internet

## Bước 3: Quy Trình Phê Duyệt & Hoàn Tiền
**Trước đi công tác:**
- Tờ trình đi công tác (mục đích, dự kiến chi)
- Approval matrix theo số tiền dự chi:
  - <5tr: Trưởng phòng
  - 5-20tr: Giám đốc
  - >20tr: TGĐ

**Sau đi công tác:**
- Trong 7 ngày làm việc nộp đề nghị hoàn
- Kèm 100% chứng từ gốc (HĐ điện tử OK)
- Kế toán check trong 3 ngày, hoàn trong 7 ngày
- Thiếu chứng từ <5%: vẫn hoàn, NV bù thuế
- Vượt định mức: NV tự gánh hoặc xin duyệt ngoại lệ

**Quy định chứng từ:**
- ≥200k phải có HĐ đỏ/điện tử ghi MST công ty
- <200k chấp nhận bill ATM/POS
- Tiếp khách phải có danh sách khách + lý do gặp

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: Lưu policy chính thức + version history
- Gmail MCP: Gửi NV thông báo policy mới + acknowledge
- Google Sheets MCP: Form online NV submit đề nghị hoàn (link với approval workflow)
- WebSearch: Benchmark policy DN cùng ngành/quy mô

**Fallback bằng API:**
```python
# Tích hợp với Expensify/Concur/MISA AMIS Expense
import requests
expense_claim = {
    "employee": "EMP001",
    "trip_purpose": "Họp KH Đà Nẵng",
    "from_date": "2026-05-20",
    "to_date": "2026-05-22",
    "items": [
        {"category": "flight", "amount": 2_500_000, "receipt_url": "..."},
        {"category": "hotel", "amount": 3_000_000, "receipt_url": "..."},
        {"category": "meal", "amount": 1_200_000, "receipt_url": "..."}
    ]
}
# Auto-check vượt định mức
violations = []
for item in expense_claim["items"]:
    limit = get_limit(employee_level="MGR", category=item["category"])
    if item["amount"] > limit:
        violations.append(f"{item['category']}: vượt {item['amount']-limit:,}đ")
```

## Bước 5: Output Format
1. **PDF chính sách** (`expense_policy_v2_2026.pdf`): 10-15 trang, có MỤC LỤC, định nghĩa, scope, định mức (bảng), quy trình, biểu mẫu, hiệu lực.
2. **Excel định mức** (`expense_limits_2026.xlsx`): Sheet "ByLevel", "ByCategory", "ByRegion" - dễ tra cứu, có search box.
3. **HTML acknowledgment form** (`policy_acknowledge.html`): NV ký số xác nhận đọc + tuân thủ.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/policy/`

## Checklist Trước Khi Giao
- [ ] Định mức phù hợp ngân sách + benchmark ngành
- [ ] Tuân thủ điều kiện chi phí được trừ TNDN
- [ ] Có quy định rõ về vượt định mức (ai duyệt)
- [ ] Có template form xin đi + form hoàn
- [ ] Phổ biến đến 100% NV + acknowledge
- [ ] Review/cập nhật hàng năm
