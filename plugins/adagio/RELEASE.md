# Release metadata

- Package version: 0.1.4
- Distribution: `cymis/adagio-plugin`, marketplace `adagio`
- Pipeline specification: 1.0.0rc
- Hosted MCP resource: `https://mcp.adagio.run`
- MCP endpoint: `https://mcp.adagio.run`
- Supported products: Codex and Claude Code through the repository marketplace; the separately reviewed OpenAI listing remains its own distribution track
- Execution: not exposed in the first public release
- Local files: never available to the hosted integration

## Changes in 0.1.4

Pipeline building and editing default to direct parameters and file paths.
Unknown scientific values remain unset on their steps. Shared variables keep
intentionally shared values consistent. Agents may recommend which settings to
expose for a finished pipeline, but create variables for run mode or command-line
configuration only when the user explicitly requests it. Building, completing,
sharing, or asking for recommendations alone does not request those changes.

This patch changes skill guidance and release metadata. The six skills, hosted
MCP endpoint, OAuth permissions, and execution boundaries are unchanged.

Before release, confirm the direct hosted MCP connection independently on Codex and Claude Code, current vendor requirements, and the frozen hosted build. The registered OpenAI app is validated in its separate official review track. Then run repository and plugin validation and exercise the positive and negative reviewer cases.

Release ordering is strict: deploy and verify `https://docs.adagio.run/integrations/adagio-ai` first, then build or publish any plugin package or Desktop release that references it. Do not publish a listing until its final URL is known and the package has been updated and revalidated.

Keep both committed manifest versions and the Claude marketplace metadata version equal to the package version above. The GitHub release tag must be `v<package-version>` and must point at the exact commit that passed acceptance tests on both clients.
