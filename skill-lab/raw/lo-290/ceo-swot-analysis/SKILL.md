---
name: ceo-swot-analysis
description: |
  Phân tích SWOT chuyên sâu cho công ty/sản phẩm/thị trường — không chỉ liệt kê 4 ô mà còn cross-analysis (SO/WO/ST/WT), ranking theo độ ưu tiên và đề xuất hành động cụ thể.
  Kích hoạt khi người dùng nói: "phân tích SWOT", "SWOT công ty", "SWOT sản phẩm", "điểm mạnh điểm yếu", "đánh giá nội ngoại lực", "SWOT analysis", "ma trận SWOT", "SO WO ST WT".
  Output là bảng SWOT HTML/PDF + matrix chiến lược.
---

# CEO SWOT Analysis — Phân Tích SWOT Chuyên Sâu

## Mục Tiêu
SWOT đơn thuần liệt kê 4 ô không đủ. Skill này tạo SWOT level CEO với cross-analysis tạo ra chiến lược SO (tấn công), WO (chuyển hoá), ST (phòng thủ), WT (rút lui) — biến SWOT từ tài liệu trang trí thành công cụ ra quyết định.

## Khi Nào Dùng
- Đầu năm khi review chiến lược
- Trước khi vào thị trường mới
- Khi đối thủ lớn xuất hiện
- Sau cuộc khủng hoảng (COVID, kinh tế xuống)
- Trước thương vụ M&A

## Bước 1: Hỏi Phạm Vi
- Phân tích toàn công ty? Sản phẩm cụ thể? Thị trường?
- Mốc thời gian xét: 12 tháng tới hay 3 năm?
- Đối tượng đọc: CEO, board, hay external?

## Bước 2: Thu Thập 4 Ô SWOT
Mỗi ô có 5-8 điểm, kèm **bằng chứng số** (không chỉ ý kiến):
- **Strengths**: VD "Margin gross 65% (cao gấp 2 ngành)"
- **Weaknesses**: VD "CAC payback 18 tháng (benchmark 8)"
- **Opportunities**: VD "TAM Việt Nam tăng 25%/năm theo McKinsey"
- **Threats**: VD "Đối thủ X vừa raise $50M"

Mỗi điểm phải có nguồn (financial, survey, report).

## Bước 3: Cross-Analysis 4 Chiến Lược
**SO (Strengths × Opportunities)** = tấn công: dùng điểm mạnh chộp cơ hội
**WO (Weaknesses × Opportunities)** = chuyển hoá: khắc phục yếu để bắt cơ hội
**ST (Strengths × Threats)** = phòng thủ: dùng mạnh chống mối đe doạ
**WT (Weaknesses × Threats)** = rút lui: tránh né hoặc cut loss

Mỗi ô đề xuất 2-3 hành động ưu tiên + owner + ngân sách.

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- WebSearch: tìm benchmark ngành, đánh giá đối thủ, báo cáo McKinsey/Statista
- WebFetch: lấy nội dung báo cáo PDF công khai
- Notion MCP: lưu SWOT làm database để update định kỳ
- Google Drive MCP: pull số tài chính làm bằng chứng Strengths/Weaknesses
- Slack MCP: collect sentiment từ #general để đánh giá weaknesses culture

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# WebSearch + tổng hợp
queries = [
  "thị trường [ngành] Việt Nam 2026 quy mô",
  "đối thủ [ngành] funding 2026",
  "trend [ngành] consumer behavior"
]
# Tổng hợp kết quả để fill ô Opportunities + Threats
```

## Bước 5: Output Format
- HTML 1 trang: ma trận 2×2 SWOT có icon + bullet
- Trang 2: bảng 4 chiến lược SO/WO/ST/WT
- PDF cho board
- Excel cho team execution (đầu cột là action, có owner/deadline/budget)
- Lưu vào `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/swot-[scope]-YYYY.pdf`

## Checklist Trước Khi Giao
- [ ] Mỗi ô có 5-8 điểm có bằng chứng số
- [ ] Có đủ 4 chiến lược cross-analysis
- [ ] Mỗi action có owner + deadline
- [ ] Ranking ưu tiên rõ ràng (top 3 critical)
- [ ] Có nguồn cho mọi số liệu
- [ ] Không lẫn điểm Internal (S/W) với External (O/T)
