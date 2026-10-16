Set-Location D:\Openwork_Projects\trading-bot
$ft='.\.venv\Scripts\freqtrade'; $py='.\.venv\Scripts\python.exe'; $s='TrendAdx1hRegime'
function BT($st,$t,$tag){ & $ft backtesting -c user_data\config.json -s $st -i 1h --timerange $t --timeframe-detail 15m *> wf\tmp.log; "$tag"; & $py btsum.py }
BT 'TrendAdx1h' '20250701-' 'TrendAdx1h OOS rerun (stoploss now -0.08 from strategy)'
BT 'TrendAdx1h' '20240101-20250630' 'TrendAdx1h IS rerun'
BT $s '20250701-' 'Regime OOS DEFAULT params'
$w=@(@('20240101-20241231','20250101-20250630'),@('20240701-20250630','20250701-20251231'),@('20250101-20251231','20260101-'))
$i=0; foreach($p in $w){ $i++; & $ft hyperopt -c user_data\config.json -s $s -i 1h --timerange $p[0] --spaces buy sell --hyperopt-loss SharpeHyperOptLoss -e 150 --min-trades 15 --random-state 42 -j 6 *> "wf\ho_${s}_$i.log"; BT $s $p[0] "W$i TRAIN $($p[0])"; BT $s $p[1] "W$i TEST $($p[1])"; Copy-Item "user_data\strategies\$s.json" "wf\${s}_W$i.json" }
& $ft hyperopt -c user_data\config.json -s $s -i 1h --timerange 20240101-20250630 --spaces buy sell --hyperopt-loss SharpeHyperOptLoss -e 300 --min-trades 20 --random-state 42 -j 6 *> "ho_$s.log"
BT $s '20240101-20250630' 'MAIN IS'
BT $s '20250701-' 'MAIN OOS'
'stage3done'