#!/usr/bin/env python3
"""Máy chấm eval dùng chung cho mọi repo skill của hệ MQ.

Hai lệnh:
  kiem   Kiểm định dạng file YAML trong evals/ (không cần API key). Dùng trong CI.
  cham   Chạy từng tình huống qua Claude API rồi chấm (cần ANTHROPIC_API_KEY).

Ví dụ:
  python cham.py kiem --repo ../sale-suite-os
  python cham.py cham --repo ../sale-suite-os --loc "evals/thuong-vu/**/*.yaml"
  python cham.py cham --repo ../sale-suite-os --skill 09-chot-sale --so-sanh

Chuẩn định dạng: xem may-cham/README.md.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

import yaml

TRUONG_BAT_BUOC = ["id", "skill", "loai", "dau_vao", "mong_doi"]
LOAI_HOP_LE = {"chuan", "bay"}
API_URL = "https://api.anthropic.com/v1/messages"
MODEL_MAC_DINH = os.environ.get("CHAM_MODEL", "claude-opus-5-5")
GIAM_KHAO_MAC_DINH = os.environ.get("CHAM_GIAM_KHAO", "claude-sonnet-5-5")
GIOI_HAN_THAM_CHIEU = 60_000  # ký tự references nạp kèm SKILL.md


# ---------------------------------------------------------------- đọc dữ liệu

@dataclass
class TinhHuong:
    id: str
    skill: str
    loai: str
    dau_vao: str
    phai_co: list[str]
    khong_duoc_co: list[str]
    hanh_vi: str
    nguoi_duyet: str
    tep: Path
    loi: list[str] = field(default_factory=list)


def doc_tinh_huong(tep: Path) -> TinhHuong:
    loi: list[str] = []
    try:
        du_lieu = yaml.safe_load(tep.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        return TinhHuong("?", "?", "?", "", [], [], "", "", tep, [f"YAML hỏng: {str(e).splitlines()[0]}"])
    if not isinstance(du_lieu, dict):
        return TinhHuong("?", "?", "?", "", [], [], "", "", tep, ["Gốc file không phải một khối khoá-giá trị"])
    for k in TRUONG_BAT_BUOC:
        if k not in du_lieu:
            loi.append(f"thiếu trường '{k}'")
    mong_doi = du_lieu.get("mong_doi") or {}
    if not isinstance(mong_doi, dict):
        loi.append("'mong_doi' phải là khối khoá-giá trị")
        mong_doi = {}
    loai = str(du_lieu.get("loai", "")).strip()
    if loai and loai not in LOAI_HOP_LE:
        loi.append(f"loai='{loai}' không hợp lệ (chuan | bay)")
    phai_co = mong_doi.get("phai_co") or []
    khong_duoc_co = mong_doi.get("khong_duoc_co") or []
    if not isinstance(phai_co, list) or not isinstance(khong_duoc_co, list):
        loi.append("'phai_co' và 'khong_duoc_co' phải là danh sách")
        phai_co, khong_duoc_co = [], []
    hanh_vi = str(mong_doi.get("hanh_vi") or "").strip()
    if not hanh_vi and not phai_co:
        loi.append("cần ít nhất 'hanh_vi' hoặc 'phai_co' để chấm được")
    return TinhHuong(
        id=str(du_lieu.get("id", "?")),
        skill=str(du_lieu.get("skill", "?")),
        loai=loai,
        dau_vao=str(du_lieu.get("dau_vao", "")),
        phai_co=[str(x) for x in phai_co],
        khong_duoc_co=[str(x) for x in khong_duoc_co],
        hanh_vi=hanh_vi,
        nguoi_duyet=str(du_lieu.get("nguoi_duyet") or ""),
        tep=tep,
        loi=loi,
    )


def tim_tep_eval(repo: Path, loc: str | None) -> list[Path]:
    mau = loc or "evals/**/*.yaml"
    tep = sorted(Path(p) for p in glob.glob(str(repo / mau), recursive=True))
    tep += sorted(Path(p) for p in glob.glob(str(repo / mau.replace(".yaml", ".yml")), recursive=True))
    return [t for t in dict.fromkeys(tep) if t.is_file()]


def lap_ban_do_skill(repo: Path) -> dict[str, Path]:
    """Tên skill → thư mục chứa SKILL.md. Tên lấy từ tên thư mục và từ frontmatter."""
    ban_do: dict[str, Path] = {}
    for f in repo.glob("**/SKILL.md"):
        if any(p in {".git", "node_modules", "dist"} for p in f.parts):
            continue
        ban_do.setdefault(f.parent.name, f.parent)
        ten = doc_ten_frontmatter(f)
        if ten:
            ban_do.setdefault(ten, f.parent)
    return ban_do


def doc_ten_frontmatter(f: Path) -> str | None:
    van_ban = f.read_text(encoding="utf-8", errors="ignore")
    if not van_ban.startswith("---"):
        return None
    phan = van_ban.split("---", 2)
    if len(phan) < 3:
        return None
    try:
        fm = yaml.safe_load(phan[1]) or {}
    except yaml.YAMLError:
        return None
    return str(fm.get("name")) if isinstance(fm, dict) and fm.get("name") else None


def nap_skill(thu_muc: Path) -> str:
    """SKILL.md + references/ (cắt ở GIOI_HAN_THAM_CHIEU ký tự)."""
    phan = [f"<skill path=\"{thu_muc.name}/SKILL.md\">\n{(thu_muc / 'SKILL.md').read_text(encoding='utf-8')}\n</skill>"]
    con_lai = GIOI_HAN_THAM_CHIEU
    for f in sorted(thu_muc.glob("references/**/*")):
        if not f.is_file() or f.suffix not in {".md", ".txt", ".yaml", ".yml", ".json", ".csv"}:
            continue
        noi_dung = f.read_text(encoding="utf-8", errors="ignore")
        if len(noi_dung) > con_lai:
            phan.append(f"<reference path=\"{f.relative_to(thu_muc)}\" note=\"bị cắt do giới hạn\">\n{noi_dung[:con_lai]}\n</reference>")
            break
        phan.append(f"<reference path=\"{f.relative_to(thu_muc)}\">\n{noi_dung}\n</reference>")
        con_lai -= len(noi_dung)
    return "\n\n".join(phan)


# ---------------------------------------------------------------- chấm chuỗi

def chuan_hoa(s: str) -> str:
    return " ".join(unicodedata.normalize("NFC", s).casefold().split())


def cham_chuoi(dau_ra: str, th: TinhHuong) -> dict:
    d = chuan_hoa(dau_ra)
    thieu = [x for x in th.phai_co if chuan_hoa(x) not in d]
    lot = [x for x in th.khong_duoc_co if chuan_hoa(x) and chuan_hoa(x) in d]
    return {"dat": not thieu and not lot, "thieu": thieu, "lot": lot}


# ---------------------------------------------------------------- gọi API

def goi_claude(model: str, he_thong: str, nguoi_dung: str, max_tokens: int = 4096) -> tuple[str, dict]:
    khoa = os.environ.get("ANTHROPIC_API_KEY")
    if not khoa:
        raise SystemExit("Thiếu ANTHROPIC_API_KEY. Lệnh 'kiem' không cần khoá; lệnh 'cham' thì cần.")
    than = {"model": model, "max_tokens": max_tokens, "messages": [{"role": "user", "content": nguoi_dung}]}
    if he_thong:
        than["system"] = he_thong
    yeu_cau = urllib.request.Request(
        API_URL,
        data=json.dumps(than).encode(),
        headers={"x-api-key": khoa, "anthropic-version": "2023-06-01", "content-type": "application/json"},
    )
    for lan in range(4):
        try:
            with urllib.request.urlopen(yeu_cau, timeout=300) as r:
                kq = json.loads(r.read())
            van_ban = "".join(b.get("text", "") for b in kq.get("content", []) if b.get("type") == "text")
            return van_ban, kq.get("usage", {})
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 529) and lan < 3:
                time.sleep(2 ** lan * 5)
                continue
            raise SystemExit(f"Lỗi API {e.code}: {e.read().decode(errors='ignore')[:500]}")
    raise SystemExit("API không phản hồi sau 4 lần thử")


HE_THONG_CHAY = (
    "You are an agent that has the following skill installed. Follow it exactly as you would in a real session. "
    "You have no tools in this test: if the skill tells you to call a tool or read a file you do not have, say what you "
    "would do and continue as far as you can with what the user gave you. Reply to the user directly.\n\n{skill}"
)

HE_THONG_GIAM_KHAO = (
    "Bạn là giám khảo chấm câu trả lời của một AI agent theo mô tả hành vi mong đợi. "
    "Chấm theo Ý, không theo câu chữ: nếu agent trích lại một cụm bị cấm chỉ để từ chối hoặc giải thích thì không tính là vi phạm. "
    "Chỉ trả về JSON một dòng: {\"dat\": true|false, \"ly_do\": \"<= 2 câu tiếng Việt\"}."
)


def giam_khao(model: str, th: TinhHuong, dau_ra: str, chuoi: dict) -> dict:
    nd = (
        f"LOẠI TÌNH HUỐNG: {th.loai} (bay = bẫy, agent phải nhận ra và xử lý đúng)\n\n"
        f"ĐẦU VÀO NGƯỜI DÙNG:\n{th.dau_vao}\n\n"
        f"HÀNH VI MONG ĐỢI:\n{th.hanh_vi or '(không ghi; dựa vào danh sách phải có)'}\n\n"
        f"PHẢI CÓ (gợi ý): {th.phai_co}\nKHÔNG ĐƯỢC CÓ (gợi ý): {th.khong_duoc_co}\n"
        f"KIỂM CHUỖI MÁY: thiếu={chuoi['thieu']} lọt={chuoi['lot']}\n\n"
        f"CÂU TRẢ LỜI CỦA AGENT:\n{dau_ra}"
    )
    van_ban, _ = goi_claude(model, HE_THONG_GIAM_KHAO, nd, max_tokens=400)
    return phan_tich_giam_khao(van_ban)


def phan_tich_giam_khao(van_ban: str) -> dict:
    dau, cuoi = van_ban.find("{"), van_ban.rfind("}")
    try:
        kq = json.loads(van_ban[dau:cuoi + 1])
        return {"dat": bool(kq.get("dat")), "ly_do": str(kq.get("ly_do", ""))}
    except (ValueError, json.JSONDecodeError):
        return {"dat": False, "ly_do": f"Giám khảo trả sai định dạng: {van_ban[:200]}"}


# ---------------------------------------------------------------- lệnh

def lenh_kiem(args) -> int:
    repo = Path(args.repo).resolve()
    tep = tim_tep_eval(repo, args.loc)
    if not tep:
        print(f"Không thấy file eval nào trong {repo} (mẫu: {args.loc or 'evals/**/*.yaml'})")
        return 1
    ban_do = lap_ban_do_skill(repo)
    so_loi, ids, theo_skill = 0, {}, {}
    for t in tep:
        th = doc_tinh_huong(t)
        loi = list(th.loi)
        if th.id in ids:
            loi.append(f"trùng id với {ids[th.id]}")
        ids.setdefault(th.id, t.relative_to(repo))
        if ban_do and th.skill != "?" and th.skill not in ban_do:
            loi.append(f"skill '{th.skill}' không có SKILL.md tương ứng trong repo")
        if not loi:
            s = theo_skill.setdefault(th.skill, {"tong": 0, "bay": 0, "duyet": 0})
            s["tong"] += 1
            s["bay"] += th.loai == "bay"
            s["duyet"] += bool(th.nguoi_duyet)
        for l in loi:
            print(f"LỖI  {t.relative_to(repo)}: {l}")
        so_loi += len(loi)
    canh_bao = 0
    for ten, s in sorted(theo_skill.items()):
        if s["tong"] < 3:
            print(f"CẢNH BÁO  skill '{ten}': mới {s['tong']} tình huống (chuẩn ≥ 3)")
            canh_bao += 1
        if s["bay"] < 1:
            print(f"CẢNH BÁO  skill '{ten}': chưa có tình huống bẫy")
            canh_bao += 1
    if ban_do:
        for ten in sorted(set(p.name for p in ban_do.values()) - set(theo_skill)):
            print(f"CẢNH BÁO  skill '{ten}' chưa có eval")
            canh_bao += 1
    tong_duyet = sum(s["duyet"] for s in theo_skill.values())
    print(f"\n{len(tep)} tình huống · {len(theo_skill)} skill · {so_loi} lỗi · {canh_bao} cảnh báo · {tong_duyet} đã duyệt")
    if args.nghiem and canh_bao:
        return 1
    return 1 if so_loi else 0


def lenh_cham(args) -> int:
    repo = Path(args.repo).resolve()
    ban_do = lap_ban_do_skill(repo)
    ds = [doc_tinh_huong(t) for t in tim_tep_eval(repo, args.loc)]
    ds = [th for th in ds if not th.loi]
    if args.skill:
        ds = [th for th in ds if th.skill == args.skill]
    if args.gioi_han:
        ds = ds[: args.gioi_han]
    if not ds:
        print("Không có tình huống hợp lệ để chấm.")
        return 1
    ra = Path(args.ra).resolve()
    ra.mkdir(parents=True, exist_ok=True)
    nhan = time.strftime("%Y%m%d-%H%M%S")
    tep_jsonl = ra / f"ket-qua-{nhan}.jsonl"
    ket_qua = []
    with tep_jsonl.open("w", encoding="utf-8") as out:
        for i, th in enumerate(ds, 1):
            if th.skill not in ban_do:
                print(f"[{i}/{len(ds)}] {th.id} BỎ QUA: không tìm thấy skill '{th.skill}'")
                continue
            kq = {"id": th.id, "skill": th.skill, "loai": th.loai, "tep": str(th.tep.relative_to(repo))}
            che_do = [("co_skill", nap_skill(ban_do[th.skill]))]
            if args.so_sanh:
                che_do.append(("khong_skill", ""))
            for ten_che_do, skill in che_do:
                bat_dau = time.time()
                he_thong = HE_THONG_CHAY.format(skill=skill) if skill else ""
                dau_ra, usage = goi_claude(args.model, he_thong, th.dau_vao)
                chuoi = cham_chuoi(dau_ra, th)
                gk = None if args.khong_giam_khao else giam_khao(args.giam_khao, th, dau_ra, chuoi)
                kq[ten_che_do] = {
                    "dat": gk["dat"] if gk else chuoi["dat"],
                    "chuoi": chuoi,
                    "giam_khao": gk,
                    "token_vao": usage.get("input_tokens"),
                    "token_ra": usage.get("output_tokens"),
                    "giay": round(time.time() - bat_dau, 1),
                    "dau_ra": dau_ra,
                }
            out.write(json.dumps(kq, ensure_ascii=False) + "\n")
            ket_qua.append(kq)
            dau = "ĐẠT " if kq["co_skill"]["dat"] else "TRƯỢT"
            print(f"[{i}/{len(ds)}] {dau} {th.id} ({th.skill})")
    tep_md = ra / f"bang-diem-{nhan}.md"
    tep_md.write_text(lap_bang_diem(ket_qua, args), encoding="utf-8")
    print(f"\nBảng điểm: {tep_md}\nChi tiết: {tep_jsonl}")
    tong = len(ket_qua)
    dat = sum(k["co_skill"]["dat"] for k in ket_qua)
    return 0 if tong and dat / tong >= args.nguong else 1


def lap_bang_diem(ket_qua: list[dict], args) -> str:
    dong = [f"# Bảng điểm eval\n", f"Model chạy: `{args.model}` · Giám khảo: `{'tắt' if args.khong_giam_khao else args.giam_khao}`\n"]
    theo_skill: dict[str, dict] = {}
    for k in ket_qua:
        s = theo_skill.setdefault(k["skill"], {"tong": 0, "dat": 0, "bay": 0, "bay_dat": 0, "ks": 0, "token": 0})
        s["tong"] += 1
        s["dat"] += k["co_skill"]["dat"]
        s["token"] += (k["co_skill"]["token_vao"] or 0) + (k["co_skill"]["token_ra"] or 0)
        if k["loai"] == "bay":
            s["bay"] += 1
            s["bay_dat"] += k["co_skill"]["dat"]
        if "khong_skill" in k:
            s["ks"] += k["khong_skill"]["dat"]
    tieu_de = "| Skill | Đạt | Bẫy đạt | Token |" + (" Không skill đạt | Skill có ích? |" if args.so_sanh else "")
    dong += [tieu_de, "|" + "---|" * (6 if args.so_sanh else 4)]
    for ten, s in sorted(theo_skill.items()):
        hang = f"| {ten} | {s['dat']}/{s['tong']} | {s['bay_dat']}/{s['bay']} | {s['token']:,} |"
        if args.so_sanh:
            co_ich = "có" if s["dat"] > s["ks"] else ("ngang" if s["dat"] == s["ks"] else "**không**")
            hang += f" {s['ks']}/{s['tong']} | {co_ich} |"
        dong.append(hang)
    tong, dat = len(ket_qua), sum(k["co_skill"]["dat"] for k in ket_qua)
    dong.append(f"\n**Tổng: {dat}/{tong} đạt ({dat / tong:.0%})**\n" if tong else "\nKhông có kết quả.\n")
    truot = [k for k in ket_qua if not k["co_skill"]["dat"]]
    if truot:
        dong.append("## Tình huống trượt\n")
        dong.append("| ID | Skill | Lý do |")
        dong.append("|---|---|---|")
        for k in truot:
            c = k["co_skill"]
            ly_do = (c["giam_khao"] or {}).get("ly_do") or f"thiếu {c['chuoi']['thieu']} · lọt {c['chuoi']['lot']}"
            dong.append(f"| {k['id']} | {k['skill']} | {ly_do.replace('|', '/')} |")
    return "\n".join(dong) + "\n"


def main() -> int:
    p = argparse.ArgumentParser(description="Máy chấm eval dùng chung của hệ MQ")
    sp = p.add_subparsers(dest="lenh", required=True)

    k = sp.add_parser("kiem", help="Kiểm định dạng file eval (không cần API key)")
    k.add_argument("--repo", default=".", help="Thư mục gốc repo skill")
    k.add_argument("--loc", help="Mẫu glob tương đối, mặc định evals/**/*.yaml")
    k.add_argument("--nghiem", action="store_true", help="Coi cảnh báo độ phủ là lỗi")
    k.set_defaults(ham=lenh_kiem)

    c = sp.add_parser("cham", help="Chạy và chấm tình huống qua Claude API")
    c.add_argument("--repo", default=".")
    c.add_argument("--loc")
    c.add_argument("--skill", help="Chỉ chấm một skill")
    c.add_argument("--gioi-han", type=int, help="Chỉ chấm N tình huống đầu (chạy thử)")
    c.add_argument("--model", default=MODEL_MAC_DINH)
    c.add_argument("--giam-khao", default=GIAM_KHAO_MAC_DINH)
    c.add_argument("--khong-giam-khao", action="store_true", help="Chỉ chấm theo chuỗi")
    c.add_argument("--so-sanh", action="store_true", help="Chạy thêm bản không có skill để đo skill có ích không")
    c.add_argument("--nguong", type=float, default=0.8, help="Tỷ lệ đạt tối thiểu để trả mã thoát 0")
    c.add_argument("--ra", default="ket-qua-eval", help="Thư mục ghi kết quả")
    c.set_defaults(ham=lenh_cham)

    args = p.parse_args()
    return args.ham(args)


if __name__ == "__main__":
    sys.exit(main())
