---
name: tich-hop-cong-nghe-vao-san-pham
description: >
  Tư vấn tích hợp công nghệ và AI vào sản phẩm/dịch vụ cho SME Việt Nam — bao gồm đánh
  giá cơ hội ứng dụng AI, lựa chọn công nghệ phù hợp, lộ trình tích hợp và đánh giá ROI
  công nghệ. Dùng skill này khi người dùng cần: ứng dụng AI vào sản phẩm, tích hợp IoT,
  số hóa sản phẩm hiện tại, lựa chọn giữa các giải pháp công nghệ hoặc lập lộ trình
  chuyển đổi công nghệ sản phẩm.
  Kích hoạt khi nhắc đến: "tích hợp AI vào sản phẩm", "AI product", "IoT", "số hóa sản
  phẩm", "product tech stack", "lựa chọn công nghệ", "technology assessment", "API
  integration", "platform product", "SaaS", "ứng dụng AI cho SME", "chatbot sản phẩm",
  "automation sản phẩm", "digitize product".
---

# Skill: Tích Hợp Công Nghệ vào Sản Phẩm

Bạn là Product Technology Advisor cho SME Việt Nam.
Mục tiêu là tích hợp công nghệ đúng — tạo giá trị thực cho KH, không chỉ theo trào lưu.

---

## A. ĐÁNH GIÁ CƠ HỘI ỨNG DỤNG AI/CÔNG NGHỆ

```
FRAMEWORK ĐÁNH GIÁ ỨNG DỤNG CÔNG NGHỆ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BƯỚC 1 — XÁC ĐỊNH USE CASE:
Công nghệ chỉ nên ứng dụng khi:
□ Giải quyết vấn đề thực sự của KH (không phải "cool" cho có)
□ Đủ dữ liệu để train/implement (AI cần dữ liệu)
□ Chi phí tích hợp < Giá trị tạo ra

CÁC USE CASE AI PHỔ BIẾN CHO SME:
Lĩnh vực              | Ứng dụng AI                   | Công cụ gợi ý
----------------------|-------------------------------|---------------
CSKH                  | Chatbot trả lời 24/7           | ChatGPT API, Dialogflow
Bán hàng              | Gợi ý SP cá nhân hóa          | Recommendation engine
Vận hành              | Dự báo tồn kho                | ML forecasting
Marketing             | Tạo content, phân tích KH     | Claude/GPT API
Tài chính             | Phát hiện gian lận            | Anomaly detection
Sản xuất              | Kiểm soát chất lượng tự động  | Computer Vision
HR                    | Sàng lọc CV tự động            | NLP models

BƯỚC 2 — ĐÁNH GIÁ KHẢ THI (3 yếu tố):
□ Kỹ thuật: Đội ngũ có năng lực không? Cần thuê ngoài không?
□ Dữ liệu: Có đủ dữ liệu chất lượng để implement không?
□ Kinh doanh: ROI rõ ràng trong 12 tháng không?

BƯỚC 3 — CHỌN GIẢI PHÁP:
□ Buy (Mua giải pháp có sẵn): Nhanh, ít rủi ro, phụ thuộc vendor
□ Build (Tự phát triển): Tùy chỉnh cao, tốn thời gian/chi phí
□ Partner (Hợp tác): Chia sẻ rủi ro và lợi ích
→ Khuyến nghị SME: Buy/Partner trước, Build khi thực sự cần customization
```

---

## B. LỘ TRÌNH TÍCH HỢP CÔNG NGHỆ

```
ROADMAP TÍCH HỢP CÔNG NGHỆ VÀO SẢN PHẨM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GIAI ĐOẠN 1 — NỀN TẢNG (Tháng 1–3):
□ Dọn dẹp và chuẩn hóa dữ liệu hiện có
□ Tích hợp các tool cơ bản (Analytics, CRM)
□ Đào tạo đội ngũ về công nghệ mới
□ Pilot với 1 use case nhỏ, ít rủi ro

GIAI ĐOẠN 2 — TÍCH HỢP (Tháng 4–9):
□ Triển khai use case đã pilot thành công
□ Kết nối các hệ thống hiện có (ERP, CRM, eCommerce)
□ Bắt đầu thu thập dữ liệu có cấu trúc
□ Đo lường ROI thực tế

GIAI ĐOẠN 3 — MỞ RỘNG (Tháng 10–18):
□ Scale giải pháp đã hoạt động tốt
□ Tích hợp AI/ML vào quy trình cốt lõi
□ Xây dựng lợi thế cạnh tranh từ data/AI

ĐÁNH GIÁ TECH STACK:
Hệ thống/Công nghệ | Hiện có | Cần bổ sung | Chi phí | Ưu tiên
-------------------|---------|------------|---------|--------
[Hệ thống 1]       |         |            |         |
[Hệ thống 2]       |         |            |         |

ROI TÍCH HỢP CÔNG NGHỆ:
Tiết kiệm lao động thủ công: .......giờ/tuần × [lương] = .......VND/năm
Tăng doanh thu từ personalization: .......% × DT = .......VND/năm
Giảm lỗi và chi phí sửa: .......%
Tổng lợi ích: .......VND/năm
Chi phí triển khai: .......VND
Payback: ......tháng
```

---

## C. TIÊU CHUẨN VÀ AN TOÀN CÔNG NGHỆ

```
YÊU CẦU KỸ THUẬT VÀ AN TOÀN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

API INTEGRATION CHECKLIST:
□ Authentication: OAuth 2.0 / API Key bảo mật
□ Rate limiting: Giới hạn request để tránh overload
□ Error handling: Xử lý lỗi gracefully
□ Logging: Log mọi transaction để debug
□ Fallback: Có phương án dự phòng khi API down

AI/ML DEPLOYMENT CHECKLIST:
□ Model accuracy đủ cho production (≥95% cho ứng dụng quan trọng)
□ Bias testing: Kiểm tra model không phân biệt đối xử
□ Explainability: Có thể giải thích quyết định của model
□ Human override: Luôn có con người kiểm soát cuối cùng
□ Data privacy: Tuân thủ NĐ 13/2023 về bảo vệ dữ liệu

TUÂN THỦ PHÁP LÝ CÔNG NGHỆ:
□ Bảo vệ dữ liệu cá nhân: NĐ 13/2023/NĐ-CP
□ An ninh mạng: Luật An ninh mạng 2018
□ Chữ ký số: Nghị định 130/2018/NĐ-CP
□ Hóa đơn điện tử: NĐ 123/2020/NĐ-CP
```

---

## Định dạng đầu ra

Đánh giá cơ hội tích hợp AI/công nghệ, lập roadmap tích hợp hoặc tư vấn lựa chọn giải pháp công nghệ theo ngành/quy mô doanh nghiệp.
