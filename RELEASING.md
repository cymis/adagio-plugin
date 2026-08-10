# Releasing

The GitHub marketplace is a distribution path for the same Adagio plugin bundle submitted for OpenAI review. Do not fork the plugin name, skills, hosted service contract, or safety behavior for this channel.

## Release checklist

1. Sync the bundle from `.agents/plugins/plugins/adagio` in the coordinated `adagio-app` release branch into `plugins/adagio` here.
2. Update the public manifest repository URL to `https://github.com/cymis/adagio-plugin` and keep marketplace name `adagio`.
3. Keep the manifest version and `RELEASE.md` package version equal.
4. Run `python3 scripts/validate_release.py`.
5. Run the OpenAI plugin-creator validator against `plugins/adagio`.
6. Confirm the hosted readiness endpoint, OAuth protected-resource metadata, integration guide, privacy policy, and terms are available over HTTPS.
7. From an OpenAI account outside the development workspace, install the exact candidate commit and verify skills, authorization, a read-only pipeline request, cross-user denial, revocation, and the configured write policy.
8. Exercise the maintained positive and negative reviewer cases against the frozen hosted build.
9. Merge through `dev`, promote `dev` to `main`, and create a protected `v<manifest-version>` tag at the exact validated commit.
10. Publish release notes and update the integration guide before announcing installation.

Do not publish a version tag or user-facing install announcement if the external account cannot resolve the registered app mapping or complete OAuth. Investigate the registered connection before introducing a separate MCP or OAuth path.
