#!/usr/bin/env python3
"""Hộp thư bài học: agent ở mọi nền tảng nộp bài, Agent Evolution nhập vào sổ.

Mỗi bài là một file JSON riêng trong hộp thư, nên nhiều agent ghi cùng lúc không đè nhau.

  python3 hop_thu.py nop  --bot claude-sale --title "..." --text "..." --skill 09-chot-sale \
        --nen-tang claude --nhan-loi skill -e transcript:phien-123
  python3 hop_thu.py nhap [--db ledger.db]     # Agent Evolution chạy đầu mỗi lần quét

Hộp thư: --hop-thu, hoặc $SELF_EVO_INBOX, hoặc hop-thu/ cạnh file này.

Luật an toàn khi nhập (không phụ thuộc nội dung file):
- Mọi bài vào sổ ở tầng scratch, trạng thái proposed, giup = hai = 0.
- Bỏ mọi trường duyệt (owner_approval, approvers) và playbook_ma có trong file.
  Duyệt chỉ được ghi bằng lệnh của sổ, không được tự khai trong hộp thư.
- Bài có bí mật, dữ liệu liên hệ, tên skill lạ hoặc sai định dạng → chuyển sang loi/, kèm lý do.
"""
import argparse, importlib.util, json, os, shutil, sys, uuid
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("ledger", os.path.join(HERE, "ledger.py"))
ledger = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ledger)

DEFAULT_INBOX = os.environ.get("SELF_EVO_INBOX", os.path.join(HERE, "hop-thu"))
TRUONG = ["uid", "bot", "title", "body", "tags", "skill", "repo", "nen_tang", "nhan_loi",
          "tenant", "confidence", "sensitivity", "evidence", "nop_luc"]


def kiem_bai(d, catalog):
    """Kiểm như lệnh add của sổ. Lỗi → SystemExit có lý do."""
    for k in ("bot", "title", "body"):
        if not str(d.get(k) or "").strip():
            raise SystemExit("thiếu %s" % k)
    for text, cho in ((d["title"], "tiêu đề"), (d["body"], "nội dung"), (d.get("tags", ""), "tag"),
                      (d.get("repo", ""), "repo"), (d.get("tenant", ""), "tenant")):
        ledger.cam_bi_mat(text, cho)
    if d.get("nen_tang"):
        ledger.check_enum(d["nen_tang"], ledger.NEN_TANG, "nen_tang")
    if d.get("nhan_loi"):
        ledger.check_enum(d["nhan_loi"], ledger.NHAN_LOI, "nhan_loi")
    ledger.check_enum(d.get("sensitivity") or "none", ledger.SENS, "sensitivity")
    c = float(d.get("confidence", 0.5))
    if not 0 <= c <= 1:
        raise SystemExit("confidence phải trong 0..1")
    ledger.check_skill(d.get("skill") or "", catalog)
    ev = [ledger.parse_evidence(e) if isinstance(e, str) else tuple(e) for e in d.get("evidence") or []]
    return ledger.screened_evidence(ev)


def nop(args):
    catalog = os.path.abspath(args.catalog)
    d = {
        "uid": str(uuid.uuid4()), "bot": args.bot, "title": args.title, "body": args.text,
        "tags": args.tags or "", "skill": args.skill or "", "repo": args.repo or "",
        "nen_tang": args.nen_tang or "", "nhan_loi": args.nhan_loi or "", "tenant": args.tenant or "",
        "confidence": args.confidence, "sensitivity": args.sensitivity,
        "evidence": args.evidence or [], "nop_luc": ledger.now(),
    }
    ev = kiem_bai(d, catalog)
    d["evidence"] = [list(e) for e in ev]
    os.makedirs(args.hop_thu, exist_ok=True)
    ten = "%s-%s-%s.json" % (datetime.now().strftime("%Y%m%d-%H%M%S"), ledger.slugify(args.bot)[:20], d["uid"][:8])
    duong = os.path.join(args.hop_thu, ten)
    with open(duong, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(duong)
    return 0


def nhap(args):
    L = ledger.Ledger(args.db, args.actor, catalog=args.catalog)
    tep = sorted(f for f in os.listdir(args.hop_thu) if f.endswith(".json")) if os.path.isdir(args.hop_thu) else []
    thang = datetime.now().strftime("%Y-%m")
    da = os.path.join(args.hop_thu, "da-nhap", thang)
    loi = os.path.join(args.hop_thu, "loi")
    them = bo_qua = hong = 0
    for f in tep:
        p = os.path.join(args.hop_thu, f)
        try:
            with open(p, encoding="utf-8") as fh:
                d = json.load(fh)
            if not isinstance(d, dict):
                raise SystemExit("file không phải một bài")
            ev = kiem_bai(d, L.catalog)
            uid = d.get("uid") or str(uuid.uuid4())
            if L.db.execute("SELECT 1 FROM lessons WHERE uid=?", (uid,)).fetchone():
                bo_qua += 1
            else:
                # Ép an toàn: tầng nháp, chưa duyệt, bộ đếm 0, không mang playbook_ma.
                L.add(d["bot"], d["title"], d["body"], d.get("tags", ""), "scratch", ev,
                      float(d.get("confidence", 0.5)), d.get("sensitivity") or "none", "proposed",
                      uid=uid, owner_approval=None, skill=d.get("skill") or "", repo=d.get("repo") or "",
                      nen_tang=d.get("nen_tang") or "", nhan_loi=d.get("nhan_loi") or "",
                      tenant=d.get("tenant") or "", giup=0, hai=0, playbook_ma=None)
                them += 1
            os.makedirs(da, exist_ok=True)
            shutil.move(p, os.path.join(da, f))
        except (SystemExit, ValueError, KeyError, json.JSONDecodeError) as e:
            hong += 1
            os.makedirs(loi, exist_ok=True)
            shutil.move(p, os.path.join(loi, f))
            with open(os.path.join(loi, f + ".loi.txt"), "w", encoding="utf-8") as fh:
                fh.write(str(e) + "\n")
    L.audit("hop_thu_nhap", None, hop_thu=args.hop_thu, them=them, bo_qua=bo_qua, loi=hong)
    L.db.commit()
    print(json.dumps({"them": them, "bo_qua_trung": bo_qua, "loi": hong}, ensure_ascii=False))
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(description="Hộp thư bài học")
    p.add_argument("--hop-thu", default=DEFAULT_INBOX)
    p.add_argument("--catalog", default=ledger.DEFAULT_CATALOG)
    sp = p.add_subparsers(dest="lenh", required=True)

    a = sp.add_parser("nop", help="Nộp một bài học vào hộp thư")
    a.add_argument("--bot", required=True)
    a.add_argument("--title", required=True)
    a.add_argument("--text", required=True)
    a.add_argument("--skill")
    a.add_argument("--repo")
    a.add_argument("--nen-tang")
    a.add_argument("--nhan-loi")
    a.add_argument("--tenant")
    a.add_argument("--tags")
    a.add_argument("--confidence", type=float, default=0.5)
    a.add_argument("--sensitivity", default="none")
    a.add_argument("-e", "--evidence", action="append")
    a.set_defaults(ham=nop)

    b = sp.add_parser("nhap", help="Nhập mọi bài trong hộp thư vào sổ (Agent Evolution)")
    b.add_argument("--db", default=ledger.DEFAULT_DB)
    b.add_argument("--actor", default=os.environ.get("SELF_EVO_ACTOR", "agent-evolution"))
    b.set_defaults(ham=nhap)

    args = p.parse_args(argv)
    return args.ham(args)


if __name__ == "__main__":
    sys.exit(main())
