---
name: ceo-investor-update
description: |
  Tạo email + PDF update gửi nhà đầu tư hàng tháng theo chuẩn YC/Sequoia — gồm MRR, growth, churn, runway, cash, hire, ask. Format ngắn 500-800 từ để VC đọc trong 3 phút.
  Kích hoạt khi người dùng nói: "investor update", "update nhà đầu tư", "email VC tháng này", "monthly investor letter", "báo cáo nhà đầu tư", "update cho cổ đông", "VC update", "monthly update startup".
  Output là email Markdown + PDF đính kèm.
---

# CEO Investor Update — Update Nhà Đầu Tư Tháng

## Mục Tiêu
Founder phải gửi update cho VC mỗi tháng để giữ niềm tin + dễ raise round sau. Skill này tạo letter chuẩn YC trong 20 phút thay vì 2 ngày.

## Khi Nào Dùng
- Đầu tháng (5-7 hàng tháng) gửi update tháng trước
- Sau milestone lớn (close deal to, ra mắt sản phẩm)
- Trước khi mở round mới (warm-up VC)
- Khi cần bridge financing

## Bước 1: Pull 8 Số Cốt Lõi
1. MRR / ARR cuối tháng
2. % growth MoM
3. Net revenue retention (NRR)
4. Logo churn %
5. CAC payback (tháng)
6. Cash balance
7. Net burn tháng
8. Runway (tháng còn lại)

So sánh với tháng trước + plan đầu năm.

## Bước 2: Cấu Trúc Letter Chuẩn
```
Subject: [Company] Investor Update — [Month YYYY]

TL;DR (3 bullet)

The Good
- 3-5 bullet thành tựu, có số

The Bad
- 1-3 bullet không che giấu

Key Metrics (table)
MRR / Growth / NRR / Cash / Runway

What's Next (3 priorities tháng tới)

Asks
- Intro to [tên cụ thể]
- Hire [vị trí] — biết ai giới thiệu không
- Feedback về [chiến lược]

Cheers,
[CEO]
```

## Bước 3: Quy Tắc Tone
- Honest > hype: không phóng đại
- Specific > vague: tên người, số chính xác
- Asks rõ ràng: VC không đọc ý ẩn
- Tổng 500-800 từ, không quá dài
- Không markdown phức tạp — VC đọc trên iPhone

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: pull file financial close monthly
- Stripe/billing (qua sheets export): MRR, churn
- Gmail MCP: `create_draft` từng email riêng cho từng investor
- Notion MCP: lưu archive update qua các tháng
- HubSpot MCP (nếu có): pull NRR

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Stripe API: tính MRR
import stripe
stripe.api_key = 'sk_...'
subs = stripe.Subscription.list(status='active', limit=100)
mrr = sum(s.items.data[0].price.unit_amount / 100 for s in subs.auto_paging_iter())
```

## Bước 5: Output Format
- Email Markdown 500-800 từ
- PDF version đẹp hơn cho board attach (1-2 trang)
- Tên: `investor-update-YYYY-MM.md` + `.pdf`
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`
- Gửi qua Gmail draft, BCC cá nhân từng investor (không dùng list email — riêng tư)

## Checklist Trước Khi Giao
- [ ] Có đủ 8 số metric cốt lõi
- [ ] So sánh MoM rõ ràng
- [ ] Có cả "the bad" để build trust
- [ ] Asks rất cụ thể (tên người/vị trí)
- [ ] Dưới 800 từ
- [ ] BCC từng người riêng, không reveal investor list
