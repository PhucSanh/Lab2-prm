# Prompt khởi chạy cho agent Canva

Copy khối dưới vào agent có quyền đọc repo và Canva MCP. Nếu agent chỉ nhận chat, đính kèm toàn bộ file kit và asset cần dùng.

---
Hãy tạo slide thuyết trình tiếng Việt cho An Nhiên theo bộ Markdown trong `codex-runs/presentation-kit/`. Đọc README rồi 01 đến 06 trước khi thao tác. Đọc `codex.md` và các nguồn chuẩn được kit chỉ định. Mặc định 16 slide chính, 16:9, 12–15 phút, có speaker notes; phụ lục chỉ thêm nếu cần, tối đa 4 trang, ghi riêng số lượng.

Kể case study có logic: tình huống bà Lan → câu hỏi thiết kế → research có nguồn → lựa chọn và đánh đổi → màn UI thật → cách nhóm dùng AI → loop Stitch có reviewer → case trước/sau và regression → giới hạn → kế hoạch test. Nội dung hiển thị ít chữ; lời nói nằm trong notes. Dùng phong cách màu/font của app theo art direction.

Tạo bằng Canva MCP theo schema hiện có. Không chỉ trả một outline hoặc một prompt để người dùng tự làm tiếp. Không dùng tool legacy nếu create_design đang có. Chuẩn bị evidence ledger và manifest asset trước khi tạo. Chỉ dùng paper đã xác minh cho claim; nguồn PARTIAL/PROPOSED phải đọc lại hoặc bỏ claim. Không bịa user research, SUS, tác động sức khỏe hay thời gian tiết kiệm. AI roleplay phải được ghi đúng nhãn.

Chạy loop trong 05-canva-loop.md; mỗi critique giao reviewer độc lập context mới theo 06-slide-critic.md. Lưu từng vòng trong `codex-runs/presentation-kit/runs/<run-id>/`, giữ bản cũ và chọn best. Không dùng rubric UI để chấm chất lượng slide. Nếu thiếu công cụ reviewer hoặc render, ghi rõ bước thiếu, không tự nhận loop hoàn tất.

Đối chiếu case C07m/C06e với log, critique và PNG thật trước khi đưa lên slide. Nguồn repo và artifact chỉ đọc; không sửa tài liệu chung, CLAUDE.md, .claude/ hoặc stitch-runs/. Không publish hoặc gửi deck cho người khác.

Bàn giao link Canva editable của best, notes, nguồn và giới hạn còn lại. Trước khi bàn giao, đọc lại deck sau lưu và kiểm hình mọi trang. Những thông tin tên nhóm/môn học chưa có thì bỏ khỏi bìa, không đoán. Nếu không truy cập file local hoặc upload asset được thì báo rõ, hoàn thành phần nội dung độc lập trước và liệt kê chính xác asset còn thiếu.
---
