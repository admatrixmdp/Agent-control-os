---
name: sales-icp-builder
description: |
  Định nghĩa Ideal Customer Profile (ICP) + anti-ICP chi tiết theo firmographic, technographic, behavior và intent signal — giúp sales tập trung deal thắng cao. Trigger phrases: "xây dựng ICP", "định nghĩa khách hàng lý tưởng", "ICP B2B", "anti-ICP", "phân khúc khách hàng target", "ai là khách hàng tốt nhất", "profile khách hàng lý tưởng", "tiêu chí chấm KH tốt", "lọc khách target", "tạo ICP cho sales". Output là Markdown ICP doc + Excel scorecard fit.
---

# ICP & Anti-ICP Builder

## Mục Tiêu
Giúp lãnh đạo Sales/Marketing định nghĩa rõ KH lý tưởng (high fit + high intent) và loại trừ KH xấu (anti-ICP) để tăng win rate, giảm churn và rút ngắn sales cycle.

## Khi Nào Dùng
- Sản phẩm mới ra mắt, chưa có ICP
- Win rate <15% — nghi do nhắm sai
- Mở rộng sang vertical/region mới
- Chuẩn bị chiến dịch ABM
- Tái cấu trúc team sales theo segment

## Bước 1: Audit 20 KH tốt nhất + 10 KH tệ nhất
Pull từ CRM:
- 20 KH có CLV cao, retention >18 tháng, NPS >40
- 10 KH churn nhanh / đòi refund / support cost cao

Phân tích 6 chiều mỗi KH:
- Firmographic (size, revenue, industry, geo)
- Technographic (tech stack, integration cần)
- Behavior (mua nhanh hay chậm, ai quyết, ngân sách)
- Pain trigger (event nào khiến họ tìm)
- Decision criteria (giá / feature / brand)
- Use case (3-5 use case chính)

## Bước 2: Tổng hợp ICP Definition
Viết doc gồm:
- **Headline**: 1 câu định nghĩa ICP (vd: "Doanh nghiệp FMCG VN 200-2000 NV, đang scale chi nhánh tỉnh, dùng SAP/Misa")
- **Firmographic**: 5-7 tiêu chí cụ thể có ngưỡng số
- **Technographic**: stack hiện tại + tích hợp cần
- **Buying committee**: 3-5 role tham gia quyết
- **Triggers**: 5 sự kiện khiến KH tìm giải pháp
- **Pain & outcome**: 3 pain chính + 3 outcome đo được

## Bước 3: Anti-ICP — loại trừ rõ ràng
- Size quá nhỏ/quá lớn (vd <50 NV hoặc >5000)
- Vertical không match (high regulation, low margin)
- Behavioral red flag: hỏi giá ngay phút 1, không có budget, deal cycle >12 tháng
- Tech stack không tương thích
- Geo không support được
→ Cấm SDR đẩy lead này lên AE.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Salesforce/HubSpot MCP: pull KH list + CLV + churn data
- Gong/Chorus (qua MCP nếu có): phân tích call transcript top deal thắng
- WebFetch: research vertical/geo data
- WebSearch: tìm benchmark CAC/LTV ngành

**Fallback API:**
```python
# Salesforce SOQL pull top accounts
from simple_salesforce import Salesforce
sf = Salesforce(username=u, password=p, security_token=t)
top = sf.query("""SELECT Name, Industry, AnnualRevenue, NumberOfEmployees
                  FROM Account WHERE CLV__c > 100000 
                  AND ChurnDate__c = NULL LIMIT 20""")
```

## Bước 5: Output Format
- **File 1**: `ICP_<product>_<date>.md` — doc 4-6 trang đầy đủ định nghĩa
- **File 2**: `ICP_fit_scorecard.xlsx` — 15 tiêu chí có trọng số, sales fill score 0-3, tổng / 45
- **File 3**: `anti_ICP_redflags.md` — danh sách 10 red flag SDR phải check
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] ICP dựa trên data thật 20+10 KH, không cảm tính
- [ ] Mỗi tiêu chí có ngưỡng số cụ thể
- [ ] Có ít nhất 5 anti-ICP red flag
- [ ] Scorecard chấm được 0-3 mỗi tiêu chí
- [ ] Trình bày được cho SDR trong 5 phút
- [ ] Có example 3 KH thật minh hoạ
