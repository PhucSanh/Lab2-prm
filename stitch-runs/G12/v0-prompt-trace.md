# G12 – nguồn từng đoạn của v0-prompt.txt

**Biến thể của S03, screen id `cc28fdd64e6e4c70b59b419c44376787`** (màn chốt của S03 = v3; xác định như `stitch-runs/S03b/v0-prompt-trace.md`; `get_screen` xác nhận screen tồn tại, tiêu đề "An Nhiên - Hôm nay (Điều chỉnh Navigation)").

| Đoạn prompt | Lấy từ |
| --- | --- |
| Dòng đầu (giữ khung, header, bottom nav, màu, chữ) | mẫu `/stitch-loop` mục 0c |
| Bối cảnh: Bác bấm "Để sau" ở popup G11 → thẻ G12 ở đầu Hôm nay | `flutter-handoff.md` S03 Interactions và G01–G12; `ux/user-flow.md` mục 14; D29 |
| Tiêu đề thẻ "Mai gửi Bác 2 việc" | `flutter-handoff.md` G01–G12 (thẻ "Mai gửi Bác 2 việc · Xem gợi ý" ở đầu S03); `AppStyleGuide.md` mục 5 "Gợi ý từ người thân" |
| Dòng "Chưa thêm vào lịch. Bác tự chọn." | `AppStyleGuide.md` mục 5 (rút gọn theo PRD 11.2 #3); lịch chỉ đổi khi Bác nhận (P4) |
| Nút viền "Xem gợi ý" (không filled) | `CHIA-VIEC.md` A43; R-ONE-01, R-ONE-02; nút filled duy nhất là "Đã xong" |
| Icon `mail`, `eye` | `DESIGN.md` Từ điển icon (thêm `mail` 19/10/2026, mở rộng `eye` cho "Xem gợi ý") |
| Ô 48x48 nền #1F684B | `DESIGN.md` primary; không dùng màu nhấn thói quen vì thẻ không phải thói quen |
| CONSTRAINTS | `rule.md` các luật error liên quan |

R-VOI-01 (Đọc to) áp dụng cho G03, không áp dụng cho thẻ G12.
