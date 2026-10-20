# Storyboard — 16 slide chính

Thời lượng tham khảo khoảng 13 phút, chưa gồm Q&A. Mỗi slide: một ý chính, hình có chức năng chứng minh, lời nói nối với slide sau. Nguồn ID xem 02-evidence.md. Nội dung dưới đây là bản biên tập đề xuất, không phải báo cáo đã thử người thật.

## S01 — An Nhiên
- Thời gian: 20s. Vai trò: giới thiệu sản phẩm.
- Hiển thị: “Lịch sinh hoạt hằng ngày cho người lớn tuổi” và một màn app thật đã xác minh. Không thêm tuyên bố sức khỏe.
- Hình: một màn nổi bật, khoảng trắng lớn, màu xanh đậm.
- Notes: “Nhóm em thiết kế An Nhiên để hỗ trợ người lớn tuổi theo dõi việc trong ngày và nhận sự đồng hành từ gia đình.”
- Nguồn: codex.md, PRD. Nối: người dùng sẽ gặp việc gì trong một ngày?

## S02 — Một buổi sáng của bà Lan
- 45s. Hiển thị: “Đọc lời nhắc · Biết việc cần làm · Tự xác nhận”. Nhãn nhỏ: “Kịch bản minh họa từ persona tổng hợp”.
- Hình: ba khoảnh khắc/ba đoạn ngắn, không dựng quote phỏng vấn.
- Notes: “Bà Lan là nhân vật kịch bản. Nhóm dùng tình huống này để hỏi: bà có đọc được, hiểu được và tự thao tác được không?”
- Nguồn L01. Nối: biến tình huống thành câu hỏi thiết kế.

## S03 — Ba câu hỏi thiết kế
- 40s. Hiển thị: “Có đọc rõ không? Có chạm đúng không? Có giữ quyền chủ động không?”
- Hình: ba chi tiết app tương ứng, chỉ chọn asset đúng tính năng trong PRD/user-flow.
- Notes: “Hai câu đầu định hướng khả năng tiếp cận. Câu thứ ba là giả thuyết sản phẩm của nhóm về sự đồng hành trong gia đình.”
- Nguồn: L01, PRD, user-flow; không coi ba câu là kết quả khảo sát.

## S04 — Cơ sở nghiên cứu và giả thuyết
- 50s. Hiển thị: “Paper đã công bố / Persona tổng hợp / Kiểm tra artifact”.
- Hình: ba loại bằng chứng trên một trục nghiên cứu→thiết kế→kiểm tra; không xếp hạng như ba mẫu người dùng.
- Notes: “Repo có tổng hợp 13 nghiên cứu, nhưng nhóm chỉ đưa các claim đã đối chiếu vào bài nói. Sáu cuộc trao đổi nhập vai AI giúp gợi ý tình huống; chúng chưa xác nhận nhu cầu ngoài thực tế.”
- Nguồn: DESIGN, L01, E01. Không nói đã đọc đủ 13 toàn văn.

## S05 — Đơn giản hóa và vùng chạm là hai ưu tiên
- 55s. Hiển thị: “40 bài → 27 guideline” kèm “Đơn giản hóa · Tăng kích thước và khoảng cách control”.
- Hình: số lớn và một chi tiết chọn ngày của app; nguồn hiển thị E01, Gomez-Hernandez et al., 2023.
- Notes: “Tổng quan này hỗ trợ hướng giảm độ phức tạp và làm control dễ thao tác. Mẫu nghiên cứu không đồng nhất với người Việt 65+, nên nhóm dùng làm cơ sở thiết kế rồi vẫn cần test.”
- Nguồn E01. Không cho cả abstract lên slide.

## S06 — Nhóm cụ thể hóa guideline thành UI
- 55s. Hiển thị: “Đọc rõ → Chữ chính lớn / Chạm dễ → Nút chính cao 60 / Hiểu hành động → Icon có nhãn”.
- Hình: một screenshot lớn, ba chú thích gắn đúng vùng. Ghi “Thông số đặc tả dự án”; chỉ ghi kích thước thực tế nếu đo đúng artifact.
- Notes: “Research cho hướng đi; nhóm chọn thông số trong DESIGN để áp dụng. Số 60 và cỡ chữ của app là lựa chọn dự án, không phải kết quả trực tiếp của mọi paper.”
- Nguồn: E01, E04, L02, rule.md. Không trộn px/dp/sp/pt.

## S07 — Gia đình hỗ trợ, người lớn tuổi tự chọn
- 50s. Hiển thị: “Người thân gửi gợi ý → Người nhận xem → Nhận, đổi giờ hoặc bỏ qua”.
- Hình: flow thực từ user-flow và 2–3 màn tương ứng đã xác minh; không thêm tính năng ngoài phạm vi.
- Notes: “Từ giả thuyết persona, nhóm tách việc gợi ý của người thân khỏi quyết định của người nhận. Đây là lựa chọn thiết kế cần kiểm chứng về độ dễ hiểu và cảm giác tự chủ.”
- Nguồn: L01, ux/user-flow.md, PRD, log của màn được chọn.

## S08 — Power 9 được chuyển thành hoạt động gần gũi
- 40s. Hiển thị: ba ví dụ theo vocabulary hiện hành: “Vận động tự nhiên / Trà chiều cùng bạn / Gia đình trên hết”.
- Hình: một phần màn thói quen thật và nội dung nhắc tương ứng.
- Notes: “Nhóm dùng Power 9 làm khung tổ chức nội dung, Việt hóa ngôn ngữ và hoạt động. Nhóm chưa chứng minh việc dùng app hay khung này làm tăng tuổi thọ.”
- Nguồn: PRD, vocabulary, DESIGN. “Trà chiều” là cách điều chỉnh của sản phẩm; không gán hiệu quả y khoa.

## S09 — Một luồng sử dụng của An Nhiên
- 50s. Hiển thị: tối đa ba bước liên tiếp đúng user-flow, mỗi bước một nhãn hành động.
- Hình: ba screenshot thật cùng tỉ lệ, không ảnh điện thoại quá nhỏ. Nếu chữ không đọc được dùng hai màn và một chi tiết phóng lớn.
- Notes: “Các quyết định vừa trình bày được gắn vào cùng một luồng. Nhóm kiểm tra xem người nhận hiểu việc gì và bước tiếp theo ở đâu.”
- Nguồn: user-flow, PRD, manifest ảnh. Không gọi ảnh tĩnh là demo hoạt động hoàn chỉnh.

## S10 — Nhóm dùng AI ở những bước nào?
- 45s. Hiển thị: “Nhóm: chọn vấn đề, nguồn và đánh đổi / Codex: điều phối, prompt, log / Stitch: sinh UI / Reviewer: kiểm tra độc lập theo luật”.
- Hình: phân vai native editable, ít chữ. Dòng chú thích: “AI nhập vai: hỗ trợ tạo giả thuyết ban đầu”.
- Notes: “Nhóm giữ trách nhiệm quyết định. AI giúp tạo và rà soát phương án. Reviewer mới được tách context để không nhận sẵn kết luận từ agent tạo.”
- Nguồn: L01, L05, artifact run. Không tuyên bố mô hình hết thiên lệch.

## S11 — Loop Stitch có kiểm tra và lưu phiên bản
- 60s. Hiển thị: “Nguồn & luật → Prompt → Stitch → Canvas + PNG/HTML → Reviewer → Sửa từ best”.
- Hình: sơ đồ editable, nhánh dừng ghi “100 điểm / 2 vòng không cải thiện / v8”. Ghi “Điều kiện của loop UI hiện tại”.
- Notes: “Mỗi vòng giữ phiên bản và bằng chứng. Nếu vòng mới kém hơn, nhóm vẫn có thể sửa tiếp từ best. Điểm này chỉ phản ánh luật nội bộ.”
- Nguồn: L05 và rule.md; kiểm luật hiện tại khi chạy. Không nhầm luật UI v8 với loop slide v4.

## S12 — Case chọn ngày: sửa vùng chạm qua bốn vòng
- 65s. Hiển thị: “C07m: 87 → 87 → 97 → 100” và một câu về lỗi vùng chạm ban đầu.
- Hình: v0/v3 cạnh nhau ở cùng viewport; phóng chi tiết ô ngày. Chỉ ghi v3 đã sửa từng lỗi sau đối chiếu critique/ảnh.
- Notes: “Log v0 ghi nút ngày khoảng 35,4px và khoảng hở 6px, dưới ngưỡng dự án. Qua các vòng, agent báo hết lỗi theo rubric ở v3. Đây chưa phải kết quả test với người cao tuổi.”
- Nguồn L03, v0/v3 PNG và critique. Chân slide: “Điểm rubric nội bộ, không phải SUS”.

## S13 — Case lỗi nhập: bản cuối chưa chắc tốt nhất
- 60s. Hiển thị: “C06e: 97 → 97 → 77 · Giữ v1”.
- Hình: biểu đồ native 0–100 có cả ba vòng; một chi tiết v1/v2 cho thấy lỗi bố cục sau khi xác minh ảnh.
- Notes: “Sửa một thông báo có thể tạo lỗi khác. Log chọn v1 vì v2 có regression và dừng khi hai vòng không cải thiện. Lưu lịch sử giúp nhóm không chọn bản cuối theo quán tính.”
- Nguồn L04. Không diễn giải điểm thành phần trăm chất lượng hay độ chính xác AI.

## S14 — Kết quả và giới hạn hiện tại
- 50s. Hiển thị: “Có: đặc tả, UI, lịch sử sửa / Chưa chứng minh: khả năng dùng với người thật, duy trì thói quen”.
- Hình: hai đoạn rõ ràng, không bảng dashboard. Chỉ đưa artifact đã xác minh.
- Notes: “Bài lab tạo được thiết kế có truy vết quyết định và lỗi sửa. Agent review giúp sàng lọc lỗi, nhưng chưa trả lời đầy đủ người dùng có hiểu và dùng độc lập được hay không.”
- Nguồn: codex.md, L01, L03–L05. Không tuyên bố đã hoàn tất toàn bộ màn từ SUMMARY nếu chưa kiểm trạng thái mới nhất.

## S15 — Kế hoạch kiểm thử tiếp theo
- 50s. Hiển thị: “Đọc lời nhắc / Chọn ngày, giờ / Nhận hoặc bỏ qua gợi ý”. Nhãn: “Đề xuất, chưa thực hiện”.
- Hình: ba tác vụ và chỉ số cần quan sát: hoàn thành độc lập, chạm nhầm, cần trợ giúp, giải thích được lựa chọn.
- Notes: “Nhóm đề xuất mời người dùng đúng nhóm mục tiêu, ghi tác vụ và điều kiện trước khi thử. Có thể dùng SUS sau trải nghiệm nếu triển khai đúng thang đo; không đặt điểm giả định hay xem mẫu nhỏ là đại diện dân số.”
- Nguồn: E03 cho lý do cần người dùng tham gia; chi tiết kế hoạch là đề xuất nhóm, chưa là nghiên cứu được chạy.

## S16 — Quyết định thiết kế cần truy về bằng chứng
- 25s. Hiển thị: “Nghiên cứu định hướng · UI thể hiện lựa chọn · AI hỗ trợ thử và sửa”.
- Hình: một màn app tốt nhất đã xác minh. Không thêm con số mới.
- Notes: “Điều nhóm muốn bảo vệ là mỗi lựa chọn có lý do và có cách kiểm tra. Bước tiếp theo là xem các lựa chọn đó có giúp người lớn tuổi dùng độc lập trong tình huống thực hay không.”
- Nguồn: những claim đã trình bày, không thêm nguồn mới. Kết và Q&A.

## Phụ lục tùy chọn — ngoài 16 trang
- A01: bibliography E01/E03/E04 và các nguồn bổ sung chỉ khi đã xác minh; DOI/URL và claim tương ứng.
- A02: bảng research → quyết định → màn → giới hạn, chỉ 3–4 dòng dễ đọc.
- A03: rubric UI và ví dụ critique có evidence, fixed/regressions; ẩn credential.
- A04: quy trình AI roleplay và kế hoạch thay thế bằng dữ liệu người thật.

Nếu giảng viên chỉ cho 8–10 phút: gộp S03/S04, S07/S09, đưa S08 vào notes và S13 thành phụ lục; phải biên tập lại mạch và slide count trước generation. Không tự cắt khi người dùng đã chốt 16 trang.
