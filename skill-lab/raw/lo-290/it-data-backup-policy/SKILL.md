---
name: it-data-backup-policy
description: |
  Thiết kế chính sách backup dữ liệu theo quy tắc 3-2-1 (3 copies, 2 media, 1 offsite), xác định RPO/RTO, lịch backup, test restore định kỳ — đảm bảo khôi phục được sau ransomware/disaster.
  Kích hoạt khi người dùng nói: "chính sách backup", "data backup policy", "3-2-1 rule", "RTO RPO", "disaster recovery", "DR plan", "backup dữ liệu công ty", "khôi phục dữ liệu", "lịch sao lưu", "backup strategy".
  Output là policy document + lịch backup Excel + test restore checklist.
---

# Data Backup & Disaster Recovery Policy Builder

## Mục Tiêu
Đảm bảo khi xảy ra sự cố (ransomware, server cháy, NV xoá nhầm), doanh nghiệp khôi phục được dữ liệu trong RTO cam kết — không phải "đóng cửa luôn" như nhiều SME khi bị ransomware.

## Khi Nào Dùng
- Doanh nghiệp chưa có chính sách backup chính thức
- Vừa bị ransomware, mất data → cần xây lại
- Audit ISO 27001 / SOC 2 / kiểm toán tài chính
- Chuyển dữ liệu lên cloud, cần xác định backup strategy mới
- Đầu năm review BCM (Business Continuity Management)

## Bước 1: Phân Loại Dữ Liệu Theo Mức Độ Quan Trọng
Lập **Data Criticality Matrix**:
| Tier | Loại data | RPO max | RTO max | Ví dụ |
|------|-----------|---------|---------|-------|
| Tier 1 — Critical | Mất là chết | 1h | 4h | DB khách hàng, kế toán đang chạy |
| Tier 2 — Important | Mất chậm việc | 24h | 24h | Email, Drive nhân viên |
| Tier 3 — Standard | Phục hồi từ từ | 7 ngày | 7 ngày | File lưu trữ cũ |
| Tier 4 — Archive | Lưu pháp lý | 30 ngày | 30 ngày | Hợp đồng 5-10 năm trước |

## Bước 2: Áp Dụng Quy Tắc 3-2-1
Mỗi dữ liệu Tier 1-2 phải có:
- **3 copies** — 1 production + 2 backup
- **2 media khác nhau** — ví dụ HDD + cloud, hoặc tape + S3
- **1 offsite** — vật lý cách trung tâm chính (tỉnh khác / cloud region khác)

Mở rộng 3-2-1-1-0:
- 1 offline/air-gapped (chống ransomware)
- 0 lỗi sau verification (test restore = 0 lỗi)

## Bước 3: Lịch Backup Cụ Thể
Mẫu lịch:
- **Database production**: snapshot mỗi 1h, full daily 02:00, retention 30 ngày + 12 monthly
- **File server**: incremental hàng đêm, full chủ nhật
- **Email (M365/Workspace)**: backup bằng tool 3rd party (Veeam, Spanning) hàng ngày
- **SaaS data** (Salesforce, HubSpot): export weekly + tool backup
- **Endpoint**: backup laptop NV (chỉ folder Documents/Desktop) qua OneDrive/Drive
- **Config & code**: GitHub mirror, infra-as-code commit hàng ngày

## Bước 4: Test Restore Định Kỳ
**Quan trọng nhất** — nhiều công ty có backup nhưng chưa từng test:
- Hàng tháng: restore 1 file random từ mỗi tier
- Hàng quý: restore full một database staging
- Hàng năm: DR drill — giả lập datacenter chết, switch sang DR site

Ghi log mỗi lần test: thời gian, người làm, có lỗi gì, RTO thực tế.

## Bước 5: Tích Hợp Web Bên Ngoài (MCP-first + API fallback)

**Ưu tiên dùng MCP/Connectors có sẵn:**
- Google Drive MCP: backup Drive bằng snapshot + export
- GitHub MCP: mirror repo private sang offsite
- Slack MCP: notify khi backup fail / test restore xong
- Notion MCP: lưu policy & log test restore
- Linear MCP: tạo ticket mỗi lần backup fail để follow up
- WebSearch: best practice backup theo loại workload (DB, SaaS, container)
- WebFetch: pull pricing AWS Backup, Azure Backup, Backblaze B2

**Fallback bằng API (nếu cần làm sâu hơn):**
```python
# Verify S3 backup sức khoẻ
import boto3
s3 = boto3.client('s3')
resp = s3.list_objects_v2(Bucket='company-backup',
                          Prefix='db/2026-05/')
total_size = sum(o['Size'] for o in resp.get('Contents', []))
latest = max((o['LastModified'] for o in resp.get('Contents', [])),
             default=None)
print(f"Size: {total_size/1e9:.2f} GB, Latest: {latest}")
# Cảnh báo nếu latest > 25h trước
```

## Bước 6: Output Format
- File chính: `Backup_Policy_v1.md` (document chính thức)
- `Backup_Schedule.xlsx` (lịch chi tiết theo từng workload)
- `Data_Criticality_Matrix.xlsx` (phân tier)
- `Test_Restore_Log.xlsx` (theo dõi test định kỳ)
- `DR_Runbook.md` (hướng dẫn khôi phục từng bước khi đại nạn)
- Lưu tại: `/Users/nguyenkiem/Documents/Claude/SKILL/LÀM SKILL/outputs/backup-dr/`

## Checklist Trước Khi Giao
- [ ] Phân tier toàn bộ dữ liệu công ty
- [ ] RPO/RTO mỗi tier có cam kết rõ ràng
- [ ] Áp dụng 3-2-1 đầy đủ
- [ ] Có ít nhất 1 copy offline/air-gapped
- [ ] Lịch backup đã setup tự động + monitoring
- [ ] Test restore đã chạy ít nhất 1 lần thành công
- [ ] DR runbook có hướng dẫn bước-by-bước
- [ ] Sếp ký policy + cam kết ngân sách
