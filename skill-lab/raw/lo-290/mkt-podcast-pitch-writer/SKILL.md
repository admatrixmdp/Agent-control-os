---
name: mkt-podcast-pitch-writer
description: |
  Viết pitch xin làm khách mời (guest) podcast cho founder/exec doanh nghiệp Việt Nam — research host, cá nhân hóa, talking points, follow-up. Kích hoạt khi người dùng nói: "viết pitch podcast", "xin làm khách podcast", "podcast guest pitch", "email pitch host podcast", "guest pitch", "podcast appearance", "pitch lên show", "guest spot podcast". Output là Markdown email + danh sách podcast target.
---

# Pitch Host Podcast Khách Mời

## Mục Tiêu
Mỗi tháng founder/exec xuất hiện trên 3-5 podcast chất lượng giúp xây personal brand, tăng inbound lead B2B, mở rộng network — chi phí gần 0đ.

## Khi Nào Dùng
- Founder muốn xây personal brand
- Launch sản phẩm B2B cần thought leadership
- Sau khi đạt milestone đáng share
- Ra sách / khóa học
- Mở rộng vào ngành mới cần authority

## Bước 1: Brief Speaker
Hỏi:
1. Tên + chức vụ
2. 3 chủ đề chuyên sâu có thể chia sẻ
3. Câu chuyện độc đáo / contrarian view
4. Số liệu/case study minh chứng
5. Audience muốn tiếp cận
6. Sản phẩm/CTA cuối show
7. Time availability

## Bước 2: Research & List Podcast
Tiêu chí podcast target:
- Audience overlap với target
- Tier: Tier 1 (>50k listener/ep), Tier 2 (10-50k), Tier 3 (<10k - dễ vào)
- Đã có guest tương tự (không trùng vai chính)
- Format phù hợp (interview, casual, deep dive)
- Active trong 3 tháng qua

Dùng WebSearch + Apple/Spotify charts. Lọc 30-50 podcast.

## Bước 3: Soạn Pitch Cá Nhân Hóa
Email 200-300 từ:
1. **Câu mở** (cá nhân hóa): khen 1 tập cụ thể đã nghe (chứng minh đã nghiên cứu)
2. **Self intro** 2 dòng: chức vụ + 1 thành tựu nổi bật
3. **3 chủ đề** đề xuất chia sẻ (mỗi chủ đề 1 dòng)
4. **Tại sao audience của bạn quan tâm** (link với họ)
5. **Asset support**: case study link, follower social (nếu lớn)
6. **CTA** mềm: "Bạn có thể ping mình lên lịch ghi hình không?"
7. **P.S.** giới thiệu thêm 1 guest tiềm năng (cho - nhận)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tìm podcast theo ngách + chart top
- WebFetch: nghiên cứu host bio + tập gần nhất
- Spotify/Apple Podcasts MCP (nếu có)
- Gmail MCP: gửi cá nhân hóa + follow-up 7-14 ngày
- Sheets MCP: tracker pitch
- Notion MCP: podcast media list

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Lấy top podcast ngách qua Listen Notes API
import requests
def search_podcasts(query, country='vn'):
    r = requests.get('https://listen-api.listennotes.com/api/v2/search',
      headers={'X-ListenAPI-Key':API_KEY},
      params={'q':query,'type':'podcast','region':country,
              'sort_by_date':0,'len_min':30})
    return r.json()['results']
```

## Bước 5: Output Format
- File `.xlsx` danh sách 30-50 podcast với tier + contact
- 3 template email (Tier 1/2/3)
- Talking points & soundbite ready
- Follow-up sequence 2-3 lần
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 30+ podcast đã lọc
- [ ] Email cá nhân hóa (nghe tập cụ thể)
- [ ] 3 chủ đề đề xuất rõ
- [ ] Asset prove authority
- [ ] Có give-back (giới thiệu guest khác)
- [ ] Follow-up 2 lần
- [ ] Tracker conversion pitch → confirm
