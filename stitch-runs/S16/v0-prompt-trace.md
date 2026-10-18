# v0-prompt-trace – S16 Chi tiết thói quen

PRD.md 11.2 không có dòng cho S16; nội dung lấy từ `flutter-handoff.md` mục S16 (thói quen 1 "Có việc"), `vocabulary.md` mục 1 và 1.1.

| Đoạn prompt | Lấy từ |
| --- | --- |
| Tên app, 360x800, Power 9, persona, nguyên tắc | `PRD.md` 11.1 |
| Hàng tiêu đề "Thói quen 1 / 9" + tên, đoạn giới thiệu, thẻ "Tuần này Bác đã làm N lần", WeekStrip 7 ô, "Việc của Bác" + TaskRow, Footer Primary, Back "Thói quen" | `flutter-handoff.md` S16 |
| Câu giới thiệu "Đi bộ, làm vườn, tự làm việc nhà" | `vocabulary.md` mục 1.1 (dòng 1) |
| Nút "Đọc to" có chữ | R-VOI-01, SG-39 |
| Tên ngày "Hai … CN", "Nay" (không viết tắt T2) | SG-09; handoff ("Nay") |
| Chú thích 3 trạng thái ngày bằng icon + chữ | handoff UI constraints; R-COL-01 |
| Nhãn footer "Thêm việc" (handoff ghi 6 tiếng, rút còn 2 để ≤ 5 tiếng) | R-TXT-04; `[N]` |
| Bỏ khối "Học từ đâu?" và chip "Gợi ý để bắt đầu" để ít chữ, một nút | R-TXT-03, SG-07, SG-29 `[N]`; Từ điển icon chưa có icon cho "Học từ đâu" |
| Token màu, font, lề 20, bo góc, cấm gradient | `assets/stitch/DESIGN.md` |
| Màu nhấn #2BA15C, ô icon 48/64, vạch 6px | `DESIGN.md` màu nhấn; `vocabulary.md` mục 1 (footprints) |
| Chip "Chưa làm" icon + chữ | `DESIGN.md` `status-todo`, SG-23 |
| Khối ICONS | `DESIGN.md` Từ điển icon (chevron-left, circle-check, circle-minus, circle, chevron-right, plus, volume-2) + `vocabulary.md` mục 1 |
| Chữ >= 20, 24/30/22 | R-TXT-01/02 |
| Tương phản, tràn ngang | R-CON-01, R-LAY-01 |
| Vùng chạm, nút chính 60 | R-TAP-01/02 |
| Câu <= 15, nút <= 5 tiếng | R-TXT-03/04 |
| 1 nút filled | R-ONE-01 |
| Icon luôn có nhãn | R-ICON-01/02/03 |
| Từ cấm | `vocabulary.md` mục 5, R-VOC-01, R-LANG-03 |
| Không vuốt/ba chấm | `PRD.md` 11.4, R-GES-01 |
