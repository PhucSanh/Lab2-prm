# Kết nối Google Stitch với Codex

## Cấu hình đang dùng trên máy này

Đã tạo file riêng `~/.config/codex/stitch.env` (quyền 600). Nhập key sau `STITCH_API_KEY=` rồi lưu.
Codex MCP dùng `http_headers_helper` gọi `~/.config/codex/stitch_headers.py` để đọc file này, nên không cần export biến môi trường hay chạy từ terminal.
Khởi động lại Codex sau khi lưu key rồi thử lệnh liệt kê project. Không in nội dung env ra log/chat.
File TOML mẫu trong repo là phương án dùng biến môi trường thay thế; không ghép thêm bảng Stitch trùng vào cấu hình đang có.

## 1. Xác thực (phương án biến môi trường)

Mở https://stitch.withgoogle.com/ → Settings → API Keys và tạo key nếu tài khoản hỗ trợ.
Không gửi key trong chat và không lưu vào repo.

Ghép bảng trong `codex/stitch-mcp.example.toml` vào `~/.codex/config.toml` của chính bạn.
Nếu đã có `[mcp_servers.stitch]`, cập nhật bảng đó thay vì thêm bảng trùng.
Không thay thế toàn bộ cấu hình cá nhân và không sửa cấu hình Claude.

Cấu hình lấy key từ môi trường của tiến trình Codex. Trong Bash có thể nhập kín:

```bash
read -rsp 'Stitch API key: ' STITCH_API_KEY
printf '\n'
export STITCH_API_KEY
```

Sau đó khởi chạy Codex từ terminal này để tiến trình con nhận biến.
Codex desktop đã mở từ launcher thường không nhận biến vừa export; cần thoát hẳn và khởi chạy lại từ môi trường có biến, hoặc dùng cơ chế quản lý secret của môi trường desktop.
Không dùng `echo` để in key. Không ghi key vào file TOML mẫu.

## 2. Xác nhận kết nối

```bash
codex mcp list
```

Lệnh này chỉ xác nhận cấu hình, chưa chứng minh xác thực thành công.
Mở phiên Codex mới và yêu cầu: `Liệt kê project Google Stitch, không tạo hay sửa gì`.
Chỉ coi kết nối thành công khi tool read-only trả dữ liệu thật. Chưa thấy tool thì kiểm tra cấu hình được load, project trust, môi trường key và khởi động lại phiên.
401/403: kiểm tra key/quyền. Không tự chuyển sang OAuth hay cài proxy khi chưa cần.

## 3. Chạy loop

Yêu cầu: `Chạy Codex Stitch loop S03 Hôm nay`.
Agent đọc `AGENTS.md` → `codex.md` → `codex/stitch-loop.md`.
Reviewer chạy độc lập theo `codex/stitch-critic.md`; không cần khai báo model của Claude.
Nếu runtime không hỗ trợ subagent độc lập, báo thiếu khả năng đó và dừng trước khi sinh màn; không tự chấm thay reviewer.

Stitch trả kết quả qua tool response; orchestrator đợi job hoàn tất nếu tool trả trạng thái pending, rồi lấy screenshot/HTML và ghi log. Không giả định Stitch tự gửi webhook/log về chat.
Đây là workflow do agent thực thi trong phiên đang chạy, chưa phải daemon tự chạy khi đóng Codex.

## Tài liệu

- Google Stitch MCP: https://stitch.withgoogle.com/docs/mcp/setup
- Google SDK (endpoint/xác thực): https://github.com/google-labs-code/stitch-sdk/tree/main/packages/sdk
- Codex MCP (env_http_headers/timeout): https://developers.openai.com/codex/mcp
- Codex AGENTS.md: https://developers.openai.com/codex/guides/agents-md

## Helpers chạy từng vòng

Các helper riêng của Codex nằm trong `codex/scripts/`:
- `run_round.py <mã> <vòng> generate|edit|fetch`: gọi Stitch, lưu response/state, thêm từng phiên bản lên canvas, giữ khung khác và tải PNG/HTML. `fetch` phục hồi màn đã có ID, không generate lại.
- `measure.cjs <mã> <vòng>`: render360/412px bằng Chromium, tắt JavaScript trang và lưu metrics/ảnh QA.
- `checkpoint.py <mã> <vòng>`: kiểm schema critique, tính điểm, chọn best/early stop và ghi log; không thay reviewer chấm.
- `summary.py`: cập nhật bảng tiến độ làn B trong codex-runs/SUMMARY.md.

Các helper do orchestrator gọi theo workflow, không phải daemon. Prompt và reviewer độc lập vẫn do Codex điều phối. run_round không tự gọi lại generation khi timeout. Script đang dùng môi trường Python/Node/Chromium sẵn có trên máy này; key đọc từ helper ngoài repo. Chỉ chạy vòng mới khi vòng trước đã có critique hợp lệ và prompt sửa được lưu.
