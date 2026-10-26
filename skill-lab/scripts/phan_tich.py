#!/usr/bin/env python3
"""Bước 1–3 của quy trình đối chiếu (doi-chieu/quy-trinh.md) cho kho skill-lab.

  1. Kiểm dịch: quét chỉ dẫn ẩn, lệnh nguy hiểm, khoá bí mật, đường dẫn cá nhân, dữ liệu cá nhân.
  2. Dấu vân tay: tên, phòng ban, mảng, trigger, định dạng đầu ra, các bước, độ dài.
  3. Ánh xạ: so với sổ đăng ký danh-muc/skills.yaml (TF-IDF ký tự, bỏ dấu) và so trùng nội bộ trong kho.

Chạy: python -I skill-lab/scripts/phan_tich.py   (từ gốc repo Agent-control-os)
Đầu ra: skill-lab/kiem-dich/, skill-lab/van-tay/, skill-lab/anh-xa/
Script chỉ đọc file văn bản, không chạy mã trong skill.
"""
from __future__ import annotations

import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

import yaml
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

GOC = Path(__file__).resolve().parents[2]
LAB = GOC / "skill-lab"
RAW = LAB / "raw"
SO_DANG_KY = GOC / "danh-muc" / "skills.yaml"

# ------------------------------------------------------------------ phân loại phòng ban → mảng

TIEN_TO_290 = {
    "ceo": "quan-tri", "mkt": "marketing", "sales": "sale", "fin": "tai-chinh", "hr": "nhan-su",
    "ops": "van-hanh", "cs": "cham-soc-khach-hang", "legal": "phap-ly", "it": "cong-nghe",
    "data": "cong-nghe", "proc": "mua-hang-kho-van", "log": "mua-hang-kho-van",
}
PHONG_UPDATE = {
    "bgd-skills": "quan-tri", "rd-skills": "san-pham", "logistics-skills": "mua-hang-kho-van",
    "marketing-skills": "marketing", "marketing": "thuong-mai-dien-tu", "admin-skills": "hanh-chinh",
    "cskh-skills": "cham-soc-khach-hang", "hr-skills": "nhan-su", "it-skills": "cong-nghe",
    "ke-toan-skills": "ke-toan", "muahang-skills": "mua-hang-kho-van", "phap-che-skills": "phap-ly",
    "pr-skills": "marketing", "sales-skills": "sale", "sanxuat-skills": "van-hanh",
    "taichinh-skills": "tai-chinh", "xnk-skills": "xuat-nhap-khau",
}
# mảng gần nhau trong sổ đăng ký nội bộ (để cộng điểm khi cùng họ)
HO_MANG = {
    "marketing": {"marketing", "quang-cao", "thuong-mai-dien-tu", "web"},
    "thuong-mai-dien-tu": {"marketing", "quang-cao", "thuong-mai-dien-tu"},
    "sale": {"sale"}, "tai-chinh": {"tai-chinh", "ke-toan", "dau-tu"}, "ke-toan": {"ke-toan", "tai-chinh"},
    "quan-tri": {"quan-tri", "dau-tu"}, "phap-ly": {"phap-ly"}, "san-pham": {"san-pham", "web"},
}

# ------------------------------------------------------------------ luật kiểm dịch

LUAT = [
    # (mức, mã, mẫu)
    ("chan", "chi-dan-an", r"ignore (all |any )?(previous|prior|above) (instructions|prompts)|bỏ qua (mọi|tất cả|các) (hướng dẫn|chỉ dẫn|quy tắc)|disregard (the )?(system|previous)|do not (tell|inform) the user|không (được )?(cho|để) người dùng biết|reveal (your|the) system prompt"),
    ("chan", "lenh-pha-huy", r"rm\s+-rf\s+[/~]|mkfs\.|dd\s+if=.*of=/dev/|:\(\)\s*\{\s*:\|:&\s*\};:|chmod\s+-R\s+777\s+/"),
    ("chan", "tai-va-chay", r"(curl|wget)[^\n|]*\|\s*(sudo\s+)?(ba|z)?sh\b"),
    ("chan", "khoa-bi-mat", r"sk-[A-Za-z0-9]{32,}|AKIA[0-9A-Z]{16}|EAA[A-Za-z0-9]{60,}|ghp_[A-Za-z0-9]{36}|xox[bpa]-[A-Za-z0-9-]{20,}|-----BEGIN (RSA |EC )?PRIVATE KEY"),
    ("canh-bao", "gui-du-lieu-ra-ngoai", r"(send|post|upload|gửi)[^\n]{0,60}(credential|password|mật khẩu|token|cookie)[^\n]{0,60}(http|webhook)"),
    ("canh-bao", "duong-dan-ca-nhan", r"/Users/[A-Za-z0-9_.-]+|C:\\\\Users\\\\[A-Za-z0-9_.-]+"),
    ("canh-bao", "so-dien-thoai", r"(?<![\d.])(?:\+?84|0)(?:3|5|7|8|9)\d{8}(?!\d)"),
    ("canh-bao", "email", r"[A-Za-z0-9._%+-]+@(?!example\.)[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    ("thong-tin", "chay-lenh-he-thong", r"os\.system\(|subprocess\.|exec\(|eval\("),
    ("thong-tin", "goi-api", r"requests\.(get|post)|fetch\(|axios\.|curl\s"),
]
LUAT_RE = [(m, c, re.compile(p, re.I)) for m, c, p in LUAT]
EMAIL_BO_QUA = {"noreply", "no-reply", "example", "your", "ten", "abc", "email", "user", "name"}


def bo_dau(s: str) -> str:
    s = unicodedata.normalize("NFD", s.replace("đ", "d").replace("Đ", "D"))
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower()


def doc_frontmatter(van_ban: str) -> tuple[dict, str, str | None]:
    if not van_ban.startswith("---"):
        return {}, van_ban, "không có frontmatter"
    phan = van_ban.split("---", 2)
    if len(phan) < 3:
        return {}, van_ban, "frontmatter không đóng"
    try:
        fm = yaml.safe_load(phan[1]) or {}
        return (fm if isinstance(fm, dict) else {}), phan[2], None
    except yaml.YAMLError as e:
        return {}, phan[2], f"frontmatter lỗi YAML: {str(e).splitlines()[0]}"


def lay_trigger(mo_ta: str) -> list[str]:
    return [t.strip() for t in re.findall(r"[\"“]([^\"”]{2,60})[\"”]", mo_ta)][:20]


def lay_dau_ra(mo_ta: str, than: str) -> list[str]:
    nguon = mo_ta + " " + " ".join(re.findall(r"(?im)^##.*output.*$\n(?:.*\n){0,8}", than))
    dang = []
    for ten, mau in [("markdown", r"markdown|\.md\b"), ("html", r"html"), ("excel", r"excel|xlsx|google sheet"),
                     ("pdf", r"\bpdf\b"), ("docx", r"docx|word\b"), ("pptx", r"pptx|slide|powerpoint"),
                     ("csv", r"\bcsv\b"), ("json", r"\bjson\b")]:
        if re.search(mau, nguon, re.I):
            dang.append(ten)
    return dang


def quet_skill(tep: Path) -> dict:
    van_ban = tep.read_text(encoding="utf-8", errors="replace")
    fm, than, loi_fm = doc_frontmatter(van_ban)
    thu_muc = tep.parent
    lo = "lo-290" if "lo-290" in tep.parts else "lo-update"
    if lo == "lo-290":
        phong = thu_muc.name.split("-")[0]
        mang = TIEN_TO_290.get(phong, "khac")
    else:
        phong = thu_muc.parent.name
        mang = PHONG_UPDATE.get(phong, "khac")
    ten = str(fm.get("name") or thu_muc.name)
    mo_ta = " ".join(str(fm.get("description") or "").split())

    co = []
    for muc, ma, re_ in LUAT_RE:
        khop = [m.group(0) for m in re_.finditer(van_ban)]
        if ma == "email":
            khop = [k for k in khop if k.split("@")[0].lower() not in EMAIL_BO_QUA]
        if khop:
            co.append({"muc": muc, "ma": ma, "so_lan": len(khop), "vi_du": sorted(set(khop))[:3]})
    van_de_dinh_dang = []
    if loi_fm:
        van_de_dinh_dang.append(loi_fm)
    if fm.get("name") and str(fm["name"]) != thu_muc.name:
        van_de_dinh_dang.append(f"name '{fm['name']}' khác tên thư mục '{thu_muc.name}'")
    if len(mo_ta) > 1024:
        van_de_dinh_dang.append(f"description {len(mo_ta)} ký tự > 1024")
    if not mo_ta:
        van_de_dinh_dang.append("thiếu description")
    muc_cao_nhat = "chan" if any(c["muc"] == "chan" for c in co) else ("canh-bao" if any(c["muc"] == "canh-bao" for c in co) else "sach")
    tep_kem = sorted(str(p.relative_to(thu_muc)) for p in thu_muc.rglob("*") if p.is_file() and p.name != "SKILL.md")
    tieu_de = [h.strip("# ").strip() for h in re.findall(r"(?m)^#{2}\s+.+$", than)][:15]
    tieu_de_chinh = next((h.strip("# ").strip() for h in re.findall(r"(?m)^#\s+.+$", than)), ten)
    return {
        "ten": ten,
        "lo": lo,
        "duong_dan": str(thu_muc.relative_to(LAB)),
        "phong_ban": phong,
        "mang": mang,
        "tieu_de": tieu_de_chinh,
        "mo_ta": mo_ta[:400],
        "trigger": lay_trigger(mo_ta),
        "dau_ra": lay_dau_ra(mo_ta, than),
        "cac_muc": tieu_de,
        "so_dong": van_ban.count("\n") + 1,
        "co_code_mau": "```python" in van_ban or "```js" in van_ban or "```bash" in van_ban,
        "tep_kem": tep_kem,
        "kiem_dich": {"ket_luan": muc_cao_nhat, "dau_hieu": co, "dinh_dang": van_de_dinh_dang},
        "_van_ban": f"{ten} {tieu_de_chinh} {mo_ta} {' '.join(tieu_de)}",
    }


# ------------------------------------------------------------------ ánh xạ

def anh_xa(ds: list[dict], noi_bo: list[dict]) -> None:
    vb_ngoai = [bo_dau(x["_van_ban"].replace("-", " ")) for x in ds]
    vb_noi = [bo_dau(f"{s['ten'].replace('-', ' ')} {s.get('mo_ta_ngan', '')} {s.get('mang', '')}") for s in noi_bo]
    vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), sublinear_tf=True, min_df=1)
    vec.fit(vb_ngoai + vb_noi)
    A, B = vec.transform(vb_ngoai), vec.transform(vb_noi)
    sim = cosine_similarity(A, B)
    for i, x in enumerate(ds):
        ho = HO_MANG.get(x["mang"], {x["mang"]})
        diem = []
        for j, s in enumerate(noi_bo):
            d = float(sim[i, j]) + (0.05 if s.get("mang") in ho else 0.0)
            diem.append((d, s))
        diem.sort(key=lambda t: -t[0])
        x["ung_vien_chu"] = [{"ten": s["ten"], "repo": s["repo"], "diem": round(d, 3)} for d, s in diem[:3]]
        x["nhan_de_xuat"] = "loai" if x["kiem_dich"]["ket_luan"] == "chan" else "cho-doc-nghia"
    # trùng nội bộ trong kho
    sim_trong = cosine_similarity(A)
    for i, x in enumerate(ds):
        cap = [(float(sim_trong[i, j]), ds[j]["ten"], ds[j]["lo"]) for j in range(len(ds)) if j != i and sim_trong[i, j] >= 0.55]
        cap.sort(reverse=True)
        x["trung_trong_kho"] = [{"ten": t, "lo": l, "diem": round(d, 3)} for d, t, l in cap[:3]]


# ------------------------------------------------------------------ xuất

def ghi_yaml(p: Path, du_lieu) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(yaml.safe_dump(du_lieu, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")


def main() -> int:
    tep = sorted(RAW.glob("lo-*/**/SKILL.md"))
    ds = [quet_skill(t) for t in tep]
    noi_bo = (yaml.safe_load(SO_DANG_KY.read_text(encoding="utf-8")) or {}).get("skills", [])
    if not noi_bo:
        print("Không đọc được sổ đăng ký", file=sys.stderr)
        return 1
    anh_xa(ds, noi_bo)
    for x in ds:
        x.pop("_van_ban")

    # 1. kiểm dịch
    kd = [{"ten": x["ten"], "duong_dan": x["duong_dan"], **x["kiem_dich"]} for x in ds if x["kiem_dich"]["ket_luan"] != "sach" or x["kiem_dich"]["dinh_dang"]]
    ghi_yaml(LAB / "kiem-dich" / "ket-qua.yaml", {"tong": len(ds), "co_van_de": len(kd), "skills": kd})
    # 2. vân tay (đủ trường, không gồm ánh xạ)
    ghi_yaml(LAB / "van-tay" / "van-tay.yaml", {"tong": len(ds), "skills": [{k: v for k, v in x.items() if k not in ("ung_vien_chu", "nhan_de_xuat", "trung_trong_kho", "kiem_dich")} for x in ds]})
    # 3. ánh xạ
    ghi_yaml(LAB / "anh-xa" / "anh-xa.yaml", {"tong": len(ds), "ghi_chu": "ung_vien_chu = ứng viên thô theo độ giống chữ (TF-IDF ký tự, bỏ dấu); điểm thấp do lệch ngôn ngữ Anh/Việt nên không dùng để gắn nhãn. Nhãn theo nghĩa nằm ở anh-xa/theo-nghia/. Quân chốt nhãn cuối.", "skills": [{"ten": x["ten"], "lo": x["lo"], "mang": x["mang"], "nhan_de_xuat": x["nhan_de_xuat"], "ung_vien_chu": x["ung_vien_chu"], "trung_trong_kho": x["trung_trong_kho"]} for x in ds]})

    # báo cáo tóm tắt
    c_kd = Counter(x["kiem_dich"]["ket_luan"] for x in ds)
    c_ma = Counter(d["ma"] for x in ds for d in x["kiem_dich"]["dau_hieu"])
    c_nhan = Counter(x["nhan_de_xuat"] for x in ds)
    c_mang = Counter(x["mang"] for x in ds)
    theo_mang_nhan = defaultdict(Counter)
    for x in ds:
        theo_mang_nhan[x["mang"]][x["nhan_de_xuat"]] += 1
    import json
    print(json.dumps({"tong": len(ds), "kiem_dich": c_kd, "dau_hieu": c_ma, "nhan": c_nhan, "mang": c_mang,
                      "dinh_dang_loi": sum(bool(x["kiem_dich"]["dinh_dang"]) for x in ds),
                      "trung_trong_kho": sum(bool(x["trung_trong_kho"]) for x in ds),
                      "theo_mang": {k: dict(v) for k, v in theo_mang_nhan.items()}}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
