# An Nhiên – PRM393 Lab 2

App lịch sinh hoạt Power 9 cho người 65+ (Android, 360 × 800 dp). Thiết kế: Google Stitch → Figma.

- **4 file input** cho Stitch nằm ở `assets/stitch/`: `PRD.md` (làm gì, màn nào), `DESIGN.md` (token màu / chữ / spacing, chuẩn DESIGN.md của Stitch), `AppStyleGuide.md` (câu chữ, xưng hô, cư xử), `vocabulary.md` (từ nên dùng / tránh dùng). Prompt Stitch phải ghép từ 4 file này, không viết tay tự do.
- Luật thiết kế bắt buộc: `rule.md`. Mọi màn sinh bằng Stitch phải được phản biện theo file này.
- Vòng lặp Stitch tự phản biện – tự sửa: chạy `/stitch-loop <mã màn + tên>` (vd. `/stitch-loop S03 Hôm nay`). Agent điều phối gọi Stitch; subagent `stitch-critic` (`.claude/agents/`) chấm điểm. Kết quả từng vòng nằm trong `stitch-runs/<mã>/`.
- `DESIGN.md` ở thư mục gốc chỉ giữ prompt Stitch v0 làm bằng chứng lịch sử – **không dùng làm token**. Persona: `ux/persona.md`. Danh sách màn: `README.md`.
- Không ghi API key vào bất kỳ file nào trong repo.
