---
name: hr-org-chart-generator
description: |
  Sinh sơ đồ tổ chức (org chart) tự động từ dữ liệu HRIS/Google Sheets cho doanh nghiệp Việt Nam, dạng tree visual, có ảnh, span of control, vacancy, export PNG/PDF/SVG.
  Kích hoạt khi người dùng nói: "org chart", "sơ đồ tổ chức", "vẽ org chart", "generate org chart", "sơ đồ công ty", "company structure visual", "organization chart", "vẽ cây tổ chức", "biểu đồ phòng ban", "structure map".
  Output là file .html interactive + .png + .pdf + .pptx slide cho all-hands.
---

# HR - Sinh Sơ Đồ Tổ Chức Tự Động

## Mục Tiêu
Cập nhật org chart real-time khi có thay đổi nhân sự (hire, promote, leave), tránh phải redraw bằng tay mỗi quý. Sơ đồ rõ ràng giúp NV mới hiểu cấu trúc, ai báo cáo ai.

## Khi Nào Dùng
- Onboarding NV mới cần xem cơ cấu
- All-hands quý / annual report
- Tái cấu trúc, hợp nhất phòng ban
- Audit span of control (1 manager quá nhiều/ít người)

## Bước 1: Chuẩn Hóa Data Source
Bảng input tối thiểu cần các cột:
| employee_id | full_name | title | dept | manager_id | photo_url | location | start_date | status |
|---|---|---|---|---|---|---|---|---|
| E001 | Nguyễn Văn A | CEO | Exec | NULL | url | HCM | 2018 | Active |
| E002 | Trần Thị B | CMO | Marketing | E001 | url | HCM | 2020 | Active |

Quan trọng: `manager_id` reference đúng `employee_id` parent. Có dòng cho vacancy (status = "Open").

## Bước 2: Chọn Layout + Visual
- **Tree top-down**: classic, đến CEO cùng cấp dưới (≤ 7 cấp)
- **Horizontal**: cho team rộng (span of control > 10)
- **Hybrid**: top-down 3 cấp + lateral cho team rộng dưới
- **Department-colored**: mỗi phòng 1 màu
- **Vacancy highlighted**: ô màu xám/đường nét đứt

Thông tin mỗi node: avatar tròn, tên, title, dept badge, location flag (HN/HCM/Remote).

## Bước 3: Build Visualization
Tool đề xuất:
- **D3.js + dagre**: HTML interactive, zoom/pan
- **Mermaid.js**: markdown-based, đơn giản
- **OrgChart.js**: ready-made, có export
- **PowerPoint SmartArt**: cho slide BOD

Tự động tính:
- Span of control (số direct report mỗi manager) - flag > 8 hoặc < 3
- Depth (số cấp từ CEO xuống)
- Total HC per dept
- Open positions

## Bước 4: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Sheets MCP: pull employee data live
- Drive MCP: lưu version mỗi tháng (history)
- Gmail MCP: gửi org chart updated cho toàn công ty
- Slack MCP: post org chart vào #all-staff
- WebSearch: tra best practice org chart tools

**Fallback bằng API (HRIS):**
```python
# Pull data từ BambooHR/MISA HRM rồi build chart
import requests, pandas as pd, json
r = requests.get(f"https://api.bamboohr.com/api/gateway.php/{CO}/v1/employees/directory",
    auth=(API_KEY, "x"))
df = pd.DataFrame(r.json()["employees"])

# Build tree structure
def build_tree(df, root_id=None):
    nodes = df[df["manager_id"] == root_id]
    return [{"id": n["id"], "name": n["name"], "title": n["title"],
             "children": build_tree(df, n["id"])} for _, n in nodes.iterrows()]

tree = build_tree(df)
with open("org_tree.json", "w") as f:
    json.dump(tree, f, ensure_ascii=False)
```

Sau đó dùng D3.js render từ `org_tree.json`.

## Bước 5: Output Format
- File `.html` interactive org chart (zoom, search, filter)
- File `.png` static high-res (cho slide)
- File `.pdf` A3/A2 in giấy treo office
- File `.pptx` slide cho all-hands
- File `.xlsx` Span of Control analysis
- Lưu tại: `/outputs/OrgChart_<congty>_<YYYY-MM>.html`

## Checklist Trước Khi Giao
- [ ] Data source live từ HRIS
- [ ] Có ảnh + tên + title + dept
- [ ] Vacancy được highlight rõ
- [ ] Span of control phân tích (flag > 8 hoặc < 3)
- [ ] Phân biệt manager line vs functional line
- [ ] Có version archive theo tháng
- [ ] Tuân thủ quyền riêng tư (không hiển thị lương)
- [ ] HR + CEO duyệt trước khi public
