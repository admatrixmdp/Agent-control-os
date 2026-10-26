---
name: sao-luu-phuc-hoi-du-lieu
description: >
  Xây dựng chiến lược sao lưu và phục hồi dữ liệu (backup & disaster recovery) cho SME
  Việt Nam — bao gồm kế hoạch backup 3-2-1, quy trình kiểm tra backup, RTO/RPO và kế hoạch
  ứng phó sự cố mất dữ liệu. Dùng skill này khi người dùng cần: lập kế hoạch backup dữ liệu,
  xây dựng disaster recovery plan, kiểm tra và khôi phục backup hoặc tính toán RTO/RPO.
  Kích hoạt khi nhắc đến: "sao lưu dữ liệu", "backup", "khôi phục dữ liệu", "disaster
  recovery", "RTO", "RPO", "mất dữ liệu", "restore dữ liệu", "backup plan", "BCP",
  "business continuity", "phục hồi sau thảm họa", "backup định kỳ".
---

# Skill: Sao Lưu & Phục Hồi Dữ Liệu

Bạn là IT Manager chuyên bảo vệ dữ liệu cho SME Việt Nam.
Mục tiêu là đảm bảo có thể phục hồi dữ liệu trong mọi tình huống với thời gian tối thiểu.

---

## A. CHIẾN LƯỢC BACKUP 3-2-1

```
CHIẾN LƯỢC BACKUP 3-2-1
━━━━━━━━━━━━━━━━━━━━━━━━

Quy tắc 3-2-1:
□ 3 bản sao dữ liệu (1 bản gốc + 2 bản backup)
□ 2 loại phương tiện khác nhau (ổ cứng ngoài + cloud)
□ 1 bản offsite (bên ngoài văn phòng/cloud)

BẢNG KẾ HOẠCH BACKUP:
Loại dữ liệu          | Tần suất | Phương tiện 1 | Phương tiện 2 | Offsite | Lưu giữ
---------------------|---------|--------------|--------------|---------|--------
Dữ liệu ERP/kế toán  | Hàng ngày| NAS nội bộ  | Cloud (S3...)| ✓ Cloud | 1 năm
Email toàn công ty    | Hàng ngày| Exchange/Mail| Cloud backup | ✓ Cloud | 6 tháng
Dữ liệu KH/CRM      | Hàng ngày| NAS nội bộ  | Cloud        | ✓ Cloud | 2 năm
Tài liệu nội bộ      | Tuần 1 lần| NAS nội bộ | Ổ cứng ngoài | ✓ Cloud | 6 tháng
Code/Website         | Mỗi commit| Git server  | GitHub/GitLab| ✓ Cloud | Vĩnh viễn
Cấu hình server/máy  | Tháng 1 lần| NAS nội bộ| Cloud        | ✓ Cloud | 6 tháng

TÍNH TOÁN RTO/RPO:
RPO (Recovery Point Objective = Mất tối đa bao nhiêu dữ liệu?):
→ ERP quan trọng: RPO = 1 giờ (backup mỗi giờ)
→ Tài liệu bình thường: RPO = 24 giờ (backup hàng ngày)

RTO (Recovery Time Objective = Phục hồi trong bao lâu?):
→ Hệ thống critical: RTO ≤ 4 giờ
→ Hệ thống thông thường: RTO ≤ 24 giờ
```

---

## B. CHECKLIST KIỂM TRA BACKUP ĐỊNH KỲ

```
CHECKLIST KIỂM TRA BACKUP — THÁNG [THÁNG/NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KIỂM TRA BACKUP TỰ ĐỘNG HÀNG NGÀY:
□ Backup ERP đêm qua thành công?  □Có □Không — Log: .......
□ Backup email đêm qua thành công? □Có □Không — Log: .......
□ Dung lượng backup không vượt 80% ổ lưu trữ? □Có □Không

KIỂM TRA RESTORE THỬ (1 lần/tháng — BẮT BUỘC):
□ Chọn ngẫu nhiên 1 file từ backup 7 ngày trước
□ Restore vào máy test, kiểm tra file mở được và dữ liệu đúng
□ Kết quả: □ Thành công  □ Thất bại — Nguyên nhân: ............

KIỂM TRA OFFSITE BACKUP:
□ Backup cloud cập nhật trong 24 giờ qua? □Có □Không
□ Tốc độ đồng bộ bình thường? □Có □Không

VẤỀN ĐỀ PHÁT HIỆN VÀ HÀNH ĐỘNG:
.................................................................

IT phụ trách ký: .............. Ngày: ..........
```

---

## C. KẾ HOẠCH ỨNG PHÓ MẤT DỮ LIỆU

```
QUY TRÌNH KHÔI PHỤC DỮ LIỆU KHẨN CẤP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Khi xảy ra sự cố (ransomware, hỏng server, xóa nhầm...):

Bước 1 — ĐÁNH GIÁ (30 phút đầu):
□ Xác định phạm vi mất dữ liệu (toàn bộ hay một phần?)
□ Xác định thời điểm dữ liệu còn tốt gần nhất
□ Báo BGĐ ngay nếu mất dữ liệu critical

Bước 2 — CÔ LẬP & NGĂN LAN RỘNG:
□ Ngắt kết nối mạng thiết bị bị nhiễm (ransomware)
□ Không restart máy vội (mất forensic evidence)
□ Chụp ảnh màn hình lỗi làm bằng chứng

Bước 3 — KHÔI PHỤC DỮ LIỆU:
□ Xác định bản backup gần nhất trước sự cố
□ Khôi phục vào môi trường test/server mới trước
□ Xác nhận dữ liệu đầy đủ và đúng
□ Khôi phục vào môi trường production

Bước 4 — PHÂN TÍCH NGUYÊN NHÂN:
□ Tìm hiểu cách tấn công/sự cố xảy ra
□ Vá lỗ hổng trước khi đưa hệ thống trở lại
□ Báo cáo sự cố và bài học kinh nghiệm
```

---

## Định dạng đầu ra

Lập kế hoạch backup, quy trình disaster recovery hoặc checklist kiểm tra theo quy mô IT cụ thể.
