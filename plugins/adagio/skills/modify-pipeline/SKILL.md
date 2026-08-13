---
name: modify-adagio-pipeline-safely
description: Safely modify an existing Adagio pipeline with exact catalog facts, optimistic concurrency, explicit review, and recoverable conflict handling.
---

# Modify an existing pipeline safely

## Workflow

1. Call `get_adagio_context` first, resolve an unambiguous pipeline ID with `list_pipelines`, then call `get_pipeline`.
2. Record the current steps, connections, parameters, validation state, and writable status before planning changes. `update_pipeline` owns the revision precondition internally: it re-reads immediately before its conditional write and refuses a concurrent edit rather than overwriting it.
3. Search for actions and fetch exact specifications before adding or changing any action. Check every new edge with `find_compatible_actions`.
4. Preserve stable node IDs, unaffected layout, snapshots, cached-run bindings, and unrelated parameters.
5. Preflight the proposed result with the current `get_pipeline` validation state, exact action specifications, and compatibility checks for every new edge. `validate_pipeline` accepts a complete unsaved proposal rather than a patch against a stored pipeline, so do not pass it a pipeline ID or claim it dry-ran an update. Describe additions, removals, reconnections, and unresolved user decisions before writing; `update_pipeline` rejects an invalid edit without committing it.
6. Ask for explicit confirmation before removing steps, replacing methods, disconnecting data flow, or making another difficult-to-reverse change.
7. Call `update_pipeline`. It re-reads the pipeline and applies the current revision precondition internally. On a conflict, stop, refetch, explain the competing change, and ask how to reconcile it; never overwrite blindly. If the outcome is unknown, read the pipeline back and reapply only when that read proves the intended change is absent.
8. Read the pipeline back with `get_pipeline`, then return the confirmed validation state and canonical `Open in Adagio` URL.

## Guardrails

- Never invent catalog facts or fill a data-dependent value without evidence.
- Use only Adagio MCP tools to read or change Adagio state. Never fall back to UI/browser/computer control, direct HTTP/API or database access, or implementation-source inspection. If a requested edit cannot be represented, leave the pipeline unchanged and report the exact gap.
- Do not bypass community-plugin consent.
- Do not claim the hosted plugin can execute pipelines or inspect local files.
- Prefer duplicating the pipeline before a broadly destructive edit, or tell the user how Adagio history can recover it.
