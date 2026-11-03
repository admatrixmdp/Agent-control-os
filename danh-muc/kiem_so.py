"""Kiểm sổ danh-muc/skills.yaml (schema 1 và 2), không cần mạng.

    python3 danh-muc/kiem_so.py                    # kiểm sổ hiện tại
    python3 danh-muc/kiem_so.py --base origin/harness-v1   # thêm: SKILL.md đổi trong PR phải có sha256 khớp
"""
import argparse
import hashlib
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml

GOC = Path(__file__).resolve().parent.parent
REPO_NAY = "admatrixmdp/Agent-control-os"
BAT_BUOC = ["ten", "repo", "duong_dan", "mang", "mo_ta_ngan", "ngon_ngu", "nen_tang",
            "co_eval", "so_tinh_huong", "trang_thai", "trung_voi", "ghi_chu"]
MANG = {"sale", "marketing", "quang-cao", "tai-chinh", "ke-toan", "dau-tu", "quan-tri",
        "phap-ly", "san-pham", "web", "thuong-mai-dien-tu", "khac"}
TRANG_THAI = {"dang-dung", "dong-bang", "loai", "thu-nghiem"}
CTO_VERDICT = {"chua-duyet", "dat", "truot"}
TRUONG_2 = ["nguon", "phien_ban", "sha256", "eval_bay", "cto_verdict"]
BAT_BUOC_REPO_NAY = ["sha256", "cto_verdict"]  # phải ghi ngay trong mục, không lấy mặc định
BO_QUA = ("skill-lab/", "may-cham/tests/mau/")  # SKILL.md mẫu hoặc đang cách ly, không đăng ký sổ


def sha256(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def kiem_so(so, loi, canh_bao):
    ds = so.get("skills") or []
    schema = so.get("schema", 1)
    if schema not in (1, 2):
        loi.append(f"schema={schema!r}: chỉ nhận 1 hoặc 2")
    mac_dinh = so.get("mac_dinh") or {}
    for k in set(mac_dinh) - set(TRUONG_2) | ({"sha256"} & set(mac_dinh)):
        loi.append(f"mac_dinh.{k}: không được đặt mặc định")
    da_thay, thieu_ngoai = set(), Counter()
    for i, goc in enumerate(ds):
        s = {**mac_dinh, **goc}
        ma = f"skills[{i}] {s.get('ten', '?')}"
        for k in BAT_BUOC:
            if k not in s:
                loi.append(f"{ma}: thiếu trường {k}")
        if (s.get("repo"), s.get("ten")) in da_thay:
            loi.append(f"{ma}: trùng (repo, ten)")
        da_thay.add((s.get("repo"), s.get("ten")))
        if s.get("mang") not in MANG:
            loi.append(f"{ma}: mang={s.get('mang')!r} không hợp lệ")
        if s.get("trang_thai") not in TRANG_THAI:
            loi.append(f"{ma}: trang_thai={s.get('trang_thai')!r} không hợp lệ")
        if s.get("ngon_ngu") not in ("vi", "en"):
            loi.append(f"{ma}: ngon_ngu phải là vi hoặc en")
        # Trường schema 2: không bắt buộc với mục cũ, có thì phải đúng kiểu
        if "nguon" in s and not (isinstance(s["nguon"], str) and s["nguon"].strip()):
            loi.append(f"{ma}: nguon phải là chuỗi không rỗng")
        if "phien_ban" in s and not re.fullmatch(r"\d+\.\d+(\.\d+)?", str(s["phien_ban"])):
            loi.append(f"{ma}: phien_ban phải dạng 1.0 hoặc 1.0.0")
        if "sha256" in s and not re.fullmatch(r"[0-9a-f]{64}", str(s["sha256"])):
            loi.append(f"{ma}: sha256 phải là 64 ký tự hex thường")
        if "eval_bay" in s and not (isinstance(s["eval_bay"], int) and 0 <= s["eval_bay"] <= (s.get("so_tinh_huong") or 0)):
            loi.append(f"{ma}: eval_bay phải là số nguyên từ 0 tới so_tinh_huong")
        if "cto_verdict" in s and s["cto_verdict"] not in CTO_VERDICT:
            loi.append(f"{ma}: cto_verdict phải là một trong {sorted(CTO_VERDICT)}")
        if s.get("repo") == REPO_NAY:
            for k in BAT_BUOC_REPO_NAY:
                if k not in goc:
                    loi.append(f"{ma}: skill trong repo này phải ghi {k} trong mục (schema 2)")
            f = GOC / str(s.get("duong_dan", "")) / "SKILL.md"
            if not f.is_file():
                loi.append(f"{ma}: không thấy {f.relative_to(GOC)}")
            elif "sha256" in s and sha256(f) != s["sha256"]:
                loi.append(f"{ma}: sha256 trong sổ không khớp {f.relative_to(GOC)} (thực tế {sha256(f)})")
        else:
            thieu_ngoai.update(k for k in TRUONG_2 if k not in s)
    for k, n in sorted(thieu_ngoai.items()):
        canh_bao.append(f"{n} mục repo ngoài chưa có {k} (không chặn)")
    # Số tổng ở đầu file
    if so.get("tong_skill") != len(ds):
        loi.append(f"tong_skill={so.get('tong_skill')} nhưng sổ có {len(ds)} mục")
    dem = Counter(s.get("repo") for s in ds)
    if dict(dem) != (so.get("theo_repo") or {}):
        loi.append(f"theo_repo lệch số đếm thật: {dict(dem)}")
    co = sum(1 for s in ds if s.get("co_eval") is True)
    if so.get("co_eval") != co or so.get("chua_eval") != len(ds) - co:
        loi.append(f"co_eval/chua_eval lệch: thật là {co}/{len(ds) - co}")
    return ds


def kiem_thay_doi(ds, base, loi):
    """SKILL.md nào đổi so với base cũng phải có mục trong sổ kèm sha256 (đã kiểm khớp ở trên)."""
    ra = subprocess.run(["git", "diff", "--name-only", "--diff-filter=AMR", f"{base}...HEAD"],
                        cwd=GOC, capture_output=True, text=True, check=True).stdout.split()
    co_sha = {str(s.get("duong_dan")).rstrip("/") for s in ds if s.get("repo") == REPO_NAY and "sha256" in s}
    for p in ra:
        if p.endswith("SKILL.md") and not p.startswith(BO_QUA) and str(Path(p).parent) not in co_sha:
            loi.append(f"{p} đổi trong PR nhưng sổ không có mục repo {REPO_NAY} kèm sha256 cho nó")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--so", default=str(GOC / "danh-muc/skills.yaml"))
    ap.add_argument("--base", help="git ref để so SKILL.md thay đổi (dùng trong CI)")
    a = ap.parse_args()
    so = yaml.safe_load(Path(a.so).read_text(encoding="utf-8"))
    loi, canh_bao = [], []
    ds = kiem_so(so, loi, canh_bao)
    if a.base:
        kiem_thay_doi(ds, a.base, loi)
    for x in canh_bao:
        print("CẢNH BÁO  " + x)
    for x in loi:
        print("LỖI  " + x)
    print(f"{len(ds)} mục, schema {so.get('schema', 1)}: " + ("sổ đạt" if not loi else f"{len(loi)} lỗi"))
    return 1 if loi else 0


if __name__ == "__main__":
    sys.exit(main())
