# v0-prompt-trace – N12 Lặp lại

Màn sinh mới bằng `generate_screen_from_text` (không phải biến thể). Project 2013215887278758682. Khung, header, footer lấy theo N11 (`stitch-runs/N11/v0-prompt.txt`) để hai màn con dùng chung cùng bộ cục.

| Đoạn prompt | Lấy từ |
| --- | --- |
| Bối cảnh, nguyên tắc (Bác tự quyết, 1 nút chính, chỉ chạm) | `PRD.md` 11.1 |
| Nội dung màn: Một lần / Mỗi ngày / chọn ngày trong tuần, "Đã chọn · Thứ Hai…", "Lưu các ngày đã chọn", "Hủy", có kiểm tra không để trống | `flutter-handoff.md` bảng N01–N21 (dòng N12) và dòng 114 |
| Màn mở từ dòng "Lặp lại" ở form Thêm việc; back "Thêm việc" | `ux/user-flow.md` dòng 130; `PRD.md` 11.2 dòng 4 (S06) |
| Token màu / chữ / bo góc / lề | `DESIGN.md` (colors, typography, rounded, spacing) |
| "Thứ Hai … Chủ Nhật" viết đủ | `AppStyleGuide.md` SG-09 (không dùng "T2" trên màn người lớn tuổi); hàng toàn chiều ngang nên đủ chỗ |
| Tên 3 lựa chọn "Một lần", "Mỗi ngày", "Vài ngày trong tuần"; hint "Chọn những ngày Bác muốn làm việc này." | tự soạn theo SG-10/SG-11 (câu ngắn, ≤ 15 tiếng, xưng "Bác"); "Vài ngày" khớp ô S06 |
| Dòng "Đã chọn · …" và chữ "Đang chọn" | R-COL-01 (trạng thái không chỉ bằng màu); `DESIGN.md` Từ điển icon (`circle-dot` kèm chữ "Đang chọn") |
| Hàng ngày cao 56px, gap 8px, 1 cột | R-TAP-01, R-TAP-03, R-TXT-01; 1 cột để "Thứ Bảy" + "Đang chọn" không bị cắt ở 360px |
| Khối ICONS | `DESIGN.md` Từ điển icon: `chevron-left`, `repeat`, `info`, `circle`, `circle-dot`, `save`, `x` (không thêm icon mới) |
| Ràng buộc error | `rule.md` R-TXT-01/03/04, R-CON-01, R-LAY-01, R-TAP-01/02, R-ICON-01, R-NAV-02, R-ONE-01, R-COL-01, R-GES-01, R-LANG-01, R-VOC-01 |
