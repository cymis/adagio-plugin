---
name: find-compatible-adagio-actions
description: Find installed Adagio actions that can consume a pipeline output using the same semantic-type compatibility rules as the Adagio canvas.
---

# Find compatible actions

## Workflow

1. Call `get_adagio_context` first.
2. Resolve the source from an inspected pipeline or from an exact semantic type supplied by the user. Do not infer a type from a file extension or name.
3. Call `find_compatible_actions` for the exact output or semantic type.
4. Use `search_actions` to narrow results by scientific purpose, then call `get_action_specs` for serious candidates.
5. Explain factual compatibility separately from scientific suitability. When several established methods exist, compare the evidence that would lead to each and let the user decide.
6. If no action matches, distinguish a known registered type with no consumer from an unregistered type. That distinction determines whether the gap is likely one wrapper action or new types, formats, and transformers.

## Guardrails

- Never claim compatibility based on memory or similar spelling.
- Use only Adagio MCP tools to establish Adagio catalog and compatibility facts. Never fall back to UI/browser/computer control, direct HTTP/API or database access, or implementation-source inspection. Report an MCP limitation instead.
- Never silently substitute an available method for the requested method.
- Do not install a community plugin without explicit consent through the protected flow.
- This skill does not execute actions or inspect local data.
