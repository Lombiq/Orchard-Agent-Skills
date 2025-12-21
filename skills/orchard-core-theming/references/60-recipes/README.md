# Recipes Overview

Recipes are JSON documents used to initialize or migrate Orchard Core tenants.
They can enable features, set themes, create definitions, import content, and more.

Related files:
- Steps catalog: `RECIPE-STEPS.md`
- Content import patterns: `RECIPE-CONTENT.md`
- Command step examples: `RECIPE-COMMANDS.md`

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

## Related docs
- Steps and schemas: `RECIPE-STEPS.md`
- Content import patterns: `RECIPE-CONTENT.md`
- Command step: `RECIPE-COMMANDS.md`
- Ready-to-copy examples: `RECIPE-EXAMPLES.md`
- Feature IDs (enable/disable): `FEATURE-CATALOG.md`
- Base setup recipes to reuse: `BASE-RECIPES.md`
