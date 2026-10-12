# Releasing

This repository is the source of truth for the distributable Adagio plugin bundle. Keep one client-neutral skill set and thin client manifests; do not fork skills, hosted-service contracts, or safety behavior by vendor.

OpenAI's current submission is already in review and remains frozen in that process. Updating this repository does not update OpenAI's reviewed snapshot. Future official OpenAI versions must upload or import the tagged skill bundle and complete a new review. Anthropic accepts plugin bundles and MCP connectors through https://claude.ai/directory/manage. Submit both from the same Claude organization; the bundle references the connector's canonical URL.

## Release checklist

1. Make skill and manifest changes under `plugins/adagio` in this repository. Keep this GitHub distribution on the direct hosted MCP descriptor; do not add the separately reviewed OpenAI app mapping.
2. Keep the Codex and Claude manifests on the same version and keep both repository URLs set to `https://github.com/cymis/adagio-plugin`.
3. Keep `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json` pointed at the same `plugins/adagio` directory.
4. Run `python3 scripts/validate_release.py`.
5. Run the OpenAI plugin-creator validator against `plugins/adagio` and `claude plugin validate ./plugins/adagio` from the repository root.
6. Run each skill through the skill-creator validator.
7. Deploy the gateway and proxy root-endpoint changes before publishing this bundle or the updated installation guide. Confirm the hosted readiness endpoint, OAuth protected-resource metadata, integration guide, privacy policy, and terms are available over HTTPS.
8. Install the exact candidate commit from accounts outside the development workspaces on Codex and Claude Code. Confirm each client loads the direct hosted MCP server rather than an official app mapping, then verify skill loading, authorization, a read-only request, cross-user denial, revocation, and configured write policy.
9. Exercise the maintained positive and negative reviewer cases against the frozen hosted build.
10. Merge through `dev`, promote `dev` to `main`, and create a protected `v<manifest-version>` tag at the exact validated commit.
11. Update the existing Anthropic plugin submission and submit the hosted MCP connector using the settings below. Pair the two listings from the same organization; do not withdraw the pending plugin to create a duplicate.
12. Publish release notes and update the integration guide before announcing installation.

Do not publish a version tag or user-facing install announcement while either client cannot install the package, load all six skills, connect to the hosted service, and complete OAuth. A direct MCP connection is a tools-only fallback and is not evidence that the skills-bearing plugin works.

## Claude connector submission

Submit the MCP server separately from the existing `plugins/adagio` bundle in
[the developer portal](https://claude.ai/directory/manage). Use:

| Field | Value |
| --- | --- |
| Submission kind | MCP connector |
| Connection | Universal URL: `https://mcp.adagio.run` |
| Authentication | OAuth with dynamic client registration (`oauth_dcr`) |
| Sign-in | Required before tools can run; no static request headers |
| Documentation | `https://docs.adagio.run/integrations/adagio-ai/` |
| Privacy policy | `https://adagio.run/privacy` |
| Product and support | `https://adagio.run` and `https://adagio.run/contact` |
| Capabilities | Reads and writes pipeline definitions and plugin-library metadata; no pipeline execution or local-file access |

The gateway advertises S256 PKCE, the authorization and token endpoints, and
dynamic registration. Leave manually supplied OAuth client credentials empty.
The hosted Claude callback is `https://claude.ai/api/mcp/auth_callback`.
Use the same MCP URL for the connector and plugin so they can be paired.

In **Test & launch**, supply the dedicated synthetic reviewer's credentials
privately, together with these steps. Never commit credentials, tokens, or
concrete private fixture IDs to this repository.

1. Add/connect the server in a fresh Claude account or browser session. Choose
   **Register automatically** if Claude asks how to identify its OAuth client.
2. For the existing isolated reviewer account, choose **Continue with
   AdagioOpenAIReviewer** on Adagio's sign-in page, then enter the supplied
   credentials on the reviewer sign-in page. Its password does not work in the
   ordinary Adagio email/password form. The account must already be provisioned,
   confirmed, and populated with the named sample pipelines.
   Document any required second factor or invitation steps so the reviewer can
   complete them without access to the maintainer's inbox or device.
3. Ask: "Show my Adagio pipelines." Then ask Claude to inspect and validate the
   supplied sample pipeline. Record the expected fixture names privately.
4. Ask for a small new pipeline, review its proposed actions, approve saving,
   and verify it appears in Adagio. Use disposable synthetic data and ensure the
   reviewer is allowed through the write rollout gate and has remaining quota.
5. Exercise every exposed tool, including protected plugin-library consent, and
   confirm cross-account reads and writes are refused. The app repository's
   `mcp/evals/openai-review-cases.md` supplies reusable synthetic cases; adapt the
   client-specific steps for Claude.
6. Verify a real token refresh after sign-in, including the configured refresh
   token rotation. Disconnect/reconnect, then verify that revoking **Claude** in
   **Adagio → Settings → AI → AI assistants** requires a fresh authorization.

Do not attest that these checks passed until they have run against the deployed
candidate using the supplied account. A successful package scan or an existing
maintainer connection is not a reviewer-account acceptance test.

References checked October 5, 2026:
[submission types](https://claude.com/docs/directory/publish),
[connector submission](https://claude.com/docs/connectors/building/submission),
[authentication](https://claude.com/docs/connectors/building/authentication).
