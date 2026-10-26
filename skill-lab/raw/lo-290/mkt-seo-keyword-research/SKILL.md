---
name: mkt-seo-keyword-research
description: |
  Nghiên cứu keyword SEO và phân cluster topic cho website doanh nghiệp Việt Nam. Tự động sinh danh sách 100-300 keyword theo intent (informational/commercial/transactional), gom thành topic clusters và đề xuất content map. Kích hoạt khi người dùng nói: "nghiên cứu từ khóa SEO", "keyword research", "tìm keyword SEO", "cluster topic", "lập kế hoạch SEO", "tìm từ khóa cho website", "phân tích keyword", "SEO topical map". Output là Excel có 4 sheet (Seed, Long-tail, Cluster, Content Map).
---

# Nghiên Cứu Keyword SEO + Cluster Topic

## Mục Tiêu
Giúp team SEO/Content xây dựng kế hoạch nội dung dựa trên dữ liệu thay vì cảm tính. Trong 30 phút có thể tạo ra danh sách 200+ keyword đã phân loại theo intent, gom topic cluster, và bản đồ content cho 3 tháng tới.

## Khi Nào Dùng
- Khởi tạo SEO cho website mới
- Mở rộng sang ngách mới
- Cần kế hoạch blog 30-90 ngày
- Audit lại keyword cũ và tìm gap
- Chuẩn bị brief content cho cộng tác viên

## Bước 1: Xác Định Seed Keyword
Hỏi: ngành, sản phẩm/dịch vụ, vùng địa lý (Việt Nam/HCM/HN), đối thủ chính (3-5 domain).
Sinh 20-30 seed keyword chính (1-2 từ), ví dụ "máy lọc nước", "khóa học AI", "đại lý sơn".

## Bước 2: Mở Rộng Long-tail Theo Modifier
Áp dụng 7 nhóm modifier:
- Câu hỏi: "là gì", "có tốt không", "cách dùng", "tại sao"
- So sánh: "vs", "hay", "tốt hơn"
- Mua hàng: "giá", "mua ở đâu", "khuyến mãi"
- Địa điểm: "Hà Nội", "TP.HCM", "gần đây"
- Thời gian: "2026", "mới nhất", "đầu năm"
- Đối tượng: "cho người mới", "cho doanh nghiệp"
- Tính năng: "loại nào", "review"

## Bước 3: Phân Cluster + Map Intent
Mỗi cluster có 1 pillar page + 5-15 supporting articles. Gán intent (I/C/T) và funnel stage (TOFU/MOFU/BOFU).

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: lấy gợi ý "People also ask", autocomplete Google
- WebFetch: parse top 10 SERP để hiểu nội dung đang xếp hạng
- Google Drive MCP: lưu báo cáo
- Notion MCP: đẩy vào Content Hub
- GA4/Search Console MCP (nếu có): kéo keyword hiện đang impression

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Gọi Google Search Console API lấy keyword hiện tại
from googleapiclient.discovery import build
service = build('searchconsole', 'v1', credentials=creds)
res = service.searchanalytics().query(siteUrl='https://abc.vn', body={
  'startDate':'2026-03-01','endDate':'2026-05-28',
  'dimensions':['query'],'rowLimit':5000
}).execute()
```

## Bước 5: Output Format
- File `.xlsx` tên `SEO_Keyword_Research_<domain>.xlsx`
- Sheet 1: Seed (20-30 từ)
- Sheet 2: Long-tail (200-500 từ + volume ước tính + intent)
- Sheet 3: Cluster (pillar + supporting)
- Sheet 4: Content Map 90 ngày
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ 200+ keyword đã phân intent
- [ ] Mỗi cluster có pillar + tối thiểu 5 supporting
- [ ] Có cột difficulty (Easy/Medium/Hard) ước lượng
- [ ] Đã ánh xạ với funnel stage
- [ ] Đã loại trừ keyword không liên quan
- [ ] Có Content Map sắp xếp theo tuần
