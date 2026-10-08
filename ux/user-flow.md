# Information Architecture & User Flows

## 1. Information architecture

App có 4 tab cấp cao và mỗi tab sâu tối đa 2 cấp con, để người lớn tuổi không bị lạc. Màn Cài đặt mở từ nút có chữ trên app bar, không chiếm một tab riêng.

```mermaid
flowchart TD
    S01["S01 Chào mừng<br/>(chọn cỡ chữ)"] --> S02["S02 Thiết lập hồ sơ"]
    S02 --> NAV{{"Bottom navigation – 4 tab có nhãn"}}
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
    S07 --> S03
    S03 -. "không có việc" .-> EMPTY["ST Home trống"]
```

| Cấp | Màn hình |
| --- | --- |
| Onboarding (chỉ lần đầu) | S01, S02 |
| Cấp 1 – tab | S03 Hôm nay · S07 Lịch tuần · S08 9 thói quen · S09 Gia đình |
| Cấp 2 | S04 Chi tiết · S05 Thêm việc bước 1 · S10 Cài đặt |
| Cấp 3 | S06 Thêm việc bước 2 |
| State / overlay | ST-Empty, ST-Validation, ST-Loading, ST-Error, ST-Saved, DLG-Done |

## 2. Flow 1 – Lần đầu mở app (Onboarding)

**Mục tiêu:** bà Lan cài xong và thấy lịch hôm nay trong dưới 2 phút.

```mermaid
flowchart LR
    A(["Mở app lần đầu"]) --> S01["S01 Chọn cỡ chữ<br/>Vừa / Lớn / Rất lớn"]
    S01 -- "Bắt đầu" --> S02["S02 Nhập tên,<br/>giờ thức dậy"]
    S02 -- "Tiếp tục" --> C{"Tên đã nhập?"}
    C -- "chưa" --> E1["Báo lỗi dưới ô Tên<br/>+ ví dụ"] --> S02
    C -- "rồi" --> D{"Đã có việc nào?"}
    D -- "có" --> S03(["S03 Hôm nay"])
    D -- "chưa" --> EMPTY["ST Home trống"]
    EMPTY -- "Dùng lịch mẫu Power 9" --> S03
    EMPTY -- "Thêm việc đầu tiên" --> S05["S05 → Flow 2"]
    S02 -- "Quay lại" --> S01
```

| Loại nhánh | Mô tả |
| --- | --- |
| Happy path | S01 → S02 → S03 |
| Alternate | Chưa có việc → ST-Empty → "Dùng lịch mẫu Power 9" → S03 |
| Error / recovery | Bỏ trống tên → báo lỗi ngay dưới ô (icon + chữ + ví dụ) → nhập lại |

## 3. Flow 2 – Thêm việc mới (có lỗi và phục hồi)

**Mục tiêu:** thêm "Tập thở chậm 10 phút, 8:00 sáng mỗi ngày" trong ≤ 60 giây.

```mermaid
flowchart LR
    S03(["S03 Hôm nay"]) -- "Thêm việc" --> S05["S05 Chọn thói quen<br/>(Thư giãn mỗi ngày)"]
    S05 -- "Tiếp tục" --> S06["S06 Tên việc, giờ,<br/>lặp lại, nhắc nhở"]
    S06 -- "Lưu việc này" --> V{"Đủ tên việc?"}
    V -- "không" --> VAL["ST Validation<br/>lỗi + chip gợi ý"]
    VAL -- "chọn gợi ý / sửa" --> S06
    V -- "có" --> LOAD["ST Đang lưu…"]
    LOAD -- "lưu được" --> SAVED["ST Đã lưu"]
    LOAD -- "mất mạng" --> ERR["ST Lưu thất bại"]
    ERR -- "Thử lại" --> LOAD
    ERR -- "Lưu trên máy, gửi sau" --> SAVED
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
| Error / recovery 2 | Mất mạng → ST-Error → Thử lại / Lưu trên máy / Quay lại sửa |

## 4. Flow 3 – Hoàn thành một việc

**Mục tiêu:** đánh dấu "Đi bộ quanh công viên" đã xong trong ≤ 2 lần chạm.

```mermaid
flowchart LR
    S03(["S03 Hôm nay<br/>thẻ Việc tiếp theo"]) -- "Đã xong" --> DLG["DLG Bà đã đi bộ<br/>xong rồi chứ?"]
    DLG -- "Đúng, đã xong" --> R(["S03 tiến độ 3/6 → 4/6<br/>con gái nhận tin"])
    DLG -- "Chưa, để sau" --> S03
    S03 -- "chạm tên việc" --> S04["S04 Chi tiết hoạt động"]
    S04 -- "Tôi đã làm xong" --> DLG
    S04 -- "Dời 30 phút" --> S03
    S04 -- "Bỏ qua hôm nay" --> S03
    S04 -- "Quay lại" --> S03
```

| Loại nhánh | Mô tả |
| --- | --- |
| Happy path | S03 → "Đã xong" → DLG → "Đúng, đã xong" → S03 cập nhật |
| Alternate | S03 → S04 → "Dời 30 phút" hoặc "Bỏ qua hôm nay" |
| Error prevention | Dialog xác nhận chặn việc bấm nhầm; "Chưa, để sau" đưa về như cũ, không đổi dữ liệu |

## 5. Ánh xạ flow → màn hình → frame Figma

| Flow | Màn hình / state đi qua | Starting point trong page 06 |
| --- | --- | --- |
| Flow 1 Onboarding | S01, S02, (ST-Empty), S03 | `Flow 1 Onboarding` đặt tại S01 |
| Flow 2 Thêm việc | S03, S05, S06, ST-Validation, ST-Loading, ST-Error, ST-Saved | `Flow 2 Thêm việc` và `Flow 2b Mất mạng` đặt tại S03 |
| Flow 3 Hoàn thành | S03, S04, DLG-Done | `Flow 3 Hoàn thành` đặt tại S03 |
| Ngoài flow (bottom nav / app bar) | S07, S08, S09, S10 | Mở từ bất kỳ màn có bottom nav |

Kiểm tra không có ngõ cụt: mọi màn cấp 2–3 có nút "Quay lại" (prototype action **Back**); mọi state có ít nhất một nút dẫn tiếp.
