# Per-run design decisions

- C08: Use the official Lucide `send` icon (32×32) for the “Gửi lịch cho mẹ” action. The shared icon dictionary does not yet define a send icon; record this local decision and leave `assets/stitch/DESIGN.md` unchanged pending human approval.
- C09: Use the official Lucide `clock` icon (32×32) for the pending receipt status. The shared icon dictionary does not yet define a pending icon; record this local decision and leave `assets/stitch/DESIGN.md` unchanged pending human approval.

- N08: NEEDS_HUMAN after v3 (patience_2), best v2 score 87. The “Mở cài đặt” primary action needs an icon under R-ICON-02, but no unambiguous dictionary mapping exists for opening system app settings. Do not change shared `assets/stitch/DESIGN.md` during this loop. Decide whether the documented `smartphone` (device permissions/settings) is acceptable here or define a new icon meaning in a separate approved design update. Also shorten step 3 to at most two lines at 360px (current v3 wraps to three).
