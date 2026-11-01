# Google Connected Apps listing kit

This folder is a docs-only listing kit for Igdrasil on Google's Connected Apps Platform. Nothing in it has been submitted to Google. It does not file an application, create a console account, or add testers.

The console-ready copy is in [listing.md](listing.md).

## What the platform is

The Connected Apps Platform is a Google preview, managed in the Google Connected Console. A developer connects a cloud-hosted MCP server, then registers, tests, and submits the app in the console. Before review, the developer chooses Search, the Gemini app, or both. A user calls the app with `@` plus the app name, or Gemini selects it from the conversation.

Google's pages:

- [Connected Apps Platform](https://developers.google.com/connected-apps)
- [Build and manage Connected Apps in one place](https://blog.google/innovation-and-ai/technology/developers-tools/connected-apps-one-place/) (28 October 2026)
- [MCP server developer guide](https://developers.google.com/connected-apps/mcp)
- [Prerequisites](https://developers.google.com/connected-apps/gpc/prerequisites) (updated 30 October 2026 UTC)
- [Register, test, and publish](https://developers.google.com/connected-apps/gpc/perform-the-steps)
- [Connected Apps policy](https://developers.google.com/connected-apps/connected-apps-policy)

The policy page calls the catalog the Connected Apps Registry. Google's launch post says access is opening in phases, with more developers, markets, and Google products over the coming months. The preview starts with the [interest form](https://connected.google.com/console/help/?apply). The console is at [connected.google.com/console](https://connected.google.com/console).

## Who can use it today

Checked against Google's help pages on 1 November 2026. Igdrasil in this listing is a Swedish-only product. The surfaces Google documents today are the United States and English.

- Gemini custom connected apps: people in the United States, age 18 or over, signed in with a personal Google Account, in English, on the Gemini web app and the Gemini mobile app. Google's help page says a work or school Google Account cannot use this yet. [Connect and manage custom apps for Gemini Apps](https://support.google.com/gemini/answer/17209137).
- Connected Apps in Search AI Mode: available in AI Mode in the United States, in English. [Use and manage Connected Apps in Search](https://support.google.com/websearch/answer/17265703).

Each version has country and language selectors in Connected Console ([step 7](https://developers.google.com/connected-apps/gpc/perform-the-steps)). The user limits above are the ones Google documents for those products today, so a Swedish-only listing has no audience on them yet.

## Approval still required

Nothing has been submitted. Filing Google's interest form, creating a Connected Console account, and choosing testers need Gson's approval first.

Google allows only `@gmail.com` accounts as testers ([step 8](https://developers.google.com/connected-apps/gpc/perform-the-steps)). That conflicts with Igdrasil's rule that identities are `@igdrasil.se` only. An account owner or admin must also accept the Connected Apps Terms of Service before anyone can create an app ([prerequisites](https://developers.google.com/connected-apps/gpc/prerequisites)).

Category and connection type are chosen when the app is created, and both stay fixed after that ([step 1](https://developers.google.com/connected-apps/gpc/perform-the-steps)). This kit leaves both for that later decision.

## Requirements checklist

The copy covers three read-only areas: results and balance, the VAT position, and unpaid customer invoices. Those areas follow the skills in this repo:

- `skills/monthly-finance-review` for results and balance
- `skills/swedish-vat-review` for the VAT position
- `skills/open-invoice-review` for unpaid customer invoices

| Item | Status | Owner |
| --- | --- | --- |
| Metadata and copy (name, description, capabilities, example prompts, terms, privacy, website) | done | This kit |
| 512×512 icon, and a round SVG account-linking logo | todo | Design |
| Server instructions text | todo | Philip, Vinod and Gson (accounting side) |
| Router-free endpoint choice | todo | Philip, Vinod and Gson (accounting side) |
| `/.well-known/google-connected-apps` verification file | todo | Philip, Vinod and Gson (accounting side) |
| Google OAuth redirect URIs | todo | Philip, Vinod and Gson (accounting side) |
| Seeded test account | todo | Philip, Vinod and Gson (accounting side) |

### Metadata and copy

Done in [listing.md](listing.md). Google's field rules, from the [prerequisites](https://developers.google.com/connected-apps/gpc/prerequisites) and [step 2](https://developers.google.com/connected-apps/gpc/perform-the-steps):

- The name is also the `@` handle.
- The description is one sentence, under 30 words.
- At least three capabilities, one task per entry, with no leading number.
- At least three example prompts. At least two start with `@` and the app name. At least one mentions the name mid-sentence. No leading number and no quotation marks.
- Translations sit inside locale tags, such as `<sv-SE>` and `</sv-SE>`, in the same field.
- Terms of Service and Privacy Policy URLs are required. A website URL is optional.

### Icon and account-linking logo

Todo for design.

- App icon: JPG or PNG, 512×512 px, 1 MB or less ([step 2](https://developers.google.com/connected-apps/gpc/perform-the-steps)). `assets/icon.png` and `assets/logo.png` are 500×500 px, so design still needs a 512×512 export.
- Account-linking logo: a square SVG with a circular appearance, at least 500×500 px, for the account-linking and consent screens ([OAuth 2.1 guide](https://developers.google.com/connected-apps/mcp/oauth)). The repo has no such SVG yet.

### Server instructions text

Todo for Philip, Vinod and Gson on the accounting side.

Google strongly recommends server instructions at initialize time, describing the domain and the capabilities, because the model uses them when deciding when to call the app ([MCP guide, phase 1](https://developers.google.com/connected-apps/mcp)). The [policy](https://developers.google.com/connected-apps/connected-apps-policy) requires those instructions to be available at ingestion, to leave other tools alone, to stay out of tool responses, and to describe the real behaviour.

### Router-free endpoint choice

Todo for Philip, Vinod and Gson on the accounting side.

Each connected app has one global MCP connection, and Google recommends a new one for each published version ([prerequisites](https://developers.google.com/connected-apps/gpc/prerequisites), [step 6](https://developers.google.com/connected-apps/gpc/perform-the-steps)). This listing is read-only. The accounting side still chooses one router-free connection that exposes those read-only tools directly. The address stays out of this kit.

### Verification file

Todo for Philip, Vinod and Gson on the accounting side.

After a console account exists, Google provides a `google-connected-apps.json` token file. Its content has to be served at `/.well-known/google-connected-apps` on the MCP server's domain, with HTTP 200 and no redirect ([step 3](https://developers.google.com/connected-apps/gpc/perform-the-steps)). The token exists only after someone is in the console, which needs Gson's approval.

### Google OAuth redirect URIs

Todo for Philip, Vinod and Gson on the accounting side.

User-delegated sign-in needs the app-specific Google OAuth redirect URIs from Connected Console on the authorization server's allowlist. The console shows the exact URIs for that app ([step 4](https://developers.google.com/connected-apps/gpc/perform-the-steps), [OAuth 2.1 guide](https://developers.google.com/connected-apps/mcp/oauth)).

### Seeded test account

Todo for Philip, Vinod and Gson on the accounting side.

User-delegated review needs seeded test credentials with realistic sample data, two-factor authentication turned off, and written test instructions. If Google cannot fully test the app, it may be rejected ([step 5](https://developers.google.com/connected-apps/gpc/perform-the-steps)).
