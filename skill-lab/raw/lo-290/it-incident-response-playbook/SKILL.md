---
name: it-incident-response-playbook
description: |
  Soạn playbook ứng cứu sự cố ATTT theo chuẩn NIST: Preparation → Detection → Containment → Eradication → Recovery → Lessons Learned. Phù hợp các sự cố phishing, ransomware, rò rỉ data, DDoS, account compromise.
  Kích hoạt khi người dùng nói: "playbook ứng cứu sự cố", "incident response", "IR plan", "kế hoạch xử lý ransomware", "xử lý phishing", "playbook ATTT", "quy trình ứng phó sự cố mạng", "security incident plan", "đối phó tấn công mạng", "data breach response".
  Output là playbook Markdown + flowchart + form báo cáo.
---

# IT Security Incident Response Playbook Builder

## Mục Tiêu
Khi xảy ra sự cố ATTT, đội IT không bị loạn — có sẵn playbook chi tiết "bước 1 làm gì, gọi ai, log gì" theo chuẩn NIST SP 800-61. Giảm 80% thời gian phản ứng (MTTR).

## Khi Nào Dùng
- Lập kế hoạch ATTT lần đầu, cần playbook nền tảng
- Vừa bị sự cố, cần rút kinh nghiệm xây playbook
- Audit ISO 27001 / SOC 2 yêu cầu IR plan
- Mua bảo hiểm cyber, cần chứng minh có IR plan
- Tabletop exercise (diễn tập trên giấy) hàng quý

## Bước 1: Phân Loại Sự Cố
Chia 6 nhóm sự cố chính, mỗi nhóm 1 playbook riêng:
1. **Phishing / BEC** (Business Email Compromise)
2. **Malware / Ransomware**
3. **Account Compromise** (lộ password, MFA bypass)
4. **Data Breach / Leak** (rò rỉ dữ liệu khách hàng)
5. **DDoS / Service Outage**
6. **Insider Threat** (NV nội bộ rò rỉ/phá hoại)

Xếp mức độ nghiêm trọng:
- **SEV1**: Hệ thống chính ngừng, data leak >10K khách → CEO biết ngay
- **SEV2**: Một phòng ban ảnh hưởng → Manager IT điều hành
- **SEV3**: Cá nhân/máy lẻ → IT thường xử lý

## Bước 2: Xây 6 Bước NIST Cho Mỗi Playbook
**P-Preparation**: chuẩn bị tool (EDR, SIEM, backup), team, kênh liên lạc backup (Signal/SMS khi Slack chết)

**D-Detection & Analysis**: dấu hiệu nhận biết, source phát hiện (alert SIEM/user report/external notification), triage trong 15'

**C-Containment**:
- Short-term: cô lập máy nhiễm, disable account
- Long-term: vá lỗ hổng, thay password toàn bộ user bị ảnh hưởng

**E-Eradication**: xoá malware, đóng backdoor, reset toàn bộ token/key

**R-Recovery**: restore từ backup sạch, monitor 72h sau khôi phục, xác nhận về hoạt động bình thường

**L-Lessons Learned**: postmortem trong 7 ngày, root cause, action items, update playbook

## Bước 3: Bảng Phân Vai & Liên Lạc Khẩn
Định nghĩa team:
- **Incident Commander** — quyết định, thường là Head of IT
- **Tech Lead** — chỉ đạo kỹ thuật
- **Comms Lead** — liên lạc nội bộ + báo chí
- **Legal** — đánh giá nghĩa vụ thông báo (NĐ 13/2023: 72h)
- **HR** — nếu liên quan NV nội bộ

Tạo bảng số ĐT khẩn 24/7, kênh backup, mẫu thông báo email cho khách.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Slack MCP: kênh #incident-response private, bot auto-create channel khi SEV1
- Linear MCP: mỗi incident là 1 project, sub-tasks theo NIST phases
- Notion MCP: knowledge base playbooks, dễ tra cứu khi nóng
- Gmail MCP: gửi thông báo theo template (khách hàng, cơ quan chức năng)
- GitHub MCP: lưu playbook as code, version control, PR review
- WebSearch: tra CVE mới, IOC (indicator of compromise)
- WebFetch: pull thông tin threat intel từ AlienVault OTX, AbuseIPDB

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tự động cô lập máy nhiễm qua EDR (CrowdStrike)
import requests
TOKEN = "..."
HEADERS = {"Authorization": f"Bearer {TOKEN}"}
# Network containment device
host_id = "abc123"
r = requests.post(
    "https://api.crowdstrike.com/devices/entities/devices-actions/v2",
    params={"action_name": "contain"},
    json={"ids": [host_id]}, headers=HEADERS)
```

## Bước 5: Output Format
- File chính: `IR_Playbook_Master.md` (index + 6 playbooks)
- Mỗi playbook: `IR_Playbook_<Phishing|Ransomware|...>.md`
- Flowchart Mermaid embed sẵn trong playbook
- Form: `Incident_Report_Form.md` (template fill khi xảy ra)
- Postmortem template: `Postmortem_Template.md`
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/ir-playbooks/`

## Checklist Trước Khi Giao
- [ ] Có đủ 6 playbook theo loại sự cố
- [ ] Mỗi playbook đủ 6 bước NIST
- [ ] Bảng SEV1/2/3 rõ ràng, có ví dụ
- [ ] Danh bạ khẩn 24/7 đã verify số ĐT
- [ ] Kênh liên lạc backup (Signal/SMS) đã setup
- [ ] Template thông báo khách hàng tiếng Việt + Anh
- [ ] Đã chạy tabletop exercise ít nhất 1 lần
- [ ] Lưu offline 1 bản (in giấy) phòng khi mất mạng
