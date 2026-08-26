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

### Download from GitHub

```bash
git clone https://github.com/eymndev/market-analysis.git ~/plugins/market-analysis
```

Alternatively, use **Code → Download ZIP** on GitHub and extract the repository to:

```text
~/plugins/market-analysis
```

The extracted folder containing `plugin.json` is the plugin root. Agent Plugins 1.0 standardizes the package, while each client controls its own installation flow. Follow the setup guide linked in the compatibility table below and select either this GitHub repository or the downloaded plugin root.

For example, in VS Code run **Chat: Install Plugin From Source** and enter:

```text
https://github.com/eymndev/market-analysis
```

## Compatibility With

This package uses one portable Agent Plugins 1.0 component: **Agent Skills**. It does not include an MCP server, hooks, or client-specific extensions, so MCP transport support is intentionally not claimed here.

Clients are listed only when the official [Agent Plugins compatibility directory](https://agent-plugins.org/compatible-clients) identifies them as able to load Agent Skills from the portable package.

| Client | Plugin feature used |
| --- | --- |
| [VS Code](https://code.visualstudio.com/docs/agent-customization/agent-plugins) | Agent Skills |
| [Cursor](https://cursor.com/docs/plugins) | Agent Skills |
| [GitHub Copilot](https://docs.github.com/en/copilot/concepts/agents/about-plugins) | Agent Skills |
| [ChatGPT & Codex](https://developers.openai.com/plugins) | Agent Skills |
| [Kiro](https://kiro.dev/docs/powers/) | Agent Skills |
| [Hermes Agent](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins) | Agent Skills |
| [OpenClaw](https://docs.openclaw.ai/plugins/bundles) | Agent Skills |
| [Grok Bot](https://docs.x.ai/grok-bot/skills-routines-and-automations) | Agent Skills |
| [NanoClaw](https://github.com/nanocoai/nanoclaw/blob/main/docs/templates.md) | Agent Skills |

The bundled Python scripts are optional calculation and read-only API helpers. They require Python 3 and, for live API calls, the client's permission to make outbound HTTPS requests.

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
