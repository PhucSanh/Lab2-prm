# v0-prompt-trace – S15 Sửa việc

PRD.md 11.2 không có dòng cho S15; nội dung màn lấy từ `flutter-handoff.md` mục S15 và `ux/user-flow.md` Flow 7 (cùng `design-decisions.md` D15, D25, D26).

| Đoạn prompt | Lấy từ |
| --- | --- |
| Tên app, 360x800, Power 9, persona, nguyên tắc | `PRD.md` 11.1 |
| Nội dung màn: Quay lại, chip thói quen, "Sửa việc", Tên việc, Giờ làm, Lặp lại, Nhắc nhở, Xóa việc này, Lưu thay đổi | `flutter-handoff.md` S15 Layout; `ux/user-flow.md` Flow 7 |
| Ô giờ bấm mở hộp chọn giờ, không bánh xe cuộn | `PRD.md` FR05; SG-34 |
| Ô Lặp lại là ô bấm thay cho SegmentedButton (chọn thay vì gõ, tránh nhãn dài trong 3 ô hẹp) | SG-34; `[N]` điều chỉnh so với handoff |
| Nút xóa ở cuối, tách xa nút Lưu, chú thích hỏi lại | `flutter-handoff.md` S15 UI constraints; D15; SG-19 |
| "Bác" thay "Bà" trong chú thích xóa | SG-01 |
| Gợi ý "Ví dụ: Đi bộ buổi sáng" | `AppStyleGuide.md` SG-15, mục 5 (Lỗi nhập) |
| Token màu, font, lề 20, bo góc, cấm gradient | `assets/stitch/DESIGN.md` |
| Màu nhấn #2BA15C, ô icon 48, vạch 6px | `DESIGN.md` màu nhấn; `vocabulary.md` mục 1 (Vận động tự nhiên, footprints) |
| Khối ICONS | `DESIGN.md` Từ điển icon (chevron-left, pencil, clock, chevron-down, repeat, bell-ring, info, trash-2, save) + `vocabulary.md` mục 1 |
| Nhãn Lưu · Sửa · Xóa kèm tên việc | `vocabulary.md` mục 3 |
| Chữ >= 20, 24/30/22 | R-TXT-01/02 |
| Tương phản, tràn ngang | R-CON-01, R-LAY-01 |
| Vùng chạm, nút chính 60 ở đáy | R-TAP-01/02 |
| Câu <= 15, nút <= 5 tiếng | R-TXT-03/04 |
| 1 nút filled | R-ONE-01 |
| Icon luôn có nhãn, >= 32 | R-ICON-01/02/03 |
| Từ cấm | `vocabulary.md` mục 5, R-VOC-01, R-LANG-03 |
| Không vuốt/ba chấm | `PRD.md` 11.4, R-GES-01 |
