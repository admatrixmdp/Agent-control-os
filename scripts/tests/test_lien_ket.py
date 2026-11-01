#!/usr/bin/env python3
"""Kiểm thử lien_ket_skill.py: tạo liên kết, chạy lại không đổi, không đè bản riêng, báo chênh, bỏ qua plugin."""
import contextlib, importlib.util, io, os, sys, tempfile

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("lk", os.path.join(HERE, "..", "lien_ket_skill.py"))
lk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lk)


def dung_moi_truong():
    t = tempfile.mkdtemp()
    goc = os.path.join(t, "repos")
    for repo, ten in (("sale-os", "chot-sale"), ("sale-os", "dam-phan"), ("mkt-os", "viet-bai")):
        d = os.path.join(goc, repo, "skills", ten)
        os.makedirs(d)
        open(os.path.join(d, "SKILL.md"), "w", encoding="utf-8").write("---\nname: %s\n---\nBước 1\n" % ten)
    so = {
        "cach_cai_mac_dinh": "lien-ket",
        "cach_cai_theo_repo": {"x/mkt-os": {"claude-code": "plugin"}},
        "skills": [
            {"ten": "chot-sale", "repo": "x/sale-os", "duong_dan": "skills/chot-sale", "mang": "sale"},
            {"ten": "dam-phan", "repo": "x/sale-os", "duong_dan": "skills/dam-phan", "mang": "sale"},
            {"ten": "viet-bai", "repo": "x/mkt-os", "duong_dan": "skills/viet-bai", "mang": "marketing"},
            {"ten": "chua-clone", "repo": "x/khong-co", "duong_dan": "skills/a", "mang": "sale"},
        ],
    }
    cfg = {"cong_cu": {"claude-code": {"du_an": ".claude/skills", "may": os.path.join(t, "home", ".claude", "skills")},
                       "codex": {"du_an": ".agents/skills", "may": os.path.join(t, "home", ".agents", "skills")}}}
    p_so, p_cfg = os.path.join(t, "so.yaml"), os.path.join(t, "cfg.yaml")
    yaml.safe_dump(so, open(p_so, "w", encoding="utf-8"), allow_unicode=True)
    yaml.safe_dump(cfg, open(p_cfg, "w", encoding="utf-8"))
    return t, goc, p_so, p_cfg


def chay(*a):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        lk.main(list(a))
    return out.getvalue()


def bang(goc, p_so, p_cfg, cc="claude-code"):
    class A: pass
    a = A()
    a.so, a.thu_muc, a.goc, a.cong_cu, a.noi, a.dich = p_so, p_cfg, goc, cc, "may", None
    a.mang = a.skill = a.repo = None
    return {h["skill"]: h["trang_thai"] for h in lk.lap_bang(a)}


def test_tao_va_chay_lai():
    t, goc, so, cfg = dung_moi_truong()
    chay("--so", so, "--thu-muc", cfg, "lien-ket", "--goc", goc)  # chưa --ap-dung: không đổi gì
    assert bang(goc, so, cfg)["chot-sale"] == "chua-co"
    chay("--so", so, "--thu-muc", cfg, "lien-ket", "--goc", goc, "--ap-dung")
    b = bang(goc, so, cfg)
    assert b == {"chot-sale": "dung", "dam-phan": "dung", "viet-bai": "plugin", "chua-clone": "thieu-nguon"}, b
    chay("--so", so, "--thu-muc", cfg, "lien-ket", "--goc", goc, "--ap-dung")  # chạy lại: vẫn đúng
    assert bang(goc, so, cfg) == b
    # Sửa bản gốc thì công cụ thấy ngay
    f = os.path.join(goc, "sale-os", "skills", "chot-sale", "SKILL.md")
    open(f, "a", encoding="utf-8").write("Bước 2\n")
    d = os.path.join(os.path.dirname(cfg), "home", ".claude", "skills", "chot-sale", "SKILL.md")
    assert "Bước 2" in open(d, encoding="utf-8").read()


def test_khong_de_ban_rieng_va_bao_chenh():
    t, goc, so, cfg = dung_moi_truong()
    rieng = os.path.join(t, "home", ".agents", "skills", "chot-sale")
    os.makedirs(rieng)
    open(os.path.join(rieng, "SKILL.md"), "w", encoding="utf-8").write(
        "---\nname: chot-sale\n---\nBước 1\nHỏi khách chê đắt: so với cái gì?\n")
    open(os.path.join(rieng, "ghi-chu.md"), "w", encoding="utf-8").write("x\n")
    chay("--so", so, "--thu-muc", cfg, "lien-ket", "--goc", goc, "--cong-cu", "codex", "--ap-dung")
    assert bang(goc, so, cfg, "codex")["chot-sale"] == "ban-rieng"
    assert not os.path.islink(rieng)
    assert "chê đắt" in open(os.path.join(rieng, "SKILL.md"), encoding="utf-8").read()
    out = chay("--so", so, "--thu-muc", cfg, "chenh", "--goc", goc, "--cong-cu", "codex", "--skill", "chot-sale")
    assert "+Hỏi khách chê đắt" in out and "ghi-chu.md" in out, out


def test_lien_ket_lech_khong_sua():
    t, goc, so, cfg = dung_moi_truong()
    d = os.path.join(t, "home", ".claude", "skills")
    os.makedirs(d)
    os.symlink(os.path.join(goc, "sale-os", "skills", "dam-phan"), os.path.join(d, "chot-sale"))
    chay("--so", so, "--thu-muc", cfg, "lien-ket", "--goc", goc, "--ap-dung")
    assert bang(goc, so, cfg)["chot-sale"] == "lech"
    assert os.path.realpath(os.path.join(d, "chot-sale")).endswith("dam-phan")


def test_trung_ten_thi_dung():
    t, goc, so, cfg = dung_moi_truong()
    s = yaml.safe_load(open(so, encoding="utf-8"))
    s["skills"].append({"ten": "chot-sale", "repo": "x/mkt-os", "duong_dan": "skills/viet-bai", "mang": "sale"})
    yaml.safe_dump(s, open(so, "w", encoding="utf-8"), allow_unicode=True)
    try:
        chay("--so", so, "--thu-muc", cfg, "kiem", "--goc", goc)
    except SystemExit as e:
        assert "trùng tên" in str(e)
        s["skills"][-1]["ten_lien_ket"] = "chot-sale-2"
        yaml.safe_dump(s, open(so, "w", encoding="utf-8"), allow_unicode=True)
        chay("--so", so, "--thu-muc", cfg, "kiem", "--goc", goc)  # có ten_lien_ket thì qua
    else:
        raise AssertionError("phải dừng khi trùng tên")


def test_so_that_doc_duoc():
    s = yaml.safe_load(open(lk.SO_SKILL, encoding="utf-8"))
    lk.chon_skill(s)  # sổ thật không trùng tên
    cfg = yaml.safe_load(open(lk.THU_MUC, encoding="utf-8"))
    assert {"claude-code", "codex", "cursor"} <= set(cfg["cong_cu"])


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for f in tests:
        f()
        print("đạt", f.__name__)
    print("%d/%d đạt" % (len(tests), len(tests)))
