# Security policy

## Reporting a vulnerability

Do not report security vulnerabilities in public issues or discussions.

Email [security@adagio.run](mailto:security@adagio.run) with a description, affected version, reproduction steps, and impact. Do not include access tokens, customer data, protected health information, biological datasets, or credentials. If a secure transfer is needed, request one before sending sensitive material.

## Scope

Reports may cover:

- the plugin bundle or marketplace in this repository;
- the hosted endpoint at `https://mcp.adagio.run`;
- authentication, authorization, consent, revocation, or cross-account isolation;
- unexpected exposure of pipeline or catalog data.

The public plugin repository intentionally contains no hosted server implementation, credentials, customer data, local-execution code, or executable lifecycle hooks.

## Supported releases

Security fixes are applied to the latest released plugin version. Beta users may need to reinstall from a newer pinned Git tag after a fix is published.
