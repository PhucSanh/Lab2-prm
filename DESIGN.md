# DESIGN.md – An Nhiên

## 1. Prompt gốc dùng trong Google Stitch (v0, nguyên văn)

> Chế độ: **Mobile** · Công cụ: Google Stitch (stitch.withgoogle.com) · Ngày chạy: [NGÀY]

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

Ảnh output đầu tiên: `assets/stitch/v0-*.png`. Các vòng lặp xem [ai/ai-design-log.md](ai/ai-design-log.md).

## 2. Nguyên tắc thiết kế cho người cao tuổi

1. **Đọc được ngay:** chữ nội dung 18 sp, nhỏ nhất 16 sp (nhãn nav 15 sp), tiêu đề 28 sp; tương phản chữ chính 14:1.
2. **Chạm trúng ngay:** nút chính cao 56–60 dp, các nút cách nhau ≥ 8 dp.
3. **Không phải đoán:** mọi icon điều hướng có chữ; nút Back ghi "Quay lại" hoặc tên màn trước.
4. **Một việc mỗi màn:** mỗi màn có tối đa 1 nút filled; Home chỉ nổi bật "Việc tiếp theo".
5. **Không cử chỉ ẩn:** không vuốt, không nhấn giữ; chọn giờ bằng nút −/+ thay cho bánh xe.
6. **Không sợ sai:** hỏi lại trước khi đánh dấu xong; lỗi nói rõ dữ liệu không bị mất và việc cần làm tiếp.
7. **Lời lẽ đời thường:** xưng "bà/ông", không dùng từ kỹ thuật như sync, task hay notification.

## 3. Design tokens

Tạo trong Figma bằng **Variables** (color, space, radius), **Text styles** và **Effect styles**.

### 3.1 Color – collection `color`

| Token | Hex | Dùng cho | Contrast (đã đo) |
| --- | --- | --- | --- |
| `bg` | `#FBF8F2` | Nền app | — |
| `surface` | `#FFFFFF` | Thẻ, bottom nav, dialog | — |
| `on-surface` | `#1F2A24` | Chữ chính | 14.0 : 1 trên `bg` |
| `on-surface-variant` | `#4A5550` | Chữ phụ, nhãn tab chưa chọn | 7.32 : 1 trên `bg` |
| `primary` | `#1F6B4A` | Nút chính, viền focus | 6.08 : 1 trên `bg`; chữ trắng trên nó 6.44 : 1 |
| `primary-container` | `#D7EDE0` | Tab đang chọn, ô đang chọn | chữ `#0F3D2A` trên nó 9.92 : 1 |
| `on-primary-container` | `#0F3D2A` | Chữ trên `primary-container` | — |
| `secondary` | `#A3471F` | Nút "Thêm việc" | chữ trắng 6.04 : 1 |
| `error` | `#B3261E` | Viền và icon lỗi | 6.17 : 1 trên `bg`; chữ trắng 6.54 : 1 |
| `error-container` | `#FCE4E1` | Nền khối lỗi | chữ `#8C1D18` 7.52 : 1 |
| `warning-container` | `#FFF1D6` | Nhắc nhở nhẹ | chữ `#7A4E00` 6.45 : 1 |
| `success` | `#2E6B2F` | Chữ "Đã xong" | 6.08 : 1 trên `bg` |
| `outline` | `#7A857F` | Viền ô nhập, nút viền | 3.61 : 1 (UI control, yêu cầu ≥ 3 : 1) |

Màu nhận diện 9 thói quen dùng cặp nền nhạt + icon đậm. Màu chỉ là tín hiệu phụ: mỗi thói quen luôn có icon và tên riêng.

| Thói quen | Nền | Icon/chữ |
| --- | --- | --- |
| 1 Vận động tự nhiên | `#D7EDE0` | `#0F3D2A` |
| 2 Sống có mục đích | `#E3E7F8` | `#26357A` |
| 3 Thư giãn mỗi ngày | `#EDE4F6` | `#4B2A73` |
| 4 Ăn vừa no 80% | `#FFF1D6` | `#7A4E00` |
| 5 Ăn nhiều rau, đậu | `#E2F0D2` | `#2F5214` |
| 6 Trà chiều cùng bạn | `#F6E6DA` | `#7A3412` |
| 7 Gắn kết cộng đồng | `#E0EEF2` | `#154A5A` |
| 8 Gia đình trên hết | `#FCE4E1` | `#8C1D18` |
| 9 Bạn bè tích cực | `#F3E7EF` | `#6B1F4E` |

### 3.2 Typography – Text styles (font **Be Vietnam Pro**)

| Style | Size / line-height | Weight | Dùng cho |
| --- | --- | --- | --- |
| `display` | 34 / 42 | Bold | Tên app ở S01 |
| `headline` | 28 / 36 | Bold | Tiêu đề màn hình |
| `title-lg` | 24 / 32 | Bold | Tên việc, tiêu đề dialog |
| `title-md` | 20 / 28 | Bold | Tiêu đề mục, chữ nút chính |
| `body-lg` | 18 / 28 | Regular / SemiBold | Nội dung chính, nhãn ô nhập |
| `body-md` | 16 / 24 | Regular | Chữ phụ, gợi ý (nhỏ nhất trong nội dung) |
| `label-nav` | 15 / 20 | SemiBold / Bold | Chỉ dùng cho nhãn bottom nav |

### 3.3 Spacing – collection `space`

`4 · 8 · 12 · 16 · 20 · 24 · 32 · 48` (dp). Lề màn hình = `20`; khoảng cách giữa các khối = `16`; khoảng cách giữa 2 nút ≥ `8`.

### 3.4 Radius – collection `radius`

| Token | Giá trị | Dùng cho |
| --- | --- | --- |
| `sm` | 8 | Chip nhỏ |
| `md` | 12 | Ô nhập, list row |
| `button` | 14 | Nút 56–60 dp |
| `lg` | 16 | Card |
| `xl` | 24 | Dialog |
| `full` | 999 | Pill, avatar, nút tròn |

### 3.5 Elevation – Effect styles

| Token | Giá trị | Dùng cho |
| --- | --- | --- |
| `elevation/0` | không bóng, viền 1 px `#E3DED3` | List row, bottom nav |
| `elevation/1` | Drop shadow Y 2, Blur 6, `#1F2A24` 10 % | Card |
| `elevation/2` | Drop shadow Y 8, Blur 24, `#000000` 24 % | Dialog |

## 4. Layout

- Frame: 360 × 800 dp; layout grid 4 cột, margin 20, gutter 16.
- Cấu trúc mỗi màn: App bar (64) → Main (Fill, cuộn dọc) → Bottom nav (84, cố định) hoặc Footer chứa nút chính.
- Mọi khối dùng Auto Layout; chiều ngang các khối nội dung là **Fill container**, nhờ đó khung 412 dp tự giãn.

## 5. Components (9 nhóm bắt buộc)

| Nhóm | Component set | Variants / properties |
| --- | --- | --- |
| Button | `Button` | Type = Primary · Secondary · Tonal · Text; State = Default · Pressed · Disabled; `Label` (text), `Show icon` (boolean), `Icon` (swap) |
| Text field | `TextField` | State = Default · Focused · Error · Filled; `Label`, `Helper`, `Error text` |
| Card | `TaskCard`, `TaskRow` | TaskCard: State = Next; TaskRow: State = Upcoming · Done · Skipped |
| Navigation | `NavItem`, `BottomNav` | NavItem: State = Active · Inactive; BottomNav: Active = Today · Week · Habits · Family |
| App bar | `AppBar` | Type = Back+Step · Greeting · Title |
| Dialog | `Dialog` | Type = Confirm · Destructive |
| Loading | `Loading` | Size = Full-screen · Inline |
| Empty | `EmptyState` | `Title`, `Message`, `Action` |
| Error | `ErrorView` | Type = Inline field · Banner · Full-screen |
| (phụ) | `TimeStepper`, `HabitTile`, `Switch` | HabitTile: Selected = true/false |
