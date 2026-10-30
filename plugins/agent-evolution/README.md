# Agent Evolution

Thợ tiến hoá duy nhất của hệ MQ. Bản mô tả đầy đủ: [`agents/agent-evolution.md`](agents/agent-evolution.md). Nền tảng nào chạy cũng đọc cùng file này.

## Ai làm gì

| Ai | Việc |
|---|---|
| **Mọi agent** (Claude, Codex, GoClaw, Goso, Grok…) | Bị sửa hoặc gặp lỗi → nộp **một** bài học vào hộp thư: `python3 vong-lap/so-bai-hoc/hop_thu.py nop ...` |
| **Agent Evolution** | 9:00 thứ Hai và thứ Năm: nhập hộp thư → dọn sổ → chọn ≤ 3 skill → chấm trước → thêm bài học → chấm sau → mở PR nếu tốt hơn → báo cáo |
| **Quân, Dat** | Duyệt PR; duyệt bài học lên tầng chắc chắn; bài nhạy cảm cần cả hai |

## Cài

**Grok Bot (nền tảng chính):** xem mục "Agent Evolution trên Grok Bot" trong [`nen-tang/grok-bot.md`](../../nen-tang/grok-bot.md).

**Claude Code:**

```
/plugin marketplace add admatrixmdp/Agent-control-os
/plugin install agent-evolution@agent-control-os
```

Plugin chỉ chứa bản mô tả agent. Sổ bài học và máy chấm nằm trong repo, nên máy chạy phải có bản clone `Agent-control-os` và đặt biến `AGENT_CONTROL_OS`. Chưa thử cài trên máy thật.

**Chỉ chạy một thợ tiến hoá tại một thời điểm.** Hai nơi cùng chạy sẽ mở PR đá nhau.
