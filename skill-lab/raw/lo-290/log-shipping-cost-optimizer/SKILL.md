---
name: log-shipping-cost-optimizer
description: |
  Tối ưu cước vận chuyển nội địa Việt Nam (Viettel Post, GHN, GHTK, J&T, Best, NinjaVan) và quốc tế (DHL, FedEx, UPS, sea freight) — so sánh giá, lead time, COD, đặc thù từng tuyến để chọn carrier tối ưu cho từng đơn / từng vùng. Kích hoạt khi người dùng nói: "tối ưu cước ship", "so sánh GHN GHTK Viettel Post", "tính cước vận chuyển", "shipping rate optimizer", "tối ưu logistics", "tính cước nội địa", "cước quốc tế DHL FedEx", "shipping cost comparison", "giảm cước ship", "best carrier per zone". Output là Excel rule engine + dashboard PDF tiết kiệm cước + script tự gọi API carrier.
---

# Shipping Cost Optimizer — Tối Ưu Cước Vận Chuyển

## Mục Tiêu
Giúp doanh nghiệp TMĐT / sản xuất Việt Nam tiết kiệm 10-25% cước vận chuyển bằng cách chọn đúng carrier theo trọng lượng, kích thước, tuyến đường, dịch vụ. So sánh real-time + áp rule engine tự động.

## Khi Nào Dùng
- TMĐT vận hành >100 đơn/ngày, cần optimize
- Doanh nghiệp đa kho cần routing tối ưu
- Mở rộng giao hàng toàn quốc / quốc tế
- Đàm phán giá hợp đồng với carrier hàng năm
- Audit chi phí logistics phát hiện rò rỉ

## Bước 1: Thu Thập Bảng Giá + Đặc Thù 7 Carrier
**Nội địa VN:**
- **GHN**: nhanh ở TP lớn, COD tốt, giá trung
- **GHTK**: rẻ nhất ở Bắc, COD nhanh ≤24h Hà Nội/HCM
- **Viettel Post**: phủ rộng huyện xã, đặc biệt vùng sâu
- **J&T Express**: rẻ tuyến dài, phù hợp shopee/tiktok shop
- **Best Express**: cạnh tranh giá, tuyến HN-HCM tốt
- **NinjaVan**: chuyên thương hiệu lớn, lead time ổn định
- **Ahamove / Lalamove**: same-day nội thành

**Quốc tế:**
- **DHL Express**: 1-3 ngày, đắt
- **FedEx**: 2-4 ngày, ổn định Mỹ
- **UPS**: tốt cho EU
- **EMS Bưu điện**: rẻ nhất, 5-15 ngày
- **Sea freight (FCL/LCL)**: cho B2B, lead time 20-40 ngày

## Bước 2: Build Rule Engine Chọn Carrier
Theo từng tổ hợp:
| Trọng lượng | Vùng | Loại hàng | COD? | Carrier ưu tiên |
|---|---|---|---|---|
| ≤0.5kg | Nội thành HN/HCM | thường | Có | GHTK |
| 0.5-2kg | Tỉnh ngoài | thường | Có | GHN |
| 2-5kg | Toàn quốc | thường | Không | J&T |
| >5kg | Huyện xã | cồng kềnh | Có | Viettel Post |
| Hoả tốc | Nội thành | nhỏ | Không | Ahamove |
| QT ≤2kg | EU/Mỹ | gấp | Không | DHL |
| QT >5kg | EU/Mỹ | không gấp | Không | EMS |

## Bước 3: Tính TCO Logistics (Total Cost of Ownership)
Không chỉ cước mà tổng:
- Cước cơ bản
- Phí COD (1-1.5%)
- Phí hoàn hàng (50-70% cước đi)
- Phí bảo hiểm (0.5% giá trị)
- Phí quá khổ / quá tải
- Tỷ lệ thất lạc + thời gian khiếu nại
- Chiết khấu volume (>1000 đơn/tháng giảm 10-15%)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: dashboard cost monitoring + alert
- Google Drive MCP: lưu rule engine + hợp đồng carrier
- Notion MCP: vendor logistics database
- Gmail MCP: gửi báo cáo tiết kiệm cước tuần/tháng cho CFO
- WebFetch: tra biểu giá mới nhất từ ghn.vn, ghtk.vn, viettelpost.vn, jtexpress.vn
- WebSearch: tin tức điều chỉnh phụ phí xăng dầu / mùa cao điểm

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Gọi API Viettel Post / GHN / GHTK để so sánh real-time
import requests

def get_ghn_fee(from_district, to_district, weight_gram, value):
    url = "https://online-gateway.ghn.vn/shiip/public-api/v2/shipping-order/fee"
    headers = {"Token": "YOUR_GHN_TOKEN", "ShopId": "YOUR_SHOP_ID"}
    payload = {
        "from_district_id": from_district,
        "to_district_id": to_district,
        "weight": weight_gram,
        "insurance_value": value,
        "service_type_id": 2  # 2 = thường, 5 = nhanh
    }
    r = requests.post(url, json=payload, headers=headers).json()
    return r["data"]["total"]

def get_ghtk_fee(from_district, to_district, weight, value):
    url = "https://services.giaohangtietkiem.vn/services/shipment/fee"
    headers = {"Token": "YOUR_GHTK_TOKEN"}
    params = {"pick_district": from_district, "district": to_district, "weight": weight, "value": value}
    r = requests.get(url, headers=headers, params=params).json()
    return r["fee"]["fee"]

def get_vtp_fee(...):  # tương tự partner.viettelpost.vn
    pass

def choose_cheapest(order):
    fees = {
        "GHN": get_ghn_fee(...),
        "GHTK": get_ghtk_fee(...),
        "VTP": get_vtp_fee(...)
    }
    return min(fees, key=fees.get), fees
```

## Bước 5: Output Format
- File `shipping_rule_engine.xlsx`: bảng rule + công thức quyết định carrier
- File `cost_comparison_dashboard.pdf`: 5-7 trang
  - Trang 1: KPI tổng — Tiết kiệm bao nhiêu %
  - Trang 2: So sánh carrier theo zone
  - Trang 3: Top tuyến chi phí cao bất thường
  - Trang 4: Phân tích phụ phí
  - Trang 5: Đề xuất đàm phán giá năm tới
- File `carrier_api_integration.py`: script gọi API real-time tích hợp vào ERP/OMS
- File `monthly_savings_report.xlsx`: theo dõi tiết kiệm hàng tháng
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/shipping-optimizer/`

## Checklist Trước Khi Giao
- [ ] Có bảng giá cập nhật ≤30 ngày của ≥5 carrier
- [ ] Rule engine bao phủ ≥10 zone + 5 mức trọng lượng
- [ ] TCO bao gồm phí COD + hoàn hàng + bảo hiểm
- [ ] Có script gọi API real-time ít nhất GHN + GHTK
- [ ] Dashboard có baseline để đo tiết kiệm (% so với tháng trước)
- [ ] Có cảnh báo tuyến giá tăng đột biến >15%
- [ ] Có roadmap đàm phán năm tới + volume commitment
- [ ] Đã chia sẻ rule engine với team OMS/CSKH
