#!/usr/bin/env bash
# Cài Agent Evolution trên máy riêng. Chạy lại được. Không ghi bí mật, không bật hook hay cron.
set -euo pipefail

CLAUDE_SRC=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
SO=$(CDPATH= cd -- "$CLAUDE_SRC/.." && pwd)
REPO=$(CDPATH= cd -- "$SO/../.." && pwd)

DEST="${HOME}/.agent-evolution"
CLAUDE_HOME="${HOME}/.claude"
CLAUDE_MD="${CLAUDE_HOME}/CLAUDE.md"

while [ $# -gt 0 ]; do
  case "$1" in
    --dest) DEST=$2; shift 2 ;;
    --claude-home) CLAUDE_HOME=$2; shift 2 ;;
    --claude-md) CLAUDE_MD=$2; shift 2 ;;
    -h|--help)
      echo "Dùng: cai-dat.sh [--dest DIR] [--claude-home DIR] [--claude-md FILE]"
      echo "Mặc định: ~/.agent-evolution và ~/.claude/CLAUDE.md"
      exit 0
      ;;
    *) echo "Không rõ tham số: $1" >&2; exit 2 ;;
  esac
done

mkdir -p "$DEST" "$CLAUDE_HOME/agents" "$CLAUDE_HOME/skills/agent-evolution" "$CLAUDE_HOME/skills/so-bai-hoc" "$(dirname "$CLAUDE_MD")"

cp "$SO/ledger.py" "$DEST/ledger.py"
cp "$CLAUDE_SRC/ghi-nhap-phien.py" "$DEST/ghi-nhap-phien.py"
cp "$CLAUDE_SRC/ra-lich.sh" "$DEST/ra-lich.sh"
cp "$CLAUDE_SRC/loi-nhac-ra.txt" "$DEST/loi-nhac-ra.txt"
cp "$REPO/.claude/agents/agent-evolution.md" "$CLAUDE_HOME/agents/agent-evolution.md"
cp "$REPO/vong-lap/agent-evolution/SKILL.md" "$CLAUDE_HOME/skills/agent-evolution/SKILL.md"
cp "$SO/SKILL.md" "$CLAUDE_HOME/skills/so-bai-hoc/SKILL.md"
chmod +x "$DEST/ghi-nhap-phien.py" "$DEST/ra-lich.sh"

printf '%s\n' "$REPO" > "$DEST/nguon.txt"

cat > "$DEST/.gitignore" <<'EOF'
*.db
*.db-journal
*.db-wal
*.db-shm
wiki/
staging/
proposals/
bao-cao/
EOF

cat > "$DEST/sbh" <<EOF
#!/bin/sh
set -eu
DEST=\$(CDPATH= cd -- "\$(dirname "\$0")" && pwd)
ROOT=\$(cat "\$DEST/nguon.txt")
exec python3 "\$DEST/ledger.py" --db "\$DEST/ledger.db" --root "\$DEST" --catalog "\$ROOT/danh-muc/skills.yaml" --actor agent-evolution "\$@"
EOF
chmod +x "$DEST/sbh"

# Tạo sổ trống nếu chưa có. Không ghi bài.
if [ ! -f "$DEST/ledger.db" ]; then
  python3 "$DEST/ledger.py" --db "$DEST/ledger.db" --root "$DEST" list >/dev/null
fi

BLOCK="$CLAUDE_SRC/khoi-claude-md.md"
export AGENT_EVOLUTION_MD="$CLAUDE_MD"
export AGENT_EVOLUTION_BLOCK="$BLOCK"
python3 - <<'PY'
import os
md = os.environ["AGENT_EVOLUTION_MD"]
block = open(os.environ["AGENT_EVOLUTION_BLOCK"], encoding="utf-8").read().strip() + "\n"
start = "<!-- AGENT-EVOLUTION:BAT-DAU -->"
end = "<!-- AGENT-EVOLUTION:KET-THUC -->"
text = open(md, encoding="utf-8").read() if os.path.exists(md) else ""
if start in text and end in text:
    pre, rest = text.split(start, 1)
    _, post = rest.split(end, 1)
    new = pre.rstrip() + "\n\n" + block + post.lstrip("\n")
    if not new.endswith("\n"):
        new += "\n"
else:
    if text and not text.endswith("\n"):
        text += "\n"
    if text and not text.endswith("\n\n"):
        text += "\n"
    new = text + block
open(md, "w", encoding="utf-8").write(new)
PY

echo "Đã cài Agent Evolution vào $DEST"
echo "Luật CLAUDE.md: $CLAUDE_MD"
echo "Chưa bật hook, chưa đăng ký cron."
