# v0-prompt-trace – S05 Thêm việc – chọn việc quen

| Đoạn prompt | Lấy từ |
| --- | --- |
| Tên app, 360x800, Power 9, persona, nguyên tắc | `PRD.md` 11.1 |
| Nội dung màn: "Bác muốn làm gì?", 3 việc quen (Đi bộ nhẹ nhàng, Chăm cây, Gọi người thân), "Xem thêm" | `PRD.md` 11.2 dòng #4 (S05 → S06, bước 1); FR05 (3 việc + "Xem thêm") |
| "Bước 1/2", nút "Tiếp tục" | `README.md` (S05–S06), `design-decisions.md` D13 (bước đếm khớp); `AppStyleGuide.md` SG-16 |
| Tối đa 3 lựa chọn ngang hàng | `AppStyleGuide.md` SG-29 |
| Chọn thay vì gõ | SG-34, I11 |
| Trạng thái chọn icon + chữ ("Đã chọn" / "Chọn") | R-COL-01, SG-58 |
| Thói quen cho từng việc: Đi bộ, Chăm cây → Vận động tự nhiên; Gọi người thân → Gia đình trên hết | `vocabulary.md` mục 1, 2 (Chăm cây → thói quen 1; Gọi điện → thói quen 8) |
| Màu, font, lề 20, bo 16/14, cấm gradient | `assets/stitch/DESIGN.md` |
| Màu nhấn #2BA15C, #D86E75, ô icon 48x48, vạch 6px | `DESIGN.md` màu nhấn 9 thói quen |
| Dòng việc: icon · tên · 1 dòng phụ | `rule.md` R-TXT-05, R-COL-02 |
| Chữ >= 20, 24/30/22 | R-TXT-01/02 |
| Tương phản, tràn ngang | R-CON-01, R-LAY-01 |
| Vùng chạm, nút chính 60 ở đáy, cách >= 8 | R-TAP-01/02/03 |
| Câu <= 15, nút <= 5 tiếng | R-TXT-03/04 |
| 1 nút filled | R-ONE-01 |
| Quay lại có chữ; icon luôn có nhãn | R-NAV-02, R-ICON-01/02/03 |
| Từ cấm | `vocabulary.md` mục 5, R-VOC-01, R-LANG-03 |
