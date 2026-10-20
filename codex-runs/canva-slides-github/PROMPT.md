# Prompt cho agent Canva

Đọc `codex.md`, sau đó dùng bộ custom tại `codex-runs/canva-slides-github/an-nhien-canva/SKILL.md` để làm slide An Nhiên bằng Canva MCP. Đây là bản port từ K-Dense Scientific Slides; đọc START-HERE.md và ADAPTATION.md nếu cần truy nguồn. Dùng reference trong gói custom; không chạy pipeline OpenRouter/Beamer/PPTX của bản gốc.

Làm deck tiếng Việt 16:9, mặc định 16 slide chính, 12–15 phút; có speaker notes và nguồn. Kể theo mạch tình huống người dùng → research → quyết định UI/UX → màn thật → AI và loop Stitch → case sửa/regression → giới hạn → kế hoạch test. Chỉ dùng claim đã xác minh, không gọi AI nhập vai là phỏng vấn người thật hay điểm agent là SUS.

Chạy Canva loop với mỗi critique từ reviewer độc lập context mới theo reference trong gói. Giữ từng bản, chọn best, kiểm render mọi slide và kiểm lại sau save. Lưu artifact ở `codex-runs/canva-slides-github/runs/<run-id>/`. Không sửa upstream, nguồn thiết kế chung, CLAUDE.md, .claude/ hay stitch-runs/. Không publish/gửi cho người khác.

Bàn giao link Canva editable của bản best cùng notes, nguồn và giới hạn. Nếu thiếu tool/asset, báo đúng bước thiếu; không tự nhận đã review hoặc đã hoàn tất loop.
