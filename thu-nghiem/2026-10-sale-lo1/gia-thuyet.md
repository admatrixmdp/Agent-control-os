# Lô 1 — mảng sale — 2026-10-26

## Giả thuyết

1. Nhãn đề xuất ở bước 4 (`skill-lab/anh-xa/theo-nghia/sale-cskh.yaml`) đúng khi kiểm bằng chạy thử, không chỉ đọc văn bản.
2. Skill nội bộ sale-suite cho kết quả tốt hơn bản không skill trên cùng tình huống.

## Chọn mẫu

4 cặp phủ đủ các nhãn kho đã gắn:

| ID | Skill ngoài | Skill nội bộ | Nhãn kho gắn |
|---|---|---|---|
| TN1-01 | sales-lead-scoring-engine | 03-cham-diem-lead | Bổ sung (vừa) |
| TN1-02 | sales-objection-handling | 10-xu-ly-tu-choi | Bổ sung (vừa) |
| TN1-03 | sales-late-stage-rescue | 09-chot-sale | Bổ sung (cao) |
| TN1-04 | sales-discovery-call-template | 16-kham-pha-nhu-cau | Trùng |

Cộng thêm `sales-icp-builder` ↔ `01-phan-khuc-chan-dung` đã thử tay cùng ngày (không chấm mù, chỉ so theo rubric 10 tiêu chí: 18/30 vs 19/30).

## Cách chạy

- Mỗi tình huống chạy 3 bản: **skill nội bộ / skill ngoài / không skill**. Mô hình chạy: Sonnet, qua agent con trong một phiên Claude.
- Bản không skill: dặn không dùng skill, không dùng công cụ.
- Giám khảo: Opus, chấm mù, thứ tự X/Y/Z xáo ngẫu nhiên. 5 tiêu chí × 0–5: Bẫy · Quyết định · Bối cảnh VN · Trung thực · Dùng được. Tổng /25.

## Giới hạn đã biết (đọc trước khi dùng kết quả)

| Giới hạn | Hệ quả |
|---|---|
| **Bản "không skill" bị rò tri thức** — agent con chạy trong môi trường có sẵn mô tả skill và hồ sơ người dùng; nó tự dùng khung 5T và Lửa/Khí/Nước/Đất của sale-suite | Không kết luận được skill nội bộ có thừa hay không |
| Đề TN1-02 ghi sẵn "nhóm Đất" → mớm cho cả 3 bản | Tiêu chí "điều chỉnh theo tính cách" không phân biệt được |
| 1 tình huống/cặp, 1 giám khảo, 1 lần chạy | Nhiễu cao; chỉ đủ để định hướng |

→ Lô sau chạy bằng `may-cham cham --so-sanh` qua API thô (không plugin, không bộ nhớ), ≥ 3 tình huống/skill, 2 giám khảo.
