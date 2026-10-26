---
name: hr-employer-branding-content
description: |
  Sản xuất content employer branding cho LinkedIn, Facebook Career, TikTok của doanh nghiệp Việt Nam, gồm post NV chia sẻ, behind-the-scenes, ngày làm việc, tuyển dụng viral.
  Kích hoạt khi người dùng nói: "employer branding", "content tuyển dụng", "LinkedIn Career", "Facebook tuyển dụng", "đăng tuyển TikTok", "content NV chia sẻ", "video tuyển dụng", "EVP content", "thương hiệu tuyển dụng", "career page content".
  Output là file content calendar + caption + brief quay phim + visual brief designer.
---

# HR - Content Employer Branding

## Mục Tiêu
Hấp dẫn ứng viên passive (chưa rải CV) qua kênh social. Khi pipeline mạnh, công ty trả lương thấp hơn 5-10% market vẫn tuyển được - tiết kiệm payroll tổng.

## Khi Nào Dùng
- Lập content plan tháng/quý cho HR Marketing
- Trước peak hiring season (Q1, Q3)
- Khi launch chương trình EVP (Employee Value Proposition) mới
- Khi đối thủ tuyển dụng mạnh, cần đáp trả

## Bước 1: Xác Định EVP + Audience
EVP = lý do nên gia nhập. Trả lời 4 câu:
- **Lương thưởng**: cạnh tranh ở đâu?
- **Phát triển**: cơ hội học hỏi, thăng tiến?
- **Văn hóa**: làm việc với ai, môi trường thế nào?
- **Ý nghĩa**: tạo impact gì cho XH, KH?

Persona ứng viên target:
- Tech: Senior Dev 5+ năm KN, quan tâm tech stack + growth
- Sales: Top performer ngành, tăng thu nhập + lộ trình lên Manager
- Gen Z entry: flexibility + learning + môi trường vui
- Manager: scope lớn hơn + ownership

## Bước 2: Pillar Content (5 Cụm)
1. **People Stories** (40%): NV chia sẻ hành trình, "A day in the life"
2. **Behind-the-scenes** (20%): event, party, off-site, văn phòng
3. **Achievement** (15%): giải thưởng, milestone, đối tác lớn
4. **Job posting + Q&A** (15%): tuyển dụng cụ thể, AMA với hiring manager
5. **Thought Leadership** (10%): CEO/Director chia sẻ insight ngành

## Bước 3: Content Calendar Mỗi Tháng
Cường độ:
- LinkedIn: 3 post/tuần (1 dài + 2 ngắn)
- Facebook Career: 2 post/tuần + 1 video
- TikTok: 3 video/tuần (15-30s)
- Newsletter NV cũ (alumni): 1 lần/quý

Mẫu calendar tháng:
| Tuần | LinkedIn | FB Career | TikTok |
|---|---|---|---|
| 1 | NV Sales kể câu chuyện + Hot vị trí | Behind office tour | Day-in-life NV |
| 2 | CEO insight ngành | Tuyển Tech | Bữa trưa team |
| 3 | Đạt giải thưởng | Workshop NV | Pep talk |
| 4 | AMA Hiring Manager | Sự kiện trong tháng | Funny meme công sở |

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Drive MCP: lưu content + asset
- Calendar MCP: schedule post calendar
- Gmail MCP: gửi brief cho designer / NV được phỏng vấn
- Slack MCP: notify NV mới có post nói về họ
- WebSearch: tra trending hashtag #careerVN #tuyendung

**Fallback bằng API (Social):**
```python
# Auto-post LinkedIn Company Page
import requests
post = {
    "author": f"urn:li:organization:{COMPANY_ID}",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {"text": caption},
            "shareMediaCategory": "IMAGE",
            "media": [{"status": "READY", "media": IMG_URN}]
        }
    },
    "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
}
requests.post("https://api.linkedin.com/v2/ugcPosts", json=post,
    headers={"Authorization": f"Bearer {TOKEN}",
    "X-Restli-Protocol-Version": "2.0.0"})
```

## Bước 5: Output Format
- File `.xlsx` Content Calendar tháng/quý
- File `.docx` Caption library 30+ caption ready
- File `.docx` Brief quay video TikTok + production schedule
- File `.docx` Visual brief cho designer (banner, infographic)
- File `.xlsx` Performance tracker (reach, engagement, apply attributed)
- Lưu tại: `/outputs/EmployerBranding_<thang-YYYY>.xlsx`

## Checklist Trước Khi Giao
- [ ] Có EVP rõ + persona target
- [ ] 5 pillar cân đối
- [ ] Calendar có ngày cụ thể + người sản xuất
- [ ] Mọi NV xuất hiện đã ký consent
- [ ] Caption có CTA (apply, comment, tag)
- [ ] Hashtag chiến lược (#careerVN + branded)
- [ ] Tracking link UTM về job board
- [ ] KPI: reach, engagement, # apply attributed
- [ ] A/B test 2 hook/tuần
