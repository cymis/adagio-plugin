# Adagio plugin

This is the installable, client-neutral Adagio plugin bundle. One skill set carries two manifests: `.codex-plugin/plugin.json` for ChatGPT and Codex surfaces, and `.claude-plugin/plugin.json` for Claude Code. Both connect to the same hosted Adagio service; the package does not execute pipelines or access local files.

The skills and guardrails are shared across clients. Change them once here; do not fork assistant-specific copies.

Codex and Claude Code both use the adjacent `.mcp.json` connection. It declares the hosted endpoint and OAuth resource so each client owns its authorization flow. The registered Adagio OpenAI app belongs to the separately reviewed official listing and is deliberately not mapped by this GitHub fallback package. The MCP descriptor contains no credentials.

For installation, authorization, privacy, revocation, and troubleshooting, see <https://docs.adagiodata.com/integrations/adagio-ai>.
