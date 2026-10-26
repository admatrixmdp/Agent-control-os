---
name: it-it-policy-writer
description: |
  Soạn thảo bộ chính sách IT và An toàn thông tin chuẩn cho doanh nghiệp Việt Nam: Acceptable Use Policy, Password Policy, MDM (Mobile Device Management), BYOD, Email/Internet Usage, Data Classification.
  Kích hoạt khi người dùng nói: "viết chính sách IT", "policy ATTT", "acceptable use policy", "chính sách mật khẩu công ty", "chính sách BYOD", "MDM policy", "soạn quy chế IT", "internal IT policy", "chính sách an toàn thông tin", "policy bảo mật cho nhân viên".
  Output là file Markdown/Word chuẩn ban hành nội bộ.
---

# IT & Information Security Policy Writer

## Mục Tiêu
Tạo bộ chính sách IT/ATTT đầy đủ, rõ ràng, dễ ban hành theo chuẩn ISO 27001 nhưng phù hợp SME Việt Nam — giúp HR/IT Manager không phải copy từ template Tây và Việt hoá thủ công.

## Khi Nào Dùng
- Doanh nghiệp mới thành lập phòng IT, cần bộ policy nền tảng
- Audit ISO 27001 / SOC 2 yêu cầu hồ sơ chính sách
- Có sự cố rò rỉ dữ liệu, cần siết policy
- Triển khai MDM/BYOD, cần văn bản ràng buộc nhân viên
- Onboarding nhân viên mới, cần policy để ký cam kết

## Bước 1: Xác Định Phạm Vi & Đối Tượng
Hỏi người dùng:
- Quy mô công ty (số NV), lĩnh vực (tài chính/y tế/thường)
- Đã có policy nào chưa? Lỗ hổng nào cần ưu tiên?
- Mức độ chặt: Cơ bản / Trung bình / Nghiêm ngặt
- Cần loại policy nào: AUP, Password, MDM, BYOD, Email, Data Classification, Incident Response

## Bước 2: Chọn Khung Tham Chiếu
Áp dụng kết hợp:
- **ISO/IEC 27001 Annex A** — danh sách 93 controls
- **NIST CSF** — Identify/Protect/Detect/Respond/Recover
- **Luật An ninh mạng VN 2018 & Nghị định 13/2023** về bảo vệ dữ liệu cá nhân
- Best practice từ SANS Policy Templates

## Bước 3: Viết Từng Policy Theo Cấu Trúc Chuẩn
Mỗi policy có 8 phần:
1. **Mục đích** — Lý do ban hành
2. **Phạm vi** — Áp dụng cho ai, thiết bị nào
3. **Định nghĩa thuật ngữ**
4. **Nguyên tắc & Quy định cụ thể** (do/don't bullets)
5. **Vai trò & Trách nhiệm** (IT Admin, Manager, Employee)
6. **Vi phạm & Chế tài** (cảnh cáo → sa thải → kiện)
7. **Tham chiếu pháp lý** (Luật ATTT, NĐ 13/2023)
8. **Hiệu lực & Review** (ban hành ngày, review hàng năm)

Ví dụ Password Policy: tối thiểu 12 ký tự, đổi 90 ngày, không reuse 5 lần gần nhất, MFA bắt buộc cho admin & VPN.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: lưu policy vào folder "IT Policies" có version control
- Notion MCP: publish dạng wiki nội bộ, mỗi policy 1 page
- Slack MCP: thông báo ban hành policy mới đến #all-staff
- GitHub MCP: lưu policy dạng repo policy-as-code, tracking diff qua PR
- WebSearch: tra cứu template ISO 27001 / NIST / SANS mới nhất
- WebFetch: tải template từ sans.org/information-security-policy

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Tự động đăng policy lên Notion
import requests
NOTION_TOKEN = "secret_..."
DB_ID = "abc123"
headers = {"Authorization": f"Bearer {NOTION_TOKEN}",
           "Notion-Version": "2022-06-28", "Content-Type": "application/json"}
data = {"parent": {"database_id": DB_ID},
        "properties": {"Name": {"title": [{"text": {"content": "Password Policy v2.0"}}]}}}
r = requests.post("https://api.notion.com/v1/pages", json=data, headers=headers)
```

## Bước 5: Output Format
- File chính: `IT_Policy_Bundle_<YYYYMMDD>.md` (master doc)
- Tách thành các file con: `01_AUP.md`, `02_Password.md`, `03_MDM.md`, `04_BYOD.md`
- Bản Word `.docx` để ký ban hành
- Bản 1 trang `Policy_Summary_OnePager.md` cho nhân viên đọc nhanh
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/it-policies/`

## Checklist Trước Khi Giao
- [ ] Mỗi policy có đủ 8 phần cấu trúc chuẩn
- [ ] Tham chiếu Luật An ninh mạng VN 2018 và NĐ 13/2023
- [ ] Có bảng phân vai (RACI) rõ ràng
- [ ] Chế tài cụ thể, không chung chung
- [ ] Có chỗ ký tên Tổng giám đốc + ngày hiệu lực
- [ ] Tạo bản tóm tắt 1 trang cho NV
- [ ] Lên lịch review hàng năm
