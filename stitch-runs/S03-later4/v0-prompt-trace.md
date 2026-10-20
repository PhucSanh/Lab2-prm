# S03-later4 – nguồn từng đoạn của v0-prompt.txt

**Biến thể của S03, screen id `cc28fdd64e6e4c70b59b419c44376787`** (màn chốt của S03 = v3; xác định bằng `list_screens`, md5 ảnh trùng `stitch-runs/S03/v3.png`, xem `stitch-runs/ST-Empty/v0-prompt-trace.md`). Không sửa từ S03-later, theo đúng `--from S03`.

| Đoạn prompt | Lấy từ |
| --- | --- |
| Dòng đầu (giữ khung, header, bottom nav, màu, chữ) | mẫu `/stitch-loop` mục 0c |
| Bối cảnh: dời chiều nay, "Như trên" (giống S03-later) | `CHIA-VIEC.md` dòng A09 (Nguồn: `flutter-handoff.md` DLG-Later); `AppStyleGuide.md` mục 5 "Dời việc" ("Chiều nay"; snackbar "Đã dời {Đi bộ} sang {chiều nay, 4 giờ}.") |
| Giờ mới "4 giờ chiều" (chiều nay, 4 giờ) | `AppStyleGuide.md` mục 5; SG-10 (giờ viết kiểu nói) |
| Việc tiếp theo chuyển sang "Uống trà với cô Tám" 3 giờ chiều; danh sách xếp lại theo giờ | Danh sách việc S03 v3 (6 việc); thứ tự giờ 3 giờ chiều < 4 giờ chiều < 6 giờ tối; tile `coffee` theo `vocabulary.md` mục 1 |
| Chip "Đã dời" viền, icon `alarm-clock-plus` | SG-23; `DESIGN.md` Từ điển icon (Dời giờ) |
| Snackbar dạng cột dọc, "Hoàn tác" nowrap, padding-bottom 340 | bài học từ S03b và S03-later (R-TXT-03, R-LAY-01) |
| Nhãn nút đáy "Đã xong việc uống trà" | bài học từ S03b (R-ONE-02) |
| Sửa icon, màu tile = màu vạch, nav `hand-heart` / `calendar-days` | `DESIGN.md` Từ điển icon, 9 màu nhấn; lỗi kế thừa từ S03 v3 thấy ở ST-Empty, S03b, S03-later |
| CONSTRAINTS | `rule.md` các luật error liên quan |
