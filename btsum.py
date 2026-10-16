import json,zipfile,sys,pathlib
d=pathlib.Path('user_data/backtest_results')
last=json.load(open(d/'.last_result.json'))['latest_backtest']
z=zipfile.ZipFile(d/last)
n=[x for x in z.namelist() if x.endswith('.json') and '_config' not in x and '_market' not in x][0]
r=json.load(z.open(n))
for s,m in r['strategy'].items():
    print(f"{s}: trades={m['total_trades']} wins={m['wins']} winrate={m['winrate']*100:.1f}% profit={m['profit_total']*100:.2f}% maxDD(acct)={m['max_drawdown_account']*100:.2f}% sharpe={m.get('sharpe',0):.2f} calmar={m.get('calmar',0):.2f} market={m['market_change']*100:.2f}% range={m['backtest_start'][:10]}..{m['backtest_end'][:10]}")