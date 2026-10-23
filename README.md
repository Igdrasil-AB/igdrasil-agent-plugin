# Igdrasil Bokföring

The Igdrasil Bokföring plugin connects Claude, ChatGPT/Codex and Grok to [Igdrasil](https://igdrasil.se), the
Swedish BAS accounting platform from Igdrasil AB. You can ask about your
company's results, VAT position, open invoices, documents and bank
reconciliation.

This repository holds plugin manifests, MCP pointers and skills. It contains no
product code.

## What it can do

When you connect the hosted Igdrasil MCP server, your AI client can:

- **Read** headline figures, the resultaträkning (income statement), the
  balance sheet, the VAT position (rutor, amount to pay or reclaim), open
  customer invoices, accounting documents, bank balances and the
  reconciliation status.
- **Prepare** some changes, such as a proposed journal entry or a bank match,
  as *staged operations*. A staged operation changes nothing in your books. A
  person has to review it and apply it in the
  [Igdrasil app](https://accounting.igdrasil.se).

## What it cannot do

AI clients connected through this plugin cannot apply changes, move money, pay
invoices, run payroll, file tax or VAT returns, or delete records. The server
enforces this, and the skills also refuse such requests.

## Install

Claude Code:

```text
/plugin marketplace add Igdrasil-AB/igdrasil-agent-plugin
/plugin install igdrasil-bokforing@igdrasil
```

Claude.ai and ChatGPT: add Igdrasil Bokföring from the connector or plugin directory once
it is listed there. Until then, add a custom connector with the URL below.

## Connect

Hosted MCP endpoint (OAuth with PKCE; your client handles sign-in):

```text
https://accounting.igdrasil.se/api/mcp
```

ChatGPT and Codex use `https://accounting.igdrasil.se/api/mcp/chatgpt`. It
lists every operation as its own tool and leaves out the search-and-call
router, which OpenAI's plugin review does not accept. Sign-in and permissions
are the same on both.

The plugin has no API key, and none is needed.

| Path | Used by |
|---|---|
| `.claude-plugin/plugin.json`, `.mcp.json` | Claude (Code, Cowork, Desktop) and Grok Build, which reads Claude plugins |
| `plugin.json`, `mcp.json` | OpenAI ChatGPT and Codex (Agent Plugins 1.0.0) |
| `skills/` | Monthly finance review, Swedish VAT review, open invoice review |

Developer documentation: <https://developer.igdrasil.se/mcp-api>

## Legal

- Privacy policy: <https://igdrasil.se/privacy>
- Terms: <https://igdrasil.se/terms>
- Licence for this package: Apache License 2.0. The Igdrasil product is
  licensed separately.

## Contact

Support: [erik@igdrasil.se](mailto:erik@igdrasil.se). For security reports, see
`SECURITY.md`.
