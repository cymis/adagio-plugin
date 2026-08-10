# Adagio plugin

This is the installable Adagio plugin bundle. It connects Codex to the registered hosted Adagio MCP service and contributes workflows for building, inspecting, validating, and safely editing scientific pipelines.

The package contains declarative skills, branding, and a registered app mapping. It contains no executable hooks, local MCP process, graph implementation, credentials, or customer data. Hosted mode cannot execute pipelines, access local files, or inspect local run outputs.

The app ID in `.app.json` is the registered Adagio OpenAI app ID. Release validation must confirm that it still matches the registration and is usable from an OpenAI account outside the development workspace.

For installation, authorization, privacy, revocation, and troubleshooting, see <https://docs.adagiodata.com/integrations/adagio-ai/>.
