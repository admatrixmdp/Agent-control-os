---
name: mkt-linkedin-company-page
description: |
  Viết bài LinkedIn cho company page doanh nghiệp Việt Nam, kết hợp 2 trụ cột Employer Brand + Product Updates. Tự động chia 4 dạng bài (thought leadership, behind-the-scene, case study, milestone). Kích hoạt khi người dùng nói: "viết bài LinkedIn công ty", "LinkedIn company page", "content LinkedIn B2B", "viết LinkedIn employer brand", "content LinkedIn doanh nghiệp", "viết bài LinkedIn", "LinkedIn marketing", "viết post LinkedIn". Output là Markdown 8-12 bài kèm lịch.
---

# Bài LinkedIn Company Page — Employer + Product

## Mục Tiêu
Xây hình ảnh chuyên gia ngành + nhà tuyển dụng hấp dẫn trên LinkedIn, tăng follow company page 20%/tháng, tăng inbound lead B2B và CV ứng viên.

## Khi Nào Dùng
- Doanh nghiệp B2B muốn nuôi LinkedIn page
- Tuyển dụng quy mô lớn
- Ra mắt sản phẩm B2B / SaaS
- Sau khi gọi vốn / đạt milestone
- Đẩy ABM cùng sales

## Bước 1: Brief Page
Hỏi:
1. Lĩnh vực + audience B2B
2. Số nhân sự + giai đoạn công ty
3. Mục tiêu LinkedIn (followers/leads/ứng viên)
4. Sản phẩm/dịch vụ chủ lực
5. Milestone 3 tháng tới (ra mắt, gọi vốn, event)
6. Founder/key leaders để tag

## Bước 2: Phân Bổ 4 Dạng Bài
8-12 bài/tháng chia:
- 3-4 bài Thought Leadership (insight ngành từ leader)
- 2-3 bài Behind-the-scene (văn hóa, team, sự kiện)
- 2 bài Case Study khách hàng
- 1-2 bài Product Update / Hiring

## Bước 3: Viết Từng Bài
Cấu trúc post LinkedIn 1300-1500 ký tự:
- Hook 2 dòng đầu (vì IG auto truncate)
- Câu chuyện / số liệu / contrarian view
- 3-5 bullet/insight
- Câu hỏi mở để tăng comment
- CTA mềm (follow page / xem link)
- 3-5 hashtag cuối

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tra số liệu ngành VN/global
- WebFetch: lấy nội dung báo cáo industry
- LinkedIn MCP / API connector (nếu có): schedule post
- Google Drive MCP: lưu file copy
- Notion MCP: lưu vào content hub

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tạo share UGC post qua LinkedIn API
import requests
headers = {'Authorization':f'Bearer {TOKEN}',
  'X-Restli-Protocol-Version':'2.0.0'}
body = {'author':f'urn:li:organization:{ORG_ID}',
  'lifecycleState':'PUBLISHED',
  'specificContent':{'com.linkedin.ugc.ShareContent':{
    'shareCommentary':{'text':content},
    'shareMediaCategory':'NONE'}},
  'visibility':{'com.linkedin.ugc.MemberNetworkVisibility':'PUBLIC'}}
requests.post('https://api.linkedin.com/v2/ugcPosts',
  headers=headers, json=body)
```

## Bước 5: Output Format
- File `.md` 8-12 bài đầy đủ
- Lịch đăng tháng (ngày + giờ)
- Hình ảnh/carousel brief cho designer
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ 8-12 bài
- [ ] 4 dạng phân bổ cân đối
- [ ] Mỗi bài 1300-1500 ký tự
- [ ] Hook 2 dòng đầu mạnh
- [ ] Có câu hỏi tăng engagement
- [ ] Đã tag executive/employee
