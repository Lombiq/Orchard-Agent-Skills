---
name: orchard-core-theming
description: Evidence-first Orchard Core theming playbook for shapes, alternates, placement, Razor/Liquid templates, content model access, assets/resources, and recipes used in theme work. Use for theme adjustments, shape overrides, template discovery, content item/field access, placement.json rules, and recipe authoring related to theming.
---

# Orchard Core Theming Playbook

Use this skill for Orchard Core theming and content-definition/recipe work without module development. Follow the task map and load only the minimal references needed.

## Quick start
1) Read `references/INDEX.md` for navigation and conventions.
2) Use `references/TASK-MAP.md` to jump to the exact file for the task.
3) Load only those reference files.

## Anti-hallucination rules
- Prefer repo evidence over assumptions: active theme, base theme, `placement.json`, and existing templates.
- If the shape model is unclear, trace it first (see `references/70-debugging-discovery/SHAPE-TRACE.md`).
- If part/field properties are unknown, confirm in `references/40-content-model/FIELDS.md` or the tenant's `ContentDefinition.json`.
- Ask for missing identifiers (content type, part name, field name, display type) instead of inventing them.
- Do not invent recipe steps or feature IDs; use `references/60-recipes/RECIPE-STEPS.md` and `references/60-recipes/FEATURE-CATALOG.md`.

## Common workflows
- Add or update content definitions: `references/40-content-model/CONTENT-DEFINITIONS.md`
- Override a shape: `references/80-cookbook/OVERRIDE-SHAPE.md`
- Render a content item: `references/80-cookbook/RENDER-CONTENT-ITEM.md`
- Create a setup recipe: `references/60-recipes/INDEX.md`
- Add scripts/styles: `references/80-cookbook/ADD-SECTION-RESOURCE.md`
- Shape workflow checklist: `references/20-shapes-placement/SHAPE-WORKFLOW.md`

## Working in a repo
- Confirm solution layout and active theme: `references/10-theme-basics/SOLUTION-STRUCTURE.md`, `references/10-theme-basics/THEME-STRUCTURE.md`
- Determine template language by file extension:
  - `.cshtml` -> `references/30-razor/INDEX.md`
  - `.liquid` -> `references/31-liquid/INDEX.md`
- Find `placement.json` and template overrides first; scope changes to the active theme.
- Use source discovery patterns when you need evidence from Orchard Core source: `references/70-debugging-discovery/SOURCE-DISCOVERY.md`

## Reference map
Use `references/INDEX.md` and `references/TASK-MAP.md` to locate the exact reference file for a task.

