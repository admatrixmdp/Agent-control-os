---
name: ops-store-opening-checklist
description: |
  Checklist mở cửa hàng/quán mới cho chuỗi F&B, Retail Việt Nam — từ pre-opening 90 ngày tới ngày khai trương. Dùng skill này khi người dùng yêu cầu: "checklist mở cửa hàng", "store opening", "khai trương quán", "checklist khai trương", "pre-opening F&B", "mở chi nhánh mới", "ramp up new store", "grand opening". Output là Excel timeline + PDF binder + Trello board template.
---

# Store Opening Checklist — Mở Cửa Hàng/Quán Mới

## Mục Tiêu
Đảm bảo cửa hàng mở đúng hẹn, đủ điều kiện vận hành ngày đầu (giấy phép, nhân sự, hàng hoá, marketing) — tránh delay phổ biến 2-4 tuần.

## Khi Nào Dùng
- Setup chi nhánh F&B mới (coffee, lẩu, fast food)
- Mở showroom/retail offline
- Franchise mới
- Mở pop-up store mùa
- Mở rộng cửa hàng có sẵn

## Bước 1: Phân Chia Timeline T-90 / T-60 / T-30 / T-7 / D-Day
**T-90 ngày (3 tháng trước)**:
- Ký hợp đồng thuê
- Nộp đơn xin GPKD
- Brief thiết kế nội thất
- Khảo sát đối thủ trong bán kính 1km
- Lập budget chi tiết

**T-60 ngày (2 tháng)**:
- Hoàn thiện thiết kế 3D
- Đặt máy móc/thiết bị
- Tuyển dụng quản lý + nhân viên chính
- Đăng ký giấy phép VSATTP (F&B), PCCC

**T-30 ngày**:
- Bắt đầu thi công
- Training nhân viên tại cửa hàng cũ
- Đặt nguyên liệu/hàng hoá cho 2 tuần đầu
- Soft launch marketing (teaser)
- Cài đặt POS, thanh toán, wifi, CCTV

**T-7 ngày**:
- Soft opening test với F&B
- Final QC mặt bằng
- Nhập đủ tem nhãn, menu, đồng phục
- Brief lễ khai trương

**D-Day**:
- Khai trương chính thức
- Live stream
- Khuyến mãi opening (BOGO, voucher)

## Bước 2: Phân Nhóm Checklist 8 Mảng
| Mảng | Số task | Ví dụ |
|---|---|---|
| **Pháp lý** | 12 | GPKD, VSATTP, PCCC, treo bảng hiệu, biển báo |
| **Thi công** | 25 | Điện, nước, sàn, trần, biển hiệu, nội thất |
| **Thiết bị** | 18 | Máy POS, máy in bill, máy lạnh, bếp, tủ lạnh |
| **Nhân sự** | 15 | Tuyển, hợp đồng, BHXH, training, lịch ca |
| **Hàng hoá** | 14 | NCC, đơn đầu, kho, công thức, định mức |
| **Marketing** | 16 | Booking influencer, teaser, opening promo, ads |
| **Vận hành** | 20 | SOP, quy trình thu ngân, cleaning, opening/closing |
| **Tài chính** | 10 | Tài khoản, QR thanh toán, đăng ký HĐĐT |

Tổng ~130 task.

## Bước 3: Gán Owner + Due Date + Status
Mỗi task có:
- Task name
- Owner (Manager / Setup team / External vendor)
- Due date (relative to D-Day: D-90, D-60...)
- Dependency (task này blocker cho task khác)
- Status: Not started / In progress / Done / Blocked
- Risk: Low / Medium / High

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Master tracker realtime
- Google Calendar MCP: Tạo event milestone cho team
- Notion MCP: Knowledge base setup cửa hàng theo template
- Slack MCP: Channel #store-<name> chat suốt setup
- Google Drive MCP: Lưu giấy tờ, hồ sơ, ảnh tiến độ
- WebSearch: Tra quy định địa phương (PCCC, sở y tế tỉnh)
- WebFetch: Tải mẫu đơn xin GPKD từ dichvucong.gov.vn

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tạo Trello board template từ checklist
import requests
KEY, TOKEN = "...", "..."
r = requests.post("https://api.trello.com/1/boards/",
    params={"key":KEY,"token":TOKEN,
            "name":"Store Opening - Cua Hang Q1",
            "defaultLists":"false"})
board_id = r.json()["id"]
for phase in ["T-90","T-60","T-30","T-7","D-Day","Post-opening"]:
    requests.post("https://api.trello.com/1/lists",
        params={"key":KEY,"token":TOKEN,
                "name":phase,"idBoard":board_id})
```

## Bước 5: Output Format
- `Store_Opening_Master.xlsx` — bảng 130 task có timeline
- `Store_Opening_Binder.pdf` — bản in mang theo onsite
- `Trello_Template.json` — import vào Trello
- `Opening_Day_Runbook.md` — kịch bản chi tiết D-Day
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/StoreOpening/`

## Checklist Trước Khi Giao
- [ ] Đủ 8 mảng task, không bỏ pháp lý
- [ ] Mỗi task có owner thực tế (không "TBD")
- [ ] Dependency vẽ rõ (task A xong mới đến B)
- [ ] Soft opening trước hard opening ít nhất 3 ngày
- [ ] Có budget tracker đi kèm
- [ ] Có post-opening review (T+7, T+30)
