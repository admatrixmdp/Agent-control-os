<!-- AGENT-EVOLUTION:BAT-DAU -->
# Agent Evolution

Tên agent: Agent Evolution (`agent-evolution`). Sổ nằm ở `~/.agent-evolution/`, không commit.

- Trước việc giống việc cũ: `python3 ~/.agent-evolution/ledger.py search "..." --tier durable`.
- Ghi bài mới ở tầng `scratch`, kèm bằng chứng. Không chép dữ liệu khách, trích dẫn thật, bí mật.
- Bài `user`, `finance`, `sensitive` không tự lên `durable` hay `accepted`. Cần duyệt của cả Dat và Quân. Chỉ điền `--owner-approved` sau khi cả hai đã đồng ý.
- Việc đụng người khác, tiền, dữ liệu nhạy, hoặc việc vốn bị cấm: hỏi trước.
- Không commit `ledger.db`, `wiki/`, `proposals/`, `bao-cao/`.
- Khi chạy không người xem, Agent Evolution chỉ được ghi tầng `scratch`.
<!-- AGENT-EVOLUTION:KET-THUC -->
