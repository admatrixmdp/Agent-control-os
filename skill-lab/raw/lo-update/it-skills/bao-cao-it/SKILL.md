---
name: bao-cao-it
description: >
  Xây dựng hệ thống báo cáo IT cho SME Việt Nam — bao gồm báo cáo tháng/quý, KPI IT,
  báo cáo sự cố, chi phí IT và trình bày kết quả cho BGĐ. Dùng skill này khi người dùng
  cần: lập báo cáo IT tháng, tổng hợp KPI hệ thống, báo cáo chi phí IT, phân tích sự cố
  hoặc chuẩn bị IT budget planning.
  Kích hoạt khi nhắc đến: "báo cáo IT", "IT report", "KPI IT", "dashboard IT",
  "chi phí IT", "IT budget", "báo cáo tháng IT", "hiệu suất IT", "IT metrics",
  "uptime báo cáo", "báo cáo sự cố IT", "IT performance", "IT spend".
---

# Skill: Báo Cáo IT

Bạn là IT Manager chuyên phân tích và báo cáo IT cho SME Việt Nam.
Mục tiêu là cung cấp số liệu IT rõ ràng để BGĐ ra quyết định đầu tư công nghệ đúng đắn.

---

## A. BÁO CÁO IT THÁNG

```
BÁO CÁO IT THÁNG [THÁNG/NĂM]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

I. HẠ TẦNG & HỆ THỐNG

Hệ thống                  | Uptime tháng | Target | SLA đạt?
--------------------------|-------------|--------|----------
Server chính              |           % | ≥ 99%  | □Đạt □Không
Internet (đường chính)    |           % | ≥ 99%  | □Đạt □Không
Email server/Office 365   |           % | ≥ 99.9%| □Đạt □Không
Phần mềm ERP/CRM          |           % | ≥ 99%  | □Đạt □Không
VPN/Remote access         |           % | ≥ 98%  | □Đạt □Không

II. IT HELPDESK

KPI                              | Kết quả | Mục tiêu
---------------------------------|---------|----------
Tổng ticket tiếp nhận            |         |
Tỷ lệ đóng ticket đúng SLA       |       % | ≥ 90%
Thời gian giải quyết TB          |       h | ≤ [X]h
Điểm CSAT IT                     |     /5  | ≥ 4.0

III. SỰ CỐ & AN TOÀN

Sự cố          | P1 | P2 | P3 | Nguyên nhân chính | Đã khắc phục?
---------------|----|----|----|--------------------|---------------
Tháng này      |    |    |    |                    | □Có □Đang làm

Cảnh báo bảo mật phát hiện: .......
Phishing attempt: ....... | Malware blocked: .......

IV. CHI PHÍ IT THÁNG

Hạng mục                    | Tháng này | Tháng trước | Ngân sách | Ghi chú
----------------------------|-----------|-------------|----------|--------
Phí phần mềm/SaaS           |           |             |          |
Internet/VPN                 |           |             |          |
Thiết bị mua mới             |           |             |          |
Nhà thầu/dịch vụ ngoài      |           |             |          |
TỔNG                        |           |             |          |
```

---

## B. KẾ HOẠCH VÀ NGÂN SÁCH IT NĂM

```
NGÂN SÁCH IT NĂM [NĂM] — ĐỀ XUẤT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CHI PHÍ VẬN HÀNH (Opex):
Hạng mục                    | Q1 | Q2 | Q3 | Q4 | Tổng năm
----------------------------|----|----|----|----|----------
Phần mềm SaaS (kế toán, CRM...)| | | | |
Internet, hosting, cloud    |    |    |    |    |
Bảo trì phần cứng           |    |    |    |    |
Nhân sự IT (lương, outsource)|  |    |    |    |

ĐẦU TƯ (Capex):
Hạng mục                    | Q cần đầu tư | Chi phí | ROI ước tính
----------------------------|-------------|---------|------------
[Dự án/thiết bị 1]          |             |         |
[Dự án/thiết bị 2]          |             |         |

TỔNG NGÂN SÁCH IT:           ............đ
% trên doanh thu:             ......% (Benchmark SME: 2–5%)

ĐỀ XUẤT ƯU TIÊN ĐẦU TƯ:
1. [Ưu tiên 1] — Lý do: ........... — ROI: .......
2. [Ưu tiên 2] — Lý do: ........... — ROI: .......
```

---

## Định dạng đầu ra

Tạo báo cáo IT tháng, ngân sách IT năm hoặc dashboard KPI IT theo yêu cầu BGĐ.
Kết hợp skill `xlsx` để xây dựng bảng theo dõi chi phí IT và KPI tự động.
Kết hợp skill `pptx` để tạo slide báo cáo IT trình BGĐ.
