# Bắt đầu — bộ Markdown có nguồn GitHub

Folder mới này có bản gốc tải từ GitHub và bản custom cho An Nhiên. Không phải bộ tài liệu được tự viết rồi gán tên repo nổi tiếng.

## Nguồn đã chọn
**K-Dense-AI/scientific-agent-skills** (repo cũ: claude-scientific-skills), **52.786 stars / 4.678 forks** khi truy vấn GitHub API ngày 19/10/2026. Đây là số của toàn repo, không phải riêng thư mục scientific-slides. Commit cố định: `593377bb048752abb0152deab9fbb1083a6087df`. Giấy phép MIT, có giữ copyright và LICENSE.

Link gốc: https://github.com/K-Dense-AI/scientific-agent-skills/tree/593377bb048752abb0152deab9fbb1083a6087df/skills/scientific-slides

Chọn vì bộ này có hướng dẫn kể chuyện nghiên cứu, cấu trúc talk, timing, thiết kế, review hình và đánh giá độ tin cậy bằng chứng. Stars/forks cho biết mức phổ biến của repo, không tự chứng minh chất lượng mọi hướng dẫn.

## Cấu trúc
- `upstream/scientific-agent-skills/`: snapshot các file Markdown của scientific-slides và scientific-critical-thinking, README và LICENSE. Chỉ tải tài liệu, không cài/chạy script hay kéo dependency.
- `an-nhien-canva/SKILL.md`: entrypoint dùng cho agent Canva.
- `an-nhien-canva/references/`: bốn tài liệu dẫn xuất từ upstream và năm tài liệu riêng của An Nhiên.
- `CUSTOMIZATION.patch`: diff cho bốn tài liệu được custom trực tiếp từ upstream.
- `ADAPTATION.md`: phần giữ, đổi và bổ sung, phân biệt nguồn gốc.
- `sources.json`: star/fork, commit và license của các repo đã so sánh.
- `upstream-manifest.json`: đường dẫn, URL commit và SHA-256 từng file gốc.

## Giao agent
Copy prompt trong `PROMPT.md`. Agent đọc `an-nhien-canva/SKILL.md` thay vì chạy skill upstream nguyên bản. Bộ này nằm trong repo, chưa được cài vào cấu hình agent toàn cục. Nếu agent không đọc được filesystem này, gửi cả folder cho agent; một đường dẫn local trong chat không khiến Canva server đọc được file.

Bộ `codex-runs/presentation-kit/` trước đó là draft tự soạn, được giữ nguyên để không mất nội dung. Bộ mới này dùng nguồn GitHub làm nền tảng; storyboard và dữ liệu An Nhiên được ghi nhãn là bổ sung dự án.

## So sánh đã kiểm tra
| Repo | Stars | Forks | Quyết định |
|---|---:|---:|---|
| K-Dense-AI/scientific-agent-skills | 52.786 | 4.678 | Chọn scientific-slides + critical-thinking, MIT |
| slidevjs/slidev | 49.126 | 2.229 | Framework làm slide bằng Markdown; không phải workflow agent Canva |
| marp-team/marp | 12.654 | 302 | Hệ sinh thái render Markdown; không phải workflow research→Canva |
| anthropics/skills | 182.125 | 21.585 | Không dùng: license riêng của pptx ở commit kiểm tra hạn chế sao chép/tạo bản dẫn xuất; không giữ file trong gói |

Các số là snapshot GitHub API, sẽ thay đổi. Xem `sources.json` để truy vết. Không có deck Canva nào được tạo trong bước chuẩn bị bộ tài liệu này.
