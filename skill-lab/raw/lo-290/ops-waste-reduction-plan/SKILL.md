---
name: ops-waste-reduction-plan
description: |
  Lập kế hoạch giảm lãng phí theo 8 Wastes (TIMWOODS) của Lean Manufacturing — phát hiện, đo lường, đề xuất Kaizen. Dùng skill này khi người dùng yêu cầu: "giảm lãng phí sản xuất", "8 wastes Lean", "TIMWOODS", "Muda analysis", "Kaizen plan", "loại bỏ NVA", "lean waste reduction", "Gemba walk". Output là Excel waste log + HTML heatmap + danh sách Kaizen với ROI.
---

# Waste Reduction Plan — Giảm 8 Lãng Phí Theo Lean

## Mục Tiêu
Phát hiện và loại bỏ 8 dạng lãng phí (Muda) trong toàn bộ value stream — giảm chi phí, thời gian, năng lượng mà không cần đầu tư lớn.

## Khi Nào Dùng
- Triển khai Lean lần đầu
- Gemba walk định kỳ (weekly)
- Trước khi đầu tư tự động hóa
- Năm tài chính giảm budget
- Khi margin co lại do cạnh tranh

## Bước 1: Nắm Vững 8 Wastes (TIMWOODS)
| # | Tên | Ví dụ thực tế |
|---|---|---|
| 1 | **T**ransport | Vận chuyển NVL giữa 2 nhà xưởng cách 500m |
| 2 | **I**nventory | NVL tồn 3 tháng, hàng FG quá đát |
| 3 | **M**otion | Công nhân với tay quá xa, cúi gập lưng nhiều lần |
| 4 | **W**aiting | Chờ phê duyệt, chờ phụ tùng, chờ kế tiếp |
| 5 | **O**verproduction | Sản xuất nhiều hơn đơn hàng "phòng hờ" |
| 6 | **O**verprocessing | Đóng gói 3 lớp khi 1 lớp đã đủ |
| 7 | **D**efects | Lỗi rework, NG scrap |
| 8 | **S**kills (mới) | Người giỏi làm việc photocopy |

## Bước 2: Gemba Walk Quan Sát Thực Tế
Ra hiện trường 60-90 phút, ghi:
- Khu vực
- Loại waste (TIMWOODS)
- Mô tả cụ thể (số liệu)
- Tần suất (mỗi giờ/ngày)
- Ước lượng cost (VND/tháng)

Template hàng:
```
Khu: Line A, Công đoạn: Lắp ráp
Waste: Motion - Công nhân lấy ốc vít ở thùng dưới chân, cúi 80 lần/ca
Cost: 80 lần × 8s = 640s/ca × 26 ngày × 3 ca = 14h/tháng × 50k = 700k VND/tháng
Kaizen: Đặt ốc vít trong khay treo ngang tầm tay
```

## Bước 3: Prioritize Kaizen
Ma trận Impact × Effort:
- Quick win (High impact, Low effort): làm ngay
- Major project (High, High): plan
- Fill-in (Low, Low): khi rảnh
- Thankless (Low, High): bỏ

Mỗi Kaizen có:
- Tên + waste type
- Cost lãng phí hiện tại
- Đề xuất (5W2H)
- Ước tính tiết kiệm
- Owner + Due date
- Trạng thái

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Waste log realtime, dashboard 8 wastes
- Google Drive MCP: Lưu ảnh/video trước-sau Kaizen
- Slack MCP: Channel #kaizen mỗi sáng share 1 waste tìm thấy
- Notion MCP: Kaizen tracker với hình ảnh và score
- WebSearch: Tham khảo case Lean của Vinamilk, THACO, Vinfast
- WebFetch: Tải template Lean Tour audit từ leanenterprise.org

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tự sinh dashboard 8 wastes từ Sheets
import gspread, plotly.express as px
gc = gspread.service_account()
df = pd.DataFrame(gc.open("WasteLog").sheet1.get_all_records())
agg = df.groupby("Waste_Type")["Cost_VND"].sum().reset_index()
fig = px.treemap(agg, path=["Waste_Type"], values="Cost_VND",
    title="8 Wastes — Chi phí tháng này")
fig.write_html("waste_heatmap.html")
```

## Bước 5: Output Format
- `Waste_Log_<month>.xlsx` — log hàng ngày + tổng hợp
- `Kaizen_Board.xlsx` — Impact-Effort matrix + status
- `Waste_Heatmap.html` — treemap theo loại waste
- `Gemba_Photos/` — ảnh trước/sau từng Kaizen
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/Waste/`

## Checklist Trước Khi Giao
- [ ] Mỗi waste có data số (không chỉ "nhiều")
- [ ] Cost VND tính ra được
- [ ] Quick win < 1 tuần triển khai
- [ ] Có ít nhất 1 Kaizen cho mỗi loại waste TIMWOODS
- [ ] Có ảnh before/after để tracking
- [ ] Báo cáo cho COO hàng tuần
