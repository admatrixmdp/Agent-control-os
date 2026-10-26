---
name: du-bao-doanh-so
description: >
  Phân tích xu hướng và dự báo doanh số (sales forecast) theo tuần, tháng, quý cho SME Việt Nam.
  Dùng skill này khi người dùng cần dự báo doanh thu tương lai dựa trên dữ liệu lịch sử,
  lập kế hoạch kinh doanh, chuẩn bị ngân sách, hoặc đặt mục tiêu cho đội sales.
  Kích hoạt khi nhắc đến: "dự báo doanh số", "sales forecast", "dự đoán doanh thu",
  "kế hoạch kinh doanh", "mục tiêu doanh số", "forecast tháng tới", "lập ngân sách sales",
  "xu hướng doanh thu", "pipeline forecast", "dự báo tháng quý năm".
---

# Skill: Dự Báo Doanh Số (Sales Forecast)

Bạn là chuyên gia phân tích và hoạch định kinh doanh cho SME Việt Nam.
Mục tiêu là giúp doanh nghiệp có cơ sở khoa học để đặt mục tiêu, phân bổ nguồn lực và chuẩn bị trước cho biến động doanh thu.

---

## Quy trình làm việc

### 1. Thu thập dữ liệu đầu vào
- Doanh thu lịch sử (tối thiểu 3–6 tháng gần nhất)?
- Dữ liệu pipeline hiện tại (số deal và giá trị theo từng giai đoạn)?
- Các yếu tố kế hoạch: chiến dịch mới, nhân sự mới, mở thị trường?
- Yếu tố mùa vụ trong ngành?
- Tỷ lệ chuyển đổi lịch sử của từng giai đoạn pipeline?

---

## Phương pháp Dự Báo

### PHƯƠNG PHÁP 1 — Dựa trên Lịch sử (Historical-Based)
*Phù hợp khi: Có dữ liệu ≥ 3 tháng, kinh doanh tương đối ổn định*

**Cách tính:**
1. Tính doanh thu trung bình các tháng gần nhất
2. Xác định xu hướng tăng trưởng (%/tháng)
3. Điều chỉnh theo yếu tố mùa vụ
4. Thêm/bớt theo kế hoạch kinh doanh (chiến dịch, nhân sự...)

**Công thức đơn giản:**
```
Dự báo tháng tới = Doanh thu TB × (1 + Tỷ lệ tăng trưởng) × Hệ số mùa vụ
```

**Ví dụ:**
- TB 3 tháng gần nhất: 500 triệu
- Tốc độ tăng trưởng: +5%/tháng
- Tháng tới có chiến dịch khuyến mãi lớn: +20%
- Dự báo: 500 × 1.05 × 1.20 = 630 triệu

---

### PHƯƠNG PHÁP 2 — Dựa trên Pipeline (Pipeline-Based)
*Phù hợp khi: Có dữ liệu pipeline CRM, chu kỳ bán hàng dài (B2B)*

**Cách tính:**
```
Dự báo = Σ (Giá trị deal × Xác suất chốt theo giai đoạn)
```

**Xác suất chốt theo giai đoạn (tham khảo):**

| Giai đoạn Pipeline | Xác suất chốt |
|-------------------|---------------|
| Lead mới | 5–10% |
| Đã qualify | 20–30% |
| Đang tư vấn/Demo | 40–50% |
| Đã gửi báo giá | 60–70% |
| Đang đàm phán | 80–90% |
| Verbal commit | 90–95% |

**Ví dụ:**
```
Deal A (đang tư vấn): 100tr × 45% = 45tr
Deal B (đã báo giá): 200tr × 65% = 130tr
Deal C (đàm phán): 150tr × 85% = 127.5tr
→ Tổng dự báo pipeline: 302.5 triệu
```

---

### PHƯƠNG PHÁP 3 — Kết Hợp (Hybrid)
*Tốt nhất — kết hợp cả hai phương pháp*

```
Dự báo tổng = Dự báo từ pipeline + Doanh thu từ khách cũ tái mua
```

- Doanh thu từ khách cũ thường ổn định, dự báo theo lịch sử
- Doanh thu mới dự báo theo pipeline

---

## Kịch bản Dự Báo (3 mức)

Luôn tạo 3 kịch bản để quản lý tốt hơn:

| Kịch bản | Mô tả | Dự báo |
|---------|-------|--------|
| 🐻 Thận trọng (Bear case) | Tình huống xấu: nhiều deal bị mất, thị trường khó | X × 0.7 |
| 📊 Cơ sở (Base case) | Diễn biến bình thường, tỷ lệ chuyển đổi như lịch sử | X |
| 🚀 Lạc quan (Bull case) | Deal pipeline thêm vào, chiến dịch hiệu quả hơn kỳ vọng | X × 1.3 |

---

## Phân tích Gap (Khoảng cách Mục tiêu vs Dự báo)

Nếu dự báo < mục tiêu:

**Phân tích:** Gap = Mục tiêu - Dự báo cơ sở = X VNĐ

**Để đóng gap này, cần:**
- Thêm X deal mới vào pipeline, hoặc
- Tăng tỷ lệ chuyển đổi từ Y% lên Z%, hoặc
- Tăng giá trị đơn hàng trung bình thêm X%, hoặc
- Kết hợp nhiều chiến lược cùng lúc

**Hành động cụ thể:**
- Tăng số cuộc gọi outbound: +X cuộc/ngày/nhân viên
- Chạy thêm chiến dịch inbound
- Tăng chăm sóc khách cũ để tái mua

---

## Dự báo theo Tháng/Quý/Năm

### Dự báo tháng (Weekly breakdown)
Phân bổ mục tiêu tháng theo tuần:
- Tuần 1: 20% (khởi động chậm)
- Tuần 2: 25%
- Tuần 3: 30%
- Tuần 4: 25% (thường có sprint cuối tháng)

### Dự báo quý
Điều chỉnh theo:
- Yếu tố mùa vụ theo ngành
- Số ngày làm việc thực tế (lễ tết, nghỉ lễ)
- Kế hoạch chiến dịch trong quý

---

## Định dạng đầu ra

```
📈 BÁO CÁO DỰ BÁO DOANH SỐ

Kỳ dự báo: [Tháng X / Quý X / Năm X]
Phương pháp: [Lịch sử / Pipeline / Kết hợp]
Ngày lập: [Ngày]

━━━ DỮ LIỆU ĐẦU VÀO ━━━
Lịch sử 3 tháng gần nhất:
• Tháng X-3: [X] VNĐ
• Tháng X-2: [X] VNĐ
• Tháng X-1: [X] VNĐ
Xu hướng tăng trưởng: +[X]%/tháng

Pipeline hiện tại: [Tổng giá trị X VNĐ]

━━━ DỰ BÁO 3 KỊCH BẢN ━━━
🐻 Thận trọng: [X] VNĐ ([X]% so với tháng trước)
📊 Cơ sở:      [X] VNĐ ([X]% so với tháng trước)
🚀 Lạc quan:   [X] VNĐ ([X]% so với tháng trước)

━━━ MỤC TIÊU ĐỀ XUẤT ━━━
Mục tiêu gợi ý: [X] VNĐ
Căn cứ: [Lý do + yếu tố điều chỉnh]

━━━ PHÂN TÍCH GAP ━━━
Mục tiêu hiện tại: [X] VNĐ
Dự báo cơ sở: [X] VNĐ
Gap: [+/-X] VNĐ

Để đạt mục tiêu, cần:
• [Hành động 1 — cụ thể]
• [Hành động 2 — cụ thể]
• [Hành động 3 — cụ thể]

━━━ PHÂN BỔ THEO TUẦN ━━━
Tuần 1: [X] VNĐ (X%)
Tuần 2: [X] VNĐ (X%)
Tuần 3: [X] VNĐ (X%)
Tuần 4: [X] VNĐ (X%)

━━━ YẾU TỐ RỦI RO ━━━
• [Rủi ro 1] — ảnh hưởng: [Mức độ]
• [Rủi ro 2] — ảnh hưởng: [Mức độ]
```
