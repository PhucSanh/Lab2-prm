# Chạy /stitch-loop cho tất cả màn chính, mỗi màn một phiên Claude Code riêng.
# Cách dùng (PowerShell, ở thư mục gốc repo):
#   .\scripts\stitch-all.ps1                 # chạy mọi màn chưa có kết quả
#   .\scripts\stitch-all.ps1 -Only S07,S08   # chỉ chạy vài màn
#   .\scripts\stitch-all.ps1 -Force          # chạy lại cả màn đã có kết quả
param(
  [string[]]$Only = @(),
  [switch]$Force
)

# Khi gọi qua "powershell -File", "-Only S01,S02" đến dưới dạng một chuỗi -> tách theo dấu phẩy
$Only = @($Only | ForEach-Object { $_ -split '[,\s]+' } | Where-Object { $_ } | ForEach-Object { $_.Trim().ToUpper() })

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8
$env:MCP_TOOL_TIMEOUT = "600000"

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

# Thứ tự theo luồng dùng app (README.md, mục Màn chính)
$screens = [ordered]@{
  "S01" = "Chào mừng – chọn cỡ chữ"
  "S02" = "Thiết lập hồ sơ (Bước 1/2)"
  "S13" = "Cho phép nhắc việc (Bước 2/2)"
  "S03" = "Hôm nay"
  "S04" = "Chi tiết hoạt động"
  "S15" = "Sửa việc"
  "S05" = "Thêm việc – chọn hoạt động"
  "S06" = "Thêm việc – thiết lập"
  "S07" = "Lịch tuần"
  "S11" = "Chi tiết ngày"
  "S08" = "Hoạt động mỗi ngày"
  "S16" = "Chi tiết thói quen"
  "S09" = "Gia đình"
  "S12" = "Thêm người thân"
  "S17" = "Nhắn tin cho người thân"
  "S10" = "Cài đặt hiển thị"
  "S14" = "Lời nhắc đến giờ"
}

$template = Get-Content -Raw -Encoding UTF8 ".claude/commands/stitch-loop.md"

foreach ($code in $screens.Keys) {
  if ($Only.Count -gt 0 -and $Only -notcontains $code) { continue }
  $log = "stitch-runs/$code/log.md"
  if (-not $Force -and (Test-Path $log) -and (Select-String -Path $log -Pattern "Kết quả:" -Quiet)) {
    Write-Host "Bỏ qua $code (đã có kết quả)" -ForegroundColor DarkGray
    continue
  }
  $name = $screens[$code]
  New-Item -ItemType Directory -Force "stitch-runs/$code" | Out-Null
  Write-Host "`n=== $code $name – bắt đầu $(Get-Date -Format HH:mm) ===" -ForegroundColor Cyan

  $prompt = $template.Replace('$ARGUMENTS', "$code $name") + @"

Chạy không có người trông: không hỏi lại. Dùng project trong stitch-runs/project.txt, deviceType MOBILE.
Nếu gặp lỗi không tự xử lý được thì ghi lý do vào stitch-runs/$code/log.md với dòng **Kết quả: NEEDS_HUMAN** rồi dừng.
"@

  $prompt | claude -p --permission-mode auto 2>&1 | Tee-Object -FilePath "stitch-runs/$code/run.txt"
}

# Bảng tổng kết
$rows = foreach ($code in $screens.Keys) {
  $log = "stitch-runs/$code/log.md"
  $kq = "chưa chạy"
  if (Test-Path $log) {
    $m = Select-String -Path $log -Pattern "Kết quả:\s*\**\s*([A-Z_]+)" | Select-Object -First 1
    if ($m) { $kq = $m.Matches[0].Groups[1].Value } else { $kq = "đang dở" }
  }
  "| $code | $($screens[$code]) | $kq |"
}
$summary = "# Tổng kết vòng lặp Stitch`n`n| Mã | Màn | Kết quả |`n|---|---|---|`n" + ($rows -join "`n") + "`n"
Set-Content -Encoding UTF8 "stitch-runs/SUMMARY.md" $summary
Write-Host "`n$summary"
