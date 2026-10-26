---
name: mkt-positioning-statement
description: |
  Viết tuyên ngôn định vị (positioning statement) cho doanh nghiệp/sản phẩm Việt Nam — kèm 3-5 phương án thay thế và lý do chọn. Theo công thức "For [audience], who [need], [brand] is [category] that [benefit] unlike [competitor]". Kích hoạt khi người dùng nói: "viết positioning statement", "tuyên ngôn định vị", "định vị thương hiệu", "positioning brand", "viết định vị sản phẩm", "differentiation statement", "viết câu định vị", "positioning". Output là Markdown + slide deck 5 trang.
---

# Tuyên Ngôn Định Vị + Alternatives

## Mục Tiêu
Có 1 câu định vị rõ ràng làm kim chỉ nam mọi messaging, mọi quyết định product/marketing — giúp khách phân biệt brand với đối thủ trong 5 giây.

## Khi Nào Dùng
- Mới start-up cần định vị từ đầu
- Tái định vị sau giai đoạn pivot
- Ra dòng sản phẩm mới
- Sau M&A
- Khi messaging team không nhất quán

## Bước 1: Brief Brand
Hỏi:
1. Tên brand/sản phẩm
2. Audience chính + insight đậm nhất
3. Category đang/sẽ cạnh tranh
4. 3 đối thủ chính + cách họ định vị
5. 3 USP/lý do brand khác biệt (proof)
6. Vision dài hạn
7. Tone (premium / mass / niche)

## Bước 2: Khung Positioning
Công thức chính:
> "For [target audience], who [need/insight], [brand] is the [category/frame of reference] that [unique benefit + proof], unlike [competitor]."

Ví dụ: "Cho chủ doanh nghiệp SME 35-55 tuổi đang sợ AI bỏ rơi, TAKI Academy là chương trình đào tạo AI ứng dụng giúp họ tự build agent AI nội bộ trong 30 ngày, không như các khóa lý thuyết chỉ dạy ChatGPT."

## Bước 3: Sinh 5 Alternative
Mỗi alternative đổi 1 trục:
- Đổi audience (B2B exec vs SME owner)
- Đổi category (training vs coaching vs SaaS)
- Đổi benefit (speed vs result vs prestige)
- Đổi competitor (so với ai)
- Đổi proof point

So sánh và chọn 1 mạnh nhất theo 4 tiêu chí: rõ / khác biệt / sở hữu được / có chứng cứ.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: phân tích định vị đối thủ
- WebFetch: lấy tagline/hero copy đối thủ
- Notion MCP: lưu Brand Bible
- Google Drive MCP: lưu deck
- Slack MCP: chia sẻ team review

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Crawl tagline đối thủ từ website
import requests
from bs4 import BeautifulSoup
for url in competitor_urls:
    r = requests.get(url); s = BeautifulSoup(r.text,'html.parser')
    print(url, s.title.text, s.select_one('h1').text if s.select_one('h1') else '')
```

## Bước 5: Output Format
- File `.md` positioning statement chính + 5 alternative + lý do chọn
- Slide deck 5 trang trình bày cho leadership
- Bảng so sánh positioning với 3 đối thủ
- Messaging house (Pillar 1, 2, 3 → proof points)
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ 5 element trong công thức
- [ ] Phân biệt rõ với 3 đối thủ
- [ ] Proof point có thật
- [ ] Brand sở hữu được category đó
- [ ] Đã chốt cùng founder/CMO
- [ ] Đã test với 5 KH (phân biệt được không)
