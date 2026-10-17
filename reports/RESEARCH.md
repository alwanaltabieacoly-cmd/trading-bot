# Research notes (provided by user, 2026-10-17)

- "Grok Bot" trading claims circulating on TikTok/X are hype or scams.
  - IOSCO I-SCAN warning: https://www.iosco.org/i-scan/?id=55766
  - CFTC advisory on AI trading bots: https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/AITradingBots.html
- Papers: LLM-agent trading backtests suffer from look-ahead bias / memorization of the test period: arXiv 2510.07920, 2601.13770, 2609.34510.
- Candidate projects: TauricResearch/TradingAgents, iterativv/NostalgiaForInfinity, freqtrade/freqtrade-strategies, FinGPT, vectorbt.
- Data sources: alternative.me Fear & Greed, GDELT, CryptoPanic, Reddit.
- Local findings so far: see STAGES.md; no strategy shows a validated out-of-sample edge.
## Video & community research (provided by user, unverified by me)
- Alpha Arena (alphaarena.ai) real-money LLM trading: a Grok-4 variant reported -96% using 11x leverage; Grok-4.20 reported +34.6% over a short sample (too short to mean much).
- axagen YouTube video sprcALCNoW0: "Grok bot" 1 week result -0.76% live / -2.7% paper.
- Emergent Methods (FreqAI authors) XGBoost: ~3 weeks live +7% (short sample).
- Reddit: 42 Freqtrade strategies tested on BTC over 8 years, 33 lost money; winner used a long moving-average trend filter plus a funding-rate rule.
- Scams seen: "GV trader" 100x leverage video, fake 68.4% win-rate guide, "GrokBot" deposit sites.