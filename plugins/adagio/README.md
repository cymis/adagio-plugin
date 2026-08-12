# Adagio plugin

This is the installable, client-neutral Adagio plugin bundle. One skill set carries two manifests: `.codex-plugin/plugin.json` for ChatGPT and Codex surfaces, and `.claude-plugin/plugin.json` for Claude Code. Both connect to the same hosted Adagio service; the package does not execute pipelines or access local files.

The skills and guardrails are shared across clients. Change them once here; do not fork assistant-specific copies.

The app ID in `.app.json` is the registered Adagio OpenAI app ID and applies only to ChatGPT and Codex. Claude Code uses the adjacent `.mcp.json` connection. Neither file contains credentials.

For installation, authorization, privacy, revocation, and troubleshooting, see <https://docs.adagiodata.com/integrations/adagio-ai>.
