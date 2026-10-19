<#
  Push the trading bot to GitHub.

  Run this after creating the private repo on github.com/new
  (name: trading-bot, private, do NOT tick "add a README").

  Usage:
    .\push-to-github.ps1
    .\push-to-github.ps1 -RepoName my-private-repo
#>
param(
  [string]$RepoName = "trading-bot",
  [string]$Branch = "main",
  [string]$User = "alwanaltabieacoly-cmd"
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host "=== 1/4  Check GitHub auth ===" -ForegroundColor Cyan
gh auth status 2>&1 | Select-Object -First 3 | ForEach-Object { "  $_" }

$remoteUrl = "https://github.com/$User/$RepoName.git"

Write-Host "`n=== 2/4  Check the repo exists ===" -ForegroundColor Cyan
$exists = $false
try {
  gh repo view $User/$RepoName --json name 2>$null | Out-Null
  if ($?) { $exists = $true }
} catch { }

if (-not $exists) {
  Write-Host "  repo $User/$RepoName not visible to this token." -ForegroundColor Yellow
  Write-Host "  Attempting to create it..." -ForegroundColor Yellow
  gh repo create $User/$RepoName --private --description "Bybit crypto trading bot with a self-testing daily research harness" 2>&1 | ForEach-Object { "  $_" }
  if (-not $?) {
    Write-Host ""
    Write-Host "  Could not create the repo with this token." -ForegroundColor Red
    Write-Host "  Create it manually: https://github.com/new" -ForegroundColor Yellow
    Write-Host "    name: $RepoName   visibility: Private   README: leave unticked" -ForegroundColor Yellow
    Write-Host "  Then run this script again." -ForegroundColor Yellow
    exit 1
  }
}

Write-Host "`n=== 3/4  Wire up the remote ===" -ForegroundColor Cyan
if (git remote | Select-String -SimpleMatch "origin") {
  git remote set-url origin $remoteUrl
  Write-Host "  updated existing origin"
} else {
  git remote add origin $remoteUrl
  Write-Host "  added origin -> $remoteUrl"
}

Write-Host "`n=== 4/4  Push ===" -ForegroundColor Cyan
git push -u origin "HEAD:refs/heads/$Branch"
git push origin "HEAD:refs/heads/dev" 2>$null | Out-Null

Write-Host ""
Write-Host "PUSHED. Open https://github.com/$User/$RepoName" -ForegroundColor Green
Write-Host "Then check Actions tab - the daily research workflow should start." -ForegroundColor Green
Write-Host ""
Write-Host "To trigger the first run now, in the Actions tab click 'Daily research'" -ForegroundColor Gray
Write-Host "-> Run workflow." -ForegroundColor Gray
