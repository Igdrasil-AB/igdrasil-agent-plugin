# Security Policy

## This package must never contain secrets

This is a public repository. Do not add any of the following:

- API keys, OAuth client secrets or static MCP keys
- `headers`, `Authorization` values or bearer tokens in `.mcp.json` or `mcp.json`
- environment files, private keys or database credentials

CI enforces this (`.github/workflows/check.yml`).

The hosted MCP server uses OAuth only. An unauthenticated request to
`https://accounting.igdrasil.se/api/mcp` gets a `401` that points to the
protected-resource metadata. The client then completes PKCE sign-in by
itself, so the URL is the only configuration a client needs.

## The boundary we promise

A client connected through this plugin can read data and stage operations for
a person to review, including payments and VAT or tax filings. It must **not**
be able to:

- approve or apply a staged operation, or post, reverse or close books
- transfer money or pay invoices without a person approving and signing
- file VAT or tax returns without a person approving and signing
- delete records

If you find a way to do any of these through this plugin, that is a defect in
Igdrasil. Please report it.

## Reporting a vulnerability

Email [erik@igdrasil.se](mailto:erik@igdrasil.se). Do not open a public issue
that contains secrets, tokens or customer data.
