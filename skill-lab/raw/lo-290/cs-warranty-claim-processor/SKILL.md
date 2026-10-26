---
name: cs-warranty-claim-processor
description: |
  Quy trình xử lý yêu cầu bảo hành — form thu thập, SLA, kiểm tra điều kiện, route về kỹ thuật/kho, đặt linh kiện, theo dõi đến khi giao lại. Dùng skill này khi người dùng yêu cầu: "xử lý bảo hành", "warranty claim", "quy trình bảo hành", "form yêu cầu bảo hành", "SLA bảo hành", "tracking warranty", "parts replacement", "RMA process". Output là form HTML + workflow + Excel tracker.
---

# CS Warranty Claim Processor

## Mục Tiêu
Chuẩn hoá quy trình bảo hành end-to-end từ lúc KH gửi yêu cầu đến khi nhận hàng đã sửa — đảm bảo SLA, không thất lạc sản phẩm, KH biết trạng thái real-time, agent không phải gõ tay nhiều lần.

## Khi Nào Dùng
- Doanh nghiệp bán điện tử / gia dụng / điện máy
- Bảo hành lộn xộn, KH gọi không biết hàng ở đâu
- KH khiếu nại vì bảo hành quá lâu
- Mở rộng nhiều TT bảo hành / partner
- Setup mới hoặc audit lại process

## Bước 1: Form Yêu Cầu Bảo Hành Chuẩn
Field bắt buộc:
- Họ tên + SĐT + email
- Mã đơn / số seri sản phẩm
- Ngày mua
- Mô tả lỗi (text + ảnh + video tùy)
- Đã thử gì
- Phương thức gửi: trực tiếp / ship / nhân viên đến

Validation:
- Auto check số seri có trong DB không
- Auto tính còn bảo hành không (mua < N tháng?)
- Yêu cầu ảnh nếu lỗi vật lý

## Bước 2: SLA & Workflow 5 Bước
| Bước | Action | SLA |
|---|---|---|
| 1 — Receive | Tạo ticket, gửi mã RMA | < 1h |
| 2 — Diagnose | Kỹ thuật check & quote | 1-2 ngày |
| 3 — Quote & Approve | Báo KH chi phí (nếu out-of-warranty) | < 24h chờ KH OK |
| 4 — Repair | Sửa / thay linh kiện | 3-7 ngày |
| 5 — Return | Giao lại + test | 1-2 ngày |

Tổng: 7-14 ngày tùy phức tạp.

KH nhận update mỗi bước qua SMS/Zalo + portal track theo mã RMA.

## Bước 3: Kiểm Tra Điều Kiện Bảo Hành
**Trong bảo hành** (free):
- Lỗi nhà sản xuất
- Còn hạn (theo seri)
- Còn tem niêm phong

**Out-of-warranty** (charged):
- Hết hạn
- Lỗi do người dùng (rơi, vô nước)
- Tem rách / đã can thiệp

→ Báo giá rõ trước khi sửa, KH approve mới làm.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets: master RMA tracker
- Gmail MCP: gửi update tự động mỗi bước
- Slack MCP: alert kỹ thuật khi có RMA mới + alert kho khi cần linh kiện
- Google Calendar MCP: book lịch hẹn KH đến lấy hàng
- WebSearch: best practice RMA Apple / Samsung
- WebFetch: tham khảo policy bảo hành đối thủ

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tạo RMA + push thông báo Zalo
import requests, hashlib
ZALO_TOKEN = "..."
def create_rma(form):
    if not check_warranty(form["serial"]):
        return {"error": "Hết bảo hành"}
    rma_id = "RMA-" + hashlib.md5(form["serial"].encode()).hexdigest()[:8]
    save_to_db(rma_id, form)
    # Notify Zalo
    requests.post("https://openapi.zalo.me/v2.0/oa/message",
        headers={"access_token": ZALO_TOKEN},
        json={"recipient": {"user_id": form["zalo_id"]},
              "message": {"text": f"Em đã tiếp nhận yêu cầu bảo hành {rma_id}. Theo dõi tại link..."}})
    return {"rma_id": rma_id}
```

## Bước 5: Output Format
- **HTML form** yêu cầu bảo hành (KH submit)
- **Excel `RMA_Tracker.xlsx`**:
  - Sheet RMA list (đang xử lý)
  - Sheet Parts (linh kiện cần đặt)
  - Sheet SLA report
- **Email templates** mỗi bước: nhận, chẩn đoán, báo giá, sửa xong
- **Markdown SOP** cho team kỹ thuật
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-warranty-claim-processor/output/`

## Checklist Trước Khi Giao
- [ ] Form thu thập đủ thông tin + validation
- [ ] 5 bước workflow có SLA
- [ ] KH track được trạng thái real-time
- [ ] Phân biệt rõ in/out warranty
- [ ] Có process đặt linh kiện chủ động
- [ ] Đo lường: tỷ lệ on-time, complaint, % out-of-warranty
