---
name: ceo-meeting-summarizer
description: |
  Tóm tắt transcript cuộc họp thành format chuẩn: TL;DR 3 dòng, key decisions, action items có owner, parking lot. Tự động gửi email cho người dự + tạo task Linear/Notion.
  Kích hoạt khi người dùng nói: "tóm tắt meeting", "summarize cuộc họp", "biên bản họp", "meeting notes", "tóm tắt biên bản", "action items từ họp", "meeting summary", "minutes của cuộc họp".
  Output là Markdown summary + email + Linear tasks.
---

# CEO Meeting Summarizer — Tóm Tắt Cuộc Họp

## Mục Tiêu
CEO dự 15-25 cuộc họp/tuần. Sau họp không ai viết minutes thì decision quên, action không chạy. Skill này biến transcript thành biên bản chuẩn trong 2 phút thay vì 30 phút.

## Khi Nào Dùng
- Sau leadership team meeting
- Sau board meeting
- Sau khách hàng lớn
- Sau interview ứng viên
- Sau bất kỳ cuộc nào > 30 phút

## Bước 1: Nhận Input Transcript
- Otter.ai / Fireflies / Granola transcript
- Hoặc voice recording → tự transcribe
- Hoặc notes thô của trợ lý

Hỏi: chủ đề chính cuộc họp + người tham dự nếu transcript thiếu.

## Bước 2: Cấu Trúc Summary Chuẩn
```
# [Meeting Title] — [Date]
**Người dự**: Tên 1, Tên 2, ...
**Thời lượng**: 60 phút

## TL;DR (3 dòng)
1. ...
2. ...
3. ...

## Quyết Định
- [Decision 1]: Ai chốt, lý do
- [Decision 2]: ...

## Action Items
| # | Việc | Owner | Deadline |
|---|------|-------|----------|
| 1 | ... | @nam | 30/05 |
| 2 | ... | @huyền | 03/06 |

## Discussion Highlights
- Topic 1: ý chính + ai có quan điểm gì
- Topic 2: ...

## Parking Lot (chưa quyết)
- ...
- ...

## Next Meeting
[Date, Agenda preview]
```

## Bước 3: Quy Tắc Tóm Tắt
- TL;DR ≤ 3 dòng, mỗi dòng 1 câu
- Action items phải có owner + ngày cụ thể (không "ASAP")
- Quyết định phải rõ ai chốt
- Parking lot = topic chưa kết luận, để cuộc sau
- Không paste nguyên transcript

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Gmail MCP: `create_draft` gửi summary cho người dự
- Linear MCP: tự tạo issue cho mỗi action item, assign owner
- Notion MCP: lưu vào database "Meetings" có tag chủ đề
- Slack MCP: post summary lên kênh phù hợp
- Calendar MCP: tạo event next meeting nếu cần

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Linear API tạo issues từ action items
import requests
for action in action_items:
    mutation = """
    mutation { issueCreate(input: {
        title: "%s", assigneeId: "%s", dueDate: "%s",
        teamId: "%s"
    }) { success } }""" % (action['task'], action['owner_id'], action['deadline'], team_id)
    requests.post("https://api.linear.app/graphql", json={"query": mutation}, headers=headers)
```

## Bước 5: Output Format
- Markdown file `meeting-[title]-YYYY-MM-DD.md`
- Email draft với subject "Notes: [Meeting Title] — [Date]"
- Linear issues tự tạo
- Notion page lưu trữ
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/meetings/`

## Checklist Trước Khi Giao
- [ ] TL;DR ≤ 3 dòng
- [ ] Mọi action item có owner + deadline
- [ ] Quyết định có người chốt
- [ ] Email gửi trong 24h sau cuộc
- [ ] Không leak confidential ra ngoài người dự
- [ ] Next meeting đã đặt nếu cần
