# v0-prompt-trace – S09b Gia đình · đã thêm người thân

Biến thể của S09, screen id `2bac776f261e4f8986ee3bc3d86053a2` (project 2013215887278758682). Dùng `edit_screens`, không `generate_screen_from_text`.

| Đoạn prompt | Lấy từ |
| --- | --- |
| Dòng đầu "Keep the overall layout…" | lệnh `/stitch-loop` mục 0c |
| Banner thành công `primary-container` viền `primary`, "Đã thêm Cháu Bin", không tự tắt, thẻ mới ở cuối | `flutter-handoff.md` mục S09 (States – S09b); `ux/user-flow.md` Flow 5 |
| Dòng phụ "Bác có thể gọi hoặc nhắn tin ngay." | tự soạn theo `AppStyleGuide.md` (xưng "Bác", ≤ 15 tiếng); SG-48/49 không nói "đã gửi" |
| Icon `save` cho banner | `DESIGN.md` Từ điển icon (Lưu); ST-Saved cũng dùng `save` |
| Bỏ icon message-circle cạnh dòng "Bác chọn điều muốn kể cho con" | chưa có nghĩa trong Từ điển icon (R-ICON-03) |
| `info` cho "Gợi ý từ Mai" | Từ điển icon (Lưu ý, gợi ý) |
| Avatar chữ cái thay icon `user` | `flutter-handoff.md` S09 (avatar chữ cái); `user` đã là "Tên Bác, hồ sơ" |
| Tab Gia đình `hand-heart` | Từ điển icon (Điều hướng); `users` là thói quen Gắn kết cộng đồng |
| Nền phẳng sau nút "Thêm người thân" | sửa warn R-STY-02 của S09 (`stitch-runs/S09/log.md`) |
| Viền Bin 2px, không badge | tự quyết, giữ ít chữ (R-TXT-03) |
| Ràng buộc error | `rule.md` R-TXT, R-TAP, R-ICON-01, R-ONE-01, R-COL-01, R-GES |
