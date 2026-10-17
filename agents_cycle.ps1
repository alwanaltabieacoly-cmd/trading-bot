# One live agent cycle: refresh candles (incremental), then run decision agents. Writes user_data/decisions/latest.json.
Set-Location D:\Openwork_Projects\trading-bot
$log = 'reports\decisions\cycle.log'
"$(Get-Date -Format o) cycle start" | Add-Content $log
& .\.venv\Scripts\freqtrade.exe download-data -c user_data\config.json -t 5m 15m 1h 4h 1d *> reports\decisions\download.log
& .\.venv\Scripts\freqtrade.exe download-data -c user_data\config.json -p BTC/USDT ETH/USDT -t 1m *>> reports\decisions\download.log
& .\.venv\Scripts\python.exe -m agents.run_cycle --api-url http://127.0.0.1:8082/api/v1 --live-orderbook 2>&1 | Out-File -Append -Encoding utf8 $log
"$(Get-Date -Format o) cycle end exit=$LASTEXITCODE" | Add-Content $log