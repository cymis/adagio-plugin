# Releasing

This repository is the source of truth for the distributable Adagio plugin bundle. Keep one client-neutral skill set and thin client manifests; do not fork skills, hosted-service contracts, or safety behavior by vendor.

OpenAI's current submission is already in review and remains frozen in that process. Updating this repository does not update OpenAI's reviewed snapshot. Future official OpenAI versions must upload or import the tagged skill bundle and complete a new review. Third-party Claude Code plugins can be submitted to Anthropic's reviewed community marketplace after release; the separate official marketplace is curated by Anthropic and has no documented public submission path.

## Release checklist

1. Make skill and manifest changes under `plugins/adagio` in this repository.
2. Keep the Codex and Claude manifests on the same version and keep both repository URLs set to `https://github.com/cymis/adagio-plugin`.
3. Keep `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json` pointed at the same `plugins/adagio` directory.
4. Run `python3 scripts/validate_release.py`.
5. Run the OpenAI plugin-creator validator against `plugins/adagio` and `claude plugin validate .` from the repository root.
6. Run each skill through the skill-creator validator.
7. Confirm the hosted readiness endpoint, OAuth protected-resource metadata, integration guide, privacy policy, and terms are available over HTTPS.
8. Install the exact candidate commit from accounts outside the development workspaces on Codex and Claude Code. Verify skill loading, authorization, a read-only request, cross-user denial, revocation, and configured write policy.
9. Exercise the maintained positive and negative reviewer cases against the frozen hosted build.
10. Merge through `dev`, promote `dev` to `main`, and create a protected `v<manifest-version>` tag at the exact validated commit.
11. Submit the tagged repository to Anthropic's community marketplace review, then track any separate official-marketplace outreach independently.
12. Publish release notes and update the integration guide before announcing installation.

Do not publish a version tag or user-facing install announcement while either client cannot install the package, load all six skills, connect to the hosted service, and complete OAuth. A direct MCP connection is a tools-only fallback and is not evidence that the skills-bearing plugin works.
