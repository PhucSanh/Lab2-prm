# S03-later – nguồn từng đoạn của v0-prompt.txt

**Biến thể của S03, screen id `cc28fdd64e6e4c70b59b419c44376787`** (màn chốt của S03 = v3; xác định bằng `list_screens`, md5 ảnh trùng `stitch-runs/S03/v3.png`). Lệnh chạy không có `--from S03`, nhưng `CHIA-VIEC.md` dòng A08 ghi "EDIT S03", nên chạy theo chế độ biến thể.

| Đoạn prompt | Lấy từ |
| --- | --- |
| Dòng đầu (giữ khung, header, bottom nav, màu, chữ) | mẫu `/stitch-loop` mục 0c |
| Bối cảnh: S03 sau khi dời 30 phút, chỉ đổi snackbar | `CHIA-VIEC.md` A08 (Nguồn: `flutter-handoff.md` DLG-Later); `AppStyleGuide.md` mục 5 "Dời việc" ("30 phút nữa"); `flutter-handoff.md` dòng S04 (Snackbar "Đã dời “Đi bộ” sang 10:00 sáng · Hoàn tác") |
| Giờ 9:30 sáng + 30 phút = 10:00 sáng; tiến độ vẫn 3/6 (dời không phải xong) | SG-10, SG-24 |
| Chip "Đã dời" viền, nền trắng, icon `alarm-clock-plus` | `AppStyleGuide.md` SG-23 (↻ Đã dời, nền `surface` viền); `DESIGN.md` Từ điển icon (Dời giờ = `alarm-clock-plus`); giờ mới nằm ở dòng giờ của thẻ nên chip chỉ ghi "Đã dời" (tránh chip quá rộng) |
| Snackbar 1 hàng 80 px, nút "Hoàn tác" nowrap, 14 px | `AppStyleGuide.md` SG-35/36/37; bài học từ S03b (R-LAY-01, R-STY-02) |
| Nhãn nút đáy "Đã xong việc đi bộ" | bài học từ S03b (R-ONE-02: nói rõ nút áp cho việc nào) |
| padding-bottom 300 px | bài học từ S03b (R-LAY-01) |
| Sửa icon theo Từ điển (footprints, house, circle-check, alarm-clock-plus, hand-heart, calendar-days) | `DESIGN.md` Từ điển icon; lỗi kế thừa từ S03 v3 đã thấy ở ST-Empty và S03b — đưa vào v0 để khỏi tốn vòng |
| CONSTRAINTS | `rule.md` các luật error liên quan |
