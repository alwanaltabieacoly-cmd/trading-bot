# Runs the strategy research harness every 4 hours.
# Safe to run while the trading bots are stopped - it only reads market
# data and writes reports. It never places an order.
$ErrorActionPreference = "Continue"

$Root    = "D:\Openwork_Projects\trading-bot"
$Project = "D:\Openwork_Projects\ai-models"
$Python  = "$Root\.venv\Scripts\python.exe"
$LogDir  = "$Root\research\logs"
$Stamp   = Get-Date -Format "yyyyMMdd_HHmmss"

New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

$out = "$LogDir\research_$Stamp.out.log"
$err = "$LogDir\research_$Stamp.err.log"

Write-Host "research run $Stamp"

if (-not (Test-Path $Python)) {
    Write-Host "python not found at $Python" | Out-File $err
    exit 1
}

Push-Location $Root
try {
    $env:PYTHONPATH = $Root
    & $Python -m research.run_daily *>> $out
    $code = $LASTEXITCODE
    Write-Host "research exited with code $code"
    if ($code -ne 0) {
        Get-Content $err -ErrorAction SilentlyContinue | Add-Content $out
    } else {
        # Deep analysis across every run accumulated so far.
        & $Python -m research.analyze *>> $out
        Write-Host "analyze exited with code $LASTEXITCODE"
    }
} finally {
    Pop-Location
}

# Keep only the last 60 run logs
Get-ChildItem $LogDir -Filter "research_*.log" -ErrorAction SilentlyContinue |
    Sort-Object LastWriteTime -Descending |
    Select-Object -Skip 60 |
    Remove-Item -Force -ErrorAction SilentlyContinue
