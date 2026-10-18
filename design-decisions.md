# Design Decisions

Mỗi quyết định gắn với một đề xuất của AI hoặc một vấn đề tự phát hiện, kèm lý do dựa trên persona, Nielsen heuristics hoặc ràng buộc accessibility. Nhật ký AI đầy đủ: [ai/ai-design-log.md](ai/ai-design-log.md).

## 4 quyết định chính (slide "Quyết định thiết kế")

| Quyết định | Đề xuất / vấn đề | Thiết kế cuối & lý do | Màn hình | Chi tiết |
| --- | --- | --- | --- | --- |
| **Accept** | Đổi giờ / bỏ qua việc | Giữ – lịch hỗ trợ cuộc sống, không ép làm đúng giờ (US02) | S06 / S14 | D9, D16 |
| **Modify** | UI Stitch: chữ nhỏ, nhiều mục trên một màn | Chỉ nổi bật "Việc tiếp theo", chữ nội dung 24 (P2) | S03 / S01 | D4, D20 |
| **Modify** | Người thân gửi lịch thẳng vào máy ba mẹ | Người thân soạn, ông bà duyệt rồi mới vào lịch (P4) | G01 / G11 / G03 | D29, D30 |
| **Reject** | Tự gửi báo cáo, chấm điểm, streak | Chỉ gửi nội dung người lớn tuổi tự chọn | S09 / S12 | D7, D27 |

Lý do gắn với persona (P2, P4 – xem [ux/persona.md](ux/persona.md)), Nielsen #3 User control & freedom, #5 Error prevention và ràng buộc phạm vi.

## Vòng 0 – Đối chiếu output Google Stitch (11/10)

Đối chiếu trực tiếp 4 màn và bảng màu Stitch sinh ra (`assets/stitch/`). Cột "Đề xuất của AI" chỉ ghi những gì có trong ảnh.

| ID | Đề xuất của AI (Stitch) | Quyết định | Lý do | Thể hiện trong Figma |
| --- | --- | --- | --- | --- |
| D1 | Thói quen 6 hiện là "Trà chiều cùng bạn" (`power9.png`) – prompt v0 đã đổi "Wine @ 5" (rượu vang lúc 5 giờ) thành trà chiều | **Accept** | Người lớn tuổi thường dùng thuốc, rượu không an toàn; ý cốt lõi của Blue Zones là gặp bạn bè cuối ngày, uống trà hợp văn hóa Việt hơn | S05, S08, S16 – thói quen số 6 |
| D2 | Thẻ "Việc tiếp theo" chỉ có nút "Đánh dấu đã xong", không thấy bước xác nhận hay Hoàn tác; buổi tối ở Lịch tuần dùng vòng tròn trống không nhãn (`screen_day.png`, `screen_week.png`) | **Modify** → nút "Tôi đã làm xong" + `DLG-Done` hỏi lại + Snackbar "Hoàn tác"; trạng thái luôn có icon + chữ | Người tay run dễ bấm nhầm (Nielsen #5 Error prevention, #3 User control); vòng tròn trống không cho biết bấm vào sẽ ra gì (#6) | S03, S04, DLG-Done |
| D3 | Bottom nav 4 tab có nhãn: Hôm nay · Lịch tuần · 9 Thói quen · Người thân | **Accept** (chỉnh) → giữ 4 tab có nhãn, tab 4 đổi thành "Gia đình", nhãn 20 sp, Cài đặt lên app bar | Đúng ràng buộc prompt (#6 Recognition rather than recall); "Gia đình" gần với cách người lớn tuổi gọi | Component `BottomNav`, S03 |
| D4 | Home nhồi nhiều khối: lời chào, tiến trình, việc tiếp theo, 4 việc, nút thêm, lời khuyên; Lịch tuần liệt kê 21 hoạt động | **Modify** → Home chỉ nổi bật "Việc tiếp theo", các việc khác rút gọn, nội dung 24 sp; Lịch tuần chỉ tóm tắt từng ngày, chạm để mở S11 | Persona bối rối khi một màn có quá nhiều lựa chọn (pain point 5); Nielsen #8 Aesthetic & minimalist design | S03, S07 → S11 |
| D5 | Bảng màu "Serene Vitality": primary `#1F654A`, secondary đất nung `#A3471F`, tertiary `#91424A`, neutral `#1F2A24` (`bang_mau.png`) | **Accept** primary (chỉnh thành `#1F684B`, 6.69 : 1 với chữ trắng) *(sau đó bỏ đất nung, xem D21)* | Xanh lá hợp chủ đề sống tự nhiên và là màu nhận diện của nhóm; chữ phụ làm tối để đạt ≥ 4.5 : 1 (bản cuối `#526057`, 6.15 : 1) | Variables `color/*` |
| D6 | Tên việc bị cắt bằng "…" ("Ăn sáng vừa …", "Uống trà xan…"); app bar không dấu "Hom Nay", "Lich Tuan", "Nguoi Than" | **Reject** → tên việc xuống dòng, không cắt; mọi chữ có dấu đầy đủ | Người lớn tuổi không đoán được việc bị cắt chữ; WCAG 1.4.4 Resize text; Nielsen #2 Match with real world | `TaskRow`, `AppBar`, mọi màn |
| D7 | Chấm điểm và khen theo tỉ lệ: "18 / 21 hoạt động … Rất đáng khen ạ!", "Bà Lan đã thực hiện 4/9 thói quen tuần này", nhãn "Ưu tiên số 1" | **Reject** → không điểm tuần, không streak, không xếp hạng; chỉ hiện số việc đã xong trong ngày ("4/6 việc") | Ràng buộc của nhóm: không bảng xếp hạng, mất streak, điểm sức khỏe; chấm điểm tạo áp lực và cảm giác bị "quản" (P2, P4) | S03, S07, S08 |
| D7b | Thẻ đỏ "GỌI KHẨN CẤP SOS – Gọi bác sĩ & con gái Mai" to nhất màn Người thân; mỗi thẻ có 2 nút đậm với 4 kiểu gọi khác nhau (`screen_contact.png`) | **Reject** SOS; **Modify** thẻ người thân → 2 nút cố định "Gọi điện" + "Nhắn tin" | App không bảo đảm được chức năng cấp cứu, nút đỏ lớn dễ bấm nhầm (#5); 4 kiểu nút cho cùng một việc phá tính nhất quán (#4) | S09, S17 (xem D18) |

## Tự rà soát sau khi dựng Figma (11/10)

Các vấn đề dưới đây không đến từ AI mà phát hiện khi tự chạy thử prototype theo vai bà Lan.

| ID | Vấn đề phát hiện | Quyết định | Lý do | Thể hiện trong Figma |
| --- | --- | --- | --- | --- |
| D8 | Ở Lịch tuần, chạm "Thứ Sáu 9/10 · khám sức khỏe" lại mở S03 với việc của hôm nay (Thứ Năm) | **Thêm màn S11 Chi tiết ngày**: việc của đúng ngày được chọn, chia theo buổi Sáng / Trưa / Chiều / Tối; ngày đã qua (S11b) chỉ xem lại | Nielsen #1 Visibility of system status và #2 Match with real world: bà muốn biết trước hôm đi khám có việc gì để chuẩn bị. Chia theo buổi giúp đọc nhanh, đúng cách người lớn tuổi nghĩ về một ngày | S07 → S11 / S11b → S04; Flow 4 |
| D9 | Nút "Dời lại" trên thẻ Việc tiếp theo mở trang Chi tiết, không dời gì cả | **Modify** → mở dialog `DLG-Later` với 3 mốc chọn sẵn (30 phút nữa / Chiều nay / Ngày mai) + "Không dời nữa"; xem chi tiết bằng cách chạm tên việc (chữ gạch chân) | Nielsen #4 Consistency: nhãn nút phải đúng hành động. Mốc chọn sẵn tránh phải chỉnh giờ từng phút | S03, DLG-Later |
| D10 | Ngày đã qua chỉ hiện số "5/6", không biết việc nào bị bỏ | **Thêm variant** `TaskRow / Skipped`: icon ✕, chữ "Bỏ qua · 9:30 sáng (trời mưa)" | Không dùng màu làm tín hiệu duy nhất; con cháu xem lại cũng hiểu lý do | Component `TaskRow`, S11b |
| D11 | Chỉ có một trang chi tiết (Đi bộ) nên bấm các việc khác không biết việc đó là gì | **Thêm** trang chi tiết cho từng việc (vì sao tốt + cách làm 1-2-3) và nút "Xem cả ngày" ở S03. Chỉ "việc tiếp theo" có nút "Tôi đã làm xong"; việc chưa tới giờ chỉ hiện giờ hẹn và lời nhắc | Nielsen #6 Recognition rather than recall: bà không phải nhớ "Hara hachi bu" là gì. Giới hạn nút Đã xong cho việc tiếp theo để tránh đánh dấu nhầm việc buổi chiều (#5 Error prevention) | S03, S11 hôm nay, S04 × từng việc |
| D12 | Chưa có cách thêm người thân trong app; bà phải nhờ con cài | **Thêm** S12 Thêm người thân với nút "Chọn từ danh bạ điện thoại" đặt trên cùng, ô số có báo lỗi rõ (S12e) | Gõ số 10 chữ số là bước dễ sai nhất với người viễn thị, tay run; chọn từ danh bạ bỏ hẳn bước gõ. Lỗi giữ lại dữ liệu đã nhập (#9 Help users recover from errors) | S09 → S12 → S12e → S09b; Flow 5 |

## Rà soát UX vòng 2 – thêm màn còn thiếu (12/10)

Vòng này dùng Claude (skill rà soát UX cho người cao tuổi) để soi lại bản Figma theo vai bà Lan. Mỗi dòng dưới đây là một đề xuất của AI mà sinh viên đã xem xét và quyết định áp dụng; cần ghi thêm vào [ai/ai-design-log.md](ai/ai-design-log.md).

| ID | Vấn đề phát hiện | Quyết định | Lý do | Thể hiện trong Figma |
| --- | --- | --- | --- | --- |
| D13 | S02 ghi "Bước 1 / 2" nhưng không có bước 2; app sống nhờ nhắc giờ mà chưa có chỗ xin quyền thông báo | **Thêm S13** Cho phép nhắc việc (Bước 2/2): giải thích + ví dụ lời nhắc + dặn trước "điện thoại sẽ hỏi lại, bà chọn Cho phép"; **S13d** khi chọn "Để sau" | Nielsen #1 và #4 (bước đếm phải khớp). Hộp thoại xin quyền của Android hiện bất ngờ dễ bị bấm "Từ chối"; giải thích trước giúp bà hiểu mình đang cho phép cái gì. S13d nói rõ hậu quả nhưng không chặn dùng app | S02 → S13 → ST-Empty; S13 → S13d; Flow 1 |
| D14 | Lời nhắc – khoảnh khắc quan trọng nhất của app – chưa được thiết kế | **Thêm S14** Lời nhắc toàn màn hình: giờ to như màn khóa, "Còn 10 phút nữa", tên việc `headline`, đang đọc to; 3 nút lớn xếp dọc thay cho cử chỉ vuốt | Pain point 3 (cử chỉ vuốt khó với tay run) và nguyên tắc không dùng cử chỉ ẩn; báo bằng chuông + rung + chữ cùng lúc. Xem thử được từ S10 để bà quen trước | S14, S10 → S14; Flow 6 |
| D15 | Không có cách sửa hay xóa một việc đã tạo | **Thêm S15** Sửa việc (nút "Sửa" có chữ ở app bar S04) + **DLG-Delete** | Nielsen #3 User control and freedom. Nút xóa viền đỏ đặt cuối trang, xa nút Lưu; dialog nói rõ hậu quả và đặt "Không xóa, giữ lại" làm nút chính (#5 Error prevention) | S04 → S15 → DLG-Delete; Flow 7 |
| D16 | Dời / bỏ qua xong không báo gì (DLG-Later chỉ đóng lại); "Bỏ qua hôm nay" ở S04 bỏ luôn không hỏi | **Thêm Snackbar 2 tầng không tự tắt + "Hoàn tác"** cho dời, bỏ qua, xóa, sửa, nhắc lại; **DLG-Skip** hỏi lại kèm 4 lý do chọn sẵn | #1 Visibility of system status, #9 Recover from errors; không tự tắt vì WCAG 2.2.1 Timing adjustable – người đọc chậm không kịp đọc. Lý do bỏ qua hiện lại ở S11b "(trời mưa)" nên con cháu hiểu | Component `Snackbar`; S03 đã dời / bỏ qua / xóa; DLG-Skip |
| D17 | Handoff đặc tả "chạm hàng thói quen → trang mô tả" nhưng S08 chưa có màn đích, hàng cũng không có dấu hiệu bấm được | **Thêm S16** Chi tiết thói quen × 9 + mũi tên › ở S08 | #6 Recognition rather than recall: tuần này làm mấy lần thể hiện bằng ✓ ✕ ○ – có chữ chú thích, không chỉ màu. Có trạng thái trống cho thói quen chưa có việc | S08 → S16 → S05/S06; Flow 8 |
| D18 | Nút thứ hai ở thẻ người thân S09 (trước ghi "Khoe hôm nay") chưa dẫn đi đâu, và chữ "khoe" nghe không tự nhiên với người lớn tuổi; thẻ "xong cả ngày" ở S03 có trong handoff nhưng chưa vẽ | **Đổi nhãn** thành "Nhắn tin" (đi cặp với "Gọi điện") và **thêm S17** Nhắn tin cho người thân (tin soạn sẵn, chọn thêm câu bằng chip, chọn Zalo/SMS) + **S17b** Đã gửi; **S03 xong 6/6** có thẻ chúc mừng | Persona phụ (chị Mai) muốn biết mẹ đã làm gì mà không phải gọi hỏi; bà không phải gõ chữ. Thẻ chúc mừng có nút "Báo tin vui cho Mai", cho phản hồi tích cực khi xong ngày | S09 / S03 xong 6/6 → S17 → S17b; Flow 9 |
| D19 | AI đề xuất thêm hộp xác nhận trước khi gọi điện để tránh bấm nhầm | **Reject** | Handoff S09 đã chốt "Gọi điện mở ngay, không hộp thoại phụ": gọi nhầm có thể tắt ngay, còn thêm một bước làm chậm việc liên lạc khi cần gấp | Giữ nguyên S09, S17b |

## Vòng 3 – hoàn thiện MVP, gợi ý từ người thân, chế độ Người thân (13–15/10)

Vòng này đi từ góc nhìn "bàn giao được cho lập trình viên": mọi nút trong Final UI phải có màn đích (964 tham chiếu điều hướng đã kiểm tra), không còn placeholder, và app không hứa điều nó không làm được. Bản cũ được giữ ẩn trong `03 Final UI` với tiền tố `[Bản trước]`.

| ID | Vấn đề phát hiện | Quyết định | Lý do | Thể hiện trong Figma |
| --- | --- | --- | --- | --- |
| D20 | Chữ 18 sp / nhãn nav 15 sp vẫn nhỏ khi bà để cỡ "Lớn"; chú thích 16 sp phải nheo mắt | **Modify** thang chữ: nội dung 24, nhỏ nhất 20 (cả nav và caption), tiêu đề 30, nút 22; thêm collection `Dễ đọc · Cỡ chữ` để đổi cỡ toàn app | Pain point 1 của persona; cỡ nhỏ nhất 20 vẫn đọc được khi không đeo kính ở khoảng cách cầm máy | Text styles, mọi màn |
| D21 | Nút "Thêm việc" màu đất nung cạnh nút xanh "Đã xong" tạo 2 điểm nhấn tranh nhau trên Home | **Modify** → bỏ màu đất nung, `secondary` = `primary`; nền chuyển sang `#F6F7F2` (trắng ngả xanh) | Nguyên tắc "một việc mỗi màn": chỉ còn một màu nhấn nên mắt đi thẳng tới nút chính | Variables `color/*` (đổi D5) |
| D22 | Stepper −/+ 15 phút không chọn được giờ lẻ (7:05, 8:10), phải bấm nhiều lần để đi từ 5:00 tới 9:30 | **Modify** stepper −/+ 15 phút của bản Figma đầu → ô giờ bấm được mở hộp chọn `DLG-WakeTime` / `DLG-TaskTime`: 3 cột giờ (1–12), phút (00–59), sáng/chiều, hàng giữa cố định, mở đúng giá trị đã lưu, **Hủy** không lưu nháp, chỉ **Xong** mới ghi | Ít chạm hơn; hộp riêng có 2 nút rõ ràng nên không sợ đổi nhầm (#3 User control). Cột cuộn có thêm cách chạm trực tiếp vào số, nên cử chỉ vuốt không phải cách duy nhất | S02, S06, S15, N05, N06 |
| D23 | Thêm việc bắt đầu bằng lưới 9 thói quen – bà không biết "Thư giãn mỗi ngày" sẽ ra việc gì | **Modify** S05 → "Bác muốn làm gì?" với 3 việc quen thuộc (Đi bộ nhẹ nhàng, Chăm cây, Gọi người thân) + "Xem thêm hoạt động"; S08 đổi tên tab thành "Hoạt động mỗi ngày"; thói quen 4 đổi thành "Ăn vừa đủ" | #2 Match with real world: người dùng nghĩ theo việc cụ thể chứ không theo khái niệm Blue Zones. "No 80%" khó ước lượng và dễ hiểu sai thành nhịn ăn | S05, S08, S16 |
| D24 | Người mới cài app chỉ thấy Home trống, không biết lời nhắc có kêu không | **Thêm** onboarding nhẹ sau S13: N01 Thử lời nhắc → N02 / N03 (nhận được / chưa nhận + 3 bước kiểm tra) → N04 Chọn việc đầu tiên → N05 Xem lại → N18 Đã lưu → N19 | App sống nhờ lời nhắc; kiểm tra ngay lúc có con cháu bên cạnh rẻ hơn phát hiện ra sau một ngày không ai nhắc | N01 – N05, N18, N19 |
| D25 | Sửa / xóa một việc lặp lại mỗi ngày không nói rõ đổi lần nào | **Thêm** N13 "Thay đổi lần nào?" (Chỉ lần này / Lần này và các lần sau / Giữ nguyên) + câu "Lịch sử được giữ lại"; DLG-Delete và S15 ghi rõ phạm vi | #5 Error prevention; người dùng sợ xóa mất cả lịch sử đã làm | N13, S15, DLG-Delete |
| D26 | Rời form khi đang nhập là mất dữ liệu | **Thêm** N14 "Chưa lưu thay đổi" với nút chính "Tiếp tục chỉnh", nút phụ "Bỏ thay đổi" | #3 User control và #9 Recover: nút an toàn là nút chính | N14 (S06, S15, N06, N09) |
| D27 | S17b ghi "Đã gửi lúc 9:15 qua Zalo" nhưng app chỉ mở Zalo, không biết tin có được gửi | **Modify** → S17 nút "Tiếp tục gửi cho Mai"; S17b / N10 nói thật: "An Nhiên chưa xác nhận tin đã gửi" | #1 Visibility of system status phải đúng sự thật; báo "đã gửi" sai làm bà tưởng con đã biết | S17, S17b, N10 |
| D28 | Không có chỗ sửa hồ sơ, nhắc việc, sửa / xóa người thân, xem dữ liệu lưu ở đâu | **Thêm** N06 Sửa hồ sơ, N07 Nhắc việc, N08 Cách dùng đơn giản, N09 Sửa người thân, N15 Xóa người thân (danh bạ giữ nguyên) → N21, N20 Dữ liệu trên điện thoại (dùng được khi mất mạng, chưa đồng bộ sang máy khác) | #3 User control; N20 trả lời câu hỏi con cháu hay hỏi: "mất máy thì có mất lịch không?" | S10 → N06 / N07 / N08 / N20; S09 → N09 → N15 → N21 |
| D29 | Con cháu muốn giúp sắp lịch, nhưng nếu được sửa thẳng lịch của mẹ thì mẹ mất quyền quyết định | **Modify** → con cháu chỉ gửi **gợi ý** (G01); máy mẹ hiện popup G11 một lần ("Xem gợi ý" / "Để sau" → G12 nằm ở đầu Home); Bác nhận cả, đổi giờ (G04), chọn từng việc (G06) hoặc bỏ qua (G09 + Hoàn tác). App không tự báo lại việc bỏ qua cho con | Persona chính muốn tự lập, không muốn bị "quản"; quyền quyết định thuộc về người dùng chính. Persona phụ (Mai) vẫn đạt mục tiêu quan tâm | G01 – G12, S09, S03 |
| D30 | Con cháu cần lập lịch lặp (T2-T4-T6, ngày 1 và 15 hằng tháng) cho mẹ mà máy mẹ khó thao tác nhiều bước | **Thêm** chế độ Người thân C01 – C12: chọn vai trò ở màn đầu, ghép nối bằng mã 6 số (đổi sau 10 phút), lịch của mẹ theo Ngày / Tuần / Tháng, form 3 bước có kiểm tra trùng giờ (C08w), switch "Mẹ nhận trước khi thêm" bật mặc định, sửa/ngưng có hỏi phạm vi (C11, C12) | Phần phức tạp (lặp lại, phạm vi) đặt ở máy con cháu – người quen app; máy mẹ chỉ còn một nút "Nhận". Mã hết hạn có đường phục hồi rõ (C02e: nhờ mẹ mở lại mã, hoặc gọi cho mẹ) | C01 – C12; Flow 10 – 12 |
| D31 | ST-Error nói "mất mạng" nhưng app lưu trên máy, không cần mạng | **Modify** → "Chưa thể lưu trên điện thoại. Nội dung đang nhập vẫn được giữ lại." + Thử lại / Kiểm tra lại lịch / Quay lại sửa; N16 cho trường hợp lưu được việc nhưng chưa đặt được lời nhắc | Thông báo lỗi phải khớp nguyên nhân thật (#9) | ST-Error, N16 |

## Quyết định chung về bố cục

- **Một hành động chính mỗi màn:** chỉ một nút filled `primary`; các hành động phụ là nút viền hoặc text.
- **Nút xếp dọc trong dialog:** hai nút full-width xếp dọc để tránh bấm nhầm khi đặt cạnh nhau.
- **Thẻ "Việc tiếp theo" nổi bật nhất trên Home:** trả lời ngay câu hỏi "giờ tôi cần làm gì?", giảm tải trí nhớ.
- **Hỏi cỡ chữ ngay ở màn đầu (S01):** người dùng chỉnh được trước khi gặp bất kỳ nội dung nào khác.
- **Lỗi luôn nói 3 điều:** chuyện gì đã xảy ra, dữ liệu có mất không, và bước tiếp theo.
- **Thao tác đổi dữ liệu luôn có đường lui:** việc không lấy lại được thì hỏi lại trước (DLG-Done, DLG-Skip, DLG-Delete); việc đã làm thì báo bằng Snackbar không tự tắt kèm "Hoàn tác".
- **Nút nguy hiểm không bao giờ là nút chính:** màu đỏ + icon thùng rác + chữ, đặt xa nút Lưu.

## Hierarchy & consistency

| Cấp | Cách thể hiện |
| --- | --- |
| 1 – Hành động chính | Nút `primary` cao 60, chữ `label-btn` 22 trắng |
| 2 – Nội dung chính | `headline` 30 / `title-md` 26 / `body-lg` 24, màu `on-surface` |
| 3 – Thông tin phụ | `body-md` 20, màu `on-surface-variant` |
| Trạng thái | Luôn có icon + chữ (✓ Đã xong, ⓘ lỗi), màu chỉ là tín hiệu phụ |

Accessibility và responsive: xem [accessibility.md](accessibility.md).
