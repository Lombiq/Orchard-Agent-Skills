# Agent Instructions

This repository contains agent-agnostic skills under `skills/`. Follow these rules when creating or editing skills.

## Skill structure
- Place each skill in its own folder under `skills/<skill-name>/`.
- `SKILL.md` must include YAML frontmatter with only `name` and `description`.
- Use `references/` for supporting docs, and prefer task-focused leaf files.
- References to files should be relative to the skill root.
- Avoid long reference chains; make `references/TASK-MAP.md` point directly to leaf files.

## Content conventions
- Default to ASCII in skill files.
- Avoid `README.md` inside skill folders.
- Keep guidance concise and example-driven.

## Orchard Core theming skill notes
- Keep Razor and Liquid references separate (`references/30-razor/` and `references/40-liquid/`).
- Update `references/TASK-MAP.md` when adding new workflows.
- Preserve existing content unless the change is deliberate and documented.
- Follow the [orchard-core-theming maintenance guide](maintenance/orchard-core-theming.md) for step-by-step update workflows when the user requests them.
