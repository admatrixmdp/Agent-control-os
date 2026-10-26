---
name: sales-cold-email-writer
description: |
  Viết chuỗi cold email B2B 3-touch sequence (intro, bump, breakup) cá nhân hoá theo ngành & ICP, tối ưu reply rate. Trigger phrases: "viết cold email", "cold email B2B", "email tiếp cận khách lạnh", "soạn email outreach", "3-touch sequence", "email prospecting", "viết email chào hàng B2B", "cadence email lạnh", "tạo email mở đầu sales", "viết breakup email". Output là file Markdown + Excel cadence sẵn import vào HubSpot/Outreach.
---

# Cold Email B2B 3-Touch Sequence Writer

## Mục Tiêu
Giúp SDR/AE viết chuỗi 3 email lạnh đạt reply rate >8% bằng cá nhân hoá ICP, trigger event và CTA mềm. Loại bỏ template chung chung, tăng số meeting đặt được mỗi tuần.

## Khi Nào Dùng
- Bắt đầu chiến dịch outbound mới cho thị trường mới
- Cần nâng cấp template cold email cũ phản hồi thấp
- Launch sản phẩm/feature mới cần tiếp cận 200-2000 lead
- AE cần personalize email cho top 50 KH chiến lược
- Reactivate khách hàng từ chối >6 tháng trước

## Bước 1: Thu thập input KH & ICP
Hỏi user về:
- Sản phẩm/dịch vụ + 1 differentiator chính
- ICP (industry, size, role, pain point cụ thể)
- Trigger event gần đây (funding, hire, expansion, regulation)
- Mục tiêu CTA (15-min call / demo / case study)
- Tone (formal/casual) & ngôn ngữ (VN/EN)

## Bước 2: Viết Email 1 — Intro (50-90 từ)
Cấu trúc:
- Subject: <8 từ, ám chỉ pain hoặc context KH>
- Hook cá nhân hoá (1 câu, nhắc trigger event)
- Pain reframe (1 câu, đảo lại quan điểm phổ biến)
- Proof point ngắn (1 con số case study cùng ngành)
- CTA mềm: "Anh/chị có open 15 phút thứ 4 hoặc 5 không?"

Ví dụ subject: "Quản lý 200 NV bán hàng Q3 — anh Minh"

## Bước 3: Viết Email 2 (Bump, +3 ngày) & Email 3 (Breakup, +7 ngày)
- **Bump**: 30-50 từ, reply trên thread cũ, thêm 1 asset (case study PDF / 2-min video)
- **Breakup**: 40-60 từ, polite goodbye + 1 câu hỏi yes/no mở cửa lại
  - Ví dụ: "Có lẽ chưa đúng thời điểm. Em có thể gửi lại Q4 không, hay chủ đề này không liên quan?"

Mỗi email PHẢI khác angle (vd email 1: pain, email 2: peer proof, email 3: ego/curiosity).

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP/Connectors:**
- Gmail MCP: tạo draft 3 email vào draft folder để SDR review trước khi gửi
- LinkedIn (qua Sales Navigator scrape): lấy thông tin role, recent post của prospect
- WebFetch: đọc website công ty KH lấy 1-2 dấu hiệu trigger event
- WebSearch: tìm tin tức funding/expansion gần nhất của KH

**Fallback API:**
```python
import requests
# Gmail API tạo draft
headers = {"Authorization": f"Bearer {token}"}
draft = {"message": {"raw": base64.urlsafe_b64encode(
    f"To: {prospect}\nSubject: {subj}\n\n{body}".encode()).decode()}}
requests.post("https://gmail.googleapis.com/gmail/v1/users/me/drafts",
              headers=headers, json=draft)
```

## Bước 5: Output Format
- **File 1**: `cold_email_<industry>_<date>.md` — 3 email full text + variables {{first_name}}, {{company}}, {{trigger}}
- **File 2**: `cadence_<industry>.xlsx` — cột: Day, Channel, Subject, Body, Owner, sẵn import HubSpot/Outreach/Apollo
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Subject <8 từ, không clickbait, không emoji
- [ ] Email 1 <90 từ, không nhắc "I/We" quá 3 lần
- [ ] Mỗi email có 1 CTA duy nhất
- [ ] Có ít nhất 1 yếu tố cá nhân hoá thật (không placeholder)
- [ ] Breakup email có câu hỏi yes/no
- [ ] Test spam score <3 (kiểm bằng Mail-Tester)
