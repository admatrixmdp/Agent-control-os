---
name: fin-grant-application-writer
description: |
  Viết hồ sơ xin hỗ trợ từ chính phủ (Quỹ Đổi Mới Công Nghệ, Quỹ phát triển KHCN), tổ chức
  quốc tế (USAID, JICA, GIZ) hoặc quỹ tư nhân. Trigger phrases: "viết hồ sơ xin grant",
  "grant application", "xin tài trợ chính phủ", "Quỹ NATIF", "Quỹ SME", "JICA grant",
  "viết proposal grant", "đề xuất xin hỗ trợ", "innovation fund", "soạn hồ sơ xin vốn ưu đãi".
  Output là PDF hồ sơ + Excel budget detail.
---

# Viết Hồ Sơ Xin Hỗ Trợ Chính Phủ / Quỹ Phát Triển

## Mục Tiêu
Giúp SME Việt Nam tiếp cận nguồn vốn không hoàn lại / lãi suất ưu đãi từ các quỹ - tăng
tỷ lệ duyệt từ 10% lên 30-50% bằng cách viết đúng format yêu cầu, đầy đủ tài liệu,
matching đúng tiêu chí.

## Khi Nào Dùng
- Khi có dự án innovation, R&D, chuyển đổi số
- Khi DN đáp ứng tiêu chí ngành ưu tiên (xanh, KHCN, nông nghiệp công nghệ cao)
- Khi cần vốn lưu động ưu đãi lãi suất
- Khi mở rộng thị trường xuất khẩu
- Khi tuyển/đào tạo nhân lực có chính sách hỗ trợ

## Bước 1: Map Dự Án Với Quỹ Phù Hợp
**Các quỹ phổ biến VN:**
| Quỹ | Ngành ưu tiên | Mức hỗ trợ | Yêu cầu chính |
|-----|---------------|------------|---------------|
| NATIF (Quỹ Đổi mới CN QG) | KHCN, R&D | ≤30% chi phí, max 10 tỷ | Có sáng chế, technology readiness |
| SBA (Quỹ DNNVV) | Mọi ngành | Vay lãi 4-6% | DNNVV, có TS đảm bảo |
| NAFOSTED | Nghiên cứu cơ bản | 50-500tr | Đề tài KH, có cán bộ R&D |
| BUSCO (Bộ KH&ĐT) | Khởi nghiệp ĐMST | 30tr-1 tỷ | Startup <5 năm |
| JICA/KOICA | Phát triển bền vững | $50K-1M | Tác động xã hội rõ |
| USAID Vietnam | Tăng trưởng bao trùm | $20K-500K | Đối tượng yếu thế |

**Quy trình map:**
1. List 5-10 quỹ phù hợp
2. Đọc kỹ TOR/RFP từng quỹ
3. Chọn 2-3 quỹ match tốt nhất
4. Phân bổ effort tránh dàn trải

## Bước 2: Cấu Trúc Hồ Sơ Chuẩn
**Phần 1 - Thông tin DN:**
- ĐKKD, MST, quy mô, lịch sử
- BCTC 3 năm gần nhất (đã kiểm toán nếu có)
- Cơ cấu cổ đông, ban lãnh đạo

**Phần 2 - Đề xuất dự án:**
- Tên, mục tiêu, scope
- Bối cảnh: vấn đề - giải pháp - tính cấp thiết
- Đối tượng hưởng lợi
- Tính sáng tạo, khác biệt với hiện tại
- Tính khả thi: tech, thị trường, tài chính

**Phần 3 - Kế hoạch thực hiện:**
- Lộ trình 12-36 tháng (Gantt chart)
- Milestone với deliverable cụ thể
- Đội ngũ thực hiện (CV chính)

**Phần 4 - Budget:**
- Tổng đầu tư - DN tự có - xin tài trợ
- Phân bổ theo hạng mục (nhân công, thiết bị, NVL, dịch vụ)
- Phân bổ theo thời gian

**Phần 5 - Impact & sustainability:**
- KPI đo lường (số việc làm tạo, doanh thu, sáng chế...)
- Plan sau khi grant kết thúc (sustain ra sao)

## Bước 3: Đáp Ứng Đúng Tiêu Chí Chấm Điểm
Hầu hết quỹ có rubric chấm theo % weight:
- Tính sáng tạo: 20-30%
- Tính khả thi: 20%
- Năng lực đội ngũ: 15-20%
- Impact: 20-25%
- Sustainability: 10-15%

**Tip cao điểm:**
- Viết theo ngôn ngữ TOR (lặp lại keyword họ dùng)
- Có số liệu cụ thể, tránh "rất lớn", "đáng kể"
- Có letter of support từ KH/partner
- Có IP/sáng chế / nghiên cứu sơ bộ chứng minh năng lực

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: Lưu hồ sơ, version control, share team viết chung
- WebFetch: Pull TOR/RFP từ trang quỹ (natif.vn, jica.go.jp/vietnam)
- WebSearch: Tra case study dự án đã được duyệt cùng quỹ
- Gmail MCP: Liên lạc đầu mối quỹ, nộp hồ sơ điện tử

**Fallback bằng API:**
```python
# Crawl danh sách dự án đã duyệt từ NATIF để học format
import requests
from bs4 import BeautifulSoup

r = requests.get("https://natif.vn/du-an-da-duyet")
soup = BeautifulSoup(r.text, "html.parser")
projects = []
for item in soup.select(".project-item"):
    projects.append({
        "name": item.select_one("h3").text.strip(),
        "funding": item.select_one(".funding").text.strip(),
        "industry": item.select_one(".industry").text.strip()
    })
print(f"Có {len(projects)} dự án thành công - analyse format")
```

## Bước 5: Output Format
1. **PDF hồ sơ chính** (`grant_<quỹ>_<dự_án>.pdf`): 30-50 trang theo format yêu cầu quỹ, có TOC, số trang, header/footer.
2. **Excel budget detail** (`budget_<dự_án>.xlsx`): Sheet "Total", "ByCategory", "ByQuarter", "Counterpart" (đóng góp DN), "Procurement" (nếu mua sắm).
3. **PPTX defense deck** (`grant_defense.pptx`): 15-20 slide cho buổi present trước hội đồng.

Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/grant/`

## Checklist Trước Khi Giao
- [ ] Đúng template + định dạng file quỹ yêu cầu
- [ ] Có đủ tài liệu kèm (BCTC, ĐKKD, CV, MOU...)
- [ ] Budget khớp tổng với phần đề xuất
- [ ] Có letter of support, MOU từ partner
- [ ] Nộp đúng deadline (sớm 1 tuần để tránh sự cố)
- [ ] Có kế hoạch B (quỹ thay thế) nếu rớt
