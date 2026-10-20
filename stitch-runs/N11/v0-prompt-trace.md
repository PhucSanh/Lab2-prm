# v0-prompt-trace – N11 Chọn ngày

Màn sinh mới bằng `generate_screen_from_text` (không phải biến thể). Project 2013215887278758682.

| Đoạn prompt | Lấy từ |
| --- | --- |
| Bối cảnh, nguyên tắc (Bác tự quyết, 1 nút chính, chỉ chạm) | `PRD.md` 11.1 |
| Nội dung màn: lịch tháng 10/2026, T2 → CN, "Chọn ngày, rồi bấm Xong để xác nhận.", nút "Xong" / "Hủy" | `flutter-handoff.md` bảng N01–N21 (dòng N11); `ux/user-flow.md` dòng 130 (S05/S06 mở N11 bằng "Ngày thực hiện") |
| Token màu / chữ / bo góc / lề | `DESIGN.md` (colors, typography, rounded, spacing) |
| Nhãn nút "Xong", "Hủy", back "Thêm việc", dòng tóm tắt "Đã chọn · Thứ Sáu, 23/10" | `AppStyleGuide.md` SG-10, SG-11, SG-16, SG-21; `vocabulary.md` mục 3 (Cancel/OK → Hủy / Xong) |
| Thứ viết "Hai … Bảy, CN" thay "T2" | tự quyết: SG-09 không dùng "T2" trên màn người lớn tuổi; cột 48px không đủ cho "Thứ Hai" |
| Lưới rộng 336px, lề 12 (lệch lề 20) | tự quyết: 7 cột × 48px để đạt R-TAP-01; chấp nhận cảnh báo R-STY-03 |
| Dòng "Đã chọn · …" | R-COL-01 (ngày chọn không chỉ bằng màu) |
| Nút "Tháng 9" / "Tháng 11" có chữ | R-ICON-01, R-GES-01 (không vuốt đổi tháng) |
| Khối ICONS | `DESIGN.md` Từ điển icon; thêm 19/10/2026: `calendar`, `chevrons-left`, `chevrons-right`, `check` |
| Ràng buộc error | `rule.md` R-TXT-01/03/04, R-CON-01, R-LAY-01, R-TAP-01/02, R-ICON-01, R-NAV-02, R-ONE-01, R-COL-01, R-GES-01, R-LANG-01, R-VOC-01 |
