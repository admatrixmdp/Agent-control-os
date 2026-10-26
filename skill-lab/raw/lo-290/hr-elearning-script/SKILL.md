---
name: hr-elearning-script
description: |
  Viết script khóa e-learning nội bộ 20-40 phút cho doanh nghiệp Việt Nam, gồm voice-over, on-screen text, quiz interactive, kịch bản animation phù hợp Articulate/Rise/Camtasia.
  Kích hoạt khi người dùng nói: "script e-learning", "kịch bản khóa online", "soạn e-learning", "viết script khóa học", "voice-over e-learning", "Articulate Rise script", "kịch bản video training", "e-learning content", "Storyline script", "khóa online nội bộ".
  Output là file .docx script đầy đủ + storyboard + quiz JSON + asset list cho team production.
---

# HR - Script Khóa E-Learning Nội Bộ

## Mục Tiêu
Chuyển kiến thức nội bộ thành module e-learning 20-40 phút, học viên tự học bất cứ lúc nào, scale dễ, đo được tỷ lệ hoàn thành. Tiết kiệm 70% chi phí so với classroom.

## Khi Nào Dùng
- Onboarding compliance (security, anti-corruption, harassment)
- Product knowledge (sales được học sản phẩm mới)
- Policy training (chính sách HR, IT)
- Refresher annual (kỹ năng cần ôn hằng năm)

## Bước 1: Phân Tích Audience + Lựa Chọn Format
Hỏi:
- Đối tượng học là ai (level, background)?
- Trên thiết bị nào (desktop, mobile)?
- Có internet ổn định không (chọn streaming hay SCORM offline)?
- Cần đạt outcome gì (kiến thức, hành vi)?

Format phổ biến:
- **Voice-over Slides** (Articulate Rise): rẻ, nhanh
- **Whiteboard Animation** (Camtasia, Vyond): hấp dẫn cho concept
- **Live-action Video**: chuyên gia/sếp xuất hiện - tăng credibility
- **Interactive Branching**: cho situational training (decision-making)

## Bước 2: Storyboard Script
Cấu trúc khóa 25 phút:
| Phần | Thời lượng | Nội dung |
|---|---|---|
| Hook | 1' | Câu chuyện thật, câu hỏi gây tò mò |
| Learning Objectives | 1' | "Sau khóa bạn sẽ..." |
| Concept 1 + Example | 6' | Định nghĩa → ví dụ VN cụ thể |
| Quiz 1 (3 câu) | 2' | Kiểm tra hiểu |
| Concept 2 + Demo | 7' | Hướng dẫn từng bước |
| Quiz 2 (3 câu) | 2' | |
| Case thực tế | 4' | Tình huống VN, NV ra quyết định |
| Tóm tắt + Action | 1' | 3 takeaway + bước tiếp theo |
| Final Assessment | 5' | 10 câu, pass ≥ 80% |

## Bước 3: Viết Script Chi Tiết
Mỗi slide có 3 cột:
| Slide # | Voice-over | On-screen text + visual |
|---|---|---|
| 5 | "Hãy tưởng tượng bạn nhận email từ ngân hàng yêu cầu xác nhận mật khẩu..." | Hình email lừa đảo + highlight 3 red flag |

Quy tắc voice-over:
- 130-150 từ/phút (tiếng Việt 120-140)
- Câu ngắn, chủ động
- Xưng "bạn" tạo gần gũi
- Tránh thuật ngữ EN không cần thiết

Quy tắc on-screen:
- ≤ 6 từ/dòng, ≤ 6 dòng/slide
- Hình ảnh > text
- Có closed caption (cho NV xem im lặng)

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Drive MCP: lưu script + storyboard collaborative
- Gmail MCP: gửi cho SME (Subject Matter Expert) review nội dung
- Calendar MCP: book recording session voice talent
- WebSearch: tra giá voice-over VN + studio (VFS, Elite Voice)
- WebFetch: tải sample e-learning từ Coursera, LinkedIn Learning

**Fallback bằng API (LMS + AI voice):**
```python
# Generate voice-over bằng ElevenLabs Vietnamese / FPT.AI TTS
import requests
for slide in slides:
    r = requests.post("https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
        json={"text": slide["voiceover"], "model_id": "eleven_multilingual_v2"},
        headers={"xi-api-key": API_KEY})
    with open(f"audio/slide_{slide['id']}.mp3", "wb") as f:
        f.write(r.content)
```

## Bước 5: Output Format
- File `.docx` Full Script 20-40 trang (slide#, VO, on-screen, visual brief)
- File `.xlsx` Asset List (image, video, animation cần production)
- File `.json` Quiz bank (cho SCORM/LMS import)
- File `.pptx` Storyboard preview
- File `.docx` SME Review Form
- Lưu tại: `/outputs/Elearning_<ten-khoa>_v1.docx`

## Checklist Trước Khi Giao
- [ ] Thời lượng 20-40 phút (sweet spot)
- [ ] 3-5 LO rõ
- [ ] Có hook 30s đầu
- [ ] Có quiz mỗi 5-7 phút
- [ ] Final assessment 10 câu, pass ≥ 80%
- [ ] Voice-over ≤ 150 từ/phút
- [ ] On-screen ≤ 6 từ/dòng
- [ ] SME đã review tính chính xác
- [ ] Có closed caption
- [ ] Test trên mobile + desktop
