# Art direction — ấm, rõ, điềm tĩnh

Deck 16:9, 1920×1080 hoặc preset presentation tương đương. Lấy cảm hứng từ lịch sinh hoạt và sự gần gũi của app. Không sao chép layout màn điện thoại thành các thẻ trên mọi slide.

## Hệ thị giác
- Nền #F6F7F2; chữ #202B25; xanh chủ đạo #1F684B; nền phụ #D6EADF; trắng #FFFFFF. Accent lấy từ DESIGN ở mảng nhỏ; không dùng cả chín màu cùng một trang.
- Font Be Vietnam Pro nếu Canva hỗ trợ; fallback Noto Sans có đủ dấu Việt. Bìa 48–60pt, title 32–40pt, body 22–28pt, nhãn 18–20pt, nguồn 14–16pt. Đây là lựa chọn cho deck, không phải token app. Nếu chật thì cắt chữ/tách slide.
- Lề an toàn khoảng 5% mỗi cạnh, canh theo cùng grid. Mỗi trang một trọng tâm. 30–45 từ hiển thị là mục tiêu biên tập; notes chứa phần giải thích.
- Giữ text/diagram/chart ở dạng editable. Screenshot app giữ nguyên tỉ lệ; cắt vùng phóng lớn có nhãn “Chi tiết” và vẫn cho biết màn nguồn.
- Không ảnh stock bác sĩ, dashboard y tế, ảnh người già buồn hoặc hình lá cây lặp lại làm nội dung chính. Ảnh AI nếu dùng phải ghi là minh họa, không làm người tham gia nghiên cứu.

## Nhịp bố cục
Bìa tối giản; kịch bản người dùng; bằng chứng nghiên cứu; cặp research/UI; flow 3 bước; màn app lớn; phân vai AI; loop; so sánh trước/sau; giới hạn; kết. Thay đổi bố cục theo mục đích, giữ typography/màu thống nhất.

Before/after phải cùng màn, cùng tỉ lệ, cùng viewport. Đặt version và chú thích lỗi thật. Không thay ảnh cũ bằng ảnh làm xấu hoặc dựng lại screenshot bằng AI. Biểu đồ điểm ghi rõ “Điểm rubric nội bộ”; trục 0–100, giữ cả vòng regression.

## Tài sản cần thu
Ưu tiên PNG viewport 360 đã có trong codex-runs/<mã>/; đối chiếu log và critique đúng version. Chọn 3–5 màn đủ kể một luồng, không đưa mọi màn vào deck. Asset manifest ghi source_path, version, screen_id nếu có, slide_id, trạng thái upload và Canva asset_id thực trả về. Không tự đoán asset_id hoặc dựng URL công khai cho file local.

## Kiểm tra hình
Render tất cả trang, xem ở kích thước trình chiếu và thumbnail tổng thể. Soát dấu Việt, crop, khoảng trắng, độ rõ screenshot, nguồn ở chân slide, tràn/đè chữ. API báo tạo thành công hoặc chỉ đọc text chưa phải visual QA.
