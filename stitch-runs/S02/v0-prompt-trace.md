# v0-prompt-trace – S02 Thiết lập hồ sơ (Bước 1/2)

Lưu ý: `PRD.md` 11.2 không có dòng riêng cho S02. Nội dung màn lấy từ `README.md` (S02: tên gọi, xưng hô Ông/Bà, giờ thức dậy), `ux/user-flow.md` Flow 1 (S02 → "Tiếp tục", lỗi bỏ trống tên, "Quay lại" về S01) và AppStyleGuide SG-01. Chỗ tự ghép được ghi rõ.

| Đoạn prompt | Lấy từ |
| --- | --- |
| Tên app, khung 360x800, Power 9, 60+, persona Bà Lan, nguyên tắc | `PRD.md` 11.1 |
| Nội dung màn: tên, xưng hô Ông/Bà, giờ thức dậy, Bước 1/2 | `README.md` bảng màn (S02); `ux/user-flow.md` Flow 1 |
| Xưng hô mặc định "Bác", chọn Ông/Bà ở S02, dùng thống nhất toàn app | `AppStyleGuide.md` SG-01 |
| Nút "Tiếp tục", "Quay lại", lỗi bỏ trống tên + ví dụ dưới ô | `ux/user-flow.md` Flow 1 |
| Lỗi nhập 3 phần: icon + câu + ví dụ ("Bác chưa nhập tên." / "Ví dụ: Lan") | `AppStyleGuide.md` mục 5 (Lỗi nhập); `rule.md` R-SAFE-02 |
| Hạn chế gõ phím ảo, chọn giờ bằng ô bấm, nhãn ở trên ô | `DESIGN.md` Components (`text-field`) |
| Màu, lề 20, gap 16, bo 16/14/12, cấm gradient | `DESIGN.md` colors, rounded, spacing, Elevation |
| Cỡ chữ 30 / 24 / 22 / 20, giãn dòng 1,5 | `DESIGN.md` Typography |
| Căn trái form | `rule.md` R-CEN-01 |
| Nút chính 60px đáy, 1 nút filled; chữ >= 20; vùng chạm >= 48; không tràn ngang | `rule.md` R-TAP-02, R-ONE-01, R-TXT-01, R-TAP-01, R-LAY-01 |
| Nút Back có chữ "Quay lại" | `rule.md` R-NAV-02; `DESIGN.md` `button-back` |
| Câu <= 15 tiếng, nút <= 5 tiếng | `rule.md` R-TXT-03/04 |
| Lựa chọn và lỗi không chỉ bằng màu | `rule.md` R-COL-01 |
| Viền ô nhập / lựa chọn >= 3:1 (#7B887F, #526057; không dùng #A0ACA3 vì 2,35:1 – rút từ log S01) | `rule.md` R-CON-02; `stitch-runs/S01/log.md` |
| Icon ≥ 32, mọi mục có icon + nhãn | `rule.md` R-ICON-01/02/03 |
| Chữ "Giới thiệu về Bác", "Tên Bác", "Bác thức dậy lúc", helper "Để nhắc việc đúng giờ cho Bác." | tự viết theo giọng SG-01, SG-07 |
| Từ cấm | `vocabulary.md` mục 5; `rule.md` R-VOC-01, R-LANG-03 |
| Không carousel/vuốt/menu ba chấm | `PRD.md` 11.4 |
