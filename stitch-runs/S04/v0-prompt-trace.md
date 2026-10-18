# v0-prompt-trace – S04 Chi tiết việc

Lưu ý: `PRD.md` 11.2 không có dòng cho S04; nội dung màn lấy từ `README.md` (S04 Chi tiết hoạt động), `ux/user-flow.md` (Flow: S04 có "Dời", "Bỏ qua hôm nay", "Đã xong", "Sửa việc") và `rule.md` R-VOI-01 (S04 có "Đọc to").

| Đoạn prompt | Lấy từ |
| --- | --- |
| Tên app, khung 360x800, Power 9, persona, nguyên tắc | `PRD.md` 11.1 |
| Nội dung màn: tên việc, giờ, thói quen, nhãn trạng thái, các nút | `README.md` (S04), `ux/user-flow.md`, `PRD.md` 11.2 dòng S03 (dữ liệu "Đi bộ quanh công viên", 9:30, Vận động tự nhiên) |
| Màu, font, lề 20, bo 16/14, cấm gradient | `assets/stitch/DESIGN.md` |
| Màu nhấn #2BA15C, ô icon 48x48, vạch 6px, chip 40px | `DESIGN.md` bảng màu nhấn, components |
| Chữ >= 20, 24/30/22 | `rule.md` R-TXT-01/02 |
| Tương phản, tràn ngang | R-CON-01, R-LAY-01 |
| Vùng chạm, nút chính 60 ở đáy, khoảng cách | R-TAP-01/02/03 |
| Câu <= 15, nút <= 5 tiếng | R-TXT-03/04 |
| 1 nút filled | R-ONE-01 |
| Nút Quay lại có chữ | R-NAV-02, SG-21 |
| Nút "Đọc to" | R-VOI-01, SG-39 |
| Icon luôn có nhãn | R-ICON-01/02 |
| Nhãn "○ Chưa làm" | R-STA-01, SG-23 |
| Giờ "9:30 sáng" | SG-10 |
| "Dời", "Hôm nay bỏ qua", "Đã xong" | `vocabulary.md` mục 3, AppStyleGuide SG-22 |
| Từ cấm | `vocabulary.md` mục 5, R-VOC-01, R-LANG-03 |
| Không ranking/streak/%/menu 3 chấm | `PRD.md` 11.4 |
