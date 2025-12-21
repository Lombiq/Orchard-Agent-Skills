---
name: orchard-core-theming
description: Evidence-first Orchard Core theming playbook for shapes, alternates, placement, Razor/Liquid templates, content model access, assets/resources, and recipes used in theme work. Use for theme adjustments, shape overrides, template discovery, content item/field access, placement.json rules, and recipe authoring related to theming.
---

# Orchard Core Theming Playbook

Use this skill for Orchard Core theming and content-definition/recipe work. Follow the task map and load only the minimal references needed.

## Quick start
1) Read `references/INDEX.md` for navigation and conventions.
2) Use `references/TASK-MAP.md` to jump to the exact file for the task.
3) Load only those reference files.

## Anti-hallucination rules
- Prefer repo evidence over assumptions: active theme, base theme, `placement.json`, and existing templates.
- If the shape model is unclear, trace it first. Use `references/TASK-MAP.md` to find the shape tracing guidance.
- If part/field properties are unknown, confirm in `ContentDefinition.json` and the field reference (see `references/TASK-MAP.md`).
- Ask for missing identifiers (content type, part name, field name, display type) instead of inventing them.
- Do not invent recipe steps or feature IDs; use `references/TASK-MAP.md` to find the right recipe references.

## Common workflows
- Use `references/TASK-MAP.md` for tasks like content definitions, setup recipes, shape overrides, and asset inclusion.

## Working in a repo
- Confirm solution layout, active theme, and template language using `references/TASK-MAP.md`.
- Find `placement.json` and template overrides first; scope changes to the active theme.
- Use source discovery patterns when you need evidence from Orchard Core source (see `references/TASK-MAP.md`).

## Reference map
Use `references/INDEX.md` and `references/TASK-MAP.md` to locate the exact reference file for a task.

