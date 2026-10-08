# Design Decisions

Mỗi quyết định gắn với một đề xuất của AI (xem [ai/ai-design-log.md](ai/ai-design-log.md)) và lý do dựa trên persona, Nielsen heuristics hoặc ràng buộc accessibility.

> Khi nộp: sửa cột "Đề xuất của AI" cho khớp đúng những gì Stitch đã tạo ra cho bạn.

| ID | Đề xuất của AI | Quyết định | Lý do | Thể hiện trong Figma |
| --- | --- | --- | --- | --- |
| D1 | Thói quen "Wine @ 5" = uống rượu vang lúc 5 giờ chiều | **Modify** → "Trà chiều cùng bạn" | Người già thường dùng thuốc, rượu không an toàn. Ý cốt lõi của Blue Zones là gặp gỡ bạn bè cuối ngày, và uống trà hợp văn hóa Việt hơn | S05, S08 – thói quen số 6 |
| D2 | Vuốt thẻ sang phải để đánh dấu hoàn thành | **Reject** → nút "Đã xong" 56 dp + dialog xác nhận | Cử chỉ ẩn, người tay run dễ vuốt nhầm (Nielsen #5 Error prevention); persona không quen cử chỉ | S03, S04, DLG-Done |
| D3 | Bottom nav 5 tab chỉ có icon | **Modify** → 4 tab có nhãn chữ, Cài đặt chuyển lên app bar | Nielsen #6 Recognition rather than recall; ít lựa chọn hơn giúp đỡ bối rối | Component `BottomNav`, S03 |
| D4 | Bánh xe chọn giờ (time picker wheel) | **Reject** → stepper −/+ mỗi 15 phút, nút 56 × 56 | Bánh xe nhỏ, khó dừng đúng chỗ; stepper chạm chắc chắn | S02, S06 – `TimeStepper` |
| D5 | Bảng màu xanh lá – kem – đất nung | **Accept** (chỉnh đậm hơn) | Hợp chủ đề sống tự nhiên của Blue Zones. Chữ phụ được làm tối thành `#4A5550`, đạt 7.3 : 1 | Variables `color/*` |
| D6 | Placeholder làm nhãn ô nhập | **Modify** → nhãn cố định phía trên + dòng gợi ý phía dưới | Placeholder biến mất khi gõ, người già quên ô đang nhập gì | Component `TextField` |
| D7 | Thông báo thành công tự tắt sau 3 giây (toast) | **Reject** → màn "Đã lưu" ở lại tới khi người dùng bấm | Người đọc chậm không kịp đọc toast; WCAG 2.2.1 Timing adjustable | ST-Saved |

## Quyết định chung về bố cục

- **Một hành động chính mỗi màn:** chỉ một nút filled `primary`; các hành động phụ là nút viền hoặc text.
- **Nút xếp dọc trong dialog:** hai nút full-width xếp dọc để tránh bấm nhầm khi đặt cạnh nhau.
- **Thẻ "Việc tiếp theo" nổi bật nhất trên Home:** trả lời ngay câu hỏi "giờ tôi cần làm gì?", giảm tải trí nhớ.
- **Hỏi cỡ chữ ngay ở màn đầu (S01):** người dùng chỉnh được trước khi gặp bất kỳ nội dung nào khác.
- **Lỗi luôn nói 3 điều:** chuyện gì đã xảy ra, dữ liệu có mất không, và bước tiếp theo.

## Hierarchy & consistency

| Cấp | Cách thể hiện |
| --- | --- |
| 1 – Hành động chính | Nút `primary` cao 56–60, chữ `title-md` trắng |
| 2 – Nội dung chính | `headline` 28 / `title-lg` 24, màu `on-surface` |
| 3 – Thông tin phụ | `body-md` 16, màu `on-surface-variant` |
| Trạng thái | Luôn có icon + chữ (✓ Đã xong, ⓘ lỗi), màu chỉ là tín hiệu phụ |

Accessibility và responsive: xem [accessibility.md](accessibility.md).
