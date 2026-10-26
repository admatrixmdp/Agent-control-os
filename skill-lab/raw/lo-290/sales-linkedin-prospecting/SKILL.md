---
name: sales-linkedin-prospecting
description: |
  Soạn chuỗi outreach LinkedIn Sales Navigator (connect note + InMail + follow-up) cá nhân hoá theo role, hashtag, recent post của prospect. Trigger phrases: "outreach LinkedIn", "LinkedIn Sales Navigator", "connect note LinkedIn", "InMail B2B", "prospecting LinkedIn", "soạn tin nhắn LinkedIn bán hàng", "kết nối khách hàng LinkedIn", "viết InMail", "chiến lược LinkedIn outbound", "tạo cadence LinkedIn". Output là Markdown sequence + Excel list lead có dòng note riêng.
---

# LinkedIn Sales Navigator Outreach Builder

## Mục Tiêu
Tạo cadence 4-touch LinkedIn (View → Connect note → InMail → Follow-up) đạt accept rate >35% và reply rate >12% bằng cá nhân hoá ở 3 lớp: role, content, mutual.

## Khi Nào Dùng
- Penetrate enterprise account (Fortune 500/VN top 100)
- ABM outbound cho top 50 KH chiến lược
- Tiếp cận persona khó qua email (CTO, VP Eng)
- Reactivate connection cũ chưa nói chuyện >1 năm
- Tuyển distributor/đối tác qua LinkedIn

## Bước 1: Phân tích Prospect 3 lớp
Trước khi viết, lấy từ profile:
- **Role layer**: title, tenure, công ty trước
- **Content layer**: 3 post gần nhất, hashtag thường dùng, comment trên post người khác
- **Mutual layer**: connection chung, group chung, alumni

Lưu vào file `prospect_<name>.md` để tham chiếu khi viết.

## Bước 2: Viết Cadence 4-touch

**Touch 1 (Day 0) — View profile + Like 1 post gần**: không spam, tạo familiarity

**Touch 2 (Day 1) — Connect Note <300 ký tự**:
"Chào anh Minh, em đọc post của anh về <chủ đề> tuần trước, đặc biệt câu <quote>. Em đang làm <field> tương tự bên <industry>, em xin kết nối học hỏi."
→ Không pitch sản phẩm ở connect note.

**Touch 3 (Day 4 sau accept) — Message giá trị**:
Gửi 1 resource liên quan đến pain (case study PDF / báo cáo ngành), KHÔNG bán.
"Em vừa thấy báo cáo này về <topic> 2026, gửi anh tham khảo. Nếu có vibe em rất muốn nghe góc nhìn của anh."

**Touch 4 (Day 9) — Soft CTA**:
"Anh có open 20 phút chia sẻ về <topic> không? Em đang research và muốn nghe lens của anh trước khi đưa ra góc nhìn."

## Bước 3: InMail dự phòng (nếu connect bị từ chối)
- Subject <50 ký tự, đặt câu hỏi hoặc reference post
- Body <150 từ, dùng công thức P-R-O: Personal hook → Reason → Open question
- Không pitch sản phẩm trong InMail đầu tiên

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- LinkedIn Sales Navigator (qua browser MCP / Chrome): pull lead list, save search
- WebFetch: đọc bài blog/post LinkedIn cá nhân hoá insight
- HubSpot/Salesforce MCP: log activity LinkedIn vào CRM
- Apollo/Lusha MCP: enrich email + phone cho prospect

**Fallback API:**
```python
# Apollo people search
import requests
r = requests.post("https://api.apollo.io/v1/mixed_people/search",
    headers={"X-Api-Key": KEY},
    json={"q_organization_domains": "company.com",
          "person_titles": ["VP Sales", "Head of Sales"],
          "page": 1, "per_page": 25})
leads = r.json()["people"]
```

## Bước 5: Output Format
- **File 1**: `linkedin_cadence_<vertical>.md` — 4 touch + InMail dự phòng + variable
- **File 2**: `linkedin_leadlist_<vertical>.xlsx` — cột: Name, Company, Title, LinkedIn URL, Personalization note (3 dòng), Status
- **File 3**: `linkedin_templates_library.md` — 5 connect note variants test A/B
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Connect note <300 ký tự, không pitch sản phẩm
- [ ] Có ít nhất 1 personalization thật trong mỗi touch
- [ ] Touch 3 gửi giá trị trước khi CTA
- [ ] InMail subject <50 ký tự
- [ ] Cadence không quá 4 touch trong 14 ngày (tránh spam)
- [ ] Tất cả lead có note riêng (không generic)
