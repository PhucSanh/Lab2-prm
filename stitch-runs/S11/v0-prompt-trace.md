# v0-prompt-trace – S11 Chi tiết ngày

PRD.md 11.2 không có dòng cho S11; nội dung lấy từ `flutter-handoff.md` mục S11 (trạng thái "Ngày sắp tới"), `ux/user-flow.md` Flow 4, `design-decisions.md` D8. Việc mẫu lấy cùng bộ với S03 (`stitch-runs/S03/v0-prompt.txt`).

| Đoạn prompt | Lấy từ |
| --- | --- |
| Tên app, 360x800, Power 9, persona, nguyên tắc | `PRD.md` 11.1 |
| Tiêu đề ngày "Thứ Sáu, 9/10", nhóm Sáng/Trưa/Chiều/Tối, thẻ tóm tắt, TaskRow Upcoming + habit, nút Tonal "Thêm việc cho ngày này", Back "Lịch tuần", không bottom nav | `flutter-handoff.md` S11; D8 |
| Bỏ dòng gợi ý "Chạm vào một việc…" để giữ ≤ 1 dòng phụ, ít chữ | R-TXT-05, SG-07 `[N]` |
| Nhãn buổi "Buổi sáng/trưa/chiều/tối", giờ "12 giờ trưa", "3 giờ chiều" | SG-10; D8 |
| Ngày "Thứ Sáu, 9/10" | SG-11 |
| Thẻ việc: ô icon 48 + vạch 6px + giờ + tên + trạng thái | `DESIGN.md` `card-task`, R-TXT-05, R-COL-02 |
| Chip "Chưa làm" icon + chữ | `DESIGN.md` `status-todo`, SG-23, R-STA-01 |
| Không filled button; footer tonal | `DESIGN.md` `button-tonal`; R-ONE-01 (tối đa 1) |
| Token màu, font, lề 20, bo góc, cấm gradient | `assets/stitch/DESIGN.md` |
| 4 màu nhấn thói quen | `DESIGN.md` màu nhấn; `vocabulary.md` mục 1 |
| Khối ICONS | `DESIGN.md` Từ điển icon + `vocabulary.md` mục 1 (footprints, salad, coffee, house) |
| Chữ >= 20, 24/30/22 | R-TXT-01/02 |
| Tương phản, tràn ngang | R-CON-01, R-LAY-01 |
| Vùng chạm | R-TAP-01 |
| Câu <= 15, nút <= 5 tiếng | R-TXT-03/04 |
| Icon luôn có nhãn | R-ICON-01/02/03 |
| Từ cấm | `vocabulary.md` mục 5, R-VOC-01, R-LANG-03 |
| Không vuốt/ba chấm | `PRD.md` 11.4, R-GES-01 |
