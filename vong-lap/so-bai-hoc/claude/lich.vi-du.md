# Lịch ví dụ cho Agent Evolution

Bộ cài **không** đăng ký cron hay launchd, và **không** ghi `settings.json`. Muốn bật thì tự chép.

Giờ: 09:00 thứ Hai và thứ Năm, múi `Asia/Saigon`.

## cron

Trên cron có `CRON_TZ` (cronie, Vixie):

```
CRON_TZ=Asia/Saigon
0 9 * * 1,4 "$HOME/.agent-evolution/ra-lich.sh"
```

`ra-lich.sh` gọi `claude -p --agent agent-evolution` với lời nhắc trong `loi-nhac-ra.txt`. Lượt này không người xem: agent chỉ được ghi tầng `scratch`. Bài nhạy được liệt kê trong `~/.agent-evolution/bao-cao/`, không được nâng tầng.

Headless chỉ chạy được nếu máy đã cho agent đọc file và chạy `ledger.py`. Không thêm cờ bỏ qua hết câu hỏi quyền.

## launchd (macOS)

launchd lấy múi giờ của máy. Đặt máy ở `Asia/Saigon`, hoặc đừng dùng plist này.

Tệp ví dụ, không cài sẵn. `StartCalendarInterval` thứ Hai (`Weekday` 1) và thứ Năm (`Weekday` 4), giờ 9, phút 0. Hai block là hai lịch.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>agent-evolution-ra</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/sh</string>
    <string>REPLACE_HOME/.agent-evolution/ra-lich.sh</string>
  </array>
  <key>StartCalendarInterval</key>
  <array>
    <dict>
      <key>Weekday</key><integer>1</integer>
      <key>Hour</key><integer>9</integer>
      <key>Minute</key><integer>0</integer>
    </dict>
    <dict>
      <key>Weekday</key><integer>4</integer>
      <key>Hour</key><integer>9</integer>
      <key>Minute</key><integer>0</integer>
    </dict>
  </array>
</dict>
</plist>
```

Đổi `REPLACE_HOME` thành thư mục nhà. Nạp bằng `launchctl bootstrap` khi nào tự quyết định. Gỡ bằng `launchctl bootout`.
