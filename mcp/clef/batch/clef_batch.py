"""Gọi cổng Clef theo lô: <=64 câu/lần, cache, trần số lần gọi, fallback. Chỉ dùng thư viện chuẩn."""
import hashlib
import json
import urllib.request

MAX_CAU = 64


class LoQuaLon(ValueError):
    """Lô > 64 câu: từ chối trước khi gửi."""


def khoa_cache(text, context_version, qset_version, model):
    return hashlib.sha256(f"{text}|{context_version}|{qset_version}|{model}".encode()).hexdigest()


def gui_http(url, caller, secret, timeout=10.0):
    """Trả hàm send(payload) -> dict gọi POST {url}/v1/systemone. secret lấy từ biến môi trường của bên gọi."""
    def send(payload):
        req = urllib.request.Request(
            url.rstrip("/") + "/v1/systemone",
            data=json.dumps(payload).encode(),
            headers={"content-type": "application/json", "x-caller": caller, "authorization": f"Bearer {secret}"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read())
    return send


def goi_mot_lo(send, questions, state, model, context_version, qset_version):
    if len(questions) > MAX_CAU:
        raise LoQuaLon(f"{len(questions)} cau > {MAX_CAU}")
    return send({"model": model, "state": state, "questions": questions,
                 "context_version": context_version, "qset_version": qset_version})


def quyet_dinh(questions, send, *, state=None, model="clef", context_version="0", qset_version="0",
               cache=None, max_calls=10):
    """questions: {id: {type, instructions, criteria?}}. Trả {id: answer|None}, fallback=True nếu có câu không trả lời được."""
    cache = {} if cache is None else cache
    state = state or {}
    st = json.dumps(state, sort_keys=True, ensure_ascii=False)
    ket_qua, can_hoi, khoa = {}, {}, {}
    for qid, q in questions.items():
        k = khoa_cache(st + json.dumps(q, sort_keys=True, ensure_ascii=False), context_version, qset_version, model)
        khoa[qid] = k
        if k in cache:
            ket_qua[qid] = cache[k]
        else:
            can_hoi[qid] = q
    ids = list(can_hoi)
    so_lan, loi = 0, []
    for i in range(0, len(ids), MAX_CAU):
        phan = {q: can_hoi[q] for q in ids[i:i + MAX_CAU]}
        if so_lan >= max_calls:
            loi.append("het-luot-goi")
            ket_qua.update(dict.fromkeys(phan))
            continue
        so_lan += 1
        try:
            r = goi_mot_lo(send, phan, state, model, context_version, qset_version)
        except Exception as e:  # mất mạng, timeout, HTTP lỗi: không chặn bên gọi
            r = {"fallback": True, "reason": type(e).__name__}
        if r.get("fallback") or not r.get("answers"):
            loi.append(r.get("reason", "fallback"))
            ket_qua.update(dict.fromkeys(phan))
            continue
        for qid in phan:
            a = r["answers"].get(qid)
            ket_qua[qid] = a
            if a is not None:
                cache[khoa[qid]] = a
    return {"answers": ket_qua, "fallback": bool(loi), "reasons": loi, "calls": so_lan}
