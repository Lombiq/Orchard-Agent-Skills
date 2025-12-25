# Orchard Core Theming References

A compact, source-aligned knowledge base for Orchard Core theme work and recipes.
Optimized so an agent can load just the file it needs.

## How to use
- Start at `TASK-MAP.md`.
- Open only the file for the task at hand.
- Prefer examples and ready-to-copy patterns; keep edits minimal.
- Task map links directly to leaf files to keep reference chains short.

## Conventions
- ASCII only.
- File references use inline paths like `20-shapes-placement/ALTERNATES.md`.
- Keep sections short; add examples over prose.

## Sections
- `10-understand-structure/` - Use to identify the active/base theme, confirm manifests, and locate layouts/zones.
- `20-shapes-placement/` - Use to find shape names, alternates, placement rules, and override workflow steps.
- `30-razor/` - Use to implement Razor theme changes with tag helpers, shape rendering, and IOrchardHelper.
- `40-liquid/` - Use to implement Liquid theme changes with tags, filters, and shape helpers.
- `50-content-model/` - Use to inspect content definitions and access parts/fields while rendering.
- `60-assets-resources/` - Use to include scripts/styles and manage resources and static files.
- `70-recipes/` - Use to author, validate, and reuse recipes for setup, definitions, and content import.
- `80-debugging-discovery/` - Use to trace shapes, inspect logs, and find evidence in source.
- `90-glossary/` - Use to resolve terms and acronyms in Orchard Core theming docs.

## Maintenance
- Derived from Orchard Core source and common solution patterns.
- Update when source changes or new recurring tasks appear.
