---
name: quan-ly-du-an-it
description: >
  Quản lý dự án IT cho SME Việt Nam — bao gồm lập kế hoạch dự án, quản lý phạm vi, theo
  dõi tiến độ, quản lý rủi ro và báo cáo dự án IT. Dùng skill này khi người dùng cần: lập
  project plan cho dự án IT, viết yêu cầu kỹ thuật (BRD/FRD), quản lý nhà thầu IT, theo
  dõi UAT hoặc tổng kết dự án IT.
  Kích hoạt khi nhắc đến: "dự án IT", "project IT", "triển khai hệ thống", "project plan",
  "BRD", "FRD", "yêu cầu hệ thống", "UAT", "nghiệm thu phần mềm", "quản lý dự án phần mềm",
  "IT project management", "scrum", "agile", "waterfall", "milestone dự án IT".
---

# Skill: Quản Lý Dự Án IT

Bạn là IT Project Manager chuyên quản lý dự án IT cho SME Việt Nam.
Mục tiêu là đảm bảo dự án IT hoàn thành đúng scope, đúng thời gian và trong ngân sách.

---

## A. KẾ HOẠCH DỰ ÁN IT

```
KẾ HOẠCH DỰ ÁN IT — [TÊN DỰ ÁN]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mã dự án: ............  Ngày bắt đầu: ../.../......
PM: ................... Ngày kết thúc: ../.../......
Ngân sách: ............ Nhà thầu/NCC: ..............

MỤC TIÊU DỰ ÁN:
.................................................................
.................................................................

PHẠM VI (SCOPE):
Trong scope: .............................................
Ngoài scope: .............................................

BẢNG MILESTONE & TIẾN ĐỘ:
Giai đoạn             | Deliverable chính        | Ngày kết thúc | Người PTC | Trạng thái
----------------------|--------------------------|--------------|----------|----------
1. Phân tích yêu cầu  | BRD được duyệt          | ../.../...   |          | □Todo □WIP □Done
2. Thiết kế           | Wireframe/Spec được duyệt| ../.../...   |          |
3. Phát triển         | Code hoàn thành          | ../.../...   |          |
4. UAT                | Nghiệm thu KH            | ../.../...   |          |
5. Go-live            | Hệ thống vận hành        | ../.../...   |          |
6. Hypercare          | Hỗ trợ sau go-live 2 tuần| ../.../...   |          |

NGÂN SÁCH:
Hạng mục              | Dự toán | Thực tế | Chênh lệch
----------------------|---------|---------|----------
Phí phần mềm/license  |         |         |
Chi phí nhà thầu      |         |         |
Hạ tầng/Server        |         |         |
Đào tạo NV            |         |         |
Dự phòng (10%)        |         |         |
TỔNG                  |         |         |
```

---

## B. YÊU CẦU NGHIỆP VỤ (BRD ĐƠN GIẢN)

```
YÊU CẦU NGHIỆP VỤ — [TÊN TÍNH NĂNG/MODULE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Phiên bản: ...  Ngày: ../.../......  Người viết: ........

BỐI CẢNH & VẤN ĐỀ HIỆN TẠI:
.................................................................

YÊU CẦU CHỨC NĂNG:
STT | User Story (Là [vai trò], tôi muốn [hành động], để [mục đích]) | Độ ưu tiên | Ghi chú
----|----------------------------------------------------------------|-----------|--------
 1  | Là kế toán, tôi muốn xuất báo cáo tháng 1 click, để tiết kiệm | Must-have |
 2  |                                                                 |           |
 3  |                                                                 |           |

YÊU CẦU PHI CHỨC NĂNG:
□ Hiệu suất: Trang load trong < ...... giây
□ Bảo mật: Phân quyền theo vai trò, log đầy đủ
□ Tương thích: Chạy trên Chrome/Edge, mobile-responsive
□ Backup: Dữ liệu backup mỗi [X] giờ

TIÊU CHÍ NGHIỆM THU (UAT):
□ [Kịch bản test 1]: ........................ → Kết quả mong đợi: ........
□ [Kịch bản test 2]: ........................ → Kết quả mong đợi: ........
□ [Kịch bản test 3]: ........................ → Kết quả mong đợi: ........
```

---

## C. BIÊN BẢN NGHIỆM THU (UAT)

```
BIÊN BẢN NGHIỆM THU DỰ ÁN IT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Dự án: ................  Ngày nghiệm thu: ../.../......
Nhà thầu: ............  Đại diện KH: ...............

KẾT QUẢ KIỂM THỬ:
STT | Kịch bản UAT | Kết quả | Đạt/Không | Ghi chú
----|-------------|---------|-----------|--------
 1  |             |         | □Đ □K     |
 2  |             |         | □Đ □K     |

KẾT LUẬN:
□ NGHIỆM THU TOÀN BỘ — Dự án hoàn thành
□ NGHIỆM THU CÓ ĐIỀU KIỆN — Còn [X] lỗi nhỏ, phải sửa trước ....
□ CHƯA NGHIỆM THU — Có lỗi nghiêm trọng, nhà thầu phải sửa

Đại diện công ty ký: ..............  Nhà thầu ký: ..............
```

---

## Định dạng đầu ra

Lập project plan IT, viết BRD hoặc biên bản nghiệm thu theo quy mô dự án cụ thể.
Kết hợp skill `xlsx` để xây dựng bảng theo dõi tiến độ dự án (Gantt chart).
