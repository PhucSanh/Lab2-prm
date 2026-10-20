# v0-prompt-trace – S12e Thêm người thân · số sai

Biến thể của S12, screen id `4e54d2bf87a94c40a1c7a3e56e05aa3f` (màn chốt v1, 100 điểm).

| Đoạn prompt | Lấy từ |
| --- | --- |
| Dòng đầu giữ khung | `/stitch-loop` mục 0c |
| Trạng thái lỗi "Thiếu / sai số (S12e)", giữ nguyên tên và quan hệ | `flutter-handoff.md` S12 mục States; `ux/user-flow.md` Flow 5 |
| Câu lỗi "Bác chưa nhập số điện thoại." (handoff ghi "Bà", đổi sang "Bác" cho khớp cả màn) | `flutter-handoff.md` S12; R-LANG-02 |
| Lỗi 3 phần: icon + câu + ví dụ + gợi ý danh bạ | `AppStyleGuide.md` mục lỗi nhập; R-SAFE-02; `DESIGN.md` text-field-error |
| Màu lỗi #B42318 / #FDECE9 | `DESIGN.md` colors |
| Khối ICONS (circle-alert, contact, ...) | `DESIGN.md` Từ điển icon |
| Luật chữ / tương phản / tràn ngang / nút filled duy nhất | R-TXT-01, R-CON-01, R-LAY-01, R-ONE-01 |

Ghi chú: tên màn ghi "số sai" nhưng flow/handoff mô tả lỗi là **chưa nhập số** (trạng thái trống). Bản này làm trường hợp trống.
