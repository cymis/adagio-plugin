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
5. Leave data-dependent values unset when the user has not supplied inspected evidence. Explain what evidence would resolve each choice. Add a variable only for one of the reasons under Variables below.
6. Call `validate_pipeline` before writing. Present the proposed stages, unresolved decisions, and validation state.
7. Call `create_pipeline` only after the user has approved the described pipeline. Treat a retry as the same operation when the tool supports an idempotency key.
8. Read the created pipeline back with `get_pipeline`. Claim completion and return the canonical `Open in Adagio` URL only when the write and readback both confirm the intended valid graph.

## Variables

A variable is one named value that several parameters read, or one file that several inputs read. It is also the only way a pipeline exposes a setting: whoever runs it, from the command line or in run mode, can set exactly the parameters that read a variable and nothing else.

- Use a variable only when the same value or file is needed in more than one place, so one edit keeps them consistent (for example, one trim length read by two denoisers being compared, even under different parameter names, or one metadata file read by every step that needs it), or when a setting should be chosen when a finished pipeline is run or shared with others.
- Do not use one while the user is still building and running the pipeline step by step in the editor. Values go directly on the step, and file paths are typed straight on the node. An open input already takes a file at run time, so a variable never gives a single input an entry point.
- Suggest sharing a value across steps only when the user asks for it.
- A variable's value is a run-time default that can be overridden when the pipeline runs. Set one only when the variable has a real use and the science gives a reason for that value; otherwise leave it for whoever runs the pipeline and say what would decide it. A file variable stores no path, because the path depends on the machine running the pipeline.
- Use the `variables` operation to create, rename, attach, or detach variables and `removeVariables` to delete them. Remove a variable, even an unused one, only after the user confirms.
- Promotion is deprecated and no longer used; variables replace it. Do not mention promotion unless the user asks about it, and then say exactly that.

## Guardrails

- Never invent an action, type, parameter, plugin, or compatibility result.
- Use only Adagio MCP tools to read or change Adagio state. Never fall back to UI/browser/computer control, direct HTTP/API or database access, or implementation-source inspection. If the MCP cannot complete the graph, create nothing, report the exact gap, and do not claim completion.
- Do not substitute a scientifically different installed method for a missing requested method.
- Do not claim pipeline execution, local file access, or local run-output access when hosted capabilities say they are unavailable.
- Installing a community plugin always requires the separate consent flow. If host elicitation is unavailable, do not invent an approval URL: tell the user nothing was installed and direct them to add the exact plugin in Adagio's Library.
