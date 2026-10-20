# An Nhiên — Codex

App lịch sinh hoạt Power 9 cho người 65+, thiết kế Android 360 × 800 dp.
Lab này là thiết kế Google Stitch → Figma; không tự thêm phần hiện thực Flutter.

## Nguồn chuẩn

- `assets/stitch/PRD.md`: phạm vi, bối cảnh và nội dung màn.
- `assets/stitch/DESIGN.md`: token và từ điển icon.
- `assets/stitch/AppStyleGuide.md`: giọng văn, câu mẫu, xưng hô.
- `assets/stitch/vocabulary.md`: tên thói quen và từ tránh dùng.
- `rule.md`: luật chấm hiện tại; nếu tài liệu workflow cũ mâu thuẫn thì dùng luật hiện tại.
- `ux/persona.md`, `ux/user-flow.md`, `flutter-handoff.md`, `README.md`: bối cảnh và mapping màn.
- `DESIGN.md` ở gốc là prompt lịch sử, không dùng làm nguồn token.

## Workflow riêng

- Điều phối: `codex/stitch-loop.md`.
- Reviewer độc lập: `codex/stitch-critic.md`. Được phép dùng subagent cho từng critique khi người dùng yêu cầu chạy loop; không cố định model.
- Setup MCP và cách chạy: `codex/setup.md`.
- Cấu hình MCP mẫu, không chứa key: `codex/stitch-mcp.example.toml`.
- Output riêng: `codex-runs/<mã màn>/`. `stitch-runs/` chỉ được đọc để tham khảo/import.

## Quyền và phạm vi

Không sửa/xóa `CLAUDE.md`, `.claude/`, cấu hình agent khác, hay lịch sử `stitch-runs/`.
Không ghi API key vào repo, log, prompt hoặc trả lời. Không tự tìm key trong cấu hình agent khác.
Khi bắt đầu từ màn cũ, clone/biến thể thành screen ID riêng của Codex trước khi sửa; không sửa screen nguồn của agent khác.
Không sửa nguồn thiết kế chung trong loop; nếu cần token/icon mới thì ghi đề xuất riêng trong `codex-runs/design-decisions.md` và báo người dùng.
Không tự export hoặc sửa Figma khi chỉ được yêu cầu chạy Stitch loop.

## Cách gọi

Trong chat: `Chạy Codex Stitch loop S03 Hôm nay`.
Chạy tiếp: `Chạy Codex Stitch loop S03 Hôm nay --resume`.
Biến thể: `Chạy Codex Stitch loop S03b Hôm nay đã xong --from S03`.
Import lịch sử Claude: `Chạy Codex Stitch loop S03 Hôm nay --import stitch-runs/S03`.
Đây là yêu cầu bằng ngôn ngữ tự nhiên, không phải slash command được Codex đăng ký tự động.

## Project đang dùng (theo yêu cầu người dùng)

Dùng project An Nhiên của Sanh `2013215887278758682` cho công việc Hiếu/Codex, không tạo thêm project riêng. Log vẫn ở codex-runs/. C01 ở project riêng cũ đã lưu lịch sử trong codex-runs/archive/; không xóa project cũ. Chỉ thay đổi màn thuộc task được giao, giữ nguyên các màn khác.

## Quy ước đặt tên màn

Nhãn canvas theo mẫu chung `An Nhiên - <Tên màn>` (ví dụ `An Nhiên - Chọn vai trò`). Viết hoa bình thường, không in hoa toàn bộ, không thêm tên người chạy hoặc agent. Mã task/màn và thông tin người phụ trách chỉ ghi trong log nội bộ.

## Xuất màn và lịch sử từng vòng

Khi chạy loop, mỗi vòng Stitch hoàn tất phải xuất màn lên canvas project An Nhiên đang dùng ngay, lưu PNG/HTML, giao reviewer chấm, ghi lỗi và prompt sửa của Codex rồi sinh bản mới. Giữ các bản trước trên canvas và trong log, không sửa đè hay chỉ xuất màn chốt. Xem quy trình chi tiết trong codex/stitch-loop.md.
