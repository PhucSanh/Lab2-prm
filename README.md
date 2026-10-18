# An Nhiên – Lịch sống khỏe Power 9 cho người cao tuổi

**PRM393 · Laboratory 2 – AI-Assisted UI/UX Design (Google Stitch → Figma)**

| | |
| --- | --- |
| Sinh viên | Nguyễn Phúc Sanh – [MSSV] |
| Lớp | [LỚP] |
| Figma (view) | <https://www.figma.com/design/I75QlC0NIky5xHUmvVsZGE/An-Nhi%C3%AAn---Power-9> – quyền "Anyone with the link can view" |
| Prototype | <https://www.figma.com/proto/I75QlC0NIky5xHUmvVsZGE/An-Nhien---Power-9?node-id=1-3567&starting-point-node-id=1%3A3567> |
| Slide trình bày (Canva) | <https://www.canva.com/d/qp8aOv9aMMjP56i> – "An Nhiên — Product Pitch & UX Case Study" |
| Persona & user story (Docs) | <https://docs.google.com/document/d/1tloaM4YAa41kd8M1Y_5OC13CzmFxflQT3P5mOHSw9oA/edit?tab=t.sq7qua9dzk7e> |
| GitHub | [DÁN LINK REPO] |
| Nền tảng | Android, khung thiết kế 360 × 800 dp (kiểm tra thêm 412 dp) |

## Vấn đề

Người 65+ muốn duy trì thói quen sống khỏe mỗi ngày nhưng hay quên giờ ăn, giờ vận động. Các app lịch hiện có thì chữ nhỏ, icon không có chữ và quá nhiều bước, nên họ bỏ dở sau vài ngày. Con cháu ở xa muốn giúp sắp lịch nhưng không muốn "quản" bố mẹ.

**An Nhiên** sắp xếp một ngày sinh hoạt theo 9 thói quen **Power 9** của những vùng sống thọ nhất thế giới (Blue Zones). Ứng dụng dùng chữ to (nội dung 24, nhỏ nhất 20), nút chính cao 60 dp, mỗi màn chỉ có một việc chính và mọi lỗi đều có đường quay lại. Người thân chỉ **gợi ý** lịch; người lớn tuổi luôn là người chọn nhận hay bỏ qua.

## Bản đồ deliverable → rubric

| Tiêu chí rubric | Điểm | Artifact trong repo | Vị trí trong Figma |
| --- | ---: | --- | --- |
| UX analysis & user flows | 15 | [ux/persona.md](ux/persona.md), [ux/user-flow.md](ux/user-flow.md) | Page `01 User Flow` (Flow 1 – 12) |
| AI UI generation | 10 | [DESIGN.md](DESIGN.md), [ai/ai-design-log.md](ai/ai-design-log.md) (v0), `assets/stitch/` (4 màn + bảng màu) | — |
| AI iterations & UX critique | 15 | [ai/ai-design-log.md](ai/ai-design-log.md) (V1–V3, 9 phát hiện F1–F9), [design-decisions.md](design-decisions.md) | — |
| Final UI/UX design | 20 | [design-decisions.md](design-decisions.md), `assets/figma/` | Page `02 Wireframe`, `03 Final UI` (frame `START HERE` ở trên cùng) |
| Design system & components | 15 | [DESIGN.md](DESIGN.md) (tokens) | Page `04 Design System`, `05 Components` |
| Interactive prototype | 10 | [ux/user-flow.md](ux/user-flow.md) (flow → frame) | Page `06 Prototype` – 4 flow starting point (main flow + 3 flow demo) |
| Flutter handoff | 10 | [flutter-handoff.md](flutter-handoff.md) | — |
| Documentation & AI log | 5 | README này, [accessibility.md](accessibility.md) | — |

## Phạm vi trong Figma

Page `03 Final UI` có **105 màn / biến thể / popup** (không tính các frame ẩn có tiền tố `[Bản trước]` – bản cũ, không dùng để chấm hay bàn giao). Chia 5 nhóm:

| Nhóm | Mã | Vai trò |
| --- | --- | --- |
| Màn chính (người lớn tuổi) | S01 – S17 | Luồng dùng hằng ngày của bà Lan |
| State / dialog / biến thể | ST-*, DLG-*, S03-*, S11 · *, S04 · *, S16 · *, S17 · * | Lỗi, đang lưu, đã lưu, snackbar Hoàn tác, chi tiết từng việc, từng thói quen, từng người thân |
| MVP bổ sung | N01 – N21, DLG-WakeTime, DLG-TaskTime | Thử lời nhắc, việc đầu tiên, sửa hồ sơ, nhắc việc, hỗ trợ, sửa/xóa người thân, chia sẻ trung thực, chọn ngày/lặp, phạm vi sửa/xóa, rời form, dữ liệu trên máy |
| Gợi ý lịch từ người thân | G01 – G12 | Mai gửi gợi ý → Bác tự nhận / đổi giờ / chọn từng việc / bỏ qua |
| Chế độ Người thân | C01 – C12 | Con cháu ghép nối với máy của mẹ, xem lịch ngày/tuần/tháng, lập lịch lặp, sửa/ngưng |

### Màn chính (S01 – S17)

| ID | Màn hình | Tab / cấp |
| --- | --- | --- |
| S01 | Chào mừng – chọn cỡ chữ | Onboarding |
| S02 | Thiết lập hồ sơ (Bước 1/2) – tên gọi, xưng hô Ông/Bà, giờ thức dậy | Onboarding |
| S13 | Cho phép nhắc việc (Bước 2/2) | Onboarding |
| S03 | Hôm nay (Home) | Tab 1 |
| S04 | Chi tiết hoạt động | Con của S03 / S11 |
| S15 | Sửa việc | Con của S04 |
| S05 | Thêm việc – chọn hoạt động | Con của S03 |
| S06 | Thêm việc – thiết lập (tên, giờ, ngày, lặp, nhắc) | Con của S05 |
| S07 | Lịch tuần | Tab 2 |
| S11 | Chi tiết ngày | Con của S07 |
| S08 | Hoạt động mỗi ngày (9 thói quen Power 9) | Tab 3 |
| S16 | Chi tiết thói quen (× 9) | Con của S08 |
| S09 | Gia đình | Tab 4 |
| S12 | Thêm người thân | Con của S09 |
| S17 | Nhắn tin cho người thân | Con của S09 |
| S10 | Cài đặt hiển thị | Từ app bar S03 |
| S14 | Lời nhắc đến giờ (toàn màn hình) | Mở từ thông báo; xem thử từ S10 |

State và dialog: `ST-Empty`, `S13d`, `ST-Validation`, `S06e`, `S06o`, `ST-Loading`, `ST-Loading-offline`, `ST-Error`, `ST-Saved`, `S03b`, `S03-later` / `S03-later4` / `S03-tomorrow` / `S03-skip` / `S03-edited` / `S03-deleted` / `S03-snooze` / `S03-alldone`, `S11b`, `S12a`, `S12e`, `S09b`, `S17b`, `DLG-Done`, `DLG-Later`, `DLG-Skip`, `DLG-Delete`, `DLG-WakeTime`, `DLG-TaskTime`.

### MVP bổ sung (N01 – N21)

N01 Thử lời nhắc · N02 Đã nhận lời nhắc · N03 Chưa nhận lời nhắc · N04 Chọn việc đầu tiên · N05 Xem lại việc đầu tiên · N06 Sửa hồ sơ · N07 Cài đặt nhắc việc · N08 Cách dùng đơn giản (nhờ người thân hỗ trợ) · N09 Sửa người thân · N10 Đã mở ứng dụng chia sẻ · N11 Chọn ngày · N12 Lặp lại · N13 Phạm vi thay đổi · N14 Chưa lưu thay đổi · N15 Xóa người thân · N16 Đã lưu · nhắc cần kiểm tra · N17 Hôm nay · đã xử lý hết · N18 Đã lưu việc đầu tiên · N19 Hôm nay · việc đầu tiên · N20 Dữ liệu trên điện thoại · N21 Gia đình sau khi xóa người thân.

### Gợi ý lịch từ người thân (G01 – G12)

G01 / G01b Con cháu soạn lịch gợi ý · G02 Đã gửi gợi ý · G03 / G03b Lịch Mai gợi ý · G04 Đổi giờ · G05 / G05b Đã nhận · G06 Chọn từng việc · G07 / G07b Đã nhận một việc · G08 – G08d Lịch ngày mai · G09 Đã bỏ qua gợi ý · G10 Có gợi ý mới (tự hiện) · G11 Popup "Mai gửi lịch cho Bác" · G12 Để sau → gợi ý nằm ở đầu trang Hôm nay.

### Chế độ Người thân (C01 – C12)

C01 Chọn vai trò · C02 Nhập mã ghép nối · C02e Mã sai / hết hạn · C03 Lịch của mẹ · Ngày · C04 · Tuần · C05 · Tháng · C06 Thông tin việc (Bước 1/3) · C06e Thiếu tên / giờ · C07 Lặp lại mỗi tuần (Bước 2/3) · C07m Lặp lại mỗi tháng · C08 Xem lại & gửi (Bước 3/3) · C08w Trùng giờ (overlay) · C09 Đã gửi · chờ mẹ nhận · C10 Chi tiết việc lặp lại · C11 Áp dụng thay đổi cho (overlay) · C12 Ngưng lịch lặp (overlay).

## Prototype (page `06 Prototype`)

| Flow starting point | Bắt đầu tại | Nội dung |
| --- | --- | --- |
| ★ Main flow – Một ngày của bà Lan (đi hết app) | S01 Chào mừng | 24 bước qua toàn bộ màn chính |
| Flow chính 1 – Khám phá: thêm việc hợp sở thích (Flow 8 + 2) | S08 | Thói quen → chi tiết → thêm việc |
| Flow chính 2 – Lời nhắc: làm xong việc đúng giờ (Flow 6 + 3) | S14 | Lời nhắc → làm → xác nhận / dời / bỏ qua |
| Flow chính 3 – Gia đình: người thân lập lịch cho mẹ (Flow 11) | C03 | Con cháu lập lịch lặp và gửi cho mẹ |

## Cấu trúc repo

```
prm393-lab2-an-nhien/
├─ README.md               # file này
├─ DESIGN.md               # prompt Stitch gốc, design tokens, style
├─ design-decisions.md     # accept / modify / reject + lý do
├─ accessibility.md        # checklist contrast, touch target, 360/412 dp
├─ flutter-handoff.md      # đặc tả từng màn + 2 bảng mapping
├─ ux/
│  ├─ persona.md           # bối cảnh, phỏng vấn AI, P1–P4, nhân vật kịch bản
│  └─ user-flow.md         # IA + 12 flow (Mermaid) + ánh xạ flow–screen
├─ ai/
│  └─ ai-design-log.md     # v0 Stitch + 3 vòng tinh chỉnh, phản biện F1–F9
└─ assets/
   ├─ stitch/              # output Google Stitch gốc (screen_day, screen_week, power9, screen_contact, bang_mau)
   ├─ figma/               # ảnh export từ Figma
   ├─ a11y/                # ảnh kiểm tra contrast, 360 vs 412 dp
   └─ icons/               # icon Lucide (ISC) dùng trong slide
```

## Ghi chú

- Lab 2 không yêu cầu code Flutter; `flutter-handoff.md` là đặc tả để hiện thực ở các lab sau.
- Mọi ảnh trong `assets/stitch/` là output thật của Google Stitch, giữ nguyên, không chỉnh sửa.
- Slide Canva là bản trình bày; số liệu chi tiết nằm trong repo này và Figma.
- Figma là nguồn chuẩn. Khi Figma và tài liệu lệch nhau, sửa tài liệu theo Figma (đồng bộ gần nhất: 15/10/2026).
- Trước khi nộp: mở link Figma và GitHub bằng cửa sổ ẩn danh để kiểm tra quyền xem.
