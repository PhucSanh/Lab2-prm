# DESIGN.md – An Nhiên

## 1. Prompt gốc dùng trong Google Stitch (v0, nguyên văn)

> Chế độ: **Mobile** · Công cụ: Google Stitch (stitch.withgoogle.com) · Ảnh output lưu ngày 11/10/2026

```
Design a mobile app (Android, 360x800 dp) called "An Nhiên" – a daily schedule app for elderly Vietnamese users (65+), based on the Blue Zones "Power 9" habits: move naturally, purpose, down shift, 80% rule, plant slant, afternoon tea with friends, belong, loved ones first, right tribe.
Persona: Mrs. Lan, 68, retired teacher, presbyopia, low finger dexterity, only uses Zalo and YouTube, forgets meal and walking times.
Tasks: see today's activities, mark an activity as done, add a new activity with time and reminder, view the weekly schedule, learn the 9 habits, call family.
Screens: Welcome with font-size choice, Profile setup, Today (home), Activity detail, Add activity step 1 (choose habit) and step 2 (time, repeat, reminder), Weekly schedule, 9 Habits library, Family, Display settings.
Constraints: all UI text in Vietnamese; body text at least 18sp; touch targets at least 56dp; contrast at least 4.5:1; every icon has a visible text label; bottom navigation with 4 labeled tabs; no swipe-only or long-press gestures; one primary action per screen.
Style: calm, warm and natural; cream background, deep green primary, terracotta accent; rounded cards; Be Vietnam Pro font; no gradients.
```

Thành phần của prompt theo yêu cầu đề:

| Thành phần | Nội dung trong prompt |
| --- | --- |
| Persona | Bà Lan, 68 tuổi, viễn thị, ngón tay kém linh hoạt, hay quên |
| Task | Xem việc hôm nay, đánh dấu xong, thêm việc, xem lịch tuần, học 9 thói quen, gọi người thân |
| Platform | Android mobile, 360 × 800 dp |
| Constraints | Chữ ≥ 18 sp, chạm ≥ 56 dp, contrast ≥ 4.5:1, icon có nhãn, 4 tab, không cử chỉ ẩn |
| Design style | Ấm, tự nhiên; nền kem, xanh lá đậm, điểm nhấn đất nung; bo tròn; Be Vietnam Pro |

Ảnh output đầu tiên: `assets/stitch/screen_day.png`, `screen_week.png`, `power9.png`, `screen_contact.png` và bảng màu `bang_mau.png`. Các vòng lặp xem [ai/ai-design-log.md](ai/ai-design-log.md).

> Prompt trên giữ nguyên để làm bằng chứng v0. Bản Figma cuối đã đi xa hơn prompt: nền đổi sang xanh bạc hà nhạt, bỏ màu đất nung, chữ lớn hơn (xem mục 3 và [design-decisions.md](design-decisions.md) D20–D22).

## 2. Nguyên tắc thiết kế cho người cao tuổi

1. **Đọc được ngay:** chữ nội dung 24, nhỏ nhất 20 (kể cả nhãn bottom nav và chú thích), tiêu đề màn 30; tương phản chữ chính 13.6 : 1.
2. **Chạm trúng ngay:** nút chính cao 60 dp (component `Button` Primary 60, Secondary 63), mọi vùng chạm ≥ 48 dp, các nút cách nhau ≥ 8 dp.
3. **Không phải đoán:** mọi icon điều hướng có chữ; nút Back ghi "Quay lại" hoặc tên màn trước.
4. **Một việc mỗi màn:** mỗi màn có tối đa 1 nút filled; Home chỉ nổi bật "Việc tiếp theo".
5. **Chọn giờ chắc tay:** giờ hiện thành một ô bấm được (◷ 8 : 00 sáng ⌄); bấm vào mới mở hộp chọn giờ (giờ 1–12, phút 00–59, sáng/chiều). Hộp mở đúng giá trị đã lưu, **Hủy** không lưu gì, chỉ **Xong** mới ghi lại. Không có cử chỉ nào là cách duy nhất: mọi lựa chọn đều chạm được.
6. **Không sợ sai:** hỏi lại trước khi đánh dấu xong, xóa, ngưng lịch lặp; mọi thay đổi có "Hoàn tác"; sửa/xóa việc lặp lại luôn hỏi phạm vi (chỉ lần này / từ lần này về sau / tất cả).
7. **Lời lẽ đời thường:** xưng "Bác" trong lời chào và nút, "bà/ông" theo lựa chọn ở S02; không dùng từ kỹ thuật như sync, task hay notification.
8. **Người lớn tuổi quyết định:** người thân chỉ gửi *gợi ý*; lịch chỉ đổi khi Bác bấm nhận. App không tự gửi kết quả hay việc bỏ qua cho con cháu.
9. **Nói thật về những gì app biết:** dữ liệu lưu trên điện thoại, dùng được khi mất mạng; khi chia sẻ qua Zalo/SMS, app chỉ nói "đã mở ứng dụng nhắn tin", không khẳng định "đã gửi".

## 3. Design tokens

Tạo trong Figma bằng **Variables** (collection `color`, `space`, `radius` + các collection trạng thái của prototype), **Text styles** và **Effect styles**. Các giá trị dưới đây đọc trực tiếp từ file Figma ngày 15/10/2026.

### 3.1 Color

| Token | Hex | Dùng cho | Contrast |
| --- | --- | --- | --- |
| `bg` | `#F6F7F2` | Nền app | — |
| `surface` | `#FFFFFF` | Thẻ, bottom nav, dialog | — |
| `on-surface` | `#202B25` | Chữ chính | 13.60 : 1 trên `bg` |
| `on-surface-variant` | `#526057` | Chữ phụ, nhãn tab chưa chọn | 6.15 : 1 trên `bg` |
| `primary` | `#1F684B` | Nút chính, viền focus, tab đang chọn | 6.21 : 1 trên `bg`; chữ trắng trên nó 6.69 : 1 |
| `primary-pressed` | `#18533C` | Nút chính khi nhấn | — |
| `primary-container` | `#D6EADF` | Ô đang chọn, banner thành công | chữ `#174C37` 7.85 : 1 |
| `primary-container-soft` | `#E7F2EB` | Khung xem trước, hàng "đang đọc to" | chữ `#174C37` 8.61 : 1 |
| `on-primary-container` | `#174C37` | Chữ trên `primary-container` | — |
| `secondary` | `#1F684B` | Trùng `primary` (đã bỏ màu đất nung, xem D21) | — |
| `error` | `#B42318` | Viền, icon, nút nguy hiểm | 6.11 : 1 trên `bg`; chữ trắng 6.57 : 1 |
| `error-container` | `#FDECE9` | Nền khối lỗi | chữ `#912018` 7.57 : 1 |
| `warning-container` | `#FFF3DB` | Nhắc nhở nhẹ | chữ `#8A5100` 5.86 : 1 |
| `success` | `#1F684B` | Chữ "Đã xong" | 6.21 : 1 trên `bg` |
| `outline` | `#7B887F` | Viền ô nhập, nút viền | 3.44 : 1 trên `bg` (UI control ≥ 3 : 1) |
| `border-subtle` | `#DFE5DF` | Đường chia, viền thẻ | Trang trí, không mang thông tin |
| `border-strong` | `#A0ACA3` | Viền thẻ chọn chưa chọn | Đi kèm chữ, không là tín hiệu duy nhất |
| `disabled-bg` / `disabled-fg` | `#E6EAE5` / `#627067` | Nút tắt | 4.28 : 1 (miễn trừ WCAG 1.4.3) |
| `scrim` | `#0F1411` | Nền mờ sau dialog | — |

Màu nhận diện 9 thói quen (collection `color/habit/*`) dùng cặp nền nhạt + icon đậm. Màu chỉ là tín hiệu phụ: mỗi thói quen luôn có icon và tên riêng.

| Thói quen | Token | Nền | Icon/chữ | Contrast |
| --- | --- | --- | --- | --- |
| 1 Vận động tự nhiên | `move` | `#D7EDE0` | `#0F3D2A` | 9.92 : 1 |
| 2 Sống có mục đích | `purpose` | `#E3E7F8` | `#26357A` | 9.11 : 1 |
| 3 Thư giãn mỗi ngày | `downshift` | `#EDE4F6` | `#4B2A73` | 9.07 : 1 |
| 4 Ăn vừa đủ | `eighty` | `#FFF1D6` | `#7A4E00` | 6.45 : 1 |
| 5 Ăn nhiều rau, đậu | `plant` | `#E2F0D2` | `#2F5214` | 7.54 : 1 |
| 6 Trà chiều cùng bạn | `tea` | `#F6E6DA` | `#7A3412` | 7.41 : 1 |
| 7 Gắn kết cộng đồng | `belong` | `#E0EEF2` | `#154A5A` | 8.19 : 1 |
| 8 Gia đình trên hết | `family` | `#FCE4E1` | `#8C1D18` | 7.52 : 1 |
| 9 Bạn bè tích cực | `tribe` | `#F3E7EF` | `#6B1F4E` | 9.06 : 1 |

### 3.2 Typography – Text styles (font **Be Vietnam Pro**)

| Style | Size / line-height | Weight | Dùng cho |
| --- | --- | --- | --- |
| `display` | 34 / 42 | Bold | Tên app ở S01, giờ ở S14 |
| `headline` | 30 / 140 % | Bold | Tiêu đề màn hình |
| `numeric-lg` | 30 / 38 | Bold | Số giờ trong ô chọn giờ, mã ghép nối |
| `title-md` | 26 / 140 % | Bold | Tên việc, tiêu đề mục, tiêu đề dialog |
| `title-lg` | 24 / 32 | Bold | Tên việc trong thẻ |
| `body-lg-strong` | 26 / 140 % | SemiBold | Câu nhấn trong nội dung |
| `body-lg` | 24 / 140 % | Regular | Nội dung chính |
| `input` | 24 / 140 % | Regular | Chữ trong ô nhập |
| `label-btn` | 22 / 140 % | Bold | Chữ trên nút |
| `body-md` / `body-md-strong` | 20 / 140 % | Regular / SemiBold | Chữ phụ, gợi ý, nhãn ô nhập |
| `caption` | 20 / 140 % | Regular | Ghi chú nhỏ nhất (vẫn 20) |
| `label-nav` / `label-nav-active` | 20 / 140 % | SemiBold / Bold | Nhãn bottom nav |

Ngoài ra có collection **`Dễ đọc · Cỡ chữ`** (body 24, support 20, heading 30, section 26, button 22, nav 20) – đây là mức mặc định. Ba mức người dùng chọn ở S01 và S10:

| Mức | Nội dung | Tiêu đề | Nút |
| --- | --- | --- | --- |
| Vừa | 20 | 28 | 20 |
| Lớn (mặc định) | 24 | 30 | 22 |
| Rất lớn | 28 | 32 | 24 |

Figma hiện chỉ dựng mode mặc định (Lớn); hai mức còn lại là đặc tả cho bản Flutter.

### 3.3 Spacing – collection `space`

`4 · 8 · 12 · 16 · 20 · 24 · 32 · 48` (dp). Lề màn hình = `20`; khoảng cách giữa các khối = `16`; khoảng cách giữa 2 nút ≥ `8`.

### 3.4 Radius – collection `radius`

| Token | Giá trị | Dùng cho |
| --- | --- | --- |
| `sm` | 8 | Chip nhỏ |
| `md` | 12 | Ô nhập, list row |
| `button` | 14 | Nút 60 dp |
| `lg` | 16 | Card |
| `xl` | 24 | Dialog |
| `full` | 999 | Pill, avatar, nút tròn |

### 3.5 Elevation – Effect styles

| Token | Dùng cho |
| --- | --- |
| (không bóng, viền `border-subtle`) | List row, bottom nav |
| `elevation/1` | Card |
| `elevation/2` | Dialog, popup gợi ý G11 |

### 3.6 Biến trạng thái cho prototype

Figma dùng thêm các collection để prototype "nhớ" lựa chọn: `Wake-up time picker`, `Bánh xe giờ · giữa cố định` (giờ/phút/sáng-chiều cho giờ thức dậy và giờ làm), `Profile address` (Ông/Bà), `Welcome · live text size preview`, `MVP · form state` (tên việc, ngày, lặp lại 7 ngày, phạm vi sửa/xóa), `Tin nhắn do Bác chọn`, `Lịch người thân gợi ý`, `Gợi ý mới · Popup`. Đây là trạng thái mô phỏng, không phải token thiết kế; bản Flutter thay bằng state thật (xem flutter-handoff.md).

## 4. Layout

- Frame: 360 × 800 dp; lề 20.
- Cấu trúc mỗi màn: App bar → Main (Fill, cuộn dọc) → Bottom nav cố định (màn tab) hoặc Footer chứa nút chính, có safe area.
- Mọi khối dùng Auto Layout; chiều ngang các khối nội dung là **Fill container**, nhờ đó khung 412 dp tự giãn (frame kiểm tra: `S03 Hôm nay · 412 dp`).

## 5. Components (page `05 Components`)

| Nhóm | Component | Variants / properties |
| --- | --- | --- |
| Button | `Button` (set) | Type = Primary · Secondary · Tonal · Text · Danger · Danger-outline; State = Default · Pressed · Disabled; `Label`, `Show icon` |
| Text field | `TextField` (set) | State = Default · Focused · Error; `Label`, `Value`, `Helper` |
| Card | `TaskCard`, `TaskRow` (set) | TaskRow: State = Upcoming · Done · Skipped; `Time`, `Title` |
| Navigation | `NavItem`, `BottomNav` (set) | NavItem: State = Active · Inactive; BottomNav: Active = Today · Week · Habits · Family |
| App bar | `AppBar` (set) | Type = Back · Back+Step · Back+Action · Greeting; `BackLabel`, `Step`, `Title`, `ActionLabel`, `Date` |
| Dialog | `Dialog` | Dùng cho DLG-*, C08w, C11, C12 |
| Snackbar | `Snackbar` (set) | Tone = Success · Info; `Message`, `ActionLabel`, `Show action` |
| Loading | `Loading` | Toàn màn / trong nút |
| Empty | `EmptyState` | `Title`, `Message`, `Action` |
| Error | `ErrorView` (set) | Type = Full-screen · Banner |
| Phụ | `HabitTile` (Selected), `Switch` (On), `TimeStepper` | `TimeStepper` còn trong thư viện nhưng màn cuối đã thay bằng ô chọn giờ + DLG-TaskTime |
| Icon | 34 icon `icon/*` | home, calendar, leaf, users, bell, phone, clock, undo, trash, pencil, send… |
