#!/usr/bin/env python3
"""Cài Agent Evolution vào thư mục tạm. Không đụng máy thật, không có dữ liệu thật."""
import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CAI = os.path.join(ROOT, "vong-lap", "so-bai-hoc", "claude", "cai-dat.sh")
CHAM = os.path.join(ROOT, "may-cham", "cham.py")
SKILL_DIR = os.path.join(ROOT, "vong-lap", "agent-evolution")


def rd(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


class CaiDat(unittest.TestCase):
    def test_cai_hai_lan_va_hook(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        dest = os.path.join(tmp.name, "nha", ".agent-evolution")
        claude = os.path.join(tmp.name, "claude")
        md = os.path.join(claude, "CLAUDE.md")
        os.makedirs(claude)
        with open(md, "w", encoding="utf-8") as fh:
            fh.write("Dong giu.\n")
        sentinel = os.path.join(claude, "settings.json")
        with open(sentinel, "w", encoding="utf-8") as fh:
            fh.write('{"giu": true}\n')

        def cai():
            proc = subprocess.run(
                ["bash", CAI, "--dest", dest, "--claude-home", claude, "--claude-md", md],
                capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            return proc

        cai()
        cai()
        text = rd(md)
        self.assertTrue(text.startswith("Dong giu."))
        self.assertEqual(text.count("<!-- AGENT-EVOLUTION:BAT-DAU -->"), 1)
        self.assertEqual(text.count("<!-- AGENT-EVOLUTION:KET-THUC -->"), 1)
        self.assertIn("Agent Evolution", text)
        self.assertEqual(rd(sentinel), '{"giu": true}\n')
        self.assertFalse(os.path.exists(os.path.join(claude, "settings.vi-du.json")))
        self.assertTrue(os.path.isfile(os.path.join(claude, "agents", "agent-evolution.md")))
        self.assertTrue(os.path.isfile(os.path.join(claude, "skills", "agent-evolution", "SKILL.md")))
        self.assertEqual(rd(os.path.join(dest, "nguon.txt")).strip(), ROOT)
        self.assertTrue(os.path.isfile(os.path.join(dest, "ledger.py")))
        self.assertIn("name: agent-evolution", rd(os.path.join(claude, "agents", "agent-evolution.md")))
        self.assertIn("*.db", rd(os.path.join(dest, ".gitignore")))
        self.assertIn("bao-cao/", rd(os.path.join(dest, ".gitignore")))

        con = sqlite3.connect(os.path.join(dest, "ledger.db"))
        n = con.execute("SELECT COUNT(*) FROM lessons").fetchone()[0]
        con.close()
        self.assertEqual(n, 0)

        hook = os.path.join(dest, "ghi-nhap-phien.py")
        payload = json.dumps({"session_id": "gia-lap-001", "hook_event_name": "Stop"})
        for _ in range(2):
            proc = subprocess.run([sys.executable, hook], input=payload, capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        con = sqlite3.connect(os.path.join(dest, "ledger.db"))
        rows = con.execute("SELECT tier, sensitivity, title FROM lessons").fetchall()
        con.close()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], "scratch")
        self.assertEqual(rows[0][1], "user")
        self.assertNotIn("@", rows[0][2])

        proc = subprocess.run([sys.executable, hook], input="", capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        con = sqlite3.connect(os.path.join(dest, "ledger.db"))
        n = con.execute("SELECT COUNT(*) FROM lessons").fetchone()[0]
        con.close()
        self.assertEqual(n, 1)

    def test_kiem_nghiem(self):
        proc = subprocess.run(
            [sys.executable, CHAM, "kiem", "--repo", SKILL_DIR, "--nghiem"],
            capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("0 lỗi", proc.stdout)
        self.assertIn("0 cảnh báo", proc.stdout)

    def test_so_dang_ky(self):
        import yaml
        raw = rd(os.path.join(ROOT, "danh-muc", "skills.yaml"))
        data = yaml.safe_load(raw)
        names = [s["ten"] for s in data["skills"]]
        self.assertEqual(names.count("agent-evolution"), 1)
        self.assertEqual(data["tong_skill"], len(names))
        self.assertNotIn("tu-tien-hoa", raw)
        skill = next(s for s in data["skills"] if s["ten"] == "agent-evolution")
        self.assertEqual(skill["duong_dan"], "vong-lap/agent-evolution")
        self.assertEqual(skill["nen_tang"], ["claude-code"])
        self.assertLessEqual(len(skill["mo_ta_ngan"]), 120)
        self.assertTrue(skill["co_eval"])
        self.assertGreaterEqual(skill["so_tinh_huong"], 3)
        agent = rd(os.path.join(ROOT, ".claude", "agents", "agent-evolution.md"))
        self.assertIn("name: agent-evolution", agent)
        self.assertIn("Agent Evolution", agent)
        self.assertNotIn("tu-tien-hoa", agent)


if __name__ == "__main__":
    unittest.main(verbosity=2)
