# ST-Loading – nguồn từng đoạn của v0-prompt.txt

| Đoạn prompt | Lấy từ |
| --- | --- |
| CONTEXT (app, Bà Lan, nguyên tắc, xưng "Bác", câu ≤ 15 tiếng) | `PRD.md` 11.1 |
| PURPOSE, nội dung màn ("Đang lưu việc…", "Không cần bấm gì thêm", không nút, tự chuyển khi xong) | `flutter-handoff.md` bảng State, dòng ST-Loading (ST-Loading không có dòng trong `PRD.md` 11.2); luồng `ux/user-flow.md` Flow 2 (S06 → ST-Loading → ST-Saved); nguồn nhãn "Lưu việc này": `AppStyleGuide.md` SG-16 |
| LAYOUT: căn giữa cả hai chiều, chữ căn giữa | `AppStyleGuide.md` SG-25; `rule.md` R-CEN-01 |
| Vòng tròn tiến trình 88 px | `flutter-handoff.md` (CircularProgressIndicator 88); icon `loader-circle` thêm vào `DESIGN.md` "Từ điển icon" ngày 18/10/2026 |
| Cỡ chữ 30 / 24, màu | `DESIGN.md` typography `headline` 30/700, `body-lg` 24/400; colors `on-surface`, `on-surface-variant`, `primary`, `primary-container` |
| Khoảng cách 32 / 12, lề 20 | `DESIGN.md` spacing `xl` 32, `md` 12, `screen` 20 |
| STYLE TOKENS (phẳng, không gradient/bóng) | `DESIGN.md` Elevation & Depth, Do's and Don'ts |
| ICONS | `DESIGN.md` mục "Từ điển icon" (dòng mới `loader-circle`), mẫu khối ICONS của `/stitch-loop` |
| CONSTRAINTS | `rule.md`: R-TXT-01, R-TXT-03, R-CON-01, R-LAY-01, R-ICON-01/02, R-GES-01, R-LANG-01/03, R-VOC-01, R-CEN-01 |
| Không được sinh | `PRD.md` 11.4; `vocabulary.md` mục 5 (technical: đồng bộ, sao lưu, thiết bị) |

Không có bottom nav / nút: màn trạng thái toàn màn hình, nên R-NAV-01, R-TAP-02, R-ONE-01 không áp dụng.
