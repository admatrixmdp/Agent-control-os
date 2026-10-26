---
name: legal-trademark-search
description: |
  Tra cứu nhãn hiệu trên Cục Sở hữu trí tuệ Việt Nam (IPVN / NOIP) và WIPO Global Brand Database để kiểm tra khả năng đăng ký nhãn hiệu, tránh trùng/tương tự gây nhầm lẫn theo Luật SHTT 2005 sửa đổi 2022. Kích hoạt khi người dùng nói: "tra cứu nhãn hiệu", "check trademark VN", "tra IPVN", "kiểm tra logo có đăng ký được không", "tra WIPO", "trademark search", "tra nhãn hiệu trùng", "check brand availability", "tra logo trên Cục SHTT", "kiểm tra nhãn hiệu Madrid". Output là báo cáo PDF: nhãn hiệu trùng/tương tự + đánh giá khả năng cấp + đề xuất Nice Class.
---

# Tra Cứu Nhãn Hiệu IPVN + WIPO

## Mục Tiêu
Trước khi tốn 1-3 triệu VND/đơn nộp Cục SHTT + chờ 18-24 tháng, kiểm tra trước nhãn hiệu (chữ + hình) có khả năng được cấp văn bằng bảo hộ không. Tham chiếu Luật SHTT 2005 (sửa đổi 2022) Điều 72-74 + Bảng phân loại Nice 12th Edition.

## Khi Nào Dùng
- Trước khi đăng ký thương hiệu mới (sản phẩm / dịch vụ / công ty)
- Trước khi rebrand
- Trước khi mở rộng sang ngành hàng mới (đăng ký thêm Nice Class)
- Trước khi launch ở nước ngoài (Madrid System)
- Khi nhận thông báo phản đối / huỷ văn bằng

## Bước 1: Chuẩn Hoá Đối Tượng Tra Cứu
- Tên nhãn hiệu (chữ): chuẩn hoá viết hoa, dấu, font
- Logo (hình): mô tả thành phần hình (rồng, ngôi sao, hình học...)
- Ngành nghề → mapping sang Nice Class (45 nhóm)
- Ví dụ: "TAKI Academy" — đào tạo → Nice Class 41
- "Bún bò Huế" — không đăng ký được vì chỉ dẫn địa lý + mô tả sản phẩm (Đ.74)

## Bước 2: Tra Cứu Trên IPVN
Truy cập `wipopublish.ipvietnam.gov.vn` (IPLib) hoặc `iplib.noip.gov.vn`:
- Search by mark name (đối sánh chính xác + tương tự)
- Search by Nice Class
- Search by applicant name (tránh trùng chủ đơn cũ)
- Lọc theo trạng thái: Đang xử lý / Cấp văn bằng / Hết hiệu lực / Bị huỷ
Lưu ý cách viết khác (ko dấu, viết tắt, phiên âm tiếng Anh).

## Bước 3: Tra Cứu Trên WIPO Global Brand Database
Truy cập `branddb.wipo.int`:
- Search nhãn hiệu trên 84 cơ sở dữ liệu các nước
- Kiểm tra nhãn hiệu đã đăng ký Madrid (vào VN) chưa
- Nếu định mở sang Mỹ → tra USPTO TESS (`tmsearch.uspto.gov`)
- Nếu định mở sang EU → tra EUIPO eSearch (`euipo.europa.eu`)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebFetch: tra IPVN IPLib và WIPO Brand DB trực tiếp
- Google Drive MCP: lưu báo cáo tra cứu + screenshot
- Google Sheets MCP: cập nhật bảng nhãn hiệu công ty đang theo dõi
- Gmail MCP: gửi báo cáo cho luật sư đại diện SHTT
- WebSearch: tra Google Image với reverse search logo

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# WIPO Global Brand Database API (free tier)
import requests

def search_wipo(brand_name, nice_class=None):
    url = "https://www3.wipo.int/branddb/en/quicksearch.jsp"
    params = {"q": brand_name, "asStructure": '{"_id":"brand"}'}
    if nice_class:
        params["niceClass"] = nice_class
    r = requests.get(url, params=params, timeout=30)
    return r.json()

# IPVN không có public API — dùng Selenium scrape IPLib
from selenium import webdriver
def search_ipvn(mark, nice_class):
    driver = webdriver.Chrome()
    driver.get("http://wipopublish.ipvietnam.gov.vn/wopublish-search/public/trademarks?1&query=*:*")
    # input mark + filter Nice Class + crawl pagination
    # parse table: Số đơn / Ngày nộp / Chủ đơn / Trạng thái
    # Trả về list dict
    return results

results_vn = search_ipvn("TAKI ACADEMY", 41)
results_wipo = search_wipo("TAKI ACADEMY", 41)
```

## Bước 5: Output Format
- File `tracuu_NhanHieu_<ten>_<yyyymmdd>.pdf` báo cáo gồm:
  - Trang 1: Tóm tắt — khả năng cấp (CAO / TRUNG BÌNH / THẤP / KHÔNG NÊN)
  - Trang 2-3: Bảng nhãn hiệu trùng/tương tự trên IPVN (mark / chủ đơn / Nice / trạng thái)
  - Trang 4: Kết quả WIPO + USPTO/EUIPO nếu có
  - Trang 5: Đề xuất Nice Class + chiến lược đăng ký + chi phí dự kiến
  - Trang 6: Mẫu Tờ khai đăng ký nhãn hiệu (Mẫu 04/SHCN của Cục SHTT)
- File `tracuu_NhanHieu.xlsx`: dữ liệu thô để chia sẻ team Pháp chế
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/trademark-search/`

## Checklist Trước Khi Giao
- [ ] Đã tra cứu đầy đủ trên IPVN + WIPO + ít nhất 1 nước target
- [ ] Đã chuẩn hoá tên (viết hoa, không dấu, phiên âm)
- [ ] Đã chọn đúng Nice Class theo ngành nghề
- [ ] Đã đối chiếu Đ.72-74 Luật SHTT (dấu hiệu không được bảo hộ)
- [ ] Có đánh giá khả năng cấp văn bằng (CAO/TRUNG/THẤP)
- [ ] Có đề xuất chiến lược: nộp đơn / chỉnh sửa logo / đổi tên
- [ ] Có dự toán chi phí (lệ phí Cục + phí đại diện)
- [ ] Có khuyến cáo về Madrid System nếu mở quốc tế
