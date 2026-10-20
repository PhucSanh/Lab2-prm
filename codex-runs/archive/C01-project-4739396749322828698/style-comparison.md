# C01 so với màn chuẩn S03 v3

Baseline chỉ đọc: `stitch-runs/S03/v3.png` và `v3.html`.
C01 được kiểm tra bằng output Stitch v1 và bản render HTML ở viewport360×800 /412×800; không sửa ảnh hoặc HTML nguồn.

| Thuộc tính | S03 v3 | C01 v1 | Nhận xét |
|---|---|---|---|
| Nền | #F6F7F2 | #F6F7F2 | Khớp |
| Surface | #FFFFFF | #FFFFFF (thẻ chưa chọn) | Khớp; thẻ chọn dùng token #D6EADF |
| Primary | #1F684B | #1F684B | Khớp |
| Chữ chính/phụ | #202B25 / #526057 | #202B25 / #526057 | Khớp |
| Font | Be Vietnam Pro | Be Vietnam Pro (fontReady=true ở cả2 viewport) | Khớp |
| Tiêu đề / nội dung / nhãn phụ / nút |30 /24 /20 /22px|30 /24 /20 /22px|Khớp hệ phân cấp|
| Bo thẻ / nút |16 /14px|16 /14px|Khớp|
| Lề ngang |20px|20px|Khớp|
| Nhận diện |Giao diện lịch, thẻ trắng và xanh|Logo lá, thẻ chọn và xanh|Cùng hệ token; không thêm màu thói quen vào radio|

Khác biệt hợp lý: C01 có thương hiệu/câu hỏi căn giữa, danh sách radio căn trái; không có bottom nav, thẻ việc hay vạch màu thói quen vì là màn chọn vai trò trước onboarding.
S03 baseline có canvas rộng bao quanh cột mobile; ảnh Stitch C01 cũng có canvas rộng. Dùng ảnh viewport360 để xem kích thước thực, không suy ra cỡ chữ từ ảnh thumbnail canvas.

Đánh giá phong cách của orchestrator: C01 bám cùng màu/font/bo góc với S03; chưa chạy các màn B02 trở đi và chưa export sang Figma. Kết quả điểm theo reviewer độc lập trong log/critique.
