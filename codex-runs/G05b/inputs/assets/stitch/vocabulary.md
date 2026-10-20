# vocabulary.md – Từ vựng An Nhiên

> **Bảng từ vựng thân thiện với người lớn tuổi**: thuật ngữ Power 9 và từ giao diện được Việt hóa thành lời nói đời thường.
> Là 1 trong 4 file input cho Google Stitch: [`PRD.md`](PRD.md) · [`DESIGN.md`](DESIGN.md) · [`AppStyleGuide.md`](AppStyleGuide.md) · **vocabulary.md**.
> Critic Agent dùng **mục 5 (Tránh dùng)** để chạy luật `R-VOC-01` trong `rule.md`.
> Phiên bản 1.0 · 17/10/2026

---

## 0. Nguồn và cách làm

### 0.1 Nguồn

| Mã | Nguồn | Dùng cho |
| --- | --- | --- |
| `[BZ]` | Blue Zones. *Power 9®*. https://www.bluezones.com/power-9/ – trang chính thức của tổ chức Blue Zones (Dan Buettner), không ghi tác giả, ngày; truy cập 17/10/2026 | **Nguồn chính**: tên gốc và nghĩa gốc của 9 nguyên tắc, các từ khóa của người sống thọ |
| `[PDF]` | *Power Nine Principles of Blue Zones* – bản tóm tắt 1 trang (Word, 2019, không ghi người soạn), ghi rõ nội dung của Dan Buettner và National Geographic – `assets/vocabulary/Power-Nine-Principles-of-Blue-Zones.pdf` | Đối chiếu; nội dung khớp với `[BZ]` |
| `[AI]` | Bản dịch máy nguyên văn do **Claude (Opus 5.5)** thực hiện ngày 17/10/2026: dịch từng thuật ngữ đứng riêng, **không cho ngữ cảnh**, không chỉnh sửa | Cột "AI dịch" – cho thấy dịch máy gặp vấn đề gì với người lớn tuổi |
| `[SG]` | `AppStyleGuide.md` | Tiêu chí chọn từ (SG-07 ít chữ, SG-14 không từ chuyên môn) |
| `[AI-0x]` | 6 phỏng vấn giả lập (`PRD.md` mục 2) | Cách người lớn tuổi tự nói về hoạt động của mình |
| `[R]` | Research PP02, PP012 (`research/`) | Câu ngắn, từ quen thuộc |
| `[D-xx]` | `design-decisions.md` | Các lần đổi tên đã có (D1, D3, D18, D23) |
| `[N]` | Nhóm quyết định | Ghi lý do tại chỗ |

> Thuật ngữ gốc có từ sách *The Blue Zones* của Dan Buettner (National Geographic). Nhóm chưa có bản sách nên **trích qua `[BZ]`** – trang chính thức của chính tổ chức do tác giả lập.

### 0.2 Quy trình

```
① Lấy thuật ngữ + nghĩa gốc từ [BZ]  →  ② AI dịch nguyên văn [AI]  →  ③ Soi vấn đề theo 5 tiêu chí
→  ④ Chọn từ trong app + icon  →  ⑤ Đưa vào rule.md (R-VOC-01) và test với người lớn tuổi
```

**5 tiêu chí chọn từ** (bước ③):

| # | Tiêu chí | Nguồn |
| --- | --- | --- |
| C1 | **Lời nói đời thường**, người 65+ nói hằng ngày | [T] "từ vựng thân thiện với người già"; SG-14; PP02 |
| C2 | **Nói rõ việc cần làm**, không phải khái niệm | D23 ("người dùng nghĩ theo việc cụ thể"); PP09 |
| C3 | **Ngắn**: tên thói quen ≤ 4 tiếng, nhãn nút ≤ 5 tiếng | [T] "ít chữ"; SG-07; R-TXT-04 |
| C4 | **Hợp sức khỏe và văn hóa Việt** người lớn tuổi | D1; PRD non-goals |
| C5 | **Không gây hiểu lầm, không áp lực** (không %, không ẩn dụ lạ, không mệnh lệnh) | P3; SG-14 |

---

## 1. Chín nguyên tắc Power 9

Thứ tự theo `[PDF]` và app hiện tại. `[BZ]` xếp 7–8–9 là Right Tribe – Loved Ones First – Belong; nhóm giữ thứ tự cũ để khớp Figma `[N]`.

| # | Thuật ngữ gốc `[BZ]` | Nghĩa theo nguồn `[BZ]` | AI dịch nguyên văn `[AI]` | Vấn đề với người lớn tuổi | **Từ trong app** | Icon | Lý do |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Move Naturally | Môi trường sống khiến người ta vận động liên tục mà không cần nghĩ: làm vườn, tự làm việc nhà, không cần phòng gym | Di chuyển tự nhiên | "Di chuyển" nghe như đi lại, đi xe (C2) | **Vận động tự nhiên** | 🚶 `footprints` | Từ quen; dòng phụ nói rõ việc: "Đi bộ, làm vườn, việc nhà" (C1, C2) |
| 2 | Purpose | "Ikigai" / "plan de vida": lý do để thức dậy mỗi sáng | Mục đích | Một từ trừu tượng, không biết làm gì (C2) | **Sống có mục đích** | 🧭 `compass` | Thêm động từ "sống"; dòng phụ: "Mỗi sáng một việc mình mong làm" (C2) |
| 3 | Downshift | Mỗi ngày có thói quen xả căng thẳng: tưởng nhớ tổ tiên, cầu nguyện, ngủ trưa, gặp bạn | Giảm số / Chuyển xuống số thấp | Ẩn dụ sang số xe, không ai hiểu (C1, C5) | **Thư giãn mỗi ngày** | 🍃 `wind` | Động từ quen, nói rõ việc (C1, C2) |
| 4 | 80% Rule | "Hara hachi bu": dừng ăn khi no khoảng 80 %; bữa nhỏ nhất vào chiều tối | Quy tắc 80% | Người lớn tuổi không nghĩ bữa ăn bằng %; "quy tắc" nghe như luật (C5); bản trước "Ăn vừa no 80%" dễ hiểu thành nhịn ăn (D23) | **Ăn vừa đủ** | 🍚 `utensils` | Lời đời thường, không con số (C1, C5) |
| 5 | Plant Slant | Đậu (đậu tằm, đậu đen, đậu nành, đậu lăng) là nền bữa ăn; thịt ăn ít | Nghiêng về thực vật | Văn viết, "nghiêng" khó hình dung (C1, C2) | **Ăn nhiều rau, đậu** | 🥗 `salad` | Gọi tên món cụ thể; giữ "đậu" vì nguồn nhấn mạnh đậu (C2) |
| 6 | Wine @ 5 | Uống rượu điều độ 1–2 ly mỗi ngày, cùng bạn bè hoặc bữa ăn | Rượu vang lúc 5 giờ | Người lớn tuổi hay dùng thuốc, rượu không an toàn; ký hiệu "@" lạ (C4) | **Trà chiều cùng bạn** | 🍵 `coffee` | Giữ ý cốt lõi "gặp bạn cuối ngày", đổi đồ uống hợp văn hóa Việt (D1, C4) |
| 7 | Belong | 258/263 người trăm tuổi được phỏng vấn thuộc một cộng đồng tín ngưỡng, không kể tôn giáo nào | Thuộc về | Không biết thuộc về cái gì (C2) | **Gắn kết cộng đồng** | 👥 `users` | Mở rộng từ "cộng đồng tín ngưỡng" sang cả chùa, nhà thờ, hội đoàn, câu lạc bộ để không loại người không theo đạo `[N]` |
| 8 | Loved Ones First | Đặt gia đình lên trước: ở gần cha mẹ, ông bà; gắn bó với bạn đời; dành thời gian cho con | Người thân yêu trước tiên | Câu dịch cứng, như văn bản dịch (C1) | **Gia đình trên hết** | 🏠 `house` | Thành ngữ quen trong tiếng Việt (C1) |
| 9 | Right Tribe | Ở trong nhóm bạn có thói quen lành mạnh; người Okinawa lập "moai" – nhóm 5 người bạn gắn bó trọn đời | Bộ lạc phù hợp / Đúng bộ tộc | "Bộ lạc" gây hiểu lầm, nghe như dân tộc thiểu số (C5) | **Bạn bè tích cực** | 🤝 `handshake` | Từ gần gũi (C1) |

Icon ghi theo tên trong bộ **Lucide** (repo đang dùng Lucide, giấy phép ISC, ở `assets/icons/`); emoji chỉ để minh họa.

> **Không đưa con số tuổi thọ lên giao diện.** `[BZ]` ghi "thêm tới 7 năm", "thêm 4–14 năm"… Các số này chỉ để trong file nguồn; app không hứa hẹn về sức khỏe (PRD mục 5).

### 1.1 Câu mô tả một dòng (dùng ở S08, ≤ 15 tiếng)

Viết lại từ `[BZ]` bằng lời đời thường, mỗi câu là một việc làm được ngay.

| # | Thói quen | Câu mô tả trong app | Rút từ `[BZ]` |
| --- | --- | --- | --- |
| 1 | Vận động tự nhiên | Đi bộ, làm vườn, tự làm việc nhà | gardening, no mechanical conveniences |
| 2 | Sống có mục đích | Mỗi sáng có một việc mình mong làm | "why I wake up in the morning" |
| 3 | Thư giãn mỗi ngày | Ngủ trưa, ngồi tĩnh lặng, thắp hương ông bà | nap, pray, honor ancestors |
| 4 | Ăn vừa đủ | Ăn chậm, thấy vừa đủ thì dừng | stop eating at 80 % full |
| 5 | Ăn nhiều rau, đậu | Bữa nào cũng có rau và đậu | beans are the cornerstone |
| 6 | Trà chiều cùng bạn | Uống trà, trò chuyện với bạn lúc chiều | with friends, late afternoon (đổi đồ uống – D1) |
| 7 | Gắn kết cộng đồng | Đi chùa, nhà thờ, sinh hoạt hội, câu lạc bộ | faith-based community (mở rộng) |
| 8 | Gia đình trên hết | Gọi điện, ăn cơm cùng con cháu | keep family nearby, invest time |
| 9 | Bạn bè tích cực | Đi bộ, tập cùng nhóm bạn quen | moai, supportive social circles |

---

## 2. Từ khóa của người sống thọ (từ nguồn `[BZ]`)

Thầy yêu cầu "lấy từ khóa người già trong sách". Đây là các từ khóa xuất hiện trong `[BZ]` và cách app nói lại.

| Từ khóa gốc | Nghĩa theo `[BZ]` | AI dịch `[AI]` | Từ trong app | Dùng ở đâu |
| --- | --- | --- | --- | --- |
| Ikigai (Okinawa) / plan de vida (Nicoya) | Lý do để thức dậy mỗi sáng | Ý nghĩa cuộc sống / Kế hoạch cuộc đời | **Lý do để thức dậy** | S16 thói quen 2 – mục "Học từ đâu" |
| Hara hachi bu | Câu nhắc trước bữa ăn: dừng khi no 80 % | Tám phần mười dạ dày | **Ăn vừa đủ thì dừng** | S16 thói quen 4 |
| Moai | Nhóm 5 người bạn gắn bó với nhau trọn đời | Moai (không dịch) | **Nhóm bạn thân** | S16 thói quen 9; tên nhóm khi rủ bạn (sau MVP) |
| Centenarian | Người sống trên 100 tuổi | Người trăm tuổi | **Người sống trên 100 tuổi** | S16 "Học từ đâu" |
| Blue Zones | Các vùng có nhiều người sống thọ nhất | Vùng Xanh | **Những vùng có nhiều người sống thọ** | S08 dòng giới thiệu; chỉ ghi tên "Blue Zones" trong ngoặc ở mục nguồn |
| Power 9 | 9 thói quen chung của các vùng đó | Sức mạnh 9 | **9 thói quen sống khỏe** | S08 tiêu đề; "Power 9" chỉ trong mục nguồn |
| Honor ancestors | Người Okinawa dành vài phút mỗi ngày tưởng nhớ tổ tiên | Tôn vinh tổ tiên | **Thắp hương ông bà** | Gợi ý việc cho thói quen 3 |
| Nap | Người Ikaria ngủ trưa | Ngủ trưa | **Ngủ trưa** | Gợi ý việc cho thói quen 3 |
| Happy hour | Người Sardinia gặp bạn cuối ngày | Giờ vui vẻ | **Ngồi chơi với bạn** | Gợi ý việc cho thói quen 3, 6 |
| Gardening | Làm vườn – vận động không cần nghĩ | Làm vườn | **Chăm cây, tưới rau** | Gợi ý việc cho thói quen 1 |
| Life partner | Gắn bó với bạn đời | Bạn đời | **Ông / bà nhà mình** | Gợi ý việc cho thói quen 8 (theo xưng hô) |

---

## 3. Từ giao diện

Từ kỹ thuật, tiếng Anh thường gặp trong app lịch → từ An Nhiên dùng. Nhiều từ đã có sẵn trong Figma (cột cuối).

| Từ kỹ thuật / tiếng Anh | AI dịch `[AI]` | **Từ trong app** | Ghi chú | Đã có ở |
| --- | --- | --- | --- | --- |
| Notification / Reminder | Thông báo / Lời nhắc nhở | **Lời nhắc** | Một từ duy nhất cho cả hai | S13, S14 |
| Task / Activity | Nhiệm vụ / Hoạt động | **Việc** | "Nhiệm vụ" nghe như bị giao (P1) | S03, S05 |
| Schedule / Calendar | Lịch trình / Lịch | **Lịch** | | S07, C03 |
| Habit | Thói quen | **Thói quen** | | S08 |
| Today / Home | Hôm nay / Trang chủ | **Hôm nay** | Không dùng "Trang chủ" | Bottom nav |
| Done / Complete | Xong / Hoàn thành | **Đã xong** | Không dùng "Hoàn thành nhiệm vụ" | S03, DLG-Done |
| Pending / To do | Đang chờ / Cần làm | **Chưa làm** | | R-STA-01 |
| Snooze | Báo lại | **Nhắc lại sau 10 phút** | Nói rõ bao lâu | S14 |
| Reschedule / Postpone | Lên lịch lại / Hoãn | **Dời lại** | | DLG-Later |
| Skip | Bỏ qua | **Hôm nay bỏ qua** | Nói rõ chỉ hôm nay | S14, DLG-Skip |
| Undo | Hoàn tác | **Hoàn tác** | Giữ – đã quen trên Zalo; luôn đi kèm câu nói rõ vừa làm gì | Snackbar |
| Save / Edit / Delete | Lưu / Chỉnh sửa / Xóa | **Lưu · Sửa · Xóa** | Kèm tên việc: "Lưu việc này", "Xóa khỏi lịch" | S06, S15 |
| Cancel / OK | Hủy / Đồng ý | **Hủy / Xong** · hoặc động từ cụ thể | Không dùng "OK" (SG-16) | DLG-TaskTime |
| Settings | Cài đặt | **Cài đặt** | | S10 |
| Profile | Hồ sơ | **Thông tin của Bác** | "Hồ sơ" nghe như giấy tờ `[N]` | N06 |
| Font size | Cỡ phông chữ | **Cỡ chữ** | | S01, S10 |
| Text-to-speech | Chuyển văn bản thành giọng nói | **Đọc to** | | S14, R-VOI-01 |
| Family member / Caregiver | Thành viên gia đình / Người chăm sóc | **Người thân** | Không dùng "người chăm sóc" – Bác tự chủ (P1) | S09, C01 |
| Pair / Link device | Ghép nối / Liên kết thiết bị | **Ghép nối với máy của mẹ** | Màn người thân | C02 |
| Suggestion / Recommendation | Đề xuất / Khuyến nghị | **Gợi ý** | | G01 – G12 |
| Accept / Decline | Chấp nhận / Từ chối | **Thêm vào lịch / Bỏ qua** | Nói rõ hậu quả | G03 |
| Share | Chia sẻ | **Báo tin cho {Mai}** / **Gửi ảnh cho con** | | S17 |
| Sync / Backup | Đồng bộ / Sao lưu | **Lưu trên điện thoại** | Nói đúng sự thật (D31) | N20 |
| Error / Failed | Lỗi / Thất bại | **Chưa … được** ("Chưa thể lưu") | Không dùng "Lỗi", "Thất bại" ở đầu câu | ST-Error |
| Permission | Quyền | **Cho phép** | | S13 |
| Progress | Tiến độ | **Đã xong 3/6 việc** | Không phần trăm | S03 |
| Achievement / Badge | Thành tích / Huy hiệu | **Cột mốc** | Nếu có (PRD F18); không "thành tích" | — |

---

## 4. Xưng hô và cách gọi người

| Tránh | Dùng | Lý do |
| --- | --- | --- |
| Người già, cụ già, người cao tuổi (trên giao diện) | **Bác / Ông / Bà** + tên | Gọi theo lựa chọn ở S02 (SG-01); "người già" nghe xa cách `[N]` |
| Người dùng, bạn, quý khách | **Bác** | SG-01 |
| Người chăm sóc, người giám hộ | **Người thân**, **con**, **cháu** | P1 – không ngầm ý Bác cần bị trông nom |
| Hệ thống, ứng dụng, tôi | **An Nhiên** | SG-03 |

---

## 5. Tránh dùng

Danh sách cho luật `R-VOC-01`. Critic Agent tìm các từ dưới đây trong chữ hiển thị của output Stitch (không phân biệt hoa thường). **Ngoại lệ:** "Blue Zones", "Power 9" được phép trong mục nguồn ở S16 / S08 khi có lời giải thích đi kèm.

```yaml
avoid:
  english_ui: [task, notification, reminder, sync, streak, settings, done, today, home, profile, ok, cancel, snooze, skip, badge, dashboard, login, account]
  power9_raw: [move naturally, purpose, down shift, downshift, 80% rule, hara hachi bu, plant slant, "wine @ 5", wine, belong, loved ones first, right tribe, moai, ikigai]
  bad_translation: [di chuyển tự nhiên, giảm số, quy tắc 80%, ăn vừa no 80%, nghiêng về thực vật, rượu vang, rượu, bộ lạc, bộ tộc, người thân yêu trước tiên, thuộc về]
  pressure: [nhiệm vụ, mục tiêu, thử thách, chuỗi ngày, mất chuỗi, điểm sức khỏe, điểm tuổi thọ, xếp hạng, bạn đã bỏ lỡ, chưa hoàn thành, thất bại, phải làm ngay]
  medical_claims: [chữa bệnh, phòng bệnh, kéo dài tuổi thọ, chống lão hóa, sống thêm, năm tuổi thọ]
  distant_terms: [người già, cụ già, người dùng, quý khách, người chăm sóc, người giám hộ, hệ thống]
  technical: [đồng bộ, sao lưu, thiết bị, cấu hình, đăng nhập, tài khoản]
allow_with_explanation:
  - term: Blue Zones
    where: S16 "Học từ đâu", S08 dòng giới thiệu
    explain: "những vùng có nhiều người sống thọ"
  - term: Power 9
    where: S16 "Học từ đâu"
    explain: "9 thói quen sống khỏe"
```

---

## 6. Kiểm chứng

| Bước | Cách làm | Kết quả mong đợi |
| --- | --- | --- |
| Đối chiếu nguồn | So nghĩa ở cột "Nghĩa theo nguồn" với `[BZ]` và `[PDF]` | Đã khớp 9/9 (17/10/2026) |
| Dịch máy thứ hai (tùy chọn) | Dịch 9 thuật ngữ bằng Google Translate, chụp màn hình vào `assets/vocabulary/` | So với cột `[AI]`; nếu khác thì thêm cột |
| Test với người lớn tuổi | Đọc tên thói quen trong app, hỏi: "Nghe tên này, Bác nghĩ mình phải làm gì?" | ≥ 4/5 người nói đúng việc; tên nào sai ≥ 2 người thì đổi |
| Agent | `R-VOC-01` quét mục 5 trên mọi output Stitch | 0 vi phạm |
