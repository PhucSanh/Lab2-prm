# Bộ điều phối slide An Nhiên

Đầu vào cho agent có Canva MCP; Markdown là chỉ dẫn, không tự chạy loop.
Ngày chuẩn bị: 19/10/2026. Chỉ ghi artifact dưới `codex-runs/`.

## Đọc theo thứ tự
1. `01-brief.md`: mục tiêu và phạm vi.
2. `02-evidence.md`: nguồn, mức xác minh và giới hạn.
3. `03-storyboard.md`: 16 slide chính, lời nói mẫu và phụ lục.
4. `04-art-direction.md`: chỉ dẫn thị giác theo app.
5. `05-canva-loop.md`: sinh, xuất, review, sửa, chọn best.
6. `06-slide-critic.md`: giao riêng cho reviewer mới.
7. `07-start-prompt.md`: copy vào chat agent Canva để bắt đầu.

## Lựa chọn phương pháp
Dùng cấu trúc case study UX: vấn đề → bằng chứng → quyết định → giao diện → đánh giá → giới hạn. Tham khảo [Assertion–Evidence](https://www.assertion-evidence.com/): kết luận có bằng chứng thị giác thay vì danh sách bullet. Đây là phương pháp trình bày, không phải một bộ MD được tải về hay nghiên cứu UX của An Nhiên. Bộ MD này được viết riêng từ repo, không cài skill bên thứ ba.

Mặc định: tiếng Việt, 16:9, 16 slide chính, khoảng 12–15 phút; tối đa 4 slide phụ lục. Đây là giả định biên tập, có thể đổi theo yêu cầu môn học. Chưa có rubric của giảng viên hoặc thời lượng chính thức.

## Kết quả cần có khi thực thi
`runs/<run-id>/`: manifest nguồn và asset, nội dung chốt, ID/link Canva, render từng slide, critique từng vòng, prompt sửa, log và bản best. Lưu phiên bản trước; không đụng CLAUDE.md, .claude/, stitch-runs/ hay tài liệu chung.

## Dữ liệu còn thiếu
Không có thư mục `research/` trong checkout khi chuẩn bị bộ này, dù DESIGN nhắc hai DOCX. Không tuyên bố đã đọc chúng. Link Docs trong persona chưa được đọc trong phiên chuẩn bị. Tên nhóm, môn học, thành viên và rubric để agent lấy từ người dùng hoặc bỏ khỏi bìa, không tự đoán.
