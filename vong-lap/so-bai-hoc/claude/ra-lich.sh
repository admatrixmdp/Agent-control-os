#!/bin/sh
# Lượt rà không người xem. Cron/launchd gọi file này. Bộ cài không tự đăng ký lịch.
set -eu
DEST=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
export SELF_EVO_DB="${SELF_EVO_DB:-$DEST/ledger.db}"
export SELF_EVO_ROOT="${SELF_EVO_ROOT:-$DEST}"
export SELF_EVO_ACTOR="${SELF_EVO_ACTOR:-agent-evolution}"
exec claude -p --agent agent-evolution "$(cat "$DEST/loi-nhac-ra.txt")"
