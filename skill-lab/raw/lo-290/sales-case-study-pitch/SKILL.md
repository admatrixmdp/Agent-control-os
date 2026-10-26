---
name: sales-case-study-pitch
description: |
  Pitch case study đúng tình huống KH — match industry, persona, pain để tăng credibility. Trigger phrases: "pitch case study", "chia sẻ case study đúng lúc", "case study mapping", "case study cho khách hàng", "kể chuyện thành công", "social proof sales", "match case study deal", "case study pitch B2B", "customer story pitch", "reference case study". Output là Markdown library + Excel matching matrix + PDF case study riêng.
---

# Case Study Pitch Mapper

## Mục Tiêu
Đảm bảo AE pitch đúng case study (cùng industry + persona + pain) trong từng tình huống KH — case sai làm mất credibility, case đúng tăng deal velocity 40%.

## Khi Nào Dùng
- AE objection "chưa có case cùng ngành"
- Discovery call cần social proof
- Demo close cần proof
- KH skeptical về ROI
- Sau win logo lớn cần monetize case study

## Bước 1: Inventory Case Study
Build library:
- Case study công ty (15-50 cases)
- Mỗi case có metadata:
  - Industry (SIC code)
  - Company size
  - Geo
  - Persona (CFO/CMO/COO)
  - Pain ranked
  - Solution module
  - Outcome metric (số)
  - Format available (PDF, video, slide, reference call)

## Bước 2: Matching Matrix
Tạo matrix: tình huống KH × case study top match
- Industry match: 30 điểm
- Persona match: 25 điểm
- Pain match: 25 điểm
- Size match: 10 điểm
- Geo match: 10 điểm

→ AE input KH context, return top 3 case match.

## Bước 3: Pitch Script theo Case
Mỗi case có 3 version pitch:
- **30s elevator** (cuối discovery): "Khách X cùng size anh, gặp pain Y, sau 6 tháng đạt Z."
- **3 phút deep** (demo): bối cảnh → problem → approach → result
- **Reference call** (negotiation): book 30 phút call KH cũ với prospect

## Bước 4: Refresh & Permission
- Quarterly check: KH cũ còn happy không? Số liệu cập nhật?
- Permission: KH cho phép share PUBLIC vs INTERNAL vs CONFIDENTIAL?
- Tag CONFIDENTIAL → chỉ verbal pitch, không attach
- Refresh số liệu (KH grow hoặc shrink)

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên MCP:**
- Drive/SharePoint MCP: pull case study library
- Salesforce MCP: tag deal đã dùng case nào
- Gong MCP: phân tích case nào hiệu quả nhất
- Slack MCP: AE request case study realtime

**Fallback API:**
```python
# Match case study automatically
def match_cases(prospect, library, top_n=3):
    scores = []
    for case in library:
        s = 0
        if case["industry"] == prospect["industry"]: s += 30
        if case["persona"] == prospect["persona"]: s += 25
        if any(p in case["pains"] for p in prospect["pains"]): s += 25
        if abs(case["size_log"] - prospect["size_log"]) < 1: s += 10
        if case["geo"] == prospect["geo"]: s += 10
        scores.append((case, s))
    return sorted(scores, key=lambda x: -x[1])[:top_n]
```

## Bước 6: Output Format
- **File 1**: `case_study_library.xlsx` — 50 case + metadata + access link
- **File 2**: `case_matching_matrix.xlsx` — auto match top 3 cho mỗi industry × persona
- **File 3**: `case_pitch_scripts.md` — 3 version pitch mỗi top case
- **File 4**: `case_study_<industry>.pdf` — case study formatted cho gửi KH
- Lưu: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/`

## Checklist Trước Khi Giao
- [ ] >15 case trong library
- [ ] Metadata đầy đủ mỗi case
- [ ] Permission tag rõ ràng
- [ ] 3 version pitch (30s/3min/ref call)
- [ ] Quarterly refresh
- [ ] Tag CONFIDENTIAL không share PDF
