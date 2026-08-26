# Market Analysis

<p align="center">
  <img src="docs/assets/ai-generated-label-black.svg" alt="AI generated" width="240">
</p>

A source-backed Agent Plugins 1.0 package for TEFAS/BEFAS funds, BIST and Nasdaq equities, and Turkish IPO documents.

## What it does

- Compares TEFAS and BEFAS funds by return, volatility, maximum drawdown, fees, size, and liquidity.
- Builds financial-quality, valuation, catalyst, risk, and investment-thesis analyses for BIST and Nasdaq companies.
- Cross-checks prospectuses, valuation reports, sales announcements, audit reports, legal reports, and use-of-proceeds documents.
- Recalculates IPO size, capital increase, shareholder sale, free float, and offer discount.
- Provides read-only clients for user-authorized TEFAS/BEFAS APIs and BISTECH VERDA.

## Download and install

### Clone from GitHub

```bash
git clone https://github.com/eymndev/market-analysis.git ~/plugins/market-analysis
```

Alternatively, use **Code → Download ZIP** on GitHub and extract the repository to:

```text
~/plugins/market-analysis
```

### Register in the personal marketplace

Ensure the `plugins` array in `~/.agents/plugins/marketplace.json` contains this entry. Preserve all existing entries and the existing `interface.displayName` value.

```json
{
  "name": "market-analysis",
  "source": {
    "source": "local",
    "path": "./plugins/market-analysis"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Productivity"
}
```

Install and verify the plugin:

```bash
codex plugin add market-analysis@personal
codex plugin list
```

The list should show `market-analysis@personal` as `installed, enabled`. Start a new agent task after installation so the new skills are loaded.

## Example prompts

- `Compare AFT, YAY, and TMG on TEFAS using risk-adjusted returns.`
- `Build a current investment thesis and valuation for NASDAQ:AAPL.`
- `Cross-check this Turkish IPO document set and reproduce the valuation.`

## API configuration

Never place API keys or passwords in the README, command line, repository, or plugin files. The clients read credentials from environment variables:

- TEFAS/BEFAS: `TEFAS_API_BASE_URL`, `TEFAS_API_KEY`, and, when required, `TEFAS_API_HOST`
- BISTECH VERDA: `BIST_VERDA_USER`, `BIST_VERDA_PASSWORD`, and optional `BIST_VERDA_BASE_URL`

Confirm the TEFAS provider's current base URL and authentication headers in its live documentation. BISTECH VERDA requires an institutional account and file-type permissions issued by Borsa Istanbul.

## Disclaimer

This plugin supports research and analysis; it does not provide personalized investment advice. Verify current prices, financial statements, IPO terms, and regulatory disclosures with official sources before making a decision.
