---
name: modify-adagio-pipeline-safely
description: Safely modify an existing Adagio pipeline with exact catalog facts, optimistic concurrency, explicit review, and recoverable conflict handling.
---

# Modify an existing pipeline safely

## Workflow

1. Call `get_adagio_context` first, resolve an unambiguous pipeline ID with `list_pipelines`, then call `get_pipeline`.
2. Record the returned version or concurrency token before planning changes.
3. Search for actions and fetch exact specifications before adding or changing any action. Check every new edge with `find_compatible_actions`.
4. Preserve stable node IDs, unaffected layout, snapshots, cached-run bindings, and unrelated parameters.
5. Validate the proposed result before writing. Describe additions, removals, reconnections, and unresolved user decisions.
6. Ask for explicit confirmation before removing steps, replacing methods, disconnecting data flow, or making another difficult-to-reverse change.
7. Call `update_pipeline` with the latest expected version and a stable operation ID. On a conflict, stop, refetch, explain the competing change, and ask how to reconcile it; never overwrite blindly.
8. Return the updated validation state and canonical `Open in Adagio` URL.

## Guardrails

- Never invent catalog facts or fill a data-dependent value without evidence.
- Use only Adagio MCP tools to read or change Adagio state. Never fall back to UI/browser/computer control, direct HTTP/API or database access, or implementation-source inspection. If a requested edit cannot be represented, leave the pipeline unchanged and report the exact gap.
- Do not bypass community-plugin consent.
- Do not claim the hosted plugin can execute pipelines or inspect local files.
- Prefer duplicating the pipeline before a broadly destructive edit, or tell the user how Adagio history can recover it.
