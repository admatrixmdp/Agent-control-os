---
name: hr-okr-employee-coaching
description: |
  Coach nhân viên viết OKR cá nhân quý chuẩn (Objectives + Key Results), align với OKR công ty/phòng ban, tránh đặt KR cảm tính, đảm bảo đo lường được.
  Kích hoạt khi người dùng nói: "viết OKR cá nhân", "coach OKR", "OKR quý", "OKR template", "lập OKR nhân viên", "OKR Q1 cá nhân", "hướng dẫn viết OKR", "review OKR", "soạn OKR", "OKR cho NV mới".
  Output là file .xlsx OKR Worksheet + .docx coach guide + dashboard tracking weekly.
---

# HR - Coach Nhân Viên Viết OKR Cá Nhân

## Mục Tiêu
Giúp NV chuyển từ "làm việc theo task" sang "làm việc theo outcome". OKR cá nhân tốt sẽ kéo OKR phòng ban đạt, đồng thời là input chính cho perf review.

## Khi Nào Dùng
- Đầu quý mới (T1, T4, T7, T10)
- NV mới qua thử việc, lần đầu viết OKR
- Khi OKR cũ "fake" - không phản ánh công việc thật
- Coach manager kiểm OKR team trước khi cascade

## Bước 1: Hiểu Nguyên Tắc OKR
- **Objective**: định tính, đầy tham vọng, truyền cảm hứng (vd "Trở thành kênh truyền thông số 1 ngành F&B")
- **Key Results**: định lượng, ≤ 5 KR/objective, mỗi KR có baseline → target
- Quy tắc đo: KR đạt 70% là tốt (stretch goal), 100% có thể là đặt thấp
- Phân biệt KR (outcome) vs Task (output): KR không phải "ra mắt sản phẩm X" mà là "đạt 10K user trong 90 ngày"

## Bước 2: Cascade Từ Công Ty Xuống Cá Nhân
1. Đọc OKR công ty quý
2. Xác định OKR phòng ban liên quan
3. NV chọn 2-3 Objective cá nhân hỗ trợ Objective phòng ban
4. Mỗi Objective: 3-5 KR cụ thể
5. Mỗi KR có công thức tính, nguồn dữ liệu, người sở hữu

Ví dụ NV Marketing:
- O1: Trở thành "go-to" agency cho ngành F&B
  - KR1: Ký 5 hợp đồng F&B mới (baseline 1, target 5)
  - KR2: 3 case study được pitch trên báo lớn
  - KR3: NPS khách F&B ≥ 70

## Bước 3: Coach Conversation 1-1 (30')
Câu hỏi coach hỏi NV:
- "Nếu đạt OKR này, bộ phận sẽ được gì?"
- "KR này đo bằng gì? Ai cung cấp số?"
- "Stretch hay safe? Nếu safe thì nâng lên 30%"
- "Cản trở lớn nhất là gì? Cần hỗ trợ gì?"
- "Bạn sẽ tracking hàng tuần thế nào?"

Output: OKR Worksheet được sign-off bởi NV + Manager.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Sheets MCP: master OKR tracker toàn công ty (cập nhật weekly)
- Calendar MCP: book 1-1 OKR check-in mỗi 2 tuần
- Slack MCP: bot nhắc cập nhật KR mỗi thứ 6
- Gmail MCP: gửi báo cáo OKR Quý cho leadership
- WebSearch: tham khảo OKR mẫu Google, Lazada, MoMo

**Fallback bằng API (OKR tools):**
```python
# Push vào Lattice / Workboard / Notion OKR DB
import requests
okr_entry = {
    "user": "an.nguyen",
    "quarter": "Q2-2026",
    "objective": "Trở thành go-to agency F&B",
    "key_results": [
        {"description": "Ký 5 HĐ F&B", "target": 5, "current": 1}
    ]
}
requests.post("https://api.notion.com/v1/pages", json=okr_entry,
    headers={"Authorization": f"Bearer {TOKEN}", "Notion-Version": "2022-06-28"})
```

## Bước 5: Output Format
- File `.xlsx` OKR Worksheet cá nhân (Objective | KR | Baseline | Target | Owner | Status)
- File `.docx` Coach Guide cho manager (5-7 trang)
- Dashboard `.html` tracker tỷ lệ % đạt từng KR
- Email check-in template hàng tuần
- Lưu tại: `/outputs/OKR_<NV>_<Q-YYYY>.xlsx`

## Checklist Trước Khi Giao
- [ ] Objective có cảm hứng, không generic
- [ ] Mỗi Objective có ≤ 5 KR
- [ ] Mỗi KR đo được, có công thức + nguồn data
- [ ] OKR cá nhân align với OKR phòng ban
- [ ] Có stretch (70% = tốt)
- [ ] Có lịch check-in 2 tuần/lần
- [ ] Manager đã sign-off
- [ ] Tracker đã setup
