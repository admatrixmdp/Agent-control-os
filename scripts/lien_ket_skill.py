#!/usr/bin/env python3
"""Một skill, nhiều công cụ cùng đọc: liên kết skill từ repo gốc vào thư mục skill của từng công cụ.

Bản gốc duy nhất là thư mục skill trong repo *-os (đăng ký ở danh-muc/skills.yaml).
Script chỉ tạo liên kết (symlink; trên Windows không có quyền symlink thì dùng junction).
Script KHÔNG chép, KHÔNG xoá, KHÔNG gom thư mục có sẵn, KHÔNG đè bản ai đã sửa tại máy.

  # Xem trạng thái, không đổi gì
  python3 scripts/lien_ket_skill.py kiem --goc ~/repos --cong-cu claude-code,codex --noi may --mang sale
  # Tạo liên kết (mặc định chỉ in kế hoạch; thêm --ap-dung mới làm)
  python3 scripts/lien_ket_skill.py lien-ket --goc ~/repos --cong-cu codex --noi du-an --dich ~/du-an-x --ap-dung
  # Bản riêng tại máy khác bản gốc chỗ nào → dán vào bài học gửi hộp thư
  python3 scripts/lien_ket_skill.py chenh --goc ~/repos --cong-cu claude-code --noi may --skill 09-chot-sale

--goc: thư mục chứa các repo đã clone, mỗi repo một thư mục đặt theo tên repo (vd ~/repos/sale-suite-os).
Mặc định lấy $MQ_REPOS.

Trạng thái mỗi cặp (công cụ, skill):
  chua-co      chưa có gì ở đích → lien-ket sẽ tạo
  dung         liên kết trỏ đúng bản gốc
  lech         liên kết trỏ chỗ khác → báo, không sửa
  ban-rieng    thư mục thật (bản chép hoặc đã sửa) → giữ nguyên; dùng `chenh` để lấy phần khác
  thieu-nguon  chưa clone repo hoặc sai đường dẫn trong sổ
  plugin       repo này cài vào công cụ bằng plugin → bỏ qua để không hiện hai bản
"""
import argparse, difflib, json, os, sys

try:
    import yaml
except ImportError:
    sys.exit("cần pyyaml: pip install pyyaml")

GOC_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SO_SKILL = os.path.join(GOC_REPO, "danh-muc", "skills.yaml")
THU_MUC = os.path.join(GOC_REPO, "nen-tang", "thu-muc-skill.yaml")


def doc_yaml(p):
    with open(p, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def ten_thu_muc(s):
    """Tên thư mục ở đích. Hai repo cùng tên skill (vd analyzer) thì sổ ghi ten_lien_ket khác nhau."""
    return s.get("ten_lien_ket") or s["ten"]


def chon_skill(so, mang=None, skill=None, repo=None):
    ds = so.get("skills") or []
    if mang:
        ds = [s for s in ds if s.get("mang") in mang]
    if skill:
        ds = [s for s in ds if s.get("ten") in skill]
    if repo:
        ds = [s for s in ds if s.get("repo") in repo or s.get("repo", "").split("/")[-1] in repo]
    ds = [s for s in ds if s.get("trang_thai", "dang-dung") in ("dang-dung", "thu-nghiem")]
    ten = [ten_thu_muc(s) for s in ds]
    trung = sorted({t for t in ten if ten.count(t) > 1})
    if trung:
        sys.exit("trùng tên thư mục liên kết giữa các repo; thêm ten_lien_ket trong sổ: " + ", ".join(trung))
    return ds


def cach_cai(so, repo, cong_cu):
    """Repo cài bằng plugin cho công cụ nào thì không liên kết thêm vào công cụ đó."""
    m = (so.get("cach_cai_theo_repo") or {}).get(repo) or {}
    return m.get(cong_cu, so.get("cach_cai_mac_dinh", "lien-ket"))


def thu_muc_dich(cfg, cong_cu, noi, dich):
    c = (cfg.get("cong_cu") or {}).get(cong_cu)
    if not c:
        sys.exit("công cụ lạ: %s (có: %s)" % (cong_cu, ", ".join(cfg.get("cong_cu") or {})))
    if noi == "may":
        return os.path.expanduser(c["may"])
    if not dich:
        sys.exit("--noi du-an cần --dich <thu-muc-du-an>")
    return os.path.join(os.path.abspath(os.path.expanduser(dich)), c["du_an"])


def la_lien_ket(p):
    if os.path.islink(p):
        return True
    isj = getattr(os.path, "isjunction", None)  # Python 3.12+
    return bool(isj and isj(p))


def trang_thai(nguon, dich, cach):
    if cach == "plugin":
        return "plugin"
    if not os.path.isfile(os.path.join(nguon, "SKILL.md")):
        return "thieu-nguon"
    if la_lien_ket(dich):
        return "dung" if os.path.realpath(dich) == os.path.realpath(nguon) else "lech"
    if os.path.exists(dich):
        return "ban-rieng"
    return "chua-co"


def tao_lien_ket(nguon, dich):
    os.makedirs(os.path.dirname(dich), exist_ok=True)
    try:
        os.symlink(nguon, dich, target_is_directory=True)
        return "symlink"
    except OSError:
        if os.name != "nt":
            raise
        import _winapi  # Windows không bật Developer Mode: junction không cần quyền quản trị
        _winapi.CreateJunction(nguon, dich)
        return "junction"


def lap_bang(args):
    so, cfg = doc_yaml(args.so), doc_yaml(args.thu_muc)
    goc = os.path.abspath(os.path.expanduser(args.goc or os.environ.get("MQ_REPOS") or ""))
    if not args.goc and not os.environ.get("MQ_REPOS"):
        sys.exit("thiếu --goc (hoặc $MQ_REPOS): thư mục chứa các repo đã clone")
    hang = []
    for cc in [x.strip() for x in args.cong_cu.split(",") if x.strip()]:
        td = thu_muc_dich(cfg, cc, args.noi, args.dich)
        for s in chon_skill(so, args.mang, args.skill, args.repo):
            nguon = os.path.join(goc, s["repo"].split("/")[-1], s["duong_dan"])
            dich = os.path.join(td, ten_thu_muc(s))
            hang.append({"cong_cu": cc, "skill": s["ten"], "repo": s["repo"], "nguon": nguon, "dich": dich,
                         "trang_thai": trang_thai(nguon, dich, cach_cai(so, s["repo"], cc))})
    return hang


def in_bang(hang, as_json):
    if as_json:
        print(json.dumps(hang, ensure_ascii=False, indent=1))
        return
    dem = {}
    for h in hang:
        dem[h["trang_thai"]] = dem.get(h["trang_thai"], 0) + 1
        if h["trang_thai"] != "dung":
            print("%-11s %-12s %-32s %s" % (h["trang_thai"], h["cong_cu"], h["skill"], h["dich"]))
    print("Tổng: " + ", ".join("%s %d" % kv for kv in sorted(dem.items())))
    if dem.get("ban-rieng"):
        print("Có bản riêng tại máy: giữ nguyên. Chạy `chenh --skill <ten>` rồi nộp phần khác vào hộp thư bài học.")


def kiem(args):
    in_bang(lap_bang(args), args.json)
    return 0


def lien_ket(args):
    hang = lap_bang(args)
    lam = [h for h in hang if h["trang_thai"] == "chua-co"]
    for h in lam:
        if args.ap_dung:
            h["kieu"] = tao_lien_ket(h["nguon"], h["dich"])
            h["trang_thai"] = "dung"
        else:
            print("sẽ tạo  %-12s %-32s → %s" % (h["cong_cu"], h["skill"], h["nguon"]))
    in_bang(hang, args.json)
    if lam and not args.ap_dung:
        print("Chưa đổi gì. Thêm --ap-dung để tạo %d liên kết." % len(lam))
    return 0


def chenh(args):
    if not args.skill:
        sys.exit("chenh cần --skill")
    co = False
    for h in lap_bang(args):
        if h["trang_thai"] != "ban-rieng":
            continue
        for goc_dir, _, files in os.walk(h["nguon"]):
            for f in sorted(files):
                a = os.path.join(goc_dir, f)
                b = os.path.join(h["dich"], os.path.relpath(a, h["nguon"]))
                try:
                    ta = open(a, encoding="utf-8").read().splitlines(True)
                    tb = open(b, encoding="utf-8").read().splitlines(True) if os.path.exists(b) else []
                except UnicodeDecodeError:
                    continue
                d = list(difflib.unified_diff(ta, tb, "goc/" + os.path.relpath(a, h["nguon"]),
                                              "may/" + os.path.relpath(a, h["nguon"])))
                if d:
                    co = True
                    sys.stdout.writelines(d)
        for may_dir, _, files in os.walk(h["dich"]):
            for f in sorted(files):
                b = os.path.join(may_dir, f)
                rel = os.path.relpath(b, h["dich"])
                if not os.path.exists(os.path.join(h["nguon"], rel)):
                    co = True
                    print("+++ file chỉ có ở máy: %s" % rel)
    if not co:
        print("Không có bản riêng khác bản gốc.")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description="Liên kết skill từ repo gốc vào thư mục skill của công cụ")
    p.add_argument("--so", default=SO_SKILL, help="sổ skill (mặc định danh-muc/skills.yaml)")
    p.add_argument("--thu-muc", default=THU_MUC, help="bảng thư mục công cụ")
    sp = p.add_subparsers(dest="lenh", required=True)
    for ten, ham in (("kiem", kiem), ("lien-ket", lien_ket), ("chenh", chenh)):
        a = sp.add_parser(ten)
        a.add_argument("--goc")
        a.add_argument("--cong-cu", default="claude-code")
        a.add_argument("--noi", choices=["may", "du-an"], default="may")
        a.add_argument("--dich")
        a.add_argument("--mang", type=lambda s: s.split(","))
        a.add_argument("--skill", type=lambda s: s.split(","))
        a.add_argument("--repo", type=lambda s: s.split(","))
        a.add_argument("--json", action="store_true")
        if ten == "lien-ket":
            a.add_argument("--ap-dung", action="store_true", help="thật sự tạo liên kết")
        a.set_defaults(ham=ham)
    args = p.parse_args(argv)
    return args.ham(args)


if __name__ == "__main__":
    sys.exit(main())
