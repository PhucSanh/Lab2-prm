# Accessibility & Responsive Checklist

Mức đề yêu cầu: contrast ≥ 4.5 : 1 (chữ thường) và ≥ 3 : 1 (chữ lớn, UI control); touch target ≥ 48 × 48 dp; chữ nội dung ≥ 14 sp; kiểm tra ở 360 dp và 412 dp.
An Nhiên đặt mức cao hơn vì đối tượng là người 65+: chữ nhỏ nhất 20, nút chính cao 60 dp.

## 1. Contrast (tính theo công thức WCAG 2.x relative luminance, màu lấy từ Variables Figma 15/10/2026)

| Cặp màu | Tỉ lệ | Yêu cầu | Kết quả |
| --- | ---: | --- | --- |
| Chữ chính `#202B25` / nền `#F6F7F2` | 13.60 : 1 | 4.5 : 1 | Đạt (AAA) |
| Chữ chính `#202B25` / thẻ `#FFFFFF` | 14.65 : 1 | 4.5 : 1 | Đạt (AAA) |
| Chữ phụ `#526057` / nền `#F6F7F2` | 6.15 : 1 | 4.5 : 1 | Đạt (AA) |
| Chữ phụ `#526057` / thẻ `#FFFFFF` | 6.63 : 1 | 4.5 : 1 | Đạt (AA) |
| Chữ trắng / nút `primary #1F684B` | 6.69 : 1 | 4.5 : 1 | Đạt |
| `primary #1F684B` (chữ, viền, tab đang chọn) / nền | 6.21 : 1 | 4.5 : 1 | Đạt |
| Chữ `#174C37` / `primary-container #D6EADF` | 7.85 : 1 | 4.5 : 1 | Đạt (AAA) |
| Chữ `#174C37` / `primary-container-soft #E7F2EB` | 8.61 : 1 | 4.5 : 1 | Đạt (AAA) |
| `error #B42318` / nền | 6.11 : 1 | 4.5 : 1 | Đạt |
| Chữ trắng / nút Danger `#B42318` | 6.57 : 1 | 4.5 : 1 | Đạt |
| Chữ `#912018` / `error-container #FDECE9` | 7.57 : 1 | 4.5 : 1 | Đạt (AAA) |
| Chữ `#8A5100` / `warning-container #FFF3DB` | 5.86 : 1 | 4.5 : 1 | Đạt |
| Chữ trắng / Snackbar nền `#202B25` | 14.65 : 1 | 4.5 : 1 | Đạt (AAA) |
| Viền ô nhập `outline #7B887F` / nền | 3.44 : 1 | 3 : 1 (UI control) | Đạt |
| Chữ disabled `#627067` / `#E6EAE5` | 4.28 : 1 | Miễn trừ (WCAG 1.4.3) | — |
| `border-strong #A0ACA3` / trắng | 2.35 : 1 | — | Chỉ trang trí; thẻ chưa chọn luôn có chữ, trạng thái chọn có viền `primary` + ✓ |
| 9 cặp màu thói quen (icon/chữ trên nền nhạt) | 6.45 – 9.92 : 1 | 4.5 : 1 | Đạt cả 9 (chi tiết ở DESIGN.md 3.1) |

Bằng chứng: chạy plugin **Stark** hoặc **Contrast** trong Figma cho ít nhất 3 cặp trên, chụp vào `assets/a11y/contrast-*.png`.

## 2. Touch target

| Thành phần | Kích thước | Yêu cầu |
| --- | --- | --- |
| Nút chính (Đã xong, Lưu, Tiếp tục, Gửi lịch cho mẹ) | cao 60 dp (nút phụ viền 63 dp), ngang Fill | ≥ 48 |
| Nút Quay lại, Cài đặt, Sửa, chip gợi ý | cao 48 dp | ≥ 48 |
| Ô giờ trong S06 / S15 / N05 | 320 × 62 dp | ≥ 48 |
| Hàng giờ/phút trong hộp chọn giờ (DLG-TaskTime) | 96 × 48 dp; Hủy / Xong 142 × 60 | ≥ 48 |
| Ô ngày lịch tháng của mẹ (C05) | 45 × 50 dp | Đạt chiều cao; ngang 45 do 7 cột trong 320 dp |
| Ô ngày chọn ngày lặp hằng tháng (C07m) | 41 × 40 dp | **Chưa đạt** – xem mục 7 |
| Ô ngày trong N11 Chọn ngày | 48 × 25 dp | **Chưa đạt** chiều cao – xem mục 7 |
| Ô nhập mã ghép nối (C02) | 6 ô 47 × 64 dp | ≥ 48 cao |
| Mục bottom nav | 88 × 66 dp (88 × 92 khi nhãn xuống 2 dòng) | ≥ 48 |
| Khoảng cách giữa 2 nút kề nhau | ≥ 8 dp (thường 10–12) | — |

Bằng chứng: chọn nút trong Figma, chụp panel phải hiện W × H → `assets/a11y/touch-target.png`.

## 3. Cỡ chữ

- Nhỏ nhất trong toàn app: 20 sp (`body-md`, `caption`, `label-nav`); nội dung chính 24; tiêu đề màn 30. Tất cả ≥ 14 sp.
- S01 và S10 cho chọn cỡ chữ Vừa / Lớn / Rất lớn; collection `Dễ đọc · Cỡ chữ` đổi cỡ toàn bộ. Khi chuyển sang Flutter, giao diện phải chịu được `textScaler` tới 2.0 (frame START HERE ghi rõ: cần nghiệm thu chữ hệ thống 200 % trên thiết bị).
- Đã kiểm tra trong Figma: không có Main nào bị clipping nội dung vượt khung mà thiếu cuộn.

## 4. Không dùng màu làm tín hiệu duy nhất

| Trạng thái | Tín hiệu ngoài màu |
| --- | --- |
| Việc đã xong | Icon ✓ + chữ "Đã xong" |
| Việc bỏ qua | Icon ✕ + chữ "Bỏ qua · 9:30 sáng" |
| Tab đang chọn | Nền pill + chữ đậm |
| Ô / ngày đang chọn | Viền dày + dấu ✓; ngày lặp lại ghi bằng chữ "Đã chọn · Thứ Hai" |
| Lỗi nhập | Icon ⓘ + câu giải thích + ví dụ |
| Lịch của mẹ (C04, C05) | Số việc ghi bằng chữ "4 việc · xong 2", chấm màu chỉ là phụ |
| Nhánh lỗi trong user flow | Mũi tên có nhãn chữ |

## 5. Responsive 360 dp vs 412 dp

| Màn | 360 × 800 | 412 | Ghi chú |
| --- | --- | --- | --- |
| S03 Hôm nay | [x] | [x] | Frame `S03 Hôm nay · 412 dp (kiểm tra responsive)` trong 03 Final UI |
| S05 Thêm việc | [ ] | [ ] | Thẻ Fill giãn đều |
| S06 Thiết lập việc | [ ] | [ ] | Ô giờ Fill, hộp chọn giờ giữ 336 dp |
| S09 Gia đình | [ ] | [ ] | 2 nút trong thẻ chia đôi |
| C05 Lịch tháng | [ ] | [ ] | Ô ngày giãn từ 44 lên ~51 dp |

Cách làm: Ctrl+D frame → đổi chiều ngang thành 412 → kiểm tra không tràn hoặc cắt chữ → chụp hai bản cạnh nhau vào `assets/a11y/responsive-S03.png`.

## 6. Khác

- [x] Không có cử chỉ vuốt hay nhấn giữ là cách duy nhất (mọi hành động đều có nút; hộp chọn giờ cho chạm trực tiếp vào số).
- [x] Không có nội dung tự tắt theo thời gian (Snackbar "Hoàn tác" và popup gợi ý G11 không tự đóng).
- [ ] Mọi icon-only button có tên cho screen reader (ghi trong handoff: `tooltip` / `semanticLabel`).
- [ ] Animation chuyển màn ≤ 300 ms, không nhấp nháy.
- [ ] Usability test với người lớn tuổi trước khi phát hành (chưa làm – ghi trong START HERE).

## 7. Vấn đề còn mở (phát hiện khi đồng bộ 15/10)

| Vấn đề | Ở đâu | Đề xuất sửa |
| --- | --- | --- |
| Nhãn "Lịch tuần" và "Thói quen" xuống 2 dòng ở cỡ 20, làm 2 tab giữa cao 92 trong khi 2 tab ngoài cao 66 – bottom nav lệch hàng | `BottomNav` (vd node 1:9416 trong S03) | Rút nhãn thành "Tuần" / "Thói quen" một dòng, hoặc cố định chiều cao mọi NavItem = 92 và căn icon thẳng hàng; kiểm tra lại ở 412 dp |
| Ô ngày ở N11 chỉ cao 25 dp (frame tên "Calendar · 48px target" nhưng mỗi hàng 25); ô ngày C07m 41 × 40 dp | N11, C07m | Tăng chiều cao mỗi hàng lịch lên 48 (lịch cao ~300 dp, vẫn vừa màn vì phần thân cuộn); ở C07m có thể giảm còn 5 hàng × 7 cột và tăng ô lên 44 × 48. Người thân dùng C07m nên mức 44 chấp nhận được, N11 là màn của người lớn tuổi nên phải sửa |
| Ô ngày lịch tháng C05 rộng 45 dp ở 360 dp | C05 | Chấp nhận được (cao 50); Flutter dùng `Expanded` để ô giãn theo màn |
| Frame START HERE ghi nền "#F0FDF3" nhưng Variable `color/bg` và mọi màn đang dùng `#F6F7F2` | 03 Final UI · START HERE | Sửa chữ trong START HERE cho khớp `#F6F7F2` |
