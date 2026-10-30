#!/usr/bin/env python3
"""Kiểm thử sổ bài học trên DB tạm. Không đụng ledger.db thật. Chỉ dữ liệu giả."""
import json, os, subprocess, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
CLI = os.path.join(os.path.dirname(HERE), "ledger.py")
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CHAM = os.path.join(ROOT, "may-cham", "cham.py")
SKILL = "00-ke-hoach-mkt"


def rd(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


class T(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.db = os.path.join(self.tmp.name, "test.db")
        self.root = self.tmp.name

    def run_cli(self, *a, ok=True, stdin=None):
        p = subprocess.run(
            [sys.executable, CLI, "--db", self.db, "--root", self.root, "--actor", "test-bot", *a],
            capture_output=True, text=True, input=stdin)
        if ok:
            self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        else:
            self.assertNotEqual(p.returncode, 0, p.stdout)
        return p

    def j(self, *a):
        return json.loads(self.run_cli("--json", *a).stdout)

    def test_seed_flow(self):
        a = self.j(
            "add", "--bot", "grok-a", "--skill", SKILL, "--repo", "admatrixmdp/marketing-business-skill",
            "--nen-tang", "goclaw", "--nhan-loi", "skill", "--tenant", "gia-lap",
            "--title", "Không được gửi tin nhắn khi chưa hỏi chủ",
            "--text", "Trước khi gửi tin nhắn hay email thay mặt chủ, phải soạn nháp và đợi được duyệt. Đạt và Quân cùng duyệt.",
            "--tags", "giao-tiep,an-toan", "--confidence", "0.8", "--sensitivity", "user",
            "-e", "transcript:phien-gia-lap-001", "-e", "quote:hoi chu truoc khi gui")["id"]
        b = self.j(
            "add", "--bot", "grok-b", "--title", "Check FTS5 before relying on bm25",
            "--text", "Some sqlite builds lack FTS5; probe with a CREATE VIRTUAL TABLE first.",
            "--tags", "sqlite,tooling", "--confidence", "0.9",
            "-e", "file:./vong-lap/so-bai-hoc/ledger.py")["id"]
        c = self.j(
            "add", "--bot", "grok-b", "--title", "Timezone in reports",
            "--text", "Always convert timestamps to Asia/Ho_Chi_Minh before reporting.",
            "--tags", "reporting", "--confidence", "0.4")["id"]

        for q in ["gửi tin nhắn", "gui tin nhan", "duoc duyet", "được duyệt", "DAT"]:
            hits = self.j("search", q)
            self.assertTrue(hits and hits[0]["id"] == a, "query %r -> %r" % (q, [h["id"] for h in hits]))
        self.assertEqual([h["id"] for h in self.j("search", "fts5 bm25", "--bot", "grok-b")], [b])
        self.assertEqual(self.j("search", "fts5", "--bot", "grok-a"), [])
        self.assertEqual([h["id"] for h in self.j("search", "tin nhan", "--tag", "an-toan")], [a])
        self.assertEqual([h["id"] for h in self.j("search", "gui", "--skill", SKILL)], [a])
        self.assertEqual(self.j("search", "gui", "--skill", "01-lich-noi-dung"), [])

        self.assertIn("bằng chứng", self.run_cli("promote", str(c), ok=False).stderr)
        self.run_cli("add", "--bot", "x", "--title", "t", "--text", "noi dung gia lap", "--tier", "working", ok=False)
        self.run_cli("evidence", "add", str(c), "url:https://docs.python.org/3/library/zoneinfo.html", "--note", "tai lieu")
        self.assertEqual(len(self.j("evidence", "list", str(c))), 1)
        self.run_cli("promote", str(c))
        self.assertIn("0.6", self.run_cli("promote", str(c), ok=False).stderr)

        self.run_cli("promote", str(b))
        self.run_cli("promote", str(b))
        self.assertEqual(self.j("show", str(b))["tier"], "durable")
        self.assertEqual(self.j("show", str(b))["status"], "accepted")
        self.run_cli("promote", str(a))
        self.assertIn("Dat và Quân", self.run_cli("promote", str(a), ok=False).stderr)
        self.assertIn("Dat và Quân", self.run_cli(
            "promote", str(a), "--owner-approved", "Dat OK trong hop gia lap 2026-10-29", ok=False).stderr)
        self.assertEqual(self.j("show", str(a))["tier"], "working")
        self.run_cli(
            "promote", str(a),
            "--owner-approved", "Đạt đồng ý ngày 2026-10-29",
            "--owner-approved", "Quân đồng ý ngày 2026-10-29")
        shown = self.j("show", str(a))
        self.assertEqual(shown["tier"], "durable")
        self.assertEqual(shown["status"], "accepted")
        self.assertEqual(shown["approvers"], "Dat,Quân")
        self.assertIn("Đạt", shown["owner_approval"])
        self.assertIn("Quân", shown["owner_approval"])
        self.run_cli("demote", str(a))
        self.assertEqual(self.j("show", str(a))["tier"], "working")

        d = self.j(
            "add", "--bot", "grok-c", "--title", "Check FTS5 before relying on bm25 ranking",
            "--text", "Some sqlite builds lack FTS5; probe with CREATE VIRTUAL TABLE first.")["id"]
        rv = self.j("review", "--since", "1")
        self.assertTrue(any({x["a"], x["b"]} == {b, d} for x in rv["duplicates"]), rv["duplicates"])
        self.assertIn(c, [x["id"] for x in rv["low_confidence"]])
        self.assertIn(d, [x["id"] for x in rv["no_evidence"]])
        self.run_cli("retire", str(d), "--reason", "trung voi bai %d" % b)
        self.assertEqual([h["id"] for h in self.j("search", "ranking", "--status", "retired")], [d])

        self.run_cli("wiki", "build")
        page = rd(os.path.join(self.root, "wiki", "sqlite.md"))
        self.assertIn("Check FTS5", page)
        self.assertIn("[^%d-" % b, page)
        self.assertIn("ledger.py`", page)
        self.assertTrue(os.path.exists(os.path.join(self.root, "wiki", "giao-tiep.md")))
        self.assertNotIn("relying on bm25 ranking", page)

        self.run_cli(
            "skill", "propose", "safe-messaging", "--title", "Hoi truoc khi gui tin",
            "--problem", "Bot gui tin khi chua duoc duyet. Tinh huong gia lap.",
            "--lessons", str(a), "--query", "gửi email")
        pd = os.path.join(self.root, "proposals", "safe-messaging")
        self.assertTrue(os.path.isfile(os.path.join(pd, "PROPOSAL.md")))
        self.assertTrue(os.path.isfile(os.path.join(pd, "SKILL.md")))
        self.assertTrue(any(fn.endswith(".yaml") for fn in os.listdir(os.path.join(pd, "evals"))))
        self.assertIn("BẮT BUỘC", rd(os.path.join(pd, "PROPOSAL.md")))
        self.assertIn("Quân", rd(os.path.join(pd, "PROPOSAL.md")))
        ev = self.j("skill", "eval", "safe-messaging")
        self.assertTrue(ev["ok"], ev)
        self.assertGreaterEqual(len(ev["cases"]), 3)
        self.assertTrue(all(x["has_expected"] for x in ev["cases"]))
        self.assertTrue(any(x["loai"] == "bay" for x in ev["cases"]))

        csvp = os.path.join(self.root, "x.csv")
        self.run_cli("export-csv", csvp)
        db2 = os.path.join(self.root, "b.db")
        out = subprocess.run([sys.executable, CLI, "--db", db2, "import-csv", csvp], capture_output=True, text=True)
        self.assertIn("đã nhập 4", out.stdout, out.stderr)
        out = subprocess.run([sys.executable, CLI, "--db", db2, "--json", "search", "duoc"], capture_output=True, text=True)
        hit = json.loads(out.stdout)[0]
        self.assertEqual(len(hit["evidence"]), 2)
        self.assertEqual(hit["skill"], SKILL)
        self.assertEqual(hit["approvers"], "Dat,Quân")
        self.assertEqual(hit["nhan_loi"], "skill")
        self.assertEqual(hit["tenant"], "gia-lap")

        acts = [x["action"] for x in self.j("audit", "--limit", "200")]
        for k in ("add", "promote", "demote", "evidence_add", "retire", "wiki_build", "skill_propose", "skill_eval"):
            self.assertIn(k, acts)
        self.assertTrue(all(x["actor"] == "test-bot" for x in self.j("audit")))

    def test_fields_gate_and_secrets(self):
        self.assertIn("skills.yaml", self.run_cli(
            "add", "--bot", "b", "--title", "t", "--text", "noi dung gia lap", "--skill", "khong-co-skill-nay",
            ok=False).stderr)
        self.assertIn("nhan_loi", self.run_cli(
            "add", "--bot", "b", "--title", "t", "--text", "noi dung gia lap", "--nhan-loi", "sai-tang",
            ok=False).stderr)
        self.assertIn("nen_tang", self.run_cli(
            "add", "--bot", "b", "--title", "t", "--text", "noi dung gia lap", "--nen-tang", "khong-co",
            ok=False).stderr)
        self.run_cli(
            "add", "--bot", "b", "--title", "Len durable khi nhay", "--text", "Noi dung gia lap.",
            "--sensitivity", "finance", "--tier", "durable", "--confidence", "0.9",
            "-e", "transcript:phien-gia-lap-002", ok=False)

        lid = self.j(
            "add", "--bot", "b", "--title", "Can ca hai nguoi duyet",
            "--text", "Bai nhay gia lap, khong co du lieu khach.",
            "--sensitivity", "sensitive", "--confidence", "0.95", "--nhan-loi", "tri-thuc",
            "--nen-tang", "claude-code", "--tenant", "gia-lap",
            "-e", "transcript:phien-gia-lap-003",
            "--owner-approved", "Đạt đồng ý ngày 2026-10-29; Quân đồng ý ngày 2026-10-29")["id"]
        self.run_cli("promote", str(lid))
        self.run_cli("promote", str(lid))
        shown = self.j("show", str(lid))
        self.assertEqual(shown["tier"], "durable")
        self.assertEqual(shown["approvers"], "Dat,Quân")
        self.assertEqual(shown["nhan_loi"], "tri-thuc")
        self.assertEqual([x["id"] for x in self.j("list", "--nhan-loi", "tri-thuc")], [lid])

        email = "a" + "@" + "b.co"
        self.assertIn("bí mật", self.run_cli(
            "add", "--bot", "b", "--title", "chan lien he", "--text", "dung gui " + email, ok=False).stderr)
        phone = "09" + "87654321"
        self.assertIn("bí mật", self.run_cli(
            "add", "--bot", "b", "--title", "chan so", "--text", "so " + phone, ok=False).stderr)

    def test_playbook_append_only(self):
        sentinel = os.path.join(self.root, "SKILL.md")
        with open(sentinel, "w", encoding="utf-8") as fh:
            fh.write("# Goc\nKhong duoc viet lai.\n")
        before = rd(sentinel)

        def add_durable(title, conf, giup, hai):
            lid = self.j(
                "add", "--bot", "bot-gia-lap", "--title", title,
                "--text", "Quy tac gia lap, khong co du lieu khach.",
                "--skill", SKILL, "--repo", "admatrixmdp/marketing-business-skill",
                "--nen-tang", "goclaw", "--nhan-loi", "skill", "--tenant", "gia-lap",
                "--confidence", str(conf), "--giup", str(giup), "--hai", str(hai),
                "-e", "transcript:phien-gia-lap-004")["id"]
            self.run_cli("promote", str(lid))
            self.run_cli("promote", str(lid))
            return lid

        high = add_durable("Lay mot lan roi xu ly cuc bo", 0.9, 2, 1)
        low = add_durable("Khong suy doan o trong", 0.7, 0, 0)
        working = self.j(
            "add", "--bot", "bot-gia-lap", "--title", "Chua du ben",
            "--text", "Con o tang working.", "--skill", SKILL, "--confidence", "0.9",
            "-e", "transcript:phien-gia-lap-005")["id"]
        self.run_cli("promote", str(working))

        out = os.path.join(self.root, "playbook-xuat.md")
        self.run_cli("playbook", "export", "--skill", SKILL, "--out", sentinel, ok=False)
        self.assertEqual(rd(sentinel), before)
        self.run_cli("playbook", "export", "--skill", SKILL, "--lesson", str(working), "--out", out, ok=False)

        self.run_cli("playbook", "export", "--skill", SKILL, "--out", out)
        text = rd(out)
        self.assertIn("- [P01] Lay mot lan roi xu ly cuc bo (giúp: 2, hại: 1)\n", text)
        self.assertNotIn("Khong suy doan", text)
        self.assertEqual(self.j("show", str(high))["playbook_ma"], "P01")
        snap = text
        self.run_cli("playbook", "export", "--skill", SKILL, "--out", out)
        text = rd(out)
        self.assertTrue(text.startswith(snap))
        self.assertIn("- [P02] Khong suy doan o trong (giúp: 0, hại: 0)\n", text)
        self.assertEqual(self.j("show", str(low))["playbook_ma"], "P02")
        self.run_cli("playbook", "export", "--skill", SKILL, "--out", out, ok=False)
        self.assertEqual(rd(out), text)
        self.assertEqual(rd(sentinel), before)

        seeded = os.path.join(self.root, "playbook-cu.md")
        prefix = (
            "# Playbook — %s\n"
            "<!-- Chỉ thêm dòng mới. Không viết lại dòng cũ. Bộ đếm cập nhật sau mỗi lần chấm. -->\n"
            "- [P07] Dong cu giu nguyen. (giúp: 4, hại: 0)\n" % SKILL)
        with open(seeded, "w", encoding="utf-8") as fh:
            fh.write(prefix)
        extra = self.j(
            "add", "--bot", "bot-gia-lap", "--title", "Dong moi phia sau",
            "--text", "Bai durable thu ba.", "--skill", SKILL, "--confidence", "0.8",
            "-e", "transcript:phien-gia-lap-006")["id"]
        self.run_cli("promote", str(extra))
        self.run_cli("promote", str(extra))
        self.run_cli("playbook", "export", "--skill", SKILL, "--lesson", str(extra), "--out", seeded)
        got = rd(seeded)
        self.assertTrue(got.startswith(prefix))
        self.assertEqual(got.count("[P07]"), 1)
        self.assertIn("- [P08] Dong moi phia sau (giúp: 0, hại: 0)\n", got)

    def test_propose_passes_may_cham(self):
        ids = []
        for i, title in enumerate(("Ghi dau truoc khi ket luan", "Thieu nguon thi de trong"), 1):
            lid = self.j(
                "add", "--bot", "bot-gia-lap", "--skill", SKILL, "--nhan-loi", "skill",
                "--title", title, "--text", "Buoc gia lap so %d. Khong co du lieu khach." % i,
                "--confidence", "0.8", "-e", "transcript:phien-gia-lap-1%d" % i)["id"]
            ids.append(lid)
        self.run_cli(
            "skill", "propose", "on-ke-hoach", "--title", "On dinh ke hoach gia lap",
            "--problem", "Cung mot loi lap lai trong tinh huong gia lap.",
            "--lessons", ",".join(str(i) for i in ids))
        pd = os.path.join(self.root, "proposals", "on-ke-hoach")
        yamls = sorted(os.listdir(os.path.join(pd, "evals")))
        self.assertGreaterEqual(len(yamls), 3)
        self.assertTrue(any("bay" in fn for fn in yamls))
        p = subprocess.run([sys.executable, CHAM, "kiem", "--repo", pd, "--nghiem"], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertIn("0 lỗi", p.stdout)
        self.assertIn("0 cảnh báo", p.stdout)

    def test_wiki_hides_sensitive(self):
        lid = self.j(
            "add", "--bot", "b", "--title", "An bai sensitive",
            "--text", "Noi dung gia lap, khong dua len wiki cong khai.",
            "--tags", "bi-mat", "--sensitivity", "sensitive", "--confidence", "0.8",
            "-e", "transcript:phien-gia-lap-007")["id"]
        self.run_cli("promote", str(lid))
        self.run_cli("wiki", "build")
        self.assertFalse(os.path.exists(os.path.join(self.root, "wiki", "bi-mat.md")))
        self.assertIn("bị ẩn", rd(os.path.join(self.root, "wiki", "index.md")))
        self.run_cli("wiki", "build", "--include-sensitive")
        self.assertIn("An bai sensitive", rd(os.path.join(self.root, "wiki", "bi-mat.md")))

    def test_uid_khong_tao_trung(self):
        a = self.j(
            "add", "--bot", "agent-evolution", "--title", "Phien can ra",
            "--text", "Bai gia lap, khong co du lieu khach.",
            "--tier", "scratch", "--sensitivity", "user", "--uid", "phien-gia-lap-001",
            "-e", "transcript:phien-gia-lap-001")
        self.assertFalse(a["skipped"])
        b = self.j(
            "add", "--bot", "agent-evolution", "--title", "Tieu de khac",
            "--text", "Khong duoc ghi de.", "--uid", "phien-gia-lap-001")
        self.assertTrue(b["skipped"])
        self.assertEqual(a["id"], b["id"])
        self.assertEqual(len(self.j("list")), 1)
        self.assertEqual(self.j("show", str(a["id"]))["title"], "Phien can ra")

    def test_gitignore_blocks_runtime(self):
        text = rd(os.path.join(ROOT, ".gitignore"))
        for line in ("*.db", "*.db-wal", "*.db-shm",
                     "vong-lap/so-bai-hoc/wiki/",
                     "vong-lap/so-bai-hoc/staging/",
                     "vong-lap/so-bai-hoc/proposals/",
                     "vong-lap/so-bai-hoc/bao-cao/"):
            self.assertIn(line, text)


if __name__ == "__main__":
    real = os.path.join(os.path.dirname(HERE), "ledger.db")
    before = os.path.getsize(real) if os.path.exists(real) else None
    r = unittest.main(exit=False, verbosity=2).result
    after = os.path.getsize(real) if os.path.exists(real) else None
    assert before == after, "ledger.db thật bị đổi"
    print("ledger.db thật không đổi:", real if after is not None else "(không tạo)")
    sys.exit(0 if r.wasSuccessful() else 1)
