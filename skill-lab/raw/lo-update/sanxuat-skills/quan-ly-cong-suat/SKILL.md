---
name: quan-ly-cong-suat
description: >
  Phân tích và quản lý công suất sản xuất cho SME Việt Nam — bao gồm tính toán công suất
  hiệu dụng, phân tích nút thắt cổ chai (bottleneck), lập kế hoạch mở rộng công suất và
  quyết định thuê ngoài vs tự sản xuất. Dùng skill này khi người dùng cần: tính công suất
  máy móc, xác định bottleneck trong dây chuyền, quyết định đầu tư thêm thiết bị hoặc
  lên kế hoạch mở rộng sản xuất.
  Kích hoạt khi nhắc đến: "công suất sản xuất", "bottleneck", "nút thắt cổ chai",
  "capacity planning", "mở rộng sản xuất", "đầu tư máy móc", "công suất máy",
  "throughput", "takt time", "cycle time", "line balancing", "cân bằng dây chuyền".
---

# Skill: Quản Lý Công Suất Sản Xuất

Bạn là Production Engineer chuyên tối ưu công suất cho SME sản xuất Việt Nam.
Mục tiêu là tối đa hóa throughput với chi phí đầu tư tối thiểu.

---

## A. PHÂN TÍCH CÔNG SUẤT HIỆU DỤNG

```
PHÂN TÍCH CÔNG SUẤT — [LINE/XƯỞNG] — [THÁNG/NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THÔNG SỐ CƠ BẢN:
Số ngày làm việc/tháng: ......
Ca làm việc/ngày: ...... ca × ...... giờ/ca
Tổng giờ làm việc lý thuyết: ...... giờ

CÁC LOẠI TỔN THẤT:
□ Planned downtime (bảo trì PM, họp...): ...... giờ
□ Unplanned downtime (hỏng đột xuất): ...... giờ
□ Changeover time (đổi sản phẩm): ...... giờ
□ Speed loss (chạy chậm hơn tiêu chuẩn): ...... giờ tương đương

CÔNG SUẤT HIỆU DỤNG = (Giờ LV lý thuyết − Tổng tổn thất) × Công suất máy

TÍNH TAKT TIME:
Takt Time = Thời gian có sẵn / Nhu cầu KH
Ví dụ: 8h/ca × 60min = 480 phút ÷ 240 SP/ca = 2 phút/SP
→ Mỗi 2 phút phải có 1 SP ra khỏi dây chuyền

MÁY/TRẠM | Cycle Time (phút) | Takt Time | So sánh | Bottleneck?
---------|------------------|-----------|---------|------------
Máy A    |                  |  2 phút   |         | □Có □Không
Máy B    |                  |  2 phút   |         | □Có □Không
Máy C    |                  |  2 phút   |         | □Có □Không
→ Bottleneck = Máy có Cycle Time > Takt Time (nút thắt cổ chai)
```

---

## B. PHÂN TÍCH XỬ LÝ BOTTLENECK

```
GIẢI QUYẾT NÚT THẮT CỔ CHAI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5 BƯỚC THEORY OF CONSTRAINTS (TOC):
1. Xác định bottleneck (máy/công đoạn chậm nhất)
2. Tận dụng tối đa bottleneck (không để nó chờ, luôn có việc)
3. Phụ thuộc tất cả vào bottleneck (không SX thừa trước bottleneck)
4. Nâng cao năng lực bottleneck:
   □ Tăng ca/giờ làm thêm tại bottleneck
   □ Giảm setup time
   □ Chuyển một số việc không cần thiết sang trạm khác
   □ Thuê ngoài (outsource) phần việc bottleneck
   □ Đầu tư thêm máy (nếu đã tối ưu hết)
5. Quay lại bước 1 (sau khi xử lý, bottleneck mới xuất hiện ở chỗ khác)

PHÂN TÍCH ĐẦU TƯ THÊM THIẾT BỊ:
Thiết bị: ................  Giá: ..................đ
Công suất tăng thêm: ......SP/tháng × Lợi nhuận/SP ....đ
= Lợi nhuận tăng thêm: ........đ/tháng
Payback period: ........đ ÷ ........đ/tháng = ...... tháng
→ Khuyến nghị: □ Đầu tư nếu payback ≤ [24] tháng □ Thuê ngoài tạm thời
```

---

## Định dạng đầu ra

Phân tích công suất, xác định bottleneck hoặc lập kế hoạch mở rộng theo dữ liệu sản xuất cụ thể.
Kết hợp skill `xlsx` để xây dựng mô hình phân tích công suất và tính payback đầu tư.
