---
name: validate-adagio-pipeline
description: Validate an Adagio pipeline and collect unresolved scientific, data, and configuration decisions without guessing their answers.
---

# Validate a pipeline and collect decisions

## Workflow

1. Call `get_adagio_context` first.
2. Resolve the pipeline through `list_pipelines` when necessary, then call `get_pipeline`.
3. Call `validate_pipeline` against the current graph. Fetch exact action specifications for errors involving inputs or parameters, and use `find_compatible_actions` for invalid connections.
4. Group findings into structural errors, missing runtime data, unset required parameters, and scientific decisions that require evidence.
5. For every unresolved item, explain the exact evidence or user choice needed. Leave data-dependent thresholds, depths, reference choices, and similar values unset until that evidence exists.
6. If the user asks for repairs, propose a concrete change set and switch to the safe modification workflow; do not mutate during validation alone.
7. Return the validation summary and canonical `Open in Adagio` URL.

## Guardrails

- A missing runtime file is not necessarily an invalid graph. The hosted plugin cannot inspect or bind local files.
- Do not infer data properties from names, tutorial resemblance, or method popularity.
- Do not invent actions, parameters, or compatibility results.
- This workflow is read-only until the user explicitly asks to apply a reviewed repair.
