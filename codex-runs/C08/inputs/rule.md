# rule.md – Luật thiết kế An Nhiên (dùng cho Critic Agent)

File này là "luật chơi" mà Critic Agent đọc mỗi vòng để phản biện output của Google Stitch.
Nguồn: `assets/stitch/DESIGN.md` (token), `assets/stitch/AppStyleGuide.md` (câu chữ, cư xử – mã `SG-xx`), `assets/stitch/PRD.md` (yêu cầu), `accessibility.md` và góp ý của thầy (`ai/feedback-thay-2026-10-16.md`). Sửa luật ở đây → vòng sau agent áp dụng ngay. Agent chạy vòng lặp bằng lệnh `/stitch-loop` trong Claude Code (xem `.claude/commands/stitch-loop.md`).

Quy ước:
- **ID** để agent trích dẫn khi báo lỗi (vd. `R-TXT-01`).
- **Mức**: `error` = chặn, phải sửa mới được qua vòng; `warn` = nên sửa, không chặn.
- **Kiểm**: `auto` = đo được bằng số trong HTML của Stitch (class Tailwind, px, mã màu → tính contrast, đếm chữ); `ai` = đánh giá bằng mắt từ ảnh chụp.
- **Đếm chữ** theo *tiếng* (âm tiết, tách bằng dấu cách): "Nhắc lại sau 10 phút" = 5 tiếng.

## Bối cảnh người dùng

Bà Lan, 68 tuổi, giáo viên về hưu, viễn thị, ngón tay kém linh hoạt, chỉ quen Zalo và YouTube, hay quên giờ ăn và giờ đi bộ.
App: **An Nhiên** – lịch sinh hoạt theo 9 thói quen Power 9 (Blue Zones). Android, khung 360 × 800 dp.

## 1. Đọc được ngay

| ID | Luật | Mức | Kiểm |
| --- | --- | --- | --- |
| R-TXT-01 | Mọi chữ hiển thị ≥ 20 px (kể cả nhãn bottom nav, chú thích, chip) | error | auto |
| R-TXT-02 | Chữ nội dung chính ≈ 24 px; tiêu đề màn ≈ 30 px; chữ trên nút ≈ 22 px | warn | ai |
| R-CON-01 | Tương phản chữ ≥ 4.5 : 1 (chữ lớn ≥ 24 px hoặc ≥ 18.67 px đậm: ≥ 3 : 1) | error | auto |
| R-CON-02 | Viền ô nhập / control, ô icon màu nhấn ≥ 3 : 1 so với nền | warn | auto |
| R-LAY-01 | Không tràn ngang ở 360 px (không có thanh cuộn ngang, không chữ bị cắt) | error | auto |

## 2. Ít chữ, nhiều icon *(góp ý của thầy: "ít chữ", "dùng icon nhiều")*

Icon thay cho câu giải thích, **không** thay cho nhãn: icon luôn đi kèm 1 nhãn ngắn (R-ICON-01).

| ID | Luật | Mức | Kiểm |
| --- | --- | --- | --- |
| R-TXT-03 | Không câu nào dài hơn 15 tiếng; không đoạn văn quá 2 dòng | error | auto |
| R-TXT-04 | Nhãn nút ≤ 5 tiếng; nhãn tab ≤ 3 tiếng; tên thói quen ≤ 4 tiếng (theo `vocabulary.md`) | error | auto |
| R-TXT-05 | Thẻ việc chỉ gồm: icon thói quen · giờ · tên việc · nhãn trạng thái; tối đa 1 dòng phụ | error | ai |
| R-TXT-06 | Không có khối chữ giải thích / lời khuyên trên màn Hôm nay; giải thích để ở màn chi tiết (sau nút "Đọc to") | warn | ai |
| R-ICON-02 | Mọi việc, mọi thói quen, mọi nút hành động chính, mọi tab và mọi mục cài đặt đều có icon | error | ai |
| R-ICON-03 | Icon quen thuộc, cụ thể (chuông, điện thoại, lịch, lá, người…), ≥ 32 px; một icon chỉ mang một nghĩa trong toàn app (theo Từ điển icon trong `assets/stitch/DESIGN.md`). **Ngoại lệ:** icon nằm trong chip trạng thái ("✓ Đã xong", "○ Chưa làm", "Đã bỏ qua") được ≥ 24 px, vì luôn có chữ đi kèm | warn | ai |

## 3. Màu sắc bắt mắt *(góp ý của thầy: "màu sắc bắt mắt")*

Màu nhấn đặt ở **mảng nhỏ** (ô icon, viền, nhãn trạng thái); nền app và chữ giữ tương phản cao.

| ID | Luật | Mức | Kiểm |
| --- | --- | --- | --- |
| R-COL-02 | Mỗi thẻ việc / thói quen có **ô icon nền màu nhấn** của thói quen (`habit-*-accent`, icon trắng) và **vạch màu bên trái** cùng màu | error | ai |
| R-COL-03 | 9 thói quen dùng đúng 9 màu nhấn trong DESIGN.md, không tự chế màu; cùng thói quen cùng màu ở mọi màn | warn | auto |
| R-COL-04 | Màu nhấn không dùng làm nền cho chữ dài; không neon, không gradient, không nền tối | warn | ai |
| R-COL-01 | Không dùng màu làm tín hiệu duy nhất (trạng thái luôn có icon + chữ) | error | ai |

## 4. Chạm trúng ngay

| ID | Luật | Mức | Kiểm |
| --- | --- | --- | --- |
| R-TAP-01 | Mọi vùng chạm ≥ 48 × 48 px | error | auto |
| R-TAP-02 | Nút hành động chính cao ≥ 60 px, rộng gần hết chiều ngang (lề 20), đặt ở đáy màn | error | ai |
| R-TAP-03 | Hai nút kề nhau cách nhau ≥ 8 px (cặp nút lời nhắc ≥ 20 px) | warn | ai |

## 5. Không phải đoán

| ID | Luật | Mức | Kiểm |
| --- | --- | --- | --- |
| R-ICON-01 | Mọi nút có icon đều có chữ nhìn thấy được (không có nút chỉ-icon) | error | auto |
| R-NAV-01 | Bottom nav đúng 4 tab có icon + nhãn: Hôm nay · Lịch tuần · Thói quen · Gia đình | error | ai |
| R-NAV-02 | Nút Back ghi chữ "Quay lại" hoặc tên màn trước, không chỉ có mũi tên | error | ai |
| R-GES-01 | Không có hành động chỉ làm được bằng vuốt / kéo / nhấn giữ; mọi việc làm bằng chạm | error | ai |

## 6. Nhìn vào là biết làm hay chưa làm *(góp ý của thầy)*

| ID | Luật | Mức | Kiểm |
| --- | --- | --- | --- |
| R-STA-01 | Mỗi việc hiện 1 trong 5 nhãn, đặt cạnh tên việc: **✓ Đã xong** (chip xanh đậm, chữ trắng) · **○ Chưa làm** (viền vàng đậm) · **🔔 Đến giờ** · **↻ Đã dời** · **✕ Bỏ qua** | error | ai |
| R-STA-02 | Tiến độ ngày ghi bằng chữ "Đã xong 3/6 việc"; không phần trăm, không vòng tròn không nhãn | warn | ai |

## 7. Một việc mỗi màn, bố cục

| ID | Luật | Mức | Kiểm |
| --- | --- | --- | --- |
| R-ONE-01 | Tối đa 1 nút filled (nền đậm) trên một màn; các nút khác là viền/tonal/text | error | ai |
| R-ONE-02 | Màn Hôm nay: khối "Việc tiếp theo" là điểm nhấn duy nhất | warn | ai |
| R-CEN-01 | **Căn giữa** nội dung đứng một mình (lời nhắc, hộp hỏi lại, màn trống, màn kết quả, chọn cỡ chữ); **căn trái** danh sách và form | warn | ai |

## 8. Không sợ sai

| ID | Luật | Mức | Kiểm |
| --- | --- | --- | --- |
| R-SAFE-01 | Hành động khó đảo ngược (xóa, đánh dấu xong, ngưng lặp) phải có bước xác nhận hoặc "Hoàn tác" | warn | ai |
| R-SAFE-02 | Lỗi nhập có icon + câu giải thích + ví dụ; không chỉ đổi màu viền | warn | ai |

## 9. Giọng đọc *(góp ý của thầy: "Voice")*

| ID | Luật | Mức | Kiểm |
| --- | --- | --- | --- |
| R-VOI-01 | Lời nhắc (S14), chi tiết việc (S04), chi tiết thói quen (S16), gợi ý từ người thân (G03) có nút "🔊 Đọc to" có chữ | error | ai |

## 10. Lời lẽ

| ID | Luật | Mức | Kiểm |
| --- | --- | --- | --- |
| R-LANG-01 | 100 % chữ trên UI là tiếng Việt có dấu; không sót tiếng Anh (Today, Done, Settings…) | error | ai |
| R-LANG-02 | Xưng hô thống nhất một kiểu (Bác / Ông / Bà) trên cả màn; câu đời thường; nút là động từ + việc, không "OK / Có / Không" | warn | auto |
| R-LANG-03 | Không bảng xếp hạng, mất streak, điểm sức khỏe, điểm tuổi thọ, lời lẽ gây áp lực | error | ai |
| R-VOC-01 | Không có từ trong cột "Tránh dùng" của `vocabulary.md` (task, notification, sync, streak, Down Shift…) | error | auto |

## 11. Phong cách (design tokens)

| ID | Luật | Mức | Kiểm |
| --- | --- | --- | --- |
| R-STY-01 | Nền `#F6F7F2`, thẻ `#FFFFFF`, chữ chính `#202B25`, chữ phụ `#526057`, primary `#1F684B`, lỗi `#B42318`; 9 màu nhấn thói quen theo `assets/stitch/DESIGN.md` | warn | auto |
| R-STY-02 | Font Be Vietnam Pro; không gradient; card bo 16, nút bo 14 | warn | ai |
| R-STY-03 | Lề màn 20 px; khoảng cách giữa các khối 16 px | warn | ai |

## Điều kiện dừng vòng lặp

Không dùng ngưỡng điểm cố định. Vòng lặp chạy tới khi điểm Critic không tăng nữa:

1. Điểm mỗi vòng = 100 − 10 × số `error` − 3 × số `warn` (xem `.claude/agents/stitch-critic.md`).
2. Giữ **màn tốt nhất** (điểm cao nhất tới giờ). Vòng nào tụt điểm thì vòng sau sửa tiếp từ màn tốt nhất.
3. Dừng khi 2 vòng liên tiếp không vượt điểm tốt nhất, hoặc điểm = 100 → **CONVERGED**. Chốt an toàn: tối đa v8 → **MAX_ROUNDS**.
4. Màn chốt là màn tốt nhất. Nếu màn đó vẫn còn vi phạm mức `error` → **needs-human** (con người quyết định, ghi vào design-decisions.md).

Cơ sở: luật dừng "không cải thiện sau N lần thì dừng" là early stopping với patience = 2 (Prechelt, *Early Stopping – But When?*, 1998). Vòng lặp tự phản biện – tự sửa theo Self-Refine (Madaan và cs., NeurIPS 2023), bài này ghi nhận lợi ích giảm dần qua các vòng. Cách trừ điểm theo mức nặng của lỗi tương tự điểm accessibility của Lighthouse (trọng số theo mức ảnh hưởng).
