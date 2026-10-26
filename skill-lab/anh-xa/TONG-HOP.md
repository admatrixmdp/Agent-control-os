# Tổng hợp đối chiếu 510 skill bên ngoài (kho Taki) — 2026-10-26

**Trạng thái:** bước 1–4 của `doi-chieu/quy-trinh.md` xong ở mức **đề xuất**. Nhãn do agent đọc nghĩa gắn; **Quân chốt** trước khi trích (bước 5). Chưa có skill nội bộ nào bị sửa.
**Tầng tri thức:** toàn bộ "thu thập, chưa kiểm chứng".

## 1. Kết quả tổng

| Nhãn | Số | Ý nghĩa | Việc tiếp theo |
|---|---:|---|---|
| **Bổ sung** | 117 (17 giá trị cao) | Nội bộ đã có khái niệm, skill ngoài có phần đáng lấy | Trích phần đáng lấy → PR vào skill nội bộ → chấm trước/sau |
| **Mới** | 243 (72 giá trị cao) | Nội bộ chưa có | Qua màng lọc Hermes → dựng skill mới trong repo phù hợp |
| **Trùng** | 92 | Nội bộ đã có và không kém | Không làm gì |
| **Loại** | 58 | Bản yếu trong cụm trùng nội bộ kho, quá chung, sai luật | Không làm gì |

| Nhóm | Tổng | Trùng | Bổ sung | Mới | Loại |
|---|---:|---:|---:|---:|---:|
| Marketing – TMĐT | 136 | 46 | 55 | 35 | 0 |
| Sale – CSKH | 102 | 24 | 36 | 39 | 3 |
| Quản trị – pháp lý – sản phẩm | 80 | 18 | 18 | 43 | 1 |
| Tài chính – kế toán | 51 | 0 | 3 | 41 | 7 |
| Nhân sự – vận hành – mua hàng – IT – hành chính – XNK | 141 | 4 | 5 | 85 | 47 |
| **Tổng** | **510** | **92** | **117** | **243** | **58** |

Chi tiết từng skill: `theo-nghia/<nhóm>.yaml`.

## 2. Đánh giá chất lượng kho

| Lô | Đặc điểm | Dùng được gì |
|---|---|---|
| **Lô 290** (`ceo-`, `mkt-`, `sales-`…) | Khung mỏng ~80–100 dòng, đúc một khuôn 5 bước; thiên SaaS doanh nghiệp lớn kiểu Mỹ; nhiều lời hứa không nguồn ("tăng 35% win rate", "tiết kiệm 50–70%") | Dàn ý, checklist, bảng khung |
| **Lô update** (tên tiếng Việt) | Dày hơn, nhiều bảng và mẫu điền tiếng Việt, sát thực tế SME/TMĐT Việt Nam; còn chỗ trống "[X]"; nhiều benchmark chưa kiểm chứng | Mẫu, kịch bản tiếng Việt, quy trình vận hành |

**Khi trùng giữa hai lô, bản lô update thường tốt hơn.**

## 3. Ba lỗi hệ thống của kho — không được mang sang

| Lỗi | Phạm vi | Ví dụ |
|---|---|---|
| **Endpoint API bịa** trong mục "MCP-first + API fallback" | Gần như toàn bộ lô 290 | `api.misa.vn/sme/v1`, `openapi.vietcombank.com.vn`, `api.gdt.gov.vn`, `legal-log.internal` |
| **Căn cứ pháp lý sai hoặc lỗi thời** | Tài chính, kế toán, nhân sự, pháp lý, CSKH | Thuế suất TNDN SME ghi 17%/15% sai theo Luật TNDN 2025; TT200 đã bị TT99/2025 thay từ 01/01/2026; NĐ 13/2023 đã bị Luật BVDLCN 2025 thay; Điều 125 BLLĐ 2019 có 6 căn cứ sa thải, skill ghi 3; thiếu NĐ 91/2020 (SMS), NĐ 81/2018 (khuyến mại có thưởng) |
| **Số liệu không nguồn** | Toàn kho | Benchmark ngành, tỷ lệ cải thiện, bảng hệ số EBITDA M&A |

Nhận định pháp lý trên do agent đối chiếu theo hiểu biết, **chưa tra văn bản gốc** trong lượt này. Mọi đoạn pháp lý lấy về phải viết lại từ văn bản hiện hành có mã điều khoản (nguyên tắc "pháp lý làm gốc" của `Company-finance-accountant-os`).

## 4. Khoảng trống của hệ MQ mà kho này chỉ ra

| Mảng | Skill "mới" | Giá trị cao | Hiện trạng nội bộ | Đề xuất |
|---|---:|---:|---|---|
| **Nhân sự** | 31 | 11 | `Hr-suite-os` rỗng | **Dựng trước.** Tuyển dụng, hợp đồng lao động, kỷ luật, lương thưởng, đánh giá |
| **Tài chính – kế toán** | 39 | 11 | 3 skill đã phát hành; bản đồ skill có tên nhưng "chưa làm" | Lấp theo bản đồ có sẵn: dòng tiền 13 tuần, P&L quản trị theo SKU/kênh, khoá sổ tháng, công nợ, đối soát |
| **CSKH vận hành** | 18 | 9 | Không có repo; `sale-suite-os` chỉ B2B | Repo mới `cskh`: ticket, SLA, leo thang, câu trả lời mẫu, chatbot, đổi trả, bảo hành |
| **Pháp lý hợp đồng** | 13 | 4 | Chỉ có `compliance-vn` (tuân thủ) | Repo mới hoặc mở rộng `compliance-vn`: soạn / rà hợp đồng, NDA, sở hữu trí tuệ |
| **Mua hàng – kho vận** | 15 | 4 | `pancake-suite` có stock-alert | Bổ sung `pancake-suite` trước (theo dõi đơn, hàng hoàn, kiểm kê); nhà cung cấp để sau |
| Vận hành | 13 | 2 | `Company-suite-os` tầng thực thi | **Không cần repo mới**: SOP, RCA, Kaizen vào `Company-suite-os` |
| PR – truyền thông | 7 | 2 | Trống | Gộp vào `marketing-business-skill` hoặc repo mới |
| Bán hàng B2C qua chat | 2 | 2 | Trống | Gộp vào `pancake-suite` (Pancake Chat) hoặc ZAgent |
| Dữ liệu (RFM, cohort) | 4 | 2 | Có Bluecore MCP | Đặt cạnh Bluecore; KPI phải theo chuẩn chỉ số Bluecore |

## 5. Đề xuất thứ tự làm

| Lô | Việc | Số skill | Lý do |
|---|---|---:|---|
| **1** | Trích 17 skill "bổ sung" giá trị cao vào skill nội bộ (Phụ lục A) — 8 cái vào `sale-suite-os` | 17 | Rẻ nhất, đo được ngay bằng eval đã có |
| **2** | Lấp `Company-finance-accountant-os` theo bản đồ skill có sẵn, dùng 11 skill "mới" giá trị cao làm khung (viết lại pháp lý) | 11 | Repo đã có hạ tầng, chỉ thiếu skill |
| **3** | Dựng `Hr-suite-os` | 11 | Khoảng trống lớn nhất; có repo rỗng chờ sẵn |
| **4** | Quyết định repo CSKH và pháp lý hợp đồng | 13 | Cần Quân chốt cấu trúc repo |
| Sau | 69 "bổ sung" giá trị vừa, các "mới" giá trị vừa | ~200 | Theo nhịp 30 skill/tuần |

## 6. Cần Quân chốt

1. Duyệt nhãn lô 1 (Phụ lục A) — đồng ý thì trích và mở PR vào repo skill tương ứng.
2. Mở repo mới hay gộp: `cskh`, pháp lý hợp đồng, `pr-truyen-thong`, `ban-hang-b2c`.
3. `sale-suite-os` có mở nhánh bán lẻ (B2C) không, hay để tham chiếu bán lẻ trong skill 11–12.
4. Trùng tên: skill ngoài `hoach-dinh-chien-luoc` trùng y tên skill nội bộ trong `Company-suite-os`; `ceo-daily-briefing` có thể trùng skill `morning` cấp tài khoản.

## Phụ lục A — 17 skill "bổ sung" giá trị cao (lô 1 nên làm)

| # | Skill ngoài | Lô | Vào skill nội bộ | Repo | Lấy gì |
|---|---|---|---|---|---|
| 1 | `Báo cáo Tài chính & Unit Economics cho TMĐT` | update | `ho-so-tai-chinh`, `10-tinh-kpi-nguoc` | Company-finance-accountant-os | P&L theo đơn/SKU + bảng cấu trúc chi phí TMĐT VN + cash flow → references/ của ho-so-tai-chinh; bỏ phần thuế, kiểm lại với pháp lý gốc |
| 2 | `fin-internal-control-soc1` | 290 | `kiem-toan-noi-bo` | Company-finance-accountant-os | Risk-Control Matrix theo chu trình P2P/O2C/R2R + bảng cỡ mẫu TOE theo tần suất (ngày 25, tuần 15, tháng 5, quý 2) + 3 mức kết luận → references/ của kiem-toan-noi-bo |
| 3 | `bao-ve-du-lieu-ca-nhan` | update | `tuan-thu-doanh-nghiep` | compliance-vn | Quy trình xử lý sự cố rò rỉ dữ liệu + 7 nguyên tắc kèm ví dụ thực tế → templates/xu-ly-ro-ri-du-lieu.md của tuan-thu-doanh-nghiep, viết lại theo Luật BVDLCN 2025 |
| 4 | `Zalo Marketing Toàn Diện cho TMĐT` | update | `11-thiet-lap-kenh` | marketing-business-skill | Thiết kế menu OA + lịch/tần suất broadcast + mẫu tin + Zalo Ads/Pixel + Zalo B2B + luật nền tảng → references/ của 11-thiet-lap-kenh; kiểm lại chính sách Zalo hiện hành |
| 5 | `fin-pricing-margin-simulator` | 290 | `dinh-gia-san-pham`, `10-tinh-kpi-nguoc` | marketing-business-skill | Margin waterfall (giá niêm yết → KM → voucher sàn → phí sàn/thanh toán/ship → COGS → CM → OP) + bảng độ nhạy 2 chiều + giá hoà vốn → references/ của dinh-gia-san-pham |
| 6 | `mkt-meta-pixel-audit` | 290 | `meta-ads-analyzer`, `measurement` | meta-suite-os | Checklist 10 điểm Pixel + CAPI (event_id khử trùng, EMQ, advanced matching băm SHA256, tỷ lệ browser/server) → references/ của analyzer meta-suite-os; bỏ số hứa ROAS |
| 7 | `log-warehouse-stock-alert` | 290 | `stock-alert` | pancake-suite | Công thức SS/ROP/EOQ + 6 quy tắc cảnh báo (LOW, CRITICAL, OVERSTOCK, DEAD, NEGATIVE, EXPIRY) → references/ của stock-alert; bỏ code KiotViet |
| 8 | `quan-ly-ton-kho-mua-hang` | update | `stock-alert` | pancake-suite | Ma trận ABC-XYZ 9 ô + thang xử lý tồn chậm 5 mức + bảng KPI tồn kho → references/ của stock-alert |
| 9 | `sales-churn-risk-detector` | 290 | `13-do-luong-trai-nghiem`, `11-quan-ly-khach-hang` | sale-suite-os | 12 tín hiệu rủi ro 4 nhóm, chấm trọng số ra 4 vùng màu, playbook can thiệp theo vùng, theo dõi kết quả 30/60/90 → references/ của 13-do-luong-trai-nghiem |
| 10 | `sales-customer-health-score` | 290 | `13-do-luong-trai-nghiem`, `11-quan-ly-khach-hang` | sale-suite-os | 4 trục sức khoẻ 25 điểm/trục, cách lượng hoá từng tiểu mục, 4 ngưỡng phân lớp kèm hành động mặc định → references/ của 13-do-luong-trai-nghiem |
| 11 | `sales-late-stage-rescue` | 290 | `09-chot-sale`, `10-xu-ly-tu-choi` | sale-suite-os | 8 câu chẩn đoán deal kẹt, 6 nước cứu theo nguyên nhân gốc, kịch bản hỏi lại champion, mutual deadline có lý do thật → references/ của 09-chot-sale; bỏ số 'cứu 40-60%' |
| 12 | `sales-meddic-template` | 290 | `03-cham-diem-lead`, `16-kham-pha-nhu-cau` | sale-suite-os | Câu hỏi từng chữ MEDDPICC, tiêu chí champion thật = Power + Pain + Plan, red flag chưa gặp người ký sau demo → references/meddpicc.md của 03-cham-diem-lead |
| 13 | `sales-stakeholder-map` | 290 | `15-dam-phan-ban-hang`, `01-phan-khuc-chan-dung` | sale-suite-os | 8 vai trò trong hội đồng mua, chấm Power/Interest/Sentiment/Relationship, ma trận 2x2 kèm cách tiếp cận từng ô, tiêu chí champion thật → references/ của 15-dam-phan-ban-hang |
| 14 | `sales-win-loss-analyzer` | 290 | `14-huan-luyen-doi-sale`, `18-chuan-hanh-vi-sale` | sale-suite-os | Phân tích quy luật 6 chiều (lý do, giai đoạn kẹt, nguồn lead, người bán, ngành, đối thủ), phỏng vấn khách không để người bán tự hỏi → references/ của 14-huan-luyen-doi-sale |
| 15 | `cham-soc-sau-ban-hang` | update | `11-quan-ly-khach-hang`, `hot-leads` | sale-suite-os | Lịch follow-up sau bán theo mốc, kịch bản gọi chăm sóc, chiến lược tái kích hoạt khách cũ → references/ nhánh bán lẻ của 11-quan-ly-khach-hang |
| 16 | `xu-ly-khieu-nai-kho` | update | `12-xu-ly-su-co` | sale-suite-os | 3 kịch bản (giao trễ, đòi hoàn tiền không đủ điều kiện, dọa đăng Facebook), mẫu trả lời bình luận tiêu cực, danh sách điều kiện phải leo thang → references/ của 12-xu-ly-su-co |
| 17 | `Tối ưu Gian Hàng TMĐT - Shopee, Lazada, TikTok Shop` | update | `shopee-shop-analyzer`, `shopee-ads-analyzer` | shopee-suite-os | Checklist vận hành ngày/tuần/tháng + điểm shop + đồng bộ tồn/giá đa sàn + phần Lazada/TikTok Shop → references/ của shopee-shop-analyzer |

## Phụ lục B — 72 skill "mới" giá trị cao, theo nơi đặt

| Nơi đặt | Skill ngoài | Lấy gì |
|---|---|---|
| *mới: ban-hang-b2c* | `Chatbot & Bán Hàng Tự Động TMĐT` | 10 flow bắt buộc (chào, gợi ý, báo giá, lên đơn, tra vận đơn, FAQ, giỏ bỏ, kéo lại 30-60-90, feedback, upsell) + auto-tag/auto-assign + mẫu câu VN → skill kịch bản chatbot |
| *mới: ban-hang-b2c* | `Bán Hàng Qua Chat & Inbox Chuyên Sâu` | Quy trình 5 bước chat (chào, hỏi nhu cầu, tư vấn, xử lý lưỡng lự, chốt) + 4 kỹ thuật chốt + upsell trong chat + follow-up → skill bán qua chat mới |
| *mới: cskh* | `cs-canned-response-library` | Danh mục 30+ tình huống, cấu trúc template có biến {ten_kh} {ma_don}, quy tắc tone và pháp lý |
| *mới: cskh* | `cs-chatbot-script-designer` | Khung liệt kê intent, luồng top 10 intent, quy tắc fallback và handover sang người → nền cho bot CSKH của ZAgent/GoClaw |
| *mới: cskh* | `cs-escalation-matrix` | Bảng 4 mức S1-S4, ma trận leo thang theo thời gian lên TL/Manager/CEO, mẫu tin nhắn escalate có deadline |
| *mới: cskh* | `cs-faq-knowledge-base` | Quy trình thu câu hỏi nguồn từ ticket, cấu trúc KB theo danh mục-tag-phiên bản, mẫu article chuẩn |
| *mới: cskh* | `cs-review-response-shopee` | Template theo từng mức sao, lưu ý chính sách từng sàn, mẹo SEO local cho Google review |
| *mới: cskh* | `cs-ticket-tagging-automation` | Cách xây taxonomy tag, luật auto-tag theo từ khoá, ngưỡng chuyển AI cho ca khó, đo độ chính xác |
| *mới: cskh* | `chinh-sach-doi-tra-hang` | Mẫu chính sách đổi trả đầy đủ, form yêu cầu đổi trả, bảng phân chia phí ship, xử lý tình huống đặc biệt; bổ sung căn cứ pháp lý đã kiểm |
| *mới: cskh* | `kich-ban-tu-van-khach-hang` | Kịch bản tổng đài inbound, mẫu trả lời nhanh qua chat, nguyên tắc tone of voice → nền cho skill kịch bản tư vấn CSKH |
| *mới: cskh* | `quan-ly-ticket-ho-tro` | Vòng đời ticket 6 trạng thái, mẫu phiếu ticket, bảng SLA phản hồi/giải quyết/leo thang theo loại yêu cầu, mẫu báo cáo helpdesk |
| *mới: du-lieu* | `data-cohort-analysis` | Định nghĩa cohort + SQL bảng cohort + heatmap + LTV từ cohort; viết lại theo bảng chuẩn Bluecore |
| *mới: du-lieu* | `data-customer-segmentation` | SQL tính điểm RFM + bảng 11 phân khúc và hành động theo kênh Zalo/SMS/email |
| *mới: hanh-chinh* | `quan-ly-hop-dong` | Sổ hợp đồng + checklist ký + mẫu phụ lục/thanh lý + quy tắc cảnh báo 60/30/7 ngày; gộp điều khoản mua từ hop-dong-mua-hang |
| *mới: it* | `chuyen-doi-so` | Thang đánh giá mức số hoá + lộ trình theo giai đoạn + bảng ROI; bổ sung tầng AI agent |
| *mới: it* | `bao-mat-thong-tin` | Chính sách bảo mật + ma trận phân quyền + quy trình sự cố; gộp chính sách mật khẩu/BYOD từ it-it-policy-writer |
| *mới: mua-hang-kho-van* | `xu-ly-hang-huy-hang-loi` | Quy trình hàng hoàn + phiếu tiếp nhận + biên bản hủy hàng; nối kế toán hủy hàng với Company-finance-accountant-os |
| *mới: mua-hang-kho-van* | `log-shipping-cost-optimizer` | Bảng tiêu chí chọn hãng theo vùng/loại đơn + phương pháp so cước; giá cước phải tra lại, không dùng số trong skill |
| *mới: mua-hang-kho-van* | `quy-trinh-mua-hang` | Quy trình PR–PO–nhận hàng–hoá đơn, đối chiếu 3 bên, ma trận phê duyệt theo hạn mức; gộp mẫu PO từ proc-po-template |
| *mới: mua-hang-kho-van* | `quan-ly-nha-cung-cap` | Scorecard NCC + phân loại chiến lược; gộp 4 trục PQDS từ ops-supplier-scorecard |
| *mới: nhan-su* | `tuyen-dung` | Toàn bộ quy trình tuyển 7 bước + mẫu JD + kênh đăng tuyển VN; gộp phần Success Metrics từ hr-jd-writer |
| *mới: nhan-su* | `phong-van` | Kịch bản phỏng vấn theo vòng + ngân hàng câu hỏi + phiếu chấm; gộp rubric 5 điểm từ hr-candidate-scorecard |
| *mới: nhan-su* | `hop-dong-lao-dong` | 4 mẫu HĐLĐ + checklist điều khoản bắt buộc theo BLLĐ 2019; rà lại căn cứ trước khi dùng |
| *mới: nhan-su* | `onboarding-nhan-vien` | Checklist onboarding + kế hoạch tuần đầu + phiếu đánh giá thử việc; gộp khung mốc 30-60-90 từ hr-onboarding-30-60-90 |
| *mới: nhan-su* | `danh-gia-nhan-vien` | Phiếu đánh giá KPI + năng lực, quy trình calibration, mẫu 360; gắn với KR từ ke-hoach-okr |
| *mới: nhan-su* | `xu-ly-ky-luat` | Quy trình 5 bước + biên bản họp + mẫu PIP + thủ tục chấm dứt; SỬA: Đ.125 có 6 căn cứ sa thải, không phải 3 |
| *mới: nhan-su* | `chinh-sach-noi-bo` | Khung nội quy lao động + các chính sách lương thưởng, phép, làm việc từ xa; gộp mục lục sổ tay từ hr-employee-handbook |
| *mới: nhan-su* | `hr-payroll-input-checker` | Checklist soát input lương theo nhóm lỗi + bảng đối chiếu; bỏ phần code mẫu |
| *mới: nhan-su* | `hr-comp-band-builder` | Bảng band × level, công thức Min/Mid/Max theo P50, quy tắc compa-ratio; bỏ ví dụ lương cụ thể chưa có nguồn |
| *mới: nhan-su* | `hr-bonus-plan-design` | Cấu trúc quỹ thưởng + ma trận xếp loại × hệ số; bỏ các tỷ lệ % không nguồn |
| *mới: nhan-su* | `hr-headcount-plan` | Bảng định biên theo phòng × quý, giả định nghỉ việc, thay thế vs tuyển mới, tổng quỹ lương |
| *mới: phap-ly* | `legal-contract-review` | Phân loại hợp đồng → luật áp dụng + mẫu comment [RỦI RO CAO] kèm đề xuất sửa → gộp vào skill ra-soat-hop-dong |
| *mới: phap-ly* | `legal-nda-template` | Chọn loại NDA (1 chiều/2 chiều) + 8 thông tin bắt buộc + bố cục song ngữ 2 cột → skill nda |
| *mới: phap-ly* | `kiem-tra-phap-ly-hop-dong` | Checklist rà 8 phần + ma trận rủi ro 10 dòng + 5 điều khoản đỏ + thư đề nghị chỉnh sửa → skill ra-soat-hop-dong |
| *mới: phap-ly* | `soan-thao-hop-dong` | Cấu trúc hợp đồng 8 phần + mẫu hợp đồng dịch vụ + mua bán rút gọn + điều khoản đặc biệt → skill soan-hop-dong |
| *mới: pr-truyen-thong* | `mkt-pr-crisis-response` | Bảng phân vai 7 vai (CEO, PR, Pháp lý, CSKH, Sản phẩm, nội bộ, giám sát) + holding statement 50-100 chữ → gộp vào skill khủng hoảng mới |
| *mới: pr-truyen-thong* | `truyen-thong-khung-hoang` | Bảng phân cấp khủng hoảng + giao thức 24h + cấu trúc 4R + kế hoạch phục hồi + checklist chuẩn bị → skill khủng hoảng mới (thêm bảng phân vai của mkt-pr-crisis-response) |
| *mới: van-hanh* | `ops-rpa-opportunity-scout` | Bảng chấm cơ hội tự động hoá (tần suất, thời gian, lỗi, độ ổn định quy tắc) + công thức ROI; thêm lựa chọn GoClaw agent |
| *mới: van-hanh* | `ops-store-audit-template` | Bảng 100 mục chấm theo 6P + thang điểm + mẫu báo cáo theo cửa hàng |
| Company-finance-accountant-os | `ceo-cash-position-dashboard` | Dự báo tiền 13 tuần (vào/ra/tích luỹ, tuần đáy) + 5 chỉ số và ngưỡng cảnh báo → skill dong-tien-13-tuan |
| Company-finance-accountant-os | `fin-ar-aging-report` | Bảng tuổi nợ 0-30/31-60/61-90/>90 + action plan thu hồi theo nhóm → ban-chiu-cong-no (dự kiến) |
| Company-finance-accountant-os | `fin-bank-reconciliation` | Luật matching (số tiền, ngày ±n, nội dung) + mẫu bảng điều chỉnh chênh lệch → doi-soat (dự kiến); bỏ API Vietcombank bịa |
| Company-finance-accountant-os | `fin-cashflow-forecast-13week` | Mô hình 13 tuần 5 khối + cờ đỏ/đen theo ngưỡng tồn quỹ + 4 hành động cứu thanh khoản → ke-hoach-dong-tien (dự kiến) |
| Company-finance-accountant-os | `fin-cogs-breakdown` | Phân bổ chi phí ABC + bảng lợi nhuận SKU xếp Star/Marginal/Cut + phân tích 80-20 khách và kênh → pl-quan-tri (dự kiến) |
| Company-finance-accountant-os | `fin-credit-application-pack` | Danh mục hồ sơ vay + dàn ý phương án vay + bộ câu hỏi RM hay hỏi → von-luu-dong-va-vay-tra (dự kiến) |
| Company-finance-accountant-os | `fin-financial-model-3statement` | Cấu trúc tab model + P&L theo driver + quy tắc liên kết BS–CF và kiểm cân → mo-hinh-tai-chinh (dự kiến) |
| Company-finance-accountant-os | `fin-monthly-closing-checklist` | Checklist 4 cụm theo ngày (tiền – doanh thu/AR – chi phí/AP – báo cáo) + bảng task 5 trường → khoa-so-thang (dự kiến) |
| Company-finance-accountant-os | `phan-tich-tai-chinh` | Scorecard sức khoẻ tài chính 100 điểm + cây DuPont → kham-suc-khoe-tai-chinh (dự kiến); mốc chuẩn ngành phải ghi nguồn |
| Company-finance-accountant-os | `quan-ly-cong-no` | Mẫu biên bản đối chiếu công nợ + quy trình thu hồi nợ quá hạn theo mốc → ban-chiu-cong-no / doi-soat (dự kiến) |
| Company-finance-accountant-os | `bao-cao-tai-chinh-cho-bgd` | Bố cục CFO dashboard tháng + phân tích cầu nối lợi nhuận (bridge) + rolling forecast → pl-quan-tri (dự kiến) và agent cfo |
| Company-suite-os | `ops-incident-rca` | Quy trình RCA 3 công cụ + mẫu xương cá 6M + Pareto; đặt là cai-tien-rca cạnh cai-tien-dmaic |
| Company-suite-os | `cai-tien-lien-tuc-kaizen` | Bảng 7 muda + phiếu sáng kiến + vòng PDCA; thêm bảng 8 lãng phí TIMWOODS từ ops-waste-reduction-plan |
| Company-suite-os | `ops-sop-writer` | Khung SOP 5 phần + checklist; gộp kiểm soát thay đổi quy trình từ kiem-soat-quy-trinh-san-xuat; đặt là thuc-thi-sop |
| Company-suite-os | `ceo-decision-log` | Khung 7 trường bắt buộc + 4 loại quyết định + nhịp rà tháng/quý/năm → skill so-quyet-dinh |
| Company-suite-os | `ceo-meeting-summarizer` | Cấu trúc biên bản (TL;DR 3 dòng, quyết định, việc-người-hạn, parking lot) + quy tắc tóm tắt → skill bien-ban-hop, đẩy việc qua linear-task |
| compliance-vn | `legal-privacy-policy` | Cấu trúc chính sách 12 mục + bảng loại dữ liệu/nguồn/mục đích/cơ sở + phần cookie → templates/chinh-sach-quyen-rieng-tu.md của tuan-thu-doanh-nghiep |
| compliance-vn | `tieu-chuan-va-chung-nhan-san-pham` | Bảng chứng nhận bắt buộc theo ngành + quy trình đạt ISO 7 bước + chứng nhận theo thị trường xuất khẩu → skill tuan-thu-san-pham |
| investment-MA-os | `ceo-fundraising-deck` | 12 slide chuẩn + quy tắc thiết kế slide + danh sách tư liệu cần thu → skill goi-von-pitch-deck |
| investment-MA-os | `ceo-investor-update` | 8 số cốt lõi (chỉnh cho bán lẻ, không chỉ SaaS) + cấu trúc thư TL;DR/Tốt/Xấu/Tiếp theo/Đề nghị + quy tắc giọng → skill cap-nhat-nha-dau-tu |
| marketing-business-skill | `mkt-loyalty-program-design` | Bước tính ROI chương trình và quy tắc điểm gộp vào skill loyalty mới |
| marketing-business-skill | `CRM, Chăm sóc khách hàng & Chương trình Loyalty TMĐT` | RFM chấm 1-5 + 6 phân khúc kèm hành động + thiết kế hạng/điểm + mẫu tin chăm sóc → skill loyalty-RFM mới; bỏ % doanh thu/giữ chân bịa |
| marketing-business-skill | `ecom-livestream-seller` | Kịch bản live 2 giờ theo mốc phút + câu thoại xử lý nghi ngờ/FOMO/chốt + checklist trước live 24h/1h/10' + KPI sau live → skill livestream mới |
| marketing-business-skill | `ecom-product-listing` | Công thức tiêu đề theo từng sàn + bullet template + cấu trúc 7 phần + power words theo ngành → skill mô tả sản phẩm mới |
| marketing-business-skill | `xay-dung-loyalty-program` | Khung hạng thành viên và quyền lợi, quy trình tích/đổi điểm, nâng/hạ hạng, lịch truyền thông, chỉ số đo hiệu quả loyalty |
| pancake-suite | `theo-doi-don-hang` | Sơ đồ trạng thái đơn + quy trình xử lý đơn trễ/thất bại + báo cáo tỷ lệ giao thành công/hoàn |
| sale-suite-os | `cs-customer-success-onboarding` | Hành trình 0-90 ngày, checklist onboarding cho khách, healthcheck và cảnh báo sớm → một skill mới ban giao + onboarding cùng sales-postsale-handover |
| sale-suite-os | `sales-channel-partner-recruit` | Chân dung đối tác lý tưởng, 6 điểm kiểm thẩm định đối tác, khung điều khoản thương mại → skill mới kenh-dai-ly gộp cùng sales-distributor-onboarding |
| sale-suite-os | `sales-demo-script` | Khung demo 30 phút Tell-Show-Tell, recap discovery đầu buổi, 3 use case theo persona, trial close và chốt bước tiếp |
| sale-suite-os | `sales-distributor-onboarding` | Lộ trình 3 giai đoạn 30-60-90, hệ chứng nhận đại lý, ramp chỉ tiêu → skill mới kenh-dai-ly gộp cùng sales-channel-partner-recruit |
| sale-suite-os | `sales-mutual-action-plan` | Quy tắc đồng soạn với champion, 8 mốc phổ biến, bảng 2 cột chủ phía khách/phía mình, luật trễ mốc phải leo thang → references/ của 09-chot-sale |
| sale-suite-os | `sales-postsale-handover` | Agenda họp bàn giao nội bộ 45 phút, hồ sơ bàn giao 2 trang (gồm cam kết miệng), kickoff với khách, 30 ngày sale kèm → skill mới ban-giao gộp cùng cs-customer-success-onboarding |
| sale-suite-os | `du-bao-doanh-so` | Các phương pháp dự báo, 3 kịch bản, phân tích gap mục tiêu vs dự báo, dự báo theo tháng/quý/năm; gộp thêm weighted pipeline từ sales-pipeline-forecast |

## Phụ lục C — 58 skill "loại"

| Skill ngoài | Nhóm | Lý do |
|---|---|---|
| `hr-jd-writer` | nhan-su-van-hanh-khac | Trùng tuyen-dung; chỉ giữ ý Success Metrics trong JD để gộp vào bản tốt hơn. |
| `hr-interview-question-bank` | nhan-su-van-hanh-khac | Trùng phong-van, mỏng hơn; ngân hàng câu hỏi chung chung. |
| `hr-onboarding-30-60-90` | nhan-su-van-hanh-khac | Trùng onboarding-nhan-vien; chỉ khung mốc 30-60-90 đáng gộp vào bản tốt hơn. |
| `hr-perf-review-template` | nhan-su-van-hanh-khac | Trùng danh-gia-nhan-vien, mỏng hơn. |
| `hr-360-feedback-tool` | nhan-su-van-hanh-khac | Đã nằm trong danh-gia-nhan-vien; SME dưới 50 người ít dùng 360 riêng. |
| `hr-disciplinary-letter` | nhan-su-van-hanh-khac | Trùng xu-ly-ky-luat; có số bịa (DN thua >60%), endpoint giả, thời hiệu tính sai mốc. Chỉ lấy mẫu quyết định kỷ luật. |
| `hr-pip-builder` | nhan-su-van-hanh-khac | PIP đã có trong xu-ly-ky-luat; bản này không thêm gì đáng kể. |
| `hr-employee-handbook` | nhan-su-van-hanh-khac | Trùng chinh-sach-noi-bo; chỉ có mục lục 8–10 phần, nội dung mỏng. |
| `hr-leave-policy` | nhan-su-van-hanh-khac | Trùng quan-ly-nghi-phep, ngắn hơn. |
| `hr-training-needs-analysis` | nhan-su-van-hanh-khac | TNA đã nằm trong ke-hoach-dao-tao. |
| `hr-training-curriculum` | nhan-su-van-hanh-khac | Trùng ke-hoach-dao-tao; chỉ khung module và Kirkpatrick đáng gộp. |
| `hr-culture-survey-analyzer` | nhan-su-van-hanh-khac | Gần trùng hr-engagement-survey; chỉ ý so khoảng cách giá trị tuyên bố và thực tế đáng gộp. |
| `ops-5why-builder` | nhan-su-van-hanh-khac | Tập con của ops-incident-rca. |
| `ops-waste-reduction-plan` | nhan-su-van-hanh-khac | Trùng cai-tien-lien-tuc-kaizen; chỉ bảng TIMWOODS đáng gộp. |
| `kiem-soat-quy-trinh-san-xuat` | nhan-su-van-hanh-khac | SOP bản sản xuất, trùng ops-sop-writer; chỉ phần kiểm soát thay đổi quy trình đáng gộp. |
| `ops-quality-checklist` | nhan-su-van-hanh-khac | Trùng quan-ly-chat-luong-qc; chỉ bảng AQL đáng gộp. |
| `ops-capacity-planning` | nhan-su-van-hanh-khac | Trùng ke-hoach-san-xuat và quan-ly-cong-suat. |
| `quan-ly-cong-suat` | nhan-su-van-hanh-khac | Trùng ke-hoach-san-xuat; ý tự làm vs thuê ngoài có thể gộp. |
| `ops-bom-builder` | nhan-su-van-hanh-khac | Trùng quan-ly-nguyen-vat-lieu; chỉ cấu trúc BOM đa cấp đáng gộp. |
| `ops-maintenance-schedule` | nhan-su-van-hanh-khac | Trùng bao-tri-thiet-bi. |
| `ops-oee-tracker` | nhan-su-van-hanh-khac | OEE nên là một mục trong bao-cao-san-xuat; phần dashboard thời gian thực là code giả. |
| `ops-energy-cost-audit` | nhan-su-van-hanh-khac | Audit điện theo máy cho nhà máy; nhiều số % tiết kiệm không nguồn, xa trọng tâm MQ. |
| `an-toan-lao-dong-san-xuat` | nhan-su-van-hanh-khac | Trùng noi-quy-an-toan; phần nhận dạng nguy cơ sản xuất có thể gộp. |
| `quan-ly-hang-ton-kho` | nhan-su-van-hanh-khac | Trùng hai bản trên và stock-alert, không thêm gì. |
| `an-toan-kho-bai` | nhan-su-van-hanh-khac | Trùng noi-quy-an-toan; phần PCCC kho gộp vào bản đó. |
| `toi-uu-chi-phi-logistics` | nhan-su-van-hanh-khac | Trùng log-shipping-cost-optimizer; phần phân tích cấu trúc chi phí logistics có thể gộp. |
| `quan-ly-nha-cung-cap-logistics` | nhan-su-van-hanh-khac | Trùng log-shipping-cost-optimizer và quan-ly-nha-cung-cap; KPI nhà vận chuyển gộp vào bản tốt hơn. |
| `proc-po-template` | nhan-su-van-hanh-khac | Mẫu PO là một phần của quy-trinh-mua-hang. |
| `mua-sam-va-dau-thau` | nhan-su-van-hanh-khac | Bản hành chính trùng quy-trinh-mua-hang và dau-thau-va-rfq. |
| `proc-rfq-builder` | nhan-su-van-hanh-khac | Trùng dau-thau-va-rfq. |
| `proc-vendor-shortlist-scoring` | nhan-su-van-hanh-khac | Trùng dau-thau-va-rfq và quan-ly-nha-cung-cap; bảng chấm 5 tiêu chí đáng gộp. |
| `ops-supplier-scorecard` | nhan-su-van-hanh-khac | Trùng quan-ly-nha-cung-cap; chỉ khung PQDS đáng gộp. |
| `hop-dong-mua-hang` | nhan-su-van-hanh-khac | Trùng quan-ly-hop-dong; điều khoản riêng của hợp đồng mua có thể gộp làm một phụ lục. |
| `mua-hang-ben-vung` | nhan-su-van-hanh-khac | Mua hàng xanh/ESG chung chung, ít giá trị thực cho SME Việt Nam hiện tại. |
| `so-hoa-mua-hang` | nhan-su-van-hanh-khac | Chọn phần mềm procurement/e-procurement chung chung; đã bao trong chuyen-doi-so. |
| `data-sql-query-helper` | nhan-su-van-hanh-khac | Viết và tối ưu SQL chung chung, mô hình đã tự làm tốt; không đặc thù MQ. |
| `it-it-policy-writer` | nhan-su-van-hanh-khac | Trùng bao-mat-thong-tin; chính sách mật khẩu, BYOD, sử dụng chấp nhận được gộp vào bản đó. |
| `it-data-backup-policy` | nhan-su-van-hanh-khac | Trùng sao-luu-phuc-hoi-du-lieu. |
| `it-saas-cost-optimizer` | nhan-su-van-hanh-khac | Trùng it-vendor-saas-audit; hứa tiết kiệm 25-40% không căn cứ. |
| `quan-ly-nha-cung-cap-it` | nhan-su-van-hanh-khac | Trùng quan-ly-nha-cung-cap và it-vendor-saas-audit. |
| `quan-ly-ha-tang-it` | nhan-su-van-hanh-khac | Trùng quan-ly-tai-san và it-asset-inventory; phần mạng nội bộ chung chung. |
| `it-asset-inventory` | nhan-su-van-hanh-khac | Trùng quan-ly-tai-san (sổ tài sản, cấp phát, khấu hao). |
| `bao-cao-it` | nhan-su-van-hanh-khac | Báo cáo KPI IT chung chung, SME ít có bộ phận IT riêng. |
| `bao-cao-hanh-chinh` | nhan-su-van-hanh-khac | Báo cáo chi phí hành chính chung chung, không có khung đặc thù. |
| `quan-ly-van-phong` | nhan-su-van-hanh-khac | Văn phòng phẩm, cơ sở vật chất; giá trị thấp, phần tài sản đã có ở quan-ly-tai-san. |
| `cham-soc-khach-hang-noi-bo` | nhan-su-van-hanh-khac | Tiếp nhận yêu cầu nội bộ; trùng ho-tro-ky-thuat-it và onboarding, nội dung chung chung. |
| `bao-cao-xnk` | nhan-su-van-hanh-khac | Dashboard kim ngạch XNK chung chung, không có khung đặc thù. |
| `tich-hop-cong-nghe-vao-san-pham` | quan-tri-phap-ly-san-pham | Quá chung chung (bảng use case AI phổ thông, ROI để trống); hệ MQ đã đi sâu hơn nhiều về AI agent. |
| `cs-renewal-risk-alert` | sale-cskh | Trùng trong kho: tín hiệu rủi ro đã có ở sales-churn-risk-detector, mốc 90/60/30 đã có ở sales-renewal-playbook. |
| `sales-pitch-deck-investor-style` | sale-cskh | Trùng sales-sales-deck-builder, thiên deck enterprise kiểu Mỹ; pitch deck gọi vốn đã có ở repo đầu tư. |
| `cham-soc-khach-hang` | sale-cskh | Trùng trong kho với cham-soc-sau-ban-hang (bản đầy đủ hơn, có win-back và kịch bản gọi). |
| `fin-finance-ops-automation` | tai-chinh-ke-toan | Chung chung Make/Zapier, hứa tiết kiệm 50-70% không căn cứ, API bịa; MQ đã đi hướng agent GoClaw/MCP. |
| `fin-revenue-recognition-asc606` | tai-chinh-ke-toan | Theo US GAAP/IFRS 15, không phải chuẩn bắt buộc của SME Việt Nam (VAS/TT99); dễ gây áp sai chuẩn. |
| `fin-tax-cit-estimator` | tai-chinh-ke-toan | Bịa thuế suất TNDN (17% DT ≤3 tỷ, 15% ≤200tr, 0% 4 năm); 'TT 132' thật ra NĐ132/2020; căn cứ NĐ218/TT78 hết hiệu lực; API MISA bịa. |
| `fin-tax-vat-summary` | tai-chinh-ke-toan | Ngưỡng tiền mặt 20 triệu lỗi thời (nay 5 triệu), điều kiện hoàn 12 tháng âm đã bỏ từ 2016; thue-gtgt phải viết từ luật gốc. |
| `ke-khai-thue` | tai-chinh-ke-toan | Căn cứ lỗi thời: chi quảng cáo trần 15% đã bỏ từ 2015, ngưỡng 20 triệu, giảm trừ cũ, hạn nộp TNDN sai; lịch thuế đã có ở compliance-vn. |
| `tinh-luong-thuong` | tai-chinh-ke-toan | Căn cứ lỗi thời: giảm trừ 11/4,4 triệu, lương tối thiểu vùng cũ, Luật BHXH 2014; trần BHTN tính sai. Tính lương phải dựng lại từ luật gốc. |
| `thue-doanh-nghiep` | tai-chinh-ke-toan | Sai/lỗi thời: DN ≤3 tỷ 'không ưu đãi' trái Luật TNDN 2025 (15%), hiểu sai quỹ KH&CN 10%, gán thời hạn thanh tra cho NĐ126, giảm trừ cũ. |
