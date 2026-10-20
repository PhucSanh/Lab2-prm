# Kết quả Stitch do Codex tạo

Mỗi màn có thư mục riêng chứa prompt, response đã bỏ thông tin xác thực, ảnh, HTML, critique, state và log.
Không ghi đè `stitch-runs/`. Project ID riêng lưu ở `codex-runs/project.txt` sau khi tool xác nhận.
Không tự lấy project của Claude làm project ghi mặc định. Chỉ dùng project cũ khi người dùng chỉ định; screen nguồn vẫn phải giữ nguyên.
