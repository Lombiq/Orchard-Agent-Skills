# Recipes Overview

Purpose: Use to author, validate, and reuse recipes for setup, definitions, and content import.

Recipes are JSON documents used to initialize or migrate Orchard Core tenants.
They can enable features, set themes, create definitions, import content, and more.

Related files:
- `RECIPE-STEPS.md` - step catalog.
- `RECIPE-STEPS-CORE.md` - features, themes, settings.
- `RECIPE-STEPS-DEFINITIONS.md` - types, parts, fields.
- `RECIPE-STEPS-CONTENT-MEDIA.md` - content and media steps.
- `RECIPE-STEPS-SEARCH.md` - search steps.
- `RECIPE-STEPS-SECURITY.md` - security steps.
- `RECIPE-STEPS-MISC.md` - misc steps.
- `RECIPE-STEPS-TEMPLATES-WORKFLOWS.md` - templates and workflows.
- `RECIPE-CONTENT.md` - content import patterns.
- `RECIPE-COMMANDS.md` - command step examples.
- `RECIPE-EXAMPLES.md` - ready-to-copy examples.
- `RECIPE-EXAMPLES-SETUP.md` - setup recipe examples.
- `RECIPE-EXAMPLES-CONTENT.md` - content recipe examples.
- `FEATURE-CATALOG.md` - feature IDs (full list: `FEATURE-CATALOG-ALL.md`).
- `BASE-RECIPES.md` - base setup recipes.

## Where recipes live
- `*/Recipes/*.recipe.json`: reusable recipes in modules/themes.
- `*/Migrations/*.recipe.json`: recipes used by data migrations.
- `HostProject/Recipes/`: optional, common location for setup recipes.

## Top-level schema
```json
{
  "name": "My.Recipe.Name",
  "displayName": "My Recipe",
  "description": "What this recipe does",
  "author": "Org",
  "website": "https://example.com",
  "version": "1.0",
  "issetuprecipe": true,
  "tags": [ "setup", "content" ],
  "variables": {
    "homeId": "[js:uuid()]"
  },
  "steps": [
    { "name": "feature", "enable": [ "OrchardCore.Contents" ] }
  ]
}
```

## Recipe helpers (inline values)
- `js`: execute JavaScript expressions.
  - `"[js:uuid()]"`, `"[js:variables('homeId')]"`.
- `file`: load file contents.
  - `"[file:text('Snippets/page.liquid')]"`
- `env`: read environment variables.
  - `"[env:MY_VAR]"`
- `appsettings`: read configuration values.
  - `"[appsettings:OrchardCore:SiteName]"`
- `localization`: read localized strings.
  - `"[localization:WelcomeTitle]"`
- `base64`, `html`, `gzip`: decode content.

## Execution and composition
- Use the `recipes` step to include other recipes by `name`.
- Order matters; definitions and settings should usually come before content.
- Setup recipes (`issetuprecipe: true`) are available during tenant setup and AutoSetup.
