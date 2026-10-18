# v0-prompt-trace – S10 Cài đặt hiển thị

> `PRD.md` 11.2 không có dòng riêng cho S10; nội dung màn lấy từ F12 và `flutter-handoff.md` (mục S10).

| Đoạn prompt | Lấy từ |
| --- | --- |
| Tên app, 360x800, Power 9, persona, nguyên tắc | `PRD.md` 11.1 |
| Cỡ chữ Vừa / Lớn / Rất lớn, mặc định Lớn, xem thử "Đi bộ 20 phút lúc 9:30 sáng" | `PRD.md` F12, FR12; `DESIGN.md` Typography; `flutter-handoff.md` S10 (Layout) |
| 3 công tắc: tương phản cao, Đọc to, rung kèm chuông; nút "Xem thử lời nhắc"; 4 hàng Cách dùng / Hồ sơ / Nhắc việc / Dữ liệu | `flutter-handoff.md` S10 (Layout, Interactions) |
| Đổi tên cho hợp từ vựng: "Thông tin của Bác" (không "Hồ sơ"), "Lời nhắc" (không "Nhắc việc"), "Rung khi có lời nhắc" | `vocabulary.md` mục 3 (Profile, Notification/Reminder) |
| Không bottom nav, nút Back "‹ Hôm nay" | `flutter-handoff.md` S10 (Navigation); `AppStyleGuide.md` SG-21; R-NAV-02 |
| Trạng thái chọn / công tắc bằng icon + chữ ("Đã chọn"/"Chọn", "Đang bật"/"Đang tắt") | R-COL-01; SG-58 |
| Không nút filled; nút viền "Xem thử lời nhắc" | R-ONE-01; `AppStyleGuide.md` SG-17 |
| Mỗi dòng một icon khác nhau | R-ICON-03; SG-32; bài học S08/S09 |
| Không gradient kể cả thanh cố định | R-STY-02; bài học S09 |
| Không cắt chữ, cột chữ >= 200px | R-LAY-01; SG-13; bài học S08 |
| Màu, font, lề 20, bo 16/14 | `assets/stitch/DESIGN.md` |
| Chữ >= 20, 24/30/22; tương phản; vùng chạm 48; nút 60 | R-TXT-01/02, R-CON-01, R-TAP-01/02 |
| Câu <= 15, nút <= 5 tiếng | R-TXT-03/04 |
| Icon luôn có nhãn | R-ICON-01/02 |
| Không vuốt/nhấn giữ, không gõ chữ | R-GES-01; SG-34 |
| Từ cấm | `vocabulary.md` mục 5, R-VOC-01, R-LANG-03 |
