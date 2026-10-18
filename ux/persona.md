# Persona & Problem

## Bối cảnh

- Việt Nam có **14,2 triệu người từ 60 tuổi** (Cục Thống kê, Điều tra dân số và nhà ở giữa kỳ 2024, công bố 2025).
- UNFPA Việt Nam dự báo Việt Nam bước vào giai đoạn **xã hội già năm 2036** (vietnam.unfpa.org/en/topics/ageing-0).
- Hai nhóm người dùng: **người cao tuổi** muốn sống vui, tự chủ; **người con** muốn an tâm từ xa nhưng không "quản" ba mẹ.

## Nguồn nghiên cứu

### Phỏng vấn giả lập bằng AI (6 vai)

Mỗi vai là một cuộc trò chuyện ChatGPT nhập vai điền khảo sát. Đây là dữ liệu giả lập để định hướng, **không thay thế phỏng vấn người thật** và không đồng nhất với persona bên dưới. Danh mục đầy đủ: [Docs • AI trả lời Form](https://docs.google.com/document/d/1tloaM4YAa41kd8M1Y_5OC13CzmFxflQT3P5mOHSw9oA/edit?tab=t.9norodox6mzh).

| Vai | Nhóm | Ý chính |
| --- | --- | --- |
| [AI-01 • Cô Mai, 62](https://chatgpt.com/share/6ace39f0-a138-83ec-85e1-c7580e798406) | Có điều kiện | "đồng hành với mình chứ không phải quản lý mình"; nhận gợi ý từ con nhưng tự chọn; không muốn app tự báo cáo khi bỏ qua |
| [AI-02 • Ông Minh, 68](https://chatgpt.com/share/6acf5059-48b4-83ec-8550-d89fb1567e6b) | Có điều kiện | "khả năng cá nhân hóa và khám phá hoạt động mới"; gợi ý theo sở thích; tự đổi giờ, ít thông báo |
| [AI-03 • Anh Công, 36](https://chatgpt.com/share/6ad083bb-2728-83ec-b243-a92f10b16217) | Có điều kiện | "Cha/mẹ chủ động chọn thông tin muốn chia sẻ"; ba mẹ 76 và 78 tuổi; cần xem demo trước khi thử |
| [AI-04 • Chú Minh, 58](https://chatgpt.com/share/6acf5039-81b8-83ec-992f-794002d89b8b) | Chưa đủ lý do dùng | Công cụ hiện có đã nhắc lịch; cần gợi ý khác biệt |
| [AI-05 • Phúc, 20](https://chatgpt.com/share/6ad07de1-fb84-83ec-b982-635441679fab) | Chưa đủ lý do dùng | "thiếu động lực với dễ trì hoãn"; muốn hoạt động ngắn, vui; không chủ động tìm tải |
| [AI-06 • Anh Nam, 26](https://chatgpt.com/share/6ad07bd8-5c9c-83ec-94b7-4aebdc19df75) | Chưa đủ lý do dùng | Gym 3–4 buổi/tuần; cần cân bằng ngủ, nghỉ; muốn thử trước khi giới thiệu ba mẹ |

### Persona tổng hợp (Docs • User Story)

| Persona | Mô tả | Nhu cầu chính | User story |
| --- | --- | --- | --- |
| P1 • Ông Văn Minh, 68 | Cựu giảng viên CNTT, Đà Nẵng | Gợi ý hoạt động mới, lịch linh hoạt | US01 – US04 |
| P2 • Bà Phó Đoan, 61 | Dùng Zalo cơ bản, ngại nhiều bước | Gợi ý dễ hiểu, lời nhắc nhẹ | US05 – US08 |
| P3 • Chị Tuyết, 28 | Nhân viên văn phòng, con bà Đoan | Gửi gợi ý, kết nối tự nguyện | US09 – US12 |
| P4 • Cụ Cố Hồng, 76 | Sống một mình, con trai ở Nhật | Thích gặp bạn, coi trọng riêng tư | US13 – US16 |

Nguồn: [Docs • User Story • P1 – P4, US01 – US16](https://docs.google.com/document/d/1tloaM4YAa41kd8M1Y_5OC13CzmFxflQT3P5mOHSw9oA/edit?tab=t.sq7qua9dzk7e).

### Nhân vật kịch bản trong Figma

Prototype và các màn trong Figma dùng hai nhân vật kịch bản **bà Lan** và **chị Mai** để demo liền mạch. Bà Lan gộp nhu cầu của người cao tuổi ở P2 và P4 (chữ to, ít bước, tự quyết định, coi trọng riêng tư); chị Mai đại diện cho người thân ở P3. Chi tiết hai nhân vật ở dưới.

## Nhân vật chính – Bà Nguyễn Thị Lan

| Mục | Nội dung |
| --- | --- |
| Tuổi, nghề | 68 tuổi, giáo viên tiểu học đã về hưu |
| Nơi sống | Biên Hòa, sống cùng gia đình con trai; con gái ở TP.HCM |
| Thiết bị | Điện thoại Android màn 6.5", cỡ chữ hệ thống đã chỉnh "Lớn" |
| Thói quen số | Dùng Zalo để gọi video, YouTube để nghe nhạc; chưa từng dùng app lịch |
| Thể chất | Viễn thị, đeo kính đọc; ngón tay hơi run, khó chạm chính xác; đi bộ được 20–30 phút |
| Trí nhớ | Hay quên giờ uống nước, giờ đi bộ, đôi khi quên đã ăn trưa chưa |

### Mục tiêu

- Giữ sức khỏe để tự lập, không phải phiền con cháu.
- Có một nếp sinh hoạt đều đặn mỗi ngày: vận động, ăn uống điều độ, nghỉ ngơi.
- Giữ liên lạc thường xuyên với con gái ở xa.

### Pain points

1. Chữ trong app quá nhỏ và xám nhạt, phải tháo kính ra đeo vào.
2. Icon không có chữ nên không biết bấm vào sẽ ra gì; sợ bấm nhầm.
3. Thao tác vuốt, nhấn giữ hay bánh xe chọn giờ đều khó làm với tay run.
4. App báo lỗi bằng tiếng Anh hoặc từ kỹ thuật, không biết dữ liệu có bị mất không.
5. Quá nhiều lựa chọn trên một màn hình làm bà bối rối và bỏ app sau vài ngày.

### Câu nói đặc trưng

> "Bà chỉ cần nó nhắc giờ đi bộ, giờ ăn, chữ to bà đọc được là được rồi."

## Nhân vật phụ – Chị Mai (con gái)

35 tuổi, nhân viên văn phòng ở TP.HCM. Chị muốn biết mẹ có đi bộ và ăn uống đều không mà không phải gọi hỏi mỗi ngày. Chị thường là người cài app giúp mẹ.

Từ vòng 3, chị Mai là người dùng thật của **chế độ Người thân** (C01 – C12): ghép nối máy mình với máy mẹ bằng mã 6 số, xem lịch của mẹ theo ngày / tuần / tháng và lập lịch lặp (vd đi bộ T2-T4-T6). Chị chỉ gửi *gợi ý*; mẹ chọn nhận, đổi giờ hoặc bỏ qua (G03 – G09).

| Mục | Nội dung |
| --- | --- |
| Mục tiêu | Giúp mẹ có nếp sinh hoạt đều mà không "quản" mẹ; biết mẹ ổn mà không gọi hỏi mỗi ngày |
| Pain points | Ở xa, không cầm được máy mẹ để cài; đặt lịch lặp trên máy mẹ quá nhiều bước; sợ mẹ thấy bị theo dõi |
| Câu nói | "Con chỉ muốn đặt sẵn giờ đi bộ cho mẹ, mẹ đồng ý là được." |

## Problem statement

Bà Lan muốn duy trì các thói quen sống khỏe mỗi ngày nhưng hay quên. Các app lịch hiện có thì chữ nhỏ, icon khó hiểu và quá nhiều bước, nên bà bỏ dở sau vài ngày và vẫn phải nhờ con cháu nhắc.

**How might we** giúp người 65+ tự duy trì một ngày sinh hoạt theo 9 thói quen Power 9 mà không cần người khác hỗ trợ?

## Chỉ số thành công (đo được)

| # | Chỉ số | Mục tiêu | Cách đo |
| --- | --- | --- | --- |
| 1 | Số lần chạm để đánh dấu xong 1 việc từ màn Hôm nay | ≤ 2 lần chạm | Đếm trong prototype (Đã xong → Đúng, đã xong) |
| 2 | Thời gian thêm 1 việc mới | ≤ 60 giây, không cần trợ giúp | Test prototype với 3–5 người trên 60 tuổi trong gia đình |
| 3 | Bấm nhầm nút | 0 lần trong bài test | Quan sát khi test; nút chính cao 60 dp, vùng chạm ≥ 48 dp, cách nhau ≥ 8 dp |
| 4 | Đọc được nội dung không cần kính | ≥ 4/5 người test | Hỏi trực tiếp khi xem màn S03 cỡ chữ "Lớn" |
| 5 | Người thân lập 1 lịch lặp cho mẹ | ≤ 90 giây, ≤ 3 bước | Đo trong prototype Flow 11 (C03 → C09) |
| 6 | Mẹ nhận gợi ý từ con | ≤ 2 lần chạm | G11 "Xem gợi ý" → G03 "Thêm 2 việc vào lịch" |

## Power 9 – cách app chuyển thành việc hằng ngày

| # | Thói quen Blue Zones | Tên trong app | Ví dụ việc trong lịch |
| --- | --- | --- | --- |
| 1 | Move Naturally | Vận động tự nhiên | Đi bộ quanh công viên 20 phút, tưới rau |
| 2 | Purpose | Sống có mục đích | Viết 1 điều mình mong làm hôm nay |
| 3 | Down Shift | Thư giãn mỗi ngày | Tập thở chậm 10 phút, ngủ trưa 20 phút |
| 4 | 80% Rule | Ăn vừa đủ (bản trước: "Ăn vừa no 80%", đổi ở D23) | Ăn trưa chậm rãi, dừng khi thấy vừa đủ |
| 5 | Plant Slant | Ăn nhiều rau, đậu | Bữa sáng có rau và đậu |
| 6 | Wine @ 5 | Trà chiều cùng bạn (đổi ngay từ prompt v0, xem design-decisions.md D1) | Uống trà với hàng xóm lúc 5 giờ chiều |
| 7 | Belong | Gắn kết cộng đồng | Đi chùa, nhà thờ, sinh hoạt hội |
| 8 | Loved Ones First | Gia đình trên hết | Gọi điện cho con gái Mai |
| 9 | Right Tribe | Bạn bè tích cực | Đi bộ cùng nhóm bạn buổi sáng |
