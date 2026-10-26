---
name: legal-cease-and-desist
description: |
  Soạn Thư Yêu cầu Chấm dứt Vi phạm (Cease & Desist Letter) chuẩn cho các trường hợp xâm phạm nhãn hiệu, bản quyền, sáng chế, bí mật kinh doanh, vi phạm hợp đồng, vu khống tại Việt Nam. Kích hoạt khi người dùng nói: "soạn thư cease desist", "thư yêu cầu chấm dứt vi phạm", "thư cảnh báo vi phạm", "C&D letter", "yêu cầu gỡ bài vi phạm", "thư đòi gỡ logo nhái", "thư xâm phạm SHTT", "thư yêu cầu ngừng cạnh tranh không lành mạnh", "thư cảnh cáo pháp lý", "thư warning". Output là file .docx + .pdf có chữ ký luật sư / đại diện pháp lý, sẵn gửi qua bưu điện hoặc email.
---

# Thư Yêu Cầu Chấm Dứt Vi Phạm (Cease & Desist)

## Mục Tiêu
Soạn thư yêu cầu chấm dứt vi phạm theo Luật SHTT 2005 (sửa đổi 2022), Luật Cạnh tranh 2018, BLDS 2015 — giúp doanh nghiệp đòi gỡ vi phạm trong 5-15 ngày mà chưa cần khởi kiện. Phần lớn trường hợp (~70%) bên vi phạm sẽ tuân thủ ngay khi nhận thư từ luật sư.

## Khi Nào Dùng
- Đối thủ dùng logo / tên thương hiệu giống của mình
- Website / fanpage copy nội dung, hình ảnh có bản quyền
- Cựu nhân viên dùng database khách hàng của công ty
- KOL / KOC nói xấu sai sự thật về sản phẩm (vu khống)
- NCC vi phạm thoả thuận độc quyền / non-compete
- Domain squatter giữ domain trùng thương hiệu

## Bước 1: Xác Định Loại Vi Phạm + Cơ Sở Pháp Lý
- **Vi phạm nhãn hiệu**: Luật SHTT Đ.129 + Đ.198 (yêu cầu ngừng + bồi thường)
- **Vi phạm bản quyền**: Luật SHTT Đ.28 + NĐ 17/2023 (mức phạt 250M-500M)
- **Cạnh tranh không lành mạnh**: Luật Cạnh tranh 2018 Đ.45 (lừa dối, gièm pha, bí mật KD)
- **Vu khống / xâm phạm danh dự**: BLDS Đ.34 + BLHS Đ.156
- **Vi phạm hợp đồng**: BLDS Đ.351 + Luật TM Đ.292

## Bước 2: Thu Thập Bằng Chứng (Evidence Pack)
- Screenshot URL vi phạm (lưu nguyên IP + timestamp)
- Lập vi bằng Thừa phát lại (Thông tư 05/2020 — giá trị chứng cứ trước toà)
- Văn bằng bảo hộ nhãn hiệu / bản quyền của mình
- Hợp đồng / NDA bị vi phạm
- Email / tin nhắn của đối tượng vi phạm
- Báo cáo thiệt hại định lượng

## Bước 3: Cấu Trúc Thư C&D (7 Phần)
1. Tiêu đề + thông tin bên gửi (công ty / luật sư đại diện + số GP hành nghề)
2. Thông tin bên nhận (cá nhân / tổ chức vi phạm — tên, địa chỉ, MST)
3. Trình bày sự việc + bằng chứng (URL, screenshot, vi bằng)
4. Căn cứ pháp lý (chỉ rõ điều luật bị vi phạm)
5. **Yêu cầu cụ thể**:
   - Chấm dứt hành vi vi phạm trong N ngày (thường 7-15 ngày)
   - Gỡ nội dung khỏi mọi nền tảng
   - Đăng đính chính công khai (nếu vu khống)
   - Bồi thường thiệt hại (kèm con số định lượng)
   - Cam kết không tái phạm bằng văn bản
6. Hậu quả nếu không tuân thủ (khởi kiện ra toà / báo cơ quan chức năng / công khai)
7. Thông tin liên hệ phản hồi + chữ ký luật sư

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: lưu bằng chứng + thư + biên nhận gửi
- Gmail MCP: gửi thư qua email (có request read receipt + DKIM verify)
- WebFetch: lưu archive URL vi phạm (qua web.archive.org để chứng cứ vĩnh viễn)
- Notion MCP: lưu case management — theo dõi response của bên vi phạm
- DocuSign MCP: ký số thư + đóng dấu thời gian (timestamp)
- WebSearch: tra cứu hồ sơ doanh nghiệp vi phạm (Cổng TT DN Quốc gia)

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Archive URL vi phạm + sinh evidence pack tự động
import requests
from datetime import datetime
import hashlib

def archive_url(url):
    # Wayback Machine - lưu snapshot vĩnh viễn
    r = requests.get(f"https://web.archive.org/save/{url}")
    archive_url = f"https://web.archive.org/web/{datetime.now().strftime('%Y%m%d%H%M%S')}/{url}"
    return archive_url

def screenshot_and_hash(url, output_path):
    # Selenium full-page screenshot + hash để chứng cứ
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get(url)
    driver.save_screenshot(output_path)
    file_hash = hashlib.sha256(open(output_path, "rb").read()).hexdigest()
    return {"url": url, "screenshot": output_path, "sha256": file_hash, "captured_at": datetime.utcnow().isoformat()}

evidence = [screenshot_and_hash(url, f"evidence_{i}.png") for i, url in enumerate(vi_phạm_urls)]
```

## Bước 5: Output Format
- File `CD_<TenBenViPham>_<yyyymmdd>.docx`: thư chính, font Times New Roman 13
- File `CD_<TenBenViPham>_<yyyymmdd>.pdf`: bản PDF có chữ ký + đóng dấu
- Thư mục `evidence/`: screenshot + URL archive + vi bằng + hash SHA256
- File `tracking.xlsx`: theo dõi response + ngày deadline + escalation
- Lưu tại `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/cease-and-desist/`

## Checklist Trước Khi Giao
- [ ] Có đủ bằng chứng (screenshot + URL archive + vi bằng nếu cần)
- [ ] Đã verify thông tin bên vi phạm (tên thật, địa chỉ, MST)
- [ ] Căn cứ pháp lý chỉ rõ điều luật (không nói chung chung)
- [ ] Yêu cầu cụ thể + thời hạn rõ ràng (7-15 ngày)
- [ ] Có cảnh báo hậu quả pháp lý (khởi kiện / báo cơ quan)
- [ ] Thư ký bởi luật sư có giấy phép hành nghề (hiệu lực tâm lý cao hơn)
- [ ] Gửi qua kênh có bằng chứng nhận (email + bưu điện chuyển phát nhanh có ký nhận)
- [ ] Có kế hoạch escalation nếu sau N ngày không phản hồi
