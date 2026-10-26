---
name: fin-finance-ops-automation
description: |
  Tự động hoá quy trình kế toán bằng Make.com / Zapier + Google Sheets + ERP - loại bỏ
  manual entry, giảm sai sót, tiết kiệm 50-70% giờ kế toán. Trigger phrases:
  "tự động hoá kế toán", "finance automation", "Make.com kế toán", "Zapier accounting",
  "RPA finance", "no-code finance", "tích hợp ERP", "automate AP/AR", "kế toán không giấy",
  "digital finance ops". Output là sơ đồ workflow + Excel inventory automation +
  hướng dẫn setup.
---

# Tự Động Hoá Quy Trình Kế Toán (Make / Zapier + Sheets + ERP)

## Mục Tiêu
Phòng kế toán SME thường tốn 70-80% thời gian làm data entry thủ công. Skill này map ra
20-30 workflow tự động hoá phổ biến với no-code tools, giải phóng kế toán làm phân tích
+ tư vấn cho lãnh đạo thay vì nhập liệu.

## Khi Nào Dùng
- Phòng kế toán cần "scale" mà không tuyển thêm người
- Tỷ lệ lỗi data entry cao (>2%)
- KTT muốn chuyển sang vai trò strategic finance
- DN scale doanh thu nhưng kế toán không scale kịp
- Lương kế toán đang chiếm tỷ trọng quá lớn trong OpEx

## Bước 1: Map Pain Points & Tasks Lặp Lại
**Audit thời gian 1 tuần của kế toán:**
- Nhập hoá đơn vào sổ: X giờ
- Đối soát ngân hàng: Y giờ
- Báo cáo tổng hợp: Z giờ
- Trả lời câu hỏi NCC/KH: T giờ

**Phân loại tasks:**
- **High repetition + low judgment** → automate ngay (data entry, file moving)
- **Medium repetition + medium judgment** → semi-auto (template + human approve)
- **Low repetition + high judgment** → giữ thủ công (estimate, judgement call)

## Bước 2: Top 15 Workflows Khả Thi Nhất
| # | Workflow | Input | Tool | Output | Tiết kiệm/tháng |
|---|----------|-------|------|--------|-----------------|
| 1 | Auto-import e-invoice từ email vào sổ | Gmail | Make + MISA API | Bút toán JE | 20h |
| 2 | Sync sao kê NH → recon sheet | Open Banking API | Make + Sheets | Match table | 15h |
| 3 | Send AR aging reminder mỗi tuần | AR data | Sheets + Gmail | Email gửi KH | 5h |
| 4 | Sync sales sàn TMĐT → revenue book | Shopee/Lazada API | Make + ERP | Doanh thu daily | 10h |
| 5 | Auto-payment batch từ AP list | Sheets approved | Make + VCB API | Lệnh CK | 8h |
| 6 | Khấu hao TSCĐ tự động hạch toán | FA register | Cron + ERP | JE T01-T12 | 4h |
| 7 | Phân bổ CCDC, CP trả trước | Allocation sched | Cron + ERP | JE auto | 3h |
| 8 | Tính lương + đẩy bảng lương | HRIS | Payroll API | File net pay | 12h |
| 9 | Tạo tờ khai VAT từ e-invoice | E-invoice DB | Script Python | XML 01/GTGT | 8h |
| 10 | Reminder due date thuế, BHXH | Calendar | Calendar + Slack | Notify | 2h |
| 11 | Daily cash position report | Bank API | Sheets + Slack | Slack message | 5h |
| 12 | OCR hoá đơn giấy → entry | Photo | Mindee/AWS Textract | JSON → ERP | 10h |
| 13 | Tự sinh phiếu chi từ approval | Approval form | Make + ERP | PChi PDF | 6h |
| 14 | Đẩy biến động AR/AP về CRM | ERP | Make + CRM | Updated record | 4h |
| 15 | Báo cáo daily P&L cho CEO | ERP | Sheets + Looker | Dashboard | 5h |

**Tổng tiết kiệm:** ~120 giờ/tháng = 0.75 FTE = 12-15tr/tháng

## Bước 3: Roadmap Implement 90 Ngày
**Month 1 - Quick wins (≤ 2 ngày setup mỗi flow):**
- Flow #3, #6, #7, #10, #11 (reminder, auto JE, dashboard)

**Month 2 - Medium (≤ 1 tuần setup):**
- Flow #1, #2, #4 (email → ERP, bank recon, sales sync)

**Month 3 - Advanced (≤ 2 tuần setup):**
- Flow #5, #8, #12 (payment batch, payroll, OCR)

**Cost:**
- Make.com Pro: $16-30/tháng
- Google Workspace: đã có
- ERP API license: tuỳ MISA/FAST (3-10tr/năm)
- One-time setup: $500-2000 (tự làm) hoặc consultant $3-10K

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Make.com / Zapier: chính tool orchestration
- Gmail MCP: trigger từ email
- Google Sheets MCP: as data layer
- Google Drive MCP: lưu PDF generated
- WebSearch: tra template Make/Zapier community share

**Fallback bằng API:**
```python
# Custom workflow: email hoá đơn → OCR → tạo JE
import requests
import imaplib
import email

# 1. Pull emails từ Gmail có attachment PDF hoá đơn
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(USER, PASS)
mail.select("invoice_inbox")
_, msgs = mail.search(None, "UNSEEN")

for num in msgs[0].split():
    _, data = mail.fetch(num, "(RFC822)")
    msg = email.message_from_bytes(data[0][1])
    for part in msg.walk():
        if part.get_content_disposition() == "attachment":
            pdf = part.get_payload(decode=True)

            # 2. OCR bằng Mindee
            ocr = requests.post(
                "https://api.mindee.net/v1/products/mindee/invoices/v4/predict",
                files={"document": pdf},
                headers={"Authorization": f"Token {MINDEE_KEY}"}
            ).json()

            # 3. Tạo JE trên MISA
            je = {
                "voucher_date": ocr["prediction"]["date"]["value"],
                "supplier_taxcode": ocr["prediction"]["supplier_company_registration"][0]["value"],
                "total": ocr["prediction"]["total_amount"]["value"],
                "vat": ocr["prediction"]["total_tax"]["value"]
            }
            requests.post("https://api.misa.vn/sme/v1/purchase-invoices",
                         json=je, headers={"Authorization": f"Bearer {MISA_TOKEN}"})
```

## Bước 5: Output Format
1. **Excel automation inventory** (`automation_inventory.xlsx`): Sheet "Workflow_list" 15 flows, "ROI_calc" giờ tiết kiệm × cost rate, "Implementation_plan" theo tuần.
2. **PDF playbook** (`automation_playbook.pdf`): 20-30 trang - cho mỗi workflow: trigger, action, tool, code snippet, screenshots.
3. **HTML status dashboard** (`automation_dashboard.html`): % done, hours saved YTD, error rate, next priorities.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/automation/`

## Checklist Trước Khi Giao
- [ ] Đã audit thời gian baseline trước khi automate
- [ ] Có error monitoring: gửi alert khi workflow fail
- [ ] Có manual override - không khoá kế toán hoàn toàn vào auto
- [ ] Đã document workflow cho người kế nhiệm
- [ ] Backup data trước khi cho automation ghi vào ERP
- [ ] Có ROI tracking: giờ tiết kiệm thực tế sau 3 tháng
