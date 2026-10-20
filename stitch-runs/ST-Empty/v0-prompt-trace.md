# ST-Empty – nguồn từng đoạn của v0-prompt.txt

**Biến thể của S03, screen id `cc28fdd64e6e4c70b59b419c44376787`** (màn chốt của S03 = v3; `stitch-runs/S03/log.md` chưa có dòng "Màn chốt" và không có `run.txt`, nên tìm bằng `list_screens`: ảnh "An Nhiên - Hôm nay (Điều chỉnh Navigation)" có md5 trùng `stitch-runs/S03/v3.png`).

| Đoạn prompt | Lấy từ |
| --- | --- |
| Dòng đầu (giữ khung, header, bottom nav, màu, chữ) | mẫu `/stitch-loop` mục 0c |
| Nội dung: "Hôm nay chưa có việc nào", "Bắt đầu nhẹ nhàng với một việc nhỏ.", nút "Thêm việc đầu tiên", nút phụ lịch mẫu, thay danh sách khi không có việc | `flutter-handoff.md` bảng State, dòng ST-Empty; `AppStyleGuide.md` mục 5 "Màn trống" |
| Nút phụ rút từ "Dùng lịch mẫu hoạt động hằng ngày" (7 tiếng) còn "Dùng lịch mẫu" | `AppStyleGuide.md` mục 5 (câu mẫu "Dùng lịch mẫu"); R-TXT-04 (nút ≤ 5 tiếng) |
| Dòng ngày chỉ còn "Thứ Năm, 8/10" | SG-11; SG-24 (không có việc thì không có tiến độ) |
| Vị trí 2 nút ngay trên bottom nav | `DESIGN.md` Layout (nút chính cố định đáy); SG-27 |
| Căn giữa khối trống | SG-25, R-CEN-01 |
| Icon `sun`, `plus`, `layout-list` | `DESIGN.md` Từ điển icon (thêm `layout-list` ngày 18/10/2026) |
| CONSTRAINTS | `rule.md` các luật error liên quan |

Không có "Đọc to" vì R-VOI-01 không áp dụng cho ST-Empty.
