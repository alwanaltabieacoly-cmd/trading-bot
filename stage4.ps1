Set-Location D:\Openwork_Projects\trading-bot
$ft='.\.venv\Scripts\freqtrade'; $py='.\.venv\Scripts\python.exe'; $s='FreqaiClfRegime'
$base=@('-c','user_data\config.json','-c','user_data\config_freqai_clf.json','-s',$s,'--freqaimodel','LightGBMClassifier','-i','1h')
& $ft backtesting @base --timerange 20240101-20250630 *> fai2_is.log; 'IS default'; & $py btsum.py
& $ft hyperopt @base --timerange 20240101-20250630 --spaces buy --hyperopt-loss SharpeHyperOptLoss -e 60 -j 1 --min-trades 20 --random-state 42 *> fai2_ho.log; 'hyperopt done'; Get-Content "user_data\strategies\$s.json" | Select-String entry_prob
& $ft backtesting @base --timerange 20240101-20250630 *> fai2_is.log; 'IS tuned'; & $py btsum.py
& $ft backtesting @base --timerange 20250701-20261015 *> fai2_oos.log; 'OOS tuned'; & $py btsum.py
& $ft lookahead-analysis @base --timerange 20250901-20251101 *> fai2_lookahead.log; 'lookahead done'
& $ft recursive-analysis @base --timerange 20250901-20251101 *> fai2_recursive.log; 'recursive done'
'stage4done'