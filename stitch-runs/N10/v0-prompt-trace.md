# v0-prompt-trace – N10 Đã mở ứng dụng chia sẻ

Biến thể của S17b, screen id `8dbd82153c14463aa7a54d58eb920e7b` (màn chốt v1 – điểm 100, project 2013215887278758682). Dùng `edit_screens`.

| Đoạn prompt | Lấy từ |
| --- | --- |
| Dòng đầu "Keep the overall layout…" | lệnh `/stitch-loop` mục 0c |
| "Người nhận: Con gái Mai", "Chưa xác nhận đã gửi" | `flutter-handoff.md` bảng N10 (dòng 271) |
| Nút "Về Gia đình" (filled), "Xem lại nội dung" (outlined) | `flutter-handoff.md` bảng N10; R-ONE-01 |
| "Bác bấm gửi trong ứng dụng nhắn tin nhé." | `AppStyleGuide.md` mục 5 "Thật thà" + SG-03; câu ≤ 15 tiếng (R-TXT-03) |
| Khung thông tin `primary-container` viền `primary`, không tự tắt | cùng kiểu S17b, S09b; DESIGN.md token |
| Thẻ người nhận trắng, viền `border-subtle` | DESIGN.md `surface`, `border-subtle` |
| Bỏ khối "Mai sẽ thấy" và nút gọi điện | N10 chỉ báo kết quả; nội dung xem lại ở nút "Xem lại nội dung" |
| Icon `message-square`, `info`, `eye`, `hand-heart`, `chevron-left` | `DESIGN.md` Từ điển icon (Nhắn tin, Lưu ý, Xem thử, Tab Gia đình, Quay lại) |
| Ràng buộc error | `rule.md` R-TXT, R-TAP, R-ICON-01, R-ONE-01, R-COL-01, R-GES, R-LANG-03 |
