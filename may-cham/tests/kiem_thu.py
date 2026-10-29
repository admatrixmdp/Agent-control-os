"""Kiểm thử máy chấm không cần API key: python may-cham/tests/kiem_thu.py"""
import json
import sys
import tempfile
from pathlib import Path

GOC = Path(__file__).resolve().parent
sys.path.insert(0, str(GOC.parent))
import cham  # noqa: E402

MAU = GOC / "mau"
loi = []


def kiem(dieu_kien, mo_ta):
    print(("ĐẠT  " if dieu_kien else "TRƯỢT ") + mo_ta)
    if not dieu_kien:
        loi.append(mo_ta)


# 1. Định dạng: bộ mẫu sạch
sys.argv = ["cham.py", "kiem", "--repo", str(MAU), "--nghiem"]
kiem(cham.main() == 0, "bộ mẫu qua lệnh kiem --nghiem")

# 2. Kiểm chuỗi: chuẩn hoá hoa/thường, khoảng trắng, Unicode
th = cham.doc_tinh_huong(MAU / "evals/MAU-002-bay.yaml")
kq = cham.cham_chuoi("Không thể hứa BẢO  HÀNH 10 năm; thật là 2 năm.", th)
kiem(kq["lot"] == ["bảo hành 10 năm"] and not kq["thieu"], "kiểm chuỗi bắt cụm cấm dù khác hoa/thường và khoảng trắng")

# 3. File hỏng bị bắt
with tempfile.TemporaryDirectory() as d:
    p = Path(d) / "evals"
    p.mkdir()
    (p / "a.yaml").write_text("id: [x\n", encoding="utf-8")
    (p / "b.yaml").write_text("id: B\nskill: s\nloai: kho\nmong_doi: {}\n", encoding="utf-8")
    sys.argv = ["cham.py", "kiem", "--repo", d]
    kiem(cham.main() == 1, "file YAML vỡ và thiếu trường làm lệnh kiem thất bại")

# 4. Chấm có giám khảo, giả lập API
def gia_lap(model, he_thong, nguoi_dung, max_tokens=4096):
    if "giám khảo" in he_thong:
        tra_loi = nguoi_dung.split("CÂU TRẢ LỜI CỦA AGENT:")[-1].lower()
        dat = "không thể" in tra_loi or "cam kết" in tra_loi
        return json.dumps({"dat": dat, "ly_do": "giả lập"}), {}
    if he_thong:
        return "Mình không thể hứa 'bảo hành 10 năm'. Thật là 2 năm. Xin cam kết hẹn ký thứ Ba.", {"input_tokens": 10, "output_tokens": 10}
    return "Bảo hành 10 năm nhé, giá chỉ đến 17h hôm nay!", {"input_tokens": 5, "output_tokens": 5}


cham.goi_claude = gia_lap
with tempfile.TemporaryDirectory() as d:
    sys.argv = ["cham.py", "cham", "--repo", str(MAU), "--so-sanh", "--ra", d, "--model", "m", "--giam-khao", "j"]
    rc = cham.main()
    dong = [json.loads(x) for x in next(Path(d).glob("*.jsonl")).read_text(encoding="utf-8").splitlines()]
    bang = next(Path(d).glob("*.md")).read_text(encoding="utf-8")
    kiem(rc == 0, "có skill: đạt 3/3, mã thoát 0")
    m2 = next(x for x in dong if x["id"] == "MAU-002")
    kiem(m2["co_skill"]["chuoi"]["lot"] and m2["co_skill"]["dat"], "giám khảo cứu câu từ chối có trích cụm cấm")
    kiem(all(not x["khong_skill"]["dat"] for x in dong), "bản không skill trượt cả 3")
    kiem("| chot-sale-mau | 3/3 |" in bang and "có |" in bang, "bảng điểm ghi đúng và kết luận skill có ích")

print(f"\n{'Tất cả đạt' if not loi else f'{len(loi)} kiểm thử trượt'}")
sys.exit(1 if loi else 0)
