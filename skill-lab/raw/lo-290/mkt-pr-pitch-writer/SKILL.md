---
name: mkt-pr-pitch-writer
description: |
  Viết pitch PR gửi báo Việt Nam (VnExpress, ICTNews, CafeF, VietnamNet, Tuổi Trẻ Online, Báo Đầu Tư...) — tự động chọn góc câu chuyện, viết tiêu đề báo chí và soạn pitch email. Kích hoạt khi người dùng nói: "viết pitch PR", "pitch báo", "email gửi báo", "PR pitch VN", "press release VN", "viết bài PR", "gửi báo viết bài", "pitch journalist". Output là email + press release Markdown.
---

# Pitch PR Gửi Báo Việt Nam

## Mục Tiêu
Mỗi tháng có 1-3 bài được báo lớn đăng (organic PR), tăng brand authority và backlink chất lượng, mà không phải book booth PR đắt đỏ.

## Khi Nào Dùng
- Doanh nghiệp ra mắt sản phẩm/dịch vụ mới
- Gọi vốn / mở rộng thị trường
- Nghiên cứu/báo cáo ngành độc quyền
- Sự kiện CSR/ESG
- Bổ nhiệm leader / milestone

## Bước 1: Xác Định Góc Câu Chuyện (Angle)
6 góc thường được báo chọn:
1. First/biggest/only (đầu tiên/lớn nhất)
2. Conflict/controversy
3. Data-driven insight (báo cáo độc quyền)
4. Human interest (founder story)
5. Trend timely (gắn xu hướng nóng)
6. Local impact (tác động địa phương)

Chọn 1-2 góc phù hợp.

## Bước 2: Lập Danh Sách Báo Mục Tiêu
Chia 3 tier:
- Tier 1: VnExpress, Tuổi Trẻ, Thanh Niên, CafeF, Báo Đầu Tư
- Tier 2: ICTNews, VietnamNet, Dân Trí, Vietnambiz
- Tier 3: Báo ngành (Diễn Đàn DN, Tạp chí Kinh tế Sài Gòn)

Với mỗi báo: xác định chuyên mục + phóng viên phụ trách + email/Zalo.

## Bước 3: Viết Pitch + Press Release
**Pitch email** (300-400 từ):
- Subject line báo chí: "[Loại tin] + [Thông tin shock/số liệu]"
- Câu mở 2 dòng nói rõ TẠI SAO báo nên viết
- Đoạn tóm tắt 5W1H
- 2-3 quote sẵn từ founder
- Số liệu cụ thể
- Link press release + asset (logo, ảnh, video)

**Press release** (600-800 từ):
- Inverted pyramid
- Headline báo chí
- Subhead
- Lead 50 từ
- Body có quote, số liệu, context
- About company boilerplate
- Contact PR

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tìm phóng viên ngành đang viết chủ đề tương tự
- WebFetch: đọc bài đã viết của phóng viên để cá nhân hóa
- Gmail MCP: gửi pitch cá nhân
- Google Drive MCP: lưu press kit folder
- Notion MCP: PR media list CRM

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Crawl email/contact phóng viên từ chuyên mục
import requests, re
from bs4 import BeautifulSoup
r = requests.get('https://vnexpress.net/kinh-doanh').text
soup = BeautifulSoup(r,'html.parser')
authors = set(a.text for a in soup.select('.author-name'))
```

## Bước 5: Output Format
- File `.md`:
  - Pitch email (3 phiên bản subject A/B/C)
  - Press release đầy đủ
  - Bullet talking points 5-7 điểm
  - Boilerplate
- Press kit folder (logo, exec bio, ảnh, fact sheet)
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Subject email <60 ký tự, news-worthy
- [ ] Lead < 50 từ trả lời 5W1H
- [ ] >= 2 quote sẵn
- [ ] Số liệu cụ thể, nguồn rõ
- [ ] Có asset (logo, ảnh HD)
- [ ] Embargo time rõ (nếu có)
- [ ] Đã cá nhân hóa cho từng phóng viên
