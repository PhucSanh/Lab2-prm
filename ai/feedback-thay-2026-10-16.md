# Feedback của thầy – 16/10/2026

## Ghi chép nguyên văn

- Prd.md
- Design.md
- Coursery
- Keyword xuất hiện trong app thân thiện với persona
- Việt hoá coursery + việt hoá
- Appstyleguid.md
- Ipo/ibo : input đầu vào chặt chẽ
- Guidrail: tự động phản biện
- Bộ kiểm soát
- Agent + stitch loop
- Taji product req
- Từ vựng thân thiện với người già
- Lấy từ khóa người già trong sách
- Phải có file design.md
- Thiết kế luồng tập trung vào việc click
- Cho cái app style guide
- Build harness ở đầu ra
- Thành lập loop
- Chữ nhiều
- Căn giữa
- không kéo trượt
- Nhìn vào là bik làm hay chưa làm
- Voice

## Diễn giải: kiến trúc thầy muốn

```
INPUT chặt chẽ (IPO)                      PROCESS              OUTPUT + HARNESS
PRD.md ─────────────┐
DESIGN.md ──────────┤
AppStyleGuide.md ───┼──► prompt ──► Google Stitch ──► màn hình ──► Agent đọc rule.md (guardrail)
vocabulary.md ──────┘                    ▲                              │ phản biện, chấm điểm
(từ vựng người già, có nguồn)            └──── lệnh sửa ◄───────────────┘ loop tới khi đạt
```

## Việc cần làm

| Ghi chú của thầy | Deliverable | Hiện trạng |
| --- | --- | --- |
| Prd.md, "product req" | `PRD.md`: vấn đề, persona, mục tiêu, phạm vi MVP, user story, yêu cầu chức năng / phi chức năng, tiêu chí đo | Có – `assets/stitch/PRD.md` (17/10) |
| Phải có design.md | `DESIGN.md` | Có – bản chuẩn Stitch ở `assets/stitch/DESIGN.md` (17/10); `DESIGN.md` gốc giữ prompt v0 |
| Appstyleguide.md | `AppStyleGuide.md`: giọng văn, cách xưng hô, bố cục, căn lề, icon + chữ, trạng thái, do / don't có ví dụ | Có – `assets/stitch/AppStyleGuide.md` (17/10), 58 quy tắc có nguồn |
| Từ vựng thân thiện người già; lấy từ khóa người già trong sách; keyword thân thiện persona | `vocabulary.md`: bảng từ nên dùng / tránh dùng (vd. "nhắc việc" thay "notification"), có trích nguồn sách / tài liệu | Chưa có |
| Coursery, Việt hoá coursery | Cần hỏi lại: có phải tài liệu khoá Coursera (UX / thiết kế cho người cao tuổi) cần Việt hoá làm nguồn không? | ? |
| IPO / IBO: input đầu vào chặt chẽ | Prompt Stitch phải sinh từ 4 file input ở trên, không viết tay tự do | Một phần (`/stitch-loop` mới đọc DESIGN.md + persona) |
| Guardrail tự động phản biện, bộ kiểm soát | `rule.md` | Có, cần bổ sung luật mới bên dưới |
| Agent + Stitch loop, build harness ở đầu ra, thành lập loop | Claude Code + Stitch MCP + `/stitch-loop` | Đã cấu hình, chưa chạy thật |
| Thiết kế luồng tập trung vào việc click | User flow: mọi hành động bằng chạm / bấm, ít bước | Có ux/user-flow.md, cần rà lại |
| Chữ nhiều *(sửa 17/10: thầy chê **nhiều chữ** → muốn **ít chữ**)* | Câu ≤ 15 tiếng, nút ≤ 5 tiếng, thẻ ≤ 1 dòng phụ | Đã thêm R-TXT-03 – R-TXT-06 |
| *(bổ sung 17/10)* Dùng icon nhiều | Mọi việc / thói quen / tab / nút chính có icon, icon luôn kèm nhãn ngắn | Đã thêm R-ICON-02, R-ICON-03 |
| *(bổ sung 17/10)* Màu sắc bắt mắt | 9 màu nhấn thói quen ở ô icon + vạch màu thẻ việc; nền và chữ giữ tương phản cao | Đã thêm R-COL-02 – R-COL-04; token ở `assets/stitch/DESIGN.md` |
| Căn giữa | Căn giữa nội dung đứng một mình, căn trái danh sách | Đã thêm R-CEN-01 |
| Không kéo trượt | Luật R-GES-01 | Có |
| Nhìn vào là biết làm hay chưa làm | 5 nhãn trạng thái icon + chữ + màu đậm cạnh từng việc | Đã thêm R-STA-01, R-STA-02 |
| Voice | Nút "Đọc to" ở S14, S04, S16, G03; lời nhắc tự đọc to | Đã thêm R-VOI-01; AppStyleGuide mục 10 |

## Luật cần thêm vào rule.md *(đã thêm 17/10, xem rule.md mục 2, 3, 6, 7, 9, 10)*

- Căn giữa: tiêu đề màn, nút chính, nội dung trạng thái căn giữa.
- Trạng thái rõ: mỗi việc hiện "Đã xong" / "Chưa làm" bằng icon + chữ, nhìn lướt là biết.
- Voice: màn có nội dung chính phải có nút "Đọc to"; lời nhắc có giọng nói.
- Từ vựng: mọi chữ trên UI phải nằm trong `vocabulary.md` (cột "nên dùng"), không dùng từ ở cột "tránh".

## Câu hỏi còn mở

- "Coursery" là gì: khoá Coursera, sách cụ thể, hay tài liệu thầy đưa?
- "Taji" là gì?
- "Lấy từ khóa người già trong sách": thầy có chỉ định sách nào không?
