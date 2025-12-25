# Lombiq Orchard Agent Skills

## About

This repository contains [agent skills](https://agentskills.io/home) for [Orchard Core](https://orchardproject.net) development tasks. Orchard Core is an open-source, modular, and multi-tenant application framework and CMS built on .NET and ASP.NET Core. With these skills, you can use your favorite agent efficiently for common Orchard Core tasks.

## Skills included

### `orchard-core-theming`

A playbook covering common Orchard Core theme development tasks, such as shape development, and recipe management. It contains many agent-optimized markdown docs with guides and examples as well as scripts for recurring operations.

Highlights:
- Creates and implements ad-hoc shape templates, or override content templates using the correct alternates.
- Can use common tag helpers, Liquid filters, and `IOrchardHelper` extensions in templates.
- Reads content definitions via `ContentDefinition.json` (when `OrchardCore.Contents.FileContentDefinition` is enabled) or directly from the SQLite database, and can also pull the latest content items for inspection.
- Accesses all relevant content models for content items and fields, including parts like `BagPart` and `FlowPart` when the task requires them (e.g., implementing a content item display shape).
- Can manage recipes using common recipe steps for sample content items, content definitions, site settings, roles, and users (using commands).

## Installing skills

The skills are agent-agnostic, but each agent has its own discovery locations. Here are concise setups for common agents:

### GitHub Copilot (coding agent, Copilot CLI, VS Code agent mode)

- Place the skill folders into the `.github/skills/` directory of your repository or VS Code workspace. This is the recommended setup.
- Skills placed under `.claude/skills/` are also detected for backward compatibility.
- VS Code support is currently in preview and requires VS Code Insiders.
- Docs: https://docs.github.com/copilot/concepts/agents/about-agent-skills

### OpenAI Codex (CLI and IDE extensions)

- Place the skill folders into one of the following locations inside your repository. Codex checks these in order, from highest to lowest priority:
  ```text
  $CWD/.codex/skills
  $CWD/../.codex/skills
  $REPO_ROOT/.codex/skills
  ```
- To make the skills available across all repositories on your machine, place them into `$CODEX_HOME/skills`. On macOS and Linux this defaults to `~/.codex/skills`.
- Docs: https://developers.openai.com/codex/skills

### Anthropic Claude Code

- To use skills in a single repository or workspace, place the skill folders into `.claude/skills/`.
- To make the skills available globally for all projects, place them into `~/.claude/skills/`.
- Some Claude plugins include and manage their own skills automatically.
- Docs: https://code.claude.com/docs/en/skills

## Maintenance

See the [orchard-core-theming maintenance guide](maintenance/orchard-core-theming.md) for the step-by-step update workflow.

## Contributing

Bug reports, feature requests, comments, questions, code contributions and love letters are warmly welcome. You can send them to us via GitHub issues and pull requests. Please adhere to our [open-source guidelines](https://lombiq.com/open-source-guidelines) while doing so.

This project is developed by [Lombiq Technologies](https://lombiq.com/). Commercial-grade support is available through Lombiq.
