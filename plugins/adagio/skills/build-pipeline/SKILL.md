---
name: build-adagio-pipeline
description: Build a new Adagio pipeline from a user's scientific goal while using only actions and parameter names verified against their installed catalog.
---

# Build an Adagio pipeline

Use this workflow when the user wants a new pipeline or a substantial new branch of work.

## Workflow

1. Call `get_adagio_context` first. Treat its release, capabilities, and installed catalog as authoritative.
2. Clarify the scientific objective, input semantic types, desired outputs, and any choices whose answers materially change the method.
3. Use `search_actions` for concepts, never memory-derived identifiers. Use `find_compatible_actions` to verify every intended connection.
4. Call `get_action_specs` for every selected action before setting inputs or parameters. Use exact returned names and allowed values.
5. Leave data-dependent values unset when the user has not supplied inspected evidence. Explain what evidence would resolve each choice.
6. Call `validate_pipeline` before writing. Present the proposed stages, unresolved decisions, and validation state.
7. Call `create_pipeline` only after the user has approved the described pipeline. Treat a retry as the same operation when the tool supports an idempotency key.
8. Read the created pipeline back with `get_pipeline`. Claim completion and return the canonical `Open in Adagio` URL only when the write and readback both confirm the intended valid graph.

## Guardrails

- Never invent an action, type, parameter, plugin, or compatibility result.
- Use only Adagio MCP tools to read or change Adagio state. Never fall back to UI/browser/computer control, direct HTTP/API or database access, or implementation-source inspection. If the MCP cannot complete the graph, create nothing, report the exact gap, and do not claim completion.
- Do not substitute a scientifically different installed method for a missing requested method.
- Do not claim pipeline execution, local file access, or local run-output access when hosted capabilities say they are unavailable.
- Installing a community plugin always requires the separate consent flow. If host elicitation is unavailable, do not invent an approval URL: tell the user nothing was installed and direct them to add the exact plugin in Adagio's Library.
