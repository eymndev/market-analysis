---
name: equity-analysis
description: Analyze BIST- or Nasdaq-listed companies through financials, valuation, price behavior, catalysts, and thesis risks. Use for equity comparisons, earnings or multiple/DCF reviews, investment theses, and watchlists; do not use for fund analysis or IPO document cross-checking.
---

# BIST and Nasdaq Equity Analysis

Structure the analysis around company quality, expectations, valuation, catalysts, and thesis breakers.

## Scope and sources

1. Resolve the ticker, exchange, share class, analysis date, currency, and user time horizon. Do not mix securities that share a ticker across different exchanges.
2. Current prices, financial results, management guidance, and regulatory events are time-sensitive; verify them online.
3. Prioritize KAP/Borsa Istanbul or SEC/Nasdaq filings, then audited statements and investor-relations material, and finally reputable data providers. Do not substitute news coverage for a primary filing.
4. Read [the Nasdaq source notes](references/nasdaq-data-sources.md) for Nasdaq access options and [the VERDA notes](references/bistech-verda.md) for authorized BISTECH file access.

## Financial review

- Review at least three years of revenue, gross profit, EBITDA or operating income, net income, working capital, operating cash flow, capital expenditure, free cash flow, and net debt. Do not compare an interim period with a full year without addressing seasonality.
- Separate one-off gains and losses, inflation accounting, stock-based compensation, acquisition accounting, and currency translation. For BIST issuers, explain TMS 29 effects and distinguish nominal from real comparisons.
- Assess unit economics, customer/product/geographic concentration, competitive advantage, and capital-allocation quality.

## Valuation and market behavior

- Match the method to the business: equity-based multiples for banks and financial institutions; EV/EBITDA and free cash flow for mature industrial or service companies; unit economics, EV/revenue, and scenario DCFs for high-growth companies. Explain when a negative or unstable denominator makes a multiple meaningless.
- Filter peers for business model, margins, growth, country/currency, and accounting standards. When mixing BIST and Nasdaq peers, explicitly address country risk and currency effects.
- Use split- and dividend-adjusted prices. With sufficient history, cross-check total return, volatility, and maximum drawdown using `scripts/market_metrics.py`.
- Present base, upside, and downside cases with explicit assumptions. Do not label scenarios as probabilities unless probabilities were actually estimated.

## Thesis discipline and output

Lead with the view and what the market appears to price in. Then provide an evidence table, valuation range, three to five catalysts, three to five risks, measurable thesis confirmations and breakers, and the next dates to monitor. Put data cutoffs and sources near the claims they support. Avoid definitive buy/sell language or personalized investment advice.
