# Flutter Handoff – An Nhiên

Tài liệu này đủ để một lập trình viên Flutter chưa biết dự án hiện thực từng màn hình và các trạng thái của nó. Lab 2 không yêu cầu code.

**Quy ước chung**

- Flutter 3.x, Material 3 (`useMaterial3: true`), font `GoogleFonts.beVietnamPro`.
- Điều hướng: `go_router` + `StatefulShellRoute` cho 4 tab (chế độ Người lớn tuổi) và một nhánh `/caregiver` riêng cho chế độ Người thân.
- Dữ liệu: lưu trên máy trước (offline-first, `drift`/`sqflite`), dùng được khi mất mạng (N20). Đồng bộ với máy người thân cần backend – ngoài phạm vi Lab 2.
- Chọn giờ: ô giờ `◷ 8 : 00 sáng ⌄` mở `DLG-TaskTime` / `DLG-WakeTime`. Picker khởi tạo từ giá trị đã lưu; Hủy không lưu nháp; chỉ Xong mới ghi. Giờ 1–12, phút 00–59, sáng/chiều. Native picker cần snap theo vị trí khi thả tay.
- Mọi kích thước tính bằng dp (logical pixels). Token lấy từ `AppTheme`, `AppSpace` và `AppRadius` (bảng 1), không hard-code.
- Ràng buộc chung cho mọi màn: chữ ≥ 20 sp (kể cả nhãn nav), nội dung 24 sp, nút chính 60 dp, vùng chạm ≥ 48 dp, khoảng cách giữa nút ≥ 8 dp, hỗ trợ `textScaler` tới 2.0 mà không tràn, contrast ≥ 4.5 : 1, không có cử chỉ vuốt bắt buộc.

## Route map

| Route | Màn | Ghi chú |
| --- | --- | --- |
| `/welcome` | S01 | Chỉ khi chưa onboarding |
| `/setup` | S02 | Bước 1/2 |
| `/setup/notifications` | S13 / S13d | Bước 2/2; S13d là trạng thái của cùng route khi quyền bị từ chối |
| `/reminder/:taskId` | S14 | Mở từ `flutter_local_notifications` với `fullScreenIntent: true`; cũng mở được từ S10 ("Xem thử lời nhắc", tham số `?preview=true`) |
| `/today` | S03 | Tab 0 |
| `/today/task/:id` | S04 | |
| `/today/task/:id/edit` | S15 | Push từ nút "Sửa" trên app bar S04 |
| `/today/add/type` | S05 | |
| `/today/add/time?habit=` | S06 | |
| `/today/add/result` | ST-Saved / ST-Error | Thay thế (`go`), không push chồng |
| `/week` | S07 | Tab 1 |
| `/today/all` | S11 (chế độ hôm nay) | Push từ nút "Xem cả ngày" ở S03 |
| `/week/:date` | S11 / S11b | Push từ S07; `date` dạng `2026-10-09`. Chạm hàng hôm nay ở S07 thì chuyển sang tab `/today` |
| `/week/:date/task/:id` | S04 | Cùng widget với `/today/task/:id` |
| `/habits` | S08 | Tab 2 |
| `/habits/:key` | S16 | `key` = `move`, `purpose`, `downshift`, `eighty`, `plant`, `tea`, `belong`, `family`, `tribe` |
| `/family` | S09 | Tab 3 |
| `/settings` | S10 | Push từ S03 |
| `/family/add` | S12 | Push từ S09; lưu xong `pop` về S09 kèm thông báo thành công (S09b) |
| `/family/:personId/share` | S17 → S17b / N10 | Push từ nút "Nhắn tin" ở thẻ người thân S09 hoặc từ thẻ chúc mừng ở S03; mở `share_plus` xong `replace` sang S17b |
| `/family/:personId/edit` | N09 → N15 → N21 | Sửa / xóa người thân |
| `/family/suggestions/:id` | G03 – G09 | Mở từ hàng "Gợi ý từ Mai" ở S09, popup G11 hoặc thẻ G12 ở S03 |
| `/setup/try-reminder` | N01 → N02 / N03 | Sau S13 khi đã bật nhắc việc |
| `/setup/first-task` | N04 → N05 → N18 → N19 | Việc đầu tiên |
| `/settings/profile` · `/settings/reminders` · `/settings/help` · `/settings/data` | N06 · N07 · N08 · N20 | Push từ S10 |
| `/task/date` · `/task/repeat` · `/task/scope` | N11 · N12 · N13 | Màn con dùng chung cho S06, S15, N05; trả kết quả bằng `pop(result)` |
| `/role` | C01 | Màn đầu tiên khi chưa chọn vai trò |
| `/caregiver/pair` | C02 / C02e | |
| `/caregiver/schedule?view=day\|week\|month` | C03 / C04 / C05 | Tab trong màn |
| `/caregiver/task/new` → `/repeat` → `/review` | C06 / C06e → C07 / C07m → C08 (+ C08w) → C09 | Form 3 bước, giữ state bằng một `Cubit` chung |
| `/caregiver/task/:id` | C10 → C06 (sửa) → C11; C12 | |

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
| Layout | AppBar (Back+Step "Bước 1 / 2") → `ListView(padding 20)`: `headline` "Làm quen một chút", mô tả, TextField "Tên gọi" (gợi ý "Ví dụ: Lan, Sáu, Tư…"), nhóm "An Nhiên gọi là" ○ Ông / ● Bà, ô giờ "Thường thức dậy lúc" (◷ 5 : 00 sáng ⌄), TextField "Số điện thoại người thân (không bắt buộc)" → Footer nút "Tiếp tục" |
| Components | AppBar, TextField × 2, Radio × 2, TimeField + `DLG-WakeTime`, Button Primary |
| States | Default; Focused; Error khi Tên trống ("Bà chưa nhập tên gọi"); SĐT sai định dạng → Error; Bàn phím mở (frame `S02 · Bàn phím mở · số điện thoại`) – nút Tiếp tục vẫn thấy |
| Interactions | Chạm ô giờ → `DLG-WakeTime` (mặc định 5:00 sáng); chọn Ông/Bà đổi cách xưng hô toàn app; "Tiếp tục" validate rồi lưu |
| Navigation | Back → S01; hợp lệ → `push('/setup/notifications')` (S13, Bước 2/2) |
| UI constraints | `keyboardType: TextInputType.phone` cho SĐT; nút không bị bàn phím che (`resizeToAvoidBottomInset`) |

## S03 – Hôm nay

| Mục | Đặc tả |
| --- | --- |
| Layout | `Scaffold(bg)`; body = `Column`: Header ("Thứ Năm, 8/10" + nút "Cài đặt", lời chào `headline` "Chào Bác Lan") → `Expanded(ListView(padding 20, gap 16))`: (thẻ gợi ý G12 nếu có) → tiêu đề "Việc tiếp theo" + "Xem cả ngày", NextTaskCard, hàng tiêu đề "Còn lại hôm nay" + Button Tonal "Thêm việc", danh sách TaskRow, thẻ "Nhìn lại hôm nay · 3 việc đã làm"; `bottomNavigationBar` |
| Components | AppBar Greeting, TaskCard Next (Button Primary "Đã xong" + Secondary "Dời lại"), TaskRow (Upcoming/Done/Skipped), Button Tonal, BottomNav |
| States | Loading: spinner + "Đang tải lịch…"; Empty: ST-Empty; Có dữ liệu; Lỗi tải: `ErrorView` banner + "Thử lại"; **Tất cả đã xong** (S03 xong 6/6): lời chào đổi theo buổi, `CelebrateCard` (icon ✓ 72, "Bà đã xong cả 6 việc hôm nay!", Primary "Báo tin vui cho Mai" → S17, Text "Xem lịch ngày mai" → S11 ngày mai) thay NextTaskCard, danh sách đổi tiêu đề thành "Đã xong"; **Sau khi dời / bỏ qua / xóa / sửa / nhắc lại**: `Snackbar` 2 tầng ngay trên bottom nav (xem bảng States) |
| Interactions | Có gợi ý mới từ người thân → popup G11 hiện **một lần** ("Xem gợi ý" → G03, "Để sau" → thẻ G12 ở đầu trang); xử lý hết việc → N17; "Đã xong" → `showDialog(DLG-Done)`; "Xem cả ngày" (cạnh tiêu đề Việc tiếp theo) → S11 chế độ hôm nay; chạm tên việc (gạch chân) hoặc chạm một TaskRow → S04 của việc đó; "Dời lại" → `showDialog(DLG-Later)`; "Thêm việc" → S05; "Cài đặt" → S10; kéo xuống để làm mới (tùy chọn, không bắt buộc) |
| Navigation | Tab 0 của `NavigationBar`; Back hệ thống tại đây → thoát app |
| UI constraints | NextTaskCard luôn ở đầu, không cuộn mất khi chỉ có ≤ 6 việc; `Semantics` cho thẻ Nhìn lại: "Đã làm 3 việc hôm nay"; kiểm tra ở 412 dp (frame `S03 Hôm nay · 412 dp`) |

## S04 – Chi tiết hoạt động

| Mục | Đặc tả |
| --- | --- |
| Layout | AppBar Back "Quay lại" (mở được từ S03 và S11 nên không ghi tên màn) → `ListView(padding 20)`: nhãn "Thói quen 1 · Vận động tự nhiên", giờ "9:30 sáng · 20 phút", `headline` tên việc, mục "Cách làm" (3 bước có số), Card "Lợi ích" → Footer `surface`: Primary "Tôi đã làm xong", hàng Secondary "Dời 30 phút" + Text "Bỏ qua hôm nay" |
| Components | AppBar (Back+Action ở chế độ Next/Later, Back ở chế độ Done), HabitBadge, Card, numbered list, Button Primary/Secondary/Text |
| States | Theo việc được mở: **Next** – việc tiếp theo hôm nay, Footer có Primary "Tôi đã làm xong" + "Dời 30 phút" + "Bỏ qua hôm nay"; **Later** – việc chưa tới giờ (hôm nay hoặc ngày sau), Footer chỉ có hộp nhắc `warning-container` "Hẹn 7:00 sáng, Thứ Sáu… An Nhiên sẽ nhắc bà trước 10 phút." + Secondary "Quay lại lịch"; **Done** – hộp `primary-container` "Bà đã làm xong việc này hôm nay" + "Quay lại lịch" (bản Flutter thêm "Hoàn tác"). Nội dung "Cách làm" và "Lợi ích" lấy theo từng việc |
| Interactions | (chế độ Next) "Tôi đã làm xong" → DLG-Done; "Dời 30 phút" → cập nhật giờ, quay về S03 kèm Snackbar "Đã dời “Đi bộ” sang 10:00 sáng · Hoàn tác"; "Bỏ qua hôm nay" → DLG-Skip; nút "Sửa" (chữ + icon bút, góc phải app bar, chỉ có ở việc chưa làm) → S15 |
| Navigation | `push('/today/task/:id')` từ S03 hoặc `push('/week/:date/task/:id')` từ S11; Back → `pop()` về đúng màn đã mở |
| UI constraints | Footer cố định, nội dung cuộn phía trên; nút 60 dp |

## S05 – Thêm việc: chọn hoạt động

| Mục | Đặc tả |
| --- | --- |
| Layout | AppBar "Hủy" + "Bước 1 / 2" → `headline` "Bác muốn làm gì?" + "Chọn một việc quen thuộc." → 3 thẻ việc lớn (icon + tên + mô tả: "Đi bộ nhẹ nhàng – Vận động theo sức của Bác", "Chăm cây – Tưới cây hoặc chăm vườn", "Gọi người thân – Dành thời gian trò chuyện") → Text button "Xem thêm hoạt động" (mở danh sách theo 9 thói quen) |
| Components | ActivityCard × 3 (`HabitTile` biến thể lớn), Button Text |
| States | Mặc định 3 việc quen thuộc; "Xem thêm" → danh sách theo 9 thói quen Power 9 |
| Interactions | Chạm một thẻ → S06 với tên việc và thói quen điền sẵn (không cần nút Tiếp tục) |
| Navigation | `push('/today/add/type')`; "Hủy" → `pop` về S03 (hỏi N14 nếu đã chọn gì) |
| UI constraints | Thẻ cao ≥ 92 dp, cả thẻ là vùng chạm; màu thói quen chỉ là tín hiệu phụ (có icon + tên) |

## S06 – Thêm việc: thiết lập việc

| Mục | Đặc tả |
| --- | --- |
| Layout | AppBar Back + "Bước 2 / 2" → `ListView(padding 20, gap 16)`: nhãn "Thiết lập việc", `headline` "Làm lúc nào?", TextField "Tên việc" (gợi ý "Ví dụ: Tập thở 10 phút, Ngủ trưa 20 phút"), ô "Giờ làm" (◷ 8 : 00 sáng ⌄, 320 × 62), hàng "Lặp lại": Mỗi ngày / Chọn ngày, hàng "Nhắc bằng chuông và rung · Trước 10 phút", hàng "Ngày thực hiện · Ngày mai" → Footer "Lưu việc này" |
| Components | TextField, TimeField + `DLG-TaskTime`, SegmentedButton (156 × 60), SwitchListTile, ListTile mở N11 / N12, Button Primary |
| States | Default; Validation (S06e → ST-Validation: tên trống → viền `error`, icon, chữ lỗi, chip gợi ý); Lưu thất bại (S06o → ST-Loading-offline → ST-Error); Lưu được nhưng chưa đặt được lời nhắc → N16 |
| Interactions | Chạm ô giờ → `DLG-TaskTime`; "Chọn ngày" → N12 (7 ngày, có kiểm tra không để trống); "Ngày thực hiện" → N11; "Lưu việc này" → validate → ST-Loading → ST-Saved |
| Navigation | Back → S05 (nếu đã nhập → N14); lưu → `go('/today/add/result')` |
| UI constraints | Ô giờ là nút, không phải TextField; nút Lưu không bị bàn phím che; Switch có vùng chạm toàn hàng |

## S07 – Lịch tuần

| Mục | Đặc tả |
| --- | --- |
| Layout | Header `headline` + khoảng ngày → `ListView` 7 hàng ngày (cao ≥ 68, hôm nay ≥ 76 viền `primary`) → BottomNav |
| Components | DayRow (Past-done / Past-partial / Today / Future), mỗi hàng có mũi tên › báo hiệu bấm được, BottomNav |
| States | Loading; Có dữ liệu; Tuần trống: dòng "Tuần này chưa có việc" + nút "Thêm việc" |
| Interactions | Chạm hàng "Hôm nay" → chuyển sang tab Hôm nay (S03); chạm ngày khác → S11 Chi tiết ngày của đúng ngày đó |
| Navigation | Tab 1 |
| UI constraints | Trạng thái ngày luôn có chữ (6/6, 5/6), không chỉ màu |

## S11 – Chi tiết ngày

| Mục | Đặc tả |
| --- | --- |
| Layout | AppBar Back "Lịch tuần" (chế độ hôm nay: "Hôm nay" + nhãn HÔM NAY trên tiêu đề) → `ListView(padding 20, gap 8)`: `headline` "Thứ Sáu, 9 tháng 10", thẻ tóm tắt (icon + "6 việc · bắt đầu 6:00 sáng" + gợi ý "Chạm vào một việc để xem cách làm"), rồi từng nhóm buổi (Sáng < 11h, Trưa 11–13h, Chiều 13–18h, Tối ≥ 18h): nhãn buổi `body-md` bold + các TaskRow → Footer `surface`: Button Tonal "Thêm việc cho ngày này" (chỉ ngày sắp tới) |
| Components | AppBar Back, SummaryCard, SessionHeader, TaskRow (Upcoming / Done / Skipped), Button Tonal |
| States | Hôm nay (mở từ S03): tóm tắt "Đã xong 3 / 6 việc · tiếp theo 9:30 sáng", trộn TaskRow Done và Upcoming, đều bấm được, nút "Thêm việc cho hôm nay"; Ngày sắp tới (S11): TaskRow Upcoming, dòng giờ ghi kèm tên thói quen ("9:30 sáng · Vận động tự nhiên"); Ngày đã qua (S11b): tóm tắt "Đã xong 5 / 6 việc" + "Ngày đã qua – chỉ xem lại", TaskRow Done ("Đã xong · 6:00 sáng") hoặc Skipped ("Bỏ qua · 9:30 sáng (trời mưa)"), không có Footer; Ngày không có việc: `EmptyState` "Ngày này chưa có việc nào" + "Thêm việc cho ngày này"; Loading / Lỗi tải: như S03 |
| Interactions | Chạm TaskRow của ngày sắp tới → S04 của việc đó; TaskRow của ngày đã qua không bấm được (chỉ xem); "Thêm việc cho ngày này" → S05, S06 điền sẵn ngày |
| Navigation | `push('/week/:date')` từ S07; Back → S07. Không có bottom nav vì là màn con của tab Lịch tuần |
| UI constraints | Nhóm buổi trống thì ẩn; trạng thái luôn có chữ, không chỉ màu; danh sách cuộn dọc, giữ nguyên khi `textScaler` 2.0; `Semantics(header: true)` cho tiêu đề ngày và nhãn buổi để TalkBack nhảy theo nhóm |

## S08 – 9 thói quen Power 9

| Mục | Đặc tả |
| --- | --- |
| Layout | Header `headline` "Hoạt động mỗi ngày" + phụ đề "Chọn việc phù hợp với sức của Bác." → `ListView` 9 hàng "1. Vận động tự nhiên … 9. Bạn bè tích cực" (icon, tên `body-lg` bold, mô tả `body-md`, mũi tên ›) → BottomNav. Thói quen 4 hiển thị là "Ăn vừa đủ" |
| Components | HabitRow, BottomNav |
| States | Tĩnh (nội dung có sẵn trong app); không cần trạng thái mạng |
| Interactions | Chạm hàng (cả hàng là vùng chạm, có mũi tên ›) → S16 Chi tiết thói quen |
| Navigation | Tab 2 |
| UI constraints | Nội dung dạng văn bản ngắn, câu ≤ 20 từ |

## S09 – Gia đình

| Mục | Đặc tả |
| --- | --- |
| Layout | Header "Gia đình" + "Gọi nhanh, trò chuyện và nhận gợi ý từ người thân." → hàng "Gợi ý từ Mai · 2 việc" (khi có gợi ý) → `ListView(gap 12)`: FamilyCard × n (thẻ lâu chưa gọi có câu nhắc "Bà có muốn gọi cho Hùng hôm nay không?"), nút viền "Thêm người thân" → BottomNav |
| Components | FamilyCard (avatar chữ cái 56, tên, lần gọi cuối, Primary "Gọi điện", Secondary "Nhắn tin" có icon tin nhắn), Banner, Button |
| States | Chưa có người thân → Empty "Thêm số điện thoại con cháu"; Có dữ liệu; Vừa thêm người thân (S09b): banner `primary-container` viền `primary` "Đã thêm Cháu Bin…" không tự tắt + thẻ mới ở cuối; Gửi tin nhắn lỗi → `ErrorView` banner |
| Interactions | "Gọi điện" → `url_launcher` `tel:`; "Nhắn tin" → S17 cho đúng người đó; chạm tên → N09 Sửa người thân; "Gợi ý từ Mai" → G03; "Thêm người thân" → S12 |
| Navigation | Tab 3 |
| UI constraints | Gọi điện mở ngay, không hộp thoại phụ; tên người thân `title-md` |

## S12 – Thêm người thân

| Mục | Đặc tả |
| --- | --- |
| Layout | AppBar Back "Gia đình" → `ListView(padding 20, gap 16)`: `headline` "Thêm người thân", Button Secondary "Chọn từ danh bạ điện thoại" (đặt trên cùng vì nhanh nhất), chữ phụ "hoặc tự nhập", TextField "Tên gọi", nhãn "Là gì của bà?" + 4 lựa chọn Con / Cháu / Bạn bè / Khác (cao 52), TextField "Số điện thoại", hàng công tắc "Gọi nhanh cho người thân" (chú thích "Lưu số để gọi nhanh. Chỉ gửi tin khi Bác chọn gửi.") → Footer Primary "Lưu người thân" |
| Components | AppBar Back, Button Secondary/Primary, TextField (Default/Error), SegmentedButton tùy biến cho quan hệ, SwitchListTile |
| States | Mới mở (S12a): số trống, gợi ý "Ví dụ: 0912 345 678"; Đã điền (S12); Thiếu / sai số (S12e): `errorText` "Bà chưa nhập số điện thoại. Bấm “Chọn từ danh bạ điện thoại” ở trên cho nhanh.", giữ nguyên tên và quan hệ đã nhập; Đang lưu: nút hiện `CircularProgressIndicator` nhỏ + "Đang lưu…" |
| Interactions | "Chọn từ danh bạ điện thoại" → `flutter_contacts` (`FlutterContacts.openExternalPick()`), xin quyền danh bạ kèm câu giải thích; điền sẵn tên + số. "Lưu người thân" → validate số 10 chữ số (bỏ khoảng trắng, chấp nhận +84) → lưu → `pop` về S09 với banner thành công |
| Navigation | `push('/family/add')` từ S09; Back → S09, nếu đã nhập dữ liệu thì hỏi "Bỏ người thân đang nhập?" trước khi thoát |
| UI constraints | `keyboardType: TextInputType.phone`, `autofillHints: [AutofillHints.telephoneNumber]`; tự chèn khoảng trắng 4-3-3 khi gõ; không bắt chọn quan hệ (mặc định "Khác"); nút Lưu không bị bàn phím che |

## S10 – Cài đặt hiển thị

| Mục | Đặc tả |
| --- | --- |
| Layout | AppBar Back "Hôm nay" → `headline` "Cài đặt hiển thị" → Card cỡ chữ (Vừa / Lớn / Rất lớn + "Xem thử: Đi bộ 20 phút lúc 9:30 sáng") → Card 3 `SwitchListTile` (Tương phản cao, Đọc to nội dung, Rung khi nhắc việc – kèm chuông) → nút viền "Xem thử lời nhắc" → danh sách: "Cách dùng đơn giản" (N08), "Sửa hồ sơ" (N06), "Nhắc việc" (N07), "Dữ liệu trên điện thoại" (N20) |
| Components | SegmentedButton/Radio, SwitchListTile × 3, Button Secondary × 2 |
| States | Giá trị đọc từ `SharedPreferences`; Tương phản cao bật → đổi `ColorScheme` sang biến thể high-contrast |
| Interactions | Đổi cỡ chữ → áp dụng toàn app ngay; "Xem thử lời nhắc" → S14 ở chế độ xem trước (có đọc to, không ghi nhận gì vào lịch); 4 hàng dưới cùng → N08 / N06 / N07 / N20 |
| Navigation | `push('/settings')` từ S03; Back → S03 |
| UI constraints | Đọc to dùng `flutter_tts` ngôn ngữ `vi-VN`; không có thiết lập nào cần nhập chữ |

## S13 – Cho phép nhắc việc (Bước 2/2)

| Mục | Đặc tả |
| --- | --- |
| Layout | AppBar Back+Step "Bước 2 / 2" → `Column(padding 24, gap 16)`: hình chuông tròn 104, `headline` "Cho phép An Nhiên nhắc việc", 1 câu giải thích `body-lg`, thẻ "Ví dụ · 9:20 sáng – Còn 10 phút: Đi bộ quanh công viên" (giống thông báo thật), hộp `warning-container` "Bấm nút bên dưới, điện thoại sẽ hỏi lại. Bà chọn “Cho phép” là xong." → Footer: Primary "Bật nhắc việc", Text "Để sau" |
| Components | AppBar, Card xem trước thông báo, InlineHint, Button Primary/Text |
| States | Chưa hỏi; Đã cho phép → đi tiếp; Bị từ chối / "Để sau" → **S13d**: icon chuông gạch 112 trên `error-container`, `headline` "Nhắc việc đang tắt", câu nói rõ hậu quả ("đến giờ điện thoại sẽ không đổ chuông… phải tự mở An Nhiên"), hộp chỉ đường bật lại "Hôm nay › Cài đặt › Nhắc việc", Primary "Bật nhắc việc" (mở `openAppSettings()` khi đã bị từ chối hẳn) + Secondary "Vẫn để sau" |
| Interactions | "Bật nhắc việc" → `Permission.notification.request()` (`permission_handler`); Android 14+ thêm `USE_FULL_SCREEN_INTENT` và `SCHEDULE_EXACT_ALARM`; xong → `go('/today')` (ST-Empty nếu chưa có việc) |
| Navigation | Back → S02; không chặn người dùng: cả hai nhánh đều vào được app |
| UI constraints | Giải thích **trước** khi hộp thoại hệ thống hiện (priming), vì người lớn tuổi hay bấm "Từ chối" khi bất ngờ; không xin quyền ngay ở S01 |

## S14 – Lời nhắc đến giờ (toàn màn hình)

| Mục | Đặc tả |
| --- | --- |
| Layout | Không AppBar, không bottom nav. `Column(padding 20, top 28)`: giờ hiện tại `display` + ngày `body-md` bold căn giữa (như màn khóa) → Card `surface` radius 24: icon thói quen 88, chip `warning-container` "Còn 10 phút nữa" (icon đồng hồ), tên việc `headline` căn giữa, dòng "9:30 sáng · 20 phút · Vận động tự nhiên", hàng `primary-container-soft` "Đang đọc to lời nhắc" + Text "Đọc lại" → Footer 3 nút xếp dọc: Primary "Bắt đầu làm", Secondary "Nhắc lại sau 10 phút", Text "Hôm nay bỏ qua" |
| Components | ReminderCard, Chip đếm ngược, ReadAloudRow, Button Primary/Secondary/Text |
| States | Trước giờ hẹn ("Còn 10 phút nữa"); Đúng giờ ("Đến giờ rồi"); Trễ ("Trễ 15 phút – làm bây giờ vẫn tốt"); Xem trước từ S10 (nhãn "Đây là lời nhắc mẫu", các nút chỉ đóng màn) |
| Interactions | "Bắt đầu làm" → S04 của việc đó; "Nhắc lại sau 10 phút" → hẹn lại thông báo, về S03 với Snackbar "An Nhiên sẽ nhắc lại lúc 9:30 sáng."; "Hôm nay bỏ qua" → DLG-Skip; "Đọc lại" → `flutter_tts.speak` |
| Navigation | Mở bằng `fullScreenIntent` khi máy khóa, hoặc heads-up notification khi đang dùng máy → chạm vào thì mở route này |
| UI constraints | Không có cử chỉ vuốt để tắt (vuốt nhầm là mất lời nhắc); chuông + rung + chữ cùng lúc; tự đọc to nếu bật ở S10; chuông lặp tối đa 1 phút rồi chuyển thành thông báo thường (không kêu mãi) |

## S15 – Sửa việc

| Mục | Đặc tả |
| --- | --- |
| Layout | AppBar Back "Quay lại" → `ListView(padding 20, gap 12)`: chip thói quen, `headline` "Sửa việc", TextField "Tên việc", nhãn "Giờ làm" + ô giờ mở `DLG-TaskTime`, dòng "Đã đổi từ 9:30 sáng" (icon đồng hồ, chỉ hiện khi đã đổi giờ), SegmentedButton Lặp lại, SwitchListTile Nhắc nhở, vùng nguy hiểm (kẻ ngang phía trên): Button Danger-outline "Xóa việc này" + chú thích "Bà sẽ được hỏi lại trước khi xóa." → Footer Primary "Lưu thay đổi" |
| Components | AppBar, Chip, TextField, TimeField + `DLG-TaskTime`, SegmentedButton, SwitchListTile, Button Danger-outline, Button Primary |
| States | Chưa đổi gì → "Lưu thay đổi" disabled; Đã đổi; Validation (tên trống) như ST-Validation; Đang lưu → nút hiện spinner nhỏ + "Đang lưu…" |
| Interactions | Chạm ô giờ → `DLG-TaskTime`; việc lặp lại → hỏi phạm vi N13 ("Chỉ lần này" / "Lần này và các lần sau" / "Giữ nguyên") trước khi lưu; "Lưu thay đổi" → lưu → `pop` 2 cấp về S03 với Snackbar "Đã lưu: Đi bộ lúc 10:00 sáng, mỗi ngày."; "Xóa việc này" → DLG-Delete |
| Navigation | `push('/today/task/:id/edit')`; Back khi đã đổi → N14 "Chưa lưu thay đổi" ("Tiếp tục chỉnh" là nút chính, "Bỏ thay đổi") |
| UI constraints | Nút xóa đặt cuối nội dung, cách nút Lưu ≥ 1 màn cuộn hoặc ≥ 32 dp; chỉ việc chưa làm mới sửa được (việc ngày đã qua chỉ xem) |

## S16 – Chi tiết thói quen

| Mục | Đặc tả |
| --- | --- |
| Layout | AppBar Back "Thói quen" → `ListView(padding 20, gap 14)`: hàng icon 72 + "Thói quen 3 / 9" + tên `headline`, đoạn giới thiệu `body-lg` → Card "Tuần này bà đã làm 4 lần": 7 ô T2…CN (hôm nay ghi "Nay", viền `primary`), mỗi ô có dấu ✓ (đã làm), ✕ (bỏ qua), vòng tròn rỗng (sắp tới) hoặc "–" (không có việc), chú thích bằng chữ bên dưới → hộp màu thói quen "Học từ đâu?" (icon quả địa cầu + vùng Blue Zones) → "Việc của bà thuộc thói quen này" (TaskRow, dòng giờ "9:30 sáng · mỗi ngày") → "Gợi ý để bắt đầu" (chip có dấu +) → Footer Primary "Thêm việc cho thói quen này" |
| Components | HabitHeader, WeekStrip (7 × DayMark), OriginCard, TaskRow, Chip, Button Primary |
| States | Có việc; **Chưa có việc** (vd thói quen 9): hộp "Bà chưa có việc nào cho thói quen này. Thử một gợi ý bên dưới nhé."; Tuần chưa làm lần nào: tiêu đề "Tuần này bà chưa làm lần nào" (không trách) |
| Interactions | "Thêm việc cho thói quen này" / chạm chip gợi ý → S06 với `habit` chọn sẵn (chip điền sẵn tên việc); chạm TaskRow → S04 của lần làm gần nhất sắp tới |
| Navigation | `push('/habits/:key')`; Back → S08 |
| UI constraints | Ô ngày ≥ 36 dp rộng; trạng thái ngày có icon + `Semantics(label: 'Thứ Hai: đã làm')`, không chỉ dựa vào màu; nội dung "Học từ đâu" ≤ 2 câu |

## S17 – Nhắn tin cho người thân

| Mục | Đặc tả |
| --- | --- |
| Layout | AppBar Back "Gia đình" → `ListView(padding 20, gap 14)`: `headline` "Nhắn tin cho Mai", "Chọn điều Bác muốn kể. Xem lại trước khi gửi." → nhóm "Bác muốn kể điều gì?" (Hỏi thăm con cháu / Kể việc đi bộ / Kể việc chăm cây) → khung xem trước "Tin nhắn gửi Con gái Mai" (các việc đã xong có ✓) + "Nội dung Bác chọn gửi" → "Thêm một câu (không bắt buộc)" 3 chip → "Gửi bằng" 2 radio card (Zalo – khuyên dùng / SMS) → Footer Primary "Tiếp tục gửi cho Mai" |
| Components | ChoiceChip, MessagePreview, Chip, RadioCard, Button Primary |
| States | Mặc định; Đã chọn chủ đề / câu thêm; **S17b**: "Nội dung gửi cho Mai – Tiếp tục trong ứng dụng nhắn tin để kiểm tra và gửi. An Nhiên chưa xác nhận tin đã gửi." + trích câu đầu, Primary "Về trang Gia đình", Secondary "Gọi điện cho Mai"; **N10** khi đã mở app nhắn tin |
| Interactions | "Tiếp tục gửi cho Mai" → `share_plus` / `url_launcher` (Zalo / `sms:`) với nội dung soạn sẵn → `replace` S17b; "Gọi điện cho Mai" → `tel:` |
| Navigation | `push('/family/:personId/share')`; Back → màn trước |
| UI constraints | Bà không phải gõ chữ; xưng hô theo quan hệ (Mẹ – con, Bà – cháu); **không bao giờ** báo "Đã gửi" vì app không biết kết quả |

## States & Dialog dùng chung

| ID | Layout | Thành phần / hành vi |
| --- | --- | --- |
| ST-Empty | Trong S03: "Hôm nay chưa có việc nào", "Bắt đầu nhẹ nhàng với một việc nhỏ.", Primary "Thêm việc đầu tiên", Secondary "Dùng lịch mẫu hoạt động hằng ngày" | Thay danh sách khi không có việc |
| ST-Validation | Trong S06: `InputDecoration(errorText)` + icon + chip gợi ý | `Semantics(liveRegion)` để TalkBack đọc lỗi |
| ST-Loading | Toàn màn: `CircularProgressIndicator` 88 + "Đang lưu việc…" + "Không cần bấm gì thêm" | Không có nút; tự chuyển khi xong |
| ST-Error | Toàn màn: icon cảnh báo trong nền `error-container`, `headline` "Chưa lưu được", "Chưa thể lưu trên điện thoại. Nội dung đang nhập vẫn được giữ lại. Hãy thử lại." + 3 nút xếp dọc | Thử lại → Loading; Kiểm tra lại lịch → S03 (xem việc đã có chưa, tránh lưu trùng); Quay lại sửa → S06 |
| ST-Saved | Icon ✓ 128 trên `primary`, `headline` "Đã lưu xong!", Card tóm tắt việc ("8:00 sáng · mỗi ngày · nhắc trước 10 phút"), Primary "Về trang Hôm nay", Secondary "Thêm việc khác" | Không tự tắt |
| DLG-Done | `AlertDialog` radius 24, icon ✓ 64, tiêu đề `title-lg`, mô tả, 2 nút full-width xếp dọc | `barrierDismissible: true`; "Đúng, đã xong" → cập nhật + đóng; "Chưa, để sau" → đóng |
| DLG-Later | `AlertDialog` radius 24, icon lịch 64, tiêu đề "Dời việc này đến lúc nào?", dòng giờ đang hẹn, 3 Secondary full-width ("30 phút nữa", "Chiều nay, 4 giờ", "Ngày mai, cùng giờ") + Text "Không dời nữa" | Chọn mốc → cập nhật giờ, đóng dialog, Snackbar "Đã dời “Đi bộ” sang 10:00 sáng / 4:00 chiều nay / 9:30 sáng mai" + "Hoàn tác"; không dùng `showTimePicker` |
| DLG-Skip | `AlertDialog` radius 24, icon ✕ 64 trên `disabled-bg`, tiêu đề "Bỏ qua đi bộ hôm nay?", câu "Ngày mai An Nhiên vẫn nhắc như thường. Vì sao bà bỏ qua? (không bắt buộc – bỏ qua được mà không cần chọn lý do)", 4 Secondary lý do ("Trời mưa", "Thấy trong người mệt", "Bận việc nhà", "Lý do khác") + Text "Không bỏ qua nữa" | Chọn lý do → TaskRow Skipped "Bỏ qua · 9:30 sáng (trời mưa)", Snackbar + "Hoàn tác"; chọn "Thấy trong người mệt" → Snackbar thêm nút "Báo cho Mai" |
| DLG-Delete | `AlertDialog` radius 24, icon thùng rác 64 trên `error-container`, tiêu đề "Xóa việc “Đi bộ quanh công viên”?", câu nói rõ phạm vi ("Chỉ thay đổi lần này. Những ngày khác giữ nguyên." – lấy từ N13), Primary "Không xóa, giữ lại", khoảng trống 8 dp, Danger "Xóa khỏi lịch" | Nút an toàn là nút chính và nằm trên; xóa → `pop` về S03 với Snackbar "Đã xóa “Đi bộ” khỏi lịch mọi ngày." + "Hoàn tác" (xóa mềm, giữ 7 ngày) |
| Snackbar | 2 tầng (Material "longer action"): hàng icon 24 + câu `body-md` bold trắng trên nền `on-surface`, hàng dưới nút viền "Hoàn tác" cao 48 căn phải; đặt ngay trên bottom nav | `SnackBar(duration: Duration(days: 1), showCloseIcon: false, behavior: SnackBarBehavior.floating)` + đóng khi đổi màn; `Semantics(liveRegion: true)`; Tone Success (✓) / Info (đồng hồ) |
| S13d / S17b | Xem S13, S17 | |
| DLG-WakeTime / DLG-TaskTime | `showModalBottomSheet` hoặc `Dialog` rộng 336: tiêu đề "Giờ thức dậy" / "Giờ làm", gợi ý "Vuốt để chọn giờ", 3 cột `ListWheelScrollView` (giờ 1–12, phút 00–59, sáng/chiều) với hàng giữa cố định 96 × 48, 2 nút "Hủy" / "Xong" 142 × 60 | Mở đúng giá trị đã lưu; chạm vào một số cũng chọn được (không bắt buộc vuốt); Hủy → đóng, không đổi gì; Xong → ghi và đóng; `Semantics` mỗi cột: "Giờ, 8", "Phút, 00" |

## N01 – N21 · Màn MVP bổ sung

Các màn này dùng chung khung: AppBar Back "Quay lại" → `headline` + 1 câu mô tả → nội dung → Footer tối đa 1 Primary + 1 Secondary/Text.

| ID | Mục đích | Nội dung chính | Nút / điều hướng |
| --- | --- | --- | --- |
| N01 Thử lời nhắc | Kiểm tra máy có nhận lời nhắc | Thẻ "Lời nhắc thử · Đi bộ nhẹ nhàng / Ví dụ · 5 phút"; ghi chú quyền | Gửi thử (`flutter_local_notifications.show`) → N02; "Để sau" → S03 |
| N02 Đã nhận lời nhắc | Hỏi kết quả | "Ông/bà nhận được chưa?" + 3 điều kiểm tra (thông báo / chuông-rung / chữ dễ đọc) | "Tôi đã nhận được" → N04; "Chưa nhận được" → N03 |
| N03 Chưa nhận lời nhắc | Phục hồi | 3 bước: kiểm tra quyền, âm lượng / Không làm phiền, thử lại | "Thử lại" → N01; "Dùng lịch trước" → S03 (nhắc việc tắt) |
| N04 Chọn việc đầu tiên | Bắt đầu bằng 1 việc | 3 thẻ: Đi bộ nhẹ nhàng / Chăm cây / Gọi người thân + "Tự đặt tên việc" | Chọn → N05; "Để sau" → ST-Empty |
| N05 Xem lại việc đầu tiên | Kiểm tra trước khi lưu | Tên, giờ (DLG-TaskTime), ngày thực hiện, lặp lại | "Lưu việc" → N18; "Đổi ngày hoặc lặp lại" → N11 / N12 |
| N06 Sửa hồ sơ | Từ S10 | Như S02 + lưu ý "Đổi giờ thức dậy không tự đổi giờ những việc đã lưu." | "Lưu hồ sơ" / "Hủy" (đã sửa → N14) |
| N07 Nhắc việc | Từ S10 | 3 mục: quyền thông báo, chuông và rung, đọc nội dung | "Thử lời nhắc" → N01; mở cài đặt hệ thống (`openAppSettings`) |
| N08 Cách dùng đơn giản | Hướng dẫn 3 bước, cho người thân đọc cùng | Chọn việc · Nhắc nhẹ nhàng · Gần gũi người thân; "Người thân có thể gửi gợi ý lịch. Bác tự chọn nhận hoặc bỏ qua." | "Mở cài đặt" / "Thử lời nhắc" |
| N09 Sửa người thân | Từ S09 | Tên gọi, quan hệ, số điện thoại | "Lưu thay đổi"; "Xóa khỏi An Nhiên" → N15 |
| N10 Đã mở ứng dụng chia sẻ | Sau S17 | "Người nhận: Con gái Mai", "Chưa xác nhận đã gửi" | "Về Gia đình" / "Xem lại nội dung" |
| N11 Chọn ngày | Dùng chung | Lịch tháng 10/2026, T2 → CN; "Chọn ngày, rồi bấm Xong để xác nhận." | "Xong" → `pop(date)`; "Hủy" | 
| N12 Lặp lại | Dùng chung | Một lần / Mỗi ngày / chọn ngày trong tuần ("Đã chọn · Thứ Hai"…) | "Lưu các ngày đã chọn" (lỗi nếu không chọn ngày nào); "Hủy" |
| N13 Phạm vi thay đổi | Sửa / xóa việc lặp | "Thay đổi lần nào?" + "Lịch sử được giữ lại" | "Chỉ lần này" / "Lần này và các lần sau" / "Giữ nguyên" |
| N14 Chưa lưu thay đổi | Rời form | "Nếu rời khỏi đây, phần vừa chỉnh sẽ không được lưu." | Primary "Tiếp tục chỉnh"; "Bỏ thay đổi" (`PopScope.onPopInvoked`) |
| N15 Xóa người thân | Xác nhận | "Danh bạ điện thoại giữ nguyên · Lịch sử hoạt động không bị xóa" | Primary "Giữ lại"; Danger "Xóa khỏi An Nhiên" → N21 |
| N16 Đã lưu · nhắc cần kiểm tra | Lưu được, đặt nhắc lỗi | "Không cần nhập lại · Kiểm tra nhắc việc" | "Về Hôm nay"; link → N07 |
| N17 Hôm nay · đã xử lý hết | Cuối ngày (có việc bỏ qua) | "5 việc đã xong · 1 việc bỏ qua" | "Xem những việc đã làm" / "Xem lịch ngày mai" / "Về Hôm nay" |
| N18 / N19 | Sau khi lưu việc đầu tiên | Thẻ tóm tắt việc | N18: "Xem lịch" / "Thêm việc khác"; N19: "Sửa việc" / "Mở Lịch tuần" / "Về Hôm nay" |
| N20 Dữ liệu trên điện thoại | Minh bạch dữ liệu | Dùng được khi mất mạng · Chưa đồng bộ sang máy khác · Chia sẻ do ông/bà quyết định | "Về Cài đặt" |
| N21 Gia đình sau khi xóa | Kết quả N15 | Banner "Con gái Mai đã được xóa · Danh bạ điện thoại vẫn giữ nguyên." | "Thêm người thân" / "Về Hôm nay" |

## G01 – G12 · Gợi ý lịch từ người thân

| Mục | Đặc tả |
| --- | --- |
| Layout | AppBar Back "‹ Gia đình" → `headline` → thẻ lời nhắn của người gửi (trích dẫn) → danh sách việc gợi ý (tên + "Ngày mai · 08:00 sáng · 15 phút") → dòng trạng thái ("Chưa thêm vào lịch. Bác tự chọn việc và giờ phù hợp.") → Footer |
| Màn | G01 / G01b (máy người thân: soạn gợi ý, chọn giờ gợi ý 08:00 / 09:00, "Gửi gợi ý cho mẹ") → G02 ("Bà Lan sẽ tự chọn nhận, đổi giờ hoặc bỏ qua.") · G03 Lịch Mai gợi ý: Primary "Thêm 2 việc vào lịch", Secondary "Đổi giờ đi bộ", "Chọn từng việc", Text "Bỏ qua gợi ý" · G04 chọn giờ → G03b · G05 / G05b Đã thêm vào lịch → "Xem lịch ngày mai" → G08 / G08b · G06 "Bác muốn nhận việc nào?" → G07 / G07b → G08c / G08d · G09 Đã bỏ qua + "Hoàn tác" · G10 / G11 popup trên S03 ("Mai gửi lịch cho Bác · 2 việc cho ngày mai", "Xem gợi ý" / "Để sau") · G12 thẻ "Mai gửi Bác 2 việc · Xem gợi ý" ở đầu S03 |
| States | Mới (popup hiện **một lần**, biến `Đã hiện gợi ý này`); Để sau (thẻ G12); Đã nhận toàn bộ / một phần / đổi giờ; Đã bỏ qua |
| Data | `Suggestion { id, fromPersonId, message, items[{title, date, time, durationMin}], status: pending/accepted/partial/dismissed }`; nhận → tạo `Task` thật trên máy |
| UI constraints | Lịch chỉ đổi sau khi Bác bấm nhận; không tự gửi kết quả hay việc bỏ qua cho người thân ("Không tự gửi kết quả cho Mai."); popup không tự đóng, đóng bằng "Để sau" |

## C01 – C12 · Chế độ Người thân

| ID | Layout & nội dung | Hành vi |
| --- | --- | --- |
| C01 Chọn vai trò | Logo + "Ai đang dùng máy này?" + 2 thẻ chọn cao 130: "Tôi là người lớn tuổi – Tự xem và làm theo lịch của mình" / "Tôi là con, cháu – Lập lịch giúp bố mẹ, ông bà và theo dõi từ xa" → "Tiếp tục" | Lưu vai trò; người lớn tuổi → S01, con cháu → C02 |
| C02 / C02e Nhập mã ghép nối | "Nhập mã từ máy của mẹ · Mã gồm 6 số, tự đổi mới sau 10 phút." 6 ô 47 × 64 + hướng dẫn "Gia đình › Mã ghép nối" → "Ghép nối". Lỗi: 6 ô viền đỏ, banner "Mã chưa đúng hoặc đã hết hạn", "Thử lại" / "Gọi cho mẹ" | `keyboardType: number`, `autofillHints: oneTimeCode`; gọi API ghép nối; lỗi giữ nguyên các số đã nhập |
| C03 / C04 / C05 Lịch của mẹ | Header avatar "L" + "Lịch của mẹ Lan · Đã ghép nối · 2 phút trước" → `SegmentedButton` Ngày / Tuần / Tháng → điều hướng ‹ ngày/tuần/tháng › → Ngày: danh sách giờ + tên; Tuần: 7 hàng "T5 15/10 · 4 việc · xong 2"; Tháng: lưới 7 cột 45 × 50 + tóm tắt ngày đang chọn → Footer "Tạo lịch cho mẹ" | Chạm ngày ở Tuần/Tháng → C03 của ngày đó; chạm việc → C10 |
| C06 / C06e Thông tin việc (1/3) | Chip thói quen (Vận động / Thư giãn / Ăn uống / Gia đình), TextField "Tên việc" ("Mẹ sẽ thấy đúng tên này"), ô giờ, "Làm trong 15 phút" | "Tiếp tục" validate: thiếu tên → "Hãy nhập tên việc để mẹ biết cần làm gì"; thiếu giờ → "Chọn giờ để nhắc mẹ đúng lúc" |
| C07 / C07m Lặp lại (2/3) | Một lần / Mỗi ngày / Mỗi tuần / Mỗi tháng; tuần: chip T2…CN; tháng: lưới 1–31 + "Cuối tháng"; Bắt đầu, Kết thúc / Thời gian; câu tóm tắt bằng chữ ("Mẹ được nhắc đi bộ lúc 8:00 sáng vào Thứ Hai, Thứ Tư, Thứ Sáu hằng tuần.") | Lưu dạng RRULE (RFC 5545); "Xem lại" → C08 |
| C08 Xem lại & gửi (3/3) | Thẻ tóm tắt, "Lời nhắn cho mẹ" (không bắt buộc), Switch "Mẹ nhận trước khi thêm" (bật sẵn) → "Gửi lịch cho mẹ" | Kiểm tra trùng giờ → C08w (`AlertDialog`: "Đổi giờ khác" / "Vẫn gửi") → C09 |
| C09 Đã gửi | "Đã gửi cho mẹ · Lịch sẽ hiện trên máy mẹ sau khi mẹ chọn Nhận." + trạng thái "Đang chờ mẹ nhận · Gửi lúc 16:20 · mẹ chưa xem" | "Về lịch của mẹ" / "Tạo thêm việc"; máy mẹ hiện G11 |
| C10 Chi tiết việc (lặp lại) | Tên + chip thói quen, giờ · lặp · thời gian, "Mai tạo · mẹ đã nhận 16/10", "6 lần gần nhất" ✓/✕ + câu "Mẹ đã đi bộ 4 / 5 lần, bỏ qua 1 lần vì trời mưa." | "Sửa việc" → C06 điền sẵn → C11; "Ngưng lặp lại" → C12 |
| C11 Áp dụng thay đổi cho | Dialog: "Đổi giờ đi bộ từ 8:00 sang 7:30 sáng." + "Chỉ lần này · 19/10" / "Từ lần này về sau" / "Tất cả các lần" / "Hủy" | Cập nhật RRULE (tách chuỗi khi "từ lần này về sau") |
| C12 Ngưng lịch lặp | Dialog: "Mẹ sẽ không còn được nhắc vào T2, T4, T6. Những lần mẹ đã làm vẫn được giữ lại." Primary "Giữ lại", Danger "Ngưng lặp lại" | Đặt `until = hôm nay`; về C03 với Snackbar "Hoàn tác" |

Ràng buộc chung chế độ Người thân: dùng cùng design system nhưng có thể dùng cỡ chữ "Vừa"; mọi thay đổi trên lịch của mẹ đi qua cơ chế gợi ý/nhận (G) – không ghi thẳng vào máy mẹ khi switch "Mẹ nhận trước khi thêm" bật; không có màn theo dõi vị trí hay sức khỏe.

---

## Bảng 1 – Token → Flutter

| Token Figma | Giá trị | Flutter |
| --- | --- | --- |
| `color/primary` | `#1F684B` | `ColorScheme.primary` |
| `color/on-surface` | `#202B25` | `ColorScheme.onSurface` |
| `color/on-surface-variant` | `#526057` | `ColorScheme.onSurfaceVariant` |
| `color/bg` | `#F6F7F2` | `ThemeData.scaffoldBackgroundColor`, `ColorScheme.surface` |
| `color/surface` | `#FFFFFF` | `ColorScheme.surfaceContainerLowest` |
| `color/primary-container` | `#D6EADF` | `ColorScheme.primaryContainer` |
| `color/on-primary-container` | `#174C37` | `ColorScheme.onPrimaryContainer` |
| `color/secondary` | `#1F684B` (= primary) | `ColorScheme.secondary` |
| `color/error` | `#B42318` | `ColorScheme.error` |
| `color/error-container` | `#FDECE9` | `ColorScheme.errorContainer` |
| `color/warning-container` | `#FFF3DB` | `AppColors.warningContainer` (ThemeExtension) |
| `color/success` | `#1F684B` | `AppColors.success` (ThemeExtension) |
| `color/outline` | `#7B887F` | `ColorScheme.outline` |
| `display` 34/42 Bold | | `TextTheme.displaySmall` (fontSize 34, height 42/34) |
| `headline` 30/140 % Bold | | `TextTheme.headlineMedium` (30, height 1.4) |
| `title-md` 26/140 % Bold | | `TextTheme.titleLarge` (26, height 1.4) |
| `title-lg` 24/32 Bold | | `TextTheme.titleMedium` (24, height 1.33) |
| `numeric-lg` 30/38 Bold | | `AppText.numericLg` (ThemeExtension) – số giờ, mã ghép nối |
| `label-btn` 22/140 % Bold | | `TextTheme.labelLarge` (22, height 1.4) – chữ trên nút |
| `body-lg` 24/140 % | | `TextTheme.bodyLarge` (24, height 1.4); `body-lg-strong` 26 SemiBold |
| `body-md` / `caption` 20/140 % | | `TextTheme.bodyMedium` / `bodySmall` (20, height 1.4) |
| `label-nav` 20/140 % SemiBold (Bold khi chọn) | | `NavigationBarThemeData.labelTextStyle` – cần `maxLines: 1` để 4 tab cùng chiều cao |
| `space/4…48` | 4, 8, 12, 16, 20, 24, 32, 48 | `abstract final class AppSpace { static const s4 = 4.0; … s48 = 48.0; }` |
| `radius/sm, md, button, lg, xl` | 8, 12, 14, 16, 24 | `AppRadius.sm …` → `BorderRadius.circular(x)` |
| `radius/full` | 999 | `StadiumBorder()` |
| `elevation/1` | Y2 Blur6 10 % | `BoxShadow(offset: Offset(0, 2), blurRadius: 6, color: Color(0x1A202B25))` |
| `elevation/2` | Y8 Blur24 24 % | `DialogThemeData(elevation: 6, shadowColor: Colors.black38)` |
| Font Be Vietnam Pro | | `GoogleFonts.beVietnamProTextTheme(base)` |

## Bảng 2 – Component → Widget

| Component Figma | Variant | Widget Flutter |
| --- | --- | --- |
| `Button` | Primary | `FilledButton(style: FilledButton.styleFrom(minimumSize: Size.fromHeight(60), shape: RoundedRectangleBorder(borderRadius: AppRadius.button)))` |
| `Button` | Secondary | `OutlinedButton` (side 2 dp `primary`) |
| `Button` | Tonal ("Thêm việc") | `FilledButton.tonal` nền `primary-container`, chữ `on-primary-container`, `StadiumBorder`, cao 48 |
| `Button` | Text | `TextButton` gạch chân |
| `Button` | Disabled | `onPressed: null` |
| `TextField` | Default / Focused / Error | `TextField` + `InputDecoration(labelText ở ngoài qua Column, helperText, errorText)`, `OutlineInputBorder(radius 12)` |
| `TaskCard` | Next | `Card(color: primaryContainer-lighter, shape: side 2 primary)` + `Column` |
| `TaskRow` | Upcoming / Done / Skipped | `ListTile(minTileHeight: 64, leading: CircleAvatar 44)`; Skipped: icon ✕ trên `disabled-bg`, chữ `onSurfaceVariant`, không gạch ngang chữ; `enabled: false` khi là ngày đã qua |
| `NavItem` / `BottomNav` | Active / Inactive | `NavigationBar(height: 84, labelBehavior: NavigationDestinationLabelBehavior.alwaysShow)` + `NavigationDestination` |
| `AppBar` | Back / Back+Step / Greeting | `AppBar(leading: TextButton.icon(icon: arrow_back, label: Text('Quay lại')), leadingWidth: 140, actions: [Text('Bước 1 / 2')])` |
| `AppBar` | Back+Action | như trên, `actions: [OutlinedButton.icon(icon: Icon(Icons.edit_outlined), label: Text('Sửa'), style: minimumSize Size(48, 48), StadiumBorder)]` |
| `Button` | Danger / Danger-outline | `FilledButton` nền `error` / `OutlinedButton` viền 2 dp `error`, chữ `error`; cao 60 |
| `Snackbar` | Success / Info | `SnackBar` floating, nội dung `Column(Row(icon, Text), Align(right, OutlinedButton.icon(undo, 'Hoàn tác')))`, nền `colorScheme.onSurface` |
| `Dialog` | Confirm | `AlertDialog` + `actions` là `Column` 2 nút full-width; mở bằng `showDialog` |
| `Loading` | Full-screen / Inline | `CircularProgressIndicator(strokeWidth: 6)` + `Text`, bọc `Semantics(liveRegion: true)` |
| `EmptyState` | — | Widget tự viết `EmptyState({icon, title, message, primaryAction, secondaryAction})` |
| `ErrorView` | Inline / Banner / Full-screen | `InputDecoration.errorText` / `MaterialBanner` / widget `ErrorView({message, onRetry, onSaveLocal, onEdit})` |
| `TimeStepper` | — (chỉ còn trong thư viện) | Màn cuối dùng `TimeField` (`OutlinedButton` 320 × 62: icon đồng hồ + `numeric-lg` + ⌄) mở `DLG-TaskTime` / `DLG-WakeTime` = 3 `ListWheelScrollView` (itemExtent 48, `FixedExtentScrollPhysics`) + Hủy / Xong |
| `HabitTile` | Selected | `Material` + `InkWell` hoặc `ChoiceChip` tùy biến, viền 3 dp khi chọn, `Semantics(selected: true)` |
| `Switch` | On / Off | `SwitchListTile(minTileHeight: 68)` |

## Hạn chế & việc tiếp theo

- Chưa test với người dùng thật ngoài gia đình; số liệu thành công trong persona.md cần đo lại.
- Chưa thiết kế dark mode (chế độ tương phản cao ở S10 là ưu tiên hơn).
- "Đọc to nội dung" phụ thuộc engine TTS tiếng Việt có trên máy.
- Chế độ Người thân (C02 ghép nối, C09 chờ mẹ nhận) và gợi ý lịch (G) cần backend + push notification, ngoài phạm vi Lab 2. Nhắn tin (S17) không cần backend: dùng `share_plus` mở Zalo/SMS, S17b/N10 ghi "chưa xác nhận đã gửi".
- Lịch tháng 10/2026 trong Figma là dữ liệu mẫu: app cần lịch đầy đủ, kiểm tra thời điểm quá khứ và múi giờ.
- Form và thông báo trong prototype là mô phỏng (biến Figma): cần nghiệm thu nhập liệu thật, lưu bền vững, quyền hệ điều hành, bàn phím và chữ hệ thống 200 % trên thiết bị.
- S14 phụ thuộc quyền thông báo toàn màn hình; một số máy (Xiaomi, Oppo) còn chặn chạy nền, cần hướng dẫn riêng ở S13d.
- Prototype chỉ có trang Sửa cho việc "Đi bộ"; bản Flutter dùng chung S15 cho mọi việc chưa làm.
- Bottom nav: nhãn "Lịch tuần" / "Thói quen" ở cỡ 20 xuống 2 dòng trong Figma (xem accessibility.md mục 7) – bản Flutter đặt `maxLines: 1` hoặc rút nhãn.
