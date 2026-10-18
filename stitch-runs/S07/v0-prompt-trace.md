# v0-prompt-trace – S07 Lịch tuần

> `PRD.md` 11.2 không có dòng riêng cho S07; nội dung màn lấy từ F06 và `flutter-handoff.md` (mục S07).

| Đoạn prompt | Lấy từ |
| --- | --- |
| Tên app, 360x800, Power 9, persona, nguyên tắc | `PRD.md` 11.1 |
| Mục đích màn: xem 7 ngày, chạm một ngày để mở | `PRD.md` F06 (Lịch tuần và chi tiết ngày); `flutter-handoff.md` S07 (Interactions) |
| 7 hàng ngày cao ≥ 68, hôm nay ≥ 76 viền primary, mũi tên báo bấm được | `flutter-handoff.md` S07 (Layout, Components) |
| Trạng thái ngày luôn có chữ (6/6, 5/6), không chỉ màu | `flutter-handoff.md` S07 (UI constraints); `AppStyleGuide.md` SG-23, SG-24 |
| Tiến độ bằng chữ "Đã xong 6/6 việc", không % | R-STA-02, `AppStyleGuide.md` SG-24; `design-decisions.md` D7 |
| Nhãn "Chưa làm" nền vàng nhạt | `DESIGN.md` status-todo; SG-23 |
| Ngày viết đủ "Thứ Hai", ngày/tháng "5/10" | SG-09, SG-11 |
| Bottom nav 4 tab, tab "Lịch tuần" đang chọn | `PRD.md` NFR03; `DESIGN.md` bottom-nav; R-NAV-01 |
| Chấm màu thói quen ở lịch tuần, 9 màu nhấn | `DESIGN.md` mục "Màu nhấn 9 thói quen"; SG-54 |
| Không nút filled (màn tab chỉ để xem) | R-ONE-01; `PRD.md` 11.2 dòng S08 (mẫu "không có nút filled") |
| Màu, font, lề 20, bo 16, cấm gradient | `assets/stitch/DESIGN.md` |
| Chữ >= 20, 24/30; tương phản; tràn ngang | R-TXT-01/02, R-CON-01, R-LAY-01 |
| Vùng chạm 48, cách >= 8 | R-TAP-01/03 |
| Câu <= 15, nhãn <= 5, tab <= 3 tiếng | R-TXT-03/04 |
| Icon luôn có nhãn, >= 32px | R-ICON-01/02/03 |
| Không vuốt/nhấn giữ | R-GES-01, SG-33 |
| Từ cấm | `vocabulary.md` mục 5, R-VOC-01, R-LANG-03 |
