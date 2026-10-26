---
name: mkt-customer-persona-builder
description: |
  Tạo 5 customer persona chi tiết cho doanh nghiệp Việt Nam — nhân khẩu học, hành vi, pain point, JTBD, ngân sách, kênh tiếp xúc. Tự động sinh từ data CRM/khảo sát/interview. Kích hoạt khi người dùng nói: "tạo persona khách hàng", "customer persona", "buyer persona", "chân dung khách hàng", "ICP ideal customer", "phác họa khách hàng", "phân khúc khách hàng", "JTBD persona". Output là HTML deck 5 persona + PDF.
---

# Tạo 5 Customer Persona

## Mục Tiêu
Toàn team marketing + sales + product có cùng góc nhìn về khách hàng, ngừng làm việc theo cảm tính, mọi messaging/ad/sản phẩm bám sát insight thực.

## Khi Nào Dùng
- Doanh nghiệp mới chưa có persona
- Tái định vị sản phẩm
- Mở rộng segment mới
- Trước khi build content/ads chiến dịch lớn
- Onboard team mới

## Bước 1: Thu Thập Data
Nguồn:
1. CRM data (đơn hàng, churn, LTV)
2. Khảo sát 50-200 KH hiện tại
3. Interview 5-15 KH thân thiết
4. Social listening + review platform
5. Hỗ trợ KH ticket
6. Google Analytics / Meta audience insights

Hỏi user nguồn nào có sẵn để dùng.

## Bước 2: Phân Cluster
Phân theo 4 trục:
- Demographic (tuổi, giới, thu nhập, khu vực)
- Psychographic (lifestyle, value)
- Behavior (mua thường xuyên hay không, kênh nào)
- Stage (TOFU/MOFU/BOFU)

Tìm 5 nhóm có khối lượng + value lớn nhất.

## Bước 3: Viết Từng Persona
Mỗi persona có template:
- Tên + ảnh + age + nghề
- 1 câu mô tả ("Chị Linh - chủ shop online 8M follower IG")
- Goals (3 mục tiêu trong cuộc sống/công việc)
- Pain points (3 nỗi đau lớn nhất)
- Jobs-to-be-Done (cần làm gì)
- Frustrations với giải pháp hiện tại
- Sources of info (đọc đâu, follow ai)
- Buying behavior (ai duyệt mua, ngân sách, decision time)
- Quote tiêu biểu
- Brand they love
- Channel tiếp cận (FB/IG/TikTok/email/event)
- Messaging gợi ý (3 angle ăn nhất)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- GA4 MCP: kéo demographic + behavior
- Meta Audience Insights MCP: tâm lý + interest
- CRM MCP (HubSpot/Salesforce): segment data
- Notion MCP: persona database
- WebSearch: research insight ngành VN

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Phân cluster KH bằng K-means trên CRM data
import pandas as pd
from sklearn.cluster import KMeans
df = pd.read_csv('customers.csv')
features = df[['age','aov','frequency','recency']]
km = KMeans(n_clusters=5, random_state=42).fit(features)
df['segment'] = km.labels_
df.groupby('segment').mean()
```

## Bước 5: Output Format
- File HTML deck 5 persona đẹp (mỗi persona 1 trang)
- PDF in được
- Markdown copy paste vào Notion
- Persona poster A3 in treo team
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] 5 persona đại diện 80%+ doanh thu
- [ ] Mỗi persona có quote + ảnh
- [ ] Có pain point + JTBD cụ thể
- [ ] Channel + messaging gợi ý
- [ ] Có data nguồn (CRM/khảo sát) backup
- [ ] Đã chia sẻ với team
