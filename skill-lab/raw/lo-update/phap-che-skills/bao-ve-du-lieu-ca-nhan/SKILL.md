---
name: bao-ve-du-lieu-ca-nhan
description: >
  Xây dựng chính sách bảo vệ dữ liệu cá nhân (PDPA) cho SME Việt Nam theo Nghị định 13/2023/NĐ-CP
  — bao gồm chính sách quyền riêng tư, quy trình xử lý dữ liệu, đánh giá tác động và ứng phó
  sự cố rò rỉ dữ liệu. Dùng skill này khi người dùng cần: soạn chính sách bảo vệ dữ liệu,
  xây dựng quy trình thu thập dữ liệu khách hàng, chuẩn bị cho kiểm tra tuân thủ PDPA,
  xử lý yêu cầu xóa dữ liệu hoặc thiết lập cơ chế bảo vệ dữ liệu nhân viên.
  Kích hoạt khi nhắc đến: "bảo vệ dữ liệu cá nhân", "PDPA", "Nghị định 13/2023",
  "privacy policy", "chính sách quyền riêng tư", "dữ liệu khách hàng", "xóa dữ liệu",
  "rò rỉ dữ liệu", "data breach", "DPIA", "đồng ý thu thập dữ liệu".
---

# Skill: Bảo Vệ Dữ Liệu Cá Nhân (PDPA)

Bạn là pháp chế/DPO (Data Protection Officer) cho SME Việt Nam.
Mục tiêu là xây dựng hệ thống bảo vệ dữ liệu cá nhân đúng Nghị định 13/2023/NĐ-CP, tránh rủi ro pháp lý và bảo vệ uy tín doanh nghiệp.

---

**Cơ sở pháp lý:** Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân (có hiệu lực từ 1/7/2023)

⚠️ **Vi phạm có thể bị phạt hành chính từ 50–100 triệu VNĐ hoặc truy cứu trách nhiệm hình sự.**

---

## A. CÁC KHÁI NIỆM CỐT LÕI

```
DỮ LIỆU CÁ NHÂN (DLCN) là gì?
→ Mọi thông tin gắn với 1 con người cụ thể:
  Họ tên, CCCD, SĐT, email, địa chỉ nhà, vị trí GPS, ảnh khuôn mặt,
  thông tin sức khỏe, tài khoản ngân hàng, lịch sử mua hàng...

PHÂN LOẠI:
□ DLCN thông thường: Tên, SĐT, email, địa chỉ
□ DLCN nhạy cảm (cần bảo vệ cao hơn):
  Sức khỏe, chính kiến, tín ngưỡng, tình trạng hôn nhân, CCCD,
  thông tin tài chính, sinh trắc học (vân tay, khuôn mặt)

CÁC BÊN LIÊN QUAN:
- Chủ thể dữ liệu: Người mà dữ liệu thuộc về
- Bên Kiểm soát dữ liệu: Doanh nghiệp quyết định mục đích xử lý DLCN
- Bên Xử lý dữ liệu: Đơn vị xử lý DLCN theo ủy thác (ví dụ: công ty cloud)
```

---

## B. NGUYÊN TẮC XỬ LÝ DỮ LIỆU CÁ NHÂN (Điều 3 NĐ 13)

```
7 NGUYÊN TẮC PHẢI TUÂN THỦ:
━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. CÓ SỰ ĐỒNG Ý: Thu thập DLCN phải có sự đồng ý của chủ thể dữ liệu
   (Trừ trường hợp pháp luật quy định khác — khẩn cấp, nghĩa vụ pháp lý)

2. MỤC ĐÍCH RÕ RÀNG: Chỉ xử lý đúng mục đích đã thông báo
   → Không dùng email KH để gửi quảng cáo nếu chỉ thu thập cho giao dịch

3. TỐI THIỂU HÓA: Chỉ thu thập dữ liệu cần thiết cho mục đích
   → Không hỏi ngày sinh nếu chỉ cần SĐT để liên hệ

4. CHÍNH XÁC: Cập nhật dữ liệu khi có thay đổi

5. GIỚI HẠN LƯU TRỮ: Xóa dữ liệu khi hết mục đích
   → Không giữ DLCN ứng viên sau 6 tháng không tuyển

6. BẢO MẬT: Có biện pháp kỹ thuật và tổ chức phù hợp

7. TRÁCH NHIỆM GIẢI TRÌNH: Có thể chứng minh tuân thủ khi được yêu cầu
```

---

## C. MẪU CHÍNH SÁCH BẢO VỆ DỮ LIỆU CÁ NHÂN

```
CHÍNH SÁCH BẢO VỆ DỮ LIỆU CÁ NHÂN
[TÊN CÔNG TY]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ngày ban hành: .../.../...... | Phiên bản: 1.0

1. THÔNG TIN ĐƠN VỊ KIỂM SOÁT DỮ LIỆU
   Tên: [Tên công ty]
   Địa chỉ: ................. MST: .................
   Email liên hệ BVDLCN: ......................
   Người phụ trách BVDLCN: ....................

2. DỮ LIỆU CÁ NHÂN CHÚNG TÔI THU THẬP
   Với khách hàng: Họ tên, SĐT, email, địa chỉ giao hàng, lịch sử giao dịch
   Với nhân viên: Họ tên, CCCD, địa chỉ, thông tin lương, BHXH, sức khỏe
   Với ứng viên: CV, thông tin liên lạc, kết quả phỏng vấn

3. MỤC ĐÍCH XỬ LÝ
   □ Thực hiện hợp đồng và giao dịch
   □ Hỗ trợ khách hàng
   □ Gửi thông tin sản phẩm/dịch vụ (có sự đồng ý)
   □ Tuân thủ nghĩa vụ pháp lý (khai thuế, BHXH...)
   □ Cải thiện dịch vụ và phân tích kinh doanh

4. THỜI GIAN LƯU TRỮ
   Dữ liệu KH: Trong thời gian quan hệ + [X] năm sau
   Dữ liệu NV: Trong thời gian làm việc + [X] năm (theo luật thuế, BHXH)
   Dữ liệu ứng viên không tuyển: Tối đa 6 tháng (trừ khi có đồng ý lâu hơn)

5. QUYỀN CỦA CHỦ THỂ DỮ LIỆU (Điều 9 NĐ 13/2023)
   □ Quyền biết: Được biết dữ liệu nào đang được xử lý
   □ Quyền truy cập: Xem dữ liệu của mình
   □ Quyền chỉnh sửa: Yêu cầu cập nhật dữ liệu sai
   □ Quyền xóa: Yêu cầu xóa dữ liệu (khi hết mục đích/rút đồng ý)
   □ Quyền hạn chế xử lý: Yêu cầu tạm dừng xử lý
   □ Quyền phản đối: Phản đối việc xử lý DLCN của mình
   □ Quyền khiếu nại: Khiếu nại lên Cục An toàn thông tin — Bộ TT&TT

6. LIÊN HỆ ĐỂ THỰC HIỆN QUYỀN
   Email: ................... | SĐT: ...................
   Thời gian xử lý yêu cầu: Trong vòng 72 giờ (kể từ khi nhận)

7. BẢO MẬT DỮ LIỆU
   Chúng tôi áp dụng: Mã hóa dữ liệu, kiểm soát truy cập theo phân quyền,
   sao lưu định kỳ, huấn luyện nhân viên về BVDLCN.

8. CHIA SẺ VỚI BÊN THỨ BA
   Chúng tôi chỉ chia sẻ DLCN khi:
   □ Có sự đồng ý của chủ thể dữ liệu
   □ Thực hiện hợp đồng với đối tác được ủy quyền (có ký NDA/DPA)
   □ Theo yêu cầu bắt buộc của pháp luật
```

---

## D. CHECKLIST TUÂN THỦ PDPA

```
CHECKLIST TUÂN THỦ NGHỊ ĐỊNH 13/2023
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ Đã ban hành Chính sách BVDLCN và đăng tải công khai
□ Có form đồng ý thu thập DLCN (rõ mục đích, không ép buộc)
□ Có cơ chế để khách hàng/nhân viên thực hiện quyền của họ
□ Ký hợp đồng xử lý dữ liệu (DPA) với các vendor (Google, Salesforce, CRM...)
□ Có quy trình xử lý khi phát hiện rò rỉ dữ liệu (trong 72 giờ phải thông báo)
□ Đã đào tạo nhân viên về BVDLCN
□ Hạn chế quyền truy cập vào DLCN theo nguyên tắc "need to know"
□ Có kế hoạch xóa/hủy dữ liệu khi hết mục đích lưu trữ
□ Đã đánh giá tác động BVDLCN (DPIA) nếu xử lý DLCN nhạy cảm quy mô lớn
```

---

## E. QUY TRÌNH XỬ LÝ SỰ CỐ RÒ RỈ DỮ LIỆU

```
KHI PHÁT HIỆN RÒ RỈ DỮ LIỆU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Trong 72 giờ:
□ Xác định phạm vi rò rỉ (bao nhiêu người, dữ liệu gì)
□ Ngăn chặn rò rỉ tiếp theo (đổi mật khẩu, vô hiệu hóa truy cập)
□ Thông báo lên Cục An toàn thông tin — Bộ TT&TT (tại: mic.gov.vn)
□ Lập biên bản sự cố, ghi nhận chi tiết

Sau 72 giờ:
□ Thông báo đến các chủ thể dữ liệu bị ảnh hưởng (nếu gây rủi ro cao)
□ Điều tra nguyên nhân và khắc phục
□ Báo cáo đầy đủ cho cơ quan quản lý
□ Rút kinh nghiệm và cập nhật quy trình bảo mật
```

---

## Định dạng đầu ra

Soạn chính sách BVDLCN, checklist tuân thủ hoặc quy trình xử lý sự cố theo nhu cầu cụ thể.
Nếu cần file Word, kết hợp skill `docx`.
