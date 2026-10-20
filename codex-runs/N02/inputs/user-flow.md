# Information Architecture & User Flows

## 1. Information architecture

App có **hai chế độ**, chọn ở màn đầu tiên (C01 "Ai đang dùng máy này?"):

- **Người lớn tuổi** (bà Lan): 4 tab cấp cao, mỗi tab sâu tối đa 2 cấp con, để không bị lạc. Màn Cài đặt mở từ nút có chữ trên app bar, không chiếm một tab riêng.
- **Người thân** (chị Mai): ghép nối với máy của mẹ bằng mã 6 số, xem và lập lịch cho mẹ (C02 – C12). Lịch chỉ vào máy mẹ khi mẹ chọn Nhận.

```mermaid
flowchart TD
    C01{{"C01 Chọn vai trò"}} -- "Tôi là người lớn tuổi" --> S01
    C01 -- "Tôi là con, cháu" --> C02["C02 Nhập mã ghép nối"] --> C03["C03–C05 Lịch của mẹ<br/>Ngày / Tuần / Tháng"]
    C03 --> C06["C06–C08 Tạo lịch 3 bước"] --> C09["C09 Chờ mẹ nhận"]
    C03 --> C10["C10 Chi tiết việc lặp"]
    S01["S01 Chào mừng<br/>(chọn cỡ chữ)"] --> S02["S02 Thiết lập hồ sơ<br/>Bước 1/2"]
    S02 --> S13["S13 Cho phép nhắc việc<br/>Bước 2/2"]
    S13 -.-> S13D["ST Nhắc việc đang tắt"]
    S13 --> NAV{{"Bottom navigation – 4 tab có nhãn"}}
    NAV --> S03["S03 Hôm nay"]
    NAV --> S07["S07 Lịch tuần"]
    NAV --> S08["S08 9 thói quen"]
    NAV --> S09["S09 Gia đình"]
    S03 --> S04["S04 Chi tiết hoạt động"]
    S04 -.-> DLG["DLG Xác nhận đã xong<br/>(overlay)"]
    S03 -.-> DLG
    S03 --> S05["S05 Thêm việc – chọn thói quen"]
    S05 --> S06["S06 Thêm việc – chọn giờ"]
    S06 --> LOAD["ST Loading"]
    LOAD --> SAVED["ST Đã lưu"]
    LOAD --> ERR["ST Lưu thất bại"]
    S06 --> VAL["ST Validation"]
    S03 --> S10["S10 Cài đặt hiển thị"]
    S07 -- "chạm hôm nay" --> S03
    S07 -- "chạm ngày khác" --> S11["S11 Chi tiết ngày"]
    S11 --> S04
    S11 --> S05
    S03 -- "Xem cả ngày" --> S11
    S09 --> S12["S12 Thêm người thân"]
    S03 -.-> LATER["DLG Dời việc<br/>(overlay)"]
    S03 -. "không có việc" .-> EMPTY["ST Home trống"]
    S04 --> S15["S15 Sửa việc"]
    S15 -.-> DEL["DLG Xác nhận xóa<br/>(overlay)"]
    S04 -.-> SKIP["DLG Bỏ qua hôm nay<br/>(overlay)"]
    S08 --> S16["S16 Chi tiết thói quen"]
    S09 --> S17["S17 Nhắn tin cho người thân"]
    S17 --> SENT["ST Đã gửi"]
    NOTI(["Thông báo của hệ thống<br/>(đến giờ)"]) --> S14["S14 Lời nhắc đến giờ<br/>(toàn màn hình)"]
    S10 -. "Xem thử lời nhắc" .-> S14
    S14 --> S04
    S13 -. "Thử lời nhắc" .-> N01["N01–N05 Thử lời nhắc,<br/>chọn việc đầu tiên"]
    S10 --> N06["N06 Sửa hồ sơ · N07 Nhắc việc<br/>N08 Cách dùng · N20 Dữ liệu"]
    S09 --> N09["N09 Sửa người thân → N15 Xóa"]
    C09 -. "gợi ý đến máy mẹ" .-> G11["G11 Popup gợi ý trên S03"]
    S09 --> G03["G03 Lịch Mai gợi ý<br/>nhận / đổi giờ / chọn / bỏ qua"]
    G11 --> G03
```

| Cấp | Màn hình |
| --- | --- |
| Onboarding (chỉ lần đầu) | S01, S02 (Bước 1/2), S13 Cho phép nhắc việc (Bước 2/2) |
| Ngoài app (hệ thống gọi) | S14 Lời nhắc đến giờ – hiện toàn màn hình khi tới giờ, kể cả lúc khóa máy; xem thử được từ S10 |
| Cấp 1 – tab | S03 Hôm nay · S07 Lịch tuần · S08 9 thói quen · S09 Gia đình |
| Cấp 2 | S04 Chi tiết hoạt động · S05 Thêm việc bước 1 · S10 Cài đặt · S11 Chi tiết ngày (con của S07, hoặc "Xem cả ngày" từ S03) · S12 Thêm người thân (con của S09) · S16 Chi tiết thói quen (con của S08) · S17 Nhắn tin cho người thân (con của S09, hoặc từ thẻ "xong 6/6" ở S03) |
| Cấp 3 | S06 Thêm việc bước 2 · S15 Sửa việc (con của S04) · N06 / N07 / N08 / N20 (con của S10) · N09 Sửa người thân (con của S09) |
| Gợi ý từ người thân | G03 – G09 mở từ hàng "Gợi ý từ Mai · 2 việc" ở S09 hoặc popup G11 / thẻ G12 ở S03 |
| Chế độ Người thân | C01 → C02 / C02e → C03 · C04 · C05 (3 tab Ngày / Tuần / Tháng) → C06 / C06e → C07 / C07m → C08 (+ C08w) → C09; C03 → C10 → C06 (sửa) → C11 → C03; C10 → C12 → C03 |
| State / overlay | ST-Empty, S13d (nhắc việc đang tắt), ST-Validation, ST-Loading, ST-Error, ST-Saved, S03 + snackbar "Hoàn tác" (đã dời / đã bỏ qua / đã xóa / đã sửa / nhắc lại sau), S03 xong 6/6, S11b (ngày đã qua), S12e (thiếu số điện thoại), S09b (đã thêm người thân), S17b (đã gửi), DLG-Done, DLG-Later, DLG-Skip, DLG-Delete |

S04 mở được từ hai nơi (S03 và S11) nên nút Back ghi "Quay lại" thay vì tên màn trước.

## 2. Flow 1 – Lần đầu mở app (Onboarding)

**Mục tiêu:** bà Lan cài xong và thấy lịch hôm nay trong dưới 2 phút.

```mermaid
flowchart LR
    A(["Mở app lần đầu"]) --> S01["S01 Chọn cỡ chữ<br/>Vừa / Lớn / Rất lớn"]
    S01 -- "Bắt đầu" --> S02["S02 Nhập tên,<br/>giờ thức dậy"]
    S02 -- "Tiếp tục" --> C{"Tên đã nhập?"}
    C -- "chưa" --> E1["Báo lỗi dưới ô Tên<br/>+ ví dụ"] --> S02
    C -- "rồi" --> S13["S13 Cho phép nhắc việc<br/>Bước 2/2"]
    S13 -- "Bật nhắc việc<br/>(Android hỏi → Cho phép)" --> D{"Đã có việc nào?"}
    S13 -- "Để sau" --> OFF["S13d Nhắc việc đang tắt<br/>nói rõ hậu quả + cách bật lại"]
    OFF -- "Bật nhắc việc / Vẫn để sau" --> D
    D -- "có" --> S03(["S03 Hôm nay"])
    D -- "chưa" --> EMPTY["ST Home trống"]
    EMPTY -- "Dùng lịch mẫu hoạt động hằng ngày" --> S03
    EMPTY -- "Thêm việc đầu tiên" --> S05["S05 → Flow 2"]
    S02 -- "Quay lại" --> S01
```

| Loại nhánh | Mô tả |
| --- | --- |
| Happy path | S01 → S02 → S13 "Bật nhắc việc" → ST-Empty (người mới chưa có việc) → "Dùng lịch mẫu hoạt động hằng ngày" → S03 |
| Alternate | ST-Empty → "Thêm việc đầu tiên" → Flow 2; người đã có lịch (cài lại app) → thẳng S03 |
| Error / recovery | Bỏ trống tên → báo lỗi ngay dưới ô (icon + chữ + ví dụ) → nhập lại; S13 chọn "Để sau" hoặc bấm "Từ chối" ở hộp thoại Android → S13d nói rõ "đến giờ sẽ không đổ chuông" và chỉ đường bật lại, không chặn bà dùng app |

## 3. Flow 2 – Thêm việc mới (có lỗi và phục hồi)

**Mục tiêu:** thêm "Tập thở chậm 10 phút, 8:00 sáng mỗi ngày" trong ≤ 60 giây.

```mermaid
flowchart LR
    S03(["S03 Hôm nay"]) -- "Thêm việc" --> S05["S05 Bác muốn làm gì?<br/>3 việc quen + Xem thêm"]
    S05 -- "chạm một việc" --> S06["S06 Tên việc, giờ (DLG-TaskTime),<br/>ngày, lặp lại, nhắc nhở"]
    S06 -- "Lưu việc này" --> V{"Đủ tên việc?"}
    V -- "không" --> VAL["ST Validation<br/>lỗi + chip gợi ý"]
    VAL -- "chọn gợi ý / sửa" --> S06
    V -- "có" --> LOAD["ST Đang lưu…"]
    LOAD -- "lưu được" --> SAVED["ST Đã lưu"]
    LOAD -- "lỗi lưu" --> ERR["ST Lưu thất bại"]
    ERR -- "Thử lại" --> LOAD
    ERR -- "Kiểm tra lại lịch" --> S03
    ERR -- "Quay lại sửa" --> S06
    SAVED -- "Về trang Hôm nay" --> S03
    SAVED -- "Thêm việc khác" --> S05
    S05 -- "Hủy" --> S03
    S06 -- "Quay lại" --> S05
```

| Loại nhánh | Mô tả |
| --- | --- |
| Happy path | S03 → S05 → S06 → Loading → Đã lưu → S03 |
| Alternate | Đã lưu → "Thêm việc khác" → S05; S05 → "Hủy" → S03 |
| Error / recovery 1 | Thiếu tên việc → ST-Validation → chọn chip gợi ý → S06 |
| Error / recovery 2 | Lưu thất bại (demo S06o) → ST-Error "Chưa thể lưu trên điện thoại. Nội dung đang nhập vẫn được giữ lại." → Thử lại / Kiểm tra lại lịch / Quay lại sửa; lưu được việc nhưng chưa đặt được lời nhắc → N16 "Việc đã được lưu · Kiểm tra nhắc việc" |
| Thoát giữa chừng | Bấm Quay lại khi đã nhập → N14 "Chưa lưu thay đổi": "Tiếp tục chỉnh" (nút chính) / "Bỏ thay đổi" |

> Từ 15/10, S05 không còn là lưới 9 thói quen mà là "Bác muốn làm gì?" với 3 việc quen thuộc (Đi bộ nhẹ nhàng, Chăm cây, Gọi người thân) + "Xem thêm hoạt động"; giờ chọn bằng ô giờ mở `DLG-TaskTime`, ngày bằng N11, lặp lại bằng N12.

## 4. Flow 3 – Hoàn thành, dời hoặc bỏ qua một việc

**Mục tiêu:** đánh dấu "Đi bộ quanh công viên" đã xong trong ≤ 2 lần chạm.

```mermaid
flowchart LR
    S03(["S03 Hôm nay<br/>thẻ Việc tiếp theo"]) -- "Đã xong" --> DLG["DLG Bà đã đi bộ<br/>xong rồi chứ?"]
    DLG -- "Đúng, đã xong" --> R(["S03 tiến độ 3/6 → 4/6<br/>con gái nhận tin"])
    DLG -- "Chưa, để sau" --> S03
    S03 -- "chạm tên việc" --> S04["S04 Chi tiết hoạt động"]
    S04 -- "Tôi đã làm xong" --> DLG
    S04 -- "Dời 30 phút" --> SNACK(["S03 + snackbar<br/>“Đã dời… · Hoàn tác”"])
    S04 -- "Bỏ qua hôm nay" --> SKIP["DLG Bỏ qua đi bộ hôm nay?<br/>chọn lý do (không bắt buộc)"]
    SKIP -- "Trời mưa / Mệt / Bận / Khác" --> SNACK
    SKIP -- "Không bỏ qua nữa" --> S04
    S04 -- "Quay lại" --> S03
    S03 -- "Dời lại" --> LATER["DLG Dời việc này<br/>đến lúc nào?"]
    LATER -- "30 phút nữa / Chiều nay / Ngày mai" --> SNACK
    LATER -- "Không dời nữa" --> S03
    SNACK -- "Hoàn tác" --> S03
```

| Loại nhánh | Mô tả |
| --- | --- |
| Happy path | S03 → "Đã xong" → DLG → "Đúng, đã xong" → S03 cập nhật |
| Alternate | S03 → S04 → "Dời 30 phút" hoặc "Bỏ qua hôm nay" (DLG-Skip, chọn lý do); S03 → "Dời lại" → DLG-Later chọn một trong 3 mốc giờ có sẵn. Mọi kết quả quay về S03 với snackbar nói rõ đã đổi gì |
| Error prevention / recovery | Dialog xác nhận chặn việc bấm nhầm; "Chưa, để sau" / "Không bỏ qua nữa" đưa về như cũ, không đổi dữ liệu; snackbar không tự tắt và có nút "Hoàn tác" cao 48 dp. Cuối ngày xong cả 6 việc → S03 hiện thẻ chúc mừng thay thẻ Việc tiếp theo (Flow 9) |

## 5. Flow 4 – Xem trước lịch một ngày trong tuần

**Mục tiêu:** từ Lịch tuần, bà Lan biết ngày Thứ Sáu có việc gì, mấy giờ, và xem được cách làm một việc trong ≤ 2 lần chạm.

```mermaid
flowchart LR
    S07(["S07 Lịch tuần"]) -- "chạm một ngày" --> D{"Ngày nào?"}
    D -- "hôm nay" --> S03(["S03 Hôm nay"])
    D -- "sắp tới" --> S11["S11 Chi tiết ngày<br/>việc chia theo buổi"]
    D -- "đã qua" --> S11B["S11b Ngày đã qua<br/>chỉ xem lại"]
    S11 -- "chạm một việc" --> S04["S04 Chi tiết hoạt động"]
    S11 -- "Thêm việc cho ngày này" --> S05["S05 → Flow 2"]
    S04 -- "Quay lại" --> S11
    S11 -- "Quay lại" --> S07
    S11B -- "Quay lại" --> S07
```

| Loại nhánh | Mô tả |
| --- | --- |
| Happy path | S07 → chạm "Thứ Sáu 9/10" → S11 → chạm "Đi bộ quanh công viên" → S04 → Quay lại |
| Alternate | Chạm hàng "Hôm nay" → S03; ngày sắp tới → "Thêm việc cho ngày này" → Flow 2 |
| Error prevention | Ngày đã qua (S11b) chỉ cho xem, không có nút sửa hay đánh dấu xong, nên không thể vô tình đổi dữ liệu cũ; việc bị bỏ qua ghi bằng chữ "Bỏ qua · 9:30 sáng (trời mưa)" chứ không chỉ đổi màu |

## 6. Flow 5 – Thêm người thân (có lỗi và phục hồi)

**Mục tiêu:** bà Lan tự thêm số của cháu Bin để gọi bằng một lần chạm và để cháu nhận tin khi bà xong việc, trong ≤ 60 giây, không phải gõ số nếu số đã có trong danh bạ.

```mermaid
flowchart LR
    S09(["S09 Gia đình"]) -- "Thêm người thân" --> S12["S12 Tên gọi, quan hệ,<br/>số điện thoại"]
    S12 -- "Lưu người thân" --> D{"Có số điện thoại?"}
    D -- "có" --> OK(["S09b Đã thêm Cháu Bin<br/>thẻ mới + báo thành công"])
    D -- "chưa" --> E["S12e Báo lỗi dưới ô số<br/>+ gợi ý chọn từ danh bạ"]
    E -- "Chọn từ danh bạ / gõ số" --> S12
    S12 -- "Chọn từ danh bạ điện thoại" --> S12
    S12 -- "Quay lại" --> S09
```

| Loại nhánh | Mô tả |
| --- | --- |
| Happy path | S09 → "Thêm người thân" → "Chọn từ danh bạ điện thoại" → "Lưu người thân" → S09b |
| Alternate | Tự gõ tên và số thay vì chọn từ danh bạ |
| Error / recovery | Bấm Lưu khi chưa có số → S12e: viền đỏ, icon, câu "Bà chưa nhập số điện thoại", gợi ý dùng danh bạ; tên và quan hệ đã nhập vẫn giữ nguyên |

## 7. Flow 6 – Lời nhắc đến giờ

**Mục tiêu:** tới 9:20 điện thoại đổ chuông, bà Lan biết ngay việc gì, mấy giờ, và chọn được cách xử lý trong 1 lần chạm, không cần vuốt.

```mermaid
flowchart LR
    N(["9:20 · Android hiện<br/>thông báo toàn màn hình"]) --> S14["S14 Lời nhắc<br/>“Còn 10 phút nữa”<br/>đang đọc to"]
    S14 -- "Bắt đầu làm" --> S04["S04 Chi tiết – cách làm 1-2-3"]
    S04 -- "Tôi đã làm xong" --> DONE(["DLG Xác nhận → S03 4/6"])
    S14 -- "Nhắc lại sau 10 phút" --> SNZ(["S03 + snackbar<br/>“Sẽ nhắc lại lúc 9:30”"])
    S14 -- "Hôm nay bỏ qua" --> SKIP["DLG Bỏ qua (lý do)"]
    SKIP --> SK(["S03 + snackbar<br/>“Đã bỏ qua · Hoàn tác”"])
    S10["S10 Cài đặt"] -. "Xem thử lời nhắc" .-> S14
```

| Loại nhánh | Mô tả |
| --- | --- |
| Happy path | Thông báo → S14 → "Bắt đầu làm" → S04 → "Tôi đã làm xong" → DLG-Done |
| Alternate | "Nhắc lại sau 10 phút" → nhắc lại đúng giờ hẹn; "Hôm nay bỏ qua" → DLG-Skip; xem thử từ S10 để bà quen trước khi nhận thật |
| Error prevention | Không có cử chỉ vuốt để tắt (vuốt nhầm là mất lời nhắc); 3 nút xếp dọc cao 60 dp, cách nhau 10 dp; bỏ qua phải xác nhận; lời nhắc vừa đọc to vừa hiện chữ vừa rung |

## 8. Flow 7 – Sửa và xóa một việc

**Mục tiêu:** đổi giờ đi bộ từ 9:30 sang 10:00 trong ≤ 4 lần chạm; xóa nhầm thì lấy lại được.

```mermaid
flowchart LR
    S04(["S04 Chi tiết Đi bộ"]) -- "Sửa (góc phải app bar)" --> S15["S15 Sửa việc<br/>tên · giờ · lặp lại · nhắc"]
    S15 -- "Lưu thay đổi" --> SAVED(["S03 + snackbar<br/>“Đã lưu: 10:00 sáng”"])
    S15 -- "Xóa việc này" --> DEL{"DLG Xóa việc?<br/>nói rõ: mất ở mọi ngày"}
    DEL -- "Không xóa, giữ lại<br/>(nút chính)" --> S15
    DEL -- "Xóa khỏi lịch" --> GONE(["S03 + snackbar<br/>“Đã xóa · Hoàn tác”"])
    GONE -- "Hoàn tác" --> S03(["S03 như cũ"])
    S15 -- "Quay lại" --> S04
```

| Loại nhánh | Mô tả |
| --- | --- |
| Happy path | S04 → "Sửa" → S15 → chạm ô giờ → DLG-TaskTime chọn 10 : 00 sáng → "Xong" → "Lưu thay đổi" → N13 "Chỉ lần này" → S03 |
| Alternate | S15 → "Xóa việc này" → DLG-Delete (ghi rõ phạm vi) → "Xóa khỏi lịch" → S03 còn 3/5 việc; với việc lặp lại, N13 cho chọn "Chỉ lần này" / "Lần này và các lần sau" / "Giữ nguyên", ngày đã làm hoặc đã bỏ qua không bị đổi |
| Error prevention / recovery | Nút xóa viền đỏ đặt cuối nội dung, xa nút Lưu; dialog nói rõ hậu quả và nút an toàn "Không xóa, giữ lại" là nút chính; sau khi xóa vẫn có "Hoàn tác"; dòng "Đã đổi từ 9:30 sáng" cho bà thấy mình vừa sửa gì |

## 9. Flow 8 – Tìm hiểu một thói quen

**Mục tiêu:** bà Lan hiểu "Ăn vừa đủ" là gì, tuần này mình đã làm được mấy lần, và thêm một việc cho thói quen đó.

```mermaid
flowchart LR
    S08(["S08 9 thói quen"]) -- "chạm một hàng ›" --> S16["S16 Chi tiết thói quen<br/>tuần này ✓ ✕ ○ · học từ đâu<br/>việc của bà · gợi ý"]
    S16 -- "Thêm việc cho thói quen này<br/>/ chạm chip gợi ý" --> ADD["S05 / S06 → Flow 2"]
    S16 -- "chạm một việc của bà" --> S04["S04 Chi tiết việc"]
    S16 -- "Quay lại" --> S08
```

| Loại nhánh | Mô tả |
| --- | --- |
| Happy path | S08 → chạm "3. Thư giãn mỗi ngày" → S16 → "Thêm việc cho thói quen này" → S06 (đã chọn sẵn thói quen) → Flow 2 |
| Alternate | Chạm một việc trong "Việc của bà" → S04 của lần làm gần nhất sắp tới |
| Empty state | Thói quen chưa có việc nào (vd "9. Bạn bè tích cực") → hộp "Bà chưa có việc nào cho thói quen này. Thử một gợi ý bên dưới nhé." + 3 chip gợi ý |

## 10. Flow 9 – Nhắn tin cho con cháu

**Mục tiêu:** bà Lan gửi cho Mai tin "hôm nay mẹ đã làm gì" trong 2 lần chạm, không phải gõ chữ.

```mermaid
flowchart LR
    ALL(["S03 xong 6/6<br/>thẻ chúc mừng"]) -- "Báo tin vui cho Mai" --> S17["S17 Xem trước tin nhắn<br/>chọn thêm câu · Zalo / SMS"]
    S09(["S09 Gia đình"]) -- "Nhắn tin" --> S17
    S17 -- "Tiếp tục gửi cho Mai" --> SENT(["S17b Mở Zalo / SMS<br/>chưa xác nhận đã gửi"])
    SENT -- "Về trang Gia đình" --> S09
    S17 -- "Quay lại" --> S09
```

| Loại nhánh | Mô tả |
| --- | --- |
| Happy path | S03 xong 6/6 → "Báo tin vui cho Mai" → S17 (chọn điều muốn kể) → "Tiếp tục gửi cho Mai" → S17b |
| Alternate | Từ S09 bấm "Nhắn tin" ở thẻ của Mai, Hùng hoặc Bin (mỗi người một bản, xưng hô đúng: "Mẹ – con", "Bà – cháu") |
| Trung thực về kết quả | An Nhiên chỉ mở Zalo / SMS với nội dung soạn sẵn; S17b và N10 ghi "An Nhiên chưa xác nhận tin đã gửi" thay vì báo "Đã gửi" |

## 11. Flow 10 – Người thân ghép nối với máy của mẹ (chế độ Người thân)

**Mục tiêu:** chị Mai ở TP.HCM ghép nối điện thoại của mình với máy của mẹ trong ≤ 1 phút, qua điện thoại, không cần cầm máy mẹ.

```mermaid
flowchart LR
    C01(["C01 Chọn vai trò"]) -- "Tôi là con, cháu" --> C02["C02 Nhập mã ghép nối<br/>6 số, đổi sau 10 phút"]
    C01 -- "Tôi là người lớn tuổi" --> S01(["S01 Chọn cỡ chữ (Flow 1)"])
    C02 -- "Ghép nối" --> D{"Mã đúng?"}
    D -- "đúng" --> C03(["C03 Lịch của mẹ"])
    D -- "sai / hết hạn" --> E["C02e Mã chưa đúng hoặc đã hết hạn"]
    E -- "nhập lại / Thử lại" --> C02
    E -- "Gọi cho mẹ" --> CALL(["Gọi điện nhờ mẹ mở lại mã"])
```

| Loại nhánh | Mô tả |
| --- | --- |
| Happy path | C01 → "Tôi là con, cháu" → C02 (mẹ đọc 6 số qua điện thoại: máy mẹ › Gia đình › Mã ghép nối) → "Ghép nối" → C03 |
| Alternate | C01 → "Tôi là người lớn tuổi" → Flow 1 |
| Error / recovery | Mã sai hoặc quá 10 phút → C02e: 6 ô viền đỏ, banner giải thích, hướng dẫn lấy mã mới, nút "Thử lại" và "Gọi cho mẹ" |

## 12. Flow 11 – Người thân lập lịch cho mẹ theo ngày / tuần / tháng

**Mục tiêu:** chị Mai đặt "Đi bộ nhẹ nhàng 8:00 sáng, T2-T4-T6 hằng tuần" cho mẹ trong ≤ 90 giây; mẹ chỉ cần bấm Nhận.

```mermaid
flowchart LR
    C03(["C03 Lịch của mẹ · Ngày"]) -- "+ Tạo lịch cho mẹ" --> C06["C06 Thông tin việc<br/>Bước 1/3"]
    C03 -- "Tuần / Tháng" --> C04["C04 / C05 Tuần · Tháng"]
    C04 -- "chạm một ngày" --> C03
    C06 -- "Tiếp tục" --> V{"Đủ tên & giờ?"}
    V -- "chưa" --> C06E["C06e Thiếu tên / giờ"] -- "điền lại" --> C06
    V -- "đủ" --> C07["C07 Lặp lại<br/>Bước 2/3"]
    C07 -- "Mỗi tháng" --> C07M["C07m Chọn ngày 1–31"]
    C07 -- "Xem lại" --> C08["C08 Xem lại & gửi<br/>Bước 3/3"]
    C07M -- "Xem lại" --> C08
    C08 -- "Gửi lịch cho mẹ" --> W{"Trùng giờ?"}
    W -- "có" --> C08W["C08w Trùng giờ với việc khác"]
    C08W -- "Đổi giờ khác" --> C06
    C08W -- "Vẫn gửi" --> C09
    W -- "không" --> C09(["C09 Đã gửi · chờ mẹ nhận"])
    C09 -. "mẹ chọn Nhận" .-> G05(["Máy mẹ: G11 → G05 Đã thêm vào lịch"])
```

| Loại nhánh | Mô tả |
| --- | --- |
| Happy path | C03 → C06 (Vận động · Đi bộ nhẹ nhàng · 8:00 sáng · 15 phút) → C07 (Mỗi tuần, T2 T4 T6, từ 16/10, không kết thúc) → C08 → "Gửi lịch cho mẹ" → C09 |
| Alternate | Lặp mỗi tháng (C07m: ngày 1 và 15, 1/11 – 31/12/2026); xem lịch theo Tuần (C04: số việc và số đã xong mỗi ngày) hoặc Tháng (C05) |
| Error prevention / recovery | C06e báo lỗi ngay dưới ô thiếu tên / thiếu giờ; câu tóm tắt bằng chữ ở C07 ("Mẹ được nhắc… vào Thứ Hai, Thứ Tư, Thứ Sáu") để kiểm tra trước khi gửi; C08w cảnh báo trùng giờ nhưng vẫn cho gửi; switch "Mẹ nhận trước khi thêm" bật sẵn nên lịch không tự chen vào máy mẹ |

## 13. Flow 12 – Người thân sửa / ngưng một lịch lặp

**Mục tiêu:** đổi giờ đi bộ từ 8:00 sang 7:30 cho một ngày, hoặc ngưng hẳn lịch, mà không xóa lịch sử mẹ đã làm.

```mermaid
flowchart LR
    C03(["C03 Lịch của mẹ"]) -- "chạm việc" --> C10["C10 Chi tiết việc (lặp lại)<br/>6 lần gần nhất"]
    C10 -- "Sửa" --> C06["C06 Sửa việc (điền sẵn)"]
    C06 -- "Lưu" --> C11{"C11 Áp dụng cho lần nào?"}
    C11 -- "Chỉ lần này / Từ lần này về sau / Tất cả" --> OK(["C03 · đã cập nhật lịch"])
    C11 -- "Hủy" --> C06
    C10 -- "Ngưng lặp lại" --> C12{"C12 Ngưng lịch đi bộ?"}
    C12 -- "Ngưng lặp lại" --> STOP(["C03 · đã ngưng + Hoàn tác"])
    C12 -- "Giữ lại" --> C10
    STOP -- "Hoàn tác" --> SAME(["C03 như cũ"])
```

| Loại nhánh | Mô tả |
| --- | --- |
| Happy path | C03 → C10 → "Sửa việc" → C06 đổi 7:30 → C11 "Chỉ lần này · 19/10" → C03 |
| Alternate | C11 "Từ lần này về sau" hoặc "Tất cả các lần" |
| Error prevention / recovery | C12 nói rõ hậu quả ("Mẹ sẽ không còn được nhắc vào T2, T4, T6. Những lần mẹ đã làm vẫn được giữ lại"), nút an toàn "Giữ lại"; sau khi ngưng có "Hoàn tác" |

## 14. Flow bổ sung – Bác nhận gợi ý lịch từ người thân (G01 – G12)

Flow này chưa vẽ trên page `01 User Flow` nhưng đã có đủ màn trong `03 Final UI` và `06 Prototype`.

```mermaid
flowchart LR
    G01(["G01 Mai soạn gợi ý<br/>(máy Mai)"]) -- "Gửi gợi ý cho mẹ" --> G02(["G02 Đã gửi"])
    G02 -.-> G11["G11 Popup trên S03 máy Bác<br/>“Mai gửi lịch cho Bác”"]
    G11 -- "Để sau" --> G12["G12 Thẻ gợi ý ở đầu Hôm nay"]
    G11 -- "Xem gợi ý" --> G03["G03 Lịch Mai gợi ý"]
    G12 -- "Xem gợi ý" --> G03
    S09(["S09 · Gợi ý từ Mai"]) --> G03
    G03 -- "Thêm 2 việc vào lịch" --> G05["G05 Đã thêm"] --> G08["G08 Lịch ngày mai"]
    G03 -- "Đổi giờ đi bộ" --> G04["G04 Chọn 8:00 / 9:00"] --> G03B["G03b Gợi ý theo giờ của Bác"] --> G05B["G05b"] --> G08B["G08b"]
    G03 -- "Chọn từng việc" --> G06["G06"] -- "Chỉ đi bộ / Chỉ gọi điện" --> G07["G07 / G07b"] --> G08C["G08c / G08d"]
    G03 -- "Bỏ qua gợi ý" --> G09["G09 Đã bỏ qua"] -- "Hoàn tác" --> G03
```

| Loại nhánh | Mô tả |
| --- | --- |
| Happy path | G11 "Xem gợi ý" → G03 → "Thêm 2 việc vào lịch" → G05 → "Xem lịch ngày mai" → G08 |
| Alternate | Đổi giờ (G04 → G03b → G05b), chọn từng việc (G06 → G07 / G07b), để sau (G12) |
| Error prevention / recovery | Lịch chỉ đổi khi Bác bấm nhận ("Chưa thêm vào lịch. Bác tự chọn việc và giờ phù hợp."); bỏ qua có "Hoàn tác"; app không tự báo cho Mai là Bác đã bỏ qua hay đã làm |

## 15. Ánh xạ flow → màn hình → frame Figma

| Flow | Màn hình / state đi qua | Vị trí trong page 06 |
| --- | --- | --- |
| ★ Demo chính (gồm Flow 1) | 24 bước, đi qua 14 màn chính: S01 → S02 → S13 → ST-Empty → S03 → S11 hôm nay → S04 → DLG-Done → S03b → S05 → S06 → ST-Loading → ST-Saved → S07 → S11 Thứ Sáu → S04 Đi khám → S08 → S09 → S12a → S12e → S12 → S09b → S10 → S14 | Flow starting point `★ Main flow – Một ngày của bà Lan` đặt tại S01 – từ đây đi được tới cả 17 màn chính bằng nút bấm (S15 qua nút "Sửa" ở S04, S16 qua S08, S17 qua S09) |
| Flow 2 Thêm việc | S03, S05, S06, ST-Validation, ST-Loading, ST-Error, ST-Saved | Hàng chính bước 10–13; hàng "↳ từ S06 · Lỗi khi thêm việc" (S06e → ST-Validation → S06o → ST-Error) |
| Flow 3 Hoàn thành / dời / bỏ qua | S03, S04, DLG-Done, DLG-Later, DLG-Skip, S03 + snackbar (đã dời 30 phút / chiều nay / ngày mai, đã bỏ qua) | Hàng chính bước 5–9; hàng "↳ từ S03 · Dời lại" và "↳ từ S04 · Bỏ qua hôm nay" |
| Flow 4 Xem lịch một ngày | S07, S11, S11b, S04, (S03, S05) | Hàng chính bước 14–16; hàng "↳ từ S07 · Các ngày khác trong tuần" |
| Flow 5 Thêm người thân | S09, S12a (chưa có số), S12e, S12, S09b | Hàng chính bước 18–22 |
| Flow 6 Lời nhắc đến giờ | S14, S04, DLG-Done, S03 + snackbar nhắc lại, DLG-Skip | Flow starting point `Flow chính 2 – Lời nhắc` đặt tại S14 |
| Flow 7 Sửa & xóa | S04, S15, S03 đã lưu, DLG-Delete, S03 đã xóa | Hàng "↳ từ S04 · Sửa & xóa việc (Flow 7)" |
| Flow 8 Thói quen | S08, S16 × 9 thói quen, S05 / S06, S04 | Flow starting point `Flow chính 1 – Khám phá` đặt tại S08 |
| Flow 9 Nhắn tin cho con cháu | S03 xong 6/6, S09, S17 (Mai / Hùng / Bin), S17b | Hàng "↳ từ S09 · Nhắn tin cho từng người" và "↳ từ S03b · Cuối ngày xong 6/6" |
| Ngoài flow (bottom nav / app bar) | S08, S10 | Mở từ bất kỳ màn có bottom nav / nút Cài đặt |
| Trạng thái onboarding | S13d Nhắc việc đang tắt | Từ S13 bấm "Để sau" |

Trong prototype, mỗi việc của hôm nay và các ngày sắp tới có một frame chi tiết riêng (hàng ④ ở page 06). Chỉ "việc tiếp theo" (Đi bộ 9:30) có nút "Tôi đã làm xong"; việc chưa tới giờ hiện giờ hẹn và lời nhắc, việc đã xong hiện "Bà đã làm xong việc này".

Bổ sung từ 13–15/10:

| Flow | Màn hình / state đi qua | Vị trí trong page 06 |
| --- | --- | --- |
| Flow 10 Ghép nối | C01, C02, C02e, C03 | Hàng "NGƯỜI THÂN – Con, cháu ghép nối & lập lịch cho mẹ" (bước 1 – 3) |
| Flow 11 Lập lịch cho mẹ | C03, C04, C05, C06, C06e, C07, C07m, C08, C08w, C09 | `Flow chính 3 – Gia đình: người thân lập lịch cho mẹ (Flow 11)` đặt tại C03 |
| Flow 12 Sửa / ngưng lịch lặp | C10, C11, C12 | Cùng hàng Người thân (bước 14 – 16) |
| Gợi ý lịch (G) | G01 – G12 | Hàng G ở page 06, mở từ S09 "Gợi ý từ Mai" hoặc G11 |
| Flow chính 1 Khám phá (Flow 8 + 2) | S08, S16, S05, S06, ST-Saved | `Flow chính 1 – Khám phá` đặt tại S08 |
| Flow chính 2 Lời nhắc (Flow 6 + 3) | S14, S04, DLG-Done, DLG-Skip, S03-snooze | `Flow chính 2 – Lời nhắc` đặt tại S14 |

Page 06 hiện có 4 flow starting point: ★ Main flow (S01), Flow chính 1 (S08), Flow chính 2 (S14), Flow chính 3 (C03). Các flow 2 – 9 cũ vẫn đi được từ Main flow; nhãn "↳ từ …" phía trên mỗi hàng cho biết hàng đó mở từ màn nào.

Kiểm tra không có ngõ cụt: mọi màn cấp 2–3 có nút "Quay lại" (prototype action **Back**); mọi state có ít nhất một nút dẫn tiếp. Frame START HERE ghi: 964 tham chiếu điều hướng đều có đích trong Final UI.
