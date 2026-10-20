# Chạy lần lượt các khung Stitch còn lại của làn A bằng Claude Code CLI.
# Cách dùng (PowerShell, đứng ở thư mục gốc repo):
#   .\scripts\stitch-remaining.ps1                 # chạy hết
#   .\scripts\stitch-remaining.ps1 -Only S06o,S11b # chỉ vài khung
#   .\scripts\stitch-remaining.ps1 -DryRun         # chỉ in danh sách sẽ chạy
# Khung đã có dòng "Kết quả:" (khác NEEDS_HUMAN) trong log.md thì bỏ qua; khung chạy dở (có critique nhưng chưa có Kết quả) thì thêm --resume.
# Khung --from X mà X chưa xong thì bỏ qua, chạy lại script là làm tiếp.
# Dừng hẳn khi Claude báo lỗi liên tiếp 2 lần (thường là hết quota Stitch / hết lượt Claude).
param(
  [string[]]$Only = @(),
  [switch]$DryRun,
  [string]$PermissionMode = "acceptEdits"
)
$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

# Mã | Tên | Màn gốc (rỗng = NEW)
$jobs = @(
  @("S03-alldone","Hôm nay · xong 6/6","S03"),
  @("S13d","Nhắc việc đang tắt","S13"),
  @("S06o","Thêm việc · đã sửa lỗi","S06"),
  @("S11b","Chi tiết ngày · ngày khác","S11"),
  @("S12a","Thêm người thân · chưa có số","S12"),
  @("S12e","Thêm người thân · số sai","S12"),
  @("S09b","Gia đình · đã thêm người thân","S09"),
  @("S17b","Nhắn tin · đã mở chia sẻ","S17"),
  @("ST-Loading-offline","Đang lưu · mất mạng","ST-Loading"),
  @("DLG-Later","Dời việc","DLG-Done"),
  @("DLG-Skip","Bỏ qua hôm nay","DLG-Done"),
  @("DLG-Delete","Xóa việc","DLG-Done"),
  @("DLG-TaskTime","Chọn giờ làm","DLG-WakeTime"),
  @("N06","Sửa hồ sơ","S02"),
  @("N09","Sửa người thân","S12"),
  @("N10","Đã mở ứng dụng chia sẻ","S17b"),
  @("N11","Chọn ngày",""),
  @("N12","Lặp lại",""),
  @("N13","Phạm vi thay đổi","DLG-Done"),
  @("N14","Chưa lưu thay đổi","DLG-Done"),
  @("N15","Xóa người thân","DLG-Delete"),
  @("N16","Đã lưu · nhắc cần kiểm tra","ST-Saved"),
  @("N18","Đã lưu việc đầu tiên","ST-Saved"),
  @("N17","Hôm nay · đã xử lý hết","S03-alldone"),
  @("N19","Hôm nay · việc đầu tiên","S03"),
  @("N21","Gia đình sau khi xóa người thân","S09"),
  @("G12","Hôm nay · thẻ gợi ý của Mai","S03"),
  @("G11","Popup Mai gửi lịch cho Bác","S03"),
  @("G10","Có gợi ý mới (tự hiện)","G11")
)

function Test-Done($code) {
  $log = Join-Path $root "stitch-runs\$code\log.md"
  if (-not (Test-Path $log)) { return $false }
  # Chỉ tính dòng kết quả chính ("**Kết quả: ..."); NEEDS_HUMAN / CHƯA XONG = lần trước bị kẹt (timeout, thiếu màn gốc...), chạy lại.
  $done = Select-String -Path $log -Pattern "^\*\*Kết quả:" -Encoding UTF8 | Where-Object { $_.Line -notmatch "NEEDS_HUMAN|CHƯA XONG" }
  return [bool]$done
}
function Test-Started($code) {
  $dir = Join-Path $root "stitch-runs\$code"
  return (Test-Path $dir) -and [bool](Get-ChildItem $dir -Filter "v*-critique.json" -ErrorAction SilentlyContinue)
}

$fails = 0
foreach ($j in $jobs) {
  $code, $name, $from = $j
  if ($Only.Count -gt 0 -and $Only -notcontains $code) { continue }
  if (Test-Done $code) { Write-Host "[bỏ qua] $code đã có Kết quả" -ForegroundColor DarkGray; continue }
  if ($from -and -not (Test-Done $from)) { Write-Host "[chờ] $code – màn gốc $from chưa xong" -ForegroundColor Yellow; continue }
  $args2 = "$code $name"
  if ($from) { $args2 += " --from $from" }
  if (Test-Started $code) { $args2 += " --resume" }
  $prompt = "/stitch-loop $args2"
  Write-Host "`n=== $prompt ===" -ForegroundColor Cyan
  if ($DryRun) { continue }
  $logFile = Join-Path $root "stitch-runs\_batch-$code.txt"
  # Hiện từng bước (gọi tool, chữ Claude viết) ngay khi chạy; file log chỉ giữ câu trả lời cuối.
  "" | Set-Content $logFile -Encoding UTF8
  claude -p $prompt --permission-mode $PermissionMode --output-format stream-json --verbose 2>&1 | ForEach-Object {
    $line = "$_"
    try { $e = $line | ConvertFrom-Json -ErrorAction Stop } catch { Write-Host $line -ForegroundColor DarkGray; return }
    $t = (Get-Date -Format HH:mm:ss)
    if ($e.type -eq "assistant") {
      foreach ($c in $e.message.content) {
        if ($c.type -eq "tool_use") {
          $arg = ""
          if ($c.input.file_path) { $arg = $c.input.file_path } elseif ($c.input.command) { $arg = $c.input.command } elseif ($c.input.description) { $arg = $c.input.description }
          if ($arg.Length -gt 90) { $arg = $arg.Substring(0,90) + "…" }
          Write-Host "  $t  → $($c.name)  $arg" -ForegroundColor Cyan
        } elseif ($c.type -eq "text" -and $c.text.Trim()) {
          $x = $c.text.Trim(); if ($x.Length -gt 200) { $x = $x.Substring(0,200) + "…" }
          Write-Host "  $t  $x"
        }
      }
    } elseif ($e.type -eq "result") {
      Write-Host "`n$($e.result)" -ForegroundColor Green
      $e.result | Add-Content $logFile -Encoding UTF8
      $global:LASTEXITCODE = [int]([bool]$e.is_error)
    }
  }
  $text = Get-Content $logFile -Raw -Encoding UTF8 -ErrorAction SilentlyContinue
  if ($LASTEXITCODE -ne 0 -or $text -match "(?i)quota|rate limit|usage limit|denied|RESOURCE_EXHAUSTED") {
    $fails++
    Write-Host "[lỗi] $code (xem $logFile)" -ForegroundColor Red
    if ($fails -ge 2) { Write-Host "Lỗi 2 khung liên tiếp (quyền / quota) – dừng. Chạy lại script sau." -ForegroundColor Red; break }
  } else {
    $fails = 0
    if (-not (Test-Done $code)) { Write-Host "[cần xem tay] $code chạy xong nhưng chưa có Kết quả – xem $logFile" -ForegroundColor Yellow }
  }
}
Write-Host "`nXong đợt này. Xem stitch-runs\*\log.md và cập nhật SUMMARY.md." -ForegroundColor Green
