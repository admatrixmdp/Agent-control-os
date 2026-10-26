---
name: sales-demo-script
description: |
  Soạn script demo SaaS/sản phẩm 30 phút theo công thức Tell-Show-Tell, có hook, 3 use case theo persona, trial close và CTA next step. Trigger phrases: "script demo SaaS", "kịch bản demo sản phẩm", "soạn demo 30 phút", "demo script B2B", "demo product script", "kịch bản demo bán hàng", "demo cho khách hàng", "viết flow demo", "trial close demo", "demo cá nhân hoá". Output là Markdown script + Slide deck + checklist.
---

# SaaS/Product Demo Script Builder

## Mục Tiêu
Tạo script demo 30 phút cá nhân hoá theo persona/pain KH, tránh "feature dump", tối ưu tỷ lệ demo→proposal >40% bằng công thức Tell-Show-Tell và trial close giữa demo.

## Khi Nào Dùng
- AE chuẩn bị demo cho enterprise prospect
- Onboard SE/Solution Consultant mới
- Launch feature mới cần demo update
- Demo cho persona mới (CFO/CIO/Ops)
- Demo cứu deal late-stage

## Bước 1: Pre-demo Discovery Recap (5 phút)
Mở demo bằng recap pain KH đã chia sẻ:
- "Lần trước anh nói 3 pain: A, B, C. Hôm nay em sẽ show cách tool giải quyết đúng 3 cái này, OK không?"
- Confirm ai đang dự (role) + thời gian thực có
- Set expectation: "20 phút em show, 10 phút Q&A"

## Bước 2: Demo Flow Tell-Show-Tell (20 phút)

**Use case 1 (7 phút)** — pain quan trọng nhất KH:
- **Tell** (1 phút): "Đây là cách tool giải quyết pain X"
- **Show** (4 phút): click thật vào sản phẩm, KHÔNG screenshot tĩnh
- **Tell** (2 phút): "Vậy là anh sẽ tiết kiệm <metric>" + trial close: "Nó có giải quyết pain A của anh không?"

**Use case 2 (7 phút)**: pain thứ 2 — workflow khác

**Use case 3 (6 phút)**: pain thứ 3 hoặc differentiator vs đối thủ KH đang xài

Mỗi use case PHẢI có trial close cuối.

## Bước 3: Close + Next Step (5 phút)
- Recap 3 use case + outcome đo được
- Trial close: "Trên thang 1-10, anh thấy giải pháp này fit pain bao nhiêu?"
- Đặt next step cụ thể: proposal trong 3 ngày / POC 2 tuần / meeting với CFO
- Gửi follow-up email trong 2h sau demo có recap + link record + next step

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Gong/Chorus MCP: ghi demo + tạo summary AI
- Calendar MCP: book next meeting ngay khi KH đồng ý
- Salesforce/HubSpot MCP: log demo + update stage
- Slack MCP: alert team SE/CSM về deal nóng

**Fallback API:**
```python
# Zoom API tạo recording + share
import requests
r = requests.post("https://api.zoom.us/v2/users/me/recordings",
    headers={"Authorization": f"Bearer {token}"})
# Push transcript vào Salesforce
sf.Opportunity.update(opp_id, {"DemoNotes__c": transcript,
    "Stage": "Proposal"})
```

## Bước 5: Output Format
- **File 1**: `demo_script_<persona>.md` — script 30 phút từng phút
- **File 2**: `demo_deck_<product>.pptx` — 10 slide hỗ trợ (chỉ dùng khi cần)
- **File 3**: `demo_checklist.md` — pre-demo prep + post-demo action
- **File 4**: `demo_followup_email.md` — template email recap
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Recap discovery pain ở mở demo
- [ ] 3 use case match đúng 3 pain KH
- [ ] Mỗi use case có trial close
- [ ] Demo dữ liệu thật/sample sạch (không lỗi)
- [ ] Có next step cụ thể + deadline cuối demo
- [ ] Follow-up email gửi trong 2h sau demo
