# AI Design Log – Google Stitch

> **Cách ghi log:** mỗi lần chạy giữ nguyên văn prompt, lưu ảnh output gốc vào `assets/stitch/` và ghi nhận xét theo ảnh thật.
> Các ô `[ … ]` là chỗ bạn điền sau khi chạy Stitch. Không viết nhận xét cho thứ Stitch không tạo ra.

| Vòng | Mục tiêu | Ngày | Ảnh trước | Ảnh sau |
| --- | --- | --- | --- | --- |
| v0 | Sinh UI ban đầu từ persona + constraints | [NGÀY] | — | `assets/stitch/v0-home.png`, `v0-*.png` |
| V1 | Đọc dễ: cỡ chữ, vùng chạm, tương phản | [NGÀY] | `v0-home.png` | `v1-home.png` |
| V2 | Điều hướng đơn giản: tab có nhãn, bỏ cử chỉ ẩn | [NGÀY] | `v1-home.png` | `v2-home.png` |
| V3 | Chống lỗi & phục hồi: dialog, validation, loading, offline | [NGÀY] | `v2-add.png` | `v3-add.png`, `v3-error.png` |

---

## v0 – Sinh UI ban đầu

**Prompt (nguyên văn):**

```
Design a mobile app (Android, 360x800 dp) called "An Nhiên" – a daily schedule app for elderly Vietnamese users (65+), based on the Blue Zones "Power 9" habits: move naturally, purpose, down shift, 80% rule, plant slant, afternoon tea with friends, belong, loved ones first, right tribe.
Persona: Mrs. Lan, 68, retired teacher, presbyopia, low finger dexterity, only uses Zalo and YouTube, forgets meal and walking times.
Tasks: see today's activities, mark an activity as done, add a new activity with time and reminder, view the weekly schedule, learn the 9 habits, call family.
Screens: Welcome with font-size choice, Profile setup, Today (home), Activity detail, Add activity step 1 (choose habit) and step 2 (time, repeat, reminder), Weekly schedule, 9 Habits library, Family, Display settings.
Constraints: all UI text in Vietnamese; body text at least 18sp; touch targets at least 56dp; contrast at least 4.5:1; every icon has a visible text label; bottom navigation with 4 labeled tabs; no swipe-only or long-press gestures; one primary action per screen.
Style: calm, warm and natural; cream background, deep green primary, terracotta accent; rounded cards; Be Vietnam Pro font; no gradients.
```

**Output:** ![v0 home](../assets/stitch/v0-home.png)

**Stitch tạo ra:** [liệt kê số màn, tên màn Stitch thực sự sinh ra]

**Điểm tốt giữ lại:** [ví dụ: bảng màu xanh lá – kem đúng hướng, có card "Việc tiếp theo"]

**Vấn đề thấy được:** [ghi theo ảnh thật – đối chiếu checklist phát hiện ở cuối file]

---

## V1 – Đọc dễ (Readability & accessibility)

**Vấn đề nhắm tới:** [ví dụ: chữ nội dung còn ~14 sp, chữ phụ xám nhạt, nút cao ~40 dp]

**Prompt (nguyên văn):**

```
Increase all body text to 18sp and screen titles to 28sp. Make every button at least 56dp tall with 8dp spacing between buttons. Darken secondary grey text to #4A5550 so contrast is above 7:1 on the cream background. Replace the time-picker wheel with large minus/plus buttons.
```

**Trước / sau:**

| Trước | Sau |
| --- | --- |
| ![](../assets/stitch/v0-home.png) | ![](../assets/stitch/v1-home.png) |

**Kết quả:** [Stitch đã sửa được gì / chưa sửa được gì]

**Quyết định:** [Accept / Modify / Reject – lý do] → thay đổi tương ứng trong Figma: `03 Final UI / S03`, text styles `body-lg`, `headline`.

---

## V2 – Điều hướng đơn giản (Navigation & recognition)

**Vấn đề nhắm tới:** [ví dụ: bottom nav 5 tab chỉ có icon; hoàn thành việc bằng cách vuốt thẻ; không có nút quay lại có chữ]

**Prompt (nguyên văn):**

```
Reduce the bottom navigation to exactly 4 tabs, each with an icon and a visible Vietnamese label: Hôm nay, Lịch tuần, Thói quen, Gia đình. Move Settings to a labeled button in the top app bar. Replace swipe-to-complete with a visible "Đã xong" button on the next-activity card. Add a labeled back button ("Quay lại") on every sub-screen.
```

**Trước / sau:**

| Trước | Sau |
| --- | --- |
| ![](../assets/stitch/v1-home.png) | ![](../assets/stitch/v2-home.png) |

**Kết quả:** [ … ]

**Quyết định:** [ … ] → Figma: component `BottomNav`, `AppBar` (Type = Back+Step).

---

## V3 – Chống lỗi & phục hồi (Error prevention & recovery)

**Vấn đề nhắm tới:** [ví dụ: bấm "Đã xong" là đổi ngay không hỏi lại; bấm Lưu không có phản hồi; không có màn lỗi]

**Prompt (nguyên văn):**

```
Add a confirmation dialog before marking an activity as done, with two stacked full-width buttons "Đúng, đã xong" and "Chưa, để sau". On the add-activity screen, show inline validation when the task name is empty: red border, error icon, the message "Bà chưa nhập tên việc. Ví dụ: Tập thở chậm 10 phút." and two suggestion chips. Add a loading screen "Đang lưu việc…" and an offline error screen that says the data is not lost, with buttons "Thử lại", "Lưu trên máy, gửi sau" and "Quay lại sửa".
```

**Trước / sau:**

| Trước | Sau |
| --- | --- |
| ![](../assets/stitch/v2-add.png) | ![](../assets/stitch/v3-add.png) |

**Kết quả:** [ … ]

**Quyết định:** [ … ] → Figma: component `Dialog`, `TextField` State = Error, `Loading`, `ErrorView`; frames `ST-Validation`, `ST-Loading`, `ST-Error`.

---

## Phản biện UX (≥ 5 phát hiện, gắn màn cụ thể)

> Bảng dưới là các lỗi thường gặp ở output AI cho đối tượng người già. **Chỉ giữ những dòng đúng với ảnh Stitch của bạn**, sửa mô tả cho khớp ảnh thật, và thêm dòng nếu thấy lỗi khác.

| # | Màn hình | Vấn đề quan sát | Căn cứ | Mức độ | Sửa ở | Trạng thái |
| --- | --- | --- | --- | --- | --- | --- |
| F1 | S03 Hôm nay | Chữ nội dung ~14 sp, chữ phụ xám nhạt khó đọc | Accessibility (WCAG 1.4.3); persona viễn thị | Cao | V1 | [ ] |
| F2 | Bottom nav | 5 tab, chỉ có icon, không có nhãn | Nielsen #6 Recognition rather than recall | Cao | V2 | [ ] |
| F3 | S03 Hôm nay | Hoàn thành việc bằng cách vuốt thẻ, không có nút | Nielsen #5 Error prevention; ngón tay kém linh hoạt | Cao | V2 | [ ] |
| F4 | S06 Chọn giờ | Bánh xe chọn giờ nhỏ, dễ cuộn quá | Touch target < 48 dp; motor | Trung bình | V1 | [ ] |
| F5 | S06 Chọn giờ | Bấm Lưu không có phản hồi, không có trạng thái đang lưu | Nielsen #1 Visibility of system status | Cao | V3 | [ ] |
| F6 | S04 Chi tiết | "Đã xong" chỉ thể hiện bằng đổi màu + gạch ngang | WCAG 1.4.1 Use of color | Trung bình | V3 | [ ] |
| F7 | S06 Chọn giờ | Placeholder thay cho nhãn ô nhập, gõ vào là mất | Nielsen #6; NN/g về form | Trung bình | V1 | [ ] |
| F8 | S08 / S05 | Giữ nguyên "Wine @ 5" (uống rượu) cho người già | Persona + an toàn sức khỏe | Trung bình | Figma (modify) | [ ] |

## Truy vết một thay đổi end-to-end (dùng khi demo bước 6)

| Bước | Nội dung |
| --- | --- |
| Prompt | V2 – "Replace swipe-to-complete with a visible 'Đã xong' button…" |
| AI output | `assets/stitch/v2-home.png` – [mô tả Stitch đã đổi gì] |
| Critique | F3: cử chỉ vuốt bị ẩn, người tay run dễ vuốt nhầm |
| Decision | Reject cử chỉ vuốt → nút "Đã xong" 56 dp + dialog xác nhận (design-decisions.md, D2) |
| Figma | `03 Final UI / S03` thẻ Việc tiếp theo; `05 Components / Button`; `06 Prototype` Flow 3 |
