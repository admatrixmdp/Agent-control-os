#!/usr/bin/env python3
"""Sổ bài học vòng lặp cải tiến. SQLite + FTS5 (BM25). Chỉ thư viện chuẩn.

DB: --db, hoặc $SELF_EVO_DB, hoặc ledger.db cạnh file này (máy riêng, không commit).
Thư mục wiki/, staging/, proposals/: --root hoặc $SELF_EVO_ROOT, mặc định cạnh file này.
Actor trong nhật ký: --actor, hoặc $SELF_EVO_ACTOR, hoặc $USER.

Repo này public. Không ghi dữ liệu khách, trích dẫn thật, email, số điện thoại, token.
Bài sensitivity khác none chỉ lên durable/accepted khi có duyệt của cả Dat và Quân.
"""
import argparse, csv, glob, json, os, re, sqlite3, sys, unicodedata, uuid
from datetime import datetime, timedelta

try:
    from zoneinfo import ZoneInfo
    _TZ = ZoneInfo("Asia/Ho_Chi_Minh")
except Exception:
    _TZ = None

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DB = os.environ.get("SELF_EVO_DB", os.path.join(HERE, "ledger.db"))
DEFAULT_ROOT = os.environ.get("SELF_EVO_ROOT", HERE)
DEFAULT_CATALOG = os.path.abspath(os.path.join(HERE, "..", "..", "danh-muc", "skills.yaml"))
TIERS = ["scratch", "working", "durable"]
STATUSES = ["proposed", "accepted", "retired"]
SENS = ["none", "user", "finance", "sensitive"]
EV_KINDS = ["transcript", "session", "file", "url", "quote", "other"]
NHAN_LOI = ["harness", "skill", "agent", "tri-thuc", "mo-hinh", "khong-loi"]
NEN_TANG = ["claude", "claude-code", "chatgpt", "codex", "goclaw", "goso", "claude-duet", "dots", "muse", "grok-bot"]
APPROVER_KEYS = (("dat", "Dat"), ("quan", "Quân"))

SCHEMA = """
CREATE TABLE IF NOT EXISTS lessons(
  id INTEGER PRIMARY KEY, uid TEXT UNIQUE NOT NULL, bot TEXT NOT NULL,
  title TEXT NOT NULL, body TEXT NOT NULL, tags TEXT NOT NULL DEFAULT '',
  tier TEXT NOT NULL DEFAULT 'scratch' CHECK(tier IN ('scratch','working','durable')),
  confidence REAL NOT NULL DEFAULT 0.5 CHECK(confidence BETWEEN 0 AND 1),
  sensitivity TEXT NOT NULL DEFAULT 'none' CHECK(sensitivity IN ('none','user','finance','sensitive')),
  status TEXT NOT NULL DEFAULT 'proposed' CHECK(status IN ('proposed','accepted','retired')),
  owner_approval TEXT,
  approvers TEXT NOT NULL DEFAULT '',
  skill TEXT NOT NULL DEFAULT '',
  repo TEXT NOT NULL DEFAULT '',
  nen_tang TEXT NOT NULL DEFAULT '',
  nhan_loi TEXT NOT NULL DEFAULT '' CHECK(nhan_loi IN ('','harness','skill','agent','tri-thuc','mo-hinh','khong-loi')),
  tenant TEXT NOT NULL DEFAULT '',
  giup INTEGER NOT NULL DEFAULT 0 CHECK(giup >= 0),
  hai INTEGER NOT NULL DEFAULT 0 CHECK(hai >= 0),
  playbook_ma TEXT,
  created_at TEXT NOT NULL, updated_at TEXT NOT NULL, last_used_at TEXT);
CREATE TABLE IF NOT EXISTS evidence(
  id INTEGER PRIMARY KEY, lesson_id INTEGER NOT NULL REFERENCES lessons(id) ON DELETE CASCADE,
  kind TEXT NOT NULL, ref TEXT NOT NULL, note TEXT, added_by TEXT, added_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS audit(
  id INTEGER PRIMARY KEY, ts TEXT NOT NULL, actor TEXT NOT NULL, action TEXT NOT NULL,
  lesson_id INTEGER, details TEXT);
CREATE VIRTUAL TABLE IF NOT EXISTS lessons_fts USING fts5(
  title, body, tags, tokenize='unicode61 remove_diacritics 2');
"""

_SKILL_CACHE = {}
_SECRET_RES = [
    re.compile(r"(?<![\w])[\w.+\-]+@[\w\-]+\.[A-Za-z]{2,}"),
    re.compile(r"(?<!\w)(?:\+84|0)\d{8,10}(?!\w)"),
    re.compile(r"(?i)\b(?:sk-[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{16,}|github_pat_[A-Za-z0-9_]{16,}|xox[baprs]-[A-Za-z0-9-]{10,}|AKIA[A-Z0-9]{16}|glpat-[A-Za-z0-9\-]{16,})\b"),
    re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._\-]{12,}"),
]


def now_dt():
    if _TZ is not None:
        return datetime.now(_TZ)
    return datetime.now().astimezone()


def now():
    return now_dt().isoformat(timespec="seconds")


def fold(s):
    """unicode61 bỏ dấu kết hợp nhưng không bỏ đ/Đ. Gấp đ→d để 'duoc' khớp 'được'."""
    s = (s or "").replace("đ", "d").replace("Đ", "D")
    s = unicodedata.normalize("NFD", s)
    return "".join(ch for ch in s if unicodedata.category(ch) != "Mn")


def tokens(s):
    return [t for t in re.findall(r"\w+", fold(s).lower()) if len(t) > 1 or t.isdigit()]


def fts_query(q, mode="or"):
    toks = tokens(q)
    if not toks:
        return None
    return (" OR " if mode == "or" else " AND ").join('"%s"' % t for t in toks)


def norm_tags(t):
    if isinstance(t, (list, tuple)):
        t = ",".join(t)
    out = []
    for x in (t or "").split(","):
        x = x.strip().lower().replace(" ", "-")
        if x and x not in out:
            out.append(x)
    return ",".join(out)


def cam_bi_mat(text, cho):
    if not text:
        return
    for rx in _SECRET_RES:
        if rx.search(str(text)):
            raise SystemExit("không ghi bí mật hoặc dữ liệu liên hệ vào sổ (%s)" % cho)


def check_enum(value, allowed, label):
    value = (value or "").strip()
    if value and value not in allowed:
        raise SystemExit("%s %r không hợp lệ (chọn: %s)" % (label, value, ", ".join(allowed)))
    return value


def check_count(name, value):
    n = int(value or 0)
    if n < 0:
        raise SystemExit("%s phải >= 0" % name)
    return n


def load_skill_names(path):
    path = os.path.abspath(path)
    if not os.path.isfile(path):
        raise SystemExit("không thấy danh-muc skill: %s" % path)
    mtime = os.path.getmtime(path)
    hit = _SKILL_CACHE.get(path)
    if hit and hit[0] == mtime:
        return hit[1]
    rx = re.compile(r"""^\s*-\s*ten:\s*(?:"([^"]+)"|'([^']+)'|([^\s#]+))\s*(?:#.*)?$""")
    names = set()
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = rx.match(line)
            if m:
                names.add(next(g for g in m.groups() if g))
    if not names:
        raise SystemExit("danh-muc skill trống: %s" % path)
    _SKILL_CACHE[path] = (mtime, names)
    return names


def check_skill(skill, catalog):
    skill = (skill or "").strip()
    if not skill:
        return ""
    if skill not in load_skill_names(catalog):
        raise SystemExit("skill %r không có trong danh-muc/skills.yaml" % skill)
    return skill


def approval_chunks(raw):
    if raw is None:
        return []
    if isinstance(raw, (list, tuple)):
        out = []
        for item in raw:
            out.extend(approval_chunks(item))
        return out
    return [p.strip() for p in re.split(r"\s*\|\s*|\s*;\s*|\n+", str(raw)) if p.strip()]


def approval_state(raw):
    """Trả (chuỗi lưu, tập khóa dat/quan). Một mệnh đề có cả hai tên vẫn tính đủ."""
    chunks = approval_chunks(raw)
    found = {}
    for chunk in chunks:
        hits = [k for k, _label in APPROVER_KEYS if k in set(tokens(chunk))]
        for h in hits:
            found.setdefault(h, chunk)
    text = " | ".join(chunks) if chunks else None
    return text, set(found)


def format_approvers(keys):
    return ",".join(label for k, label in APPROVER_KEYS if k in keys)


def merge_approval(old, new):
    parts = []
    if old:
        parts.append(old)
    if new:
        if isinstance(new, (list, tuple)):
            parts.extend(str(x) for x in new if str(x).strip())
        else:
            parts.append(str(new))
    return parts or None


def parse_evidence(spec):
    """'kind:ref' hoặc trần: http(s) → url, đường dẫn → file, còn lại → quote."""
    m = re.match(r"^(\w+):(.*)$", spec, re.S)
    if m and m.group(1).lower() in EV_KINDS and not spec.lower().startswith(("http:", "https:")):
        kind, ref = m.group(1).lower(), m.group(2).strip()
        if kind == "session":
            kind = "transcript"
    elif re.match(r"^https?://", spec):
        kind, ref = "url", spec
    elif spec.startswith(("/", "~", "./")):
        kind, ref = "file", spec
    else:
        kind, ref = "quote", spec
    if not ref:
        raise SystemExit("bằng chứng rỗng: %r" % spec)
    return kind, ref


def screened_evidence(evidence):
    ev = []
    for e in evidence:
        if isinstance(e, str):
            kind, ref = parse_evidence(e)
            note = None
        else:
            kind, ref = e[0], e[1]
            note = e[2] if len(e) > 2 else None
        cam_bi_mat(ref, "bằng chứng")
        cam_bi_mat(note or "", "bằng chứng")
        ev.append((kind, ref, note))
    return ev


class Ledger:
    def __init__(self, path, actor, catalog=None):
        self.path, self.actor = path, actor
        self.catalog = os.path.abspath(catalog or DEFAULT_CATALOG)
        d = os.path.dirname(os.path.abspath(path))
        os.makedirs(d, exist_ok=True)
        self.db = sqlite3.connect(path)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys=ON")
        try:
            self.db.executescript(SCHEMA)
        except sqlite3.OperationalError as e:
            raise SystemExit("SQLite thiếu FTS5 (%s)." % e)

    def audit(self, action, lesson_id=None, **details):
        self.db.execute("INSERT INTO audit(ts,actor,action,lesson_id,details) VALUES(?,?,?,?,?)",
                        (now(), self.actor, action, lesson_id, json.dumps(details, ensure_ascii=False)))

    def reindex(self, lid):
        r = self.get(lid)
        extra = " ".join(x for x in (r["tags"].replace(",", " "), r["skill"] or "", r["nhan_loi"] or "", r["repo"] or "") if x)
        self.db.execute("DELETE FROM lessons_fts WHERE rowid=?", (lid,))
        self.db.execute("INSERT INTO lessons_fts(rowid,title,body,tags) VALUES(?,?,?,?)",
                        (lid, fold(r["title"]), fold(r["body"]), fold(extra)))

    def get(self, lid):
        r = self.db.execute("SELECT * FROM lessons WHERE id=?", (lid,)).fetchone()
        if not r:
            raise SystemExit("không thấy bài %s" % lid)
        return r

    def evidence(self, lid):
        return self.db.execute("SELECT * FROM evidence WHERE lesson_id=? ORDER BY id", (lid,)).fetchall()

    def _gate(self, sensitivity, tier, status, keys):
        if sensitivity == "none":
            return
        if tier != "durable" and status != "accepted":
            return
        missing = [label for k, label in APPROVER_KEYS if k not in keys]
        if missing:
            raise SystemExit(
                "sensitivity=%s: cần duyệt của cả Dat và Quân trước khi lên durable/accepted. Thiếu: %s. "
                "Truyền hai lần --owner-approved, mỗi người một mệnh đề (ai, khi nào, ở đâu)."
                % (sensitivity, ", ".join(missing)))

    def add(self, bot, title, body, tags="", tier="scratch", evidence=(), confidence=0.5,
            sensitivity="none", status="proposed", uid=None, created_at=None, updated_at=None,
            owner_approval=None, skill="", repo="", nen_tang="", nhan_loi="", tenant="",
            giup=0, hai=0, playbook_ma=None, log=True):
        if tier not in TIERS or status not in STATUSES or sensitivity not in SENS:
            raise SystemExit("tầng, trạng thái hoặc sensitivity không hợp lệ")
        if not 0 <= float(confidence) <= 1:
            raise SystemExit("confidence phải trong khoảng 0..1")
        cam_bi_mat(title, "tiêu đề")
        cam_bi_mat(body, "nội dung")
        cam_bi_mat(tags, "tag")
        cam_bi_mat(repo, "repo")
        cam_bi_mat(tenant, "tenant")
        cam_bi_mat(owner_approval if isinstance(owner_approval, str) else " ".join(approval_chunks(owner_approval)), "duyệt")
        skill = check_skill(skill, self.catalog)
        nen_tang = check_enum(nen_tang, NEN_TANG, "nen_tang")
        nhan_loi = check_enum(nhan_loi, NHAN_LOI, "nhan_loi")
        giup, hai = check_count("giup", giup), check_count("hai", hai)
        ev = screened_evidence(evidence)
        if tier != "scratch" and not ev:
            raise SystemExit("bài chưa có bằng chứng phải ở tầng scratch")
        text, keys = approval_state(owner_approval)
        self._gate(sensitivity, tier, status, keys)
        ts = now()
        cur = self.db.execute(
            """INSERT INTO lessons(uid,bot,title,body,tags,tier,confidence,sensitivity,status,
               owner_approval,approvers,skill,repo,nen_tang,nhan_loi,tenant,giup,hai,playbook_ma,created_at,updated_at)
               VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (uid or uuid.uuid4().hex, bot, title, body, norm_tags(tags), tier, float(confidence),
             sensitivity, status, text, format_approvers(keys), skill, (repo or "").strip(), nen_tang,
             nhan_loi, (tenant or "").strip(), giup, hai, playbook_ma or None, created_at or ts, updated_at or ts))
        lid = cur.lastrowid
        for kind, ref, note in ev:
            self.db.execute("INSERT INTO evidence(lesson_id,kind,ref,note,added_by,added_at) VALUES(?,?,?,?,?,?)",
                            (lid, kind, ref, note, self.actor, ts))
        self.reindex(lid)
        if log:
            self.audit("add", lid, bot=bot, title=title, tier=tier, evidence=len(ev), skill=skill,
                       approvers=format_approvers(keys))
        self.db.commit()
        return lid

    def add_evidence(self, lid, spec, note=None):
        self.get(lid)
        kind, ref = parse_evidence(spec)
        kind, ref, note = screened_evidence([(kind, ref, note)])[0]
        self.db.execute("INSERT INTO evidence(lesson_id,kind,ref,note,added_by,added_at) VALUES(?,?,?,?,?,?)",
                        (lid, kind, ref, note, self.actor, now()))
        self.db.execute("UPDATE lessons SET updated_at=? WHERE id=?", (now(), lid))
        self.audit("evidence_add", lid, kind=kind, ref=ref)
        self.db.commit()

    def set_fields(self, lid, action, **f):
        f["updated_at"] = now()
        old = dict(self.get(lid))
        self.db.execute("UPDATE lessons SET %s WHERE id=?" % ",".join("%s=?" % k for k in f),
                        (*f.values(), lid))
        self.audit(action, lid, **{k: [old.get(k), v] for k, v in f.items() if k != "updated_at"})
        self.reindex(lid)
        self.db.commit()

    def promote(self, lid, approval=None):
        r = self.get(lid)
        if r["status"] == "retired":
            raise SystemExit("bài %s đã retire" % lid)
        i = TIERS.index(r["tier"])
        if i == 2:
            raise SystemExit("đã ở durable")
        new = TIERS[i + 1]
        if not self.evidence(lid):
            raise SystemExit("bài %s chưa có bằng chứng; thêm bằng `evidence add` trước khi promote" % lid)
        f = {"tier": new}
        if new == "durable":
            if r["confidence"] < 0.6:
                raise SystemExit("confidence %.2f < 0.6; nâng confidence trước khi lên durable" % r["confidence"])
            f["status"] = "accepted"
        text, keys = approval_state(merge_approval(r["owner_approval"], approval))
        self._gate(r["sensitivity"], new, f.get("status", r["status"]), keys)
        if text:
            f["owner_approval"] = text
            f["approvers"] = format_approvers(keys)
        self.set_fields(lid, "promote", **f)
        return new

    def demote(self, lid):
        r = self.get(lid)
        i = TIERS.index(r["tier"])
        if i == 0:
            raise SystemExit("đã ở scratch")
        self.set_fields(lid, "demote", tier=TIERS[i - 1])
        return TIERS[i - 1]

    def accept(self, lid, approval=None):
        r = self.get(lid)
        text, keys = approval_state(merge_approval(r["owner_approval"], approval))
        self._gate(r["sensitivity"], r["tier"], "accepted", keys)
        f = {"status": "accepted"}
        if text:
            f["owner_approval"] = text
            f["approvers"] = format_approvers(keys)
        self.set_fields(lid, "accept", **f)

    def search(self, q, bot=None, tag=None, tier=None, status=None, limit=10, mode="or", include_retired=False,
               skill=None, repo=None, nen_tang=None, nhan_loi=None, tenant=None):
        mq = fts_query(q, mode)
        if not mq:
            return []
        sql = ("SELECT l.*, bm25(lessons_fts, 10.0, 3.0, 5.0) AS score FROM lessons_fts "
               "JOIN lessons l ON l.id=lessons_fts.rowid WHERE lessons_fts MATCH ?")
        args = [mq]
        for col, val in (("bot", bot), ("tier", tier), ("status", status), ("skill", skill), ("repo", repo),
                         ("nen_tang", nen_tang), ("nhan_loi", nhan_loi), ("tenant", tenant)):
            if val:
                sql += " AND l.%s=?" % col
                args.append(val)
        if not status and not include_retired:
            sql += " AND l.status!='retired'"
        if tag:
            sql += " AND (','||l.tags||',') LIKE ?"
            args.append("%%,%s,%%" % norm_tags(tag))
        sql += " ORDER BY score LIMIT ?"
        args.append(limit)
        return self.db.execute(sql, args).fetchall()

    def duplicates(self, ids=None, jaccard_min=0.5, ratio_min=0.6):
        rows = self.db.execute("SELECT * FROM lessons WHERE status!='retired'").fetchall()
        byid = {r["id"]: r for r in rows}
        toks = {r["id"]: set(tokens(r["title"] + " " + r["body"])) for r in rows}
        out, seen = [], set()
        for r in rows:
            if ids is not None and r["id"] not in ids:
                continue
            q = fts_query(r["title"] + " " + r["body"])
            if not q:
                continue
            hits = self.db.execute(
                "SELECT rowid, bm25(lessons_fts) s FROM lessons_fts WHERE lessons_fts MATCH ? ORDER BY s LIMIT 6",
                (q,)).fetchall()
            selfs = next((h["s"] for h in hits if h["rowid"] == r["id"]), None)
            for h in hits:
                o = h["rowid"]
                if o == r["id"] or o not in byid:
                    continue
                key = tuple(sorted((r["id"], o)))
                if key in seen:
                    continue
                a, b = toks[r["id"]], toks[o]
                jac = len(a & b) / max(1, len(a | b))
                ratio = (h["s"] / selfs) if selfs else 0
                if jac >= jaccard_min or ratio >= ratio_min:
                    seen.add(key)
                    out.append((key[0], key[1], round(jac, 2), round(ratio, 2)))
        return out


def fmt(r, ev=None, score=None):
    s = "#%d [%s/%s] %s  (bot=%s skill=%s nhan=%s conf=%.2f sens=%s tags=%s)" % (
        r["id"], r["tier"], r["status"], r["title"], r["bot"], r["skill"] or "-", r["nhan_loi"] or "-",
        r["confidence"], r["sensitivity"], r["tags"] or "-")
    if score is not None:
        s += "  bm25=%.3f" % score
    s += "\n    " + r["body"].replace("\n", "\n    ")
    if ev is not None:
        for e in ev:
            s += "\n    - E%d %s: %s%s" % (e["id"], e["kind"], e["ref"], (" (%s)" % e["note"]) if e["note"] else "")
    return s


def emit(args, data, text):
    if getattr(args, "json", False):
        print(json.dumps(data, ensure_ascii=False, indent=2, default=str))
    else:
        print(text)


def rowd(r):
    return {k: r[k] for k in r.keys()}


def slugify(s):
    s = re.sub(r"[^\w]+", "-", fold(s).lower()).strip("-")
    return s or "khong-ten"


def cite(e):
    if e["kind"] == "url":
        return "[%s](%s)" % (e["ref"], e["ref"])
    if e["kind"] == "file":
        return "`%s`" % e["ref"]
    if e["kind"] == "quote":
        return "“%s”" % e["ref"]
    return "%s `%s`" % (e["kind"], e["ref"])


def wiki_build(L, outdir, include_sensitive=False):
    if os.path.isfile(os.path.join(outdir, "SKILL.md")):
        raise SystemExit("wiki build từ chối thư mục có SKILL.md")
    os.makedirs(outdir, exist_ok=True)
    for f in os.listdir(outdir):
        if f.endswith(".md"):
            os.remove(os.path.join(outdir, f))
    rows = L.db.execute(
        "SELECT * FROM lessons WHERE tier IN ('working','durable') AND status!='retired' "
        "ORDER BY tier DESC, confidence DESC, id").fetchall()
    pages, skipped = {}, 0
    for r in rows:
        if r["sensitivity"] == "sensitive" and not include_sensitive:
            skipped += 1
            continue
        for t in (r["tags"].split(",") if r["tags"] else ["khong-tag"]):
            pages.setdefault(t, []).append(r)
    for t, rs in sorted(pages.items()):
        lines = ["# %s" % t, "",
                 "_Sinh bởi `ledger.py wiki build` lúc %s. Sửa trong sổ, không sửa file này._" % now(), ""]
        for r in rs:
            ev = L.evidence(r["id"])
            refs = "".join("[^%d-%d]" % (r["id"], e["id"]) for e in ev)
            badge = "" if r["sensitivity"] == "none" else " · nhạy: %s" % r["sensitivity"]
            skill = (" · skill %s" % r["skill"]) if r["skill"] else ""
            lines += ["## %s" % r["title"], "",
                      "*Bài #%d · %s/%s · confidence %.2f · bot %s%s%s*" % (
                          r["id"], r["tier"], r["status"], r["confidence"], r["bot"], skill, badge), "",
                      r["body"].strip() + " " + refs, ""]
            for e in ev:
                lines.append("[^%d-%d]: %s%s" % (r["id"], e["id"], cite(e), (" — " + e["note"]) if e["note"] else ""))
            lines.append("")
        with open(os.path.join(outdir, slugify(t) + ".md"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
    idx = ["# Wiki bài học", "", "_Sinh %s từ bài working và durable._" % now(), ""]
    idx += ["- [%s](%s.md) — %d bài" % (t, slugify(t), len(rs)) for t, rs in sorted(pages.items())]
    if skipped:
        idx += ["", "_%d bài sensitive bị ẩn (thêm --include-sensitive)._" % skipped]
    with open(os.path.join(outdir, "index.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(idx) + "\n")
    L.audit("wiki_build", None, pages=len(pages), lessons=len(rows), outdir=outdir)
    L.db.commit()
    return pages, skipped


PROPOSAL_SECTIONS = ["## Vấn đề", "## Bài học dẫn chứng", "## SKILL.md đề xuất", "## Tham chiếu", "## Duyệt"]


def _q(s):
    return json.dumps("" if s is None else str(s), ensure_ascii=False)


def dump_eval(case, path):
    def seq(items, indent):
        items = list(items or [])
        if not items:
            return "[]"
        pad = " " * indent
        return "\n" + "\n".join("%s- %s" % (pad, _q(x)) for x in items)

    lines = [
        "id: %s" % _q(case["id"]),
        "skill: %s" % _q(case["skill"]),
        "loai: %s" % _q(case["loai"]),
        "mo_ta: %s" % _q(case.get("mo_ta") or ""),
        "dau_vao: %s" % _q(case["dau_vao"]),
        "mong_doi:",
        "  phai_co: %s" % seq(case.get("phai_co"), 4),
        "  khong_duoc_co: %s" % seq(case.get("khong_duoc_co"), 4),
        "  hanh_vi: %s" % _q(case.get("hanh_vi") or ""),
        "can_cu: %s" % seq(case.get("can_cu"), 2),
        "nguoi_duyet: %s" % _q(case.get("nguoi_duyet") or ""),
    ]
    text = "\n".join(lines) + "\n"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return text


def _yaml_val(v):
    v = v.strip()
    if v == "[]":
        return []
    if v.startswith('"'):
        return json.loads(v)
    return v


def parse_eval_yaml(text):
    root, mong, cur = {}, {}, None
    for raw in text.splitlines():
        if not raw.strip():
            continue
        stripped = raw.lstrip()
        if stripped.startswith("- "):
            if cur is None:
                raise ValueError("mục danh sách không có khóa: %s" % raw)
            cur.append(json.loads(stripped[2:].strip()))
            continue
        m = re.match(r"^(\w+):\s*(.*)$", raw)
        if m:
            k, v = m.group(1), m.group(2).strip()
            cur = None
            if k == "mong_doi" and v == "":
                continue
            if v == "":
                root[k] = []
                cur = root[k]
            else:
                root[k] = _yaml_val(v)
            continue
        m = re.match(r"^  (\w+):\s*(.*)$", raw)
        if m:
            k, v = m.group(1), m.group(2).strip()
            if v == "":
                mong[k] = []
                cur = mong[k]
            else:
                mong[k] = _yaml_val(v)
                cur = None
            continue
        raise ValueError("không đọc được dòng YAML: %s" % raw)
    root["mong_doi"] = mong
    return root


def _case_chuan(slug, n, title, body, lesson_id, dau_vao):
    return {
        "id": "%s-%03d-chuan" % (slug, n),
        "skill": slug,
        "loai": "chuan",
        "mo_ta": title,
        "dau_vao": dau_vao,
        "phai_co": [title] if title else [],
        "khong_duoc_co": [],
        "hanh_vi": body.strip(),
        "can_cu": ["bài học #%d trong sổ (dữ liệu giả lập khi sinh đề)" % lesson_id],
        "nguoi_duyet": "",
    }


def _case_bay(slug, n):
    return {
        "id": "%s-%03d-bay" % (slug, n),
        "skill": slug,
        "loai": "bay",
        "mo_ta": "Tình huống giả lập nằm ngoài phạm vi",
        "dau_vao": "Tình huống giả lập: người dùng hỏi thời tiết hôm nay. Không có việc thuộc skill này.",
        "phai_co": [],
        "khong_duoc_co": [],
        "hanh_vi": "Không áp dụng skill. Nói rõ yêu cầu nằm ngoài phạm vi, không bịa bước và không bịa số liệu.",
        "can_cu": ["bẫy gần đúng — skill không được kích hoạt"],
        "nguoi_duyet": "",
    }


def skill_propose(L, root, slug, title, problem, lesson_ids=None, query=None, force=False):
    slug = slugify(slug)
    ids = list(lesson_ids or [])
    if query:
        ids += [r["id"] for r in L.search(query, limit=10) if r["id"] not in ids]
    if not ids:
        raise SystemExit("chưa chọn bài học (--lessons hoặc --query)")
    rows = [L.get(i) for i in ids]
    for r in rows:
        cam_bi_mat(r["title"], "tiêu đề bài #%d" % r["id"])
        cam_bi_mat(r["body"], "nội dung bài #%d" % r["id"])
    sens = sorted({r["sensitivity"] for r in rows} - {"none"})
    root_prop = os.path.abspath(os.path.join(root, "proposals"))
    d = os.path.abspath(os.path.join(root_prop, slug))
    if not d.startswith(root_prop + os.sep):
        raise SystemExit("slug không hợp lệ")
    if os.path.exists(d) and not force:
        raise SystemExit("%s đã có (thêm --force để ghi đè bản nháp)" % d)
    os.makedirs(os.path.join(d, "evals"), exist_ok=True)
    for fn in os.listdir(os.path.join(d, "evals")):
        if fn.endswith((".yaml", ".yml")):
            os.remove(os.path.join(d, "evals", fn))
    desc = (title or rows[0]["title"]).replace("\n", " ")
    skill = ["---", "name: %s" % slug, "description: %s" % _q(desc), "---", "",
             "# %s" % desc, "", "## Khi nào dùng", "", problem.strip(), "", "## Các bước", ""]
    for n, r in enumerate(rows, 1):
        skill.append("%d. %s — %s" % (n, r["title"], r["body"].strip().replace("\n", " ")))
    skill += ["", "## Chặn", "",
              "- Đụng người khác, tiền, dữ liệu nhạy, hoặc việc vốn bị cấm: dừng, hỏi Dat và Quân.",
              "- Không ghi dữ liệu khách, email, số điện thoại, token vào sổ hay vào repo.",
              "- Khi skill sai hoặc bị sửa, ghi một bài học kèm bằng chứng vào sổ."]
    refs, lessons_md = [], []
    for r in rows:
        ev = L.evidence(r["id"])
        lessons_md.append("- #%d **%s** (%s/%s, conf %.2f, sens %s, bot %s, skill %s): %s" % (
            r["id"], r["title"], r["tier"], r["status"], r["confidence"], r["sensitivity"], r["bot"],
            r["skill"] or "-", r["body"].strip().replace("\n", " ")))
        refs += ["- #%d E%d %s" % (r["id"], e["id"], cite(e)) for e in ev]
    if sens:
        duyet = ("BẮT BUỘC: bài học có sensitivity %s. Cần duyệt của cả Dat và Quân trước khi cài. "
                 "Bản này là nháp, không sửa skill đang chạy." % ", ".join(sens))
    else:
        duyet = "Không có bài sensitivity khác none. Vẫn là nháp: báo Dat và Quân trước khi cài. Không sửa skill đang chạy."
    md = ["# Đề xuất skill: %s" % slug, "",
          "_Tạo %s bởi %s. Trạng thái: nháp — chưa cài._" % (now(), L.actor), "",
          "## Vấn đề", "", problem.strip(), "",
          "## Bài học dẫn chứng", ""] + lessons_md + ["",
          "## SKILL.md đề xuất", "", "```markdown"] + skill + ["```", "",
          "## Tham chiếu", ""] + (refs or ["- (chưa có bằng chứng — thêm trước khi nhận)"]) + ["",
          "## Duyệt", "", duyet, "",
          "Máy chấm cần mỗi skill ≥ 3 tình huống và ≥ 1 bẫy. File trong `evals/` là dữ liệu giả lập sinh từ bài học; người duyệt đọc lại trước khi đưa sang repo skill.", ""]
    with open(os.path.join(d, "PROPOSAL.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))
    with open(os.path.join(d, "SKILL.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(skill) + "\n")
    cases = []
    n = 1
    for r in rows:
        cases.append(_case_chuan(
            slug, n, r["title"], r["body"], r["id"],
            "Tình huống giả lập cần áp dụng quy tắc: %s" % r["title"]))
        n += 1
    if len(cases) < 2:
        cases.append(_case_chuan(
            slug, n, rows[0]["title"], rows[0]["body"], rows[0]["id"],
            "Tình huống giả lập khác, cùng quy tắc: %s. Mọi dữ liệu đều là giả." % rows[0]["title"]))
        n += 1
    cases.append(_case_bay(slug, n))
    for case in cases:
        dump_eval(case, os.path.join(d, "evals", "%s.yaml" % case["id"]))
    L.audit("skill_propose", None, slug=slug, lessons=ids, dir=d, cases=len(cases))
    L.db.commit()
    return d, ids


def skill_eval(L, root, slug, responses=None):
    d = os.path.join(root, "proposals", slugify(slug))
    errs, warns, cases = [], [], []
    p = os.path.join(d, "PROPOSAL.md")
    if not os.path.isfile(p):
        errs.append("thiếu PROPOSAL.md")
    else:
        txt = open(p, encoding="utf-8").read()
        errs += ["PROPOSAL.md thiếu mục %r" % s for s in PROPOSAL_SECTIONS if s not in txt]
        for lid in set(int(x) for x in re.findall(r"^- #(\d+) \*\*", txt, re.M)):
            if not L.db.execute("SELECT 1 FROM lessons WHERE id=?", (lid,)).fetchone():
                warns.append("bài #%d được dẫn nhưng không có trong sổ này" % lid)
    s = os.path.join(d, "SKILL.md")
    if os.path.isfile(s):
        head = open(s, encoding="utf-8").read()
        if not re.match(r"^---\nname: \S+\ndescription: .+\n---\n", head):
            errs.append("SKILL.md cần frontmatter name và description")
    else:
        warns.append("không có SKILL.md riêng (nháp chỉ nằm trong PROPOSAL.md)")
    paths = sorted(glob.glob(os.path.join(d, "evals", "*.yaml")) + glob.glob(os.path.join(d, "evals", "*.yml")))
    if not paths:
        errs.append("thiếu evals/*.yaml")
    else:
        for path in paths:
            try:
                data = parse_eval_yaml(open(path, encoding="utf-8").read())
            except (ValueError, json.JSONDecodeError) as ex:
                errs.append("%s: YAML không đọc được (%s)" % (os.path.basename(path), ex))
                continue
            if not data.get("id") or not str(data.get("dau_vao") or "").strip():
                errs.append("%s: cần id và dau_vao" % os.path.basename(path))
            mong = data.get("mong_doi") or {}
            loai = str(data.get("loai") or "")
            if loai not in ("chuan", "bay"):
                errs.append("%s: loai phải là chuan hoặc bay" % os.path.basename(path))
            phai = mong.get("phai_co") or []
            hanh = str(mong.get("hanh_vi") or "").strip()
            if not isinstance(phai, list):
                errs.append("%s: phai_co phải là danh sách" % os.path.basename(path))
                phai = []
            cases.append({
                "id": data.get("id"), "loai": loai, "dau_vao": data.get("dau_vao") or "",
                "phai_co": phai, "hanh_vi": hanh,
                "_has_expected": bool(hanh or phai),
            })
        if not cases:
            errs.append("evals không có tình huống")
        if not any(c["loai"] == "bay" for c in cases):
            warns.append("chưa có tình huống bẫy (loai: bay)")
        if len(cases) < 3:
            warns.append("mới %d tình huống (chuẩn ≥ 3)" % len(cases))
    graded = {}
    if responses:
        resp = {}
        for line in open(responses, encoding="utf-8"):
            if line.strip():
                j = json.loads(line)
                resp[j["id"]] = j.get("output", "")
        for c in cases:
            if c["id"] not in resp:
                continue
            if c.get("phai_co"):
                out = set(tokens(resp[c["id"]]))
                miss = []
                for phrase in c["phai_co"]:
                    need = tokens(phrase)
                    if need and not set(need) <= out:
                        miss.append(phrase)
                graded[c["id"]] = "pass" if not miss else "fail"
            else:
                graded[c["id"]] = "needs human/LLM judge (no phai_co)"
    L.audit("skill_eval", None, slug=slug, errors=len(errs), cases=len(cases))
    L.db.commit()
    return {"dir": d, "ok": not errs, "errors": errs, "warnings": warns,
            "cases": [{"id": c.get("id"), "loai": c.get("loai"), "has_expected": c["_has_expected"]} for c in cases],
            "graded": graded}


CSV_FIELDS = ["uid", "bot", "title", "body", "tags", "tier", "confidence", "sensitivity", "status",
              "owner_approval", "approvers", "skill", "repo", "nen_tang", "nhan_loi", "tenant",
              "giup", "hai", "playbook_ma", "created_at", "updated_at", "evidence_json"]


def export_csv(L, path):
    rows = L.db.execute("SELECT * FROM lessons ORDER BY id").fetchall()
    fh = sys.stdout if path == "-" else open(path, "w", newline="", encoding="utf-8")
    w = csv.DictWriter(fh, fieldnames=CSV_FIELDS)
    w.writeheader()
    for r in rows:
        d = {k: r[k] for k in CSV_FIELDS if k != "evidence_json"}
        d["evidence_json"] = json.dumps([[e["kind"], e["ref"], e["note"]] for e in L.evidence(r["id"])], ensure_ascii=False)
        w.writerow(d)
    if fh is not sys.stdout:
        fh.close()
    L.audit("export_csv", None, path=path, rows=len(rows))
    L.db.commit()
    return len(rows)


def import_csv(L, path):
    added = skipped = 0
    with open(path, newline="", encoding="utf-8") as fh:
        for d in csv.DictReader(fh):
            if d.get("uid") and L.db.execute("SELECT 1 FROM lessons WHERE uid=?", (d["uid"],)).fetchone():
                skipped += 1
                continue
            ev = [tuple(x) for x in json.loads(d.get("evidence_json") or "[]")]
            approval = d.get("owner_approval") or None
            if not approval and d.get("approvers"):
                approval = d.get("approvers")
            L.add(d["bot"], d["title"], d["body"], d.get("tags", ""), d.get("tier") or "scratch", ev,
                  float(d.get("confidence") or 0.5), d.get("sensitivity") or "none", d.get("status") or "proposed",
                  uid=d.get("uid") or None, created_at=d.get("created_at") or None,
                  updated_at=d.get("updated_at") or None, owner_approval=approval, skill=d.get("skill") or "",
                  repo=d.get("repo") or "", nen_tang=d.get("nen_tang") or "", nhan_loi=d.get("nhan_loi") or "",
                  tenant=d.get("tenant") or "", giup=int(d.get("giup") or 0), hai=int(d.get("hai") or 0),
                  playbook_ma=d.get("playbook_ma") or None, log=False)
            added += 1
    L.audit("import_csv", None, path=path, added=added, skipped=skipped)
    L.db.commit()
    return added, skipped


def assert_not_skill_file(path):
    base = os.path.basename(os.path.abspath(path)).lower()
    if base in {"skill.md", "agents.md"}:
        raise SystemExit("từ chối ghi %s — lệnh này chỉ thêm dòng playbook, không viết lại skill" % base)


def next_playbook_index(text):
    nums = [int(n) for n in re.findall(r"\[P(\d+)\]", text or "")]
    return (max(nums) + 1) if nums else 1


def playbook_header(skill):
    return ("# Playbook — %s\n<!-- Chỉ thêm dòng mới. Không viết lại dòng cũ. "
            "Bộ đếm cập nhật sau mỗi lần chấm. -->\n" % skill)


def playbook_export(L, skill, out_path, lesson_id=None):
    skill = check_skill(skill, L.catalog)
    if not skill:
        raise SystemExit("playbook export cần --skill đúng tên trong danh-muc/skills.yaml")
    assert_not_skill_file(out_path)
    if lesson_id:
        r = L.get(lesson_id)
        if r["skill"] != skill:
            raise SystemExit("bài #%d không thuộc skill %s" % (r["id"], skill))
        if r["tier"] != "durable" or r["status"] != "accepted":
            raise SystemExit("chỉ xuất bài durable đã accepted")
        if r["playbook_ma"]:
            raise SystemExit("bài #%d đã xuất thành %s" % (r["id"], r["playbook_ma"]))
    else:
        r = L.db.execute(
            """SELECT * FROM lessons WHERE skill=? AND tier='durable' AND status='accepted'
               AND (playbook_ma IS NULL OR playbook_ma='')
               ORDER BY confidence DESC, id ASC LIMIT 1""", (skill,)).fetchone()
        if not r:
            raise SystemExit("không có bài durable đã accepted chưa xuất cho skill %s" % skill)
    title = " ".join((r["title"] or "").split())
    existed = os.path.exists(out_path)
    prev = ""
    if existed:
        with open(out_path, encoding="utf-8") as fh:
            prev = fh.read()
    else:
        parent = os.path.dirname(os.path.abspath(out_path))
        if parent:
            os.makedirs(parent, exist_ok=True)
    ma = "P%02d" % next_playbook_index(prev)
    line = "- [%s] %s (giúp: %d, hại: %d)\n" % (ma, title, r["giup"], r["hai"])
    cam_bi_mat(line, "dòng playbook")
    if existed:
        with open(out_path, "a", encoding="utf-8") as fh:
            if prev and not prev.endswith("\n"):
                fh.write("\n")
            fh.write(line)
    else:
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(playbook_header(skill))
            fh.write(line)
    L.set_fields(r["id"], "playbook_export", playbook_ma=ma)
    return r["id"], ma, out_path, line


def _add_filters(sql, args_list, pairs):
    for col, val in pairs:
        if val:
            sql += " AND %s=?" % col
            args_list.append(val)
    return sql


def main(argv=None):
    ap = argparse.ArgumentParser(prog="ledger.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--root", default=DEFAULT_ROOT, help="thư mục chứa wiki/, staging/, proposals/")
    ap.add_argument("--catalog", default=DEFAULT_CATALOG, help="đường dẫn danh-muc/skills.yaml")
    ap.add_argument("--actor", default=os.environ.get("SELF_EVO_ACTOR") or os.environ.get("USER") or "unknown")
    ap.add_argument("--json", action="store_true")
    sp = ap.add_subparsers(dest="cmd", required=True)

    a = sp.add_parser("add", help="thêm bài học")
    a.add_argument("--bot", required=True)
    a.add_argument("--title", required=True)
    a.add_argument("--text", required=True, help="nội dung ('-' = stdin)")
    a.add_argument("--tags", default="")
    a.add_argument("--tier", default="scratch", choices=TIERS)
    a.add_argument("--evidence", "-e", action="append", default=[],
                   help="lặp: transcript:<id> | file:<đường dẫn> | url:<url> | quote:<câu>")
    a.add_argument("--confidence", type=float, default=0.5)
    a.add_argument("--sensitivity", default="none", choices=SENS)
    a.add_argument("--status", default="proposed", choices=STATUSES)
    a.add_argument("--owner-approved", action="append", default=None,
                   help="lặp lại: một mệnh đề duyệt. Bài nhạy cần cả Dat và Quân")
    a.add_argument("--skill", default="", help="tên trong danh-muc/skills.yaml; để trống nếu không gắn skill")
    a.add_argument("--repo", default="")
    a.add_argument("--nen-tang", default="")
    a.add_argument("--nhan-loi", default="")
    a.add_argument("--tenant", default="")
    a.add_argument("--giup", type=int, default=0)
    a.add_argument("--hai", type=int, default=0)

    s = sp.add_parser("search", help="tìm BM25, không phân biệt dấu")
    s.add_argument("query")
    s.add_argument("--bot")
    s.add_argument("--tag")
    s.add_argument("--tier", choices=TIERS)
    s.add_argument("--status", choices=STATUSES)
    s.add_argument("--skill")
    s.add_argument("--repo")
    s.add_argument("--nen-tang")
    s.add_argument("--nhan-loi")
    s.add_argument("--tenant")
    s.add_argument("--limit", type=int, default=10)
    s.add_argument("--all-terms", action="store_true")
    s.add_argument("--include-retired", action="store_true")
    s.add_argument("--evidence", action="store_true")

    sh = sp.add_parser("show")
    sh.add_argument("id", type=int)
    ls = sp.add_parser("list")
    ls.add_argument("--bot")
    ls.add_argument("--tier", choices=TIERS)
    ls.add_argument("--status", choices=STATUSES)
    ls.add_argument("--tag")
    ls.add_argument("--skill")
    ls.add_argument("--nen-tang")
    ls.add_argument("--nhan-loi")
    ls.add_argument("--tenant")
    ls.add_argument("--limit", type=int, default=50)

    ev = sp.add_parser("evidence").add_subparsers(dest="evcmd", required=True)
    ea = ev.add_parser("add")
    ea.add_argument("id", type=int)
    ea.add_argument("ref")
    ea.add_argument("--note")
    el = ev.add_parser("list")
    el.add_argument("id", type=int)

    p = sp.add_parser("promote")
    p.add_argument("id", type=int)
    p.add_argument("--owner-approved", action="append", default=None)
    sp.add_parser("demote").add_argument("id", type=int)
    r = sp.add_parser("retire")
    r.add_argument("id", type=int)
    r.add_argument("--reason", default="")
    ac = sp.add_parser("accept")
    ac.add_argument("id", type=int)
    ac.add_argument("--owner-approved", action="append", default=None)
    u = sp.add_parser("update", help="sửa trường")
    u.add_argument("id", type=int)
    u.add_argument("--title")
    u.add_argument("--text")
    u.add_argument("--tags")
    u.add_argument("--confidence", type=float)
    u.add_argument("--sensitivity", choices=SENS)
    u.add_argument("--skill")
    u.add_argument("--repo")
    u.add_argument("--nen-tang")
    u.add_argument("--nhan-loi")
    u.add_argument("--tenant")
    u.add_argument("--giup", type=int)
    u.add_argument("--hai", type=int)
    sp.add_parser("used").add_argument("id", type=int)

    rv = sp.add_parser("review")
    rv.add_argument("--since", type=float, default=3)
    rv.add_argument("--stale-days", type=float, default=30)
    rv.add_argument("--low-conf", type=float, default=0.5)

    ex = sp.add_parser("export-csv")
    ex.add_argument("path", nargs="?", default="-")
    im = sp.add_parser("import-csv")
    im.add_argument("path")
    w = sp.add_parser("wiki").add_subparsers(dest="wcmd", required=True)
    wb = w.add_parser("build")
    wb.add_argument("--out")
    wb.add_argument("--include-sensitive", action="store_true")
    sk = sp.add_parser("skill").add_subparsers(dest="scmd", required=True)
    pp = sk.add_parser("propose")
    pp.add_argument("slug")
    pp.add_argument("--title", default="")
    pp.add_argument("--problem", required=True)
    pp.add_argument("--lessons", default="")
    pp.add_argument("--query")
    pp.add_argument("--force", action="store_true")
    pe = sk.add_parser("eval")
    pe.add_argument("slug")
    pe.add_argument("--responses")
    pb = sp.add_parser("playbook").add_subparsers(dest="pbcmd", required=True)
    px = pb.add_parser("export", help="thêm một dòng [Pnn] từ bài durable đã accepted")
    px.add_argument("--skill", required=True)
    px.add_argument("--out", help="file playbook.md; mặc định staging/playbook-<skill>.md")
    px.add_argument("--lesson", type=int, help="một bài cụ thể")
    au = sp.add_parser("audit")
    au.add_argument("--id", type=int)
    au.add_argument("--limit", type=int, default=30)

    args = ap.parse_args(argv)
    L = Ledger(args.db, args.actor, args.catalog)
    c = args.cmd

    if c == "add":
        text = sys.stdin.read() if args.text == "-" else args.text
        lid = L.add(args.bot, args.title, text, args.tags, args.tier, args.evidence, args.confidence,
                    args.sensitivity, args.status, owner_approval=args.owner_approved, skill=args.skill,
                    repo=args.repo, nen_tang=args.nen_tang, nhan_loi=args.nhan_loi, tenant=args.tenant,
                    giup=args.giup, hai=args.hai)
        emit(args, {"id": lid}, "đã thêm bài #%d" % lid)
    elif c == "search":
        rs = L.search(args.query, args.bot, args.tag, args.tier, args.status, args.limit,
                      "and" if args.all_terms else "or", args.include_retired, args.skill, args.repo,
                      args.nen_tang, args.nhan_loi, args.tenant)
        emit(args, [dict(rowd(x), evidence=[rowd(e) for e in L.evidence(x["id"])]) for x in rs],
             "\n".join(fmt(x, L.evidence(x["id"]) if args.evidence else None, x["score"]) for x in rs) or "(không khớp)")
    elif c == "show":
        x = L.get(args.id)
        emit(args, dict(rowd(x), evidence=[rowd(e) for e in L.evidence(x["id"])]), fmt(x, L.evidence(x["id"])))
    elif c == "list":
        sql, a2 = "SELECT * FROM lessons WHERE 1", []
        sql = _add_filters(sql, a2, (("bot", args.bot), ("tier", args.tier), ("status", args.status),
                                     ("skill", args.skill), ("nen_tang", args.nen_tang),
                                     ("nhan_loi", args.nhan_loi), ("tenant", args.tenant)))
        if args.tag:
            sql += " AND (','||tags||',') LIKE ?"
            a2.append("%%,%s,%%" % norm_tags(args.tag))
        rs = L.db.execute(sql + " ORDER BY updated_at DESC LIMIT ?", a2 + [args.limit]).fetchall()
        emit(args, [rowd(x) for x in rs], "\n".join(fmt(x) for x in rs) or "(trống)")
    elif c == "evidence":
        if args.evcmd == "add":
            L.add_evidence(args.id, args.ref, args.note)
            print("đã thêm bằng chứng cho #%d" % args.id)
        else:
            es = L.evidence(args.id)
            emit(args, [rowd(e) for e in es], "\n".join(
                "E%d %s: %s%s  (bởi %s, %s)" % (
                    e["id"], e["kind"], e["ref"], " — " + e["note"] if e["note"] else "", e["added_by"], e["added_at"])
                for e in es) or "(không có bằng chứng)")
    elif c == "promote":
        print("#%d -> %s" % (args.id, L.promote(args.id, args.owner_approved)))
    elif c == "demote":
        print("#%d -> %s" % (args.id, L.demote(args.id)))
    elif c == "retire":
        L.set_fields(args.id, "retire", status="retired")
        L.audit("retire_reason", args.id, reason=args.reason)
        L.db.commit()
        print("#%d đã retire" % args.id)
    elif c == "accept":
        L.accept(args.id, args.owner_approved)
        print("#%d đã accepted" % args.id)
    elif c == "update":
        x = L.get(args.id)
        f = {}
        if args.title is not None:
            cam_bi_mat(args.title, "tiêu đề")
            f["title"] = args.title
        if args.text is not None:
            cam_bi_mat(args.text, "nội dung")
            f["body"] = args.text
        if args.tags is not None:
            cam_bi_mat(args.tags, "tag")
            f["tags"] = norm_tags(args.tags)
        if args.confidence is not None:
            if not 0 <= args.confidence <= 1:
                raise SystemExit("confidence phải trong khoảng 0..1")
            f["confidence"] = args.confidence
        if args.sensitivity is not None:
            f["sensitivity"] = args.sensitivity
        if args.skill is not None:
            f["skill"] = check_skill(args.skill, L.catalog)
        if args.repo is not None:
            cam_bi_mat(args.repo, "repo")
            f["repo"] = args.repo.strip()
        if args.nen_tang is not None:
            f["nen_tang"] = check_enum(args.nen_tang, NEN_TANG, "nen_tang")
        if args.nhan_loi is not None:
            f["nhan_loi"] = check_enum(args.nhan_loi, NHAN_LOI, "nhan_loi")
        if args.tenant is not None:
            cam_bi_mat(args.tenant, "tenant")
            f["tenant"] = args.tenant.strip()
        if args.giup is not None:
            f["giup"] = check_count("giup", args.giup)
        if args.hai is not None:
            f["hai"] = check_count("hai", args.hai)
        if not f:
            raise SystemExit("không có gì để sửa")
        keys = approval_state(x["owner_approval"])[1]
        L._gate(f.get("sensitivity", x["sensitivity"]), x["tier"], x["status"], keys)
        L.set_fields(args.id, "update", **f)
        print("#%d đã sửa" % args.id)
    elif c == "used":
        L.get(args.id)
        L.db.execute("UPDATE lessons SET last_used_at=? WHERE id=?", (now(), args.id))
        L.audit("used", args.id)
        L.db.commit()
        print("#%d đã đánh dấu dùng" % args.id)
    elif c == "review":
        cut = (now_dt() - timedelta(days=args.since)).isoformat(timespec="seconds")
        stale_cut = (now_dt() - timedelta(days=args.stale_days)).isoformat(timespec="seconds")
        q = lambda sql, *a: L.db.execute(sql, a).fetchall()
        recent = q("SELECT * FROM lessons WHERE created_at>=? OR updated_at>=? ORDER BY updated_at DESC", cut, cut)
        stale = q("SELECT * FROM lessons WHERE status!='retired' AND tier!='scratch' AND updated_at<? "
                  "AND (last_used_at IS NULL OR last_used_at<?)", stale_cut, stale_cut)
        old_scratch = q("SELECT * FROM lessons WHERE status!='retired' AND tier='scratch' AND created_at<?", stale_cut)
        low = q("SELECT * FROM lessons WHERE status!='retired' AND confidence<?", args.low_conf)
        noev = q("SELECT * FROM lessons l WHERE status!='retired' AND NOT EXISTS(SELECT 1 FROM evidence e WHERE e.lesson_id=l.id)")
        needs_owner = q("SELECT * FROM lessons WHERE status!='retired' AND sensitivity!='none' AND status!='accepted'")
        dups = L.duplicates()
        data = {"since_days": args.since, "recent": [rowd(x) for x in recent],
                "stale": [rowd(x) for x in stale + old_scratch],
                "low_confidence": [rowd(x) for x in low], "no_evidence": [rowd(x) for x in noev],
                "needs_owner_approval": [rowd(x) for x in needs_owner],
                "duplicates": [{"a": a_, "b": b_, "jaccard": j, "bm25_ratio": rt} for a_, b_, j, rt in dups]}

        def sec(name, rs):
            return ["== %s (%d)" % (name, len(rs))] + [
                "  #%d [%s/%s] %s (conf %.2f, %s, duyệt %s)" % (
                    x["id"], x["tier"], x["status"], x["title"], x["confidence"], x["bot"], x["approvers"] or "-")
                for x in rs]
        txt = (sec("thêm/sửa trong %g ngày" % args.since, recent)
               + sec("cũ (> %g ngày, không dùng)" % args.stale_days, stale + old_scratch)
               + sec("confidence thấp (< %g)" % args.low_conf, low)
               + sec("chưa có bằng chứng", noev)
               + sec("nhạy và chưa accepted: cần cả Dat và Quân", needs_owner)
               + ["== nghi trùng (%d)" % len(dups)]
               + ["  #%d ~ #%d  jaccard=%.2f bm25_ratio=%.2f" % d for d in dups])
        emit(args, data, "\n".join(txt))
        L.audit("review", None, since=args.since, duplicates=len(dups))
        L.db.commit()
    elif c == "export-csv":
        n = export_csv(L, args.path)
        if args.path != "-":
            print("đã xuất %d bài ra %s" % (n, args.path))
    elif c == "import-csv":
        print("đã nhập %d, bỏ qua %d bản đã có (theo uid)" % import_csv(L, args.path))
    elif c == "wiki":
        out = args.out or os.path.join(args.root, "wiki")
        pages, skipped = wiki_build(L, out, args.include_sensitive)
        print("wiki: %d trang trong %s%s" % (len(pages), out, (", ẩn %d bài sensitive" % skipped) if skipped else ""))
    elif c == "skill":
        if args.scmd == "propose":
            ids = [int(x) for x in args.lessons.split(",") if x.strip()]
            d, ids = skill_propose(L, args.root, args.slug, args.title, args.problem, ids, args.query, args.force)
            emit(args, {"dir": d, "lessons": ids}, "đã ghi đề xuất: %s (bài %s)" % (d, ",".join(map(str, ids))))
        else:
            res = skill_eval(L, args.root, args.slug, args.responses)
            if args.json:
                emit(args, res, "")
            else:
                print("eval %s: %s" % (res["dir"], "OK" if res["ok"] else "FAIL"))
                for e in res["errors"]:
                    print("  LỖI", e)
                for wn in res["warnings"]:
                    print("  cảnh báo", wn)
                for cc in res["cases"]:
                    print("  %-16s %s expected: %s%s" % (
                        cc["id"], cc.get("loai") or "-", "có" if cc["has_expected"] else "THIẾU",
                        ("  chấm: " + res["graded"][cc["id"]]) if cc["id"] in res["graded"] else ""))
            if not res["ok"]:
                sys.exit(1)
    elif c == "playbook":
        out = args.out or os.path.join(args.root, "staging", "playbook-%s.md" % slugify(args.skill))
        lid, ma, path, line = playbook_export(L, args.skill, out, args.lesson)
        emit(args, {"lesson": lid, "ma": ma, "path": path, "line": line.rstrip("\n")},
             "đã thêm [%s] từ bài #%d vào %s" % (ma, lid, path))
    elif c == "audit":
        sql, a2 = "SELECT * FROM audit", []
        if args.id:
            sql += " WHERE lesson_id=?"
            a2.append(args.id)
        rs = L.db.execute(sql + " ORDER BY id DESC LIMIT ?", a2 + [args.limit]).fetchall()
        emit(args, [rowd(x) for x in rs], "\n".join(
            "%s %-10s %-16s #%s %s" % (x["ts"], x["actor"], x["action"], x["lesson_id"] or "-", x["details"])
            for x in rs) or "(trống)")


if __name__ == "__main__":
    main()
