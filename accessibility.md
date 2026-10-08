# Accessibility & Responsive Checklist

Mức đề yêu cầu: contrast ≥ 4.5 : 1 (chữ thường) và ≥ 3 : 1 (chữ lớn, UI control); touch target ≥ 48 × 48 dp; chữ nội dung ≥ 14 sp; kiểm tra ở 360 dp và 412 dp.
An Nhiên đặt mức cao hơn vì đối tượng là người 65+.

## 1. Contrast (tính theo công thức WCAG 2.x relative luminance)

| Cặp màu | Tỉ lệ | Yêu cầu | Kết quả |
| --- | ---: | --- | --- |
| Chữ chính `#1F2A24` / nền `#FBF8F2` | 14.00 : 1 | 4.5 : 1 | Đạt (AAA) |
| Chữ phụ `#4A5550` / nền `#FBF8F2` | 7.32 : 1 | 4.5 : 1 | Đạt (AAA) |
| Chữ trắng / nút `primary #1F6B4A` | 6.44 : 1 | 4.5 : 1 | Đạt |
| `primary #1F6B4A` (chữ, viền) / nền | 6.08 : 1 | 4.5 : 1 | Đạt |
| Chữ `#0F3D2A` / `primary-container #D7EDE0` | 9.92 : 1 | 4.5 : 1 | Đạt |
| Chữ trắng / nút `secondary #A3471F` | 6.04 : 1 | 4.5 : 1 | Đạt |
| `error #B3261E` / nền | 6.17 : 1 | 4.5 : 1 | Đạt |
| Chữ `#8C1D18` / `error-container #FCE4E1` | 7.52 : 1 | 4.5 : 1 | Đạt |
| Chữ `#7A4E00` / `warning-container #FFF1D6` | 6.45 : 1 | 4.5 : 1 | Đạt |
| Viền ô nhập `outline #7A857F` / nền | 3.61 : 1 | 3 : 1 (UI control) | Đạt |
| Chữ disabled `#6B746F` / `#E6E3DC` | 3.76 : 1 | Miễn trừ (WCAG 1.4.3) | — |

Bằng chứng: chạy plugin **Stark** hoặc **Contrast** trong Figma cho ít nhất 3 cặp trên, chụp vào `assets/a11y/contrast-*.png`.

## 2. Touch target

| Thành phần | Kích thước | Yêu cầu |
| --- | --- | --- |
| Nút chính (Đã xong, Lưu, Tiếp tục) | cao 56–60 dp, ngang Fill | ≥ 48 |
| Nút −/+ chọn giờ | 56 × 56 dp | ≥ 48 |
| Nút Quay lại, Cài đặt, chip gợi ý | cao 48 dp | ≥ 48 |
| Ô chọn thói quen (S05) | ≥ 152 × 92 dp | ≥ 48 |
| Mục bottom nav | ~88 × 66 dp | ≥ 48 |
| Khoảng cách giữa 2 nút kề nhau | ≥ 8 dp (thường 10–12) | — |

Bằng chứng: chọn nút trong Figma, chụp panel phải hiện W × H → `assets/a11y/touch-target.png`.

## 3. Cỡ chữ

- Nhỏ nhất trong nội dung: 16 sp (`body-md`); nội dung chính 18 sp; nhãn bottom nav 15 sp. Tất cả ≥ 14 sp.
- S01 và S10 cho chọn cỡ chữ Vừa / Lớn / Rất lớn. Khi chuyển sang Flutter, giao diện phải chịu được `textScaler` tới 2.0.
- Kiểm tra: tăng `body-lg` lên 22 sp, các thẻ Auto Layout (Hug) tự cao lên, không bị cắt chữ.

## 4. Không dùng màu làm tín hiệu duy nhất

| Trạng thái | Tín hiệu ngoài màu |
| --- | --- |
| Việc đã xong | Icon ✓ + chữ "Đã xong" |
| Tab đang chọn | Nền pill + chữ đậm |
| Ô thói quen đang chọn | Viền dày 3 dp + dấu ✓ góc phải |
| Lỗi nhập | Icon ⓘ + câu giải thích + ví dụ |
| Nhánh lỗi trong user flow | Mũi tên có nhãn chữ |

## 5. Responsive 360 dp vs 412 dp

| Màn | 360 × 800 | 412 × 917 | Ghi chú |
| --- | --- | --- | --- |
| S03 Hôm nay | [ ] | [ ] | Card, nút Fill giãn đều |
| S05 Chọn thói quen | [ ] | [ ] | Lưới 2 cột giãn, không thêm cột |
| S06 Chọn giờ | [ ] | [ ] | Stepper giữ 56 dp, phần giữa giãn |
| S09 Gia đình | [ ] | [ ] | 2 nút trong thẻ chia đôi |

Cách làm: Ctrl+D frame → đổi kích thước thành 412 × 917 → kiểm tra không tràn hoặc cắt chữ → chụp hai bản cạnh nhau vào `assets/a11y/responsive-S03.png`.

## 6. Khác

- [ ] Không có cử chỉ vuốt hay nhấn giữ bắt buộc (mọi hành động đều có nút).
- [ ] Không có nội dung tự tắt theo thời gian (không dùng toast cho thông tin quan trọng).
- [ ] Mọi icon-only button (−/+) có tên cho screen reader (ghi trong handoff: `tooltip` / `semanticLabel`).
- [ ] Animation chuyển màn ≤ 300 ms, không nhấp nháy.
