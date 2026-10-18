# v0-prompt-trace – S12 Thêm người thân

PRD.md 11.2 không có dòng cho S12 (chỉ nhắc nút "Thêm người thân" ở S09); nội dung màn lấy từ `flutter-handoff.md` mục S12, `ux/user-flow.md` Flow 5, `design-decisions.md` D12.

| Đoạn prompt | Lấy từ |
| --- | --- |
| Tên app, 360x800, Power 9, persona, nguyên tắc | `PRD.md` 11.1 |
| Bố cục: Back "Gia đình", tiêu đề, nút danh bạ trên cùng, "hoặc tự nhập", Tên gọi, "Là gì của Bác?" 4 lựa chọn Con / Cháu / Bạn bè / Khác, Số điện thoại, Footer "Lưu người thân" | `flutter-handoff.md` S12 Layout; D12 |
| Nhãn nút "Chọn từ danh bạ" (handoff ghi 6 tiếng "Chọn từ danh bạ điện thoại", rút còn 4) | R-TXT-04 `[N]` |
| Xưng "Bác" thay "bà" | SG-01 |
| Thay hàng công tắc "Gọi nhanh" bằng một dòng chú thích "Chỉ gửi tin khi Bác chọn gửi." (Từ điển icon chưa có icon cho công tắc gọi nhanh; `phone` chỉ cho hành động gọi) | SG-50, `flutter-handoff.md` S12; `[N]` |
| Gợi ý "Ví dụ: 0912 345 678" | handoff S12 States; SG-15 |
| Ô nhập cao 60, nhãn trên ô | `DESIGN.md` `text-field` |
| Ô lựa chọn: viền 2px primary + circle-dot khi chọn, circle khi chưa | `DESIGN.md` Từ điển icon (Đang chọn / Chưa) |
| Khối ICONS | `DESIGN.md` Từ điển icon (đã thêm dòng `contact` – Chọn từ danh bạ, 17/10/2026) |
| Token màu, font, lề 20, bo góc, cấm gradient | `assets/stitch/DESIGN.md` |
| Chữ >= 20, 24/30/22 | R-TXT-01/02 |
| Tương phản, tràn ngang | R-CON-01, R-LAY-01 |
| Vùng chạm, nút chính 60 ở đáy | R-TAP-01/02 |
| Câu <= 15, nút <= 5 tiếng | R-TXT-03/04 |
| 1 nút filled | R-ONE-01 |
| Icon luôn có nhãn | R-ICON-01/02/03 |
| Từ cấm | `vocabulary.md` mục 5 (người chăm sóc…), R-VOC-01, R-LANG-03 |
| Không vuốt/ba chấm | `PRD.md` 11.4, R-GES-01 |
