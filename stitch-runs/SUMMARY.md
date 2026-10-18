# Tổng kết vòng lặp Stitch

| Mã | Màn | Kết quả |
|---|---|---|
| S01 | Chào mừng – chọn cỡ chữ | CONVERGED (v2 – 100) |
| S02 | Thiết lập hồ sơ (Bước 1/2) | PASS |
| S13 | Cho phép nhắc việc (Bước 2/2) | PASS |
| S03 | Hôm nay | PASS |
| S04 | Chi tiết hoạt động | PASS |
| S15 | Sửa việc | CONVERGED – v1 100 điểm |
| S05 | Thêm việc – chọn hoạt động | PASS |
| S06 | Thêm việc – thiết lập | PASS |
| S07 | Lịch tuần | PASS |
| S11 | Chi tiết ngày | CONVERGED – v3 100 điểm |
| S08 | 9 thói quen | PASS |
| S16 | Chi tiết thói quen | CONVERGED – v4 100 điểm |
| S09 | Gia đình | PASS |
| S12 | Thêm người thân | CONVERGED – v1 100 điểm |
| S17 | Nhắn tin cho người thân | CONVERGED – v1 100 điểm |
| S10 | Cài đặt hiển thị | PASS |
| S14 | Lời nhắc đến giờ | PASS |

> **Đổi luật 2026-10-17.** Các màn PASS ở trên chạy theo luật cũ (dừng khi 0 `error` và điểm ≥ 85). Từ nay vòng lặp dừng khi điểm không tăng nữa (2 vòng liên tiếp không vượt điểm tốt nhất, hoặc đạt 100; tối đa v8), và icon theo Từ điển icon trong `assets/stitch/DESIGN.md`. Các màn chạy tiếp bằng `--resume` được chấm lại theo luật mới trước khi sửa.
