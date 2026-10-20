<!-- Project-specific material by Codex; not upstream K-Dense content. -->
# Canva loop

## Preflight
Đọc toàn bộ kit, nguồn repo và schema Canva MCP thật. Xác nhận có thể tạo presentation, đọc trang, lấy preview, sửa và lưu phiên bản. Không đoán tên tham số. `create_design` là lựa chọn khi đang có; không dùng generate_design/create_design_from_candidate legacy nếu tool mới có sẵn.

Chỉ tạo deck khi người dùng yêu cầu chạy kit/làm slide. Không tự publish hoặc gửi cho người khác. Nếu tool thiếu khả năng, ghi BLOCKED đúng bước; tiếp tục chuẩn bị nội dung/asset được phép, không tự nhận đã tạo hoặc đã review deck.

Trước generation: tạo run-id riêng, manifest, source ledger, outline chốt, asset map. Nếu chỉ có Markdown trong chat, agent phải được cấp nội dung file; không giả định Canva server đọc được đường dẫn máy local. Upload file theo tool được hỗ trợ. Thiếu asset thì giữ placeholder có nhãn trong draft và ghi missing; chưa được chốt.

## Mỗi vòng v0…v4
1. Chuẩn bị brief tự chứa: slide IDs, text đã chốt, notes, sources, asset IDs, art direction và slide count.
2. Tạo v0 hoặc copy bản best trước khi sửa. Lưu design_id/edit_url thật. Nếu async, dùng job ID/continuation token mà API trả; không gửi lệnh tạo trùng khi timeout.
3. Đọc lại content/page list; render/preview mọi trang. Lưu mapping slide_id→page_id. Nếu preview chỉ là link tạm, dùng công cụ hỗ trợ để xem, không bịa đường dẫn local.
4. Spawn reviewer mới với context tối thiểu, không kế thừa chat; giao `slide-critic.md`, bản render, nội dung/notes, evidence ledger, storyboard và brief. Không giao prompt sinh, điểm mục tiêu hay kết luận tự chấm.
5. Reviewer trả critique JSON có lỗi, vị trí, bằng chứng, sửa cụ thể. Thiếu render/notes thì trạng thái INCOMPLETE; không chấm pass.
6. Orchestrator kiểm schema và tính điểm; viết edit prompt chỉ sửa lỗi được chứng minh. Giữ bản cũ, sửa từ best, ưu tiên lỗi nguồn/nội dung trước hình thức. Tối đa 8 sửa chính mỗi lượt.
7. Lưu state/log, so best và điều kiện dừng. Không lặp vô hạn.

## Điểm và dừng — riêng cho slide
Không lấy rubric UI trong rule.md để chấm deck. Điểm slide = max(0,100−15×blockers−5×majors−1×minors), mỗi issue chỉ đếm một lần. Blocker: bịa paper/kết quả, AI giả lập thành người thật, gán điểm agent thành SUS, thiếu slide bắt buộc, trang không đọc được. Major: logic đứt, thiếu mapping research→UI, sai token chủ đạo, screenshot sai version, text tràn. Minor: căn lề/spacing/nhãn chưa nhất quán nhưng đọc được.

Best ưu tiên ít blocker, rồi ít major, rồi điểm cao; hòa chọn bản mới. Patience tăng nếu thứ hạng không tốt hơn, kể cả thay best khi hòa. Dừng: đạt ≥95 với 0 blocker/major; hoặc 2 vòng không cải thiện; hoặc hết v4. Có blocker/major khi dừng → NEEDS_REVISION. Thiếu tool/bằng chứng → BLOCKED/INCOMPLETE. Không hạ tiêu chuẩn chỉ để đạt điểm.

100 điểm là đạt rubric trong phạm vi kiểm tra, không chứng minh thuyết trình thành công. Reviewer là agent độc lập về context, không phải người dùng độc lập.

## State
Ghi state.json bằng file tạm rồi rename; gồm run_id, status, round, design_id, parent_design_id, best_design_id, best_round, best_score, best_counts, patience, pending_job_id, slide_page_map, manifest_path, stop_reason, updated_at. Giữ token/credential/signed query ngoài log.
Nếu Canva không cho copy hoặc lưu version an toàn, không sửa đè deck nguồn; ghi giới hạn và bàn giao draft hiện có.

## Handoff
Link Canva editable của best; số slide; render/PDF nếu tool hỗ trợ và đã kiểm; lời thoại/notes; nguồn; log các vòng; giới hạn còn lại. Kiểm lại bản best sau commit/save, không chỉ bản preview trước commit. Không tuyên bố đã xem trên màn hình nếu chỉ kiểm metadata.
