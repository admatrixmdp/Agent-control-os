---
name: ops-haccp-checklist
description: |
  Checklist HACCP (Hazard Analysis Critical Control Point) cho F&B Việt Nam — xác định mối nguy sinh học/hoá học/vật lý, CCP, monitoring plan. Dùng skill này khi người dùng yêu cầu: "HACCP checklist", "kế hoạch HACCP", "an toàn thực phẩm F&B", "CCP critical control point", "audit HACCP", "GMP SSOP", "ISO 22000", "kế hoạch ATVSTP". Output là Excel HACCP plan + form monitoring + PDF training.
---

# HACCP Checklist — Kế Hoạch An Toàn Thực Phẩm F&B

## Mục Tiêu
Đáp ứng yêu cầu cơ quan quản lý (Cục ATTP, Bộ Y tế) và đối tác xuất khẩu/sàn TMĐT về an toàn thực phẩm — bắt buộc với F&B, restaurant chain, kitchen central.

## Khi Nào Dùng
- Setup nhà máy/bếp central mới
- Đăng ký công bố sản phẩm thực phẩm
- Bán vào AEON, Big C, Co.opmart, Bách Hoá Xanh
- Xuất khẩu Mỹ (FDA), EU
- Audit hàng năm theo ISO 22000

## Bước 1: 7 Nguyên Tắc HACCP
1. **Hazard Analysis** — Phân tích mối nguy (B/H/V)
2. **Identify CCP** — Xác định điểm kiểm soát tới hạn
3. **Critical Limits** — Đặt giới hạn (nhiệt, pH, thời gian, aw)
4. **Monitoring** — Theo dõi CCP
5. **Corrective Action** — Hành động khi lệch chuẩn
6. **Verification** — Kiểm tra hệ thống
7. **Record-keeping** — Lưu hồ sơ

## Bước 2: Hazard Analysis 3 Loại
**Biological** (Sinh học):
- Salmonella, E.coli, Listeria, Bacillus cereus
- Nấm mốc, men, virus

**Chemical** (Hoá học):
- Tồn dư thuốc BVTV (rau củ)
- Kim loại nặng (Pb, Hg, As)
- Aflatoxin (lạc, ngô)
- Phụ gia quá liều
- Allergen (sữa, đậu phộng, gluten)

**Physical** (Vật lý):
- Mảnh kính, kim loại, nhựa
- Tóc, móng tay
- Côn trùng

Mỗi mối nguy chấm:
- Severity (1-3): nhẹ/vừa/nặng
- Likelihood (1-3): hiếm/thỉnh thoảng/thường
- Risk = S × L → S×L ≥ 4 = SIGNIFICANT cần kiểm soát

## Bước 3: Xác Định CCP & Critical Limits
Dùng Decision Tree CODEX:
- Q1: Có biện pháp kiểm soát mối nguy?
- Q2: Bước này loại bỏ/giảm mối nguy?
- Q3: Có thể nhiễm trong bước sau?
- Q4: Bước sau có loại bỏ được không?

CCP điển hình F&B:
| Bước | CCP | Critical Limit | Monitoring |
|---|---|---|---|
| Nấu | Nhiệt độ tâm | ≥ 75°C × 30s | Nhiệt kế đầu mũi, mỗi mẻ |
| Làm nguội | Time-temp | 60°C→21°C trong 2h | Logger |
| Bảo quản lạnh | Nhiệt tủ | ≤ 4°C | 2 lần/ca |
| Đóng gói kim loại | Metal detector | Fe ≥ 1.5mm | 100% sản phẩm |
| Tiệt trùng UHT | F-value | F0 ≥ 6 | Datalogger |

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: Log monitoring CCP realtime
- Google Drive MCP: Lưu COA, CoC từ NCC
- Slack MCP: Cảnh báo khi CCP out-of-spec
- Notion MCP: Database mối nguy, CCP, action
- Gmail MCP: Gửi báo cáo HACCP cho QA Manager
- WebSearch: Tra quy định Cục ATTP, FSSAI, FDA mới nhất
- WebFetch: Tải biểu mẫu HACCP từ vfa.gov.vn

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Đọc nhiệt từ IoT logger (vd: Testo Saveris)
import requests, pandas as pd
r = requests.get("https://api.testo.com/v1/measurements",
    headers={"Authorization":"Bearer ..."},
    params={"sensor_id":"FRIDGE-01","from":"2026-05-28T00:00",
            "to":"2026-05-28T23:59"})
df = pd.DataFrame(r.json()["data"])
violations = df[df["temp_c"] > 4]
if not violations.empty:
    # Tạo CAR (corrective action report)
    print(f"OOS: {len(violations)} lần > 4°C")
    requests.post("https://hooks.slack.com/...",
        json={"text":f":warning: Tủ FRIDGE-01 OOS {len(violations)} lần"})
```

## Bước 5: Output Format
- `HACCP_Plan.xlsx` — Hazard analysis + CCP table + critical limits
- `HACCP_Monitoring_Forms/` — folder các form ghi nhật ký
- `HACCP_Training.pdf` — slide training cho nhân viên
- `HACCP_Verification.md` — kế hoạch verify hệ thống hàng quý
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/outputs/HACCP/`

## Checklist Trước Khi Giao
- [ ] Mọi mối nguy có severity + likelihood
- [ ] CCP xác định bằng Decision Tree, không tự ý
- [ ] Critical limit có nguồn (TCVN, FDA, Codex)
- [ ] Monitoring có tần suất + người thực hiện
- [ ] Corrective Action có hành động cụ thể
- [ ] Lưu hồ sơ tối thiểu 2 năm + truy xuất nguồn gốc
