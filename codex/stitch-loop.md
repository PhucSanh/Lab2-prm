# Codex Stitch loop — An Nhiên

Đầu vào: mã màn + tên, tùy chọn `--resume`, `--from <mã>` hoặc `--import <thư mục lịch sử>`.
Workflow này do Codex thực thi bằng tool và reviewer độc lập; file Markdown không tự chạy tiến trình.
Đọc `codex.md` trước. Không gọi command hoặc sửa cấu hình của Claude.

## 0. Preflight

1. Đọc 4 nguồn `assets/stitch/{PRD,DESIGN,AppStyleGuide,vocabulary}.md`, `rule.md` và nội dung màn trong nguồn bàn giao nếu PRD chưa có.
2. Xác nhận có tool Stitch và có thể chạy subagent reviewer với context riêng. Nếu thiếu, ghi rõ thiếu gì và dừng trước generation. Setup ở `codex/setup.md`.
3. Kiểm tra schema của tool đang có; tên điển hình là `list_projects`, `create_project`, `list_screens`, `get_screen`, `generate_screen_from_text`, `edit_screens`. Dùng đúng tên/schema thật, không tự chế request.
4. Output: `codex-runs/<mã>/`. Chỉ một orchestrator được ghi thư mục màn đó tại một thời điểm. Nếu state đang running do phiên khác, không chạy trùng.
5. Project: dùng ID đã được xác minh trong `codex-runs/project.txt`; nếu chưa có, tạo project `An Nhiên — Codex` rồi lưu ID thật. Nếu timeout lúc tạo, list projects trước khi thử lại; không đoán project nếu có nhiều tên trùng.
6. Lưu snapshot luật/input vào thư mục run trước lượt chạy đầu để truy vết; khi resume mà nguồn đã đổi, giữ snapshot cũ, tạo snapshot mới có timestamp.

## 1. Khởi tạo hoặc chạy tiếp

### Màn mới

Viết `v0-prompt.txt` tiếng Anh; chữ trên UI bằng tiếng Việt có dấu.
Prompt ghép từ PRD mục 11 (bối cảnh + dòng màn), token DESIGN, câu mẫu AppStyleGuide, vocabulary và các luật error áp dụng cho màn.
Lưu `v0-prompt-trace.md`: mỗi khối prompt trích nguồn nào, mục nào.
Khối ICONS ghi tên Lucide cụ thể, ánh xạ đúng nghĩa từ từ điển, stroke 2–2.5; mặc định ≥32px, icon chip trạng thái được ≥24px theo luật hiện tại. Ghi tên icon cụ thể trong layout; không tự thêm icon/token vào nguồn chung.
Nếu cần nghĩa icon chưa có, ghi đề xuất vào `codex-runs/design-decisions.md`, trạng thái NEEDS_HUMAN.
Gọi generate cho MOBILE theo schema thực tế. Lưu ID màn được trả về.

### `--resume`

Chỉ tiếp tục lịch sử trong `codex-runs/<mã>/`. Nếu chưa có, báo cần `--import`; không tự ghi vào lịch sử Claude.
Dùng best_screen_id/best_round trong state và đối chiếu get_screen/log/critique. Không chọn vòng cuối thay cho vòng tốt nhất.
Nếu state thiếu, dựng lại từ các critique hợp lệ + ID trong log; nếu không xác minh được ID thì NEEDS_HUMAN, không đoán theo tên.
Chấm lại màn tốt nhất theo luật hiện tại bằng reviewer mới. Giữ critique cũ với hậu tố timestamp trước khi ghi kết quả mới; ghi rõ lý do chạy lại, reset patience=0.
Không sinh lại v0. Vòng mới dùng số kế tiếp chưa tồn tại; không ghi đè artifact cũ. Tới v8 thì dừng MAX_ROUNDS; không reset ngân sách bằng resume.

### `--from X` / `--import stitch-runs/X`

Đọc nguồn, kết quả, critique và screen ID đã xác minh; không sửa file nguồn. `--from` mặc định tra nguồn Codex, nguồn ngoài phải chỉ định rõ.
Nguồn chưa kết thúc hoặc không xác minh được screen ID → NEEDS_HUMAN.
Tạo bản sao/biến thể qua khả năng của tool và xác nhận trả về screen ID mới khác nguồn trước khi tiếp tục sửa. Nếu API không bảo đảm giữ nguyên nguồn, dừng và báo thiếu khả năng clone; không gọi edit có nguy cơ đổi màn nguồn.
`--from`: giữ khung, đổi nội dung/trạng thái theo PRD/bàn giao.
`--import`: giữ nội dung hiện tại, chạy lại review theo luật mới trên bản sao.
Lưu provenance nguồn, project ID/screen ID gốc và ID mới vào state/log. Không chuyển project tùy tiện nếu API không hỗ trợ clone khác project; báo rõ trở ngại.

## 2. Mỗi vòng N

### Gửi và đợi Stitch

Trước lệnh ghi, lưu state với `status=running`, round, parent screen, đường dẫn prompt và thời điểm gọi.
Lưu tool response đã bỏ token/header/URL có credential vào `vN-response.json` (nếu có signed URL, chỉ lưu metadata không chứa query xác thực).
Nếu trả job pending, lưu operation ID và dùng cơ chế status/poll được tool hỗ trợ, tránh gọi lại generation. Nếu response đồng bộ thì tiếp tục ngay khi hoàn tất.
Khi timeout: list/get để đối chiếu kết quả với project, parent, thời điểm; không generate/edit lại mù. Không chắc có thành công thì status=BLOCKED, ghi lý do rồi dừng.

### Xuất màn lên canvas ngay trong từng vòng

Sau khi Stitch trả màn hoàn tất, đưa chính màn của vòng N lên canvas project đang dùng trước khi bắt đầu review hoặc gọi sửa tiếp. Làm tới đâu thấy màn tới đó, không đợi chốt best mới xuất.
- Xác minh `get_project.screenInstances` có `sourceScreen` đúng ID màn vòng N. Tool trả screen ID hoặc tải được HTML chưa chứng minh đã xuất canvas.
- Nếu thiếu, thêm instance của màn mới; giữ nguyên mọi instance khác, đọc lại bố cục mới nhất trước ghi và dừng nếu phát hiện thay đổi đồng thời. Lưu snapshot trước/sau và đối chiếu.
- Nếu chưa xuất được, log `CANVAS_PENDING` với nguyên nhân; xử lý bàn giao vòng hiện tại trước khi sinh vòng kế tiếp. Không báo đã thấy trên UI nếu mới xác nhận membership qua API.
- Đặt các phiên bản cùng màn cạnh nhau trong vùng dành cho task, không đè hoặc di chuyển màn của task khác.
- Tên theo `An Nhiên - <Tên màn>`; bản sau có thể dùng hậu tố `(Cập nhật vN)` để phân biệt. Không thêm tên người/agent hoặc in hoa toàn bộ.
- Giữ mọi phiên bản v0,v1,... đã xuất, kể cả bản tụt điểm. Màn tốt nhất được chỉ rõ bằng ID trong log; không xóa màn cũ để chỉ còn màn chốt.
- Đây là xuất lên canvas Google Stitch. Xuất Figma vẫn là bước riêng khi người dùng yêu cầu.

### Thu artifact

Get screen lấy screenshot và HTML. Tải ngay thành `vN.png`, `vN.html`; kiểm tra HTTP thành công, ảnh mở được và HTML không rỗng/không phải trang lỗi.
Không sửa output Stitch để nâng điểm. Thiếu artifact → BLOCKED, không chấm và không tăng patience.
Ghi screen ID/project ID của chính vòng đó vào state/log trước khi review.

### Reviewer độc lập

Spawn reviewer mới, không kế thừa lịch sử prompt (ví dụ công cụ collaboration: `fork_turns="none"`; không chỉ định model trừ khi người dùng yêu cầu).
Chỉ cung cấp: đường dẫn hướng dẫn `codex/stitch-critic.md`, ảnh, HTML, các nguồn luật cần đọc, critique vòng trước nếu có, mã màn/vòng và đường dẫn output. Không truyền prompt generation/edit hoặc điểm mục tiêu.
Đợi reviewer ghi `vN-critique.json`. Không tự chấm thay reviewer. Nếu thiếu bằng chứng, thu bổ sung hoặc BLOCKED; không coi lỗi review là điểm 0 hay pass.
Kiểm tra JSON, đầy đủ ID luật đúng thứ tự rule.md, không trùng ID, level/check/status đúng, đếm fail và tính lại `max(0,100-10*errors-3*warns)`. Sai schema/số liệu thì yêu cầu reviewer sửa trước khi dùng.

### Log và chọn best

Ghi `log.md`: bảng vòng/điểm/error/warn/fixed/regressions, ảnh, ID màn, lỗi và bằng chứng, prompt sửa, nguồn snapshot.
Vòng đầu đặt best=v0 và patience=0; không tính v0 là một lần không cải thiện.
So điểm với best trước vòng hiện tại: cao hơn → patience=0; bằng/thấp hơn → patience+=1.
Best chọn điểm cao nhất; hòa điểm chọn ít error hơn, rồi vòng mới hơn. Khi hòa điểm đổi best, patience vẫn tăng.
Dừng khi score=100 hoặc patience=2 → CONVERGED; nếu N=8 và chưa hội tụ → MAX_ROUNDS.
Nếu màn best vẫn có error, kết quả cuối NEEDS_HUMAN (giữ stop_reason gốc). Ghi quyết định cần người dùng vào `codex-runs/design-decisions.md`.

### Prompt sửa

Nếu chưa dừng, lấy critique của best (không dùng lỗi của bản regression để sửa bản best).
Dòng đầu: `Keep the overall layout and everything not mentioned below unchanged.`
Tối đa 10 sửa đổi đánh số, error trước; mỗi sửa có số đo/token/câu chữ cụ thể từ fix; icon dùng đúng Lucide từ điển.
Lưu `vN-edit-prompt.txt` và chép nguyên văn vào log, gồm liên hệ từng thay đổi với rule ID và critique của best. Codex viết prompt sửa từ lỗi có bằng chứng; không để Stitch tự đổi nội dung tùy ý.
Gọi edit trên best_screen_id để sinh bản sửa mới. ID kết quả phải khác ID màn nguồn và các bản trước; xác minh trước khi chấp nhận vòng mới. Nếu tool sửa đè cùng ID hoặc không bảo đảm giữ nguồn, dừng để xử lý cơ chế tạo bản mới, không gọi tiếp chuỗi edit làm mất lịch sử.
Lưu parent ID và ID mới, xuất ngay bản mới lên canvas, thu artifact rồi reviewer mới chấm vòng N+1. Không bỏ qua review vì Stitch nói đã sửa xong.

## 3. State và khôi phục

`state.json` phải chứa ít nhất:

```json
{
  "screen": "S03",
  "status": "running",
  "project_id": null,
  "round": 0,
  "screen_id": null,
  "parent_screen_id": null,
  "best_round": null,
  "best_screen_id": null,
  "best_score": null,
  "patience": 0,
  "pending_operation_id": null,
  "stop_reason": null,
  "updated_at": null
}
```

Giá trị null chỉ dùng trước khi có dữ liệu thật. Bổ sung prompt path, snapshot và provenance khi có.
Ghi state bằng file tạm rồi rename để tránh JSON dở dang. Checkpoint sau tool response, tải artifact, review và chọn best.
Sau crash, đối chiếu pending operation và remote screen trước khi gọi ghi mới; không xem state running cũ là quyền chạy song song.
Nếu phát hiện session đang chạy thật, dừng. Nếu không rõ session cũ còn sống, yêu cầu người dùng xác nhận trước khi tiếp quản.

## 4. Kết thúc

State chuyển sang CONVERGED / MAX_ROUNDS / NEEDS_HUMAN / BLOCKED đúng thực tế.
Đầu log ghi `Màn chốt: vK`, điểm, best screen ID/project ID, `Kết quả:` và stop_reason.
Cập nhật `codex-runs/SUMMARY.md` riêng; không sửa SUMMARY của Claude.
Trả lời: điểm từng vòng, màn chốt, kết quả, lỗi còn lại và link/file log. Không tuyên bố đạt khi mới có prompt hoặc MCP config.

## Xác nhận bàn giao trên Stitch canvas

Generation/edit thành công chưa chứng minh screen xuất hiện trên canvas. Trước khi báo hoàn tất, kiểm tra get_project.screenInstances có sourceScreen của màn chốt. Nếu thiếu, xác định khả năng gắn canvas; chỉ thêm instance của màn được giao, giữ nguyên instance cũ, snapshot trước/sau và xác minh lại. Không thay toàn bộ canvas bằng danh sách chỉ có màn mới. Nếu không thể gắn, báo rõ review hoàn tất nhưng canvas chưa bàn giao.

## Thứ tự bắt buộc cho mỗi vòng (theo yêu cầu người dùng)

`Prompt Codex → Stitch sinh màn mới → xuất canvas ngay → tải PNG/HTML → reviewer độc lập → lưu critique + log lỗi → Codex viết/lưu prompt sửa → Stitch sinh phiên bản mới → xuất canvas ngay → review tiếp`.
Mỗi vòng có ID màn, bằng chứng lỗi, điểm, parent/best và prompt sửa truy vết được. Áp dụng luật dừng của rule.md (100 điểm, patience2 hoặc v8), không chạy vô hạn. Không tự nhận đã kiểm chứng UI nếu chỉ đọc API.
