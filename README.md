# Adagio plugin

This repository is the public source and GitHub marketplace for the Adagio plugin. The same client-neutral skills help ChatGPT, Codex, and Claude Code inspect, build, validate, and safely update scientific pipelines through Adagio's hosted MCP service.

The GitHub marketplace is an independent distribution path. It is published by Adagio, but installing it does not mean OpenAI or Anthropic has reviewed it. OpenAI's official listing is already in review; after approval and publication, it will appear in the universal Plugins Directory shared by ChatGPT and Codex. Anthropic accepts third-party submissions into its reviewed community marketplace; its separate official marketplace is curated at Anthropic's discretion.

| Surface | Distribution | Status |
| --- | --- | --- |
| ChatGPT and Codex | OpenAI Plugins Directory | In review; OpenAI distributes the reviewed app and skill snapshot |
| Claude Code | Anthropic official marketplace | Curated by Anthropic; no public submission path is documented |
| Claude Code | Anthropic community marketplace | Submission follows the tagged public release |
| Codex | This GitHub marketplace | Release candidate; independent direct-MCP fallback |
| Claude Code | This GitHub marketplace | Release candidate; independent fallback |
| Claude and other MCP clients | Direct hosted MCP connection | Tools only; does not install the guided skills |

The public bundle lives under [`plugins/adagio`](plugins/adagio). Edit the shared skills there once; do not maintain vendor-specific skill copies.

## Install a released GitHub build

You need an Adagio account and a client with plugin marketplace support. The `v0.1.1` tag will be published only after cross-client release validation passes. Until that tag exists, these commands intentionally do not install a moving release candidate.

### Claude Code

```text
/plugin marketplace add cymis/adagio-plugin@v0.1.1
/plugin install adagio@adagio
/reload-plugins
```

Starting a new Claude Code session also loads the installed plugin. Connect your Adagio account when the hosted service first requests authorization.

### Codex

```bash
codex plugin marketplace add cymis/adagio-plugin --ref v0.1.1
codex plugin add adagio@adagio
```

Restart Codex, begin a new task, and connect your Adagio account when prompted.

For either client, start with a read-only request such as:

> Show my Adagio pipelines.

## Capabilities and boundaries

The plugin can:

- list, inspect, create, validate, and safely edit pipelines;
- search the action catalog and verify semantic-type compatibility;
- add a community plugin to your private Adagio library only through the protected consent flow.

It cannot execute pipelines, read local files, inspect local run outputs, control Adagio Desktop, or access raw biological artifacts. Local execution remains in Adagio Desktop.

The installed package contains declarative skills, SVG assets, metadata, and one direct hosted MCP descriptor shared by Codex and Claude Code. It does not contain or install the registered OpenAI app mapping used by the separately reviewed official listing, and it contains no credentials, executable hooks, package dependencies, or local server. See the [Adagio AI integration guide](https://docs.adagiodata.com/integrations/adagio-ai/) for permissions, data boundaries, revocation, and troubleshooting.

## Update

For Claude Code, refresh the marketplace and plugin:

```text
/plugin marketplace update adagio
/plugin update adagio@adagio
/reload-plugins
```

For Codex, move a pinned installation to a newer release:

```bash
codex plugin remove adagio@adagio
codex plugin marketplace remove adagio
codex plugin marketplace add cymis/adagio-plugin --ref vX.Y.Z
codex plugin add adagio@adagio
```

Start a new task after reinstalling so the client loads the updated skills and tools.

## Remove or migrate to an official listing

Remove the GitHub plugin and its marketplace before installing the corresponding official listing. This avoids duplicate skills and tool connections. Removing a plugin does not revoke its Adagio authorization; revoke the connection under **Adagio → Profile → AI assistants**.

Reviewed-directory installation links will be published in the [integration guide](https://docs.adagiodata.com/integrations/adagio-ai/) after each vendor approves and publishes its listing.

## Support and security

For public questions, use [Adagio Community](https://github.com/cymis/adagio-community/discussions). For product support, visit [Adagio contact and support](https://adagio.run/contact).

Do not report vulnerabilities in a public issue or discussion. Follow [SECURITY.md](SECURITY.md).
