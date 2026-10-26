---
name: cs-customer-apology-letter
description: |
  Viết thư xin lỗi khách hàng chuyên nghiệp — đủ 5 yếu tố (nhận trách nhiệm, giải thích, khắc phục, bồi thường, cam kết), tone phù hợp mức độ, có chữ ký CEO khi nghiêm trọng. Dùng skill này khi người dùng yêu cầu: "viết thư xin lỗi", "apology letter", "thư xin lỗi khách", "thư xin lỗi sự cố", "official apology", "thư xin lỗi B2B", "CEO apology letter", "thư xin lỗi mass incident". Output là Word/PDF + email + Markdown bản đăng web.
---

# CS Customer Apology Letter Generator

## Mục Tiêu
Viết thư xin lỗi đúng chuẩn 5 yếu tố, giảm khả năng KH escalate báo chí/kiện, giữ uy tín brand. Có template cho 4 mức nghiêm trọng từ cá nhân đến mass incident.

## Khi Nào Dùng
- Sự cố ảnh hưởng nhiều KH (downtime, data breach, recall)
- KH VIP / KOL bị xúc phạm bởi NV
- Báo chí đưa tin tiêu cực về brand
- B2B partner threaten cancel hợp đồng
- Sản phẩm bị thu hồi / lỗi nghiêm trọng

## Bước 1: Đánh Giá Mức Độ Nghiêm Trọng
| Level | Tình huống | Người ký |
|---|---|---|
| **L1 — Cá nhân nhẹ** | 1 KH trải nghiệm tệ | Agent CSKH |
| **L2 — Cá nhân nghiêm trọng** | 1 KH VIP mất tiền lớn | CS Manager |
| **L3 — Nhóm KH** | Sự cố ảnh hưởng 100-1000 KH | Head of CS / COO |
| **L4 — Mass / Public** | Hệ thống, data breach, recall | CEO + đăng website |

## Bước 2: 5 Yếu Tố Bắt Buộc Trong Thư
1. **Nhận trách nhiệm** (không né tránh): "Chúng tôi đã sai khi..."
2. **Giải thích trung thực** (không bào chữa quá): "Nguyên nhân là..."
3. **Hành động khắc phục** (cụ thể): "Chúng tôi đã/đang làm X, Y, Z"
4. **Bồi thường** (nếu phù hợp): voucher, refund, gift
5. **Cam kết tương lai** (đo được): "Chúng tôi cam kết... và sẽ minh bạch về..."

## Bước 3: Template L4 — Mass Incident (CEO ký)
```
Kính gửi Quý Khách Hàng,

Tôi là {ten_CEO}, Tổng Giám Đốc {ten_cty}.

Vào ngày {ngay}, đã xảy ra sự cố {mo_ta_su_co} khiến {so_kh} khách
hàng gặp khó khăn khi {hau_qua}. Trước hết, tôi xin gửi lời xin lỗi
chân thành nhất tới quý khách.

VỀ NGUYÊN NHÂN:
{giai_thich_minh_bach_3_4_dong}

VỀ HÀNH ĐỘNG KHẮC PHỤC:
- Đã thực hiện: {da_lam}
- Đang thực hiện: {dang_lam}
- Sẽ hoàn tất vào: {ngay_hoan_tat}

VỀ ĐỀN BÙ:
Mọi khách hàng bị ảnh hưởng sẽ nhận {bo_thuong_cu_the}. Quý khách
không cần làm gì, chúng tôi sẽ chủ động liên hệ trong {N} ngày.

VỀ CAM KẾT:
Chúng tôi sẽ {bien_phap_phong_ngua_dai_han}. Chúng tôi sẽ cập nhật
tiến độ tại {url_status} mỗi {tan_suat}.

Một lần nữa, chúng tôi vô cùng xin lỗi và mong nhận được sự thông
cảm từ Quý khách.

Trân trọng,
{Chu_ky_CEO}
{Ten_CEO} — CEO {ten_cty}
{ngay_phat_hanh}
```

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Gmail MCP: gửi mass email cá nhân hoá tới list KH ảnh hưởng
- Google Docs/Drive MCP: tạo file Word PDF có chữ ký scan
- Slack MCP: thông báo nội bộ all-hands về thư
- WebSearch: tham khảo apology letter của brand lớn (Boeing, Vinhomes)
- WebFetch: monitor reaction sau khi đăng

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Mass apology email với cá nhân hoá
import requests, csv
def send_apology(affected_csv, template):
    with open(affected_csv) as f:
        for row in csv.DictReader(f):
            body = template.format(
                ten_kh=row["name"], ma_kh=row["customer_id"],
                bo_thuong_cu_the=row["compensation"]
            )
            # Gửi qua SendGrid/SES
            requests.post("https://api.sendgrid.com/v3/mail/send",
                headers={"Authorization": "Bearer KEY"},
                json={"personalizations": [{"to": [{"email": row["email"]}]}],
                      "from": {"email": "ceo@co.vn"},
                      "subject": "Thư xin lỗi từ CEO",
                      "content": [{"type": "text/html", "value": body}]})
```

## Bước 5: Output Format
- **File Word .docx** thư có chữ ký + logo brand
- **PDF** in giấy A4 (gửi B2B/VIP)
- **Email HTML** responsive
- **Markdown** đăng website news
- **Slide** all-hands giải thích nội bộ
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/cs-customer-apology-letter/output/`

## Checklist Trước Khi Giao
- [ ] Đủ 5 yếu tố
- [ ] Người ký đúng level
- [ ] Bồi thường cụ thể, không chung chung
- [ ] Cam kết đo được, có deadline
- [ ] Legal review trước khi gửi
- [ ] Có kế hoạch follow-up sau 7-14 ngày
