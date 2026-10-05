# Adagio plugin

This is the installable, client-neutral Adagio plugin bundle. One skill set carries two manifests: `.codex-plugin/plugin.json` for ChatGPT and Codex surfaces, and `.claude-plugin/plugin.json` for Claude Code. Both connect to the same hosted Adagio service; the package does not execute pipelines or access local files.

The skills and guardrails are shared across clients. Change them once here; do not fork assistant-specific copies.

Codex and Claude Code both use the adjacent `.mcp.json` connection. It declares the hosted endpoint and OAuth resource so each client owns its authorization flow. The registered Adagio OpenAI app belongs to the separately reviewed official listing and is deliberately not mapped by this GitHub fallback package. The MCP descriptor contains no credentials.

For installation, authorization, privacy, revocation, and troubleshooting, see <https://docs.adagiodata.com/integrations/adagio-ai>.

## Connect your account

You need an existing Adagio account. If you do not have one, request access at
<https://adagio.run/contact> before connecting. The hosted MCP URL and OAuth
resource are both `https://mcp.adagio.run`. Sign in with your own Adagio account
when Claude or Codex prompts you; no API key or manually supplied OAuth client
secret is needed. In Claude's custom-connector settings, choose **Register
automatically** if a client-registration choice is shown.

Start with "Show my Adagio pipelines," then ask to explain or validate one.
The plugin can create and edit pipeline definitions after the applicable
approvals. Execution and access to local files remain in Adagio Desktop.

To revoke authorization, open **Adagio → Profile → AI assistants** and revoke
the corresponding assistant. Removing the plugin alone does not revoke access.
