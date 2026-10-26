---
name: ceo-public-speech
description: |
  Soạn bài diễn thuyết CEO 10-20 phút cho hội nghị/sự kiện — hook mở đầu, 3 message chính, story minh hoạ, CTA. Format có speaker notes & timing.
  Kích hoạt khi người dùng nói: "soạn bài diễn thuyết", "viết speech CEO", "bài keynote", "speech hội nghị", "bài phát biểu", "speech CEO", "public speech writer", "keynote address".
  Output là Markdown speech + speaker notes.
---

# CEO Public Speech — Bài Diễn Thuyết CEO

## Mục Tiêu
CEO được mời keynote = cơ hội PR + recruiting + thought leadership. Skill này tạo speech 10-20 phút có cấu trúc TED-style trong 2h thay vì 2 tuần.

## Khi Nào Dùng
- Keynote hội nghị ngành
- Toastmaster / business event
- Annual all-hands
- Customer conference
- University guest speaker
- Podcast / panel

## Bước 1: Thu Thập Input
- Sự kiện: tên, ngày, audience (số người, profession)
- Topic được mời nói
- Thời lượng (10/20/30/45 phút)
- Mục tiêu (PR / recruit / educate / sell)
- CEO style (formal/casual, có/không humor)
- 3 stories CEO có sẵn có thể dùng

## Bước 2: Cấu Trúc TED-Style
```
1. HOOK (30s) — câu chuyện shock / số gây giật / câu hỏi
2. THESIS (30s) — 1 câu "Tôi đến đây để nói với bạn rằng X"
3. CONTEXT (1 phút) — tại sao topic quan trọng bây giờ
4. POINT 1 (3-4 phút) — argument + story + data
5. POINT 2 (3-4 phút) — argument + story + data
6. POINT 3 (3-4 phút) — argument + story + data
7. SO WHAT (1 phút) — ý nghĩa cho audience
8. CTA (30s) — call to action cụ thể
9. CLOSING (30s) — câu kết memorable
```

Tổng 12-15 phút nói (10-20 phút tuỳ tốc độ).

## Bước 3: Quy Tắc Viết Speech (Khác Viết Bài)
- Viết để NÓI, không phải để đọc
- Câu ngắn (≤ 15 từ)
- Lặp lại key phrase 3 lần
- Dùng "you" liên tục để engage
- Story > data (data hỗ trợ story)
- 1 message chính = 7 từ memorable
- Pause được mark trong notes [...]
- Avoid jargon, định nghĩa nếu phải dùng

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tham khảo TED talk top ngành, story validate
- WebFetch: lấy thông tin event + attendee
- Notion MCP: lưu speech archive + audience feedback
- Google Drive MCP: pull data thực tế từ Sheets
- Gmail MCP: gửi pre-talk note cho organizer

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Đếm từ + ước lượng timing
text = open('speech.md').read()
words = len(text.split())
duration_minutes = words / 130  # tốc độ nói TB 130 wpm
print(f"Speech: {words} từ ≈ {duration_minutes:.1f} phút")
```

## Bước 5: Output Format
- Markdown speech với:
  - Body speech
  - Timing mỗi section [00:00 - 03:00]
  - Pause + emphasis mark
  - Slide cue [SLIDE 3]
- Speaker notes 1 trang (key phrases để cầm)
- Slide deck 8-12 visual support
- 1-page summary cho organizer trước event
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/speech-[event].md`

## Checklist Trước Khi Giao
- [ ] Đúng thời lượng yêu cầu ±2 phút
- [ ] Có hook mở đầu mạnh
- [ ] 3 points rõ ràng
- [ ] Mỗi point có story
- [ ] CTA cụ thể cuối
- [ ] Đã rehearse ít nhất 3 lần
- [ ] Có backup plan nếu mất slide
