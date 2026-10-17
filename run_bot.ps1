param([Parameter(Mandatory)][string]$Bot)
# Launches one DRY-RUN paper bot. Config order: base -> bot-specific extras -> bot -> private (api creds).
Set-Location D:\Openwork_Projects\trading-bot
$extra = @{ A=@(); B=@(Get-Content user_data\bots\botB.extra -ErrorAction SilentlyContinue); C=@('user_data\config_btc.json') }[$Bot]
$args2 = @('trade','-c','user_data\config.json') 
foreach($e in $extra){ if($e){ $args2 += @('-c',$e) } }
$args2 += @('-c',"user_data\bots\bot$Bot.json",'-c','config.private.json','--logfile',"user_data\logs\bot$Bot.log")
$b = Get-Content "user_data\bots\bot$Bot.json" -Raw | ConvertFrom-Json
if ($b.dry_run -ne $true) { throw "Refusing to start: dry_run is not true for bot$Bot" }
if ($b.freqaimodel) { $args2 += @('--freqaimodel',$b.freqaimodel) }
& .\.venv\Scripts\freqtrade.exe @args2