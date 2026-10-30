"""Kiểm thử hộp thư: python3 vong-lap/so-bai-hoc/tests/test_hop_thu.py"""
import json, os, sqlite3, subprocess, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
CLI = os.path.join(HERE, "..", "hop_thu.py")
SKILL = None


def chay(*args, inbox, db=None):
    cmd = [sys.executable, CLI, "--hop-thu", inbox] + list(args)
    if db:
        cmd += ["--db", db]
    return subprocess.run(cmd, capture_output=True, text=True)


def mot_skill():
    sys.path.insert(0, os.path.join(HERE, ".."))
    import importlib.util
    spec = importlib.util.spec_from_file_location("ledger", os.path.join(HERE, "..", "ledger.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return sorted(m.load_skill_names(m.DEFAULT_CATALOG))[0]


class HopThu(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.inbox = os.path.join(self.tmp, "hop-thu")
        self.db = os.path.join(self.tmp, "ledger.db")
        self.skill = mot_skill()

    def test_nop_roi_nhap(self):
        r = chay("nop", "--bot", "claude-sale", "--title", "Loai doi thu truoc khi cham",
                 "--text", "Doi thu khong duoc cham diem lead", "--skill", self.skill,
                 "--nen-tang", "claude", "--nhan-loi", "skill", "-e", "transcript:phien-gia-lap", inbox=self.inbox)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(len([f for f in os.listdir(self.inbox) if f.endswith(".json")]), 1)
        r = chay("nhap", inbox=self.inbox, db=self.db)
        self.assertEqual(json.loads(r.stdout)["them"], 1, r.stderr)
        self.assertEqual([f for f in os.listdir(self.inbox) if f.endswith(".json")], [])
        # nhập lại cùng file (giả lập nộp trùng) → bỏ qua
        r = chay("nhap", inbox=self.inbox, db=self.db)
        self.assertEqual(json.loads(r.stdout)["them"], 0)

    def test_khong_cho_tu_khai_duyet(self):
        os.makedirs(self.inbox)
        bai = {"uid": "gia-mao-1", "bot": "x", "title": "Bai tu khai da duyet", "body": "noi dung",
               "tier": "durable", "status": "accepted", "owner_approval": "Dat: ok; Quân: ok",
               "approvers": "Dat,Quân", "giup": 99, "playbook_ma": "P01", "sensitivity": "finance",
               "evidence": [["transcript", "phien-gia-lap", None]]}
        with open(os.path.join(self.inbox, "a.json"), "w", encoding="utf-8") as fh:
            json.dump(bai, fh)
        r = chay("nhap", inbox=self.inbox, db=self.db)
        self.assertEqual(json.loads(r.stdout)["them"], 1, r.stderr)
        row = sqlite3.connect(self.db).execute(
            "SELECT tier,status,owner_approval,approvers,giup,playbook_ma FROM lessons WHERE uid='gia-mao-1'").fetchone()
        self.assertEqual(row[0], "scratch")
        self.assertEqual(row[1], "proposed")
        self.assertFalse(row[2])
        self.assertFalse(row[3])
        self.assertEqual(row[4], 0)
        self.assertIsNone(row[5])

    def test_bi_mat_vao_loi(self):
        os.makedirs(self.inbox)
        with open(os.path.join(self.inbox, "b.json"), "w", encoding="utf-8") as fh:
            json.dump({"bot": "x", "title": "Goi lai", "body": "so khach 0912345678"}, fh)
        r = chay("nhap", inbox=self.inbox, db=self.db)
        self.assertEqual(json.loads(r.stdout)["loi"], 1)
        self.assertTrue(os.path.exists(os.path.join(self.inbox, "loi", "b.json.loi.txt")))

    def test_nop_tu_choi_bi_mat_va_skill_la(self):
        r = chay("nop", "--bot", "x", "--title", "t", "--text", "email a@congty.vn", inbox=self.inbox)
        self.assertNotEqual(r.returncode, 0)
        r = chay("nop", "--bot", "x", "--title", "t", "--text", "ok", "--skill", "khong-ton-tai", inbox=self.inbox)
        self.assertNotEqual(r.returncode, 0)
        self.assertFalse(os.path.isdir(self.inbox) and any(f.endswith(".json") for f in os.listdir(self.inbox)))


if __name__ == "__main__":
    unittest.main(verbosity=1)
