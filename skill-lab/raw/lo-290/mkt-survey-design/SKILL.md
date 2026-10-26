---
name: mkt-survey-design
description: |
  Thiết kế survey NPS/CSAT/Brand Health cho doanh nghiệp Việt Nam — câu hỏi đúng metric, không bias, ngắn gọn (<5 phút), kèm phân phối và phân tích. Kích hoạt khi người dùng nói: "thiết kế survey", "khảo sát NPS", "CSAT survey", "brand health survey", "survey khách hàng", "thiết kế bảng hỏi", "viết khảo sát", "survey design". Output là Markdown survey + Google Forms link.
---

# Thiết Kế Survey NPS / CSAT / Brand Health

## Mục Tiêu
Có bộ khảo sát chuẩn quốc tế, mỗi quý chạy 1 lần, đo được cảm xúc khách hàng để ra quyết định product/marketing dựa trên data thật.

## Khi Nào Dùng
- Lần đầu đo NPS/CSAT
- Đo brand awareness định kỳ
- Sau campaign lớn
- Trước/sau ra mắt sản phẩm
- Quý cần báo cáo board

## Bước 1: Chọn Loại Survey
3 loại chính:
- **NPS** (Net Promoter Score): "Mức độ sẵn sàng giới thiệu" 0-10
- **CSAT**: "Mức độ hài lòng với [trải nghiệm cụ thể]" 1-5
- **CES** (Customer Effort Score): "Mức độ dễ dàng" 1-7
- **Brand Health**: awareness, perception, consideration, preference

Hỏi: mục tiêu? đo gì? đối tượng?

## Bước 2: Soạn Câu Hỏi Chuẩn
**NPS** (3 câu):
1. "Mức độ sẵn sàng giới thiệu [brand] cho bạn bè? (0-10)"
2. "Lý do bạn cho điểm đó?" (open)
3. "Điều gì chúng tôi có thể cải thiện?" (open)

**CSAT** (5-7 câu):
1. Điểm hài lòng tổng (1-5)
2. Điểm hài lòng từng yếu tố (sản phẩm, giao hàng, CS, giá, app)
3. Khả năng mua lại
4. Lý do điểm
5. Demographic

**Brand Health** (10-15 câu): awareness top of mind, aided/unaided, attribute association, consideration, preference.

Quy tắc:
- 1 câu = 1 ý
- Tránh leading/loaded question
- Scale chẵn (4/6/10) để tránh trung lập
- <5 phút (max 15 câu)

## Bước 3: Phân Phối & Mẫu
- Sample size: tối thiểu 100, lý tưởng 300-500
- Kênh: email, SMS, in-app popup, Zalo OA
- Incentive: voucher 20-50k để tăng response rate (mục tiêu >15%)
- Thời gian: 7-14 ngày
- Anti-bias: random hóa, ẩn danh

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Forms MCP: tạo form survey
- Typeform MCP: form đẹp hơn cho B2B
- Email MCP: gửi survey hàng loạt
- Zalo OA MCP: ZNS gửi survey
- Sheets MCP: thu kết quả
- Notion MCP: lưu báo cáo

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tính NPS từ data
import pandas as pd
df = pd.read_csv('nps_responses.csv')
total = len(df)
promoters = len(df[df['score']>=9])
detractors = len(df[df['score']<=6])
nps = (promoters - detractors) / total * 100
print(f'NPS: {nps:.1f}')
```

## Bước 5: Output Format
- File `.md` câu hỏi survey
- Google Forms / Typeform link
- File `.xlsx` template phân tích kết quả
- Báo cáo HTML 1 trang sau khi thu data
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] <5 phút điền
- [ ] Câu hỏi không bias
- [ ] Scale phù hợp metric
- [ ] Mobile-friendly
- [ ] Có incentive
- [ ] Sample size đủ statistical
- [ ] Plan phân tích sẵn
