# Release metadata

- Package version: 0.1.1
- Distribution: `cymis/adagio-plugin`, marketplace `adagio`
- Pipeline specification: 1.0.0rc
- Hosted MCP resource: `https://mcp.adagio.run`
- MCP endpoint: `https://mcp.adagio.run/mcp`
- Supported products: ChatGPT and Codex surfaces that support universal plugins; Claude Code through the repository marketplace
- Execution: not exposed in the first public release
- Local files: never available to the hosted integration

Before release, confirm the registered OpenAI app ID, the Claude Code MCP connection, current vendor requirements, and the frozen hosted build. Then run repository and plugin validation and exercise the positive and negative reviewer cases.

Release ordering is strict: deploy and verify `https://docs.adagiodata.com/integrations/adagio-ai` first, then build or publish any plugin package or Desktop release that references it. Do not publish a listing until its final URL is known and the package has been updated and revalidated.

Keep both committed manifest versions and the Claude marketplace metadata version equal to the package version above. The GitHub release tag must be `v<package-version>` and must point at the exact commit that passed acceptance tests on both clients.
