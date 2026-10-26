---
name: mkt-nps-analyzer
description: |
  Phân tích kết quả khảo sát NPS — tính điểm, segment promoter/passive/detractor, phân tích verbatim bằng LLM, đề xuất action. Kích hoạt khi người dùng nói: "phân tích NPS", "đọc kết quả NPS", "NPS analyzer", "NPS report", "phân tích verbatim NPS", "detractor analysis", "promoter analysis", "phân tích kết quả khảo sát". Output là HTML report + Excel breakdown.
---

# Phân Tích NPS — Segment + Verbatim

## Mục Tiêu
Biến file kết quả survey thô thành báo cáo NPS đầy đủ trong 30 phút với insight + action cụ thể, không dừng ở "điểm bao nhiêu".

## Khi Nào Dùng
- Vừa thu xong survey NPS
- Báo cáo NPS quý/năm
- Phân tích theo segment (kênh, sản phẩm, độ tuổi)
- Theo dõi NPS theo thời gian
- Trước họp board

## Bước 1: Import Data
Hỏi file CSV/Sheet có cột:
- Score (0-10)
- Verbatim reason
- Verbatim improvement
- Segment (sản phẩm, kênh, độ tuổi, region)
- Thời gian

Validate: tối thiểu 100 responses để có ý nghĩa.

## Bước 2: Tính NPS + Phân Segment
**Công thức**:
- Promoter: score 9-10
- Passive: 7-8
- Detractor: 0-6
- NPS = %Promoter − %Detractor

Benchmark VN:
- <0: nguy hiểm
- 0-30: trung bình
- 30-50: tốt
- 50-70: rất tốt
- 70+: xuất sắc

Phân tích NPS theo:
- Sản phẩm
- Kênh mua (web/sàn/offline)
- Cohort thời gian
- Persona/khu vực
- Thời gian khách (mới/cũ)

## Bước 3: Phân Tích Verbatim
Dùng LLM phân loại verbatim Detractor + Promoter:
- Top 5 lý do Promoter yêu thích
- Top 5 lý do Detractor không hài lòng
- Top 5 ý kiến cải thiện
- Quote tiêu biểu

Mỗi nhóm có % proportion + emotion score.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Sheets MCP: import data
- Notion MCP: lưu báo cáo
- Slack MCP: alert detractor mới
- CRM MCP: gắn NPS score per customer
- LLM API: phân tích verbatim

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Phân loại verbatim bằng LLM
from anthropic import Anthropic
import pandas as pd
client = Anthropic()
df = pd.read_csv('nps.csv')
detractors = df[df['score']<=6]['verbatim'].tolist()
prompt = f'''Phân loại các verbatim sau thành 5 chủ đề chính.
Trả về JSON {{"theme":[verbatim_index]}}:
{detractors}'''
res = client.messages.create(model='claude-opus-4-5',
  max_tokens=2000, messages=[{'role':'user','content':prompt}])
```

## Bước 5: Output Format
- File HTML báo cáo:
  - NPS overall + theo segment
  - Top 5 theme Promoter/Detractor
  - 10 quote tiêu biểu
  - 5-10 action item ưu tiên
- File `.xlsx` raw data + breakdown
- Email cho leadership
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Sample size đủ (>=100)
- [ ] NPS overall + segment
- [ ] Verbatim phân theme
- [ ] Quote tiêu biểu trích nguyên văn
- [ ] Action có owner + ETA
- [ ] So sánh kỳ trước (delta)
