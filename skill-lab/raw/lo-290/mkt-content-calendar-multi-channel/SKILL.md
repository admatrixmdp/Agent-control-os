---
name: mkt-content-calendar-multi-channel
description: |
  Lập lịch content marketing đa kênh 30 ngày cho Facebook, Instagram, TikTok, YouTube và Blog cho doanh nghiệp SME Việt Nam. Tự động hóa việc phân bổ chủ đề, định dạng, tần suất đăng và CTA cho từng kênh. Kích hoạt khi người dùng nói: "lịch content đa kênh", "content calendar 30 ngày", "kế hoạch đăng bài tháng", "phân bổ content FB IG TikTok", "lịch đăng nội dung", "content plan đa kênh", "lịch content marketing", "kế hoạch content tháng". Output là Excel có 30 dòng x 8 cột chi tiết theo ngày.
---

# Lịch Content Marketing Đa Kênh 30 Ngày

## Mục Tiêu
Giúp phòng MKT tiết kiệm 20-30 giờ lập kế hoạch mỗi tháng bằng cách tự động phân bổ chủ đề content theo kênh (FB/IG/TikTok/YouTube/Blog), đảm bảo tần suất đăng đều, không trùng lặp, có chủ đề trọng tâm theo tuần và đo lường được.

## Khi Nào Dùng
- Đầu tháng cần lên lịch content cho cả 5 kênh cùng lúc
- Doanh nghiệp mới triển khai multi-channel chưa có hệ thống lịch
- Cần phối hợp content giữa team Content - Design - Ads
- Muốn đảm bảo 4 trụ cột: Educate / Entertain / Inspire / Sell
- Chuẩn bị brief giao việc hàng loạt cho freelancer

## Bước 1: Thu Thập Thông Tin Đầu Vào
Hỏi người dùng 6 thông tin bắt buộc:
1. Ngành/sản phẩm chính
2. Đối tượng khách hàng (tuổi/giới/insight)
3. Tháng cần lập lịch (ví dụ tháng 6/2026)
4. Mục tiêu chính (brand/lead/sales)
5. Kênh đang chạy (tick các kênh FB/IG/TikTok/YouTube/Blog/Zalo)
6. Sự kiện đặc biệt trong tháng (sale, ra mắt, lễ)

## Bước 2: Phân Bổ Trụ Cột Content Theo Tuần
- Tuần 1: Educate (giáo dục thị trường) - 40%
- Tuần 2: Entertain + UGC - 30%
- Tuần 3: Inspire + Case study - 20%
- Tuần 4: Sell + CTA mạnh - 10%
Mỗi tuần chốt 1 chủ đề trọng tâm (pillar topic) để tái sử dụng cross-channel.

## Bước 3: Tạo Bảng Lịch 30 Ngày
Tạo Excel có các cột:
| Ngày | Thứ | Kênh | Format | Chủ đề | Hook | CTA | Hashtag | Người phụ trách | Trạng thái |
Tần suất đề xuất: FB 1 bài/ngày, IG 5 bài/tuần, TikTok 4 video/tuần, YouTube 1 video/tuần, Blog 2 bài/tuần.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: lưu file Excel lịch content vào folder MKT
- Notion MCP: đẩy lịch vào database Content Calendar có sẵn
- Google Calendar MCP: tạo event nhắc đăng bài theo từng ngày
- WebSearch: tra trend tháng, các ngày lễ, từ khóa hot
- WebFetch: lấy nội dung từ blog đối thủ làm tham khảo

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Đẩy lịch lên Google Sheets bằng API
import gspread
from google.oauth2.service_account import Credentials

creds = Credentials.from_service_account_file('sa.json',
    scopes=['https://www.googleapis.com/auth/spreadsheets'])
gc = gspread.authorize(creds)
sh = gc.open('Content Calendar T6/2026').sheet1
sh.update('A1', [['Ngày','Thứ','Kênh','Format','Chủ đề','Hook','CTA','Hashtag']])
sh.append_rows(rows_data)
```

## Bước 5: Output Format
- File `.xlsx` tên `Content_Calendar_T<tháng>_<năm>.xlsx`
- Sheet 1: Lịch 30 ngày
- Sheet 2: Pillar topics theo tuần
- Sheet 3: Brief cho designer (size ảnh từng kênh)
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ 30 ngày, không trùng chủ đề trong 7 ngày liên tiếp
- [ ] Mỗi kênh đạt tần suất tối thiểu
- [ ] Có CTA rõ ràng cho từng bài
- [ ] Đã chèn ngày lễ/sự kiện đặc biệt
- [ ] Đã phân công người phụ trách
- [ ] File đã sync lên Drive/Notion
