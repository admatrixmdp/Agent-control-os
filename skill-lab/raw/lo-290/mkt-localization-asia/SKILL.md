---
name: mkt-localization-asia
description: |
  Bản địa hóa marketing cho 4 thị trường Đông Nam Á: Việt Nam, Thái Lan, Indonesia, Malaysia — copy, hình ảnh, kênh, payment, ngày lễ. Kích hoạt khi người dùng nói: "localize Đông Nam Á", "bản địa hóa marketing", "marketing Thailand Indonesia Malaysia", "localization Asia", "expand SEA", "go global SEA", "đa quốc gia ASEAN", "local marketing SEA". Output là Markdown localization guide + Excel matrix.
---

# Bản Địa Hóa MKT Cho Đông Nam Á

## Mục Tiêu
Khi mở rộng sang VN/TH/ID/MY, không bị "google translate" thuần túy — mọi copy, hình ảnh, payment, lễ tết đều bản địa hóa đúng văn hóa.

## Khi Nào Dùng
- Ecom/SaaS mở rộng SEA
- Launch sản phẩm cross-border
- Campaign Tết / Songkran / Lebaran
- Mở rộng kênh local (Shopee TH/ID/MY)
- Localize app/website

## Bước 1: Audit Thị Trường
4 thị trường, mỗi cái:
1. Ngôn ngữ chính + dialect
2. Tôn giáo (Hồi giáo MY/ID → halal, ăn mặc)
3. Payment phổ biến (VN: Momo, ZaloPay; TH: PromptPay; ID: GoPay, OVO; MY: Touch n Go)
4. Kênh social (VN: FB/TikTok; TH: LINE/TikTok; ID: WhatsApp/IG; MY: WhatsApp/FB)
5. Sàn TMĐT (Shopee, Lazada, Tokopedia ID, Tiki VN)
6. Ngày lễ lớn (Tết VN, Songkran TH, Lebaran ID, Hari Raya MY)
7. Đối thủ local
8. Pricing power (GDP/capita)

## Bước 2: Bản Địa Hóa 6 Yếu Tố
1. **Copy/messaging**: nhờ native review, không Google Translate
2. **Hình ảnh**: model + bối cảnh local (Indo có hijab, Thái có chùa)
3. **Color & symbol**: ID/MY xanh lá là halal-safe, đỏ Tết VN, tím TH royal
4. **Channel mix**: WhatsApp ưu tiên ID/MY, Zalo VN
5. **Payment**: tích hợp local wallet
6. **Customer Service**: hotline local + giờ local

## Bước 3: Build Localization Matrix
Bảng so sánh 4 thị trường x 10 yếu tố. Mỗi cell điền chi tiết riêng.

Ví dụ:
| Yếu tố | VN | TH | ID | MY |
|---|---|---|---|---|
| Lễ lớn | Tết 1/29 | Songkran 4/13 | Lebaran 6/16 | Hari Raya 6/17 |
| Payment | Momo, ZaloPay | PromptPay, TrueMoney | GoPay, OVO | Boost, TnG |
| Social | FB/TikTok/Zalo | LINE/TikTok/IG | WhatsApp/IG/TikTok | WhatsApp/FB/IG |
| Sàn | Shopee, Tiki | Shopee, Lazada | Tokopedia, Shopee | Shopee, Lazada |
| Ngôn ngữ | VI | TH | ID | MY+EN |

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: research benchmark từng thị trường
- WebFetch: lấy data sàn TMĐT
- Translation API connector (DeepL/Google): bản dịch ban đầu
- Notion MCP: localization library
- Hubspot CRM multi-locale: lưu segment theo country

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Bản dịch + back-translation check
import requests
def translate(text, src, tgt):
    r = requests.post('https://api-free.deepl.com/v2/translate',
      data={'auth_key':KEY,'text':text,'source_lang':src,'target_lang':tgt})
    return r.json()['translations'][0]['text']

# Translate sang ID rồi back lại EN để check
vi = 'Khóa học AI cho chủ doanh nghiệp'
en = translate(vi,'VI','EN')
id_ = translate(en,'EN','ID')
back = translate(id_,'ID','EN')
print('Original:', en, '\nBack-trans:', back)
```

## Bước 5: Output Format
- File `.md` localization playbook 4 nước
- File `.xlsx` matrix 4 x 10 yếu tố
- 4 phiên bản LP copy (1 cho mỗi nước)
- Asset pack (hình ảnh, banner, font local)
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 4 nước có matrix đầy đủ
- [ ] Copy đã native review
- [ ] Asset hình ảnh local
- [ ] Payment + sàn local tích hợp
- [ ] Ngày lễ lớn vào calendar
- [ ] CS giờ + ngôn ngữ local
- [ ] Legal/tax local check
