"""Cổng 3 — vệ sinh PR: file cấm, dữ liệu thật trong dòng thêm mới, link phiên, footer Cursor.

    python3 .github/ve_sinh.py --base origin/harness-v1     # PR_BODY lấy từ biến môi trường nếu có
Chỉ quét dòng THÊM MỚI so với base và commit message trong khoảng base..HEAD (lịch sử cũ không quét).
"""
import argparse
import os
import re
import subprocess
import sys

FILE_CAM = re.compile(r"\.(db|sqlite3?|db-journal|db-wal)$|(^|/)\.env(\..+)?$", re.I)
# File định nghĩa mẫu quét; được CODEOWNERS bảo vệ
KHONG_QUET = {".gitleaks.toml", ".github/ve_sinh.py"}
# Giữ chỗ công khai được phép: domain/org/app/tenant giả
GIU_CHO = re.compile(r"\b(?:[\w-]+\.)*example\.(?:com|vn)\b|\borg-[ab]\b|\bapp-agent\b|\btenant-demo\b", re.I)
MAU = {
    "số điện thoại": re.compile(r"(?<![\w.])(?:\+?84[ .-]?|0)[35789](?:[ .-]?\d){8}(?![\w])"),
    "email": re.compile(r"\b[\w.%+-]+@(?:[\w-]+\.)+[A-Za-z]{2,}\b"),
    "link phiên agent": re.compile(r"claude\.ai/(?:code/session_|chat/|share/)|cursor\.com/(?:agents|background-agent)\b|chatgpt\.com/(?:share|c)/", re.I),
    "domain/org nội bộ": re.compile(r"\badmatrix(?:org|mdp)?\.(?:vn|com|io|net)\b|github\.com/admatrix(?:org|mdp)\b", re.I),
    "IP": re.compile(r"(?<![\w.])(?!127\.0\.0\.1|0\.0\.0\.0|192\.0\.2\.|198\.51\.100\.|203\.0\.113\.)(?:\d{1,3}\.){3}\d{1,3}(?![\w.])"),
    "đường dẫn cá nhân": re.compile(r"/(?:Users|home)/(?!<|box\b|runner\b|ten\b|user\b)[A-Za-z][\w.-]+"),
}
FOOTER_CURSOR = re.compile(r"CURSOR_AGENT_PR_BODY|Open in Cursor|Open in Web|cursor\.com/(?:agents|background-agent)", re.I)


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout


def quet(chu, noi, loi):
    sach = GIU_CHO.sub("", chu)
    for ten, mau in MAU.items():
        for m in mau.finditer(sach):
            loi.append(f"{noi}: {ten} «{m.group(0)}»")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    a = ap.parse_args()
    loi = []
    for dong in git("diff", "--name-status", "--diff-filter=AMRC", f"{a.base}...HEAD").splitlines():
        p = dong.split("\t")[-1]
        if FILE_CAM.search(p):
            loi.append(f"{p}: file cấm (.db/.sqlite/.env) không được đưa vào repo")
    tep = None
    for d in git("diff", "-U0", "--no-color", f"{a.base}...HEAD").splitlines():
        if d.startswith("+++ "):
            tep = d[6:] if d.startswith("+++ b/") else None
        elif d.startswith("@@"):
            so = int(re.search(r"\+(\d+)", d).group(1))
        elif d.startswith("+") and tep and tep not in KHONG_QUET:
            quet(d[1:], f"{tep}:{so}", loi)
            so += 1
    for sha in git("rev-list", f"{a.base}..HEAD").split():
        msg = git("log", "-1", "--format=%B", sha)
        for m in MAU["link phiên agent"].finditer(msg):
            loi.append(f"commit {sha[:7]}: link phiên agent «{m.group(0)}» trong commit message")
    than = os.environ.get("PR_BODY", "")
    for m in MAU["link phiên agent"].finditer(than):
        loi.append(f"thân PR: link phiên agent «{m.group(0)}»")
    if FOOTER_CURSOR.search(than):
        loi.append("thân PR: còn footer Cursor, hãy xóa")
    for x in loi:
        print("LỖI  " + x)
    print("Vệ sinh đạt" if not loi else f"Vệ sinh trượt: {len(loi)} lỗi")
    return 1 if loi else 0


if __name__ == "__main__":
    sys.exit(main())
