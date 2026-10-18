---
description: Sinh 1 màn bằng Google Stitch, tự phản biện theo rule.md và bắt Stitch sửa tới khi điểm không tăng nữa
argument-hint: <mã màn + tên, vd "S03 Hôm nay"> [--resume] [--from <mã màn gốc>]
---

Màn cần làm: **$ARGUMENTS**

Bạn là agent điều phối (orchestrator) của dự án An Nhiên. Chạy vòng lặp Generate → Critique → Edit: bạn viết prompt và gọi Stitch MCP; việc chấm giao cho subagent `stitch-critic`. Làm đúng thứ tự, không dừng lại hỏi trừ khi Stitch báo lỗi.

## 0. Chuẩn bị
- Đọc 4 file input trong `assets/stitch/`: `PRD.md` (mục 11 – bối cảnh và nội dung màn),
  `DESIGN.md` (token), `AppStyleGuide.md` (câu mẫu, xưng hô), `vocabulary.md` (tên thói quen, từ tránh).
- Đọc `rule.md` (luật mức `error` đưa vào prompt).
- Thư mục làm việc: `stitch-runs/<mã màn>/` (vd. `stitch-runs/S03/`).
- Stitch project: nếu có `stitch-runs/project.txt` thì dùng id trong đó; nếu chưa có thì `create_project` tên "An Nhiên" và lưu id vào file đó.

## 0b. Chế độ chạy tiếp (`--resume`)
Nếu tham số có `--resume`: **không sinh lại v0**, bỏ qua mục 1, sửa tiếp từ màn tốt nhất đã có.
- Đọc `stitch-runs/<mã>/` lấy vòng cuối K (file `vK-critique.json` có số lớn nhất) và **screen id** của màn đó: tìm trong `log.md`, rồi `run.txt`. Không thấy thì gọi `list_screens` của project, lấy màn có tiêu đề khớp tên màn và ảnh khớp `vK.png`. Vẫn không chắc → dừng và hỏi người dùng, không đoán.
- **Chấm lại theo luật hiện tại:** luật và Từ điển icon có thể đã đổi, nên gọi `stitch-critic` chấm lại `vK.png`, `vK.html`, ghi đè `vK-critique.json` (giữ bản cũ thành `vK-critique.old.json`). Điểm này là điểm tốt nhất ban đầu, bộ đếm "không tăng" = 0.
- Trong `log.md` thêm mục `## Chạy tiếp từ vK (luật mới)` với điểm chấm lại.
- Nếu chấm lại đã 100 → dừng, kết quả **CONVERGED**. Nếu chưa, làm bước 2f (viết edit prompt từ `vK-critique.json`, sửa trên screen id vừa tìm) rồi vào vòng N = K + 1 như bình thường. Chốt an toàn v8 tính tiếp theo số vòng.

## 0c. Biến thể (`--from X`)
Nếu tham số có `--from X`: màn này là **biến thể của màn X** (cùng khung, khác trạng thái hoặc nội dung), không sinh v0 bằng `generate_screen_from_text`.
- X phải đã chạy xong: `stitch-runs/X/log.md` có dòng `Kết quả:`. Chưa có → ghi `**Kết quả: NEEDS_HUMAN** – chờ màn gốc X` vào log của màn này rồi dừng.
- Lấy **screen id màn chốt của X**: dòng `Màn chốt` trong `stitch-runs/X/log.md`, rồi `stitch-runs/X/run.txt`. Không thấy thì `list_screens` của project, lấy màn có tiêu đề khớp X và ảnh khớp `vK.png` của màn chốt. Vẫn không chắc → NEEDS_HUMAN, không đoán.
- Nội dung màn: dòng của màn ở `PRD.md` 11.2 nếu có; nếu không, lấy theo cột Nguồn trong `stitch-runs/CHIA-VIEC.md` (`flutter-handoff.md`, `ux/user-flow.md`). Câu chữ vẫn theo `AppStyleGuide.md`, `vocabulary.md`.
- Viết `v0-prompt.txt` dạng edit prompt tiếng Anh: dòng đầu `Keep the overall layout, header, bottom navigation, colors and typography of this screen unchanged. Turn it into the following variant.`, rồi liệt kê đánh số phần khác với X (có số đo, chữ tiếng Việt trong ngoặc kép), kèm khối ICONS cho icon mới và các luật `error` của `rule.md` liên quan. Ghi `v0-prompt-trace.md` (ghi rõ "biến thể của X, screen id ...").
- Gọi `edit_screens` trên screen id màn chốt của X. Màn trả về là v0 của màn này; ghi screen id vào `log.md` (dòng `screen id: ...`). Không sửa thư mục `stitch-runs/X/`.
- Sang mục 2 như bình thường (critic chấm, lặp). Các vòng sau sửa trên màn của chính biến thể này, không quay về X.

## 1. v0 – sinh màn
- Viết prompt tiếng Anh CHỈ cho màn này; chữ trên UI bằng tiếng Việt có dấu; đưa tất cả luật mức `error` của `rule.md` vào dưới dạng ràng buộc có số đo.
- Prompt ghép từ: `PRD.md` 11.1 (bối cảnh) + dòng của màn này ở `PRD.md` 11.2 + token `DESIGN.md`
  + câu mẫu `AppStyleGuide.md` mục 5 + tên thói quen `vocabulary.md` mục 1.
  + khối **ICONS** lấy từ `DESIGN.md` mục "Từ điển icon" (và cột Icon của `vocabulary.md` mục 1), viết dạng:
    ```
    ICONS: Use only the Lucide icon set (outline, stroke 2-2.5). Never draw custom icons.
    Every icon renders at least 32x32px and its glyph fills the box (habit tiles: 48x48 tile, 32px white icon).
    Use exactly these icons and never reuse one icon for another meaning:
    <mỗi icon màn này dùng: lucide-name = nghĩa, kèm ghi chú "only ..." nếu bảng có chữ Chỉ>
    ```
    Chỉ liệt kê các icon màn này cần. Mỗi chỗ có icon trong phần LAYOUT phải ghi đúng tên Lucide (vd. `bell-ring icon 32px`), không tả chung chung kiểu "leaf icon", "people icon". Nghĩa nào chưa có trong từ điển thì thêm vào `DESIGN.md` trước rồi mới viết prompt.
- Lưu `v0-prompt.txt`, và `v0-prompt-trace.md` ghi mỗi đoạn prompt lấy từ file nào, mục nào.
- Gọi `generate_screen_from_text` với deviceType MOBILE.

## 2. Mỗi vòng N (bắt đầu N = 0)
a. **Lấy kết quả:** gọi `get_screen` lấy link screenshot và HTML; tải về `vN.png` và `vN.html` (`curl -L -o`). Link có hạn nên tải ngay.
b. **Kiểm tra file:** `vN.png` mở được và `vN.html` không rỗng. Việc đo và chấm do critic làm, bạn không tự chấm.
c. **Phản biện:** gọi subagent `stitch-critic`, chỉ đưa đường dẫn `vN.png`, `vN.html` (và `v(N-1)-critique.json` nếu có).
   KHÔNG đưa prompt cho critic. Đọc `vN-critique.json` nó trả về để lấy điểm, vi phạm, lỗi đã sửa và regression.
d. **Ghi log:** thêm vào `stitch-runs/<mã>/log.md` mục `## vN – điểm X` gồm ảnh `![vN](vN.png)`, bảng vi phạm (Luật · Mức · Vị trí · Bằng chứng · Sửa), đã sửa / regression.
e. **Điều kiện dừng (dừng khi điểm không tăng nữa, không có ngưỡng điểm cố định):**
   - Giữ **màn tốt nhất** = vòng có điểm cao nhất tới giờ (bằng điểm thì lấy vòng có ít `error` hơn, rồi vòng sau hơn). Ghi `best: vK – điểm X` vào log.
   - Vòng N có điểm **cao hơn** điểm tốt nhất → cập nhật màn tốt nhất, đặt lại bộ đếm "không tăng" = 0, chạy tiếp.
   - Vòng N có điểm **không cao hơn** điểm tốt nhất → bộ đếm "không tăng" + 1.
   - Dừng khi một trong các điều sau xảy ra:
     - Bộ đếm "không tăng" = 2 (2 vòng liên tiếp không vượt điểm tốt nhất) → **CONVERGED**.
     - Điểm = 100 (không thể tăng nữa) → **CONVERGED**.
     - Đã tới v8 (chốt an toàn để không cạn quota Stitch) → **MAX_ROUNDS**.
   - Khi dừng, nếu màn tốt nhất vẫn còn lỗi `error` → đổi kết quả thành **NEEDS_HUMAN** (ghi lý do, để người quyết định, ghi vào `design-decisions.md`).
f. **Nếu chưa dừng:** viết edit prompt tiếng Anh, giữ nguyên chữ tiếng Việt trong ngoặc kép:
   - Dòng đầu: `Keep the overall layout and everything not mentioned below unchanged.`
   - Tối đa 10 sửa đổi đánh số, lỗi `error` trước, mỗi dòng một thay đổi cụ thể có số đo (px, hex, tên phần tử), lấy từ các mục `fix` trong `vN-critique.json`. Sửa icon thì ghi đúng tên Lucide theo Từ điển icon trong `DESIGN.md`.
   - Lưu vào `vN-edit-prompt.txt` và chép nguyên văn vào log, rồi gọi `edit_screens`. Sửa trên **màn tốt nhất** (nếu vòng N bị tụt điểm thì quay về màn tốt nhất và dùng `fix` trong critique của màn đó, không sửa chồng lên bản bị tụt). Lấy màn mới trả về, sang vòng N+1.

## 3. Kết thúc
- Ở đầu `log.md` thêm bảng tóm tắt: Vòng · Điểm · Số error · Số warn · Đã sửa · Regression, dòng **Màn chốt: vK – điểm X** (màn tốt nhất, không nhất thiết là vòng cuối) và dòng **Kết quả: CONVERGED / NEEDS_HUMAN / MAX_ROUNDS**.
- Trả lời ngắn gọn: điểm từng vòng, màn chốt, kết quả, các lỗi còn lại (nếu có), nhắc mở Stitch để export **màn chốt** sang Figma.

## Lưu ý
- Nếu Stitch timeout: gọi `list_screens` kiểm tra màn đã được tạo chưa trước khi gọi lại, để không sinh trùng và tốn quota.
- Dùng đúng project id / screen id mà tool trả về, không tự chế.
- Nếu Stitch hỏi lại (clarification): tự trả lời theo `rule.md` và `assets/stitch/DESIGN.md`, đừng hỏi người dùng.
