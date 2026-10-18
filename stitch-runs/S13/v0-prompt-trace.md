# v0-prompt-trace – S13 Cho phép nhắc việc

Lưu ý: `PRD.md` 11.2 không có dòng cho S13. Nội dung màn lấy từ `README.md` (S13 Bước 2/2, Onboarding), `ux/user-flow.md` (Flow 1: nút "Bật nhắc việc" và "Để sau"), `design-decisions.md` D13 (giải thích + ví dụ lời nhắc + dặn trước "điện thoại sẽ hỏi lại").

| Đoạn prompt | Lấy từ |
| --- | --- |
| Tên app, 360x800, Power 9, persona, nguyên tắc | `PRD.md` 11.1 |
| Mục đích màn, 2 nút "Bật nhắc việc" / "Để sau", "Bước 2/2" | `README.md`, `ux/user-flow.md` Flow 1, D13 |
| Câu "Để đến giờ điện thoại đổ chuông nhắc Bác." và "Điện thoại sẽ hỏi lại, Bác chọn Cho phép." | `AppStyleGuide.md` mục 5 (Xin quyền nhắc việc) |
| Ví dụ lời nhắc "Đến giờ đi bộ rồi Bác ơi", 9:30 sáng | `AppStyleGuide.md` SG-22, mục 1, SG-10; dữ liệu PRD 11.2 S03 |
| Màu, font, lề 20, bo 16/14, cấm gradient | `assets/stitch/DESIGN.md` |
| Màu nhấn #2BA15C, ô icon 48x48, vạch 6px | `DESIGN.md` màu nhấn 9 thói quen |
| Chữ >= 20, 24/30/22 | `rule.md` R-TXT-01/02 |
| Tương phản, tràn ngang | R-CON-01, R-LAY-01 |
| Vùng chạm, nút chính 60 ở đáy, cách >= 8 | R-TAP-01/02/03 |
| Câu <= 15, nút <= 5 tiếng | R-TXT-03/04 |
| 1 nút filled | R-ONE-01 |
| Quay lại có chữ; icon luôn có nhãn | R-NAV-02, R-ICON-01/02/03 |
| Căn giữa nội dung đứng một mình | R-CEN-01, SG-25 |
| Từ cấm | `vocabulary.md` mục 5, R-VOC-01, R-LANG-03 |
