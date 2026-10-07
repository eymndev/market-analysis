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

The extracted folder containing `plugin.json` is the plugin root. Agent Plugins 1.0 standardizes the package layout and portable components, while each client controls its own installation flow.

### VS Code

In VS Code, run **Chat: Install Plugin From Source** and enter:

```text
https://github.com/eymndev/market-analysis
```

### Codex

This package currently contains Agent Skills only, so it can be imported into Codex through Codex's user-level Agent Skills directory.

First clone or extract the repository as shown above, then run:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R "$HOME/plugins/market-analysis/skills/"* "$HOME/.agents/skills/"
```

Codex automatically discovers skills under:

```text
~/.agents/skills/
```

In Codex CLI or the Codex IDE extension, run:

```text
/skills
```

or type `$` to verify that the imported skills are available.

If a newly imported skill does not appear immediately, restart Codex.

See the official [Codex skills documentation](https://developers.openai.com/codex/skills).

### OpenClaw

OpenClaw supports Agent Plugins 1.0 bundles directly. Because this repository contains a root-level `plugin.json`, the entire package can be installed from the cloned directory.

```bash
cd ~/plugins
openclaw plugins install ./market-analysis
```

Verify that OpenClaw detected the bundle:

```bash
openclaw plugins list
openclaw plugins inspect market-analysis
```

Then restart the gateway:

```bash
openclaw gateway restart
```

The bundled Agent Skills will be available in the next OpenClaw session.

See the official [OpenClaw plugin bundle documentation](https://docs.openclaw.ai/plugins/bundles).

### Grok

#### Grok Build

Grok Build discovers user-level Agent Skills from `~/.agents/skills/`, so the same installation used by Codex works with Grok Build.

If you already completed the Codex import above, no additional copy is required.

Otherwise, run:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R "$HOME/plugins/market-analysis/skills/"* "$HOME/.agents/skills/"
```

Then open Grok Build and run:

```text
/skills
```

to view the available skills.

Grok Build also supports its own `~/.grok/skills/` directory, project-local `.grok/skills/`, enabled plugin skill directories, and additional skill paths configured in `~/.grok/config.toml`.

See the official [Grok Skills, Plugins & Marketplaces documentation](https://docs.x.ai/build/features/skills-plugins-marketplaces).

#### Grok Bot

In Grok Bot, open:

**Settings → Plugins**

Use **Marketplace** to discover packaged skills and **Yours** to manage installed or private skills. After installation, enable the skill for the current Bot if necessary.

The current public Grok Bot documentation does not document an arbitrary GitHub URL or local plugin-root import command. For direct local use of this GitHub repository, use the Grok Build Agent Skills flow above, or the one-prompt install below.

##### One-prompt install

Copy the block below and paste it into Grok Bot (or any assistant that can fetch URLs and create skills). The assistant should install all three skills automatically—no manual file copy.

```text
Install the market-analysis Agent Skills from https://github.com/eymndev/market-analysis into my skill library.

1. Fetch these SKILL.md files from the main branch (raw URLs):
   - https://raw.githubusercontent.com/eymndev/market-analysis/main/skills/fund-market-analysis/SKILL.md
   - https://raw.githubusercontent.com/eymndev/market-analysis/main/skills/equity-analysis/SKILL.md
   - https://raw.githubusercontent.com/eymndev/market-analysis/main/skills/ipo-document-analysis/SKILL.md
2. For each file, create or update a reusable skill using:
   - name: the `name` field in the YAML frontmatter
   - description: the `description` field in the YAML frontmatter
   - body: the full markdown after the frontmatter (keep headings, steps, and relative links as written)
3. Do not invent or rewrite the skill content. Use the fetched text as-is.
4. When done, confirm the three skill names are installed and briefly say how I can invoke each one.

Optional (if you can clone and keep local files): also clone https://github.com/eymndev/market-analysis.git so the skills' `references/` and `scripts/` helpers are available when needed.
```

See the official [Grok Bot skills documentation](https://docs.x.ai/grok-bot/skills-routines-and-automations).

### Claude

This repository is also a Claude plugin marketplace. The `.claude-plugin/` directory adds a Claude plugin manifest and a `marketplace.json` that points back at the same Agent Plugins 1.0 package root, so Claude loads the same `skills/` folder as every other client.

#### Claude Code

Inside a Claude Code session, add the marketplace and install the plugin:

```text
/plugin marketplace add eymndev/market-analysis
/plugin install market-analysis@market-analysis
```

Or from your shell:

```bash
claude plugin marketplace add eymndev/market-analysis
claude plugin install market-analysis@market-analysis
```

Plugin skills are namespaced under the plugin name. Type `/` and look for:

- `/market-analysis:fund-market-analysis`
- `/market-analysis:equity-analysis`
- `/market-analysis:ipo-document-analysis`

Claude also invokes them automatically when a request matches their descriptions. Run `claude plugin details market-analysis` to see the loaded skills.

To try a local clone without installing it, start Claude Code with `claude --plugin-dir ~/plugins/market-analysis`.

See the official [Claude Code plugin documentation](https://code.claude.com/docs/en/plugins/install).

#### Claude Desktop and claude.ai

1. Open **Customize** in the sidebar, then select **Plugins**.
2. Select **Add marketplace** and enter `eymndev/market-analysis` (or `https://github.com/eymndev/market-analysis`).
3. Find **Market Analysis** under **Discover** and click **Install**.

A plugin you install is saved to your Claude account, so its skills are also available in chat and in Claude Code sessions signed in to the same account.

To install from a file instead, create a package from your clone and use the upload option on the Plugins page:

```bash
cd ~/plugins/market-analysis
zip -r ../market-analysis.zip . -x '.git/*'
```

#### Claude Cowork

Open the **Cowork** tab, then **Customize → Plugins**, and follow the same **Add marketplace** steps above. Select **Check for updates** on the marketplace to pull new versions, or turn on **Sync automatically**.

See the official [Cowork plugin documentation](https://claude.com/docs/cowork/guide/plugins).

#### One-prompt install (Claude Code)

Copy the block below and paste it into Claude Code. Claude runs the install commands itself.

```text
Install the market-analysis Claude plugin from https://github.com/eymndev/market-analysis.

1. Run: claude plugin marketplace add eymndev/market-analysis
2. Run: claude plugin install market-analysis@market-analysis
3. Run: claude plugin details market-analysis and confirm it lists the skills
   equity-analysis, fund-market-analysis, and ipo-document-analysis.
4. Tell me to run /reload-plugins (or restart Claude Code), then briefly say how I can invoke each skill.

Do not modify the plugin files.
```

## Compatibility With

This package uses one portable Agent Plugins 1.0 component: **Agent Skills**. It does not include an MCP server or hooks, so MCP transport support is intentionally not claimed here. The only client-specific addition is the `.claude-plugin/` manifest and marketplace file used by Claude, which reuse the same skills.

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
