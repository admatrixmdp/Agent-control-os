---
name: legal-terms-of-service
description: |
  Soạn Điều khoản Dịch vụ (Terms of Service / Điều khoản Sử dụng) cho website / app / SaaS / marketplace / e-commerce theo Luật Giao dịch điện tử 2023, Luật Bảo vệ NTD 2023, NĐ 52/2013 TMĐT. Kích hoạt khi người dùng nói: "soạn ToS", "Terms of Service", "điều khoản sử dụng", "điều khoản dịch vụ website", "viết Terms of Use", "điều khoản app", "Terms cho SaaS", "điều khoản cho sàn TMĐT", "ToS marketplace", "user agreement". Output là file .md / .html + bản .docx Việt-Anh có toàn bộ điều khoản trách nhiệm + giải quyết tranh chấp.
---

# Điều Khoản Dịch Vụ (ToS) cho Web / App / SaaS / E-commerce

## Mục Tiêu
Tạo ToS bảo vệ doanh nghiệp Việt Nam khỏi tranh chấp người dùng + tuân thủ Luật Giao dịch điện tử 2023 (số 20/2023/QH15), Luật Bảo vệ quyền lợi NTD 2023 (số 19/2023/QH15, hiệu lực 01/07/2024), NĐ 52/2013 về TMĐT, NĐ 85/2021 (sửa đổi).

## Khi Nào Dùng
- Launch web/app/SaaS mới
- Mở tính năng thanh toán / subscription
- Vận hành marketplace (kết nối seller-buyer)
- Tích hợp dịch vụ trả phí qua app (in-app purchase)
- Mở rộng sang quốc tế cần ToS song ngữ

## Bước 1: Phân Loại Mô Hình
- **Web tĩnh / blog**: ToS đơn giản (1-2 trang)
- **SaaS B2B**: cần MSA + DPA + SLA chi tiết
- **Marketplace C2C/B2C**: cần Seller Agreement + Buyer Agreement + Escrow policy
- **Subscription app**: auto-renewal + huỷ + hoàn tiền (Apple/Google Play TOS)
- **Fintech**: cần thêm điều khoản KYC + AML + báo cáo NHNN

## Bước 2: 15 Điều Khoản Bắt Buộc
1. Định nghĩa (User, Account, Service, Content)
2. Điều kiện đăng ký + xác thực tài khoản
3. Quyền & nghĩa vụ user
4. Quyền & nghĩa vụ doanh nghiệp
5. Quy tắc hành vi (cấm spam, fraud, scraping, reverse engineering)
6. Sở hữu trí tuệ (Service + User-Generated Content)
7. Thanh toán + phí + hoàn tiền
8. Subscription + auto-renewal + huỷ
9. Bảo mật (link sang Privacy Policy riêng)
10. Disclaimer + giới hạn trách nhiệm (Liability Cap)
11. Bồi thường (Indemnification từ user)
12. Đình chỉ / xoá tài khoản
13. Force Majeure
14. Luật áp dụng + giải quyết tranh chấp (Toà án VN cấp huyện theo Luật BVNTD 2023 Đ.71)
15. Thay đổi ToS + thông báo

## Bước 3: Điều Khoản Đặc Biệt Theo Ngành
- **TMĐT**: thông tin người bán đầy đủ (NĐ 52/2013), cơ chế giải quyết khiếu nại trong 7 ngày
- **SaaS**: SLA 99.5%, downtime credit, data export khi terminate
- **Marketplace**: chính sách hoàn tiền/đổi trả ≥7 ngày, KYC seller
- **App có in-app purchase**: tuân thủ Apple App Store Review Guideline + Google Play Policy
- **Fintech**: tuân thủ TT 39/2014 NHNN + Luật phòng chống rửa tiền 2022

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: lưu master ToS + version history
- Gmail MCP: gửi notification khi user agree ToS / khi ToS update
- Notion MCP: lưu kho ToS theo product line
- WebFetch: tra Luật mới tại `thuvienphapluat.vn` / `chinhphu.vn`
- WebFetch: tham khảo ToS đối thủ (Tiki, Shopee, Lazada) để chuẩn industry practice
- WebSearch: search "Terms of Service 2026 best practice" cho update mới nhất

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tự động log user consent ToS để chứng cứ pháp lý (Luật GDĐT 2023 Đ.18)
import hashlib
from datetime import datetime
import json

def log_user_consent(user_id, tos_version, ip, user_agent):
    record = {
        "user_id": user_id,
        "tos_version": tos_version,
        "tos_hash": hashlib.sha256(open(f"tos_{tos_version}.md","rb").read()).hexdigest(),
        "accepted_at": datetime.utcnow().isoformat(),
        "ip": ip,
        "user_agent": user_agent
    }
    # Ghi log immutable (S3 Object Lock / blockchain để chứng cứ trước toà)
    with open("consent_log.jsonl", "a") as f:
        f.write(json.dumps(record) + "\n")
    return record
```

## Bước 5: Output Format
- File `terms_of_service_vn.md` + `terms_of_service_en.md`: dán vào website
- File `terms_of_service.html`: bản render có TOC + anchor link
- File `terms_of_service_bilingual.docx`: bản 2 cột Việt-Anh để in
- File `consent_log_schema.json`: schema log consent để team Dev triển khai
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/terms-of-service/`

## Checklist Trước Khi Giao
- [ ] Có 15 điều khoản bắt buộc
- [ ] Có Liability Cap (thường = phí 12 tháng gần nhất)
- [ ] Có cơ chế thông báo thay đổi ToS ≥30 ngày trước hiệu lực
- [ ] Có cơ chế giải quyết tranh chấp trong nước (Toà án có thẩm quyền)
- [ ] Tuân thủ Luật BVNTD 2023 (không có điều khoản bất lợi không thể thương lượng)
- [ ] Link sang Privacy Policy + Cookie Policy riêng
- [ ] Có version + ngày hiệu lực
- [ ] Có cơ chế log consent (chứng cứ pháp lý)
