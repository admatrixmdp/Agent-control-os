---
name: legal-privacy-policy
description: |
  Soạn Chính Sách Bảo Mật (Privacy Policy) chuẩn Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân Việt Nam + GDPR (EU) + PDPA (Singapore) cho website / app / e-commerce / SaaS. Kích hoạt khi người dùng nói: "soạn privacy policy", "chính sách bảo mật website", "viết policy GDPR", "Nghị định 13 PDPL VN", "chính sách dữ liệu cá nhân", "privacy policy app", "policy đa ngôn ngữ", "privacy notice", "data protection policy", "compliance dữ liệu cá nhân". Output là file .md / .html + bản .docx Việt-Anh sẵn đăng web.
---

# Chính Sách Bảo Mật Dữ Liệu Cá Nhân (Việt-Anh)

## Mục Tiêu
Tạo Privacy Policy đầy đủ theo Nghị định 13/2023/NĐ-CP (PDPL Việt Nam, hiệu lực 01/07/2023) + GDPR (EU) + PDPA (Singapore/Thailand) — tránh phạt 2-5% doanh thu năm trước (NĐ 13/2023 Đ.4) hoặc 4% doanh thu toàn cầu (GDPR Đ.83).

## Khi Nào Dùng
- Launch website / app mới
- Mở rộng sang thị trường EU / Mỹ / SEA
- Bắt đầu thu thập dữ liệu cá nhân (email, sđt, CCCD, sinh trắc học)
- Tích hợp Google Analytics / Facebook Pixel / TikTok Pixel
- Khi nhận yêu cầu DSAR (Data Subject Access Request) từ khách hàng

## Bước 1: Xác Định Phạm Vi Áp Dụng
Hỏi user:
- Đối tượng người dùng: VN / EU / Mỹ / SEA / Toàn cầu?
- Loại dữ liệu thu thập: cơ bản (tên, email) / nhạy cảm (CCCD, sinh trắc học, sức khoẻ)
- Có dùng cookies/tracking pixels không?
- Có chuyển dữ liệu xuyên biên giới không (đòi hỏi Hồ sơ đánh giá tác động theo NĐ 13/2023 Đ.25)?

## Bước 2: 8 Nội Dung Bắt Buộc Theo NĐ 13/2023 (Đ.13)
1. Loại dữ liệu cá nhân được xử lý
2. Mục đích xử lý
3. Tổ chức/cá nhân được phép tiếp cận
4. Quyền của chủ thể dữ liệu (8 quyền: biết, đồng ý, truy cập, rút lại, xoá, hạn chế, cung cấp, khiếu nại)
5. Thời gian xử lý + lưu trữ
6. Biện pháp bảo mật
7. Hậu quả nếu không cung cấp
8. Thông tin liên hệ DPO (Data Protection Officer)

## Bước 3: Cấu Trúc Policy (12 Section)
1. Định nghĩa (Personal Data, Sensitive Data, Processing, Controller, Processor)
2. Loại dữ liệu thu thập (Bảng: loại / nguồn / mục đích / cơ sở pháp lý)
3. Mục đích xử lý (cụ thể, không "improving service")
4. Cơ sở pháp lý (Consent / Contract / Legal Obligation / Legitimate Interest)
5. Chia sẻ với bên thứ ba (liệt kê: AWS, Google, Meta, payment gateway)
6. Chuyển dữ liệu xuyên biên giới (kèm Hồ sơ TIA theo NĐ 13/2023)
7. Thời gian lưu trữ (theo từng loại — KH active: 5 năm sau hợp đồng cuối, marketing: 2 năm)
8. Quyền của bạn (8 quyền theo NĐ 13, 8 quyền theo GDPR)
9. Cookies & Tracking (bảng cookies + opt-out)
10. Bảo mật (mã hoá AES-256, MFA, audit log, ISO 27001)
11. Trẻ em (không thu thập <16 tuổi mà không có sự đồng ý của cha mẹ)
12. Liên hệ DPO + cập nhật Policy

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: lưu master Policy + lịch sử version
- Gmail MCP: gửi notification cho user khi Policy update (yêu cầu của NĐ 13 Đ.18)
- Notion MCP: cập nhật DPIA (Data Protection Impact Assessment) repository
- WebFetch: tra cứu hướng dẫn mới nhất tại `mps.gov.vn` (Cục An ninh mạng Bộ Công an — cơ quan giám sát NĐ 13)
- WebFetch: kiểm tra ICO.org.uk / EDPB.europa.eu cho GDPR update

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Sinh Privacy Policy multi-jurisdiction từ template
from jinja2 import Template
import yaml

with open("policy_config.yaml") as f:
    cfg = yaml.safe_load(f)  # markets, data_types, third_parties, dpo_email

template = Template(open("privacy_policy_template.md").read())
md = template.render(**cfg)

# Convert sang HTML + DOCX
import markdown
from docx import Document
html = markdown.markdown(md)
open("privacy_policy.html", "w", encoding="utf-8").write(html)

# Submit DPIA tới Cục ATTT (NĐ 13 Đ.43 — bắt buộc lưu hồ sơ tại đơn vị + báo cáo khi có yêu cầu)
```

## Bước 5: Output Format
- File `privacy_policy_vn.md` + `privacy_policy_en.md`: dán vào website
- File `privacy_policy.html`: bản render đẹp có TOC
- File `privacy_policy_bilingual.docx`: bản 2 cột Việt-Anh để in/ký
- File `dpia_assessment.xlsx`: Hồ sơ đánh giá tác động (theo NĐ 13/2023 Đ.25-26)
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/privacy-policy/`

## Checklist Trước Khi Giao
- [ ] Có đủ 8 nội dung bắt buộc theo NĐ 13/2023 Đ.13
- [ ] Liệt kê đủ third-party processors (Google, Meta, AWS, Stripe...)
- [ ] Có mục cookies + bảng opt-out
- [ ] Có cơ chế DSAR (form / email DPO / trả lời trong 72h theo NĐ 13)
- [ ] Có DPIA cho hoạt động xử lý dữ liệu nhạy cảm
- [ ] Có thông báo cơ chế khiếu nại tới Cục ATTT (Bộ Công an)
- [ ] Có ngày hiệu lực + cơ chế thông báo update
- [ ] Đã đăng web + có link footer mọi trang
