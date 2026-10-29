# GoClaw (hạ tầng agent nội bộ MQ)

| Mục | Nội dung |
|---|---|
| Lớp | A |
| Lối vào tri thức | Skill (cấp cho agent / người dùng), file agent, memory, Knowledge Vault |
| Lối vào quy tắc | Cấu hình agent, quyền tool, MCP server được cấp, team |
| Bộ nhớ | `goclaw_memory_*`; Knowledge Vault (đang định tổ chức theo LLM Wiki) |
| Lịch | **Cron** (`goclaw_cron_*`) — nơi chạy vòng B ban đêm |
| Đầu ra & trace | **Trace** (`goclaw_trace_list/get`) — nguồn dữ liệu chính cho chấm phiên tự động |
| Giới hạn cứng | Chưa xác nhận trace có đủ token / lượt tool / kết quả để điền sổ chấm điểm tự động — cần kiểm |
| Nên giao | Việc định kỳ (báo cáo ngày/tuần), đội agent marketing, chạy vòng B |
| Không giao | Việc mức "Cấm" |
| Eval | Chạy `may-cham` như một custom tool hoặc qua cron gọi script |

Repo liên quan: `admatrixorg/goclaw-custom`, `admatrixorg/goclaw-ops`. Xác nhận: 2026-10-26.
