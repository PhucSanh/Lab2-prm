# Nguồn gốc và custom

## Giữ từ upstream MIT
- Scientific Slides: narrative Hook→Context→Gap→Approach→Results→Implications→Closure; one message per slide; minimal text; visuals and citations; consistency; planning and rehearsal; visual validation.
- Giữ phần nội dung gốc của presentation_structure.md, slide_design_principles.md, timing_guidelines.md trong các bản dẫn xuất, thêm khối adaptation ở đầu. Diff được lưu.
- Scientific Critical Thinking: đánh giá applicability, giới hạn, bias và chất lượng bằng chứng; giữ evidence_hierarchy.md cùng phần điều chỉnh UX ở đầu bản dẫn xuất.

## Thay cho phù hợp yêu cầu
- Research talk → UX design case study. Không giả vờ An Nhiên đã chạy clinical study.
- Nano Banana/OpenRouter, Beamer và PPTX scripts → Canva MCP editable. Không chạy pipeline upstream.
- Palette/font tổng quát → DESIGN của An Nhiên, có cỡ chữ dành riêng cho slide.
- Quy trình export/render một lần → tạo phiên bản, reviewer độc lập, sửa từ best và ghi regression; dừng hữu hạn.
- General evidence hierarchy → phù hợp câu hỏi UX, giữ đơn vị và phân biệt AI roleplay với người thật.

## Bổ sung riêng của dự án
SKILL.md là entrypoint được viết lại để port workflow sang Canva; không phải nguyên văn upstream. project-brief.md, evidence-ledger.md, storyboard.md, canva-loop.md, slide-critic.md là nội dung riêng từ draft trước và repo. Bốn reference còn lại là dẫn xuất có nội dung gốc upstream; patch cho thấy chính xác khối bổ sung. Không tuyên bố upstream có sẵn loop Canva, research An Nhiên hay rubric dự án.

## Giấy phép và snapshot
Giữ LICENSE.md của K-Dense cả trong upstream và gói custom. Không sửa file gốc sau tải. Không tải script thực thi hoặc tài sản ảnh. Các link đến script/template trong upstream là ngữ cảnh của bản gốc, không phải dependency đã được đóng gói. Chỉ entrypoint custom và các link mà nó chỉ định là workflow chạy được cho Canva.
