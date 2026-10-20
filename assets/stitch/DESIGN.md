---
version: alpha
name: An Nhiên
description: >-
  Lịch sinh hoạt hằng ngày theo 9 thói quen Power 9 (Blue Zones) cho người Việt
  từ 65 tuổi. Android, khung 360 x 800 dp. Chữ lớn, nút lớn, mỗi màn một việc,
  mọi icon có chữ, không cử chỉ ẩn. Căn cứ: UX-Research.docx và
  Tong_hop_UIUX_An_Nhien.docx (13 nghiên cứu), token đọc từ bản Figma ngày 15/10/2026; màu nhấn 9 thói quen thêm 17/10/2026 theo góp ý "màu sắc bắt mắt".
colors:
  background: "#F6F7F2"
  surface: "#FFFFFF"
  on-surface: "#202B25"
  on-surface-variant: "#526057"
  primary: "#1F684B"
  primary-pressed: "#18533C"
  on-primary: "#FFFFFF"
  primary-container: "#D6EADF"
  primary-container-soft: "#E7F2EB"
  on-primary-container: "#174C37"
  success: "#1F684B"
  error: "#B42318"
  on-error: "#FFFFFF"
  error-container: "#FDECE9"
  on-error-container: "#912018"
  warning-container: "#FFF3DB"
  on-warning-container: "#8A5100"
  outline: "#7B887F"
  border-subtle: "#DFE5DF"
  border-strong: "#A0ACA3"
  disabled-bg: "#E6EAE5"
  disabled-fg: "#5C6A61"
  scrim: "#0F1411"
  habit-move-bg: "#D7EDE0"
  habit-move-fg: "#0F3D2A"
  habit-purpose-bg: "#E3E7F8"
  habit-purpose-fg: "#26357A"
  habit-downshift-bg: "#EDE4F6"
  habit-downshift-fg: "#4B2A73"
  habit-eighty-bg: "#FFF1D6"
  habit-eighty-fg: "#7A4E00"
  habit-plant-bg: "#E2F0D2"
  habit-plant-fg: "#2F5214"
  habit-tea-bg: "#F6E6DA"
  habit-tea-fg: "#7A3412"
  habit-belong-bg: "#E0EEF2"
  habit-belong-fg: "#154A5A"
  habit-family-bg: "#FCE4E1"
  habit-family-fg: "#8C1D18"
  habit-tribe-bg: "#F3E7EF"
  habit-tribe-fg: "#6B1F4E"
  habit-move-accent: "#2BA15C"
  habit-purpose-accent: "#768ADB"
  habit-downshift-accent: "#AC76DB"
  habit-eighty-accent: "#B98331"
  habit-plant-accent: "#609D2A"
  habit-tea-accent: "#D0754E"
  habit-belong-accent: "#309BB5"
  habit-family-accent: "#D86E75"
  habit-tribe-accent: "#D666AD"
  warning-strong: "#B26A00"
typography:
  display:
    fontFamily: Be Vietnam Pro
    fontSize: 34px
    fontWeight: 700
    lineHeight: 1.25
  headline:
    fontFamily: Be Vietnam Pro
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.35
  title-md:
    fontFamily: Be Vietnam Pro
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.4
  title-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.4
  body-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.5
  body-lg-strong:
    fontFamily: Be Vietnam Pro
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.5
  label-btn:
    fontFamily: Be Vietnam Pro
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.4
  body-md:
    fontFamily: Be Vietnam Pro
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.5
  caption:
    fontFamily: Be Vietnam Pro
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.5
  label-nav:
    fontFamily: Be Vietnam Pro
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
  numeric-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.25
rounded:
  sm: 8px
  md: 12px
  button: 14px
  lg: 16px
  xl: 24px
  full: 999px
spacing:
  xs: 4px
  sm: 8px
  md: 12px
  base: 16px
  screen: 20px
  lg: 24px
  xl: 32px
  xxl: 48px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-btn}"
    rounded: "{rounded.button}"
    height: 60px
    width: 320px
    padding: 16px
  button-primary-pressed:
    backgroundColor: "{colors.primary-pressed}"
    textColor: "{colors.on-primary}"
  button-primary-disabled:
    backgroundColor: "{colors.disabled-bg}"
    textColor: "{colors.disabled-fg}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.label-btn}"
    rounded: "{rounded.button}"
    height: 60px
    padding: 16px
  button-tonal:
    backgroundColor: "{colors.primary-container}"
    textColor: "{colors.on-primary-container}"
    typography: "{typography.label-btn}"
    rounded: "{rounded.button}"
    height: 60px
  button-danger:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-error}"
    typography: "{typography.label-btn}"
    rounded: "{rounded.button}"
    height: 60px
  button-back:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    typography: "{typography.label-btn}"
    height: 48px
  card-next-task:
    backgroundColor: "{colors.primary-container}"
    textColor: "{colors.on-primary-container}"
    rounded: "{rounded.lg}"
    padding: 20px
  card-task:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.title-lg}"
    rounded: "{rounded.lg}"
    padding: 16px
  card-reminder:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.xl}"
    padding: 24px
  status-done:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    height: 40px
  status-todo:
    backgroundColor: "{colors.warning-container}"
    textColor: "{colors.on-warning-container}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    height: 40px
  text-field:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.md}"
    height: 60px
    padding: 16px
  text-field-error:
    backgroundColor: "{colors.error-container}"
    textColor: "{colors.on-error-container}"
  bottom-nav:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface-variant}"
    typography: "{typography.label-nav}"
    height: 80px
  bottom-nav-active:
    backgroundColor: "{colors.primary-container}"
    textColor: "{colors.primary}"
  habit-tile:
    backgroundColor: "{colors.habit-move-bg}"
    textColor: "{colors.habit-move-fg}"
    typography: "{typography.title-lg}"
    rounded: "{rounded.lg}"
    height: 96px
  habit-tile-purpose:
    backgroundColor: "{colors.habit-purpose-bg}"
    textColor: "{colors.habit-purpose-fg}"
  habit-tile-downshift:
    backgroundColor: "{colors.habit-downshift-bg}"
    textColor: "{colors.habit-downshift-fg}"
  habit-tile-eighty:
    backgroundColor: "{colors.habit-eighty-bg}"
    textColor: "{colors.habit-eighty-fg}"
  habit-tile-plant:
    backgroundColor: "{colors.habit-plant-bg}"
    textColor: "{colors.habit-plant-fg}"
  habit-tile-tea:
    backgroundColor: "{colors.habit-tea-bg}"
    textColor: "{colors.habit-tea-fg}"
  habit-tile-belong:
    backgroundColor: "{colors.habit-belong-bg}"
    textColor: "{colors.habit-belong-fg}"
  habit-tile-family:
    backgroundColor: "{colors.habit-family-bg}"
    textColor: "{colors.habit-family-fg}"
  habit-tile-tribe:
    backgroundColor: "{colors.habit-tribe-bg}"
    textColor: "{colors.habit-tribe-fg}"
  status-done-label:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.success}"
    typography: "{typography.body-md}"
  divider:
    backgroundColor: "{colors.border-subtle}"
    height: 1px
  option-card-unselected:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.lg}"
    padding: 16px
  option-card-outline:
    backgroundColor: "{colors.border-strong}"
    height: 2px
  dialog-scrim:
    backgroundColor: "{colors.scrim}"
  habit-icon-move:
    backgroundColor: "{colors.habit-move-accent}"
    rounded: "{rounded.md}"
    size: 48px
  habit-icon-purpose:
    backgroundColor: "{colors.habit-purpose-accent}"
    rounded: "{rounded.md}"
    size: 48px
  habit-icon-downshift:
    backgroundColor: "{colors.habit-downshift-accent}"
    rounded: "{rounded.md}"
    size: 48px
  habit-icon-eighty:
    backgroundColor: "{colors.habit-eighty-accent}"
    rounded: "{rounded.md}"
    size: 48px
  habit-icon-plant:
    backgroundColor: "{colors.habit-plant-accent}"
    rounded: "{rounded.md}"
    size: 48px
  habit-icon-tea:
    backgroundColor: "{colors.habit-tea-accent}"
    rounded: "{rounded.md}"
    size: 48px
  habit-icon-belong:
    backgroundColor: "{colors.habit-belong-accent}"
    rounded: "{rounded.md}"
    size: 48px
  habit-icon-family:
    backgroundColor: "{colors.habit-family-accent}"
    rounded: "{rounded.md}"
    size: 48px
  habit-icon-tribe:
    backgroundColor: "{colors.habit-tribe-accent}"
    rounded: "{rounded.md}"
    size: 48px
  card-accent-bar:
    backgroundColor: "{colors.habit-move-accent}"
    width: 6px
    rounded: "{rounded.full}"
  status-todo-icon:
    backgroundColor: "{colors.warning-strong}"
    size: 24px
  dialog:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.xl}"
    padding: 24px
  snackbar:
    backgroundColor: "{colors.on-surface}"
    textColor: "{colors.surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 16px
---

# DESIGN.md – An Nhiên (bản cho Google Stitch)

File này theo chuẩn **DESIGN.md** của Google Stitch: phần YAML ở đầu là token máy đọc được, phần chữ bên dưới giải thích *vì sao* (agent đọc cả hai). Mọi quyết định đều dẫn về nghiên cứu trong hai file research ở thư mục `research/`:

- `UX-Research.docx` – ghi chú theo mã bài (PP02, PP04 …)
- `Tong_hop_UIUX_An_Nhien.docx` – tóm tắt 13 nghiên cứu (đánh số 01–13) và checklist

Bảng nguồn (mã trong UX-Research ↔ số trong Tổng hợp):

| Mã | Nghiên cứu | Mẫu | Ý chính dùng cho An Nhiên |
| --- | --- | --- | --- |
| [01] | Optimizing Mobile App Design for Older Adults (2025) | 132 tài liệu | Chữ lớn, tương phản cao, nút lớn, hỗ trợ giọng nói; màn chính ít chức năng |
| PP02 · [02] | Design Guidelines of Mobile Apps for Older Adults (2023) | 40 bài | Đơn giản hóa; nút to và cách xa; icon có chữ; hướng dẫn từng bước; có Quay lại/Hủy |
| PP03 · [03] | Multiprofessional Mobile App to Enhance Health Habits (2024) | Người ≥ 60 | Thử – sửa theo phản hồi: SUS 71,23 → 87,14 |
| PP04 · [04] | How to Design Font Size for Older Adults (2022) | 12 bài | 18–22 pt thuận lợi, tùy thiết bị/tác vụ; cho chỉnh cỡ |
| PP07 · [05] | Button Position and Touchscreen Font Size (2020) | 64 người | 22 pt tốt nhất trong 4 mức thử; vị trí nút ảnh hưởng kết quả |
| PP08-Keypad · [06] | Smartphone Numeric Keypad Designs on Elderly Users | 51 người ≥ 65 | Nút ≈ 15 mm, cách ≈ 3 mm cho tác vụ nhập số |
| PP08-Icon · [07] | Developing Icons for Older Adults | 51 người | Nhãn chữ giúp hiểu icon tốt hơn |
| PP09 · [08] | Pictogram and Text Size for Icons | Eye-tracking | Icon quen thuộc + chữ lớn → tìm nhanh hơn |
| PP010 · [09] | Mobile Navigation Design on Older Adults (2026) | 285 khảo sát, 25 thử | Điều hướng phức tạp tăng gánh nặng nhận thức; chậm ≠ trải nghiệm kém |
| PP012 · [10] | Human Factors in Visual Information Design | Tổng quan | Font không chân rõ nét; giãn dòng 1,5–2; tương phản 7 : 1 để tham khảo |
| PP013 · [11] | Elderly-Centric Chromatics | Người ≥ 60 | Ưa màu sáng, tông ấm, bão hòa vừa (≈ 31,75–41,25 %); xanh lá cũng được ưa |
| PP06 · [12] | Digital Assistive Technology Acceptance by Caregivers (2026) | Phỏng vấn | Người thân giúp chọn, cài đặt, xử lý khó khăn |
| PP011 · [13] | Mobile Support for Older Adults and Their Caregivers (2019) | 8 cặp | Tài khoản liên kết; tách giao diện nhận nhắc và giao diện quản lý |

> Lưu ý nguồn: nội dung dựa trên UX-Research do nhóm tổng hợp, chưa đối chiếu toàn văn từng bài gốc.

## Overview

**An Nhiên** giúp Bà Lan (68 tuổi, giáo viên về hưu, viễn thị, ngón tay kém linh hoạt, chỉ quen Zalo và YouTube, hay quên giờ ăn và giờ đi bộ) làm 9 thói quen sống lâu của Blue Zones mỗi ngày.

Cảm giác: **ấm, tươi, rõ ràng** – như một tờ lịch giấy treo tường có dán nhãn màu, không phải app công nghệ. Nền sáng, chữ đậm, **ít chữ, nhiều icon có nhãn**, mỗi thói quen một màu nhấn tươi để nhìn là nhận ra.

Ba ưu tiên rút ra từ research (Tổng hợp, mục 04):

1. Người lớn tuổi **tự đọc và tự xác nhận** được lời nhắc.
2. Người thân **thiết lập thay** được (PP06, PP011) – người lớn tuổi không phải tự cấu hình.
3. **Kiểm thử với người thật** trước khi chốt (PP03).

Hai loại người dùng, hai mức giao diện (PP011):

| Người dùng | Việc chính | Yêu cầu giao diện |
| --- | --- | --- |
| Người lớn tuổi | Xem việc hôm nay, nhận lời nhắc, bấm "Đã xong", gọi người thân | Chữ rất lớn, ít nút, một việc mỗi màn |
| Người thân | Cài đặt, tạo lịch, gửi lời nhắn/gợi ý, xem phản hồi | Màn quản lý gọn, vẫn dùng cùng token |

Màn hình (Android 360 × 800): S01 Chào mừng + chọn cỡ chữ · S02 Hồ sơ · S03 Hôm nay · S04 Chi tiết việc · S05–S06 Thêm việc (chọn thói quen → giờ, lặp, nhắc) · S07 Lịch tuần · S08 9 thói quen · S09 Gia đình · S10 Cài đặt hiển thị.

## Colors

Bảng màu: **nền kem-xanh nhạt, xanh lá đậm làm màu chính**, 9 cặp màu nhạt-đậm cho 9 thói quen.

- **Nền sáng, không tối, không chói** (PP013: người cao tuổi ưa màu độ sáng cao; [10]: nền sáng, chữ đậm). `background #F6F7F2` hơi ấm, không trắng tinh để đỡ chói.
- **Xanh lá là màu chính** (PP013: xanh lá nằm trong nhóm màu được ưa thích). `primary #1F684B` được đậm hóa để giữ tương phản: chữ trắng trên nó 6,69 : 1.
- **Tông ấm, bão hòa vừa phải** cho các màu phụ (PP013: ≈ 31,75–41,25 %): màu nền 9 thói quen là các tông nhạt, dịu (vàng kem, đào, hồng nhạt…), không dùng màu neon.
- **Tương phản:** chữ chính hướng tới **≥ 7 : 1** theo khuyến nghị tham khảo của PP012 – `on-surface #202B25` đạt 13,6 : 1 trên nền. Chữ phụ tối thiểu 4,5 : 1 (`on-surface-variant` 6,15 : 1). Viền control ≥ 3 : 1 (`outline` 3,44 : 1).
- **Màu không bao giờ là tín hiệu duy nhất:** trạng thái luôn có icon + chữ ("✓ Đã xong", "○ Chưa làm").

| Vai trò | Token | Hex | Tương phản |
| --- | --- | --- | --- |
| Nền app | `background` | #F6F7F2 | — |
| Thẻ, nav, dialog | `surface` | #FFFFFF | — |
| Chữ chính | `on-surface` | #202B25 | 13,60 : 1 |
| Chữ phụ | `on-surface-variant` | #526057 | 6,15 : 1 |
| Nút chính, tab đang chọn | `primary` | #1F684B | 6,21 : 1; chữ trắng 6,69 : 1 |
| Ô đang chọn, "Đã xong" | `primary-container` | #D6EADF | chữ #174C37 7,85 : 1 |
| Lỗi, nút nguy hiểm | `error` | #B42318 | 6,11 : 1; chữ trắng 6,57 : 1 |
| Nền khối lỗi | `error-container` | #FDECE9 | chữ #912018 7,57 : 1 |
| "Chưa làm", nhắc nhẹ | `warning-container` | #FFF3DB | chữ #8A5100 5,86 : 1 |
| Viền ô nhập | `outline` | #7B887F | 3,44 : 1 |

### Màu nhấn 9 thói quen – "bắt mắt" ở mảng nhỏ

Góp ý của thầy: **màu sắc bắt mắt**. Cách làm để không mất độ dễ đọc `[nhóm quyết định]`:

- Màu tươi chỉ đặt ở **mảng nhỏ**: ô icon 48 × 48 (icon trắng), vạch màu 6 px bên trái thẻ việc, chấm màu trong lịch tuần. Nền app và chữ giữ nguyên tương phản cao.
- Mỗi màu nhấn đạt **≥ 3 : 1** với nền trắng và nền app (WCAG 1.4.11 cho thành phần không phải chữ), icon trắng trên màu nhấn cũng ≥ 3 : 1. **Không đặt chữ dài lên màu nhấn**; chữ vẫn nằm trên nền trắng.
- Tông ấm, độ sáng cao theo PP013; độ bão hòa (HSL 58 %) cao hơn khoảng 31–41 % mà PP013 ghi nhận, chấp nhận vì chỉ dùng ở mảng nhỏ. Cần hỏi ý người thật khi test.

| Thói quen | Màu nhấn `habit-*-accent` | Trắng trên màu | Màu trên nền app |
| --- | --- | --- | --- |
| Vận động tự nhiên | #2BA15C | 3,30 : 1 | 3,06 : 1 |
| Sống có mục đích | #768ADB | 3,27 : 1 | 3,03 : 1 |
| Thư giãn mỗi ngày | #AC76DB | 3,30 : 1 | 3,07 : 1 |
| Ăn vừa đủ | #B98331 | 3,30 : 1 | 3,07 : 1 |
| Ăn nhiều rau, đậu | #609D2A | 3,30 : 1 | 3,07 : 1 |
| Trà chiều cùng bạn | #D0754E | 3,32 : 1 | 3,09 : 1 |
| Gắn kết cộng đồng | #309BB5 | 3,25 : 1 | 3,02 : 1 |
| Gia đình trên hết | #D86E75 | 3,27 : 1 | 3,04 : 1 |
| Bạn bè tích cực | #D666AD | 3,30 : 1 | 3,06 : 1 |

Trạng thái dùng màu đậm để nhìn là biết: **✓ Đã xong** = chip nền `primary` #1F684B, chữ trắng (6,69 : 1); **○ Chưa làm** = icon vòng tròn `warning-strong` #B26A00 + chữ #8A5100 trên nền `warning-container`.

9 cặp màu nhạt cho nền thẻ thói quen lớn (nền / icon-chữ, tất cả ≥ 6,4 : 1): Vận động tự nhiên `move` · Sống có mục đích `purpose` · Thư giãn mỗi ngày `downshift` · Ăn vừa đủ `eighty` · Ăn nhiều rau, đậu `plant` · Trà chiều cùng bạn `tea` · Gắn kết cộng đồng `belong` · Gia đình trên hết `family` · Bạn bè tích cực `tribe`.

## Typography

- **Font không chân, nét rõ** (PP012 gợi ý Arial, Verdana, Frutiger). Chọn **Be Vietnam Pro**: cùng nhóm sans-serif nét rõ, và được thiết kế cho dấu tiếng Việt (dấu không dính vào chữ ở cỡ lớn) – điều Arial/Verdana làm kém hơn.
- **Cỡ chữ:** research ghi nhận 18–22 pt thuận lợi (PP04) và 22 pt tốt nhất trong thử nghiệm (PP07). An Nhiên lấy **22 làm mức sàn cho chữ trên nút** và **24 cho nội dung chính** (cao hơn một bậc vì Bà Lan viễn thị); **không chữ nào dưới 20**, kể cả nhãn bottom nav và chú thích.
- PP04 nói kích thước phù hợp **thay đổi theo người và thiết bị** → cho chọn 3 mức ở S01 và S10 (mặc định "Lớn"). Không coi một con số là chuẩn cố định.
- **Giãn dòng 1,5** cho chữ nội dung (PP012: 1,5–2 lần cỡ chữ). Tiêu đề 1,25–1,4 để không bị rời.
- Chữ đậm (600–700) cho tiêu đề, nút và tên việc; tránh chữ mảnh (300) và chữ nghiêng.
- **Ít chữ** (góp ý của thầy): câu ≤ 15 tiếng, nhãn nút ≤ 5 tiếng, mỗi thẻ tối đa 1 dòng phụ; giải thích dài chuyển vào màn chi tiết và nút "Đọc to". Icon thay cho câu mô tả, nhưng không thay cho nhãn.

| Style | Cỡ / giãn dòng | Đậm | Dùng cho |
| --- | --- | --- | --- |
| `display` | 34 / 1,25 | 700 | Tên app (S01), giờ lớn |
| `headline` | 30 / 1,35 | 700 | Tiêu đề màn |
| `title-md` | 26 / 1,4 | 700 | Tiêu đề mục, tiêu đề dialog |
| `title-lg` | 24 / 1,4 | 700 | Tên việc trong thẻ |
| `body-lg` | 24 / 1,5 | 400 | Nội dung chính |
| `label-btn` | 22 / 1,4 | 700 | Chữ trên nút |
| `body-md`, `caption` | 20 / 1,5 | 400 | Chữ phụ, gợi ý – mức nhỏ nhất |
| `label-nav` | 20 / 1,4 | 600 | Nhãn bottom nav |

Ba mức cỡ chữ người dùng chọn:

| Mức | Nội dung | Tiêu đề | Nút |
| --- | --- | --- | --- |
| Vừa | 20 | 28 | 20 |
| Lớn (mặc định) | 24 | 30 | 22 |
| Rất lớn | 28 | 32 | 24 |

## Layout

- Khung **360 × 800 dp**, lề màn `screen` = 20, khoảng cách giữa các khối `base` = 16.
- Cấu trúc mỗi màn: App bar (có nút "Quay lại" bằng chữ) → nội dung cuộn **dọc** → Bottom nav cố định (màn tab) hoặc Footer chứa nút chính.
- **Một màn – một việc** (PP02, [01]): tối đa 1 nút filled; màn Hôm nay chỉ nổi bật khối "Việc tiếp theo".
- **Ít nhánh lựa chọn** (PP02, PP010): bottom nav đúng 4 tab có chữ – Hôm nay · Lịch tuần · Thói quen · Gia đình. Không menu ẩn, không menu ba chấm.
- **Căn giữa** nội dung trọng tâm (tiêu đề màn trống, lời nhắc, dialog xác nhận); danh sách việc căn trái để mắt đọc theo một đường thẳng.
- **Nút chính đặt ở cùng một chỗ trên mọi màn** – đáy màn, rộng hết chiều ngang trừ lề (PP07: vị trí nút ảnh hưởng hiệu quả thao tác).
- **Nhìn vào là biết đã làm hay chưa:** mỗi việc có nhãn trạng thái chữ + icon ("✓ Đã xong" nền xanh nhạt, "○ Chưa làm" nền vàng nhạt) nằm ngay cạnh tên việc.
- **Khoảng cách giữa các nút:** tối thiểu 8; với cặp nút trong lời nhắc ("Đã xong" / "Nhắc lại sau") dùng **20 (≈ 3 mm)** theo PP08-Keypad để tránh bấm nhầm. Không áp kích thước bàn phím 15 mm cho mọi nút – chỉ cho bàn phím số / mã ghép nối.
- **Flow dựa trên chạm (click), không dựa trên vuốt** (PP02): mọi hành động làm được bằng một lần chạm; không có thao tác chỉ làm được bằng vuốt hay nhấn giữ.
- **Không ép nhanh** (PP010): không đếm ngược, không tự đóng màn khi người dùng đang đọc; snackbar "Hoàn tác" giữ ít nhất 10 giây.

## Elevation & Depth

Phẳng, ít bóng – độ sâu nhẹ chỉ để phân biệt lớp, không trang trí.

- Nền, list row, bottom nav: **không bóng**, tách bằng viền `border-subtle`.
- Thẻ việc (`card-task`), khối "Việc tiếp theo": bóng nhẹ cấp 1.
- Dialog xác nhận, lời nhắc bật lên: bóng cấp 2 + nền mờ `scrim` để mắt tập trung vào một việc.
- Không gradient, không kính mờ (glassmorphism), không chữ đặt trên ảnh rối ([10]).

## Shapes

- Bo góc mềm, thân thiện: nút `button` 14, thẻ `lg` 16, ô nhập `md` 12, dialog `xl` 24, chip trạng thái và avatar `full`.
- Nút hình chữ nhật bo góc, **cao, không dẹt** (PP08-Keypad: nút vuông/tròn thuận lợi hơn chữ nhật dọc hẹp).
- Icon nét đều, đơn giản, kiểu quen thuộc (chuông, điện thoại, lịch, lá) – không icon trừu tượng (PP09).
- Chỉ dùng bộ icon **Lucide** (nét outline 2–2,5), không tự vẽ icon. Mọi icon hiển thị **≥ 32 × 32 px** và hình vẽ lấp đầy khung (R-ICON-03); riêng icon trong chip trạng thái được ≥ 24 px vì luôn có chữ đi kèm. Icon nào dùng cho nghĩa nào xem **Từ điển icon** bên dưới.

## Components

| Component | Quy tắc |
| --- | --- |
| `button-primary` | Cao 60, rộng gần hết màn (lề 20), chữ 22 đậm. Mỗi màn tối đa 1 nút này. Có trạng thái nhấn (`-pressed`) để có phản hồi khi bấm (PP02–PP03); trạng thái tắt (`-disabled`) vẫn đọc được 4,68 : 1. |
| `button-secondary` / `button-tonal` | Cao 60, viền `outline` hoặc nền `primary-container`. Dùng cho hành động phụ. |
| `button-danger` | Xóa, ngưng lịch lặp. Luôn đi sau một dialog hỏi lại. |
| `button-back` | Chữ "‹ Quay lại" hoặc tên màn trước, vùng chạm ≥ 48. Không bao giờ chỉ có mũi tên (PP02). |
| `card-next-task` | Khối nổi bật trên Hôm nay: giờ, tên việc, icon thói quen, nút "Đã xong". |
| `card-task` | Một dòng việc: vạch màu thói quen (`card-accent-bar`) · ô icon màu (`habit-icon-*`) · giờ · tên việc · nhãn trạng thái. Tối đa 1 dòng phụ. Cả thẻ bấm được (≥ 48 cao, thực tế ≥ 72). |
| `card-reminder` | Lời nhắc: câu ngắn ("Đến giờ đi bộ rồi Bác ơi"), 2 nút **"Đã xong"** và **"Nhắc lại sau"** cách nhau 20 (checklist Tổng hợp). Có nút "🔊 Đọc to". |
| `status-done` / `status-todo` | "✓ Đã xong" chip xanh đậm chữ trắng; "○ Chưa làm" vòng tròn vàng đậm + chữ. Luôn có icon + chữ; màu chỉ là tín hiệu phụ. |
| `habit-icon-*` | Ô 48 × 48 bo 12, nền màu nhấn của thói quen, icon Lucide trắng **32 px, hình vẽ lấp đầy khung**, nét 2,5 (R-ICON-03); đúng tên icon ở `vocabulary.md` mục 1; luôn có tên thói quen hoặc tên việc bên cạnh. |
| `text-field` | Cao 60, nhãn ở trên (không dùng placeholder thay nhãn). Hạn chế gõ phím ảo (PP02): ưu tiên chọn từ danh sách, chọn giờ bằng ô bấm. |
| `text-field-error` | Icon + câu giải thích + ví dụ đúng; không chỉ đổi màu viền. |
| `bottom-nav` | 4 tab, mỗi tab icon + chữ 20; tab đang chọn có nền `primary-container` và chữ đậm. |
| `habit-tile`, `habit-tile-<thói quen>` | Icon + tên thói quen + màu nhận diện của thói quen đó (9 biến thể). |
| `dialog` | Hỏi lại trước khi đánh dấu xong, xóa, ngưng lặp. Hai nút rõ chữ: "Hủy" và hành động cụ thể ("Xóa việc này"). |
| `snackbar` | Sau mỗi thao tác: "Đã lưu" + nút "Hoàn tác" – để biết đã làm thành công và sửa được khi sai (PP02–PP03). |

Icon luôn có chữ đi kèm (PP08-Icon, PP09): 🔔 **Lời nhắc** · 📞 **Gọi người thân** · 📅 **Lịch tuần** · 🌿 **Thói quen**.

### Từ điển icon

Mỗi nghĩa một icon Lucide, mỗi icon chỉ một nghĩa trong toàn app (R-ICON-03). Prompt Stitch lấy nguyên bảng này; màn mới cần nghĩa chưa có thì thêm dòng vào đây trước khi chạy. Icon luôn ≥ 32 px (trừ icon trong chip trạng thái: ≥ 24 px) và luôn có chữ đi kèm (R-ICON-01).

| Nhóm | Nghĩa | Lucide | Ghi chú |
| --- | --- | --- | --- |
| Trạng thái | Đã xong | `circle-check` | **Chỉ** cho trạng thái/nút "Đã xong". Không dùng cho Lưu, Bật, Đang chọn |
| Trạng thái | Chưa (chưa làm / chưa chọn) | `circle` | Chip "Chưa làm" màu `warning-strong`; ô lựa chọn chưa chọn màu `outline` |
| Trạng thái | Đang chọn | `circle-dot` | Ô lựa chọn đang chọn (kèm viền 2 px `primary` + chữ "Đang chọn") |
| Trạng thái | Đã bỏ qua | `circle-minus` | |
| Trạng thái | Đã dời | `redo-2` | Chip "Đã dời" (↻ trong R-STA-01). Thêm 18/10/2026 vì `alarm-clock-plus` đã là hành động "Dời lại" |
| Điều hướng | Tab Hôm nay | `sun` | Không dùng `house` (đã là thói quen Gia đình trên hết) |
| Điều hướng | Tab Lịch tuần | `calendar-days` | **Chỉ** cho tab, tiêu đề Lịch tuần và nút đi tới Lịch tuần (nút "Xem lịch" ở N18, thêm 19/10/2026). "Bước 1/2" không dùng icon này |
| Điều hướng | Tab Thói quen | `leaf` | Logo app cũng là chiếc lá trong ô vuông: logo là nhận diện, không tính là icon |
| Điều hướng | Tab Gia đình | `hand-heart` | Không dùng `users` (đã là thói quen Gắn kết cộng đồng) |
| Điều hướng | Quay lại | `chevron-left` | Luôn kèm chữ "Quay lại" |
| Điều hướng | Mở chi tiết | `chevron-right` | Cuối thẻ bấm được |
| Điều hướng | Mở danh sách / ô chọn giờ | `chevron-down` | |
| Điều hướng | Tiếp tục, Bắt đầu | `arrow-right` | |
| Điều hướng | Bước 1/2, Bước 2/2 | không icon | Chỉ chữ, hoặc chấm tiến độ 12 px |
| Hành động | Lưu | `save` | |
| Hành động | Thêm việc, Xem thêm | `plus` | |
| Hành động | Thêm người thân | `user-plus` | |
| Hành động | Chọn từ danh bạ | `contact` | Thêm 17/10/2026 cho S12 |
| Hành động | Sửa | `pencil` | |
| Thông tin | Lặp lại | `repeat` | Thêm 17/10/2026 cho S06, S15 |
| Hành động | Chỉ lần này (một ngày) | `calendar-1` | Thêm 19/10/2026 cho N13; **chỉ** cho lựa chọn "Chỉ lần này"; luôn kèm chữ |
| Hành động | Lần này và các lần sau (cả chuỗi) | `calendar-range` | Thêm 19/10/2026 cho N13; **chỉ** cho lựa chọn "Lần này và các lần sau"; luôn kèm chữ |
| Thông tin | Chọn ngày, ngày đã chọn | `calendar` | Thêm 19/10/2026 cho N11; không dùng `calendar-days` (chỉ cho tab Lịch tuần); luôn kèm chữ |
| Điều hướng | Tháng trước | `chevrons-left` | Thêm 19/10/2026 cho N11; **chỉ** cho nút "Tháng trước", khác `chevron-left` (Quay lại); luôn kèm chữ |
| Điều hướng | Tháng sau | `chevrons-right` | Thêm 19/10/2026 cho N11; **chỉ** cho nút "Tháng sau", khác `chevron-right` (mở chi tiết); luôn kèm chữ |
| Hành động | Chốt lựa chọn ("Xong") | `check` | Thêm 19/10/2026 cho N11; **chỉ** cho nút "Xong" chốt ngày/giờ đã chọn; không dùng `circle-check` (chỉ cho "Đã xong") |
| Hành động | Xóa | `trash-2` | |
| Hành động | Hoàn tác | `undo-2` | |
| Hành động | Bỏ thay đổi (rời form không lưu) | `file-x` | Thêm 19/10/2026 cho N14; **chỉ** cho nút "Bỏ thay đổi"; không dùng `trash-2` (chỉ cho Xóa) và `undo-2` (Hoàn tác); luôn kèm chữ |
| Hành động | Không đổi, đóng hộp thoại | `x` | Thêm 19/10/2026 cho DLG-Later ("Không dời nữa"); luôn kèm chữ, không dùng làm nút đóng chỉ-icon |
| Hành động | Nhắc lại sau, Dời giờ | `alarm-clock-plus` | |
| Lý do bỏ qua | Trời mưa | `cloud-rain` | Thêm 19/10/2026 cho DLG-Skip; luôn kèm chữ |
| Lý do bỏ qua | Thấy mệt | `bed` | Thêm 19/10/2026 cho DLG-Skip; không dùng `heart-pulse` (gợi điểm sức khỏe) |
| Lý do bỏ qua | Bận việc nhà | `washing-machine` | Thêm 19/10/2026 cho DLG-Skip; không dùng `house` (đã là thói quen Gia đình) |
| Lý do bỏ qua | Lý do khác | `circle-help` | Thêm 19/10/2026 cho DLG-Skip; không dùng `ellipsis` (giống menu ba chấm) |
| Hành động | Hôm nay bỏ qua | `skip-forward` | |
| Hành động | Đọc to | `volume-2` | |
| Hành động | Dừng đọc | `circle-stop` | |
| Hành động | Gọi điện | `phone` | **Chỉ** cho hành động gọi |
| Hành động | Nhắn tin | `message-square` | |
| Hành động | Xem thử, Xem gợi ý | `eye` | Mở rộng 19/10/2026 cho G12 (nút "Xem gợi ý"): cùng nghĩa "xem"; luôn kèm chữ |
| Thông tin | Giờ của việc | `clock` | |
| Thông tin | Giờ thức dậy | `sunrise` | |
| Thông tin | Lời nhắc, nhắc việc | `bell` | |
| Thông tin | Bật nhắc | `bell-ring` | |
| Thông tin | Tắt nhắc, chưa đặt được lời nhắc | `bell-off` | Mở rộng 19/10/2026 cho N16 (việc đã lưu nhưng chưa đặt được lời nhắc); màu `warning-strong`, luôn kèm chữ, không dùng màu `error` vì việc vẫn được lưu |
| Thông tin | Cỡ chữ | `type` | |
| Thông tin | Tên Bác, hồ sơ | `user` | |
| Thông tin | Cách xưng hô (Bác / Ông / Bà) | `smile` | Thêm 19/10/2026 cho S02, N06; luôn kèm chữ "An Nhiên gọi Bác là" |
| Thông tin | Điện thoại (thiết bị, quyền, dữ liệu trên máy) | `smartphone` | Không dùng `phone` |
| Thông tin | Lưu ý, gợi ý | `info` | |
| Thông tin | Gợi ý lịch từ người thân | `mail` | Thêm 19/10/2026 cho G12; **chỉ** cho thẻ "Mai gửi Bác …"; không dùng `message-square` (Nhắn tin) hay `info` (lưu ý) |
| Thông tin | Lỗi nhập, lỗi lưu | `circle-alert` | Màu `error` + câu giải thích. Mở rộng 18/10/2026 cho ST-Error (chưa lưu được) |
| Trạng thái | Đang lưu | `loader-circle` | **Chỉ** cho màn/nút "Đang lưu…". Thêm 18/10/2026 cho ST-Loading; luôn kèm chữ "Đang lưu việc…" |
| Trạng thái | Mất mạng | `wifi-off` | **Chỉ** cho thông báo "Đang không có mạng" (ST-Loading-offline). Thêm 19/10/2026; luôn kèm chữ, màu `on-surface-variant`, không dùng màu `error` vì app vẫn lưu được trên máy |
| Hành động | Dùng lịch mẫu | `layout-list` | Thêm 18/10/2026 cho ST-Empty |
| Hành động | Thử lại | `rotate-ccw` | Thêm 18/10/2026 cho ST-Error |
| Hành động | Kiểm tra lại lịch | `calendar-search` | Thêm 18/10/2026 cho ST-Error; không dùng `calendar-days` (chỉ cho tab Lịch tuần) |
| Thói quen | 9 thói quen Power 9 | theo `vocabulary.md` mục 1 | `footprints` · `compass` · `wind` · `utensils` · `salad` · `coffee` · `users` · `house` · `handshake`; mỗi icon chỉ dùng cho thói quen của nó |

**Giọng nói** ([01]): màn lời nhắc, chi tiết việc và 9 thói quen có nút "🔊 Đọc to" (có chữ, không chỉ icon).

**Lời nhắc do người dùng điều chỉnh** (PP02–PP03): người dùng chọn mức nhắc (1 lần / nhắc lại sau 10 phút / tắt), không nhắc liên tục mặc định.

**Hướng dẫn đúng lúc** (PP02): gợi ý ngắn 1 câu ngay tại chỗ cần dùng; không có trang hướng dẫn dài, không carousel onboarding phải vuốt.

## Do's and Don'ts

**Nên**

- Viết 100 % tiếng Việt có dấu, xưng "Bác", câu ngắn đời thường; dùng từ trong `vocabulary.md` ("lời nhắc", "việc", "Đã xong").
- Mọi chữ ≥ 20, nội dung 24, nút 22; giãn dòng nội dung 1,5.
- Mọi vùng chạm ≥ 48 × 48; nút chính cao 60, đặt cố định ở đáy.
- Dùng nhiều icon quen thuộc: mọi việc, thói quen, tab, nút chính đều có icon – và icon nào cũng có nhãn ngắn; nút Quay lại có chữ.
- Mỗi thẻ việc có ô icon và vạch màu của thói quen để nhìn màu là nhận ra.
- Mỗi màn một việc chính, một nút filled.
- Trạng thái "Đã xong / Chưa làm" nhìn là biết, có icon + chữ.
- Có phản hồi sau mỗi lần bấm và có "Hoàn tác".
- Cho người thân cài đặt và tạo lịch thay; lịch chỉ đổi khi Bác bấm nhận gợi ý.
- Cho chỉnh cỡ chữ (Vừa / Lớn / Rất lớn).
- Có nút "Đọc to" cho nội dung quan trọng.

**Không nên**

- Chữ dưới 20, chữ mảnh, chữ nghiêng, chữ xám nhạt, chữ đặt trên ảnh; đoạn văn giải thích trên màn Hôm nay.
- Chữ dài đặt trên nền màu nhấn; tự chế màu ngoài 9 màu nhấn.
- Nút chỉ có icon, icon trừu tượng không giải thích.
- Thao tác chỉ làm được bằng vuốt, nhấn giữ, kéo thả; carousel; menu ẩn.
- Nhiều nút filled cạnh nhau; hai nút sát nhau dưới 8.
- Dùng màu làm tín hiệu duy nhất.
- Từ kỹ thuật/tiếng Anh: task, notification, sync, streak, Settings, Done.
- Bảng xếp hạng, điểm sức khỏe, "mất chuỗi", đếm ngược, lời lẽ gây áp lực.
- Gradient, màu neon, nền tối, giao diện quá chói.
- Nhắc liên tục mặc định; tự gửi kết quả cho con cháu mà Bác không biết.
- Bắt Bác tự gõ nhiều bằng bàn phím ảo hoặc đọc trang hướng dẫn dài.
