# Flutter Handoff – An Nhiên

Tài liệu này đủ để một lập trình viên Flutter chưa biết dự án hiện thực từng màn hình và các trạng thái của nó. Lab 2 không yêu cầu code.

**Quy ước chung**

- Flutter 3.x, Material 3 (`useMaterial3: true`), font `GoogleFonts.beVietnamPro`.
- Điều hướng: `go_router` + `StatefulShellRoute` cho 4 tab.
- Mọi kích thước tính bằng dp (logical pixels). Token lấy từ `AppTheme`, `AppSpace` và `AppRadius` (bảng 1), không hard-code.
- Ràng buộc chung cho mọi màn: chữ ≥ 16 sp (nhãn nav 15 sp), nút ≥ 56 dp, khoảng cách giữa nút ≥ 8 dp, hỗ trợ `textScaler` tới 2.0 mà không tràn, contrast ≥ 4.5 : 1, không có cử chỉ vuốt bắt buộc.

## Route map

| Route | Màn | Ghi chú |
| --- | --- | --- |
| `/welcome` | S01 | Chỉ khi chưa onboarding |
| `/setup` | S02 | |
| `/today` | S03 | Tab 0 |
| `/today/task/:id` | S04 | |
| `/today/add/type` | S05 | |
| `/today/add/time?habit=` | S06 | |
| `/today/add/result` | ST-Saved / ST-Error | Thay thế (`go`), không push chồng |
| `/week` | S07 | Tab 1 |
| `/habits` | S08 | Tab 2 |
| `/family` | S09 | Tab 3 |
| `/settings` | S10 | Push từ S03 |

---

## S01 – Chào mừng

| Mục | Đặc tả |
| --- | --- |
| Layout | `Scaffold(bg)` → `SafeArea` → `Padding(24, 40, 24, 28)` → `Column`: logo tròn 132, `display` "An Nhiên", mô tả `body-lg` 20 căn giữa, nhóm 3 lựa chọn cỡ chữ, `Spacer`, nút chính, ghi chú `body-md` |
| Components | Radio card × 3 (`RadioListTile` tùy biến, cao 60), Button Primary 60 "Bắt đầu" |
| States | Mặc định chọn "Lớn"; chọn khác thì xem trước cỡ chữ ngay trên chính radio card |
| Interactions | Chạm card → chọn và cập nhật `textScale` toàn app ngay lập tức; "Bắt đầu" → S02 |
| Navigation | `context.go('/setup')`; không có Back (màn gốc) |
| UI constraints | 3 lựa chọn tương ứng `textScaler` 1.0 / 1.15 / 1.3; lưu vào `SharedPreferences` |

## S02 – Thiết lập hồ sơ

| Mục | Đặc tả |
| --- | --- |
| Layout | AppBar (Back+Step "Bước 1 / 2") → `ListView(padding 24)`: tiêu đề `headline`, mô tả, TextField Tên, TimeStepper giờ thức dậy, TextField SĐT người thân → Footer nút "Tiếp tục" |
| Components | AppBar, TextField × 2, TimeStepper, Button Primary |
| States | Default; Focused; Error khi Tên trống ("Bà chưa nhập tên gọi"); SĐT sai định dạng → Error |
| Interactions | −/+ đổi 15 phút (5:30 mặc định); "Tiếp tục" validate rồi lưu |
| Navigation | Back → S01; hợp lệ → `go('/today')`; nếu chưa có việc → S03 hiện ST-Empty |
| UI constraints | `keyboardType: TextInputType.phone` cho SĐT; nút không bị bàn phím che (`resizeToAvoidBottomInset`) |

## S03 – Hôm nay

| Mục | Đặc tả |
| --- | --- |
| Layout | `Scaffold(bg)`; body = `Column`: Header (ngày + nút Cài đặt, lời chào `headline`) → `Expanded(ListView(padding 20, gap 16))`: ProgressCard, tiêu đề "Việc tiếp theo", NextTaskCard, hàng tiêu đề "Còn lại hôm nay" + Button Tonal "Thêm việc", danh sách TaskRow; `bottomNavigationBar` cao 84 |
| Components | AppBar Greeting, ProgressCard (`LinearProgressIndicator` cao 12), TaskCard Next (Button Primary "Đã xong" + Secondary "Dời lại"), TaskRow (Upcoming/Done), Button Tonal, BottomNav |
| States | Loading: spinner + "Đang tải lịch…"; Empty: ST-Empty; Có dữ liệu; Lỗi tải: `ErrorView` banner + "Thử lại"; Tất cả đã xong: thẻ chúc mừng thay NextTaskCard |
| Interactions | "Đã xong" → `showDialog(DLG-Done)`; chạm tên việc → S04; "Dời lại" → S04; "Thêm việc" → S05; "Cài đặt" → S10; kéo xuống để làm mới (tùy chọn, không bắt buộc) |
| Navigation | Tab 0 của `NavigationBar`; Back hệ thống tại đây → thoát app |
| UI constraints | NextTaskCard luôn ở đầu, không cuộn mất khi chỉ có ≤ 6 việc; `Semantics` cho progress: "Đã xong 3 trên 6 việc" |

## S04 – Chi tiết hoạt động

| Mục | Đặc tả |
| --- | --- |
| Layout | AppBar Back "Hôm nay" → `ListView(padding 20)`: hàng icon thói quen 64 + nhãn, `headline` tên việc, Card "Vì sao tốt cho bà?", danh sách bước có số → Footer `surface`: Primary "Tôi đã làm xong", hàng Secondary "Dời 30 phút" + Text "Bỏ qua hôm nay" |
| Components | AppBar, HabitBadge, Card, numbered list, Button Primary/Secondary/Text |
| States | Upcoming (mặc định); Done (Footer thay bằng dòng "✓ Đã xong lúc 9:42" + nút "Hoàn tác"); Skipped |
| Interactions | "Tôi đã làm xong" → DLG-Done; "Dời 30 phút" → cập nhật giờ, quay về S03 kèm `SnackBar` không tự tắt; "Bỏ qua hôm nay" → `AlertDialog` xác nhận |
| Navigation | `push('/today/task/:id')`; Back → S03 |
| UI constraints | Footer cố định, nội dung cuộn phía trên; nút 60/56 dp |

## S05 – Thêm việc: chọn thói quen

| Mục | Đặc tả |
| --- | --- |
| Layout | AppBar "Hủy" + "Bước 1 / 2" → tiêu đề `headline` 26 → `GridView.count(crossAxisCount: 2, spacing 10, childAspectRatio ≈ 1.65)` 9 ô → Footer nút "Tiếp tục" |
| Components | HabitTile × 9 (Selected true/false), Button Primary |
| States | Chưa chọn: "Tiếp tục" disabled + dòng gợi ý "Chọn 1 thói quen"; Đã chọn: viền 3 dp `primary` + dấu ✓ |
| Interactions | Chạm ô → chọn (chỉ 1); "Tiếp tục" → S06 với `habit` |
| Navigation | `push('/today/add/type')`; "Hủy" → `pop` về S03 |
| UI constraints | Ô ≥ 92 dp cao; màu nền thói quen chỉ là tín hiệu phụ (có icon + tên) |

## S06 – Thêm việc: chọn giờ

| Mục | Đặc tả |
| --- | --- |
| Layout | AppBar Back + "Bước 2 / 2" → `ListView(padding 20, gap 18)`: chip thói quen, `headline` "Làm lúc nào?", TextField Tên việc, TimeStepper, SegmentedButton Lặp lại, SwitchListTile Nhắc nhở → Footer "Lưu việc này" |
| Components | Chip, TextField, TimeStepper, `SegmentedButton` (Mỗi ngày / Chọn ngày), `SwitchListTile`, Button Primary |
| States | Default; Validation (ST-Validation: tên trống → viền `error`, icon, chữ lỗi, 2 chip gợi ý); Chọn ngày → hiện 7 chip ngày T2–CN cao 48 |
| Interactions | "Lưu việc này" → validate → hợp lệ thì sang ST-Loading; chạm chip gợi ý → điền tên, xóa lỗi |
| Navigation | Back → S05 (giữ lựa chọn); lưu → `go('/today/add/result')` |
| UI constraints | Không dùng `showTimePicker` dạng bánh xe; Switch có vùng chạm toàn hàng (cao ≥ 64) |

## S07 – Lịch tuần

| Mục | Đặc tả |
| --- | --- |
| Layout | Header `headline` + khoảng ngày → `ListView` 7 hàng ngày (cao ≥ 68, hôm nay ≥ 76 viền `primary`) → BottomNav |
| Components | DayRow (Past-done / Past-partial / Today / Future), BottomNav |
| States | Loading; Có dữ liệu; Tuần trống: dòng "Tuần này chưa có việc" + nút "Thêm việc" |
| Interactions | Chạm ngày → mở danh sách việc của ngày đó (dùng lại layout S03 với ngày được chọn) |
| Navigation | Tab 1 |
| UI constraints | Trạng thái ngày luôn có chữ (6/6, 5/6), không chỉ màu |

## S08 – 9 thói quen Power 9

| Mục | Đặc tả |
| --- | --- |
| Layout | Header `headline` + phụ đề → `ListView` 9 hàng (cao ≥ 60: icon 40, tên `body-lg` bold, mô tả `body-md`) → BottomNav |
| Components | HabitRow, BottomNav |
| States | Tĩnh (nội dung có sẵn trong app); không cần trạng thái mạng |
| Interactions | Chạm hàng → trang mô tả thói quen + nút "Thêm vào lịch" (dẫn tới S06 với thói quen đó) |
| Navigation | Tab 2 |
| UI constraints | Nội dung dạng văn bản ngắn, câu ≤ 20 từ |

## S09 – Gia đình

| Mục | Đặc tả |
| --- | --- |
| Layout | Header → `ListView(gap 12)`: FamilyCard × n, banner nhắc nhở (`warning-container`), nút viền đứt "Thêm người thân" → BottomNav |
| Components | FamilyCard (avatar chữ cái 56, tên, lần gọi cuối, Primary "Gọi điện", Secondary "Khoe hôm nay"), Banner, Button |
| States | Chưa có người thân → Empty "Thêm số điện thoại con cháu"; Có dữ liệu; Gửi khoe lỗi → `ErrorView` banner |
| Interactions | "Gọi điện" → `url_launcher` `tel:`; "Khoe hôm nay" → chia sẻ tiến độ (Zalo/SMS qua `share_plus`) |
| Navigation | Tab 3 |
| UI constraints | Gọi điện mở ngay, không hộp thoại phụ; tên người thân `title-md` |

## S10 – Cài đặt hiển thị

| Mục | Đặc tả |
| --- | --- |
| Layout | AppBar Back "Hôm nay" → `headline` → Card cỡ chữ (3 lựa chọn + xem thử) → Card 3 `SwitchListTile` (Tương phản cao, Đọc to nội dung, Rung khi nhắc) → nút viền "Nhờ con cháu cài giúp" |
| Components | SegmentedButton/Radio, SwitchListTile × 3, Button Secondary |
| States | Giá trị đọc từ `SharedPreferences`; Tương phản cao bật → đổi `ColorScheme` sang biến thể high-contrast |
| Interactions | Đổi cỡ chữ → áp dụng toàn app ngay; "Nhờ con cháu cài giúp" → gọi số người thân đầu tiên |
| Navigation | `push('/settings')` từ S03; Back → S03 |
| UI constraints | Đọc to dùng `flutter_tts` ngôn ngữ `vi-VN`; không có thiết lập nào cần nhập chữ |

---

## States & Dialog dùng chung

| ID | Layout | Thành phần / hành vi |
| --- | --- | --- |
| ST-Empty | Căn giữa: icon tròn 140, `title-lg`, 1 câu hướng dẫn, Primary "Thêm việc đầu tiên", Secondary "Dùng lịch mẫu Power 9" | Thay danh sách khi không có việc |
| ST-Validation | Trong S06: `InputDecoration(errorText)` + icon + chip gợi ý | `Semantics(liveRegion)` để TalkBack đọc lỗi |
| ST-Loading | Toàn màn: `CircularProgressIndicator` 88 + "Đang lưu việc…" + "Không cần bấm gì thêm" | Không có nút; tự chuyển khi xong |
| ST-Error | Toàn màn: icon wifi-off trong nền `error-container`, `headline` "Chưa lưu được", câu "vẫn được giữ lại" + 3 nút xếp dọc | Thử lại → Loading; Lưu trên máy → lưu `Hive`/`sqflite` + đồng bộ sau; Quay lại sửa → S06 |
| ST-Saved | Icon ✓ 128 trên `primary`, `headline`, Card tóm tắt việc, Primary "Về trang Hôm nay", Secondary "Thêm việc khác" | Không tự tắt |
| DLG-Done | `AlertDialog` radius 24, icon ✓ 64, tiêu đề `title-lg`, mô tả, 2 nút full-width xếp dọc | `barrierDismissible: true`; "Đúng, đã xong" → cập nhật + đóng; "Chưa, để sau" → đóng |

---

## Bảng 1 – Token → Flutter

| Token Figma | Giá trị | Flutter |
| --- | --- | --- |
| `color/primary` | `#1F6B4A` | `ColorScheme.primary` |
| `color/on-surface` | `#1F2A24` | `ColorScheme.onSurface` |
| `color/on-surface-variant` | `#4A5550` | `ColorScheme.onSurfaceVariant` |
| `color/bg` | `#FBF8F2` | `ThemeData.scaffoldBackgroundColor`, `ColorScheme.surface` |
| `color/surface` | `#FFFFFF` | `ColorScheme.surfaceContainerLowest` |
| `color/primary-container` | `#D7EDE0` | `ColorScheme.primaryContainer` |
| `color/on-primary-container` | `#0F3D2A` | `ColorScheme.onPrimaryContainer` |
| `color/secondary` | `#A3471F` | `ColorScheme.secondary` |
| `color/error` | `#B3261E` | `ColorScheme.error` |
| `color/error-container` | `#FCE4E1` | `ColorScheme.errorContainer` |
| `color/warning-container` | `#FFF1D6` | `AppColors.warningContainer` (ThemeExtension) |
| `color/success` | `#2E6B2F` | `AppColors.success` (ThemeExtension) |
| `color/outline` | `#7A857F` | `ColorScheme.outline` |
| `display` 34/42 Bold | | `TextTheme.displaySmall` (fontSize 34, height 42/34) |
| `headline` 28/36 Bold | | `TextTheme.headlineMedium` (28, height 1.29) |
| `title-lg` 24/32 Bold | | `TextTheme.titleLarge` (24, height 1.33) |
| `title-md` 20/28 Bold | | `TextTheme.titleMedium` (20, height 1.4) |
| `body-lg` 18/28 | | `TextTheme.bodyLarge` (18, height 1.56) |
| `body-md` 16/24 | | `TextTheme.bodyMedium` (16, height 1.5) |
| `label-nav` 15/20 | | `NavigationBarThemeData.labelTextStyle` |
| `space/4…48` | 4, 8, 12, 16, 20, 24, 32, 48 | `abstract final class AppSpace { static const s4 = 4.0; … s48 = 48.0; }` |
| `radius/sm, md, button, lg, xl` | 8, 12, 14, 16, 24 | `AppRadius.sm …` → `BorderRadius.circular(x)` |
| `radius/full` | 999 | `StadiumBorder()` |
| `elevation/1` | Y2 Blur6 10 % | `BoxShadow(offset: Offset(0, 2), blurRadius: 6, color: Color(0x1A1F2A24))` |
| `elevation/2` | Y8 Blur24 24 % | `DialogThemeData(elevation: 6, shadowColor: Colors.black38)` |
| Font Be Vietnam Pro | | `GoogleFonts.beVietnamProTextTheme(base)` |

## Bảng 2 – Component → Widget

| Component Figma | Variant | Widget Flutter |
| --- | --- | --- |
| `Button` | Primary | `FilledButton(style: FilledButton.styleFrom(minimumSize: Size.fromHeight(56), shape: RoundedRectangleBorder(borderRadius: AppRadius.button)))` |
| `Button` | Secondary | `OutlinedButton` (side 2 dp `primary`) |
| `Button` | Tonal ("Thêm việc") | `FilledButton` nền `secondary`, `StadiumBorder`, cao 48 |
| `Button` | Text | `TextButton` gạch chân |
| `Button` | Disabled | `onPressed: null` |
| `TextField` | Default / Focused / Error | `TextField` + `InputDecoration(labelText ở ngoài qua Column, helperText, errorText)`, `OutlineInputBorder(radius 12)` |
| `TaskCard` | Next | `Card(color: primaryContainer-lighter, shape: side 2 primary)` + `Column` |
| `TaskRow` | Upcoming / Done | `ListTile(minTileHeight: 64, leading: CircleAvatar 44)` |
| `NavItem` / `BottomNav` | Active / Inactive | `NavigationBar(height: 84, labelBehavior: NavigationDestinationLabelBehavior.alwaysShow)` + `NavigationDestination` |
| `AppBar` | Back+Step / Greeting | `AppBar(leading: TextButton.icon(icon: arrow_back, label: Text('Quay lại')), leadingWidth: 140, actions: [Text('Bước 1 / 2')])` |
| `Dialog` | Confirm | `AlertDialog` + `actions` là `Column` 2 nút full-width; mở bằng `showDialog` |
| `Loading` | Full-screen / Inline | `CircularProgressIndicator(strokeWidth: 6)` + `Text`, bọc `Semantics(liveRegion: true)` |
| `EmptyState` | — | Widget tự viết `EmptyState({icon, title, message, primaryAction, secondaryAction})` |
| `ErrorView` | Inline / Banner / Full-screen | `InputDecoration.errorText` / `MaterialBanner` / widget `ErrorView({message, onRetry, onSaveLocal, onEdit})` |
| `TimeStepper` | — | `Row(IconButton.filledTonal(56×56, tooltip: 'Sớm hơn 15 phút'), Text(titleLarge), IconButton.filledTonal(...))` |
| `HabitTile` | Selected | `Material` + `InkWell` hoặc `ChoiceChip` tùy biến, viền 3 dp khi chọn, `Semantics(selected: true)` |
| `Switch` | On / Off | `SwitchListTile(minTileHeight: 68)` |

## Hạn chế & việc tiếp theo

- Chưa test với người dùng thật ngoài gia đình; số liệu thành công trong persona.md cần đo lại.
- Chưa thiết kế dark mode (chế độ tương phản cao ở S10 là ưu tiên hơn).
- "Đọc to nội dung" phụ thuộc engine TTS tiếng Việt có trên máy.
- Đồng bộ dữ liệu cho con cháu (Khoe hôm nay) cần backend, ngoài phạm vi Lab 2.
