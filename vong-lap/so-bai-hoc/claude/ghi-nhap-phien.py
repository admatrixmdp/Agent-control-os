#!/usr/bin/env python3
"""Ghi một bài scratch trỏ tới mã phiên. Không chép nội dung phiên.

Hook Stop / SessionEnd gọi script này và đẩy JSON vào stdin.
Cùng một mã phiên thì không tạo bài thứ hai.
"""
import json
import os
import re
import sqlite3
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.environ.get("SELF_EVO_DB", os.path.join(HERE, "ledger.db"))
ROOT = os.environ.get("SELF_EVO_ROOT", HERE)
LEDGER = os.path.join(HERE, "ledger.py")


def main():
    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        return 0
    if not isinstance(data, dict):
        return 0
    sid = str(data.get("session_id") or data.get("sessionId") or "")
    sid = re.sub(r"[^A-Za-z0-9_-]", "", sid)[:64]
    if not sid:
        return 0
    uid = "phien-" + sid
    if os.path.exists(DB):
        con = sqlite3.connect(DB)
        try:
            row = con.execute("SELECT 1 FROM lessons WHERE uid=?", (uid,)).fetchone()
        except sqlite3.OperationalError:
            row = None
        con.close()
        if row:
            return 0
    cmd = [
        sys.executable, LEDGER,
        "--db", DB, "--root", ROOT, "--actor", "agent-evolution",
        "add", "--bot", "agent-evolution",
        "--title", "Phiên cần rà",
        "--text", "Có phiên mới. Chưa rút bài. Không chép nội dung phiên vào sổ.",
        "--tier", "scratch", "--sensitivity", "user",
        "--nen-tang", "claude-code", "--tenant", "may-rieng",
        "--confidence", "0.3", "--uid", uid,
        "-e", "transcript:" + sid,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr or proc.stdout)
        return proc.returncode
    return 0


if __name__ == "__main__":
    sys.exit(main())
