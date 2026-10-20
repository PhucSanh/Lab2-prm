# ST-Validation – nguồn từng đoạn của v0-prompt.txt

**Biến thể của S06, screen id `02520b9aa5a143b29ab1239cb2917908`** (màn chốt S06 = v0, 94 điểm; id ghi trong `stitch-runs/S06/log.md` và `run.txt`). Theo `--from S06`.

| Đoạn prompt | Lấy từ |
| --- | --- |
| Dòng đầu | mẫu `/stitch-loop` mục 0c |
| Bối cảnh: bấm "Lưu việc này" khi tên trống | `CHIA-VIEC.md` A17; `flutter-handoff.md` S06 States ("Validation: tên trống → viền `error`, icon, chữ lỗi, chip gợi ý") và dòng ST-Validation |
| Lỗi 3 phần: ⓘ "Bác chưa nhập tên việc." / "Ví dụ: Đi bộ buổi sáng" / chip gợi ý | `AppStyleGuide.md` mục 5 "Lỗi nhập" |
| Chip gợi ý "Tập thở chậm 10 phút", "Ngủ trưa 20 phút" | `flutter-handoff.md` S06 (gợi ý "Ví dụ: Tập thở 10 phút, Ngủ trưa 20 phút"), `ux/user-flow.md` Flow 2 |
| Nền ô lỗi `error-container` #FDECE9, viền `error` #B42318, `circle-alert` | `DESIGN.md` `text-field-error`, Từ điển icon (Lỗi nhập) |
| Chỉ 1 nút filled, chip viền | `rule.md` R-ONE-01 |
| CONSTRAINTS | `rule.md` các luật error |
