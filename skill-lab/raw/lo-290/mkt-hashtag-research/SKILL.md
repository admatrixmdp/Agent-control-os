---
name: mkt-hashtag-research
description: |
  Nghiên cứu hashtag Instagram/TikTok theo niche cho doanh nghiệp Việt Nam, phân tier (big/medium/niche), volume, competition và đề xuất bộ 20-30 hashtag tối ưu. Kích hoạt khi người dùng nói: "research hashtag", "tìm hashtag IG TikTok", "bộ hashtag niche", "hashtag strategy", "hashtag IG", "hashtag TikTok VN", "hashtag tăng reach", "hashtag bank". Output là Excel bank + Markdown guide.
---

# Hashtag Research IG/TikTok Theo Niche

## Mục Tiêu
Mỗi post có bộ hashtag mix balanced giữa big tag (volume) + niche tag (chuyển đổi cao), tăng reach 30-100% so với dùng hashtag random.

## Khi Nào Dùng
- Tài khoản mới chưa có hashtag bank
- Reach đang giảm do thuật toán
- Mở rộng niche mới
- Trước launch campaign
- Audit hashtag cũ

## Bước 1: Brief Niche
Hỏi:
1. Ngành/sản phẩm
2. Platform (IG / TikTok / cả 2)
3. Audience VN / quốc tế
4. 5 hashtag đã dùng (nếu có)
5. Đối thủ + KOL ngách

## Bước 2: Crawl & Phân Tier
3 tier:
- **Big** (>1M post): volume cao, cạnh tranh khốc liệt, dùng 2-3 tag
- **Medium** (100k-1M): cạnh tranh vừa, dùng 8-10 tag
- **Niche** (10k-100k): cạnh tranh thấp, CR cao, dùng 10-15 tag
- **Branded**: hashtag riêng brand (#TAKIacademy)

Mỗi platform có rule riêng:
- IG: max 30 tag, ưu tiên niche
- TikTok: 3-5 tag mạnh hơn 30 tag

## Bước 3: Build Hashtag Bank
Bank chia theo topic:
- Topic chính (vd AI training): 30 hashtag
- Topic phụ: 30 hashtag mỗi topic
- Trending/event: 10 hashtag thay đổi tuần
- Branded: 5 hashtag

Test 2-4 tuần, đo reach từng combo.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tra hashtag analytics qua RiteTag/Display Purposes
- WebFetch: scrape Instagram hashtag page lấy post count
- Notion MCP: lưu bank
- Google Sheets MCP: tracker reach theo hashtag
- IG Graph API connector (nếu có): hashtag insights

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Lấy hashtag insight qua Instagram Graph API (business account)
import requests
def get_hashtag_id(name):
    r = requests.get('https://graph.facebook.com/v18.0/ig_hashtag_search',
      params={'user_id':IG_USER_ID,'q':name,'access_token':TOKEN})
    return r.json()['data'][0]['id']

def hashtag_top_media(hid):
    r = requests.get(f'https://graph.facebook.com/v18.0/{hid}/top_media',
      params={'user_id':IG_USER_ID,'fields':'id,like_count,caption',
              'access_token':TOKEN})
    return r.json()
```

## Bước 5: Output Format
- File `.xlsx` hashtag bank:
  - Sheet 1: All hashtags + post count + tier + topic
  - Sheet 2: Combo theo post type
  - Sheet 3: Tracker reach
- File `.md` SOP dùng hashtag
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 100+ hashtag phân 3 tier
- [ ] Combo 20-30 tag sẵn dùng
- [ ] Branded hashtag riêng
- [ ] Đã loại hashtag bị shadowban
- [ ] Tracker test reach
- [ ] Cập nhật weekly trend tag
