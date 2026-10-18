# v0-prompt-trace – S17 Nhắn tin cho người thân

PRD.md 11.2 không có dòng cho S17; nội dung màn lấy từ `flutter-handoff.md` mục S17, `design-decisions.md` D18 và D27, PRD F13 / FR09.

| Đoạn prompt | Lấy từ |
| --- | --- |
| Tên app, 360x800, Power 9, persona, nguyên tắc | `PRD.md` 11.1 |
| Bố cục: Back "Gia đình", "Nhắn tin cho Mai", "Bác muốn kể điều gì?" 3 lựa chọn, khung xem trước, "Gửi bằng" Zalo / SMS, Footer "Tiếp tục gửi cho Mai" | `flutter-handoff.md` S17 Layout |
| Lựa chọn chủ đề rút còn "Hỏi thăm con / Kể việc đi bộ / Kể việc chăm cây" (xưng "con" theo SG-04) | handoff S17; SG-04 |
| Bỏ khối chip "Thêm một câu" để ít chữ, một việc mỗi màn | R-TXT-03, SG-07, SG-29 `[N]` |
| Khung "Mai sẽ thấy" + câu soạn sẵn "Mẹ nhớ con. Hôm nay mẹ khỏe, con nhé!" (≤ 15 tiếng, xưng Mẹ – con) | SG-50, SG-04, `AppStyleGuide.md` mục 5 (Chia sẻ cho con) |
| Dòng "An Nhiên chỉ mở Zalo. Bác bấm gửi ở đó." (không báo "Đã gửi") | D27; SG-49/50; PRD FR09; `AppStyleGuide.md` mục 1 (Thật thà) |
| Nhãn "Tin nhắn SMS" (hàng chọn SMS) | handoff S17 ("Zalo – khuyên dùng / SMS") |
| Footer "Tiếp tục gửi cho Mai" (5 tiếng) | handoff S17; SG-16 |
| Ô lựa chọn: viền 2px primary + circle-dot + chữ "Đang chọn" | `DESIGN.md` Từ điển icon (Đang chọn) |
| Khối ICONS | `DESIGN.md` Từ điển icon (chevron-left, message-square, circle-dot, circle, info, arrow-right) |
| Token màu, font, lề 20, bo góc, cấm gradient | `assets/stitch/DESIGN.md` |
| Chữ >= 20, 24/30/22 | R-TXT-01/02 |
| Tương phản, tràn ngang | R-CON-01, R-LAY-01 |
| Vùng chạm, nút chính 60 ở đáy | R-TAP-01/02 |
| Câu <= 15, nút <= 5 tiếng | R-TXT-03/04 |
| 1 nút filled | R-ONE-01 |
| Icon luôn có nhãn | R-ICON-01/02/03 |
| Từ cấm | `vocabulary.md` mục 5, R-VOC-01, R-LANG-03 |
| Không vuốt/ba chấm | `PRD.md` 11.4, R-GES-01 |
