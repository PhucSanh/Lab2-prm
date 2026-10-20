# DLG-WakeTime – nguồn từng đoạn của v0-prompt.txt

| Đoạn prompt | Lấy từ |
| --- | --- |
| CONTEXT | `PRD.md` 11.1 (DLG-WakeTime không có dòng trong 11.2) |
| PURPOSE, tiêu đề "Giờ thức dậy", giờ 1–12, phút, sáng/chiều, Hủy / Xong, mặc định 5:00 sáng | `flutter-handoff.md` dòng 10, 70 và bảng State dòng DLG-WakeTime / DLG-TaskTime |
| **Khác handoff:** thay 3 cột `ListWheelScrollView` + gợi ý "Vuốt để chọn giờ" bằng nút chạm (lưới giờ, hàng phút, Sáng/Chiều) và gợi ý "Chạm vào số Bác muốn" | `PRD.md` FR05 ("không bánh xe cuộn"), NFR04; `AppStyleGuide.md` SG-33, SG-34; `rule.md` R-GES-01 (error). Handoff vẫn cho phép chạm chọn một số |
| Dòng "Bác chọn: 5:00 sáng" | SG-10 (giờ viết kiểu nói); R-COL-01 (không dùng màu làm tín hiệu duy nhất) |
| Nút Hủy / Xong, xếp dọc, 1 nút filled | `vocabulary.md` mục 3 (Cancel/OK → Hủy / Xong); SG-17, SG-20 |
| Icon `sunrise` (Giờ thức dậy), `save` cho "Xong" | `DESIGN.md` Từ điển icon (`circle-check` chỉ cho "Đã xong" nên không dùng cho "Xong") |
| Scrim, dialog trắng, radius 24, padding 24 | `DESIGN.md` components `dialog`, `dialog-scrim`; màn DLG-Done đã chốt |
| Ô chọn: nền `primary-container`, viền đậm | `DESIGN.md` Từ điển icon (`circle-dot`: viền 2 px `primary`), components `option-card-*` |
| CONSTRAINTS | `rule.md` các luật error liên quan |
