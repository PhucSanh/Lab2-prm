# PRD.md – An Nhiên

> **Product Requirements Document** · bản dùng làm **input cho Google Stitch** (thiết kế ban đầu v0) và cho Critic Agent (`/stitch-loop`).
> Đi cùng: [`DESIGN.md`](DESIGN.md) (token, giao diện) · [`../../rule.md`](../../rule.md) (luật phản biện) · [`../../ux/persona.md`](../../ux/persona.md) · [`../../ux/user-flow.md`](../../ux/user-flow.md).
> Phiên bản 1.0 · 17/10/2026 · Nguyễn Phúc Sanh · PRM393 Lab 2

| Mục | Nội dung |
| --- | --- |
| Sản phẩm | **An Nhiên** – lịch sinh hoạt hằng ngày theo 9 thói quen Power 9 (Blue Zones) |
| Nền tảng | Android, khung 360 × 800 dp (kiểm tra thêm 412 dp) |
| Người dùng chính | Người lớn tuổi (60+) và con cháu ở xa |
| Nguồn yêu cầu | 6 cuộc phỏng vấn giả lập bằng AI (mục 2) + 13 nghiên cứu UI/UX (`research/`) |
| Trạng thái | Bản đầu cho Stitch v0; sẽ cập nhật sau khi test với người thật |

> ⚠️ **Lưu ý về dữ liệu:** 6 cuộc phỏng vấn là **ChatGPT nhập vai** điền khảo sát, không phải người thật. Chúng dùng để đặt giả thuyết và định hướng thiết kế; mọi yêu cầu trong file này cần được kiểm chứng bằng test prototype với người thật (mục 10).

---

## 1. Vấn đề

Người lớn tuổi muốn sống khỏe, vui và **tự chủ**, nhưng:

- Ngày nghỉ hưu dễ **lặp lại, nhàm chán**; có thời gian rảnh mà không biết làm gì (AI-02).
- Định làm một việc tốt cho sức khỏe rồi **quên**, nhất là khi con chỉ nhắc qua điện thoại (AI-03: mẹ "nói quên mất, hôm đó bận nấu cơm").
- App hiện có thì **nhiều thông báo, nhiều nút, nhiều bước** (AI-02 A13, AI-03 D04).

Con cháu ở xa muốn quan tâm bằng việc cụ thể, nhưng **không muốn "quản" ba mẹ**, và ba mẹ cũng không muốn bị theo dõi (AI-01, AI-02, AI-03).

**How might we** giúp người lớn tuổi mỗi ngày có vài việc nhỏ đáng làm theo Power 9, tự mình quyết định làm hay không, và để con cháu ở xa đồng hành bằng lời gợi ý thay vì kiểm soát?

---

## 2. Nguồn nghiên cứu – 6 cuộc phỏng vấn giả lập

| Mã | Vai | Hồ sơ | Nhóm | Link |
| --- | --- | --- | --- | --- |
| AI-01 | **Cô Mai, 62** | Cựu giảng viên ĐH, TP.HCM, dùng công nghệ khá; 2 con đi làm | Người lớn tuổi – có điều kiện dùng | [chat](https://chatgpt.com/share/6ace39f0-a138-83ec-85e1-c7580e798406) |
| AI-02 | **Thầy Văn Minh, 68** | Nguyên giảng viên CNTT, Đà Nẵng, sống với vợ; công nghệ cao | Người lớn tuổi – có điều kiện dùng | [chat](https://chatgpt.com/share/6acf5059-48b4-83ec-8550-d89fb1567e6b) |
| AI-03 | **Anh Công, 36** | Nhân viên VP ở TP.HCM, ba mẹ 76 và 78 tuổi ở quê | Người con ở xa | [chat](https://chatgpt.com/share/6ad083bb-2728-83ec-b243-a92f10b16217) |
| AI-04 | **Chú Minh, 58** | Tiến sĩ, giảng viên CNTT, sống một mình, không vợ con | Người trung niên – chưa đủ lý do dùng | [chat](https://chatgpt.com/share/6acf5039-81b8-83ec-992f-794002d89b8b) |
| AI-05 | **Phúc, 20** | Sinh viên, TP.HCM, thích game, ít vận động | Người trẻ – chưa đủ lý do dùng | [chat](https://chatgpt.com/share/6ad07de1-fb84-83ec-b982-635441679fab) |
| AI-06 | **Anh Nam, 26** | Nhân viên VP, TP.HCM, gym 3–4 buổi/tuần | Người trẻ – chưa đủ lý do dùng, người giới thiệu cho ba mẹ | [chat](https://chatgpt.com/share/6ad07bd8-5c9c-83ec-94b7-4aebdc19df75) |

> Tuổi lấy theo nội dung trong chat (cô Mai 62, anh Nam 26), khớp với `ux/persona.md`.

### 2.1 Mỗi vai nói gì (tóm tắt)

**AI-01 · Cô Mai, 62**
- Thích gợi ý **do chính con viết** hơn thông báo tự động; nhắc lại sau 30 phút thì tiện, nhưng phải **được chọn nhận trước**: không muốn lịch "tự động bị sắp xếp ngay".
- Không muốn app báo cho con khi mình không làm: "từ sự quan tâm lại thành cảm giác bị kiểm soát".
- Thích **chụp ảnh gửi con** sau khi làm xong; muốn **rủ ngược lại** con ("Chiều Chủ nhật con rảnh thì qua đi bộ với mẹ nhé").
- Không thay Zalo: vẫn muốn gọi điện, nghe giọng con. Gợi ý **thỉnh thoảng**, không phải "một loạt nhiệm vụ" mỗi ngày.
- Huy chương: vui nếu gắn **thành tựu có ý nghĩa** (vd 30 ngày đi bộ); không biến thư giãn thành nhiệm vụ.

**AI-02 · Thầy Văn Minh, 68**
- Pain point: thông tin hoạt động **phân tán**, tìm mãi rồi hết hứng; ngày "lặp lại, nhàm chán".
- Muốn mỗi ngày "có thêm một điều gì đó đáng để mong đợi"; **tự quyết định**, không theo thời khóa biểu cứng.
- Ưu tiên số 1: **cá nhân hóa và khám phá hoạt động mới**, không phải "ngày nào cũng chỉ thấy nhắc đi bộ, uống nước".
- Linh hoạt theo hoàn cảnh: trời mưa → **gợi ý hoạt động trong nhà**; dời giờ bằng **một nút**.
- Family linking: con **gợi ý, không quản lý**; cần **phản hồi hai chiều** (gửi ảnh, lời nhắn); không tự báo khi bỏ qua; **cha mẹ chọn thông tin chia sẻ**; muốn **lịch chung** (nếu đồng ý chia sẻ) để con không gợi ý trùng giờ.
- Muốn **nhật ký thành tựu** có ảnh, kỷ niệm; kết nối người cùng sở thích; **ít thông báo**, chọn số lượng và giờ.
- "Nếu có ngày chú không mở ứng dụng vì đang bận tham gia một hoạt động… đó vẫn là một thành công."

**AI-03 · Anh Công, 36 (con, ba mẹ 75+)**
- Nhắc mẹ qua điện thoại thì mẹ quên; anh "đâu thể ngày nào cũng gọi đúng giờ để nhắc được".
- Mẹ dùng được Zalo, YouTube; **tải app, đăng ký, cài đặt thì phải có con giúp**, "mẹ cũng hay sợ bấm nhầm".
- Mỗi tuần chỉ có **10–15 phút** để hướng dẫn qua video call; thao tác phức tạp sẽ làm giúp khi về quê.
- Chia sẻ: **cha mẹ chủ động chọn**; mẹ tự gửi ảnh khoe thì "vui hơn nhiều".
- Mẹ sẽ bỏ nếu "phải bấm nhiều bước hoặc đọc quá nhiều chữ". Anh không muốn bị thông báo liên tục "mẹ đã làm gì, chưa làm gì".
- Thành công sau 2 tuần: mẹ chủ động làm vài việc trước hay quên; **mẹ tự gửi ảnh**. Thất bại: mẹ "chỉ bấm hoàn thành cho có".

**AI-04 · Chú Minh, 58**
- Câu hỏi then chốt: tại sao dùng app này thay vì Google Calendar, Zalo? → khác biệt phải là **gợi ý hoạt động phù hợp hoàn cảnh, sở thích**.
- **Đừng xem người lớn tuổi là một nhóm giống nhau**; phân theo nhu cầu, khả năng công nghệ, hoàn cảnh (không mặc định có con cháu bên cạnh).
- Cá nhân hóa bằng **quy tắc đơn giản** (sở thích, khung giờ, phản hồi), chưa cần AI phức tạp.
- Thành tựu ghi nhận **tiến bộ cá nhân**; **không bảng xếp hạng**.
- Đo thành công bằng **hoạt động thực sự làm**, không bằng số lần mở app. Làm **bản nhỏ trước**, test prototype không hướng dẫn.
- "Hãy làm một ứng dụng giúp họ có thêm lý do để đặt điện thoại xuống."

**AI-05 · Phúc, 20**
- Vấn đề không phải thiếu thông tin mà "biết rồi nhưng lười làm"; báo thức kêu thì tắt.
- Muốn **2–3 hoạt động đơn giản mỗi sáng** để tự chọn, app chỉ nhắc cái đã chọn; **tự chọn khung giờ**, tắt nhanh, dời được.
- Xóa app nếu: thông báo nhiều / sai lúc, hoạt động lặp, **hoàn thành phải nhiều bước**, bị nhắc "chưa hoàn thành mục tiêu".

**AI-06 · Anh Nam, 26**
- Không cần app cho bản thân (đã có app gym, Google Calendar), **nhưng muốn giới thiệu cho ba mẹ** (ngoài 50).
- Ba mẹ cần giao diện "đơn giản đến mức chỉ cần mở lên là biết hôm nay mình có thể làm gì".
- Muốn **gửi lời mời hoạt động** cho ba mẹ từ xa, nhưng là gợi ý, ba mẹ được từ chối; không thành công cụ giám sát.
- Không muốn **nhập quá nhiều thông tin**; thống kê đơn giản chỉ để tham khảo, **không chấm điểm sức khỏe**.

---

## 3. Insight tổng hợp

| ID | Insight | Bằng chứng | Hệ quả thiết kế |
| --- | --- | --- | --- |
| **I1** | **Đồng hành, không quản lý.** Người thân chỉ gợi ý; người lớn tuổi quyết định nhận, đổi giờ, bỏ qua. | AI-01, 02, 03, 06 | Gợi ý không tự vào lịch; mọi gợi ý có 3 lựa chọn Nhận / Đổi giờ / Bỏ qua |
| **I2** | **Riêng tư do người lớn tuổi chọn.** Không tự báo cho con khi bỏ qua hay không phản hồi. | AI-01, 02, 03 | Mặc định không gửi gì cho con; chia sẻ chỉ khi Bác bấm |
| **I3** | **Kết nối hai chiều.** Cha mẹ cũng muốn rủ con, gửi ảnh, kể chuyện. | AI-01, 02, 03 | Có "Rủ con cùng làm" và "Gửi ảnh cho con" |
| **I4** | **Ít thông báo, tự chọn giờ.** Nhắc nhiều → tắt hoặc xóa app. | AI-02, 03, 05, 06 | Nhắc tối đa 1 lần + 1 lần nhắc lại; tự chọn khung giờ; không nhắc lại việc đã bỏ qua |
| **I5** | **Linh hoạt theo hoàn cảnh.** Mưa, bận, mệt là bình thường. | AI-01, 02, 05, 06 | Dời / bỏ qua bằng 1 chạm; bỏ qua vì "trời mưa" → gợi ý việc trong nhà |
| **I6** | **Gợi ý mới, hợp sở thích, ít mà chất.** Không lặp "uống nước, đi bộ". | AI-02, 04, 05, 06 | Mỗi sáng 2–3 gợi ý theo sở thích + 9 thói quen; người dùng tự chọn |
| **I7** | **Ghi nhận có ý nghĩa, không áp lực.** Huy chương cho cột mốc thật; không xếp hạng, không chuỗi ngày. | AI-01, 02, 04, 06 | "Cột mốc" + nhật ký kỷ niệm; cấm leaderboard, streak, điểm sức khỏe |
| **I8** | **Người 75+ cần người thân cài đặt; ít bước, ít chữ.** | AI-03, 06; research PP06, PP011 | Người thân cài đặt / lập lịch được từ xa; mỗi màn 1 việc |
| **I9** | **Không phải nhóm đồng nhất.** Khả năng công nghệ khác nhau nhiều trong cùng độ tuổi. | AI-02, 04 vs AI-03 (mẹ anh Công) | 2 mức: mặc định đơn giản; tùy chọn mở thêm (khám phá, nhật ký) |
| **I10** | **Thành công nằm ngoài màn hình.** Không thay Zalo/gọi điện; đo bằng việc thực sự làm. | AI-01, 02, 04 | Không tối ưu lượt mở app; có nút gọi điện / mở Zalo, không làm chat riêng |
| **I11** | **Ít nhập liệu.** | AI-03, 05, 06 | Chọn thay vì gõ; lịch mẫu sẵn; hoàn thành ≤ 2 chạm |
| **I12** | **Có bạn đồng hành thì dễ duy trì.** | AI-02, 04, 05, 06 | Việc có thể ghi "đi cùng ai" (cô Tám, cô Lan đầu ngõ); nhóm bạn để sau MVP |
| **I13** | **Người trẻ không phải người dùng chính**, mà là người giới thiệu và cài đặt cho ba mẹ. | AI-05, 06 | Không thiết kế cho người trẻ dùng cho bản thân; luồng người thân phải nhanh |

---

## 4. Người dùng mục tiêu

Phân theo **nhu cầu và khả năng công nghệ**, không chỉ theo tuổi (I9).

| Nhóm | Đại diện | Nhu cầu chính | Ưu tiên |
| --- | --- | --- | --- |
| **U1 – Người lớn tuổi, công nghệ cơ bản** | Bà Lan 68 (nhân vật kịch bản Figma), mẹ anh Công 76 | Nhắc nhẹ, chữ to, ít bước, tự quyết định | **Chính** – thiết kế mặc định cho nhóm này |
| **U2 – Người lớn tuổi, công nghệ khá/cao** | Thầy Minh 68, cô Mai 62 | Khám phá việc mới, linh hoạt, ghi nhận có ý nghĩa | Chính – mở rộng bằng tính năng tùy chọn |
| **U3 – Người thân ở xa** | Anh Công 36, chị Mai 35 (kịch bản), anh Nam 26 | Gợi ý từ xa, an tâm mà không giám sát, cài đặt giúp | Phụ – chế độ "Người thân" |
| Ngoài phạm vi | Phúc 20, anh Nam 26, chú Minh 58 (cho bản thân) | Đã có công cụ riêng | Không thiết kế cho nhóm này |

**Nhân vật kịch bản dùng trong Stitch/Figma:** Bà Nguyễn Thị Lan, 68 tuổi, giáo viên về hưu ở Biên Hòa; viễn thị, ngón tay hơi run; chỉ quen Zalo, YouTube; hay quên giờ đi bộ, giờ ăn. Con gái **chị Mai**, 35 tuổi, ở TP.HCM.

---

## 5. Mục tiêu và ngoài mục tiêu

### Mục tiêu sản phẩm

| # | Mục tiêu | Insight |
| --- | --- | --- |
| G1 | Mở app là biết **hôm nay làm gì, việc nào xong, việc nào chưa** | I8, I11 |
| G2 | Người lớn tuổi **tự xác nhận** một việc trong ≤ 2 chạm, không cần ai giúp | I8, I11 |
| G3 | Người thân **gợi ý / lập lịch từ xa**, người lớn tuổi **tự nhận** | I1, I8 |
| G4 | Mỗi ngày có **vài gợi ý mới, hợp sở thích** thay vì lời nhắc lặp lại | I6 |
| G5 | **Không áp lực, không làm phiền**: ít thông báo, không xếp hạng, không báo cáo ngầm | I2, I4, I7 |

### Ngoài mục tiêu (non-goals)

- Không phải app y tế: không chẩn đoán, không đo chỉ số, không "điểm sức khỏe", không "điểm tuổi thọ".
- Không thay Zalo: không làm khung chat riêng; nhắn tin / gọi điện mở Zalo, SMS hoặc trình gọi điện (I10).
- Không theo dõi vị trí, không giám sát, không tự gửi kết quả cho con cháu (I2).
- Không mạng xã hội, không bảng xếp hạng, không chuỗi ngày (streak) (I7).
- Không có AI gợi ý phức tạp ở MVP; dùng quy tắc đơn giản theo sở thích, khung giờ, lý do bỏ qua (AI-04).

---

## 6. Phạm vi tính năng (MoSCoW)

| ID | Tính năng | Mức | Insight | Màn (xem `README.md`) |
| --- | --- | --- | --- | --- |
| F01 | **Hôm nay**: việc tiếp theo nổi bật + danh sách việc trong ngày, mỗi việc có trạng thái "✓ Đã xong / ○ Chưa làm / Đã dời / Bỏ qua" | Must | G1 | S03 |
| F02 | **Đánh dấu xong** ≤ 2 chạm, có hỏi lại và "Hoàn tác" | Must | I11 | S03, DLG-Done |
| F03 | **Dời / bỏ qua** 1 chạm, chọn mốc có sẵn (30 phút nữa / chiều nay / ngày mai), lý do không bắt buộc | Must | I5 | DLG-Later, DLG-Skip |
| F04 | **Lời nhắc đến giờ** toàn màn hình: chữ to, **đọc to**, 3 nút "Bắt đầu làm / Nhắc lại sau 10 phút / Hôm nay bỏ qua"; không vuốt để tắt | Must | I4 | S14 |
| F05 | **Thêm việc** 2 bước: chọn việc quen → giờ, lặp lại, nhắc; chọn thay vì gõ | Must | I11 | S05, S06 |
| F06 | **Lịch tuần** và chi tiết ngày | Must | G1 | S07, S11 |
| F07 | **9 thói quen** Power 9: mỗi thói quen có giải thích ngắn, gợi ý việc, "Đọc to" | Must | G4 | S08, S16 |
| F08 | **Người thân gợi ý lịch** → người lớn tuổi Nhận / Đổi giờ / Chọn từng việc / Bỏ qua; lịch không tự đổi | Must | I1 | G01 – G12 |
| F09 | **Chế độ Người thân**: ghép nối bằng mã 6 số, xem lịch ngày/tuần/tháng, lập lịch lặp, sửa/ngưng | Must | I1, I8 | C01 – C12 |
| F10 | **Riêng tư mặc định**: không gửi gì cho con khi Bác chưa bấm chia sẻ; bỏ qua không bị báo | Must | I2 | Toàn app |
| F11 | **Cài đặt nhắc việc**: chọn khung giờ nhận, tắt nhắc lại, mức nhắc | Must | I4 | S13, N07 |
| F12 | **Chọn cỡ chữ** Vừa / Lớn / Rất lớn ngay lần đầu | Must | research PP04 | S01, S10 |
| F13 | **Báo tin cho con**: gửi lời kể / ảnh qua Zalo hoặc SMS soạn sẵn, do Bác bấm | Should | I3, I8 | S17 |
| F14 | **Rủ con cùng làm**: Bác gửi lời mời hoạt động cho con ("Chủ nhật con qua đi bộ với mẹ nhé") | Should | I3 | S17 (mở rộng) |
| F15 | **Gợi ý buổi sáng**: 2–3 việc theo sở thích và thói quen ít làm, chọn để thêm vào lịch | Should | I6 | S03 (thẻ gợi ý), S05 |
| F16 | **Gợi ý thay thế** khi bỏ qua vì trời mưa / mệt: đề xuất 1 việc trong nhà | Should | I5 | DLG-Skip → gợi ý |
| F17 | **Đi cùng ai**: ghi tên bạn đi cùng trong việc ("với cô Tám") | Could | I12 | S06 |
| F18 | **Cột mốc & nhật ký kỷ niệm**: ghi nhận cột mốc ý nghĩa (vd 30 lần đi bộ), lưu ảnh, xem lại theo tháng; chỉ chia sẻ khi Bác chọn | Could | I7 | Mới |
| F19 | **Lịch chung** (nếu Bác đồng ý): con thấy giờ Bác bận để gợi ý đúng lúc | Could | AI-02 | C03 |
| F20 | Nhóm bạn, thử thách chung, gợi ý sự kiện địa phương | Won't (MVP) | I12, AI-02 | — |

---

## 7. User stories

### Người lớn tuổi (U1, U2)

| ID | Là… | Tôi muốn… | Để… | F |
| --- | --- | --- | --- | --- |
| US01 | Bác | mở app là thấy việc tiếp theo và việc nào đã xong | không phải nhớ hay đoán | F01 |
| US02 | Bác | bấm "Đã xong" rồi xác nhận | ghi lại việc mình làm mà không sợ bấm nhầm | F02 |
| US03 | Bác | dời việc sang chiều hoặc ngày mai bằng 1 chạm | lịch theo mình chứ không phải mình theo lịch | F03 |
| US04 | Bác | nghe điện thoại đọc to lời nhắc | không cần đeo kính vẫn biết việc gì | F04 |
| US05 | Bác | chọn giờ nhận nhắc và tắt nhắc lại | không bị làm phiền | F11 |
| US06 | Bác | xem gợi ý của con rồi tự chọn nhận hay không | được quan tâm mà không bị quản | F08 |
| US07 | Bác | không bị báo cho con khi hôm nay mình nghỉ | không phải giải thích với ai | F10 |
| US08 | Bác | gửi ảnh và lời kể cho con khi làm xong | chia sẻ niềm vui | F13 |
| US09 | Bác | rủ con cùng đi bộ cuối tuần | quan tâm là hai chiều | F14 |
| US10 | Thầy Minh | mỗi sáng thấy 2–3 việc mới hợp sở thích | ngày nào cũng có điều đáng mong đợi | F15 |
| US11 | Bác | khi trời mưa được gợi ý việc trong nhà | vẫn giữ được thói quen | F16 |
| US12 | Bác | xem lại các cột mốc và ảnh kỷ niệm | thấy mình vẫn đang tiến bộ | F18 |

### Người thân (U3)

| ID | Là… | Tôi muốn… | Để… | F |
| --- | --- | --- | --- | --- |
| US13 | Anh Công | ghép nối với máy mẹ qua điện thoại, không cần cầm máy mẹ | cài đặt giúp mẹ từ xa | F09 |
| US14 | Chị Mai | lập lịch đi bộ T2-T4-T6 cho mẹ trong ≤ 90 giây | mẹ không phải tự cài | F09 |
| US15 | Chị Mai | gửi gợi ý kèm lời nhắn của mình | mẹ thấy đó là quan tâm, không phải thông báo máy | F08 |
| US16 | Anh Công | chỉ nhận những gì mẹ chọn chia sẻ | không thành người giám sát mẹ | F10 |

---

## 8. Yêu cầu chức năng (kèm tiêu chí chấp nhận)

| ID | Yêu cầu | Tiêu chí chấp nhận |
| --- | --- | --- |
| FR01 | Màn Hôm nay hiện **1 khối "Việc tiếp theo"** và danh sách việc theo giờ | Khối việc tiếp theo là điểm nhấn duy nhất; mỗi dòng việc có giờ, icon + tên thói quen, nhãn trạng thái bằng **icon + chữ** |
| FR02 | Đánh dấu xong | Từ S03: chạm "Đã xong" → hộp hỏi "Bác đã … xong rồi chứ?" → "Đúng, đã xong" = 2 chạm; có snackbar "Hoàn tác" |
| FR03 | Dời / bỏ qua | 3 mốc dời có sẵn; bỏ qua có lý do tùy chọn (Trời mưa / Mệt / Bận / Khác); kết quả hiện snackbar nói rõ đã đổi gì + "Hoàn tác" |
| FR04 | Lời nhắc | Toàn màn hình; giờ + tên việc chữ lớn; tự **đọc to** (tắt được); 3 nút xếp dọc cao 60; không có thao tác vuốt để tắt; nhắc lại tối đa 1 lần |
| FR05 | Thêm việc | Bước 1 chọn từ việc quen (3 việc + "Xem thêm"); bước 2 giờ (ô bấm mở hộp chọn giờ, không bánh xe cuộn), lặp lại, nhắc; thiếu tên → báo lỗi dưới ô + chip gợi ý |
| FR06 | Gợi ý từ người thân | Popup / thẻ "Mai gửi lịch cho Bác" kèm **lời nhắn của Mai**; lựa chọn: Thêm vào lịch / Đổi giờ / Chọn từng việc / Để sau / Bỏ qua; lịch **chỉ đổi khi Bác bấm nhận** |
| FR07 | Chế độ Người thân | Mã ghép nối 6 số đổi sau 10 phút; lập lịch 3 bước (thông tin → lặp lại → xem lại & gửi); cảnh báo trùng giờ; "Mẹ nhận trước khi thêm" bật sẵn |
| FR08 | Riêng tư | Không có luồng nào tự gửi trạng thái "chưa làm / bỏ qua" cho người thân; chia sẻ chỉ qua hành động bấm của Bác |
| FR09 | Chia sẻ / rủ con | Soạn sẵn câu theo xưng hô ("Mẹ – con", "Bà – cháu"); mở Zalo / SMS; app ghi "đã mở ứng dụng nhắn tin", **không** báo "đã gửi" |
| FR10 | Gợi ý buổi sáng (Should) | Tối đa 3 gợi ý; ưu tiên thói quen Bác ít làm trong tuần; không lặp gợi ý đã bỏ qua 2 lần |
| FR11 | Gợi ý thay thế (Should) | Bỏ qua với lý do "Trời mưa" → đề xuất 1 việc trong nhà cùng thói quen; Bác có thể bỏ qua đề xuất |
| FR12 | Cỡ chữ | Chọn ở S01 với xem trước trực tiếp; đổi lại được ở Cài đặt |
| FR13 | Dữ liệu | Lưu trên điện thoại, dùng được khi mất mạng; chỉ phần ghép nối người thân cần mạng |

---

## 9. Yêu cầu phi chức năng

Chi tiết token ở `DESIGN.md`; luật kiểm tự động ở `rule.md`.

| ID | Nhóm | Yêu cầu |
| --- | --- | --- |
| NFR01 | Đọc được | Chữ nội dung 24, nhỏ nhất 20, nút 22; tương phản chữ chính ≥ 7 : 1, tối thiểu 4,5 : 1; giãn dòng 1,5 |
| NFR02 | Chạm được | Vùng chạm ≥ 48 × 48; nút chính cao 60, đặt cố định ở đáy; 2 nút cách nhau ≥ 8 (cặp nút lời nhắc ≥ 20) |
| NFR03 | Không phải đoán | Mọi icon có chữ; nút "Quay lại" có chữ; bottom nav 4 tab có nhãn: Hôm nay · Lịch tuần · Thói quen · Gia đình |
| NFR04 | Không cử chỉ ẩn | Không có hành động chỉ làm được bằng vuốt, kéo, nhấn giữ; flow chỉ cần chạm |
| NFR05 | Một việc mỗi màn, ít chữ | Tối đa 1 nút filled mỗi màn; câu ≤ 15 tiếng, nút ≤ 5 tiếng, mỗi thẻ ≤ 1 dòng phụ; giải thích dài để ở màn chi tiết |
| NFR05b | Nhiều icon, màu bắt mắt | Mọi việc / thói quen / tab / nút chính có icon kèm nhãn; mỗi thẻ việc có ô icon + vạch màu nhấn của thói quen (9 màu trong DESIGN.md) |
| NFR06 | Trạng thái nhìn là biết | Mỗi việc luôn hiện trạng thái bằng icon + chữ + màu (màu chỉ là tín hiệu phụ) |
| NFR07 | Giọng nói | Lời nhắc, chi tiết việc, chi tiết thói quen có nút "🔊 Đọc to" |
| NFR08 | Lời lẽ | 100 % tiếng Việt có dấu; xưng "Bác" / "Ông" / "Bà" theo hồ sơ; không từ kỹ thuật (task, notification, sync, streak); từ ngữ theo `vocabulary.md` |
| NFR09 | Không áp lực | Không bảng xếp hạng, chuỗi ngày, điểm sức khỏe, đếm ngược, lời trách "bạn chưa hoàn thành" |
| NFR10 | Riêng tư | Không theo dõi vị trí; không thu thập dữ liệu sức khỏe; chia sẻ do người lớn tuổi chủ động |
| NFR11 | Sửa được khi sai | Mọi thay đổi có "Hoàn tác"; xóa / ngưng lịch phải hỏi lại, nói rõ hậu quả |
| NFR12 | Bố cục | Khung 360 × 800, lề 20; không tràn ngang; giãn đúng ở 412 dp; nội dung trọng tâm (lời nhắc, dialog, trạng thái trống) căn giữa |

---

## 10. Chỉ số thành công

Đo bằng **việc thực sự làm ngoài đời**, không bằng số lần mở app (I10).

| # | Chỉ số | Mục tiêu | Cách đo |
| --- | --- | --- | --- |
| M1 | Số chạm để đánh dấu xong 1 việc | ≤ 2 | Đếm trong prototype |
| M2 | Thời gian thêm 1 việc mới | ≤ 60 giây, không cần giúp | Test 3–5 người 60+ trong gia đình |
| M3 | Bấm nhầm | 0 lần trong bài test | Quan sát |
| M4 | Đọc được không cần kính | ≥ 4/5 người test | Hỏi trực tiếp ở S03 cỡ "Lớn" |
| M5 | Người thân lập 1 lịch lặp | ≤ 90 giây, ≤ 3 bước | Prototype Flow 11 |
| M6 | Nhận gợi ý từ con | ≤ 2 chạm | G11 → G03 → Thêm vào lịch |
| M7 | Hiểu mà không cần hướng dẫn | ≥ 4/5 người hoàn thành nhiệm vụ không được chỉ trước | Test prototype (gợi ý của AI-04) |
| M8 | (Sau 2 tuần, khi có app thật) Việc thực hiện / việc đã lên lịch | Tăng so với tuần đầu; có ≥ 1 lần Bác tự chia sẻ ảnh | Tự báo cáo / phỏng vấn lại |

---

## 11. Hướng dẫn cho Google Stitch – thiết kế ban đầu (v0)

**Cách dùng:** prompt Stitch được ghép từ 4 file input: **PRD.md** (màn nào, nội dung gì) + **DESIGN.md** (token, phong cách) + **AppStyleGuide.md** (giọng văn) + **vocabulary.md** (từ ngữ). Sau khi Stitch sinh màn, Critic Agent chấm theo `rule.md` và lặp (`/stitch-loop`).

### 11.1 Bối cảnh cố định đưa vào mọi prompt

```
App "An Nhiên" – Android 360x800 dp – lịch sinh hoạt theo 9 thói quen Power 9 cho người Việt 60+.
Người dùng: Bà Lan, 68, viễn thị, ngón tay run, chỉ quen Zalo/YouTube, hay quên giờ đi bộ, giờ ăn.
Nguyên tắc: Bác tự quyết định; con cháu chỉ gợi ý; không tự báo cáo cho con; ít thông báo; không áp lực.
Toàn bộ chữ tiếng Việt có dấu, xưng "Bác". Ít chữ: câu ≤ 15 tiếng, nút ≤ 5 tiếng. Dùng nhiều icon, icon nào cũng có nhãn.
Mỗi thẻ việc có ô icon 48x48 màu nhấn của thói quen (icon trắng) + vạch màu bên trái. Một nút chính mỗi màn. Không vuốt, không nhấn giữ.
Token theo DESIGN.md: nền #F6F7F2, thẻ #FFFFFF, chữ #202B25, primary #1F684B; Be Vietnam Pro; chữ ≥ 20, nội dung 24, nút cao 60.
```

### 11.2 Màn ưu tiên cho v0 (theo thứ tự sinh)

| # | Màn | Mục đích | Nội dung bắt buộc | Nút chính |
| --- | --- | --- | --- | --- |
| 1 | **S03 Hôm nay** | Mở là biết hôm nay làm gì | Lời chào "Chào buổi sáng, Bác Lan" + ngày; khối **Việc tiếp theo** (9:30 · Đi bộ quanh công viên · Vận động tự nhiên); tiến độ "Đã xong 3/6 việc"; danh sách việc trong ngày, mỗi việc có nhãn ✓ Đã xong / ○ Chưa làm; nút "Dời lại"; bottom nav 4 tab | **Đã xong** |
| 2 | **S14 Lời nhắc đến giờ** | Biết ngay việc gì, xử lý 1 chạm | Giờ lớn; tên việc; "Còn 10 phút nữa"; trạng thái "🔊 Đang đọc to"; 3 nút xếp dọc | **Bắt đầu làm** · Nhắc lại sau 10 phút · Hôm nay bỏ qua |
| 3 | **G11/G03 Gợi ý từ con** | Được quan tâm mà vẫn tự chọn | "Mai gửi lịch cho Bác" + lời nhắn của Mai ("Mẹ ơi 3 giờ chiều mẹ đi bộ với cô Tám nhé"); 2 việc gợi ý có giờ; dòng "Chưa thêm vào lịch. Bác tự chọn." | **Thêm vào lịch** · Đổi giờ · Chọn từng việc · Bỏ qua |
| 4 | **S05 → S06 Thêm việc** | Thêm việc ≤ 60 giây, không gõ | Bước 1: "Bác muốn làm gì?" 3 việc quen (Đi bộ nhẹ nhàng, Chăm cây, Gọi người thân) + "Xem thêm"; Bước 2: tên việc, ô giờ "◷ 8 : 00 sáng ⌄", lặp lại, nhắc | **Lưu việc này** |
| 5 | **S08 9 thói quen** | Hiểu Power 9 bằng lời đời thường | 9 hàng: icon + tên Việt hóa + 1 câu mô tả + số lần tuần này; nút "Đọc to" | (không có nút filled; mỗi hàng chạm được) |
| 6 | **S09 Gia đình** | Liên lạc và chia sẻ do Bác chủ động | Thẻ người thân (Mai – con gái, Hùng – con trai, Bin – cháu): "Gọi điện", "Nhắn tin"; hàng "Gợi ý từ Mai · 2 việc"; dòng "Bác chọn điều muốn kể cho con" | **Thêm người thân** |
| 7 | **C06 Người thân lập lịch** | Con lập lịch cho mẹ ≤ 90 giây | Bước 1/3: thói quen, tên việc, giờ, thời lượng, lời nhắn cho mẹ; switch "Mẹ nhận trước khi thêm" (bật) | **Tiếp tục** |

### 11.3 Tên 9 thói quen dùng trên UI

Vận động tự nhiên · Sống có mục đích · Thư giãn mỗi ngày · Ăn vừa đủ · Ăn nhiều rau, đậu · Trà chiều cùng bạn · Gắn kết cộng đồng · Gia đình trên hết · Bạn bè tích cực.

### 11.4 Stitch không được sinh

Bảng xếp hạng, chuỗi ngày, điểm sức khỏe, biểu đồ phức tạp, menu ba chấm, nút chỉ có icon, carousel phải vuốt, chữ tiếng Anh, gradient, ảnh nền sau chữ, câu kiểu "Bạn chưa hoàn thành mục tiêu".

---

## 12. Câu hỏi mở và giả thuyết cần kiểm chứng

| # | Câu hỏi | Vì sao chưa chốt | Cách kiểm chứng |
| --- | --- | --- | --- |
| Q1 | Người 75+ có tự dùng được, hay chỉ dùng được khi con cài sẵn? | AI-03 chỉ là lời kể của con | Test với ông bà thật, có và không có người hướng dẫn |
| Q2 | Huy chương / cột mốc có giúp nhóm U1 không, hay chỉ hợp U2? | Chỉ các vai công nghệ khá (AI-01, 02, 04) nói về điều này | Hỏi U1 trong test; để ở mức Could |
| Q3 | Bao nhiêu gợi ý từ con mỗi ngày thì thành "phiền"? | AI-01 nói "liên tục mỗi ngày" là nhiều | Giới hạn mặc định 2 gợi ý/ngày, hỏi lại khi test |
| Q4 | Gợi ý buổi sáng dựa trên quy tắc có đủ "mới mẻ" với U2? | AI-02, 04 kỳ vọng cao | Test kịch bản 1 tuần với bộ gợi ý mẫu |
| Q5 | Flow 3 hiện ghi "con gái nhận tin" khi xong việc – có trái I2 không? | Cần đảm bảo đó là chia sẻ do Bác bật | Rà lại `ux/user-flow.md`, chuyển thành tùy chọn Bác bật |
| Q6 | Tất cả dữ liệu phỏng vấn đều là AI nhập vai | Có thể thiên lệch "lịch sự", đồng ý với ý tưởng | Phỏng vấn ít nhất 3 người thật trước khi chốt |

---

## Phụ lục – Truy vết

| Mục tiêu | Insight | Tính năng | Yêu cầu | Chỉ số |
| --- | --- | --- | --- | --- |
| G1 Biết hôm nay làm gì | I8, I11 | F01, F06 | FR01 | M4, M7 |
| G2 Tự xác nhận | I8, I11 | F02, F04 | FR02, FR04 | M1, M3 |
| G3 Người thân gợi ý, Bác nhận | I1, I8 | F08, F09 | FR06, FR07 | M5, M6 |
| G4 Gợi ý mới | I6, I5 | F07, F15, F16 | FR10, FR11 | M8 |
| G5 Không áp lực, không phiền | I2, I4, I7 | F10, F11, F18 | FR08, NFR09, NFR10 | M8 |
