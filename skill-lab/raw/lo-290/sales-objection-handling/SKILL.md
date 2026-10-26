---
name: sales-objection-handling
description: |
  Playbook xử lý 20 phản đối phổ biến nhất B2B/B2C theo công thức LAER (Listen-Acknowledge-Explore-Respond) với script trả lời sẵn. Trigger phrases: "xử lý phản đối", "objection handling", "phản đối giá", "khách chê đắt", "khách nói cần suy nghĩ", "xử lý từ chối khách hàng", "phản đối sales", "khách hàng từ chối", "script xử lý objection", "xử lý khách kén chọn". Output là Markdown playbook + Excel matrix objection-response.
---

# 20 Objection Handling Playbook (LAER)

## Mục Tiêu
Trang bị cho sales 20 script xử lý phản đối thường gặp, áp dụng LAER framework để biến phản đối thành cơ hội qualify sâu hơn, tăng deal closure rate 10-15%.

## Khi Nào Dùng
- Training sales mới (tuần 1-2)
- Roleplay weekly sales meeting
- Cập nhật khi launch feature/giá mới
- Đối thủ tung campaign mới cần phản công
- Win-rate giảm do AE bị "ăn" objection

## Bước 1: Phân loại 20 Objection theo 5 nhóm

**Nhóm A — Giá (5)**:
1. "Đắt quá"
2. "Không có budget"
3. "Bên kia rẻ hơn"
4. "Giảm 30% được không"
5. "Năm sau xét"

**Nhóm B — Thời gian (4)**:
6. "Cần suy nghĩ"
7. "Q sau mới mua"
8. "Đang bận quý này"
9. "Chờ sếp về"

**Nhóm C — Authority (3)**:
10. "Phải hỏi sếp"
11. "Không phải tôi quyết"
12. "Cần đưa lên ban giám đốc"

**Nhóm D — Need (4)**:
13. "Đang xài rồi"
14. "Không cần"
15. "Tự build được"
16. "Đợi feature X có rồi tính"

**Nhóm E — Trust (4)**:
17. "Chưa nghe brand"
18. "Sợ chuyển đổi rủi ro"
19. "Cần case study cùng ngành"
20. "Lo về data security"

## Bước 2: Áp Dụng LAER cho mỗi Objection

**L — Listen**: im lặng 3s, không cắt lời
**A — Acknowledge**: "Em hiểu, nhiều KH bên em ban đầu cũng nghĩ vậy."
**E — Explore**: hỏi đào sâu — "Anh nói đắt là so với <gì>?" / "Cụ thể anh đang lo gì?"
**R — Respond**: trả lời có bằng chứng + trial close lại

Ví dụ "Đắt quá":
- L: lặng
- A: "Em hiểu, em đã nghe câu này từ <KH cùng ngành>."
- E: "Anh đang so với báo giá nào hay so với budget nội bộ?"
- R: "Bên <KH X> cùng size cũng nghĩ vậy, nhưng họ thấy ROI 6 tháng. Em chia sẻ case study được không?"

## Bước 3: Viết Response Script cho 20 Objection
Mỗi script gồm:
- Câu acknowledge (8-15 từ)
- Câu explore (1 câu hỏi mở)
- Câu respond (1 fact + 1 case + 1 trial close)
- Câu pivot (chuyển sang next step)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Gong/Chorus MCP: phân tích objection thật từ call ghi âm
- WebFetch: pull case study, ROI report làm bằng chứng
- Salesforce/HubSpot MCP: tag objection vào deal để phân tích trend
- Slack MCP: share script mới cho team

**Fallback API:**
```python
# Phân tích objection tần suất từ Gong
import requests
calls = requests.get("https://api.gong.io/v2/calls",
    headers={"Authorization": f"Bearer {token}"}).json()
objections = {}
for c in calls["calls"]:
    transcript = get_transcript(c["id"])
    for keyword in ["đắt", "suy nghĩ", "không cần"]:
        if keyword in transcript:
            objections[keyword] = objections.get(keyword, 0) + 1
```

## Bước 5: Output Format
- **File 1**: `objection_playbook.md` — 20 objection có LAER script đầy đủ
- **File 2**: `objection_matrix.xlsx` — Objection / Acknowledge / Explore / Respond / Case study link / Trial close
- **File 3**: `roleplay_scenarios.md` — 5 scenario roleplay cho team weekly
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] Đủ 20 objection chia 5 nhóm
- [ ] Mỗi response áp dụng LAER đủ 4 bước
- [ ] Có link case study cho mỗi objection nhóm Trust
- [ ] Câu trả lời <30 giây speak time
- [ ] Có roleplay weekly scenarios
- [ ] Script test với 5 AE trước rollout
