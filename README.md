# An Nhiên – Lịch sống khỏe Power 9 cho người cao tuổi

**PRM393 · Laboratory 2 – AI-Assisted UI/UX Design (Google Stitch → Figma)**

| | |
| --- | --- |
| Sinh viên | Nguyễn Phúc Sanh – [MSSV] |
| Lớp | [LỚP] |
| Figma (view) | [DÁN LINK FIGMA – quyền "Anyone with the link can view"] |
| GitHub | [DÁN LINK REPO] |
| Nền tảng | Android, khung thiết kế 360 × 800 dp (kiểm tra thêm 412 × 917 dp) |

## Vấn đề

Người 65+ muốn duy trì thói quen sống khỏe mỗi ngày nhưng hay quên giờ ăn, giờ vận động. Các app lịch hiện có thì chữ nhỏ, icon không có chữ và quá nhiều bước, nên họ bỏ dở sau vài ngày.

**An Nhiên** sắp xếp một ngày sinh hoạt theo 9 thói quen **Power 9** của những vùng sống thọ nhất thế giới (Blue Zones). Ứng dụng dùng chữ to, nút to, mỗi màn chỉ có một việc chính và mọi lỗi đều có đường quay lại.

## Bản đồ deliverable → rubric

| Tiêu chí rubric | Điểm | Artifact trong repo | Vị trí trong Figma |
| --- | ---: | --- | --- |
| UX analysis & user flows | 15 | [ux/persona.md](ux/persona.md), [ux/user-flow.md](ux/user-flow.md) | Page `01 User Flow` |
| AI UI generation | 10 | [DESIGN.md](DESIGN.md), [ai/ai-design-log.md](ai/ai-design-log.md) (v0), `assets/stitch/` | — |
| AI iterations & UX critique | 15 | [ai/ai-design-log.md](ai/ai-design-log.md) (V1–V3, ≥5 phát hiện) | — |
| Final UI/UX design | 20 | [design-decisions.md](design-decisions.md), `assets/figma/` | Page `02 Wireframe`, `03 Final UI` |
| Design system & components | 15 | [DESIGN.md](DESIGN.md) (tokens) | Page `04 Design System`, `05 Components` |
| Interactive prototype | 10 | [ux/user-flow.md](ux/user-flow.md) (flow → frame) | Page `06 Prototype` |
| Flutter handoff | 10 | [flutter-handoff.md](flutter-handoff.md) | — |
| Documentation & AI log | 5 | README này, [accessibility.md](accessibility.md) | — |

## Danh sách màn hình (10 màn + 6 state)

| ID | Màn hình | Tab / cấp |
| --- | --- | --- |
| S01 | Chào mừng – chọn cỡ chữ | Onboarding |
| S02 | Thiết lập hồ sơ | Onboarding |
| S03 | Hôm nay (Home) | Tab 1 |
| S04 | Chi tiết hoạt động | Con của S03 |
| S05 | Thêm việc – chọn thói quen | Con của S03 |
| S06 | Thêm việc – chọn giờ | Con của S05 |
| S07 | Lịch tuần | Tab 2 |
| S08 | 9 thói quen Power 9 | Tab 3 |
| S09 | Gia đình | Tab 4 |
| S10 | Cài đặt hiển thị | Từ app bar S03 |

Các state và dialog (không tính vào 8 màn tối thiểu): `ST-Empty` (Home trống), `ST-Validation` (thiếu tên việc), `ST-Loading` (đang lưu), `ST-Error` (lưu thất bại), `ST-Saved` (đã lưu), `DLG-Done` (xác nhận đã xong – overlay).

## Cấu trúc repo

```
prm393-lab2-an-nhien/
├─ README.md               # file này
├─ DESIGN.md               # prompt Stitch gốc, design tokens, style
├─ design-decisions.md     # accept / modify / reject + lý do
├─ accessibility.md        # checklist contrast, touch target, 360/412 dp
├─ flutter-handoff.md      # 6 mục × mỗi màn + 2 bảng mapping
├─ ux/
│  ├─ persona.md
│  └─ user-flow.md         # IA + 3 flow (Mermaid) + ánh xạ flow–screen
├─ ai/
│  └─ ai-design-log.md     # v0 + 3 vòng lặp, ảnh trước/sau, phản biện
└─ assets/
   ├─ stitch/              # ảnh output Google Stitch THẬT
   ├─ figma/               # ảnh export từ Figma
   └─ a11y/                # ảnh kiểm tra contrast, 360 vs 412 dp
```

## Ghi chú

- Lab 2 không yêu cầu code Flutter; `flutter-handoff.md` là đặc tả để hiện thực ở các lab sau.
- Mọi ảnh trong `assets/stitch/` là output thật của Google Stitch, giữ nguyên, không chỉnh sửa.
- Trước khi nộp: mở link Figma và GitHub bằng cửa sổ ẩn danh để kiểm tra quyền xem.
