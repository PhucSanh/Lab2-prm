# Chia việc chạy Stitch – đủ 105 khung

> Mục tiêu: sinh lại bằng `/stitch-loop` toàn bộ khung trong page `03 Final UI` (105 khung), để prototype dùng một bộ màn đồng đều.
> Đã xong: **17 màn chính S01 – S17** (xem `SUMMARY.md`). Còn lại: **88 khung**, chia cho 2 người như bên dưới.

| Làn | Người chạy | Stitch project | Phạm vi | Số khung |
| --- | --- | --- | --- | ---: |
| **A** | Sanh | `2013215887278758682` (trong `project.txt`) | State, dialog, biến thể của S01 – S17, N "con" của S, G10 – G12 (nằm trên S03) | 45 |
| **B** | Hieu | Project riêng của teammate (agent tự tạo) | Chế độ Người thân C01 – C12, Gợi ý lịch G01 – G09, N độc lập | 40 |
| **C** | Ai rảnh làm | Không dùng Stitch | Biến thể chỉ đổi chữ (S04 ·, S11 ·, S16 ·, S17 ·) – duplicate trong Figma rồi sửa chữ | 3 |

**Vì sao chia như vậy:** biến thể (cách `EDIT`) phải sửa trên màn gốc nằm **cùng project Stitch**. Các màn gốc S01 – S17 nằm trong project của Sanh, nên mọi biến thể của S thuộc làn A. Làn B gồm những nhóm khép kín (C, G, N độc lập): teammate tự sinh màn gốc của nhóm rồi làm biến thể ngay trong project của mình.

---

## 1. Cách chạy

### Hai cách sinh

| Cách | Lệnh | Khi nào |
| --- | --- | --- |
| `NEW` | `/stitch-loop <mã> <tên>` | Màn mới hoàn toàn, sinh v0 bằng `generate_screen_from_text` |
| `EDIT X` | `/stitch-loop <mã> <tên> --from X` | Biến thể của màn X: v0 = `edit_screens` trên **màn chốt của X**. X phải chạy xong trước (có dòng `Kết quả:` trong `stitch-runs/X/log.md`) |

Ví dụ: `/stitch-loop S03b Hôm nay sau khi xong 1 việc --from S03`

### Chạy hàng loạt (không cần ngồi trông)

```powershell
.\scripts\stitch-all.ps1 -Lane A        # Sanh
.\scripts\stitch-all.ps1 -Lane B        # Teammate
.\scripts\stitch-all.ps1 -Lane A -Only S03b,S12a   # chỉ vài khung
```

Script đọc bảng của làn trong file này, chạy **theo đúng thứ tự** (màn gốc trước, biến thể sau) và bỏ qua khung đã có `Kết quả:`. Khung `EDIT X` mà X chưa xong sẽ bị bỏ qua, chạy lại script là nó làm tiếp.

### Nguồn nội dung

`PRD.md` 11.2 chỉ có 7 màn. Với các khung còn lại, agent lấy nội dung theo cột **Nguồn** (chủ yếu `flutter-handoff.md` và `ux/user-flow.md`) và ghi rõ vào `v0-prompt-trace.md`, giống cách đã làm cho S12. Token, câu chữ, từ ngữ vẫn lấy từ 4 file trong `assets/stitch/`, luật lấy từ `rule.md`.

---

## 2. Luật làm chung (tránh conflict git)

1. Mỗi người chỉ commit thư mục `stitch-runs/<mã>/` của khung mình chạy. Không sửa thư mục của làn kia.
2. **Teammate:** xóa `stitch-runs/project.txt` trên máy mình trước khi chạy (agent sẽ tạo project mới và ghi id vào đó). **Không commit** file này: chạy `git update-index --skip-worktree stitch-runs/project.txt`.
3. Khi chạy hết, `stitch-all.ps1` ghi đè `SUMMARY.md` → **chỉ Sanh commit `SUMMARY.md`**. Teammate bỏ thay đổi file này trước khi commit (`git checkout -- stitch-runs/SUMMARY.md`).
4. API key mỗi người tự cài vào Stitch MCP trên máy mình. Không ghi key vào file nào trong repo.
5. Sửa `rule.md`, `assets/stitch/*.md` hay `.claude/` thì báo người kia, vì đổi luật giữa chừng làm hai làn chấm lệch nhau.
6. Quota Stitch có giới hạn. Mỗi khung tốn tối đa 9 lần sinh/sửa. Nên chạy từng đợt, xem `SUMMARY.md` rồi mới chạy tiếp.
7. Khung nào ra `NEEDS_HUMAN` thì đọc lý do trong `log.md`, quyết định rồi ghi vào `design-decisions.md`.

---

## 3. Làn A – Sanh (45 khung)

| # | Mã | Tên màn | Cách | Nguồn | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| A01 | ST-Loading | Đang lưu việc | NEW | handoff · States | Màn gốc của ST-* |
| A02 | ST-Saved | Đã lưu xong | NEW | handoff · States | |
| A03 | ST-Error | Chưa lưu được | NEW | handoff · States | 3 nút xếp dọc |
| A04 | DLG-Done | Xác nhận đã xong | NEW | handoff · States | Màn gốc của DLG-*, overlay trên S03 |
| A05 | DLG-WakeTime | Chọn giờ thức dậy | NEW | handoff · States | Overlay trên S02 |
| A06 | ST-Empty | Hôm nay chưa có việc | EDIT S03 | handoff · States | |
| A07 | S03b | Hôm nay sau khi xong 1 việc | EDIT S03 | user-flow · Flow 3 | Snackbar "Hoàn tác" |
| A08 | S03-later | Hôm nay · đã dời 30 phút | EDIT S03 | handoff · DLG-Later | Chỉ đổi snackbar – có thể làm ở Figma |
| A09 | S03-later4 | Hôm nay · dời chiều nay | EDIT S03 | handoff · DLG-Later | Như trên |
| A10 | S03-tomorrow | Hôm nay · dời ngày mai | EDIT S03 | handoff · DLG-Later | Như trên |
| A11 | S03-skip | Hôm nay · đã bỏ qua | EDIT S03 | handoff · DLG-Skip | TaskRow "Bỏ qua · 9:30 sáng (trời mưa)" |
| A12 | S03-edited | Hôm nay · đã lưu thay đổi | EDIT S03 | user-flow · Flow 7 | |
| A13 | S03-deleted | Hôm nay · đã xóa việc | EDIT S03 | handoff · DLG-Delete | |
| A14 | S03-snooze | Hôm nay · nhắc lại sau 10 phút | EDIT S03 | user-flow · Flow 6 | |
| A15 | S03-alldone | Hôm nay · xong 6/6 | EDIT S03 | user-flow · Flow 9 | Thẻ chúc mừng + "Nhắn tin" |
| A16 | S13d | Nhắc việc đang tắt | EDIT S13 | handoff · S13 | |
| A17 | ST-Validation | Thêm việc · báo lỗi nhập | EDIT S06 | handoff · States | |
| A18 | S06e | Thêm việc · thiếu thông tin | EDIT S06 | user-flow · Flow 2 | |
| A19 | S06o | Thêm việc · đã sửa lỗi | EDIT S06 | user-flow · Flow 2 | |
| A20 | S11b | Chi tiết ngày · ngày khác | EDIT S11 | handoff · S11 | |
| A21 | S12a | Thêm người thân · chưa có số | EDIT S12 | user-flow · Flow 5 | |
| A22 | S12e | Thêm người thân · số sai | EDIT S12 | user-flow · Flow 5 | |
| A23 | S09b | Gia đình · đã thêm người thân | EDIT S09 | user-flow · Flow 5 | |
| A24 | S17b | Nhắn tin · đã mở chia sẻ | EDIT S17 | handoff · S17 | |
| A25 | ST-Loading-offline | Đang lưu · mất mạng | EDIT ST-Loading | handoff · States | |
| A26 | DLG-Later | Dời việc | EDIT DLG-Done | handoff · States | |
| A27 | DLG-Skip | Bỏ qua hôm nay | EDIT DLG-Done | handoff · States | |
| A28 | DLG-Delete | Xóa việc | EDIT DLG-Done | handoff · States | Nút an toàn ở trên |
| A29 | DLG-TaskTime | Chọn giờ làm | EDIT DLG-WakeTime | handoff · States | |
| A30 | N06 | Sửa hồ sơ | EDIT S02 | handoff · N01–N21 | |
| A31 | N09 | Sửa người thân | EDIT S12 | handoff · N01–N21 | |
| A32 | N10 | Đã mở ứng dụng chia sẻ | EDIT S17b | handoff · N01–N21 | |
| A33 | N11 | Chọn ngày | NEW | handoff · N01–N21 | Lịch tháng 10/2026 |
| A34 | N12 | Lặp lại | NEW | handoff · N01–N21 | |
| A35 | N13 | Phạm vi thay đổi | EDIT DLG-Done | handoff · N01–N21 | |
| A36 | N14 | Chưa lưu thay đổi | EDIT DLG-Done | handoff · N01–N21 | |
| A37 | N15 | Xóa người thân | EDIT DLG-Delete | handoff · N01–N21 | |
| A38 | N16 | Đã lưu · nhắc cần kiểm tra | EDIT ST-Saved | handoff · N01–N21 | |
| A39 | N18 | Đã lưu việc đầu tiên | EDIT ST-Saved | handoff · N01–N21 | |
| A40 | N17 | Hôm nay · đã xử lý hết | EDIT S03-alldone | handoff · N01–N21 | |
| A41 | N19 | Hôm nay · việc đầu tiên | EDIT S03 | handoff · N01–N21 | |
| A42 | N21 | Gia đình sau khi xóa người thân | EDIT S09 | handoff · N01–N21 | |
| A43 | G12 | Hôm nay · thẻ gợi ý của Mai | EDIT S03 | handoff · G01–G12 | |
| A44 | G11 | Popup Mai gửi lịch cho Bác | EDIT S03 | handoff · G01–G12; PRD 11.2 #3 | Popup không tự đóng |
| A45 | G10 | Có gợi ý mới (tự hiện) | EDIT G11 | handoff · G01–G12 | |

**Đợt gợi ý:** A01 – A05 (5 màn gốc) → A06 – A24 (biến thể của S) → A25 – A45.

---

## 4. Làn B – Teammate (40 khung)

| # | Mã | Tên màn | Cách | Nguồn | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| B01 | C01 | Chọn vai trò | NEW | handoff · C01–C12 | Màn đầu tiên của app |
| B02 | C02 | Nhập mã ghép nối | NEW | handoff · C01–C12 | 6 ô 47 × 64 |
| B03 | C03 | Lịch của mẹ · Ngày | NEW | handoff · C01–C12 | Màn gốc của C04, C05 |
| B04 | C06 | Thông tin việc (Bước 1/3) | NEW | handoff · C01–C12; PRD 11.2 #7 | |
| B05 | C07 | Lặp lại mỗi tuần (Bước 2/3) | NEW | handoff · C01–C12 | |
| B06 | C08 | Xem lại & gửi (Bước 3/3) | NEW | handoff · C01–C12 | |
| B07 | C09 | Đã gửi · chờ mẹ nhận | NEW | handoff · C01–C12 | |
| B08 | C10 | Chi tiết việc lặp lại | NEW | handoff · C01–C12 | |
| B09 | C02e | Mã sai / hết hạn | EDIT C02 | handoff · C01–C12 | |
| B10 | C04 | Lịch của mẹ · Tuần | EDIT C03 | handoff · C01–C12 | |
| B11 | C05 | Lịch của mẹ · Tháng | EDIT C03 | handoff · C01–C12 | |
| B12 | C06e | Thiếu tên / giờ | EDIT C06 | handoff · C01–C12 | |
| B13 | C07m | Lặp lại mỗi tháng | EDIT C07 | handoff · C01–C12 | |
| B14 | C08w | Trùng giờ (overlay) | EDIT C08 | handoff · C01–C12 | |
| B15 | C11 | Áp dụng thay đổi cho (overlay) | EDIT C10 | handoff · C01–C12 | |
| B16 | C12 | Ngưng lịch lặp (overlay) | EDIT C10 | handoff · C01–C12 | |
| B17 | G01 | Con cháu soạn lịch gợi ý | NEW | handoff · G01–G12 | Máy người thân |
| B18 | G03 | Lịch Mai gợi ý | NEW | handoff · G01–G12; PRD 11.2 #3 | Màn gốc nhóm G phía Bác |
| B19 | G05 | Đã nhận | NEW | handoff · G01–G12 | |
| B20 | G08 | Lịch ngày mai | NEW | handoff · G01–G12 | |
| B21 | G01b | Soạn gợi ý · chọn giờ | EDIT G01 | handoff · G01–G12 | |
| B22 | G02 | Đã gửi gợi ý | EDIT G01 | handoff · G01–G12 | |
| B23 | G03b | Lịch Mai gợi ý · đã đổi giờ | EDIT G03 | handoff · G01–G12 | |
| B24 | G04 | Đổi giờ | EDIT G03 | handoff · G01–G12 | |
| B25 | G06 | Chọn từng việc | EDIT G03 | handoff · G01–G12 | |
| B26 | G05b | Đã nhận · đổi giờ | EDIT G05 | handoff · G01–G12 | |
| B27 | G07 | Đã nhận một việc | EDIT G05 | handoff · G01–G12 | |
| B28 | G07b | Đã nhận một việc (b) | EDIT G07 | handoff · G01–G12 | |
| B29 | G09 | Đã bỏ qua gợi ý | EDIT G05 | handoff · G01–G12 | Có "Hoàn tác" |
| B30 | G08b | Lịch ngày mai (b) | EDIT G08 | handoff · G01–G12 | |
| B31 | G08c | Lịch ngày mai (c) | EDIT G08 | handoff · G01–G12 | |
| B32 | G08d | Lịch ngày mai (d) | EDIT G08 | handoff · G01–G12 | |
| B33 | N01 | Thử lời nhắc | NEW | handoff · N01–N21 | |
| B34 | N04 | Chọn việc đầu tiên | NEW | handoff · N01–N21 | |
| B35 | N07 | Cài đặt nhắc việc | NEW | handoff · N01–N21 | |
| B36 | N08 | Cách dùng đơn giản | NEW | handoff · N01–N21 | |
| B37 | N02 | Đã nhận lời nhắc | EDIT N01 | handoff · N01–N21 | |
| B38 | N03 | Chưa nhận lời nhắc | EDIT N02 | handoff · N01–N21 | |
| B39 | N05 | Xem lại việc đầu tiên | EDIT N04 | handoff · N01–N21 | |
| B40 | N20 | Dữ liệu trên điện thoại | EDIT N07 | handoff · N01–N21 | |

**Đợt gợi ý:** chạy B01 trước rồi mở ảnh so với `stitch-runs/S03/v3.png`. Nếu khác phong cách nhiều (màu, cỡ chữ, bo góc) thì báo Sanh trước khi chạy tiếp. Sau đó chạy B02 – B08, B17 – B20, B33 – B36 (màn gốc) → các khung `EDIT`.

Các khung `(b)`, `(c)`, `(d)` của G: xem đúng nội dung trong frame Figma cùng tên, ghi vào prompt trace.

---

## 5. Làn C – làm trong Figma (3 khung)

Biến thể `S04 ·`, `S11 ·`, `S16 ·`, `S17 ·` (chi tiết từng việc, từng thói quen, từng người thân) chỉ khác chữ. Duplicate frame chốt của S04 / S11 / S16 / S17 trong Figma rồi sửa chữ, khỏi tốn quota Stitch. Trước khi làm, đếm lại trong page `03 Final UI` xem còn những frame nào chưa có trong làn A, B (tổng 3 làn phải bằng 88).

---

## 6. Xong hết thì

- [ ] `SUMMARY.md` không còn dòng `chưa chạy` / `đang dở`; mọi `NEEDS_HUMAN` đã ghi quyết định vào `design-decisions.md`
- [ ] Export màn chốt của từng khung từ Stitch sang Figma (page mới, giữ tên frame đúng mã)
- [ ] Nối prototype theo mục 15 của `ux/user-flow.md` (4 flow starting point)
- [ ] Export PNG 2x vào `assets/figma/`, cập nhật link prototype trong `README.md`
