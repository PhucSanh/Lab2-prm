# Sổ bằng chứng

Đã đối chiếu web ngày 19/10/2026. Các URL bên dưới là nguồn, không phải bằng chứng mọi claim trong repo đã đúng. Trạng thái: VERIFIED = đã xem nội dung hỗ trợ claim hẹp; PARTIAL = tìm được bài nhưng chưa đủ hỗ trợ claim định lượng; LOCAL = bằng chứng nội bộ; PROPOSED = nghiên cứu mới gợi ý cho deck, chưa chứng minh nhóm đã dùng trong quá khứ.

## Nguồn bên ngoài
| ID | Nguồn | Trạng thái và điều được nói | Giới hạn / áp dụng |
|---|---|---|---|
| E01 | Gomez-Hernandez, Ferre, Moral, Villalba-Mora (2023), Design Guidelines of Mobile Apps for Older Adults: Systematic Review and Thematic Analysis. DOI 10.2196/43186. https://mhealth.jmir.org/2023/1/e43186/ | VERIFIED: 40 bài được chọn, tổng hợp 27 guideline; hai hướng xuyên suốt là đơn giản hóa và tăng kích thước/khoảng cách control | Tổng quan nghiên cứu có người >60 tuổi, không riêng người Việt 65+. Áp dụng: giảm lựa chọn và ưu tiên vùng chạm; kích thước cụ thể của An Nhiên là quyết định nhóm. |
| E02 | How to design font size for older adults: A systematic literature review with a mobile device (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9376262/ | PARTIAL: xác nhận bài và chủ đề qua kết quả tìm kiếm; trang toàn văn bị chặn khi mở | Chưa dùng số 18–22 pt hay số lượng nghiên cứu trên slide. Phải đọc bản publisher/full text, lấy tác giả, DOI và đoạn hỗ trợ trước khi nâng trạng thái. Không đổi pt sang dp/sp/px trực tiếp. |
| E03 | Developing a Multiprofessional Mobile App to Enhance Health Habits in Older Adults: User-Centered Approach (2024). DOI 10.2196/54214. https://formative.jmir.org/2024/1/e54214/ | VERIFIED ở mức quy trình: bài mô tả phát triển có sự tham gia người lớn tuổi | Dùng để lý giải cần phản hồi người thật. Không chép SUS 71,23→87,14 từ DESIGN trước khi xác minh chính xác các nhóm, vòng và phép đo trong bài. Không gán kết quả của bài cho An Nhiên. |
| E04 | W3C WAI, Older Users and Web Accessibility. https://www.w3.org/WAI/older-users/ | VERIFIED: tài liệu chuyên môn nối nhu cầu người lớn tuổi với accessibility | Là hướng dẫn, không phải thử nghiệm An Nhiên; web accessibility không đồng nghĩa chứng nhận app Android. |
| E05 | Lally et al. (2010), How are habits formed: Modelling habit formation in the real world. DOI 10.1002/ejsp.674. https://doi.org/10.1002/ejsp.674 | PROPOSED/PARTIAL: tìm được nguồn publisher; chưa đọc đầy đủ kết quả trong lần chuẩn bị | Chỉ đưa vào sau khi đọc và ghi claim cụ thể. Không kể như nguồn đã chi phối thiết kế trước đây. Không dùng “21 ngày”, “66 ngày cho tất cả” hay suy luận notification tạo được thói quen. |
| M01 | Assertion–Evidence approach. https://www.assertion-evidence.com/ | VERIFIED: tham khảo cách trình bày thông điệp với bằng chứng thị giác | Phương pháp làm slide, không phải paper UX hoặc bằng chứng hiệu quả An Nhiên. |

## Bằng chứng nội bộ
| ID | Artifact | Cách dùng đúng |
|---|---|---|
| L01 | ux/persona.md | Sáu vai phỏng vấn AI giả lập; persona tổng hợp và bà Lan/chị Mai là nhân vật kịch bản. Không phải mẫu khảo sát 6 người thật. |
| L02 | assets/stitch/DESIGN.md | Token gốc: nền #F6F7F2, primary #1F684B, chữ #202B25, Be Vietnam Pro; body chính 24, button 22, nút chính cao 60 theo YAML. Đây là đặc tả, cần đo artifact mới biết thực tế có đúng. |
| L03 | codex-runs/C07m/log.md và v0…v3-critique.json | Log ghi 87→87→97→100; lỗi v0 gồm ô ngày khoảng 35,4px và khoảng hở 6px. Chọn v0 và v3 làm case sau khi đối chiếu ảnh/critique. |
| L04 | codex-runs/C06e/log.md và v0…v2-critique.json | Log ghi 97→97→77, best v1, dừng patience_2. Điểm là rubric nội bộ; không chứng minh usability tăng hoặc giảm tương ứng. |
| L05 | codex/stitch-loop.md, codex/stitch-critic.md, rule.md | Mô tả quy trình và công thức nội bộ. Muốn nói “đã chạy” phải có artifact của màn tương ứng; tài liệu hướng dẫn tự nó chưa đủ. |

## Chuỗi nguồn → quyết định → bằng chứng
- E01 → giảm độ phức tạp, tăng vùng chạm → quy tắc trong DESIGN/rule → L03, ảnh thật trước/sau. Nghiên cứu hỗ trợ hướng đi; ngưỡng 48/60 và cách sửa lưới là lựa chọn dự án.
- E04 → chú ý khả năng đọc và thao tác → chữ rõ, tương phản, không dùng màu làm dấu hiệu duy nhất → đo screenshot/HTML ở màn được chọn. Không tuyên bố toàn app đạt WCAG.
- E03 → cần sự tham gia người thật → kế hoạch kiểm thử tiếp theo. Agent review là bước kiểm tra trước test, không thay thế test.
- L01 → giả thuyết về quyền tự chủ → luồng nhận/đổi giờ/bỏ qua trong user-flow và ảnh thật nếu có. Không gán quyền tự chủ cho paper chưa đọc.

## Quy tắc trích dẫn
Mỗi claim ngoài repo có ID nguồn ở chân slide; notes ghi tác giả, năm, tên, DOI/URL, vị trí section và giới hạn. Số liệu luôn có đơn vị, quần thể và bối cảnh. Nếu không có bằng chứng thì bỏ claim hoặc ghi “giả thuyết cần kiểm chứng”. Chỉ dẫn nguồn không đủ để biến suy luận thành kết quả nghiên cứu.

Mỗi claim mới phải thêm record: id; claim; source_url/path; section; status; supported_scope; limitation; applied_decision; slide_ids; checked_at. Đánh dấu rõ nguồn bổ sung hiện tại và nguồn đã có từ lịch sử dự án.
