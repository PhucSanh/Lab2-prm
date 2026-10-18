# v0-prompt-trace – S06 Thêm việc – thiết lập

| Đoạn prompt | Lấy từ |
| --- | --- |
| Tên app, 360x800, Power 9, persona, nguyên tắc | `PRD.md` 11.1 |
| Nội dung màn: tên việc, ô giờ "8 : 00 sáng ⌄", lặp lại, nhắc; nút "Lưu việc này" | `PRD.md` 11.2 dòng #4 (S05 → S06, bước 2); FR05 (ô bấm mở hộp chọn giờ, không bánh xe cuộn) |
| "Bước 2/2", tên việc từ bước 1 "Đi bộ nhẹ nhàng" | `README.md` (S05–S06), S05 v0 |
| Ví dụ "Ví dụ: Đi bộ buổi sáng" | `AppStyleGuide.md` SG-15, mục 5 (Lỗi nhập) |
| Chọn thay vì gõ | SG-34, PRD I11 |
| Nhãn "Lưu việc này", "Nhắc lại sau 10 phút" | `AppStyleGuide.md` SG-16, SG-22 |
| Từ "Giờ làm", "Lặp lại", "Lời nhắc" | `vocabulary.md` mục 3 (Reminder → Lời nhắc; Save → Lưu + tên việc) |
| Tối đa 3 lựa chọn ngang hàng | SG-29 |
| Trạng thái chọn icon + chữ | R-COL-01, SG-58 |
| Màu, font, lề 20, bo 16/14/12, cấm gradient | `assets/stitch/DESIGN.md` |
| Màu nhấn #2BA15C, ô icon 48x48, vạch 6px | `DESIGN.md` màu nhấn; `vocabulary.md` mục 1 |
| #E7F2EB (primary-container-soft) cho nền lựa chọn đã chọn | `DESIGN.md` colors (token có sẵn); chọn nền nhạt để không trùng icon màu nhấn (bài học critique S05 v2) |
| Chữ >= 20, 24/30/22; không nowrap/ellipsis | R-TXT-01/02, R-LAY-01 (bài học S05) |
| Tương phản, vùng chạm, nút chính 60 ở đáy | R-CON-01, R-TAP-01/02/03 |
| Câu <= 15, nút <= 5 tiếng | R-TXT-03/04 |
| 1 nút filled | R-ONE-01 |
| Quay lại có chữ; icon luôn có nhãn | R-NAV-02, R-ICON-01/02/03 |
| Từ cấm | `vocabulary.md` mục 5, R-VOC-01, R-LANG-03 |
