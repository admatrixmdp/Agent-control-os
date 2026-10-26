---
name: mkt-meta-pixel-audit
description: |
  Audit Meta Pixel + Conversion API setup cho doanh nghiệp Việt Nam — kiểm tra trigger event, deduplication, EMQ score, hit rate. Đề xuất fix kỹ thuật cho dev. Kích hoạt khi người dùng nói: "audit Meta Pixel", "kiểm tra Facebook Pixel", "Conversion API CAPI", "audit Pixel setup", "EMQ score", "deduplication FB", "Pixel debug", "fix Pixel website". Output là báo cáo HTML + checklist dev.
---

# Audit Meta Pixel + Conversion API

## Mục Tiêu
Đảm bảo Pixel + CAPI bắn đủ event, không duplicate, EMQ >7, giúp Meta Ads tối ưu tốt hơn — cải thiện 15-30% ROAS nhờ data chất lượng.

## Khi Nào Dùng
- iOS 14.5+ tracking giảm
- Pixel chỉ có trên web nhưng chưa CAPI
- ROAS Meta Ads thấp bất thường
- Sau khi đổi platform (Shopify ↔ WooCommerce)
- Audit định kỳ quý

## Bước 1: Inventory Setup
Hỏi:
1. Pixel ID
2. Platform website (Shopify/WooCommerce/Wix/custom)
3. Đã cài CAPI chưa? Qua đâu (GTM server / native)
4. Event đang track (ViewContent, AddToCart, Purchase...)
5. URL trang chính cần audit

## Bước 2: Kiểm Tra 10 Điểm
1. Pixel base code ở tất cả trang
2. Event tự động (PageView) bắn đúng
3. Event chính (ViewContent, AddToCart, InitiateCheckout, Purchase) bắn đúng tham số (value, currency, content_ids)
4. CAPI gửi server-side đủ event không
5. Deduplication key (event_id) khớp giữa browser + server
6. Advanced Matching (em, ph, fn, ln hashed) gửi đủ
7. EMQ Score (Event Match Quality) - cần >7
8. Hit rate browser vs CAPI (lý tưởng CAPI >= browser)
9. Customer Info (em, ph) hash đúng SHA256
10. Conversions API access token còn valid

## Bước 3: Sinh Báo Cáo + Action
Mỗi điểm: status (✅/⚠️/❌) + giải thích + cách fix kỹ thuật cụ thể (code snippet, GTM tag setting).

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Meta Ads MCP / Marketing API: lấy diagnostic
- WebFetch: kiểm tra trang xem Pixel có không
- Chrome MCP: dùng Meta Pixel Helper
- Google Drive MCP: lưu báo cáo
- Slack MCP: gửi cho dev

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Gửi test event qua CAPI để kiểm tra
import requests, time, hashlib
def hash_(s): return hashlib.sha256(s.lower().strip().encode()).hexdigest()
event = {'event_name':'Purchase','event_time':int(time.time()),
  'event_id':'test_123','action_source':'website',
  'user_data':{'em':[hash_('test@x.vn')]},
  'custom_data':{'currency':'VND','value':500000}}
r = requests.post(f'https://graph.facebook.com/v18.0/{PIXEL_ID}/events',
  params={'access_token':TOKEN},
  json={'data':[event],'test_event_code':'TEST123'})
```

## Bước 5: Output Format
- File HTML báo cáo có 10 điểm + status
- File `.md` action list cho dev có code snippet
- Test event log để verify sau fix
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 10 điểm đều check
- [ ] EMQ score ghi rõ
- [ ] Hit rate browser/CAPI có số
- [ ] Action có code snippet
- [ ] Đã test event end-to-end
- [ ] Đã sync dev (có ETA)
