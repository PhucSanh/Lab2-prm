# AppStyleGuide.md – An Nhiên

> **App Style Guide**: quy định app **nói gì, nói thế nào và cư xử ra sao** với người dùng.
> Là 1 trong 4 file input cho Google Stitch: [`PRD.md`](PRD.md) (làm gì) · [`DESIGN.md`](DESIGN.md) (trông thế nào) · **AppStyleGuide.md** (nói và cư xử thế nào) · `vocabulary.md` (dùng từ nào).
> Critic Agent dùng file này cùng [`../../rule.md`](../../rule.md) để phản biện output Stitch.
> Phiên bản 1.1 · 17/10/2026 (thêm ít chữ, nhiều icon, màu bắt mắt) · nhóm tự định nghĩa (thầy không đưa mẫu).

---

## 0. File này được làm ra như thế nào

### 0.1 Nguồn

Mỗi quy tắc đều ghi mã nguồn trong ngoặc vuông. Không có quy tắc nào chỉ dựa trên cảm tính; chỗ nào **nhóm tự chọn** giữa nhiều phương án thì ghi `[N]` kèm lý do.

| Mã | Loại nguồn | Cụ thể | Ở đâu |
| --- | --- | --- | --- |
| `[T]` | Góp ý của thầy, 16/10/2026 | "Chữ nhiều" (= chê nhiều chữ → **ít chữ**), **"màu sắc bắt mắt"**, **"dùng icon nhiều"**, "Căn giữa", "không kéo trượt", "Nhìn vào là bik làm hay chưa làm", "Voice", "Từ vựng thân thiện với người già", "Thiết kế luồng tập trung vào việc click" | `ai/feedback-thay-2026-10-16.md` (3 ý in đậm bổ sung 17/10 theo lời sinh viên) |
| `[R-xx]` | Nghiên cứu UI/UX (13 bài) | PP02 (Design Guidelines 2023), PP03 (Health Habits 2024), PP04 (Font size 2022), PP07 (Button position 2020), PP08 (Keypad, Icon), PP09 (Pictogram), PP010 (Navigation 2026), PP012 (Visual info), PP06 / PP011 (Caregivers); [01] Optimizing Mobile App Design 2025 | `research/UX-Research.docx`, `research/Tong_hop_UIUX_An_Nhien.docx` |
| `[AI-0x]` | Phỏng vấn giả lập (6 vai) | AI-01 cô Mai, AI-02 thầy Minh, AI-03 anh Công, AI-04 chú Minh, AI-05 Phúc, AI-06 anh Nam | `PRD.md` mục 2 |
| `[W-…]` | Chuẩn và bộ rule công khai | **WCAG 2.2** (W3C, 2023) · **W3C WAI – Older Users** (cập nhật 11/2025) · **NN/g – Usability for Senior Citizens** (2013) · **CHI App Guidelines** (Tan Tock Seng Hospital, Singapore, 2022) · **Quy chuẩn App thân thiện người già** của Bộ Công nghiệp và Thông tin Trung Quốc (MIIT, 2021) | Mục 15 |
| `[D-xx]` | Quyết định thiết kế đã có trong repo | D1 – D31 (rút ra khi phản biện output Stitch và tự test Figma) | `design-decisions.md` |
| `[N]` | Nhóm tự quyết định | Khi các nguồn không nói cụ thể hoặc có nhiều cách làm | Ghi lý do ngay tại chỗ |

### 0.2 Quy trình 5 bước

```
① Gom nguồn ──► ② Rút nguyên tắc ──► ③ Viết thành quy tắc có ví dụ ──► ④ Đối chiếu Figma ──► ⑤ Chuyển thành luật kiểm
  [T] [R] [AI]     mỗi nguồn → 1 câu     ID SG-xx, Nên / Không nên       sửa quy tắc nếu        rule.md (Critic Agent)
  [W] [D]          "người dùng cần gì"   + câu mẫu dùng được ngay        mâu thuẫn bản cuối     + checklist mục 14
```

1. **Gom nguồn:** đọc lại ghi chú của thầy, 2 file research, 6 cuộc phỏng vấn, WCAG 2.2, W3C WAI, NN/g và các quyết định D1–D31.
2. **Rút nguyên tắc:** mỗi phát hiện viết lại thành một câu "người dùng cần…". Ví dụ PP02 "sau mỗi lần bấm nên có tín hiệu rõ" → "Bác cần biết ngay mình vừa làm được chưa".
3. **Viết quy tắc:** mỗi nguyên tắc thành quy tắc `SG-xx`, có ví dụ **Nên** / **Không nên** bằng câu chữ thật của app.
4. **Đối chiếu Figma:** so với câu chữ đang có trong 105 màn (S, N, G, C). Chỗ lệch thì ghi vào mục 14.3 để sửa Figma hoặc sửa quy tắc.
5. **Chuyển thành luật kiểm:** quy tắc nào kiểm được thì đưa vào `rule.md` để Critic Agent tự bắt lỗi (mục 14.2).

### 0.3 Ba nguyên tắc gốc

Mọi quy tắc bên dưới đều phục vụ ba nguyên tắc này:

| # | Nguyên tắc | Vì sao |
| --- | --- | --- |
| **P1** | **Bác là người quyết định.** App gợi ý, không ra lệnh; con cháu đồng hành, không quản lý. | AI-01: "đồng hành với mình chứ không phải quản lý mình"; AI-02, AI-03, AI-06; D29 |
| **P2** | **Nhìn là hiểu, chạm là xong.** Ít chữ, nhiều icon có nhãn, màu thói quen tươi để nhận ra ngay, mỗi màn một việc, không phải đoán, không phải vuốt. | [T] "ít chữ", "dùng icon nhiều", "màu sắc bắt mắt", "căn giữa", "không kéo trượt", "tập trung vào việc click"; PP02, PP08, PP09, PP010, PP013; W-WAI (giảm trí nhớ ngắn hạn, khéo tay) |
| **P3** | **Nói thật, không gây áp lực.** Không chấm điểm, không trách, không hứa điều app không làm được. | AI-04, AI-05: "app cứ nhắc mình chưa hoàn thành mục tiêu làm mình thấy bị áp lực"; D7, D27, D31 |

---

## 1. Giọng nói và tính cách

An Nhiên nói chuyện như **một người cháu lễ phép, ân cần, nói ngắn gọn**: không như máy móc, cũng không như bác sĩ hay thầy giáo. `[N]` (chọn hình ảnh "người cháu" vì gần với cách con cháu viết gợi ý trong AI-01, AI-03)

| Nên | Không nên | Nguồn |
| --- | --- | --- |
| **Ấm áp, kính trọng**: "Chào buổi sáng, Bác Lan" | Lạnh, kỹ thuật: "Xin chào người dùng" | AI-01, AI-02 (thích lời "mang tính cá nhân") |
| **Ngắn, rõ việc**: "Đến giờ đi bộ rồi Bác ơi" | Dài, giải thích: "Hệ thống ghi nhận đã đến thời điểm thực hiện hoạt động vận động…" | [T] "chữ nhiều"; PP02; AI-03 ("đọc quá nhiều chữ, chắc mẹ sẽ bỏ") |
| **Gợi ý, mời**: "Bác thử đi bộ 15 phút nhé?" | Ra lệnh: "Hãy đi bộ ngay!" | P1; AI-02 ("không muốn sinh hoạt theo một thời khóa biểu quá cứng nhắc") |
| **Động viên nhẹ**: "Hôm nay Bác đã đi bộ rồi, tốt quá!" | Khen quá lố, so sánh: "Bác giỏi hơn 80% người dùng!" | D7; AI-04 ("không muốn thấy bảng xếp hạng") |
| **Bình thường hóa việc bỏ qua**: "Không sao, để hôm khác nhé." | Trách: "Bác đã bỏ lỡ 3 việc hôm nay." | P3; AI-05, AI-06 |
| **Thật thà**: "An Nhiên đã mở Zalo. An Nhiên chưa biết tin đã gửi hay chưa." | Hứa sai: "Đã gửi cho Mai!" | D27; W-NNG (người lớn tuổi tự trách mình khi app sai) |

---

## 2. Xưng hô

| Quy tắc | Chi tiết | Nguồn |
| --- | --- | --- |
| **SG-01** App gọi người dùng theo lựa chọn ở S02 | Mặc định **"Bác"**; nếu chọn ở S02 thì dùng **"Ông" / "Bà"** trên **toàn app**, không trộn lẫn | DESIGN.md gốc mục 2.7; `[N]` (chọn "Bác" làm mặc định vì không phân biệt giới và tuổi người nói) |
| **SG-02** Gọi kèm tên ở lời chào và lời nhắc | "Chào buổi sáng, **Bác Lan**"; các câu khác chỉ cần "Bác" | AI-02 (thông báo "mang tính cá nhân hơn nhiều") |
| **SG-03** App tự xưng là **"An Nhiên"** | Không xưng "tôi", "hệ thống", "ứng dụng" | `[N]` (tên riêng thân thiện hơn "hệ thống"; dùng sẵn ở S17b, N10) |
| **SG-04** Tin gửi cho người thân dùng xưng hô gia đình | Gửi con: "**Mẹ** – **con**"; gửi cháu: "**Bà** – **cháu**"; chọn theo quan hệ ở S12 | Flow 9 (`ux/user-flow.md`); AI-01 |
| **SG-05** Lời gợi ý của con giữ **nguyên văn và tên người gửi** | "**Mai** gợi ý: *Mẹ ơi 3 giờ chiều mẹ đi bộ với cô Tám nhé*" | AI-01, AI-02 (gợi ý từ con có ý nghĩa hơn thông báo máy) |
| **SG-06** Chế độ Người thân gọi người lớn tuổi theo quan hệ | "Lịch của **mẹ**", "Gửi lịch cho **mẹ**" | C03 – C09 |

---

## 3. Câu chữ

| Quy tắc | Nên | Không nên | Nguồn |
| --- | --- | --- | --- |
| **SG-07** **Ít chữ:** câu ≤ 15 tiếng; nhãn nút ≤ 5 tiếng; nhãn tab / icon ≤ 3 tiếng; thẻ việc ≤ 1 dòng phụ; giải thích dài để ở màn chi tiết + "Đọc to" | "Đi bộ quanh công viên" · "20 phút" | Đoạn văn 4 dòng trên thẻ; khối "Lời khuyên hôm nay" trên màn Hôm nay | [T] "ít chữ"; PP02; AI-03 ("đọc quá nhiều chữ, chắc mẹ sẽ bỏ"); W-WAI (khó tập trung) |
| **SG-08** Việc quan trọng nói trước | "**9:30 sáng** · Đi bộ" | "Hoạt động đi bộ được lên lịch vào lúc 9:30 sáng" | PP02 (làm nổi bật hành động quan trọng) |
| **SG-09** 100 % tiếng Việt có dấu, không viết tắt | "Thứ Hai", "phút" | "T2" (trên màn người lớn tuổi), "ph", "Mon", "OK", "Done" | D6; rule.md R-LANG-01 |
| **SG-10** Giờ viết kiểu nói hằng ngày | "**9:30 sáng**", "**3 giờ chiều**", "**8 giờ tối**" | "09:30", "15:00", "21h" | `[N]` (người lớn tuổi quen chia buổi sáng/chiều/tối; D8 chia ngày theo buổi) |
| **SG-11** Ngày viết đủ thứ + ngày/tháng | "**Thứ Sáu, 9/10**"; "**Hôm nay**", "**Ngày mai**" | "09/10/2026", "Fri" | D8 |
| **SG-12** Số đếm bằng chữ số, đơn vị đầy đủ | "**20 phút**", "**3 việc**" | "hai mươi phút", "20'" | `[N]` (chữ số nhận ra nhanh hơn khi lướt) |
| **SG-13** Không cắt chữ bằng "…" | Tên việc dài thì xuống dòng | "Ăn sáng vừa …" | D6; WCAG 1.4.4 |
| **SG-14** Không dùng từ chuyên môn, tiếng Anh, khái niệm trừu tượng | "Lời nhắc", "Việc", "Thư giãn mỗi ngày" | "Notification", "Task", "Down Shift", "Hara hachi bu" | [T] "từ vựng thân thiện với người già"; D23; danh sách đầy đủ ở `vocabulary.md` |
| **SG-15** Hướng dẫn ngắn, đặt đúng chỗ cần | 1 câu gợi ý ngay dưới ô nhập: "Ví dụ: Đi bộ buổi sáng" | Trang hướng dẫn dài, carousel giới thiệu | PP02 ("hướng dẫn ngắn, từng bước và đúng lúc") |

---

## 4. Nhãn nút

| Quy tắc | Nên | Không nên | Nguồn |
| --- | --- | --- | --- |
| **SG-16** Nhãn = **động từ + việc**, nói đúng điều sẽ xảy ra | "**Lưu việc này**", "**Gửi lịch cho mẹ**", "**Gọi điện**" | "OK", "Xác nhận", "Tiếp" (khi không rõ tiếp đi đâu) | D9 (nhãn phải đúng hành động); W-WCAG 2.5.3, 3.2.4 |
| **SG-17** Mỗi màn **1 nút chính** | "Đã xong" là nút filled duy nhất ở S03 | 2 nút màu đậm tranh nhau | PP02; [01]; D21; rule.md R-ONE-01 |
| **SG-18** Nút xác nhận nhắc lại đúng việc | "**Đúng, đã xong**" / "**Chưa, để sau**" | "Có" / "Không" | `[N]` (người tay run bấm nhầm vẫn hiểu mình vừa chọn gì); D2 |
| **SG-19** Trong hộp hỏi lại, **nút an toàn là nút chính** khi hậu quả khó lấy lại | "**Không xóa, giữ lại**" (nút chính) · "Xóa khỏi lịch" (nút viền đỏ) | "Xóa" là nút đậm, nằm trên cùng | D15, D26; W-WCAG 3.3.4 |
| **SG-20** Hai nút trong hộp thoại xếp **dọc**, rộng hết màn | Nút chính trên, nút phụ dưới, cách ≥ 8 | 2 nút nhỏ đặt cạnh nhau | PP08-Keypad (khoảng cách tránh bấm nhầm); design-decisions "Nút xếp dọc trong dialog" |
| **SG-21** Nút "Quay lại" luôn có chữ | "‹ **Quay lại**" | Chỉ có mũi tên ← | PP02; rule.md R-NAV-02 |
| **SG-22** Bộ nhãn cố định cho lời nhắc | "**Bắt đầu làm**" · "**Nhắc lại sau 10 phút**" · "**Hôm nay bỏ qua**" | Mỗi màn một kiểu chữ khác nhau | Checklist research ("Đã hoàn thành" và "Nhắc lại sau"); S14; W-WCAG 3.2.4 |

---

## 5. Câu mẫu theo tình huống

Stitch và Figma dùng nguyên các câu này (thay phần trong `{ }`).

| Tình huống | Mẫu câu | Nguồn |
| --- | --- | --- |
| **Lời chào** (S03) | "Chào buổi {sáng/chiều/tối}, {Bác} {Lan}" · dòng phụ: "{Thứ Năm, 8/10} · Đã xong {3}/{6} việc" | AI-02; D7 (chỉ đếm trong ngày) |
| **Việc tiếp theo** | "Việc tiếp theo · {9:30 sáng}" / "{Đi bộ quanh công viên}" / "{20 phút} · {Vận động tự nhiên}" | D4 |
| **Lời nhắc** (S14) | "Còn {10} phút nữa" / "{Đi bộ quanh công viên}" / "{9:30 sáng}" | D14 |
| **Hỏi lại khi đánh dấu xong** | "{Bác} đã {đi bộ} xong rồi chứ?" → "Đúng, đã xong" / "Chưa, để sau" | D2; PP02 |
| **Xong việc** (snackbar) | "Đã ghi: {Đi bộ} xong lúc {9:42 sáng}." + **Hoàn tác** | PP02, PP03 (tín hiệu rõ sau mỗi lần bấm, sửa được khi sai) |
| **Xong cả ngày** | "Hôm nay {Bác} đã làm xong {6} việc. Nghỉ ngơi thôi!" + "Báo tin vui cho {Mai}" | D18 |
| **Dời việc** | "Dời việc này đến lúc nào?" → "30 phút nữa" / "Chiều nay" / "Ngày mai" / "Không dời nữa" · snackbar: "Đã dời {Đi bộ} sang {chiều nay, 4 giờ}." | D9, D16 |
| **Bỏ qua** | "Bỏ qua {đi bộ} hôm nay?" · "Vì sao? (không bắt buộc)" → "Trời mưa" / "Mệt" / "Bận" / "Lý do khác" · snackbar: "Không sao, để hôm khác nhé. · Hoàn tác" | D16; P3; AI-02 (trời mưa) |
| **Gợi ý thay thế** (khi bỏ qua vì mưa) | "Trời mưa thì {Bác} thử {tập thở chậm 10 phút} trong nhà nhé?" → "Thêm vào lịch" / "Thôi, để hôm khác" | AI-02; PRD F16 |
| **Gợi ý từ người thân** (G11) | "{Mai} gửi lịch cho {Bác}" / lời nhắn nguyên văn của {Mai} / "Chưa thêm vào lịch. {Bác} tự chọn việc và giờ phù hợp." | D29; AI-01 |
| **Lỗi nhập** (3 phần) | ⓘ "{Bác} chưa nhập tên việc." / "Ví dụ: Đi bộ buổi sáng" / chip gợi ý | W-WCAG 3.3.1, 3.3.3; W-NNG (giải thích lỗi, sửa dễ) |
| **Lỗi hệ thống** (3 điều) | "Chưa thể lưu trên điện thoại." / "Nội dung đang nhập vẫn được giữ lại." / "Thử lại" · "Quay lại sửa" | design-decisions "Lỗi luôn nói 3 điều"; D31 |
| **Màn trống** | "{Bác} chưa có việc nào cho hôm nay." / "Thêm việc đầu tiên" · "Dùng lịch mẫu" | Flow 1; AI-06 ("mở lên là biết hôm nay mình có thể làm gì") |
| **Xin quyền nhắc việc** | "Để đến giờ điện thoại đổ chuông nhắc {Bác}." / "Điện thoại sẽ hỏi lại, {Bác} chọn **Cho phép**." | D13 |
| **Chia sẻ cho con** | "{Mẹ} đi bộ xong rồi, hôm nay vui lắm!" (soạn sẵn, Bác chọn thêm câu) | AI-01, AI-02, AI-03 |
| **Rủ con** | "Chủ nhật này {con} rảnh thì qua đi bộ với {mẹ} nhé?" | AI-01; PRD F14 |

---

## 6. Trạng thái: nhìn vào là biết làm hay chưa làm

`[T]` "Nhìn vào là bik làm hay chưa làm" · PP02 · W-WCAG 1.4.1 · D2, D10

**SG-23** Mỗi việc **luôn** hiện trạng thái bằng **icon + chữ + màu** (màu chỉ là tín hiệu phụ), đặt **ngay cạnh tên việc**. Chỉ dùng đúng 5 nhãn sau:

| Trạng thái | Icon | Chữ | Nền | Nguồn |
| --- | --- | --- | --- | --- |
| Đã làm xong | ✓ | **Đã xong** | `primary-container` (xanh nhạt) | D2 |
| Chưa tới giờ / chưa làm | ○ | **Chưa làm** | `warning-container` (vàng nhạt) | [T] |
| Đang đến giờ | 🔔 | **Đến giờ** | `primary` viền đậm | S14 |
| Đã dời | ↻ | **Đã dời · {4 giờ chiều}** | `surface` viền | D16 |
| Bỏ qua | ✕ | **Bỏ qua · {lý do}** | `surface` viền | D10 |

**SG-24** Tiến độ trong ngày ghi bằng chữ "**Đã xong 3/6 việc**", không dùng phần trăm, không vòng tròn không nhãn. (D2, D7)

---

## 7. Bố cục và căn chỉnh

`[T]` "Căn giữa" · PP02 · PP07 · D4

| Quy tắc | Chi tiết | Nguồn |
| --- | --- | --- |
| **SG-25** **Căn giữa** nội dung cần chú ý một mình | Lời nhắc S14, hộp hỏi lại, màn trống, màn "Đã lưu / Đã gửi", lời chúc xong cả ngày, chọn cỡ chữ S01 | [T]; `[N]` (căn giữa khi màn chỉ có 1 thông điệp để mắt tập trung) |
| **SG-26** **Căn trái** danh sách và nội dung đọc theo dòng | Danh sách việc, lịch tuần, form, chi tiết thói quen | `[N]` (chữ tiếng Việt đọc từ trái; căn giữa nhiều dòng làm mắt khó tìm đầu dòng – W-WAI "Understandable Content") |
| **SG-27** Nút chính **ở cùng một chỗ** trên mọi màn | Đáy màn, rộng hết chiều ngang trừ lề 20 | PP07 (vị trí nút ảnh hưởng thao tác); W-NNG (tránh đổi điều hướng đột ngột) |
| **SG-28** Thứ tự đọc trên mỗi màn | Tiêu đề (đang ở đâu) → nội dung chính (việc gì, mấy giờ) → nút chính (làm gì) | PP02; W-WCAG 2.4.6 |
| **SG-29** Ít lựa chọn mỗi màn | Tối đa 3 lựa chọn ngang hàng; còn lại vào "Xem thêm" | PP010 (điều hướng phức tạp tăng gánh nặng nhận thức); D23 |

---

## 8. Icon

| Quy tắc | Chi tiết | Nguồn |
| --- | --- | --- |
| **SG-30** Icon **luôn có chữ** đi kèm | 🔔 Lời nhắc · 📞 Gọi điện · 💬 Nhắn tin · 📅 Lịch tuần · 🌿 Thói quen · 👪 Gia đình · ⚙ Cài đặt · 🔊 Đọc to | PP08-Icon; PP09; rule.md R-ICON-01 |
| **SG-31** Chỉ dùng icon **quen thuộc, cụ thể** | Chuông, điện thoại, lịch, lá cây, người | PP09 ("không nên dùng icon trừu tượng mà không có giải thích") |
| **SG-32** Một icon = một nghĩa trong toàn app | Chuông chỉ dùng cho lời nhắc | W-WCAG 3.2.4 Consistent Identification |
| **SG-52** **Dùng icon nhiều:** mọi việc, mọi thói quen, mọi tab, mọi nút chính, mọi mục cài đặt đều có icon (≥ 32 px; ô icon thói quen 48 × 48) | Nên: thẻ việc có 🚶 ô xanh + "Đi bộ". Không nên: danh sách việc chỉ có chữ | [T] "dùng icon nhiều"; PP09 (icon + chữ lớn giúp tìm nhanh hơn); [01] |
| **SG-53** **Icon thay câu, không thay nhãn** | Nên: icon 🍵 + "Trà chiều cùng bạn" thay cho câu "Uống trà với bạn bè giúp gắn kết…". Không nên: chỉ icon 🍵 không chữ | PP08-Icon (nhãn chữ giúp hiểu icon); W-CHI ("pair icons with text labels") |

## 8b. Màu sắc

[T] "màu sắc bắt mắt" · PP013 (ưa màu sáng, tông ấm) · PP012 (tương phản cao) · W-WCAG 1.4.1, 1.4.11

| Quy tắc | Chi tiết | Nguồn |
| --- | --- | --- |
| **SG-54** **Mỗi thói quen một màu nhấn tươi**, dùng ở mảng nhỏ: ô icon 48 × 48 (icon trắng), vạch 6 px bên trái thẻ việc, chấm màu ở lịch tuần | 9 màu `habit-*-accent` trong DESIGN.md (mỗi màu ≥ 3 : 1 với nền) | [T]; PP013; `[N]` (đặt màu tươi ở mảng nhỏ để vẫn giữ nền sáng, chữ rõ) |
| **SG-55** Không đặt chữ dài trên màu nhấn; chữ luôn trên nền trắng / nền app | Tên việc nằm cạnh ô icon màu | PP012 (chữ đậm, tương phản cao); W-WCAG 1.4.3 |
| **SG-56** Trạng thái dùng màu **đậm** để nhìn là biết | ✓ Đã xong = chip xanh đậm chữ trắng; ○ Chưa làm = vòng vàng đậm | [T] "nhìn vào là biết làm hay chưa làm" |
| **SG-57** Cùng thói quen cùng màu ở mọi màn; không tự chế màu, không neon, không gradient | Vận động luôn xanh lá #2BA15C | W-WCAG 3.2.4; PP013 (tránh quá chói) |
| **SG-58** Màu chỉ là tín hiệu phụ | Luôn có icon + chữ đi kèm | W-WCAG 1.4.1; W-MIIT (không dùng màu làm cách duy nhất truyền tin) |

---

## 9. Tương tác

`[T]` "không kéo trượt", "tập trung vào việc click" · PP02 · W-WCAG 2.5.1, 2.5.7

| Quy tắc | Chi tiết | Nguồn |
| --- | --- | --- |
| **SG-33** **Chỉ cần chạm** | Mọi hành động làm được bằng 1 lần chạm vào nút có chữ. Không vuốt để xóa, không kéo thả, không nhấn giữ, không chạm 2 lần, không vuốt để tắt lời nhắc | [T]; PP02; W-WCAG 2.5.1, 2.5.7; D14 |
| **SG-34** Chọn thay vì gõ | Chọn từ danh sách, chip gợi ý, danh bạ; giờ chọn bằng ô bấm | PP02 (hạn chế bàn phím ảo); AI-06 ("không muốn nhập quá nhiều thông tin"); D12, D22 |
| **SG-35** **Phản hồi sau mỗi lần chạm** | Nút đổi màu khi nhấn; sau khi đổi dữ liệu luôn có snackbar nói rõ vừa làm gì | PP02, PP03 |
| **SG-36** **Mọi thay đổi đều có đường lui** | Khó lấy lại → hỏi lại trước; đã làm → "Hoàn tác" | PP02 ("cần có cách sửa thao tác sai"); D15, D16; W-WCAG 3.3.4 |
| **SG-37** **Không ép thời gian** | Snackbar "Hoàn tác" và popup gợi ý **không tự tắt**; không đếm ngược | PP010 ("thao tác chậm không đồng nghĩa trải nghiệm kém"); W-WCAG 2.2.1; D16 |
| **SG-38** Đếm số bước | Đánh dấu xong ≤ 2 chạm; nhận gợi ý của con ≤ 2 chạm | PRD M1, M6; AI-05 ("mỗi lần hoàn thành phải thao tác nhiều bước" → xóa app) |

---

## 10. Giọng đọc (Voice)

`[T]` "Voice" · [01] (hỗ trợ giọng nói) · W-WAI (thị lực giảm)

| Quy tắc | Chi tiết | Nguồn |
| --- | --- | --- |
| **SG-39** Nút "**🔊 Đọc to**" có chữ | Có ở S14 Lời nhắc, S04 Chi tiết việc, S16 Chi tiết thói quen, G03 Gợi ý từ con | [T]; [01] |
| **SG-40** Lời nhắc **tự đọc to** khi đến giờ (tắt được ở Cài đặt) | Đọc: "{Bác Lan} ơi, {9 giờ 30} rồi, đến giờ {đi bộ quanh công viên}." | D14; `[N]` (đọc cả tên để người nghe biết là gọi mình) |
| **SG-41** Viết câu **để đọc lên được** | Giờ viết "9:30 sáng" để đọc thành "9 giờ 30 sáng"; không đặt ký hiệu (·, /, %) vào giữa câu sẽ được đọc | `[N]` (TTS tiếng Việt đọc ký hiệu sai) |
| **SG-42** Khi đang đọc thì hiện trạng thái bằng chữ | "🔊 **Đang đọc to…**" + nút "**Dừng đọc**" | W-WCAG 1.4.2 Audio Control |
| **SG-43** Giọng đọc chậm, rõ; cho chọn tốc độ "Chậm / Vừa" | Mặc định "Chậm" | W-WAI (khó nghe âm cao, khó tách âm); `[N]` |

---

## 11. Thông báo

PP02 · AI-02, AI-03, AI-05, AI-06 (cả 4 vai đều nói "quá nhiều thông báo" là lý do xóa app)

| Quy tắc | Chi tiết | Nguồn |
| --- | --- | --- |
| **SG-44** Mỗi việc nhắc **1 lần** + nhiều nhất **1 lần nhắc lại** do Bác chọn | Không tự nhắc lại khi Bác không phản hồi | PP02 ("tự điều chỉnh mức thông báo thay vì mặc định nhắn liên tục"); AI-02 |
| **SG-45** Bác chọn **khung giờ được nhắc** | Ngoài khung giờ, App im lặng | AI-05, AI-06 |
| **SG-46** Gợi ý từ con: tối đa **2 lần/ngày** | Quá số đó thì gom vào thẻ "Gợi ý từ {Mai}" ở đầu Hôm nay, không hiện popup | AI-01 ("nếu con gửi gợi ý liên tục… cô cũng sẽ thấy hơi phiền"); `[N]` (con số 2 cần kiểm chứng – PRD Q3) |
| **SG-47** Không gửi thông báo để kéo người dùng mở app | Không có "Lâu rồi Bác chưa mở An Nhiên" | AI-04 ("đừng đánh giá thành công chỉ bằng số lượt mở ứng dụng"); P3 |

---

## 12. Gia đình và riêng tư

AI-01, AI-02, AI-03 · D29

| Quy tắc | Nên | Không nên | Nguồn |
| --- | --- | --- | --- |
| **SG-48** Lời của app với con cháu là **gợi ý**, không phải **giao việc** | "Gửi **gợi ý** cho mẹ", "Mẹ sẽ tự chọn nhận hay không" | "Giao việc cho mẹ", "Theo dõi mẹ" | AI-01, AI-06; D29 |
| **SG-49** Không có câu nào báo cho con việc Bác **không làm** | — | "Mẹ đã bỏ qua 2 việc hôm nay" | AI-01, AI-02, AI-03; PRD FR08 |
| **SG-50** Khi chia sẻ, nói rõ **ai sẽ thấy gì** | "Mai sẽ thấy: Mẹ đi bộ xong lúc 9:42 sáng." | Chia sẻ ngầm | AI-03 ("Cha/mẹ chủ động chọn thông tin muốn chia sẻ") |
| **SG-51** Ghép nối, lập lịch dùng từ ngữ an tâm | "Mẹ nhận trước khi thêm" (bật sẵn) | "Tự động thêm vào máy mẹ" | D30 |

---

## 13. Không bao giờ

Tổng hợp từ P3, D7, D7b, AI-04, AI-05, rule.md R-LANG-03.

- Bảng xếp hạng, so sánh với người khác, "chuỗi ngày", "mất chuỗi", điểm sức khỏe, điểm tuổi thọ.
- Câu trách, gây lo lắng: "Bạn chưa hoàn thành mục tiêu", "Bác đã bỏ lỡ…", "Sức khỏe của Bác đang giảm".
- Từ y tế không có căn cứ: "chữa", "phòng bệnh", "kéo dài tuổi thọ".
- Nút SOS / "Gọi khẩn cấp" (app không bảo đảm được chức năng cấp cứu – D7b).
- Chữ tiếng Anh, chữ không dấu, viết tắt.
- Icon không có chữ; nút "OK", "Có", "Không".
- Thao tác vuốt, kéo, nhấn giữ là cách duy nhất.
- Báo "Đã gửi" khi app chỉ mở Zalo / SMS.

---

## 14. Kiểm tra

### 14.1 Checklist cho mỗi màn (người hoặc Critic Agent)

| # | Câu hỏi | Quy tắc |
| --- | --- | --- |
| 1 | Xưng hô đúng một kiểu (Bác / Ông / Bà) trên cả màn? | SG-01 |
| 2 | Có câu nào > 15 tiếng, nút nào > 5 tiếng, thẻ nào quá 1 dòng phụ? | SG-07 |
| 3 | Giờ, ngày viết kiểu nói hằng ngày? | SG-10, SG-11 |
| 4 | Mọi nút là động từ + việc; chỉ 1 nút chính? | SG-16, SG-17 |
| 5 | Mỗi việc có nhãn trạng thái icon + chữ? | SG-23 |
| 6 | Nội dung đứng một mình được căn giữa, danh sách căn trái? | SG-25, SG-26 |
| 7 | Mọi việc / thói quen / tab / nút chính có icon, và icon nào cũng có chữ? | SG-30, SG-52, SG-53 |
| 7b | Mỗi thẻ việc có ô icon + vạch màu đúng màu thói quen? Chữ không nằm trên màu nhấn? | SG-54, SG-55, SG-57 |
| 8 | Có chỗ nào phải vuốt / nhấn giữ? | SG-33 |
| 9 | Sau thao tác đổi dữ liệu có phản hồi + Hoàn tác? | SG-35, SG-36 |
| 10 | Màn có nội dung chính có nút "Đọc to"? | SG-39 |
| 11 | Có chữ nào thuộc mục 13 "Không bao giờ"? | Mục 13 |

### 14.2 Đã đưa vào `rule.md` (17/10/2026)

| Luật trong rule.md | Mức | Từ quy tắc |
| --- | --- | --- |
| R-TXT-03 Câu ≤ 15 tiếng, đoạn ≤ 2 dòng | error | SG-07 |
| R-TXT-04 Nhãn nút ≤ 5 tiếng, nhãn tab/icon ≤ 3 tiếng | error | SG-07 |
| R-TXT-05 Thẻ việc chỉ gồm icon · giờ · tên · trạng thái | error | SG-07, SG-52 |
| R-TXT-06 Không khối chữ giải thích trên Hôm nay | warn | SG-07 |
| R-ICON-02 Mọi việc / thói quen / nút chính / tab / mục cài đặt có icon | error | SG-52 |
| R-ICON-03 Icon quen thuộc, ≥ 32 px, một nghĩa | warn | SG-31, SG-32 |
| R-COL-02 Ô icon màu nhấn + vạch màu trên thẻ | error | SG-54 |
| R-COL-03 Đúng 9 màu nhấn, cùng thói quen cùng màu | warn | SG-57 |
| R-COL-04 Không chữ dài trên màu nhấn, không neon / gradient | warn | SG-55, SG-57 |
| R-STA-01 5 nhãn trạng thái icon + chữ | error | SG-23, SG-56 |
| R-STA-02 Tiến độ bằng chữ | warn | SG-24 |
| R-CEN-01 Căn giữa / căn trái | warn | SG-25, SG-26 |
| R-VOI-01 Nút "Đọc to" | error | SG-39 |
| R-VOC-01 Không từ "Tránh dùng" | error | SG-14 |
| R-LANG-02 Xưng hô thống nhất, không "OK / Có / Không" | warn | SG-01, SG-16, SG-18 |

### 14.3 Đối chiếu với Figma hiện tại – chỗ cần sửa

| Chỗ lệch | Quy tắc | Đề xuất |
| --- | --- | --- |
| Có màn dùng "Bà" (DLG-Done "Bà đã đi bộ xong rồi chứ?"), có màn dùng "Bác" (S05 "Bác muốn làm gì?") | SG-01 | Lấy theo xưng hô chọn ở S02; trong bản demo bà Lan thống nhất "Bà" hoặc "Bác" |
| Flow 3 ghi "con gái nhận tin" khi xong việc | SG-49, SG-50 | Đổi thành chia sẻ do Bác bấm (PRD Q5) |
| Lịch tuần của người thân (C07) dùng "T2-T4-T6" | SG-09 | Được giữ ở màn của người thân (người trẻ, chỗ hẹp); màn của người lớn tuổi phải ghi "Thứ Hai" |
| Nhãn "Chưa làm" chưa có trong component `TaskRow` (mới có Upcoming / Done / Skipped) | SG-23 | Thêm chữ "○ Chưa làm" cho state Upcoming |
| Thẻ việc trong Figma chưa có ô icon màu nhấn và vạch màu thói quen | SG-54 | Thêm vào component `TaskRow` / `TaskCard` |
| Màn Hôm nay còn khối chữ lời khuyên (nếu có) | SG-07 | Chuyển sang S16 + "Đọc to" |
| Đọc to đã có ở S14 (Flow 6 "đang đọc to"); chưa thấy ghi cho S04, S16, G03 trong tài liệu | SG-39 | Kiểm tra trong Figma; thiếu thì thêm nút "🔊 Đọc to" |

---

## 15. Nguồn tham khảo

**Góp ý của thầy**
- Ghi chép buổi góp ý 16/10/2026 – `ai/feedback-thay-2026-10-16.md`.

**Nghiên cứu (tóm tắt trong `research/`)**
- [01] Optimizing Mobile App Design for Older Adults (2025) – tổng quan 132 tài liệu.
- PP02 – Design Guidelines of Mobile Apps for Older Adults (2023) – 40 bài.
- PP03 – Developing a Multiprofessional Mobile App to Enhance Health Habits (2024).
- PP04 – How to Design Font Size for Older Adults (2022).
- PP07 – Impact of Button Position and Touchscreen Font Size (2020) – 64 người.
- PP08 – Effects of Smartphone Numeric Keypad Designs on Elderly Users (51 người); Developing Icons for Older Adults (51 người).
- PP09 – Designing Combinations of Pictogram and Text Size for Icons.
- PP010 – Influence of Mobile Navigation Design on Older Adults (2026).
- PP012 – Human Factors in Visual Information Design for Older Adults.
- PP06, PP011 – Caregivers & older adults (2026, 2019).

**Chuẩn và tài liệu công khai**
- W3C. *Web Content Accessibility Guidelines (WCAG) 2.2*, 2023 – https://www.w3.org/TR/WCAG22/ (dùng: 1.4.1 Use of Color, 1.4.2 Audio Control, 1.4.4 Resize Text, 2.2.1 Timing Adjustable, 2.4.6 Headings and Labels, 2.5.1 Pointer Gestures, 2.5.3 Label in Name, 2.5.7 Dragging Movements, 3.2.4 Consistent Identification, 3.3.1 Error Identification, 3.3.3 Error Suggestion, 3.3.4 Error Prevention).
- W3C WAI. *Older Users and Web Accessibility: Meeting the Needs of Ageing Web Users*, cập nhật 20/11/2025 – https://www.w3.org/WAI/older-users/
- Nielsen, J. *Usability for Senior Citizens: Improved, But Still Lacking*. Nielsen Norman Group, 28/5/2013 – https://www.nngroup.com/articles/usability-seniors-improvements/ (người 65+ tự trách mình khi gặp lỗi 90 % số lần; cần thông báo lỗi rõ, sửa dễ; tránh đổi điều hướng đột ngột).

**Bộ rule thiết kế cho người cao tuổi đã công bố** (dùng để đối chiếu)
- Centre for Healthcare Innovation, Tan Tock Seng Hospital (Singapore). *CHI App Guidelines and Examples*, 2022 – https://child.chi.sg/files/pdffiles/chi_app_guidelines.pdf (chữ ≥ 16 pt, giãn dòng ≥ 1,5, vùng chạm ≥ 48 dp, icon kèm nhãn, một chạm cho mỗi hành động, tránh giới hạn thời gian).
- Bộ Công nghiệp và Công nghệ Thông tin Trung Quốc (MIIT). *Quy chuẩn chung thiết kế App thân thiện người cao tuổi* (移动互联网应用（App）适老化通用设计规范), 4/2021 – tin công bố: https://www.ithome.com/0/544/652.htm (cho chỉnh cỡ chữ, giãn dòng ≥ 1,3, không dùng màu làm cách duy nhất, cấm quảng cáo và nút dụ bấm).
- Chisnell, D., Redish, J., Lee, A. *New Heuristics for Understanding Older Adults as Web Users*. Technical Communication 53(1), 2006 – https://www.ingentaconnect.com/contentone/stc/tc/2006/00000053/00000001/art00006 (bộ heuristic do AARP tài trợ).
- Czaja, S., Boot, W., Charness, N., Rogers, W. *Designing for Older Adults*, 3rd ed. CRC Press, 2019.

**Phỏng vấn giả lập** – 6 link ChatGPT, xem `PRD.md` mục 2.

**Quyết định trong repo** – `design-decisions.md` D1 – D31.
