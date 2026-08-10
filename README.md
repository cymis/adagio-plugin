# Adagio for Codex

This repository is the public source and GitHub marketplace for the Adagio plugin for Codex. It lets Codex inspect, build, validate, and safely update scientific pipelines in your Adagio account.

The GitHub distribution is a beta installation path while the same plugin completes review for OpenAI's public plugin directory. It is not an OpenAI-reviewed listing.

## Install

You need an Adagio account and a current Codex installation with plugin marketplace support.

Install the released, version-pinned marketplace and plugin:

```bash
codex plugin marketplace add cymis/adagio-plugin --ref v0.1.0
codex plugin add adagio@adagio
```

Restart Codex, begin a new task, and connect your Adagio account when prompted. Start with a read-only request such as:

> Show my Adagio pipelines.

The `v0.1.0` tag will be published only after the external-account authorization test passes. Until that tag exists, this repository is a release candidate and the commands above intentionally do not install from a moving branch.

## Capabilities and boundaries

The plugin can:

- list, inspect, create, validate, and safely edit pipelines;
- search the action catalog and verify semantic-type compatibility;
- add a community plugin to your private Adagio library only through the protected consent flow.

It cannot execute pipelines, read local files, inspect local run outputs, control Adagio Desktop, or access raw biological artifacts. Local execution remains in Adagio Desktop.

The installed package contains only declarative skills, SVG assets, metadata, and a registered hosted app mapping. It does not install executable hooks, scripts, package dependencies, or a local server. Inspect the complete bundle under [`plugins/adagio`](plugins/adagio).

See the [Adagio AI integration guide](https://docs.adagiodata.com/integrations/adagio-ai/) for requested permissions, data boundaries, revocation, and troubleshooting.

## Update

Pinned marketplace releases do not move automatically. To move to a newer released tag, remove the installed beta and marketplace, then add the new tag and reinstall:

```bash
codex plugin remove adagio@adagio
codex plugin marketplace remove adagio
codex plugin marketplace add cymis/adagio-plugin --ref vX.Y.Z
codex plugin add adagio@adagio
```

Start a new task after reinstalling so Codex loads the updated skills and tools.

## Remove or migrate to the reviewed listing

Remove the GitHub beta with:

```bash
codex plugin remove adagio@adagio
codex plugin marketplace remove adagio
```

Removing the plugin does not revoke its Adagio authorization. To revoke access, open **Adagio → Profile → AI assistants** and choose **Revoke access**.

When the reviewed listing becomes available, remove this GitHub beta before installing the reviewed Adagio listing to avoid duplicate skills or tools. The official installation link will be published in the [integration guide](https://docs.adagiodata.com/integrations/adagio-ai/).

## Support and security

For public questions, use [Adagio Community](https://github.com/cymis/adagio-community/discussions). For product support, visit [Adagio contact and support](https://adagio.run/contact).

Do not report vulnerabilities in a public issue or discussion. Follow [SECURITY.md](SECURITY.md).
