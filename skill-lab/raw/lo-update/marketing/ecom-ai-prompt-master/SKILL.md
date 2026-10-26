---
name: ecom-ai-prompt-master
description: >
  Viết prompt chuyên nghiệp cho TẤT CẢ AI tools phục vụ TMĐT.
  Dùng khi cần: "prompt cho ảnh sản phẩm", "hướng dẫn prompt", "prompt cho video", "prompt AI tools", "cách viết prompt bán hàng", "prompt Midjourney", "prompt DALL-E", "prompt Gemini Imagen", "prompt Grok", "prompt Veo", "prompt Suno", "prompt Kling", "Seedance prompt"
---

# SKILL: Viết Prompt Chuyên Nghiệp Cho AI Tools TMĐT

## 1. NGUYÊN TẮC PROMPT ENGINEERING CỐT LÕI

### 1.1. Specificity (Chi tiết cụ thể)
**Nguyên tắc:** Càng cụ thể, kết quả càng tốt

**Sai:** "Ảnh sản phẩm"
**Đúng:** "Tấm ảnh sản phẩm kem chống nắng SPF 50+ trên nền đá cẩm thạch trắng, khay gỗ tối, điểm sáng vàng, phong cách flat lay"

**Sai:** "Video sản phẩm"
**Đúng:** "Video 15 giây, chiếc tai nghe wireless màu đen bóng, giơ tay từ từ đặt lên tai, rồi bấm nút, màn hình thắp sáng hiển thị "Connected", camera zoom từ xa tới gần, nền mờ phòng tối, góc quay 45 độ"

**Tips cụ thể hóa:**
- Camera angle: Wide, medium, close-up, overhead, 45°, eye-level
- Lighting: Studio soft, golden hour, chiaroscuro, backlighting, ring light
- Color palette: Warm, cool, vibrant, pastel, monochrome, high contrast
- Style: Minimalist, luxury, casual, vintage, futuristic, editorial
- Details: Texture, material, finish, size comparison, dimensions

### 1.2. Context (Bối cảnh)
**Lý do:** AI cần hiểu mục đích sử dụng

**Format prompt bối cảnh:**
```
Mục đích: [Bán hàng trên TikTok/Facebook/Website]
Thương hiệu: [Tên brand]
Sản phẩm: [Tên sản phẩm + loại]
Giá: [Mức giá để AI không tạo quá cao/thấp]
Target audience: [Gen Z / Chị em 25-45 / Dân văn phòng]
Nội dung hình ảnh: [Chi tiết]
```

**Ví dụ:**
```
Mục đích: Quảng cáo TikTok cho bộ sưu tập mùa hè
Thương hiệu: LUXE VIET
Sản phẩm: Áo linen trắng bản rộng
Giá: 590,000 VND
Target: Gen Z nữ, yêu thích phong cách tối giản, thích chụp ảnh lifestyle
```

### 1.3. Style (Phong cách)
**Quyền lực của phong cách:**
- Thay đổi cảm xúc của hình ảnh
- Quyết định xem có bán được hay không
- Phải match brand identity

**Style keywords thường dùng:**
- **Ảnh/Video:**
  - Photography style: Product photography, lifestyle photography, candid, editorial, minimalist, luxury
  - Art style: Oil painting, watercolor, sketch, digital art, 3D render, cinematic
  - Tone: Warm, cool, bright, moody, vibrant, muted, pastel, high-contrast

**Ví dụ style prompt:**
```
Phong cách: Product photography chuyên nghiệp, studio lighting, shallow depth of field
vs
Phong cách: Lifestyle photography, natural lighting, golden hour, bohemian aesthetic
vs
Phong cách: Cinematic, Hollywood lighting, dramatic shadows, moody, 24mm lens
```

### 1.4. Format (Định dạng)
**Tại sao format quan trọng:**
- Ảnh: Aspect ratio (1:1, 4:3, 16:9), resolution, file size
- Video: Duration, aspect ratio, resolution, FPS
- Audio: BPM, length, format, loudness level

**Format specs cần nêu:**
```
Định dạng: 1080x1080px (Instagram square), PNG, 300 DPI
vs
Định dạng: 15 giây, 9:16 (mobile), 1080p, MP4, âm thanh rõ ràng
vs
Định dạng: 30 giây, 1:1 (Instagram feed), 4K, H.264 codec
```

### 1.5. Negative Prompts (Những gì KHÔNG muốn)
**Nguyên tắc:** Nêu rõ những gì cần tránh

**Cấu trúc:**
```
Tránh: Watermark, text overlay không xấu, hỏng sản phẩm, mờ nhoè, contrast thấp, người mẫu
cứng nhắc, quần áo sai size, hư hỏng, rotted, decay, deformed, distorted, blurry, worst quality
```

**Ví dụ negative prompt hoàn chỉnh:**
```
Negative: Deformed hands/fingers, watermark, blurry background, poor lighting,
overly saturated, cheap looking, pixelated, low resolution, text overlay,
person looking unhappy, product damage, discolored, wrinkled fabric, dust,
bad composition, ugly, distorted proportions
```

---

## 2. IMAGE GENERATION PROMPTS CHO TẤT CẢ AI TOOLS

### 2.1. GEMINI IMAGEN

**Cú pháp cơ bản:**
```
[Chủ đề sản phẩm], [Mô tả chi tiết], [Phong cách], [Bối cảnh], [Điều kiện ánh sáng], [Định dạng/Chất lượng]
```

**Cấu trúc prompt Imagen:**
```
[Product name] on [background], [style], [lighting], [camera angle], [mood], shot with [camera type],
[lens], professional photography, high resolution, 8k, [color mood], [specific details]
```

**Style options cho Imagen:**
- Photography styles: Product photography, Lifestyle, Editorial, Minimalist, Luxury, Candid
- Art styles: Watercolor, Oil painting, Digital illustration, 3D render, Pencil sketch
- Lighting: Studio lighting, Golden hour, Backlighting, Neon, Dramatic, Soft natural

**Product photography prompts Imagen:**

1. **Flat lay thời trang:**
```
Prompt: "White linen shirt laid flat on warm sand-colored linen fabric,
wooden accessories beside it, soft shadows from afternoon sunlight,
minimalist composition, product photography, natural textures, clean aesthetic,
shot from directly above, high resolution, 8k, warm color grading"

Negative: "wrinkles, stains, dust, watermark, people, cluttered, dark, low quality, blurry"
```

2. **Mỹ phẩm trên bề mặt đá:**
```
Prompt: "Luxury skincare cream jar on white Carrara marble surface,
golden liquid droplets beside it, soft studio lighting from the left,
shallow depth of field, professional beauty photography, high end aesthetic,
bright and clean, 50mm lens simulation, product-focused, 8k quality"

Negative: "deformed jar, missing lid, cracked marble, cheap appearance, watermark,
blurry, overexposed, dust, discolored, wrinkled label"
```

3. **Thực phẩm overhead shot:**
```
Prompt: "Vietnamese spring rolls on a ceramic plate, peanut sauce in small glass bowl
beside it, fresh herbs (mint, cilantro) scattered artfully, overhead view (90 degrees),
natural daylight from window, warm golden tones, food styling, professional photography,
restaurant quality, steaming appearance, appetizing, shallow DOF on rolls, 8k,
high resolution"

Negative: "overcooked, dried out, brown colors, wilted herbs, messy, watermark,
low quality, blurry, unappetizing, burnt edges, dark lighting"
```

### 2.2. GROK (xAI) IMAGE GENERATION

**Đặc điểm Grok:** Nhanh, xử lý context tốt, có thể hiểu ngôn ngữ tự nhiên

**Cú pháp Grok:**
```
[Miêu tả chi tiết] trong phong cách [style], [bối cảnh], [ánh sáng],
[tâm trạng/mood], chất lượng [quality], [định dạng]
```

**Prompt examples cho Grok:**

1. **Sản phẩm công nghệ:**
```
Prompt: "Smartphone mới nhất hiển thị trên bàn kính hiện đại, đèn LED xanh
phía sau, tay cầm điện thoại, góc quay 45 độ, phong cách minimalist hiện đại,
ánh sáng studio mạnh, nền xanh đen gradient, chất lượng 8K, cinematic"

Negative: "fingerprints, scratches, watermark, blurry, low quality, wrinkled background"
```

2. **Quần áo lifestyle:**
```
Prompt: "Cô gái mặc áo hoodie màu xanh navy, ngồi trên nền tường gạch đỏ vintage,
cười tự nhiên, ánh sáng chiều tự nhiên, phong cách street style Gen Z,
phối cảnh relaxed, chất lượng cao, atmospheric, warm color grading"

Negative: "stiff pose, fake smile, watermark, blurry, unnatural lighting,
wrinkled clothes, poor quality, background distraction"
```

### 2.3. MIDJOURNEY - PARAMETERS & KEYWORDS

**Midjourney là công cụ mạnh nhất hiện tại cho TMĐT - phải nắm rõ parameters**

**Essential Midjourney Parameters:**

| Parameter | Ý nghĩa | Giá trị phổ biến |
|-----------|---------|-----------------|
| `--ar` | Aspect ratio | 1:1, 4:5, 9:16, 16:9 |
| `--v` | Version model | 6, 6.1 (mới nhất) |
| `--s` | Style strength | 0-1000 (default 100) |
| `--q` | Quality | .25, .5, 1 (default), 2 |
| `--niji` | Anime/Illustration mode | - |
| `--no` | Exclude elements | text, watermark |
| `--tile` | Seamless pattern | - |
| `--iw` | Image weight | 0-2 |

**Cấu trúc Midjourney prompt hoàn chỉnh:**
```
[Detailed description], [style keywords], [lighting], [camera], [mood/emotion],
--ar [ratio] --v 6.1 --s [style strength] --q 1
```

**Style keywords Midjourney:**
```
Photography: professional product photography, studio lighting, shallow DOF,
cinematic lighting, high end magazine, editorial style

Art: oil painting, watercolor, digital illustration, 3D render, abstract,
surreal, hyperrealistic

Mood: luxurious, minimal, elegant, bold, moody, bright, warm, cool,
dreamy, dynamic, serene
```

**Midjourney prompts cho TMĐT:**

1. **Túi xách hàng hiệu flat lay:**
```
Prompt: "Luxury leather handbag in cognac brown on white marble surface,
scattered designer accessories (sunglasses, gold watch, lipstick),
soft shadows, afternoon sunlight, minimalist composition, professional
product photography, 50mm lens, shallow depth of field, warm color grading,
high end fashion magazine aesthetic --ar 4:5 --v 6.1 --s 80 --q 1"

Negative: "--no watermark text wrinkles damage cheap"
```

2. **Sản phẩm trên lifestyle scene:**
```
Prompt: "Premium jade roller placed on marble bathroom counter next to luxury
skincare bottles, warm golden hour light from window, minimalist luxury bathroom
setting, soft shadows, professional beauty photography, shallow DOF, warm white
tones, editorial style, high resolution --ar 9:16 --v 6.1 --s 100 --q 2"

Negative: "--no watermark text blurry deformed damage"
```

3. **Fashion product on model:**
```
Prompt: "Woman wearing oversized beige linen shirt, standing against neutral
off-white wall, morning natural light from left, confident pose, relaxed elegance,
soft shadows on face, professional fashion photography, warm skin tone,
editorial magazine style --ar 4:5 --v 6.1 --s 75 --q 1"

Negative: "--no watermark text wrinkles stains unflattering unfocused"
```

### 2.4. DALL-E 3 PROMPTS

**DALL-E strengths:** Natural language understanding, các chi tiết nhỏ, text in images

**Cú pháp DALL-E:**
```
[Full descriptive sentence], [style], [mood], [technical specs], [specific details]
```

**DALL-E prompts cho TMĐT:**

1. **Mỹ phẩm product shot:**
```
Prompt: "A sleek rose gold facial serum bottle placed on a marble vanity,
surrounded by fresh pink roses and a gold-rimmed mirror, soft diffused
lighting from window, warm tones, luxury skincare aesthetic, high resolution,
professional beauty photography"
```

2. **Food product:**
```
Prompt: "A beautiful Vietnamese coffee presentation with a traditional
phin coffee maker pouring dark coffee into a white cup with condensed
milk, steam rising, warm rustic wooden table in background, natural
afternoon light, cozy Vietnamese café atmosphere, high resolution,
food styling photography"
```

3. **Tech product:**
```
Prompt: "A premium wireless earbuds case displayed on a sleek black surface,
with one earbud floating beside it, metallic reflections, studio lighting,
cool tones, modern minimalist aesthetic, professional product photography,
8K quality, shallow depth of field"
```

---

## 3. VIDEO GENERATION PROMPTS

### 3.1. GOOGLE VEO - VIDEO GENERATION

**Đặc điểm Veo:**
- Tạo video 6-60 giây
- Hiểu movement tốt
- Có thể control camera movement

**Cú pháp Veo:**
```
[Mô tả chi tiết scene], [camera movement: pan/zoom/tilt/dolly],
[duration], [style], [lighting], [emotion/mood]
```

**Cấu trúc prompt Veo chi tiết:**
```
[Action description with motion], camera [movement type] [direction],
shot duration [X seconds], [lighting condition], [color mood],
[camera type if relevant], cinematic quality, 1080p
```

**Camera movement keywords:**
- Pan: Quét ngang từ trái sang phải hoặc ngược lại
- Tilt: Quét dọc từ trên xuống hoặc ngược lại
- Dolly: Chuyển động camera tiến/lùi
- Zoom: Phóng to/thu nhỏ
- Tracking shot: Theo dõi đối tượng
- Aerial: Camera bay lên cao
- Orbit: Quay vòng quanh đối tượng

**Veo prompts cho TMĐT:**

1. **Product demo 20 giây:**
```
Prompt: "A white cosmetic serum bottle on marble counter. Camera slowly
dollies in from far to close-up of the bottle. Hand enters frame from right,
gently picks up the bottle, tilts it to show the liquid inside, liquid
shimmers under soft studio lighting. Duration 20 seconds. Warm golden hour
lighting. Luxury beauty product aesthetic. Cinematic, 1080p, professional"
```

2. **Lifestyle video 30 giây:**
```
Prompt: "Woman wearing white linen shirt putting on silver necklace while
looking in mirror. Camera starts wide, then slowly zooms in to show her
face smiling, then pans down to show the necklace catching light.
Natural window light from left side. Duration 30 seconds. Warm tones.
Slow, elegant movement. Cinematic fashion video style, 1080p"
```

3. **Unboxing animation 15 giây:**
```
Prompt: "Luxury white box with gold ribbon on neutral background. Hands
enter frame and slowly open the box. Inside reveals folded beige silk
fabric. Camera tilts down to show the product inside. Soft shadows,
studio lighting. Duration 15 seconds. Cinematic, premium aesthetic, 1080p"
```

4. **Food product showcase 25 giây:**
```
Prompt: "Vietnamese fresh spring rolls arranged on white ceramic plate.
Camera pans slowly across each roll from left to right. Wooden table
underneath, glass of peanut sauce in the background. Natural sunlight
from window. Camera pulls back to show full composition. Duration 25 seconds.
Warm, appetizing colors. Food styling professional quality, 1080p"
```

### 3.2. SEEDANCE - CHARACTER & PRODUCT ANIMATION

**Đặc điểm Seedance:**
- Tốt cho character animation
- Motion capture-like quality
- Có thể generate múi động lặp

**Cú pháp Seedance:**
```
[Character/object description], [motion: jumping/walking/floating],
[background], [style], [lighting], [duration 4-8 giây]
```

**Seedance prompts:**

1. **Product mascot animation:**
```
Prompt: "Cute cartoon character mascot representing a skincare brand,
cute round shape, pastel colors, jumping and rotating 360 degrees while
holding a skincare bottle, pink background with geometric shapes,
soft glow, playful animation style, 6 seconds, bright cheerful mood"
```

2. **Product floating animation:**
```
Prompt: "Skincare cream jar slowly rotating on its axis while floating
and gently rising up, surrounded by floating flower petals and gold particles,
white background with subtle glow, luxury animation style, smooth motion,
5 seconds, cinematic lighting, premium aesthetic"
```

### 3.3. KLING AI - VIDEO GENERATION

**Đặc điểm Kling:**
- Tạo video sắc nét cao
- Tốt cho product videos
- Có style transfer

**Cú pháp Kling:**
```
[Scene description], [motion direction], [style: photorealistic/cinematic/anime],
[duration 5-60 giây]
```

**Kling prompts:**

1. **Product reveal video:**
```
Prompt: "Sleek black smartphone appearing from darkness, rotating slowly
to reveal its design. Neon blue and purple lighting accents the edges.
Smooth 360-degree rotation. Duration 10 seconds. Photorealistic, cinematic
lighting, high quality, 1080p, tech product aesthetic"
```

2. **Beauty product video:**
```
Prompt: "Luxury liquid lipstick in deep wine color pouring into a glass
container in slow motion. Golden light refracts through the liquid.
Droplets suspended in mid-air catching light. Duration 8 seconds.
Photorealistic, dramatic lighting, premium beauty aesthetic, 1080p"
```

---

## 4. MUSIC & AUDIO PROMPTS

### 4.1. SUNO AI - MUSIC GENERATION

**Suno là AI music creator tốt nhất hiện tại cho brand music & jingles**

**Cú pháp Suno:**
```
[Thể loại nhạc], [bài hát mô tả], [phong cách vocal], [công cụ], [BPM], [tinh thần]
```

**Cấu trúc prompt Suno chi tiết:**
```
Genre: [Genre]
Mood: [Mood description]
Instruments: [Danh sách nhạc cụ]
Vocal style: [Style]
BPM: [Tempo]
Duration: [Length - usually 15s, 30s for ads]
Specific details: [Chi tiết]
```

**Suno prompts cho TMĐT:**

1. **Upbeat TikTok brand jingle (15 giây):**
```
Genre: Pop, Upbeat
Title: "LUXE VIET VIBES"
Description: Energetic Vietnamese pop-inspired track perfect for TikTok ads.
Catchy hook about fashion and lifestyle. Female vocals singing in Vietnamese
over modern beat. Includes synth and light drums.
Mood: Happy, energetic, youthful, Gen Z vibe
Instruments: Synth, kick drum, hi-hat, bass, female vocal
Vocal style: Young, bright, confident, conversational
BPM: 120
Duration: 15 seconds
Specific: Include the brand name "LUXE VIET" in the hook,
catchy and memorable melody
```

2. **Emotional product story (30 giây):**
```
Genre: Indie Pop, Emotional
Title: "SKINCARE JOURNEY"
Description: Touching story about skincare transformation.
Soft vocals telling a story of confidence and self-care.
Piano with modern beat underneath. Vietnamese lyrics about beauty journey.
Mood: Warm, inspiring, emotional, hopeful
Instruments: Soft piano, cello, subtle beat, reverb-heavy
Vocal style: Intimate, genuine, warm female voice
BPM: 90
Duration: 30 seconds
Specific: Make the lyrics about skincare journey, include
Vietnamese words, emotional but not sad, inspirational tone
```

3. **Luxury brand background music (60 giây):**
```
Genre: Ambient, Lounge
Title: "PREMIUM MOMENTS"
Description: Sophisticated ambient track for luxury product videos.
No lyrics, just instrumental. Cello, piano, subtle electronic elements.
High-end luxury feel.
Mood: Sophisticated, calming, luxurious, elegant
Instruments: Cello, grand piano, ambient pads, subtle strings
Vocal style: Instrumental only
BPM: 80
Duration: 60 seconds
Specific: Make it sound expensive and premium, use jazz chords,
subtle strings, high production quality, no vocal distractions
```

4. **Flash sale urgency music (15 giây):**
```
Genre: Electronic, Dance Pop
Title: "FLASH SALE MOMENT"
Description: High-energy, urgency-driven music for flash sale ads.
Pulsing beat, stabs, electronic sounds. Creates FOMO feeling.
Mood: Urgent, exciting, energetic, FOMO
Instruments: Kick drum, synth stabs, rising pads, hi-hat, bass
Vocal style: Can include brief vocal hits like "SALE!", "NOW!", "LIMITED"
BPM: 128
Duration: 15 seconds
Specific: Make it punchy, include energy builds, sound urgent
but fun, good for countdown sequences
```

### 4.2. UDIO AI - BACKGROUND MUSIC

**Udio là alternative cho Suno, có thể generate longer tracks**

**Udio prompts:**
```
[Mood/vibe], [genre], [instruments], [vocal type], [tempo], [description]
```

**Udio example:**
```
Prompt: "Warm, calm, ambient Indonesian music with gamelan sounds,
relaxing spa atmosphere, no vocals, 60 BPM, perfect for skincare
product video background, 3 minutes, tropical vibe with modern production"
```

---

## 5. TEXT & COPY GENERATION PROMPTS

**Khi dùng ChatGPT/Claude để generate copy bán hàng**

### 5.1. Product Description Prompt:
```
Bối cảnh: Bạn là copywriter bán hàng chuyên nghiệp cho TMĐT Việt Nam

Nhiệm vụ: Viết product description cho [TÊN SẢN PHẨM]

Thông tin sản phẩm:
- Tên: [Tên]
- Loại: [Loại hàng]
- Giá: [Giá]
- Đặc điểm chính: [3-5 đặc điểm nổi bật]
- Thành phần/Chất liệu: [Chi tiết]
- Size/Option: [Có sẵn]
- Target audience: [Ai sẽ mua]

Yêu cầu output:
- Viết bằng tiếng Việt
- Dài 150-200 từ
- Bắt đầu bằng hook hấp dẫn
- Nêu rõ benefit (không phải feature)
- Gồm 2-3 đoạn ngắn
- Có call-to-action rõ ràng ở cuối
- Tone: Thân thiện, không quá marketing, thực tế
- Highlight unique selling point
- Tránh: Từ ngữ quá thô, quảng cáo fake, obey quá

Output format:
[Tiêu đề hấp dẫn - nếu cần]
[Nội dung]
[CTA]
```

### 5.2. Ad Copy Variations Prompt:
```
Bối cảnh: Viết 5 phiên bản ad copy khác nhau cho cùng 1 sản phẩm

Sản phẩm: [TÊN SẢN PHẨM]
Mục đích: Chạy ads TikTok/Facebook/Instagram
Angle 1: Problem-solution (nêu vấn đề rồi giải quyết)
Angle 2: Social proof (dùng testimonial/review)
Angle 3: Scarcity/Urgency (hạn chế/flash sale)
Angle 4: Benefit-focused (lợi ích trực tiếp)
Angle 5: Story/Emotional (kể chuyện)

Mỗi phiên bản:
- 50-80 ký tự (vừa 1 dòng caption)
- Viết bằng tiếng Việt tự nhiên
- Có emoji phù hợp (nếu cần)
- Kết thúc bằng CTA (Link bio, Shop ngay, Comment)
- Tone match target audience

Output: Liệt kê 5 phiên bản cạnh nhau để so sánh
```

### 5.3. Email Marketing Prompt:
```
Viết email marketing bán hàng:

Subject: [Chủ đề email - dưới 50 ký tự]
Sản phẩm: [Tên]
Tiêu chí: Increase click-through rate, conversions

Cấu trúc:
1. Subject line hấp dẫn (3 options)
2. Greeting cá nhân hóa
3. Hook/Opening sentence mạnh (5-10 từ)
4. Main benefit (3-4 sentence)
5. Social proof/Testimonial (1 paragraph)
6. Product details (bullet points 3-4 items)
7. Urgency element (limited time, stock)
8. CTA button (nổi bật, clear)
9. Footer + Unsubscribe link

Tone: Thân thiện, persuasive nhưng không aggressive
Language: Tiếng Việt tự nhiên
Target: [Describe customer]
```

---

## 6. PROMPT CHAINING - KỘI HỢP NHIỀU AI TOOLS

**Khái niệm:** Dùng output của AI này làm input cho AI khác để tạo content hoàn chỉnh

### 6.1. WORKFLOW 1: Hình ảnh → Video → Nhạc → Edit

**Quá trình:**
```
Step 1: GEMINI IMAGEN hoặc MIDJOURNEY
→ Tạo 5-10 ảnh sản phẩm chất lượng cao theo themes khác nhau

Step 2: GOOGLE VEO hoặc KLING
→ Dùng ảnh từ Step 1 làm reference, tạo video từ ảnh tĩnh thành động
→ Prompt: "Create a video based on this [uploaded image], add subtle movement
and zoom to make it dynamic, 15 seconds"

Step 3: SUNO AI
→ Tạo background music phù hợp với product video
→ Prompt: "Create upbeat, modern pop music for [product] video, 15 seconds,
energetic, Gen Z vibe"

Step 4: CapCut / Adobe Premiere
→ Dưa video từ Veo + nhạc từ Suno
→ Add text overlay, transition, effects
→ Export tối ưu cho TikTok/Facebook/Instagram
```

**Ví dụ cụ thể:**
```
TEMA: Makeup product - Liquid Lipstick

Step 1 - Ảnh (Midjourney):
Prompt: "Close-up of wine-red liquid lipstick swatched on white paper,
gold droplets beside, soft studio lighting, shallow DOF, luxury beauty
product photography, high resolution --ar 1:1 --v 6.1"

Step 2 - Video (Veo):
Base image: Ảnh từ Midjourney
Prompt: "Liquid lipstick pouring slowly into a glass container,
camera zooms in to show rich color, droplets fall in slow motion,
duration 8 seconds, cinematic, luxury aesthetic"

Step 3 - Nhạc (Suno):
Prompt: "Upbeat electronic pop, 15 seconds, feminine vocals singing about
confidence and beauty, modern beat, energetic, perfect for makeup ad,
include product name 'LUXE LIPS', Vietnamese language"

Step 4 - Edit:
Ghép video + nhạc + text overlay "LUXE LIPS - BE CONFIDENT"
Add product link + CTA buttons
Export 15s version cho TikTok, 30s version cho Facebook ads
```

### 6.2. WORKFLOW 2: Concept → Ảnh → Animate

```
Step 1: ChatGPT
→ Brainstorm concept visual cho campaign
→ Prompt: "Create 5 different visual concepts for a sustainable fashion
brand campaign, describe each in detail for artist reference"

Step 2: MIDJOURNEY hoặc GROK
→ Tạo key visuals dựa trên concepts
→ Prompt: [Chi tiết từ ChatGPT output]

Step 3: SEEDANCE
→ Animate các ảnh tĩnh thành motion graphics
→ Prompt: "Animate this fashion product image, add floating elements,
subtle movement, luxury feel, 5 seconds, cinematic"

Result: Set of animated product videos ready for ads
```

### 6.3. WORKFLOW 3: Script → Visual → Video → Music

**Cho livestream intro/outro content:**
```
Step 1: Viết script (ChatGPT)
"Introduce new product collection, 30 seconds, Vietnamese, energetic tone"

Step 2: Ảnh (Midjourney)
"Create header image for product collection launch"

Step 3: Video (Veo/Kling)
"Create 15-second intro video with product shots, upbeat energy, duration 15s"

Step 4: Nhạc (Suno)
"Create energetic jingle for product launch, 15s, Vietnamese, broadcast quality"

Step 5: Edit (CapCut)
"Combine video + music + text overlay with product details"

Final: Ready-to-use livestream intro video
```

---

## 7. PROMPT LIBRARY - 50+ PROMPT TEMPLATES SẴN DÙNG

### 7.1. FLAT LAY - TÀN ĐÔNG

**Template 1 - Minimalist flat lay:**
```
Prompt (Midjourney/Imagen):
"[PRODUCT NAME] arranged on [BACKGROUND COLOR] flat surface, minimalist
composition, 45-degree angle shadows, natural daylight, [SUPPORTING ITEMS]
beside it, shot from directly above, shallow depth of field, professional
product photography, magazine-quality, high resolution, 8k, warm color grading"

Negative: "watermark, text, clutter, dust, deformed, low quality, blurry"

Customize:
- PRODUCT NAME: Skincare cream, handbag, jewelry, etc.
- BACKGROUND: White marble, kraft paper, linen, wood, concrete
- SUPPORTING ITEMS: Flowers, leaves, candles, accessories, etc.
```

**Template 2 - Luxury flat lay:**
```
Prompt:
"Luxury [PRODUCT] on premium [MATERIAL] background, scattered [LUXURY ITEMS],
golden accents, dramatic side lighting creating long shadows, editorial fashion
photography, high-end magazine aesthetic, 50mm equivalent, color-graded
moody tones, 8k resolution, cinematic, sophisticated"

Negative: "cheap, plastic, wrinkled, watermark, imperfect product,
overly bright, cluttered"

Customize:
- LUXURY ITEMS: Jewelry, designer accessories, premium items
- MATERIAL: Marble, silk, leather, velvet
```

### 7.2. MODEL SHOTS - CHỤP NGƯỜI MẪU

**Template 3 - Fashion lifestyle:**
```
Prompt (Midjourney):
"Beautiful woman wearing [PRODUCT DESCRIPTION], standing in [LOCATION],
[POSE DESCRIPTION], natural [LIGHTING CONDITION], [MOOD], [STYLE],
professional fashion photography, editorial magazine, shallow DOF focusing
on product, warm color grading, 8k --ar 4:5 --v 6.1 --s 80"

Negative: "unflattering, stiff, watermark, wrinkles, awkward pose,
cheap-looking, blurry, bad skin"

Customize:
- PRODUCT: White linen shirt, blue denim jacket, etc.
- LOCATION: Modern apartment, street corner, beach, urban setting
- POSE: Sitting casually, looking over shoulder, hand in pocket
- LIGHTING: Golden hour, overcast, window light
- MOOD: Confident, relaxed, elegant, playful
```

**Template 4 - Beauty/Skincare model:**
```
Prompt:
"Close-up portrait of [DESCRIPTION] holding [PRODUCT] near face,
[LIGHTING SETUP], [SKIN TONE], [EXPRESSION], professional beauty
photography, magazine quality, shallow depth of field, warm tones,
makeup applied, luxurious feel --ar 4:5"

Negative: "unflattering lighting, skin imperfections amplified,
watermark, blurry, low quality, bad makeup"

Customize:
- LIGHTING: Soft window light, professional ring light
- EXPRESSION: Smiling confidently, serene, glowing
```

### 7.3. FOOD & BEVERAGE PRODUCTS

**Template 5 - Food overhead:**
```
Prompt (Midjourney):
"[DISH NAME] on [PLATE TYPE], arranged artfully, [PROPS/GARNISH],
overhead 90-degree view, [LIGHTING TYPE] from [DIRECTION], steaming
appearance, appetizing, food styling photography, restaurant quality,
shallow DOF on main dish, warm color palette, professional, 8k
--ar 1:1 --s 100"

Negative: "overcooked, brown, wilted, messy, unappetizing, watermark,
low quality, dark"

Customize:
- DISH: Spring rolls, pho, coffee, smoothie bowl, etc.
- PLATE: Ceramic white, gold-rimmed, wooden board, glass
- PROPS: Fresh herbs, chopsticks, sauce cups, napkins
- LIGHTING: Window light, golden hour, studio soft light
```

**Template 6 - Beverage close-up:**
```
Prompt:
"[BEVERAGE] in [GLASS TYPE], [GARNISH] detail, liquid [COLOR/APPEARANCE],
macro photography, shallow extreme depth of field, [LIGHTING], droplets
and condensation visible, appetizing, professional beverage photography,
luxury aesthetic, 8k, high resolution"

Negative: "flat, no sparkle, overexposed, watermark, blurry"

Customize:
- BEVERAGE: Coffee, cocktail, juice, wine, etc.
- GLASS: Classic coupe, modern tumbler, wine glass, mason jar
- GARNISH: Lemon slice, mint leaf, chocolate drizzle
```

### 7.4. TECHNOLOGY PRODUCTS

**Template 7 - Tech product studio:**
```
Prompt (Midjourney):
"Sleek [TECH PRODUCT] on [SURFACE], [ANGLE], minimalist [COLOR] background,
studio lighting with [LIGHT DIRECTION], shallow DOF, professional product
photography, high-end tech aesthetic, sharp details, reflections on surface,
8k, premium quality --ar 1:1 --v 6.1 --s 100 --q 1"

Negative: "dusty, fingerprints, scratches, cheap plastic, watermark,
low resolution, blurry"

Customize:
- TECH PRODUCT: Smartphone, earbuds, smartwatch, laptop
- SURFACE: Dark glass, metallic, wood, neon-lit
- LIGHTING: Side-lit, back-lit, front-lit
```

### 7.5. JEWELRY & ACCESSORIES

**Template 8 - Jewelry luxury:**
```
Prompt:
"[JEWELRY ITEM] on [LUXURY SURFACE], [LIGHTING], [STYLING ELEMENTS],
macro photography, shallow DOF, focus on sparkle and details, professional
jewelry photography, luxury brand aesthetic, 8k, high resolution,
magazine quality, warm/cool tones depending on metal --ar 1:1"

Negative: "dull, low quality, watermark, unfocused, cheap-looking,
overexposed"

Customize:
- SURFACE: Velvet, marble, silk, leather, stone
- LIGHTING: Edge lighting, spotlight, reflected light
- STYLING: Pearls, flowers, complementary items
```

### 7.6. VIDEO TEMPLATES

**Template 9 - Product reveal (Veo/Kling):**
```
Prompt:
"[PRODUCT] slowly rotating from black background, [LIGHTING EFFECT],
smooth 360-degree rotation, camera [MOVEMENT], [DURATION] seconds,
cinematic, product showcase, premium aesthetic, high definition,
professional commercial quality"

Customize:
- LIGHTING: Neon glow, golden light, dramatic color, spotlight
- MOVEMENT: Orbits around product, zooms in, pans
- DURATION: 10-15 seconds for social, 20-30 for long form
```

**Template 10 - Lifestyle video (Veo):**
```
Prompt:
"Person [ACTION] with [PRODUCT], natural [SETTING], [LIGHTING CONDITION],
camera [MOVEMENT], [DURATION] seconds, cinematic slow motion on key moments,
warm color grading, lifestyle content, authentic feel, professional"

Customize:
- ACTION: Opening package, applying product, using item
- SETTING: Modern home, outdoor, office, café
- LIGHTING: Natural window, golden hour, studio
```

### 7.7. SOCIAL MEDIA SPECIFIC TEMPLATES

**Template 11 - TikTok hook thumbnail:**
```
Prompt (Midjourney):
"Thumbnail image for TikTok video, [HOOK TEXT/EMOJI], [PRODUCT VISUAL],
bright colors, high contrast, eye-catching, text readable on small screen,
viral aesthetics, Gen Z style, bold and dynamic, 9:16 format --ar 9:16"

Negative: "blurry text, low contrast, watermark, cluttered, hard to read"

Customize:
- TEXT: "POV:", "3 secrets:", "MUST HAVE:", "Wait for end"
- COLORS: Bright neon, trending colors, contrasting palette
```

**Template 12 - Instagram Reels preview:**
```
Prompt:
"First frame of Instagram Reel, [HOOK IMAGE], 9:16 aspect ratio,
Instagram aesthetic, high engagement potential, shows product and benefit,
professional, clean, modern --ar 9:16"

Customize:
- HOOK: Close-up of product, person reacting, transformation before/after
```

### 7.8. CAMPAIGN TEMPLATES

**Template 13 - Campaign hero image:**
```
Prompt (Midjourney):
"Hero image for [CAMPAIGN NAME] campaign, [MAIN MESSAGE], [PRODUCT INTEGRATION],
[AESTHETIC], [COLOR PALETTE], [COMPOSITION TYPE], professional,
high resolution, suitable for website banner, print, social --ar 16:9"

Customize:
- CAMPAIGN: "Summer Collection", "Flash Sale", "New Launch"
- AESTHETIC: Minimalist, bold, luxury, playful
- COLOR: Brand colors integrated naturally
```

**Template 14 - Email banner:**
```
Prompt:
"Email header banner, [HEADLINE], [PRODUCT], [CALL TO ACTION TEXT],
clear hierarchy, professional, [STYLE], suitable for email clients,
responsive design, 1200x400px equivalent, high conversion potential"

Customize:
- HEADLINE: "[PRODUCT] - Limited Time Offer"
- CTA: "SHOP NOW", "DISCOVER MORE", "CLAIM DISCOUNT"
- COLOR SCHEME: Brand colors with high contrast text
```

---

## 8. TIPS TỐI ƯU HÓA PROMPT

### 8.1. Seed Consistency - Tạo các biến thể nhưng giữ consistency

**Vấn đề:** Tạo 5 ảnh sản phẩm khác nhau nhưng cùng style

**Giải pháp:**
```
Midjourney: Dùng seed number giống nhau
--seed [SAME NUMBER]

Ví dụ:
Prompt 1: "Luxury skincare cream on marble --seed 12345 --ar 1:1"
Prompt 2: "Same skincare cream from different angle --seed 12345 --ar 1:1"
→ Kết quả: Cùng style/lighting nhưng khác góc độ

Hoặc dùng image reference weight:
--iw [0.5-1.5] để kiểm soát mức độ tương tự với reference image
```

### 8.2. Style Reference - Học từ ảnh hiện có

**Cách làm:**
```
Upload ảnh bạn thích (từ competitor, Pinterest, magazine)
Dùng trong prompt: "In the style of [REFERENCE IMAGE], similar aesthetic
but with [YOUR PRODUCT]"

Hoặc dùng prompt chaining:
1. Analyze ảnh reference bằng Claude/GPT4V
2. Extract style description chi tiết
3. Dùng description trong prompt AI tools
```

**Ví dụ:**
```
Bước 1: Upload ảnh competitor vào Claude/GPT
Prompt: "Analyze this product photography. What style is it?
Describe lighting, composition, colors, mood, aesthetic in detail."

Output: "Studio lighting with left-side key light, shallow DOF,
white marble background, warm color grading (2700K), minimalist
composition, luxury aesthetic, editorial magazine style"

Bước 2: Dùng description trong Midjourney
Prompt: "My product on white marble background, studio lighting
with left-side key light, shallow DOF, warm color grading, minimalist
luxury aesthetic, editorial magazine style --v 6.1"
```

### 8.3. Batch Generation & Variation

**Tạo nhiều version cùng 1 lúc:**

```
Midjourney batch:
/imagine [PROMPT 1] [PARAMETERS]
/imagine [PROMPT 2] [PARAMETERS - chỉ thay chi tiết nhỏ]
/imagine [PROMPT 3]
/imagine [PROMPT 4]

Ví dụ - 4 variation của cùng 1 sản phẩm:
1. "Skincare jar flat lay on white marble --ar 1:1"
2. "Skincare jar flat lay on black marble --ar 1:1"
3. "Skincare jar flat lay on kraft paper --ar 1:1"
4. "Skincare jar on model's hand applying --ar 4:5"

→ Tạo 4 ảnh khác nhau để test landing page/ads
```

**A/B Testing prompts:**
```
Variation A - Minimal:
"Skincare jar, white background, studio lighting, clean, minimal --ar 1:1"

Variation B - Lifestyle:
"Skincare jar on woman's hand in natural light, confidence, beauty --ar 4:5"

Variation C - Luxury:
"Skincare jar on marble, gold accents, luxury aesthetic, expensive-looking --ar 1:1"

→ Generate cả 3 → Test conversion rate → Scale cái winner
```

### 8.4. Iterative Refinement

**Loop lặp để tối ưu:**
```
Bước 1: Generate bản 1 với prompt cơ bản
↓ Xem kết quả
Bước 2: Adjust prompt dựa vào feedback
- Quá sáng? → Thêm "muted tones" vào prompt
- Không cách ly sản phẩm? → Thêm "isolated on background"
- Style sai? → Thay "photography" thành "illustration"
↓
Bước 3: Generate bản 2 với prompt improved
↓ Xem kết quả
Bước 4: Repeat cho tới khi hài lòng

Ví dụ iteration:
Attempt 1: "Product on background" → Quá generic
↓
Attempt 2: "Product on white marble, studio light" → Better, nhưng ánh sáng tây
↓
Attempt 3: "Product on white marble, soft diffused north light, shallow DOF" → Lạc
↓
Attempt 4: "Product on white marble, soft window light from left,
shallow DOF, professional product photography, 8k" → Perfect!
```

---

## 9. VIETNAMESE MARKET SPECIFICS - ĐẶC THÙ THỊ TRƯỜNG VIỆT NAM

### 9.1. Aesthetic Preferences - Thẩm mỹ yêu thích

**What Vietnamese audience loves:**
```
✓ Pastels + neutrals (chứ không oversaturated)
✓ Minimalist but warm (không quá lạnh)
✓ Natural + luxury blend (không fake quá)
✓ Lifestyle over pure product shot (ngữ cảnh thực tế)
✓ Face/skin tone visibility (phải thấy mặt, da)
✓ Authentic moments (chứ không quá posed)
```

**Aesthetic to use in prompts:**
```
"Warm Vietnamese aesthetic", "organic minimal", "natural luxury",
"authentic lifestyle photography", "soft and welcoming",
"aspirational but relatable", "warm color temperature"
```

**Avoid:**
```
"Overly bright", "harsh lighting", "cheap plastic look",
"artificial", "too studio-like", "cold blue tones"
```

### 9.2. Color Meanings in Vietnamese Culture

**Color implications:**
```
🟢 Green: Growth, natural, healthy (good for skincare/health)
🔴 Red: Lucky, prosperity, energy (perfect for flash sales/CNY)
⚪ White: Purity, clean, premium (skincare, luxury)
🟡 Gold: Wealth, luxury, premium (jewelry, high-end products)
🟣 Purple: Mystery, creativity, high-end (beauty, fashion)
🔵 Blue: Trust, calm, reliability (tech, health)
🟠 Orange: Friendly, approachable, fun (F&B, lifestyle)
```

**Cultural don'ts:**
```
❌ Black clothing on Lunar New Year
❌ Unhappy faces in festive content
❌ Numbers 4, 13 (bad luck)
❌ Too dark/gloomy aesthetic in traditional occasions
❌ Western-only models without diverse representation
```

### 9.3. Cultural Elements to Include

**Vietnamese cultural touchpoints:**
```
- Traditional elements (lanterns, conical hats, embroidery patterns)
- Seasonal elements (plum blossoms in spring, chrysanthemums in fall)
- Festival timing (Lunar New Year, Tet holidays, Black Friday)
- Daily lifestyle (morning coffee ritual, family gathering aesthetics)
- Architectural elements (minimalist French colonial, modern Vietnamese)
```

**Prompt examples with cultural elements:**
```
1. "Product with traditional Vietnamese embroidery pattern in background,
modern luxury aesthetic, bridging traditional and contemporary"

2. "Product in modern Vietnamese apartment setting,
warm family-oriented aesthetic"

3. "Lunar New Year-themed product shot, red and gold accents,
festive but not kitschy"

4. "Vietnamese coffee ritual aesthetic, skincare product paired with
morning routine, authentic lifestyle"
```

---

## 10. QUICK REFERENCE - CÚ PHÁP NHANH

### 10.1. Midjourney Formula
```
[Detailed object] on [background], [style], [lighting], [camera],
[mood], [quality] --ar [ratio] --v 6.1 --s [0-1000] --q 1
```

### 10.2. Imagen Formula
```
[Full descriptive sentence describing scene], [style], [lighting],
[technical specs], [mood], high resolution, 8k
```

### 10.3. DALL-E Formula
```
"A [descriptive sentence], [style], [mood], [artistic direction],
professional photography/illustration, high resolution"
```

### 10.4. Veo Video Formula
```
[Scene with motion], camera [movement], [duration] seconds,
[lighting], [style], cinematic quality, 1080p
```

### 10.5. Suno Music Formula
```
Genre: [Genre]
Mood: [Mood]
Instruments: [List]
Vocal: [Style]
BPM: [Tempo]
Duration: [Length]
Specific: [Details]
```

---

## 11. COMMON MISTAKES & HOW TO FIX

| Lỗi | Nguyên nhân | Cách sửa |
|-----|-----------|---------|
| Ảnh quá generic | Prompt không chi tiết | Thêm specificity: "not generic, unique lighting, specific background" |
| Sản phẩm hư hỏng | Không dùng negative prompts | Thêm: "--no damage, deformed, broken, scratched" |
| Style sai | Lựa chọn style keywords sai | Copy exact style từ reference image hay competitor |
| Ánh sáng tệ | Không specify lighting | Luôn nêu lighting source: "window light from left", "studio soft light" |
| Sản phẩm nhỏ | Composition không rõ | Thêm "product centered, close-up focus, fills frame" |
| Màu sắc sai | Color grading không specify | Thêm "warm color grading (2700K)", "cool tones", "muted palette" |
| Video bị flickering | Quality setting thấp | Dùng high quality setting, specify "smooth motion, no flicker" |
| Âm thanh quá thô | BPM/genre không match | Specify exact BPM, professional production quality |

---

## 12. RESOURCE & TOOL LINKS

**AI Image Tools:**
- Midjourney: midjourney.com (Best for TMĐT)
- Gemini Imagen: https://makersuite.google.com/
- DALL-E 3: openai.com/dall-e-3
- Grok: grok.com (xAI)

**AI Video Tools:**
- Google Veo: google.com/labs/veo
- Kling AI: kling.kuaishou.com
- Runway: runway.ml
- Seedance: seedance.com

**AI Music Tools:**
- Suno AI: suno.com
- Udio: udio.com

**Workflow Tools:**
- CapCut: capcut.com (edit video)
- Claude/ChatGPT: For scripting, copy, concept ideation
