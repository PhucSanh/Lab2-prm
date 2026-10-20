# S03b – nguồn từng đoạn của v0-prompt.txt

**Biến thể của S03, screen id `cc28fdd64e6e4c70b59b419c44376787`** (màn chốt của S03 = v3; xác định bằng `list_screens`, md5 ảnh trùng `stitch-runs/S03/v3.png`, xem `stitch-runs/ST-Empty/v0-prompt-trace.md`).

| Đoạn prompt | Lấy từ |
| --- | --- |
| Dòng đầu (giữ khung, header, bottom nav, màu, chữ) | mẫu `/stitch-loop` mục 0c |
| Bối cảnh: S03b = Hôm nay sau khi xong 1 việc, snackbar "Hoàn tác" | `CHIA-VIEC.md` dòng A07 (Nguồn: `ux/user-flow.md` Flow 3); luồng demo S04 → DLG-Done → S03b |
| "Đã xong 4/6 việc" (3 → 4) | `AppStyleGuide.md` mục 5 "Lời chào", SG-24; PRD.md 11.2 (S03: "Đã xong 3/6 việc") |
| Việc tiếp theo chuyển sang "3 giờ chiều · Uống trà với cô Tám · Trà chiều cùng bạn" | Danh sách việc của S03 v3 (việc chưa làm kế tiếp); `vocabulary.md` mục 1 (Trà chiều cùng bạn, `coffee`) |
| Chip "Đã xong" nền `primary`, chữ trắng, icon 24 px | `DESIGN.md` `status-done`, SG-23, R-STA-01 |
| Snackbar "Đã ghi: Đi bộ xong lúc 9:42 sáng." + "Hoàn tác" | `AppStyleGuide.md` mục 5 "Xong việc (snackbar)"; SG-36, SG-37 (không tự tắt); `DESIGN.md` `snackbar` (nền `on-surface`, bo 12, padding 16) |
| Nút "Hoàn tác" dạng nút viền 48 px có icon `undo-2` 32 px | R-TAP-01 (≥ 48 px), R-ICON-01/02; `DESIGN.md` Từ điển icon (`undo-2` = Hoàn tác) |
| Icon `circle-check`, `coffee`, `undo-2` | `DESIGN.md` Từ điển icon; `vocabulary.md` mục 1 |
| CONSTRAINTS | `rule.md` các luật error liên quan |

Việc "Đọc to" (R-VOI-01) không áp dụng. Quyết định: snackbar đặt trên nút "Đã xong" cố định (không che bottom nav).
