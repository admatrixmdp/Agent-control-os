---
name: mkt-brand-name-generator
description: |
  Sinh 50+ phương án tên thương hiệu cho doanh nghiệp/sản phẩm Việt Nam, kèm check domain .com/.vn còn trống và check trademark cơ bản. Kích hoạt khi người dùng nói: "đặt tên thương hiệu", "brand naming", "tạo tên brand", "naming sản phẩm", "đặt tên công ty", "tên thương hiệu hay", "brand name generator", "đặt tên hay cho công ty". Output là Excel 50+ option có cột check.
---

# Đặt Tên Thương Hiệu — 50+ Options + Check Domain

## Mục Tiêu
Trong 30 phút có shortlist 5-10 tên thương hiệu khả thi, domain còn, không trùng trademark, dễ phát âm tiếng Việt + tiếng Anh.

## Khi Nào Dùng
- Founder mới startup
- Ra dòng sản phẩm sub-brand
- Đổi tên do conflict
- Mở rộng quốc tế cần tên global-friendly
- Naming nội bộ dự án/agent AI

## Bước 1: Brief Naming
Hỏi:
1. Lĩnh vực + sản phẩm
2. Audience target
3. 5 từ khóa cảm xúc muốn liên tưởng (vd: nhanh, tin cậy, hiện đại)
4. Phong cách: descriptive / suggestive / made-up / acronym / founder name
5. Yêu cầu domain: .com / .vn / cả 2
6. Ngôn ngữ: VI / EN / global
7. Số ký tự ưa thích (4-8 chữ cái)

## Bước 2: Sinh 50+ Tên Theo 6 Pattern
1. **Descriptive**: mô tả thẳng (VnExpress, Topica)
2. **Suggestive**: gợi ý (Tiki = nhỏ gọn, Shopee = shop ee)
3. **Made-up**: bịa từ (Bizflow, Zappify, Lumio)
4. **Compound**: ghép 2 từ (FaceBook, NetFlix, BeatVN)
5. **Acronym**: viết tắt (IBM, KFC, VNG)
6. **Founder/Place**: theo tên người/địa danh (Ford, Hanoi Tech)

Mỗi pattern ~8-10 tên.

## Bước 3: Filter & Check
Mỗi tên check:
- Phát âm dễ (3 người đọc đúng lần đầu)
- Không có nghĩa xấu tiếng VN + EN
- Domain .com / .vn còn?
- Trademark VN còn?
- Social handle FB/IG/TikTok còn?
- SEO-friendly (không trùng từ phổ biến)

Cho điểm 0-10 mỗi tiêu chí. Giữ top 10.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: kiểm tra Google có brand nào trùng
- WebFetch: check domain qua whois.com / matbao.net
- IP Library MCP (nếu có): tra cứu IPVN trademark
- Google Drive MCP: lưu shortlist
- Slack MCP: vote team

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Check domain availability qua Namecheap API
import requests
def check_domain(name):
    for tld in ['.com','.vn','.io','.co']:
        d = name+tld
        r = requests.get('https://api.namecheap.com/xml.response', params={
          'ApiUser':USER,'ApiKey':KEY,'UserName':USER,
          'Command':'namecheap.domains.check','DomainList':d})
        # Parse XML to get Available=true/false
```

## Bước 5: Output Format
- File `.xlsx` 50+ tên có cột:
  - Tên | Pattern | Nghĩa | Phát âm | .com | .vn | TM | IG | Điểm tổng
- Top 10 shortlist có giải thích
- Top 3 finalist có moodboard visual
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 50+ tên 6 pattern
- [ ] Đã check domain .com/.vn
- [ ] Đã loại nghĩa xấu VN/EN
- [ ] Top 3 có moodboard
- [ ] Phát âm test 3 người
- [ ] Trademark search xong
