---
name: ceo-personal-okr
description: |
  OKR cá nhân CEO theo 3 trục: lãnh đạo công ty + sức khoẻ + học tập. Tránh CEO chỉ work, burn-out. Có tracker tuần và review quarterly.
  Kích hoạt khi người dùng nói: "OKR cá nhân CEO", "personal OKR founder", "mục tiêu cá nhân CEO", "personal goals", "CEO life balance OKR", "founder personal goals", "personal development plan CEO", "OKR sống của sếp".
  Output là Markdown plan + Notion database.
---

# CEO Personal OKR — OKR Cá Nhân CEO

## Mục Tiêu
CEO thường chỉ có OKR công ty → burn-out, gia đình lung lay, học hỏi dừng. Personal OKR balance 3 trục lãnh đạo + sức khoẻ + học tập = giữ CEO sharp 10 năm thay vì cháy 3 năm.

## Khi Nào Dùng
- Đầu quý cùng OKR công ty
- Sau coaching session
- Sau khủng hoảng cá nhân (sức khoẻ, gia đình)
- Birthday year review
- Annual off-site cá nhân

## Bước 1: Audit Hiện Trạng 3 Trục
**Trục 1 - Lãnh đạo công ty**: tự đánh giá 1-10:
- Strategic clarity
- Team energy
- Cash position
- My energy on work

**Trục 2 - Sức khoẻ**: 1-10:
- Cardio (steps/week)
- Strength (workouts/week)
- Sleep (hours avg)
- Stress level
- Annual check-up done?

**Trục 3 - Học tập**: 1-10:
- Books read this year
- Skill mới đang học
- Coach/mentor cadence
- Network mới gặp

Trục nào < 6 = ưu tiên.

## Bước 2: Set 1 Objective + 3 KR Mỗi Trục
**Trục 1 ví dụ:**
- Objective: "Trở thành CEO Strategic chứ không Reactive"
- KR1: 30% thời gian/tuần cho strategic work (không họp ops)
- KR2: Delegate hết 5 reports hiện tại cho COO
- KR3: 1 board feedback positive về strategic depth

**Trục 2 ví dụ:**
- Objective: "Cơ thể nuôi được 10 năm CEO nữa"
- KR1: Cardio 3 lần/tuần (Strava log)
- KR2: Ngủ ≥ 7h/đêm avg quý
- KR3: BMI về 23 từ 27

**Trục 3 ví dụ:**
- Objective: "Học bằng cấp tốc về AI cho business"
- KR1: Đọc 4 cuốn về AI/LLM
- KR2: Hoàn thành 1 course Anthropic/OpenAI
- KR3: Hire AI advisor monthly call

## Bước 3: Weekly Tracker
Mỗi Chủ Nhật review:
- Trục 1: % strategic time tuần này
- Trục 2: số workouts, ngủ avg, weight
- Trục 3: pages đọc, course progress

Đặt phone reminder Chủ Nhật 21h "Personal OKR Check-in".

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Notion MCP: database "Personal OKR" private
- Calendar MCP: block strategic time + workout time
- Apple Health / Strava (qua API): pull steps, workout
- Goodreads MCP: track reading
- Gmail MCP: filter emails cướp thời gian strategic

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Strava API pull weekly workouts
import requests
r = requests.get(
  "https://www.strava.com/api/v3/athlete/activities",
  params={"after": week_start_ts},
  headers={"Authorization": f"Bearer {token}"}
)
workouts = r.json()
total_distance = sum(a['distance']/1000 for a in workouts)
total_time_hr = sum(a['moving_time']/3600 for a in workouts)
```

## Bước 5: Output Format
- Markdown plan 1 trang cho 3 trục
- Notion database private có status weekly
- Weekly check-in template (5 phút)
- Quarter review template (30 phút)
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/personal-okr-Q#-YYYY.md` (private)

## Checklist Trước Khi Giao
- [ ] Đủ 3 trục với 1 objective + 3 KR mỗi trục
- [ ] KR đo lường được, không "tốt hơn"
- [ ] Weekly tracker đã đặt reminder
- [ ] Calendar block strategic + workout
- [ ] Share với spouse/coach để accountability
- [ ] Private, không share team
