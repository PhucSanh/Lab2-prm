# v0-prompt-trace – S01 Chào mừng – chọn cỡ chữ

Lưu ý: `PRD.md` 11.2 không có dòng riêng cho S01. Nội dung màn lấy từ PRD F12/FR12, `ux/user-flow.md` Flow 1 và AppStyleGuide SG-25; chỗ nào tự ghép thì ghi rõ.

| Đoạn prompt | Lấy từ |
| --- | --- |
| Tên app, khung 360x800, Power 9, 60+, nguyên tắc, persona Bà Lan | `PRD.md` 11.1 |
| Mục đích màn: chọn Vừa / Lớn / Rất lớn, xem trước trực tiếp, đổi lại được | `PRD.md` F12, FR12; `ux/user-flow.md` Flow 1 (S01 → "Bắt đầu" → S02) |
| Căn giữa nội dung đứng một mình (chọn cỡ chữ S01) | `AppStyleGuide.md` SG-25; `rule.md` R-CEN-01 |
| Tên app 34px (`display`), tiêu đề 30, nội dung 24, nút 22 | `DESIGN.md` Typography ("display: Tên app (S01)") |
| Ba mức cỡ chữ Vừa 20 / Lớn 24 (mặc định) / Rất lớn 28 | `DESIGN.md` bảng "Ba mức cỡ chữ người dùng chọn" |
| Màu nền/thẻ/chữ/primary/container/outline, lề 20, gap 16, bo 16/14, cấm gradient | `DESIGN.md` colors, rounded, spacing, Elevation |
| Nút chính 60px cố định đáy, 1 nút filled | `DESIGN.md` Layout; `rule.md` R-TAP-02, R-ONE-01 |
| Chữ >= 20, tương phản, không tràn ngang, vùng chạm >= 48 | `rule.md` R-TXT-01, R-CON-01, R-LAY-01, R-TAP-01 |
| Câu <= 15, nút <= 5 tiếng | `rule.md` R-TXT-03/04 |
| Lựa chọn không chỉ bằng màu: icon + "Đang chọn" | `rule.md` R-COL-01; `AppStyleGuide.md` SG-58 |
| Mọi icon có nhãn, mục có icon | `rule.md` R-ICON-01/02; SG-30, SG-52 |
| Câu mẫu xem thử "Đến giờ đi bộ rồi Bác ơi" | `AppStyleGuide.md` mục 1 và mục 3 (lời nhắc) |
| "Chào mừng Bác!", "Bác chọn cỡ chữ dễ đọc nhé." (tự viết, theo giọng SG-01, SG-07, gợi ý không ra lệnh) | `AppStyleGuide.md` mục 1; tự ghép |
| Nhãn nút "Bắt đầu"; từ "cỡ chữ" | `ux/user-flow.md` Flow 1; `vocabulary.md` mục 3 (Font size → Cỡ chữ) |
| Không tutorial/carousel/vuốt/menu ba chấm | `PRD.md` 11.4; `DESIGN.md` "Hướng dẫn đúng lúc" |
| Từ cấm | `vocabulary.md` mục 5; `rule.md` R-VOC-01, R-LANG-03 |
