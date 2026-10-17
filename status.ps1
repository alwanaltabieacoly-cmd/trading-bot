# Prints status of the local dry-run paper bots via their localhost API.
Set-Location $PSScriptRoot
$p = (Get-Content config.private.json -Raw | ConvertFrom-Json).api_server
$h = @{ Authorization = 'Basic ' + [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes("$($p.username):$($p.password)")) }
foreach ($b in @(@('A',8081),@('B',8082),@('C',8083))) {
  $u = "http://127.0.0.1:$($b[1])/api/v1"
  try {
    $cfg = Invoke-RestMethod "$u/show_config" -Headers $h -TimeoutSec 10
    $pr  = Invoke-RestMethod "$u/profit" -Headers $h -TimeoutSec 10
    $st  = @(Invoke-RestMethod "$u/status" -Headers $h -TimeoutSec 10 | % { $_ } | ? { $_.pair })
    "bot$($b[0]) $($cfg.strategy) [$($cfg.timeframe)] state=$($cfg.state) dry_run=$($cfg.dry_run)"
    "  open trades: $($st.Count)   closed trades: $($pr.closed_trade_count)   wins/losses: $($pr.winning_trades)/$($pr.losing_trades)"
    "  closed profit: $([math]::Round($pr.profit_closed_coin,3)) USDT ($([math]::Round($pr.profit_closed_percent,2))%)   all incl. open: $([math]::Round($pr.profit_all_coin,3)) USDT"
    "  max drawdown: $([math]::Round($pr.max_drawdown*100,2))% ($([math]::Round($pr.max_drawdown_abs,3)) USDT)"
    foreach ($t in $st) { "    open: $($t.pair) since $($t.open_date) profit $([math]::Round($t.profit_pct,2))%" }
  } catch { "bot$($b[0]) port $($b[1]): not reachable ($($_.Exception.Message))" }
}