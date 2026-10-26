# Kho lưu trữ skill đã xử lý

Nơi ghi lại mọi skill bên ngoài **đã xử lý xong**, để không ai nghiên cứu lại và để còn lý do khi muốn thử lại với mô hình mới.

## Không dời file gốc

`raw/` là bất biến (`DECISIONS.md`, 2026-10-26). Lưu trữ **không** dời hay xoá `SKILL.md` gốc. Lưu trữ gồm hai thứ:

1. Dòng `trang_thai: luu-tru` trong `skill-lab/trang-thai.yaml` — sổ duy nhất.
2. Một phiếu `luu-tru/<ten-skill>.yaml` ghi lý do, điểm, phần đã lấy.

`scripts/phan_tich.py` đọc sổ trạng thái và bỏ qua skill đã lưu trữ khi chạy lại bước 1–3.

## Vòng đời

| Trạng thái | Nghĩa | Điều kiện chuyển tiếp |
|---|---|---|
| `chua-xu-ly` | Mới nhập kho (mặc định, không cần ghi vào sổ) | Được chọn vào một lô thử |
| `dang-thu` | Đang trong một lô thử nghiệm | Có kết quả chấm |
| `cho-gop` | Đạt một phần, có delta cần trích vào skill nội bộ | **PR gộp đã merge** |
| `luu-tru` | Xử lý xong: loại, trùng, hoặc đã gộp xong delta | — |

**Luật:** skill có phần đáng lấy chỉ được lưu trữ **sau khi PR gộp đã merge**. Lưu trữ sớm là mất dấu phần chưa lấy.

## Kết luận khi lưu trữ

| `ket_luan` | Khi nào |
|---|---|
| `trung` | Skill nội bộ đã có, bản ngoài không hơn |
| `loai` | Kém, sai, rủi ro, hoặc ngoài trọng tâm |
| `da-gop` | Phần đáng lấy đã vào skill nội bộ |

## Mẫu phiếu

```yaml
ten: sales-discovery-call-template
lo: lo-290
ket_luan: trung            # trung | loai | da-gop
lo_thu: 2026-10-sale-lo1   # thư mục trong thu-nghiem/
skill_noi_bo: 16-kham-pha-nhu-cau
diem: {noi_bo: 23, ngoai: 18, khong_skill: 24}
ly_do: "..."
da_lay: []                 # với da-gop: phần đã lấy + link PR
thu_lai_khi: ""            # tuỳ chọn, vd "mô hình thế hệ mới"
ngay: 2026-10-26
nguoi_chot: Quân
```

## Skill nội bộ không đạt

Áp cùng vòng đời nhưng trong **repo của chính skill đó** (vd `sale-suite-os/luu-tru/`), không có manifest nên không bao giờ được cài, kèm phiếu cùng mẫu. Chỉ lưu trữ skill nội bộ khi đã chấm **sạch** bằng `may-cham cham --so-sanh` (không có rò tri thức sang bản không skill) và tối thiểu 3 tình huống.
